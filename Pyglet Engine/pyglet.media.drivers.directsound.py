# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.media.drivers.directsound
import ctypes, math, sys, threading, time, lib_dsound as lib
from pyglet.media import MediaException, MediaThread, AbstractAudioDriver, AbstractAudioPlayer, MediaEvent
from pyglet.window.win32 import _user32, _kernel32
import pyglet
_debug = pyglet.options['debug_media']

class DirectSoundException(MediaException):
    pass


def _db(gain):
    if gain <= 0:
        return -10000
    return max(-10000, min(int(1000 * math.log(min(gain, 1))), 0))


class DirectSoundWorker(MediaThread):
    _min_write_size = 9600
    _nap_time = 0.05
    _sleep_time = None

    def __init__(self):
        super(DirectSoundWorker, self).__init__()
        self.players = set()

    def run(self):
        while True:
            if _debug:
                print 'DirectSoundWorker run attempt acquire'
            self.condition.acquire()
            if _debug:
                print 'DirectSoundWorker run acquire'
            if self.stopped:
                self.condition.release()
                break
            sleep_time = -1
            if self.players:
                player = None
                write_size = 0
                for p in self.players:
                    s = p.get_write_size()
                    if s > write_size:
                        player = p
                        write_size = s

                if write_size > self._min_write_size:
                    player.refill(write_size)
                else:
                    sleep_time = self._nap_time
            else:
                sleep_time = self._sleep_time
            self.condition.release()
            if _debug:
                print 'DirectSoundWorker run release'
            if sleep_time != -1:
                self.sleep(sleep_time)

        if _debug:
            print 'DirectSoundWorker exiting'
        return

    def add(self, player):
        if _debug:
            print 'DirectSoundWorker add', player
        self.condition.acquire()
        self.players.add(player)
        self.condition.notify()
        self.condition.release()
        if _debug:
            print 'return DirectSoundWorker add', player

    def remove(self, player):
        if _debug:
            print 'DirectSoundWorker remove', player
        self.condition.acquire()
        try:
            self.players.remove(player)
        except KeyError:
            pass

        self.condition.notify()
        self.condition.release()
        if _debug:
            print 'return DirectSoundWorker remove', player


class DirectSoundAudioPlayer(AbstractAudioPlayer):
    _buffer_size = 44800
    _cone_inner_angle = 360
    _cone_outer_angle = 360

    def __init__(self, source_group, player):
        global driver
        super(DirectSoundAudioPlayer, self).__init__(source_group, player)
        self._lock = threading.RLock()
        self._playing = False
        self._next_audio_data = None
        self._write_cursor = 0
        self._play_cursor = 0
        self._eos_cursor = None
        self._play_cursor_ring = 0
        self._write_cursor_ring = 0
        self._events = []
        self._timestamps = []
        audio_format = source_group.audio_format
        wfx = lib.WAVEFORMATEX()
        wfx.wFormatTag = lib.WAVE_FORMAT_PCM
        wfx.nChannels = audio_format.channels
        wfx.nSamplesPerSec = audio_format.sample_rate
        wfx.wBitsPerSample = audio_format.sample_size
        wfx.nBlockAlign = wfx.wBitsPerSample * wfx.nChannels // 8
        wfx.nAvgBytesPerSec = wfx.nSamplesPerSec * wfx.nBlockAlign
        dsbdesc = lib.DSBUFFERDESC()
        dsbdesc.dwSize = ctypes.sizeof(dsbdesc)
        dsbdesc.dwFlags = lib.DSBCAPS_GLOBALFOCUS | lib.DSBCAPS_GETCURRENTPOSITION2 | lib.DSBCAPS_CTRLFREQUENCY | lib.DSBCAPS_CTRLVOLUME
        if audio_format.channels == 1:
            dsbdesc.dwFlags |= lib.DSBCAPS_CTRL3D
        dsbdesc.dwBufferBytes = self._buffer_size
        dsbdesc.lpwfxFormat = ctypes.pointer(wfx)
        self._buffer = lib.IDirectSoundBuffer()
        driver._dsound.CreateSoundBuffer(dsbdesc, ctypes.byref(self._buffer), None)
        if audio_format.channels == 1:
            self._buffer3d = lib.IDirectSound3DBuffer()
            self._buffer.QueryInterface(lib.IID_IDirectSound3DBuffer, ctypes.byref(self._buffer3d))
        else:
            self._buffer3d = None
        self._buffer.SetCurrentPosition(0)
        self.refill(self._buffer_size)
        return

    def __del__(self):
        try:
            self.delete()
        except:
            pass

    def delete(self):
        if driver and driver.worker:
            driver.worker.remove(self)
        self.lock()
        self._buffer.Stop()
        self._buffer.Release()
        self._buffer = None
        if self._buffer3d:
            self._buffer3d.Release()
            self._buffer3d = None
        self.unlock()
        return

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def play(self):
        if _debug:
            print 'DirectSound play'
        driver.worker.add(self)
        self.lock()
        if not self._playing:
            self._playing = True
            self._buffer.Play(0, 0, lib.DSBPLAY_LOOPING)
        self.unlock()
        if _debug:
            print 'return DirectSound play'

    def stop(self):
        if _debug:
            print 'DirectSound stop'
        driver.worker.remove(self)
        self.lock()
        if self._playing:
            self._playing = False
            self._buffer.Stop()
        self.unlock()
        if _debug:
            print 'return DirectSound stop'

    def clear(self):
        if _debug:
            print 'DirectSound clear'
        self.lock()
        self._buffer.SetCurrentPosition(0)
        self._play_cursor_ring = self._write_cursor_ring = 0
        self._play_cursor = self._write_cursor
        self._eos_cursor = None
        self._next_audio_data = None
        del self._events[:]
        del self._timestamps[:]
        self.unlock()
        return

    def refill(self, write_size):
        self.lock()
        while write_size > 0:
            if _debug:
                print 'refill, write_size =', write_size
            if self._next_audio_data:
                audio_data = self._next_audio_data
                self._next_audio_data = None
            else:
                audio_data = self.source_group.get_audio_data(write_size)
            if audio_data:
                for event in audio_data.events:
                    event_cursor = self._write_cursor + event.timestamp * self.source_group.audio_format.bytes_per_second
                    self._events.append((event_cursor, event))

                ts_cursor = self._write_cursor + audio_data.length
                self._timestamps.append((
                 ts_cursor, audio_data.timestamp + audio_data.duration))
                if _debug:
                    print 'write', audio_data.length
                length = min(write_size, audio_data.length)
                self.write(audio_data, length)
                if audio_data.length:
                    self._next_audio_data = audio_data
                write_size -= length
            else:
                if self._eos_cursor is None:
                    self._eos_cursor = self._write_cursor
                    self._events.append((
                     self._eos_cursor, MediaEvent(0, 'on_eos')))
                    self._events.append((
                     self._eos_cursor, MediaEvent(0, 'on_source_group_eos')))
                    self._events.sort()
                if self._write_cursor > self._eos_cursor + self._buffer_size:
                    self.stop()
                else:
                    self.write(None, write_size)
                write_size = 0

        self.unlock()
        return

    def update_play_cursor(self):
        self.lock()
        play_cursor_ring = lib.DWORD()
        self._buffer.GetCurrentPosition(play_cursor_ring, None)
        if play_cursor_ring.value < self._play_cursor_ring:
            self._play_cursor += self._buffer_size - self._play_cursor_ring
            self._play_cursor_ring = 0
        self._play_cursor += play_cursor_ring.value - self._play_cursor_ring
        self._play_cursor_ring = play_cursor_ring.value
        pending_events = []
        while self._events and self._events[0][0] <= self._play_cursor:
            _, event = self._events.pop(0)
            pending_events.append(event)

        if _debug:
            print 'Dispatching pending events:', pending_events
            print 'Remaining events:', self._events
        while self._timestamps and self._timestamps[0][0] < self._play_cursor:
            del self._timestamps[0]

        self.unlock()
        for event in pending_events:
            event._sync_dispatch_to_player(self.player)

        return

    def get_write_size(self):
        self.update_play_cursor()
        self.lock()
        play_cursor = self._play_cursor
        write_cursor = self._write_cursor
        self.unlock()
        return self._buffer_size - max(write_cursor - play_cursor, 0)

    def write(self, audio_data, length):
        if length == 0:
            return 0
        self.lock()
        p1 = ctypes.c_void_p()
        l1 = lib.DWORD()
        p2 = ctypes.c_void_p()
        l2 = lib.DWORD()
        self._buffer.Lock(self._write_cursor_ring, length, ctypes.byref(p1), l1, ctypes.byref(p2), l2, 0)
        if audio_data:
            ctypes.memmove(p1, audio_data.data, l1.value)
            audio_data.consume(l1.value, self.source_group.audio_format)
            if l2.value:
                ctypes.memmove(p2, audio_data.data, l2.value)
                audio_data.consume(l2.value, self.source_group.audio_format)
        else:
            ctypes.memset(p1, 0, l1.value)
            if l2.value:
                ctypes.memset(p2, 0, l2.value)
        self._buffer.Unlock(p1, l1, p2, l2)
        self._write_cursor += length
        self._write_cursor_ring += length
        self._write_cursor_ring %= self._buffer_size
        self.unlock()

    def get_time(self):
        self.lock()
        if self._timestamps:
            cursor, ts = self._timestamps[0]
            result = ts + (self._play_cursor - cursor) / float(self.source_group.audio_format.bytes_per_second)
        else:
            result = None
        self.unlock()
        return result

    def set_volume(self, volume):
        volume = _db(volume)
        self.lock()
        self._buffer.SetVolume(volume)
        self.unlock()

    def set_position(self, position):
        if self._buffer3d:
            x, y, z = position
            self.lock()
            self._buffer3d.SetPosition(x, y, -z, lib.DS3D_IMMEDIATE)
            self.unlock()

    def set_min_distance(self, min_distance):
        if self._buffer3d:
            self.lock()
            self._buffer3d.SetMinDistance(min_distance, lib.DS3D_IMMEDIATE)
            self.unlock()

    def set_max_distance(self, max_distance):
        if self._buffer3d:
            self.lock()
            self._buffer3d.SetMaxDistance(max_distance, lib.DS3D_IMMEDIATE)
            self.unlock()

    def set_pitch(self, pitch):
        frequency = int(pitch * self.audio_format.sample_rate)
        self.lock()
        self._buffer.SetFrequency(frequency)
        self.unlock()

    def set_cone_orientation(self, cone_orientation):
        if self._buffer3d:
            x, y, z = cone_orientation
            self.lock()
            self._buffer3d.SetConeOrientation(x, y, -z, lib.DS3D_IMMEDIATE)
            self.unlock()

    def set_cone_inner_angle(self, cone_inner_angle):
        if self._buffer3d:
            self._cone_inner_angle = int(cone_inner_angle)
            self._set_cone_angles()

    def set_cone_outer_angle(self, cone_outer_angle):
        if self._buffer3d:
            self._cone_outer_angle = int(cone_outer_angle)
            self._set_cone_angles()

    def _set_cone_angles(self):
        inner = min(self._cone_inner_angle, self._cone_outer_angle)
        outer = max(self._cone_inner_angle, self._cone_outer_angle)
        self.lock()
        self._buffer3d.SetConeAngles(inner, outer, lib.DS3D_IMMEDIATE)
        self.unlock()

    def set_cone_outer_gain(self, cone_outer_gain):
        if self._buffer3d:
            volume = _db(cone_outer_gain)
            self.lock()
            self._buffer3d.SetConeOutsideVolume(volume, lib.DS3D_IMMEDIATE)
            self.unlock()


class DirectSoundDriver(AbstractAudioDriver):

    def __init__(self):
        self._dsound = lib.IDirectSound()
        lib.DirectSoundCreate(None, ctypes.byref(self._dsound), None)
        hwnd = _user32.GetDesktopWindow()
        self._dsound.SetCooperativeLevel(hwnd, lib.DSSCL_NORMAL)
        self._buffer = lib.IDirectSoundBuffer()
        dsbd = lib.DSBUFFERDESC()
        dsbd.dwSize = ctypes.sizeof(dsbd)
        dsbd.dwFlags = lib.DSBCAPS_CTRL3D | lib.DSBCAPS_CTRLVOLUME | lib.DSBCAPS_PRIMARYBUFFER
        self._dsound.CreateSoundBuffer(dsbd, ctypes.byref(self._buffer), None)
        self._listener = lib.IDirectSound3DListener()
        self._buffer.QueryInterface(lib.IID_IDirectSound3DListener, ctypes.byref(self._listener))
        self.worker = DirectSoundWorker()
        self.worker.start()
        return

    def __del__(self):
        try:
            if self._buffer:
                self.delete()
        except:
            pass

    def create_audio_player(self, source_group, player):
        return DirectSoundAudioPlayer(source_group, player)

    def delete(self):
        self.worker.stop()
        self._buffer.Release()
        self._buffer = None
        self._listener.Release()
        self._listener = None
        return

    def _set_volume(self, volume):
        self._volume = volume
        self._buffer.SetVolume(_db(volume))

    def _set_position(self, position):
        self._position = position
        x, y, z = position
        self._listener.SetPosition(x, y, -z, lib.DS3D_IMMEDIATE)

    def _set_forward_orientation(self, orientation):
        self._forward_orientation = orientation
        self._set_orientation()

    def _set_up_orientation(self, orientation):
        self._up_orientation = orientation
        self._set_orientation()

    def _set_orientation(self):
        x, y, z = self._forward_orientation
        ux, uy, uz = self._up_orientation
        self._listener.SetOrientation(x, y, -z, ux, uy, -uz, lib.DS3D_IMMEDIATE)


def create_audio_driver():
    global driver
    driver = DirectSoundDriver()
    return driver


driver = None
# okay decompiling out\pyglet.media.drivers.directsound.pyc
