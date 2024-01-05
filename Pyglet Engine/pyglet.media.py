# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.media
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import atexit, ctypes, heapq, sys, threading, time, pyglet
from pyglet.compat import bytes_type, BytesIO
_debug = pyglet.options['debug_media']

class MediaException(Exception):
    pass


class MediaFormatException(MediaException):
    pass


class CannotSeekException(MediaException):
    pass


class MediaThread(object):
    _threads = set()
    _threads_lock = threading.Lock()

    def __init__(self, target=None):
        self._thread = threading.Thread(target=self._thread_run)
        self._thread.setDaemon(True)
        if target is not None:
            self.run = target
        self.condition = threading.Condition()
        self.stopped = False
        return

    @classmethod
    def _atexit(cls):
        cls._threads_lock.acquire()
        threads = list(cls._threads)
        cls._threads_lock.release()
        for thread in threads:
            thread.stop()

    def run(self):
        pass

    def _thread_run(self):
        if pyglet.options['debug_trace']:
            pyglet._install_trace()
        self._threads_lock.acquire()
        self._threads.add(self)
        self._threads_lock.release()
        self.run()
        self._threads_lock.acquire()
        self._threads.remove(self)
        self._threads_lock.release()

    def start(self):
        self._thread.start()

    def stop(self):
        if _debug:
            print 'MediaThread.stop()'
        self.condition.acquire()
        self.stopped = True
        self.condition.notify()
        self.condition.release()
        self._thread.join()

    def sleep(self, timeout):
        if _debug:
            print 'MediaThread.sleep(%r)' % timeout
        self.condition.acquire()
        self.condition.wait(timeout)
        self.condition.release()

    def notify(self):
        if _debug:
            print 'MediaThread.notify()'
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()


atexit.register(MediaThread._atexit)

class WorkerThread(MediaThread):

    def __init__(self, target=None):
        super(WorkerThread, self).__init__(target)
        self._jobs = []

    def run(self):
        while True:
            job = self.get_job()
            if not job:
                break
            job()

    def get_job(self):
        self.condition.acquire()
        while self._empty() and not self.stopped:
            self.condition.wait()

        if self.stopped:
            result = None
        else:
            result = self._get()
        self.condition.release()
        return result

    def put_job(self, job):
        self.condition.acquire()
        self._put(job)
        self.condition.notify()
        self.condition.release()

    def clear_jobs(self):
        self.condition.acquire()
        self._clear()
        self.condition.notify()
        self.condition.release()

    def _empty(self):
        return not self._jobs

    def _get(self):
        return self._jobs.pop(0)

    def _put(self, job):
        self._jobs.append(job)

    def _clear(self):
        del self._jobs[:]


class AudioFormat(object):

    def __init__(self, channels, sample_size, sample_rate):
        self.channels = channels
        self.sample_size = sample_size
        self.sample_rate = sample_rate
        self.bytes_per_sample = (sample_size >> 3) * channels
        self.bytes_per_second = self.bytes_per_sample * sample_rate

    def __eq__(self, other):
        return self.channels == other.channels and self.sample_size == other.sample_size and self.sample_rate == other.sample_rate

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '%s(channels=%d, sample_size=%d, sample_rate=%d)' % (
         self.__class__.__name__, self.channels, self.sample_size,
         self.sample_rate)


class VideoFormat(object):

    def __init__(self, width, height, sample_aspect=1.0):
        self.width = width
        self.height = height
        self.sample_aspect = sample_aspect
        self.frame_rate = None
        return


class AudioData(object):

    def __init__(self, data, length, timestamp, duration, events):
        self.data = data
        self.length = length
        self.timestamp = timestamp
        self.duration = duration
        self.events = events

    def consume(self, bytes, audio_format):
        self.events = ()
        if bytes == self.length:
            self.data = None
            self.length = 0
            self.timestamp += self.duration
            self.duration = 0.0
            return
        else:
            if bytes == 0:
                return
            if not isinstance(self.data, str):
                data = ctypes.create_string_buffer(self.length)
                ctypes.memmove(data, self.data, self.length)
                self.data = data
            self.data = self.data[bytes:]
            self.length -= bytes
            self.duration -= bytes / float(audio_format.bytes_per_second)
            self.timestamp += bytes / float(audio_format.bytes_per_second)
            return

    def get_string_data(self):
        if isinstance(self.data, bytes_type):
            return self.data
        buf = ctypes.create_string_buffer(self.length)
        ctypes.memmove(buf, self.data, self.length)
        return buf.raw


class MediaEvent(object):

    def __init__(self, timestamp, event, *args):
        self.timestamp = timestamp
        self.event = event
        self.args = args

    def _sync_dispatch_to_player(self, player):
        pyglet.app.platform_event_loop.post_event(player, self.event, *self.args)
        time.sleep(0)

    def __repr__(self):
        return '%s(%r, %r, %r)' % (self.__class__.__name__,
         self.timestamp, self.event, self.args)

    def __lt__(self, other):
        return hash(self) < hash(other)


class SourceInfo(object):
    title = ''
    author = ''
    copyright = ''
    comment = ''
    album = ''
    year = 0
    track = 0
    genre = ''


class Source(object):
    _duration = None
    audio_format = None
    video_format = None
    info = None

    def _get_duration(self):
        return self._duration

    duration = property((lambda self: self._get_duration()), doc='The length of the source, in seconds.\n\n        Not all source durations can be determined; in this case the value\n        is None.\n\n        Read-only.\n\n        :type: float\n        ')

    def play(self):
        player = ManagedSoundPlayer()
        player.queue(self)
        player.play()
        return player

    def get_animation(self):
        from pyglet.image import Animation, AnimationFrame
        if not self.video_format:
            return Animation([])
        else:
            frames = []
            last_ts = 0
            next_ts = self.get_next_video_timestamp()
            while next_ts is not None:
                image = self.get_next_video_frame()
                if image is not None:
                    delay = next_ts - last_ts
                    frames.append(AnimationFrame(image, delay))
                    last_ts = next_ts
                next_ts = self.get_next_video_timestamp()

            return Animation(frames)
            return

    def get_next_video_timestamp(self):
        pass

    def get_next_video_frame(self):
        pass

    def seek(self, timestamp):
        raise CannotSeekException()

    def _get_queue_source(self):
        return self

    def get_audio_data(self, bytes):
        return


class StreamingSource(Source):
    _is_queued = False
    is_queued = property((lambda self: self._is_queued), doc='Determine if this source has been queued\n        on a `Player` yet.\n\n        Read-only.\n\n        :type: bool\n        ')

    def _get_queue_source(self):
        if self._is_queued:
            raise MediaException('This source is already queued on a player.')
        self._is_queued = True
        return self


class StaticSource(Source):

    def __init__(self, source):
        source = source._get_queue_source()
        if source.video_format:
            raise NotImplementedError('Static sources not supported for video yet.')
        self.audio_format = source.audio_format
        if not self.audio_format:
            return
        buffer_size = 1048576
        data = BytesIO()
        while True:
            audio_data = source.get_audio_data(buffer_size)
            if not audio_data:
                break
            data.write(audio_data.get_string_data())

        self._data = data.getvalue()
        self._duration = len(self._data) / float(self.audio_format.bytes_per_second)

    def _get_queue_source(self):
        return StaticMemorySource(self._data, self.audio_format)

    def get_audio_data(self, bytes):
        raise RuntimeError('StaticSource cannot be queued.')


class StaticMemorySource(StaticSource):

    def __init__(self, data, audio_format):
        self._file = BytesIO(data)
        self._max_offset = len(data)
        self.audio_format = audio_format
        self._duration = len(data) / float(audio_format.bytes_per_second)

    def seek(self, timestamp):
        offset = int(timestamp * self.audio_format.bytes_per_second)
        if self.audio_format.bytes_per_sample == 2:
            offset &= 4294967294
        elif self.audio_format.bytes_per_sample == 4:
            offset &= 4294967292
        self._file.seek(offset)

    def get_audio_data(self, bytes):
        offset = self._file.tell()
        timestamp = float(offset) / self.audio_format.bytes_per_second
        if self.audio_format.bytes_per_sample == 2:
            bytes &= 4294967294
        elif self.audio_format.bytes_per_sample == 4:
            bytes &= 4294967292
        data = self._file.read(bytes)
        if not len(data):
            return None
        else:
            duration = float(len(data)) / self.audio_format.bytes_per_second
            return AudioData(data, len(data), timestamp, duration, [])


class SourceGroup(object):
    _advance_after_eos = False
    _loop = False

    def __init__(self, audio_format, video_format):
        self.audio_format = audio_format
        self.video_format = video_format
        self.duration = 0.0
        self._timestamp_offset = 0.0
        self._dequeued_durations = []
        self._sources = []

    def seek(self, time):
        if self._sources:
            self._sources[0].seek(time)

    def queue(self, source):
        source = source._get_queue_source()
        self._sources.append(source)
        self.duration += source.duration

    def has_next(self):
        return len(self._sources) > 1

    def next(self, immediate=True):
        if immediate:
            self._advance()
        else:
            self._advance_after_eos = True

    def get_current_source(self):
        if self._sources:
            return self._sources[0]

    def _advance(self):
        if self._sources:
            self._timestamp_offset += self._sources[0].duration
            self._dequeued_durations.insert(0, self._sources[0].duration)
            old_source = self._sources.pop(0)
            self.duration -= old_source.duration

    def _get_loop(self):
        return self._loop

    def _set_loop(self, loop):
        self._loop = loop

    loop = property(_get_loop, _set_loop, doc='Loop the current source indefinitely or until \n    `next` is called.  Initially False.\n\n    :type: bool\n    ')

    def get_audio_data(self, bytes):
        data = self._sources[0].get_audio_data(bytes)
        eos = False
        while not data:
            eos = True
            if self._loop and not self._advance_after_eos:
                self._timestamp_offset += self._sources[0].duration
                self._dequeued_durations.insert(0, self._sources[0].duration)
                self._sources[0].seek(0)
            else:
                self._advance_after_eos = False
                if len(self._sources) > 1:
                    self._advance()
                else:
                    return
            data = self._sources[0].get_audio_data(bytes)

        data.timestamp += self._timestamp_offset
        if eos:
            if _debug:
                print 'adding on_eos event to audio data'
            data.events.append(MediaEvent(0, 'on_eos'))
        return data

    def translate_timestamp(self, timestamp):
        if timestamp is None:
            return
        else:
            timestamp = timestamp - self._timestamp_offset
            if timestamp < 0:
                for duration in self._dequeued_durations[::-1]:
                    timestamp += duration
                    if timestamp > 0:
                        break

            return timestamp

    def get_next_video_timestamp(self):
        timestamp = self._sources[0].get_next_video_timestamp()
        if timestamp is not None:
            timestamp += self._timestamp_offset
        return timestamp

    def get_next_video_frame(self):
        return self._sources[0].get_next_video_frame()


class AbstractAudioPlayer(object):

    def __init__(self, source_group, player):
        self.source_group = source_group
        self.player = player

    def play(self):
        raise NotImplementedError('abstract')

    def stop(self):
        raise NotImplementedError('abstract')

    def delete(self):
        raise NotImplementedError('abstract')

    def _play_group(self, audio_players):
        for player in audio_players:
            player.play()

    def _stop_group(self, audio_players):
        for player in audio_players:
            player.play()

    def clear(self):
        raise NotImplementedError('abstract')

    def get_time(self):
        raise NotImplementedError('abstract')

    def set_volume(self, volume):
        pass

    def set_position(self, position):
        pass

    def set_min_distance(self, min_distance):
        pass

    def set_max_distance(self, max_distance):
        pass

    def set_pitch(self, pitch):
        pass

    def set_cone_orientation(self, cone_orientation):
        pass

    def set_cone_inner_angle(self, cone_inner_angle):
        pass

    def set_cone_outer_angle(self, cone_outer_angle):
        pass

    def set_cone_outer_gain(self, cone_outer_gain):
        pass


class Player(pyglet.event.EventDispatcher):
    _last_video_timestamp = None
    _texture = None
    _volume = 1.0
    _min_distance = 1.0
    _max_distance = 100000000.0
    _position = (0, 0, 0)
    _pitch = 1.0
    _cone_orientation = (0, 0, 1)
    _cone_inner_angle = 360.0
    _cone_outer_angle = 360.0
    _cone_outer_gain = 1.0
    EOS_PAUSE = 'pause'
    EOS_LOOP = 'loop'
    EOS_NEXT = 'next'
    EOS_STOP = 'stop'
    _eos_action = EOS_NEXT

    def __init__(self):
        self._groups = []
        self._audio_player = None
        self._playing = False
        self._paused_time = 0.0
        return

    def queue(self, source):
        if self._groups and source.audio_format == self._groups[-1].audio_format and source.video_format == self._groups[-1].video_format:
            self._groups[-1].queue(source)
        else:
            group = SourceGroup(source.audio_format, source.video_format)
            group.queue(source)
            self._groups.append(group)
            self._set_eos_action(self._eos_action)
        self._set_playing(self._playing)

    def _set_playing(self, playing):
        self._playing = playing
        source = self.source
        if playing and source:
            if not self._audio_player:
                self._create_audio_player()
            self._audio_player.play()
            if source.video_format:
                if not self._texture:
                    self._create_texture()
                if self.source.video_format.frame_rate:
                    period = 1.0 / self.source.video_format.frame_rate
                else:
                    period = 1.0 / 30.0
                pyglet.clock.schedule_interval(self.update_texture, period)
        else:
            if self._audio_player:
                self._audio_player.stop()
            pyglet.clock.unschedule(self.update_texture)

    def play(self):
        self._set_playing(True)

    def pause(self):
        self._set_playing(False)
        if self._audio_player:
            time = self._audio_player.get_time()
            time = self._groups[0].translate_timestamp(time)
            if time is not None:
                self._paused_time = time
            self._audio_player.stop()
        return

    def next(self):
        if not self._groups:
            return
        else:
            group = self._groups[0]
            if group.has_next():
                group.next()
                return
            if self.source.video_format:
                self._texture = None
                pyglet.clock.unschedule(self.update_texture)
            if self._audio_player:
                self._audio_player.delete()
                self._audio_player = None
            del self._groups[0]
            if self._groups:
                self._set_playing(self._playing)
                return
            self._set_playing(False)
            self.dispatch_event('on_player_eos')
            return

    def seek(self, time):
        if _debug:
            print 'Player.seek(%r)' % time
        self._paused_time = time
        self.source.seek(time)
        if self._audio_player:
            self._audio_player.clear()
        if self.source.video_format:
            self._last_video_timestamp = None
            self.update_texture(time=time)
        return

    def _create_audio_player(self):
        group = self._groups[0]
        audio_format = group.audio_format
        if audio_format:
            audio_driver = get_audio_driver()
        else:
            audio_driver = get_silent_audio_driver()
        self._audio_player = audio_driver.create_audio_player(group, self)
        _class = self.__class__

        def _set(name):
            private_name = '_' + name
            value = getattr(self, private_name)
            if value != getattr(_class, private_name):
                getattr(self._audio_player, 'set_' + name)(value)

        _set('volume')
        _set('min_distance')
        _set('max_distance')
        _set('position')
        _set('pitch')
        _set('cone_orientation')
        _set('cone_inner_angle')
        _set('cone_outer_angle')
        _set('cone_outer_gain')

    def _get_source(self):
        if not self._groups:
            return None
        else:
            return self._groups[0].get_current_source()

    source = property(_get_source)
    playing = property((lambda self: self._playing))

    def _get_time(self):
        time = None
        if self._playing and self._audio_player:
            time = self._audio_player.get_time()
            time = self._groups[0].translate_timestamp(time)
        if time is None:
            return self._paused_time
        else:
            return time
            return

    time = property(_get_time)

    def _create_texture(self):
        video_format = self.source.video_format
        self._texture = pyglet.image.Texture.create(video_format.width, video_format.height, rectangle=True)
        self._texture = self._texture.get_transform(flip_y=True)
        self._texture.anchor_y = 0

    def get_texture(self):
        return self._texture

    def seek_next_frame(self):
        time = self._groups[0].get_next_video_timestamp()
        if time is None:
            return
        else:
            self.seek(time)
            return

    def update_texture(self, dt=None, time=None):
        if time is None:
            time = self._audio_player.get_time()
        if time is None:
            return
        else:
            if self._last_video_timestamp is not None and time <= self._last_video_timestamp:
                return
            ts = self._groups[0].get_next_video_timestamp()
            while ts is not None and ts < time:
                self._groups[0].get_next_video_frame()
                ts = self._groups[0].get_next_video_timestamp()

            if ts is None:
                self._last_video_timestamp = None
                return
            image = self._groups[0].get_next_video_frame()
            if image is not None:
                if self._texture is None:
                    self._create_texture()
                self._texture.blit_into(image, 0, 0, 0)
                self._last_video_timestamp = ts
            return

    def _set_eos_action(self, eos_action):
        self._eos_action = eos_action
        for group in self._groups:
            group.loop = eos_action == self.EOS_LOOP
            group.advance_after_eos = eos_action == self.EOS_NEXT

    eos_action = property((lambda self: self._eos_action), _set_eos_action, doc='Set the behaviour of the player when it\n        reaches the end of the current source.\n\n        This must be one of the constants `EOS_NEXT`, `EOS_PAUSE`, `EOS_STOP` or\n        `EOS_LOOP`.\n\n        :deprecated: Use `SourceGroup.loop` and `SourceGroup.advance_after_eos`\n\n        :type: str\n        ')

    def _player_property(name, doc=None):
        private_name = '_' + name
        set_name = 'set_' + name

        def _player_property_set(self, value):
            setattr(self, private_name, value)
            if self._audio_player:
                getattr(self._audio_player, set_name)(value)

        def _player_property_get(self):
            return getattr(self, private_name)

        return property(_player_property_get, _player_property_set, doc=doc)

    volume = _player_property('volume')
    min_distance = _player_property('min_distance')
    max_distance = _player_property('max_distance')
    position = _player_property('position')
    pitch = _player_property('pitch')
    cone_orientation = _player_property('cone_orientation')
    cone_inner_angle = _player_property('cone_inner_angle')
    cone_outer_angle = _player_property('cone_outer_angle')
    cone_outer_gain = _player_property('cone_outer_gain')

    def on_player_eos(self):
        if _debug:
            print 'Player.on_player_eos'

    def on_source_group_eos(self):
        self.next()
        if _debug:
            print 'Player.on_source_group_eos'

    def on_eos(self):
        if _debug:
            print 'Player.on_eos'


Player.register_event_type('on_eos')
Player.register_event_type('on_player_eos')
Player.register_event_type('on_source_group_eos')

class ManagedSoundPlayer(Player):
    pass


class PlayerGroup(object):

    def __init__(self, players):
        self.players = list(players)

    def play(self):
        audio_players = [ p._audio_player for p in self.players if p._audio_player
                        ]
        if audio_players:
            audio_players[0]._play_group(audio_players)
        for player in self.players:
            player.play()

    def pause(self):
        audio_players = [ p._audio_player for p in self.players if p._audio_player
                        ]
        if audio_players:
            audio_players[0]._stop_group(audio_players)
        for player in self.players:
            player.pause()


class AbstractAudioDriver(object):

    def create_audio_player(self, source_group, player):
        raise NotImplementedError('abstract')

    def get_listener(self):
        raise NotImplementedError('abstract')


class AbstractListener(object):
    _volume = 1.0
    _position = (0, 0, 0)
    _forward_orientation = (0, 0, -1)
    _up_orientation = (0, 1, 0)

    def _set_volume(self, volume):
        raise NotImplementedError('abstract')

    volume = property((lambda self: self._volume), (lambda self, volume: self._set_volume(volume)), doc='The master volume for sound playback.\n\n        All sound volumes are multiplied by this master volume before being\n        played.  A value of 0 will silence playback (but still consume\n        resources).  The nominal volume is 1.0.\n        \n        :type: float\n        ')

    def _set_position(self, position):
        raise NotImplementedError('abstract')

    position = property((lambda self: self._position), (lambda self, position: self._set_position(position)), doc='The position of the listener in 3D space.\n\n        The position is given as a tuple of floats (x, y, z).  The unit\n        defaults to meters, but can be modified with the listener\n        properties.\n        \n        :type: 3-tuple of float\n        ')

    def _set_forward_orientation(self, orientation):
        raise NotImplementedError('abstract')

    forward_orientation = property((lambda self: self._forward_orientation), (lambda self, o: self._set_forward_orientation(o)), doc='A vector giving the direction the\n        listener is facing.\n\n        The orientation is given as a tuple of floats (x, y, z), and has\n        no unit.  The forward orientation should be orthagonal to the\n        up orientation.\n        \n        :type: 3-tuple of float\n        ')

    def _set_up_orientation(self, orientation):
        raise NotImplementedError('abstract')

    up_orientation = property((lambda self: self._up_orientation), (lambda self, o: self._set_up_orientation(o)), doc='A vector giving the "up" orientation\n        of the listener.\n\n        The orientation is given as a tuple of floats (x, y, z), and has\n        no unit.  The up orientation should be orthagonal to the\n        forward orientation.\n        \n        :type: 3-tuple of float\n        ')


class _LegacyListener(AbstractListener):

    def _set_volume(self, volume):
        get_audio_driver().get_listener().volume = volume
        self._volume = volume

    def _set_position(self, position):
        get_audio_driver().get_listener().position = position
        self._position = position

    def _set_forward_orientation(self, forward_orientation):
        get_audio_driver().get_listener().forward_orientation = forward_orientation
        self._forward_orientation = forward_orientation

    def _set_up_orientation(self, up_orientation):
        get_audio_driver().get_listener().up_orientation = up_orientation
        self._up_orientation = up_orientation


listener = _LegacyListener()

class AbstractSourceLoader(object):

    def load(self, filename, file):
        raise NotImplementedError('abstract')


class AVbinSourceLoader(AbstractSourceLoader):

    def load(self, filename, file):
        import avbin
        return avbin.AVbinSource(filename, file)


class RIFFSourceLoader(AbstractSourceLoader):

    def load(self, filename, file):
        import riff
        return riff.WaveSource(filename, file)


def load(filename, file=None, streaming=True):
    source = get_source_loader().load(filename, file)
    if not streaming:
        source = StaticSource(source)
    return source


def get_audio_driver():
    global _audio_driver
    if _audio_driver:
        return _audio_driver
    else:
        _audio_driver = None
        for driver_name in pyglet.options['audio']:
            try:
                if driver_name == 'pulse':
                    from drivers import pulse
                    _audio_driver = pulse.create_audio_driver()
                    break
                elif driver_name == 'openal':
                    from drivers import openal
                    _audio_driver = openal.create_audio_driver()
                    break
                elif driver_name == 'directsound':
                    from drivers import directsound
                    _audio_driver = directsound.create_audio_driver()
                    break
                elif driver_name == 'silent':
                    _audio_driver = get_silent_audio_driver()
                    break
            except:
                if _debug:
                    print 'Error importing driver %s' % driver_name

        return _audio_driver


def get_silent_audio_driver():
    global _silent_audio_driver
    if not _silent_audio_driver:
        from drivers import silent
        _silent_audio_driver = silent.create_audio_driver()
    return _silent_audio_driver


_audio_driver = None
_silent_audio_driver = None

def get_source_loader():
    global _source_loader
    if _source_loader:
        return _source_loader
    try:
        import avbin
        _source_loader = AVbinSourceLoader()
    except ImportError:
        _source_loader = RIFFSourceLoader()

    return _source_loader


_source_loader = None
try:
    import avbin
    have_avbin = True
except ImportError:
    have_avbin = False
# okay decompiling out\pyglet.media.pyc
