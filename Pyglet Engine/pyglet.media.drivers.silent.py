# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.media.drivers.silent
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import time
from pyglet.media import AbstractAudioPlayer, AbstractAudioDriver, MediaThread, MediaEvent
import pyglet
_debug = pyglet.options['debug_media']

class SilentAudioPacket(object):

    def __init__(self, timestamp, duration):
        self.timestamp = timestamp
        self.duration = duration

    def consume(self, dt):
        self.timestamp += dt
        self.duration -= dt


class SilentAudioPlayerPacketConsumer(AbstractAudioPlayer):
    _buffer_time = 0.4
    _min_update_bytes = 1024
    _sleep_time = 0.2

    def __init__(self, source_group, player):
        super(SilentAudioPlayerPacketConsumer, self).__init__(source_group, player)
        self._timestamp_time = None
        self._packets = []
        self._packets_duration = 0
        self._events = []
        self._playing = False
        self._thread = MediaThread(target=self._worker_func)
        if source_group.audio_format:
            self._thread.start()
        return

    def delete(self):
        if _debug:
            print 'SilentAudioPlayer.delete'
        self._thread.stop()

    def play(self):
        if _debug:
            print 'SilentAudioPlayer.play'
        self._thread.condition.acquire()
        if not self._playing:
            self._playing = True
            self._timestamp_time = time.time()
            self._thread.condition.notify()
        self._thread.condition.release()

    def stop(self):
        if _debug:
            print 'SilentAudioPlayer.stop'
        self._thread.condition.acquire()
        if self._playing:
            timestamp = self.get_time()
            if self._packets:
                packet = self._packets[0]
                self._packets_duration -= timestamp - packet.timestamp
                packet.consume(timestamp - packet.timestamp)
            self._playing = False
        self._thread.condition.release()

    def clear(self):
        if _debug:
            print 'SilentAudioPlayer.clear'
        self._thread.condition.acquire()
        del self._packets[:]
        self._packets_duration = 0
        del self._events[:]
        self._thread.condition.release()

    def get_time(self):
        if _debug:
            print 'SilentAudioPlayer.get_time()'
        self._thread.condition.acquire()
        packets = self._packets
        if self._playing:
            result = None
            offset = time.time() - self._timestamp_time
            while packets:
                packet = packets[0]
                if offset > packet.duration:
                    del packets[0]
                    self._timestamp_time += packet.duration
                    offset -= packet.duration
                    self._packets_duration -= packet.duration
                else:
                    packet.consume(offset)
                    self._packets_duration -= offset
                    self._timestamp_time += offset
                    result = packet.timestamp
                    break

        elif packets:
            result = packets[0].timestamp
        else:
            result = None
        self._thread.condition.release()
        if _debug:
            print 'SilentAudioPlayer.get_time() -> ', result
        return result

    def _worker_func(self):
        thread = self._thread
        eos = False
        events = self._events
        while True:
            thread.condition.acquire()
            if thread.stopped or eos and not events:
                thread.condition.release()
                break
            timestamp = self.get_time()
            if _debug:
                print 'timestamp: %r' % timestamp
            while events and events[0].timestamp <= timestamp:
                events[0]._sync_dispatch_to_player(self.player)
                del events[0]

            secs = self._buffer_time - self._packets_duration
            bytes = secs * self.source_group.audio_format.bytes_per_second
            if _debug:
                print 'Trying to buffer %d bytes (%r secs)' % (bytes, secs)
            while bytes > self._min_update_bytes and not eos:
                audio_data = self.source_group.get_audio_data(int(bytes))
                if not audio_data and not eos:
                    events.append(MediaEvent(timestamp, 'on_eos'))
                    events.append(MediaEvent(timestamp, 'on_source_group_eos'))
                    eos = True
                    break
                if self._playing and not self._packets:
                    self._timestamp_time = time.time()
                self._packets.append(SilentAudioPacket(audio_data.timestamp, audio_data.duration))
                self._packets_duration += audio_data.duration
                for event in audio_data.events:
                    event.timestamp += audio_data.timestamp
                    events.append(event)

                events.extend(audio_data.events)
                bytes -= audio_data.length

            sleep_time = self._sleep_time
            if not self._playing:
                sleep_time = None
            elif events and events[0].timestamp and timestamp:
                sleep_time = min(sleep_time, events[0].timestamp - timestamp)
            if _debug:
                print 'SilentAudioPlayer(Worker).sleep', sleep_time
            thread.sleep(sleep_time)
            thread.condition.release()

        return


class SilentTimeAudioPlayer(AbstractAudioPlayer):
    _time = 0.0
    _systime = None

    def play(self):
        self._systime = time.time()

    def stop(self):
        self._time = self.get_time()
        self._systime = None
        return

    def delete(self):
        pass

    def clear(self):
        pass

    def get_time(self):
        if self._systime is None:
            return self._time
        else:
            return time.time() - self._systime + self._time
            return


class SilentAudioDriver(AbstractAudioDriver):

    def create_audio_player(self, source_group, player):
        if source_group.audio_format:
            return SilentAudioPlayerPacketConsumer(source_group, player)
        else:
            return SilentTimeAudioPlayer(source_group, player)


def create_audio_driver():
    return SilentAudioDriver()
# okay decompiling out\pyglet.media.drivers.silent.pyc
