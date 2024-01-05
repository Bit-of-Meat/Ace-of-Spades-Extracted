# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.pygletreactor
import Queue, pyglet
from twisted.python import log, runtime
from twisted.internet import _threadedselect
try:
    from pyglet.app.base import EventLoop
    pyglet_event_loop = pyglet.app.base.EventLoop
except ImportError:
    pyglet_event_loop = pyglet.app.EventLoop

class EventLoop(pyglet_event_loop):

    def __init__(self, twisted_queue=None, call_interval=1 / 10.0):
        pyglet_event_loop.__init__(self)
        if not hasattr(self, 'clock'):
            self.clock = pyglet.clock.get_default()
        if twisted_queue is not None:
            self.register_twisted_queue(twisted_queue, call_interval)
        return

    def register_twisted_queue(self, twisted_queue, call_interval):
        self._twisted_call_queue = twisted_queue
        self.clock.schedule_interval_soft(self._make_twisted_calls, call_interval)

    def _make_twisted_calls(self, dt):
        try:
            f = self._twisted_call_queue.get(False)
            f()
        except Queue.Empty:
            pass


class PygletReactor(_threadedselect.ThreadedSelectReactor):
    _stopping = False

    def registerPygletEventLoop(self, eventloop):
        self.pygletEventLoop = eventloop

    def stop(self):
        if self._stopping:
            return
        self._stopping = True
        _threadedselect.ThreadedSelectReactor.stop(self)

    def _runInMainThread(self, f):
        if hasattr(self, 'pygletEventLoop'):
            self._twistedQueue.put(f)
        else:
            self._postQueue.put(f)

    def _stopPyglet(self):
        if hasattr(self, 'pygletEventLoop'):
            self.pygletEventLoop.exit()

    def run(self, call_interval=1 / 10.0, installSignalHandlers=True):
        self._postQueue = Queue.Queue()
        self._twistedQueue = Queue.Queue()
        if not hasattr(self, 'pygletEventLoop'):
            self.registerPygletEventLoop(EventLoop(self._twistedQueue, call_interval))
        else:
            self.pygletEventLoop.register_twisted_queue(self._twistedQueue, call_interval)
        self.interleave(self._runInMainThread, installSignalHandlers=installSignalHandlers)
        self.addSystemEventTrigger('after', 'shutdown', self._stopPyglet)
        self.addSystemEventTrigger('after', 'shutdown', (lambda : self._postQueue.put(None)))
        self.pygletEventLoop.run()
        del self.pygletEventLoop
        if not self._stopping:
            self.stop()
            while 1:
                try:
                    f = self._postQueue.get(timeout=0.01)
                except Queue.Empty:
                    continue
                else:
                    if f is None:
                        break
                    try:
                        f()
                    except:
                        log.err()

        return


def install():
    reactor = PygletReactor()
    from twisted.internet.main import installReactor
    installReactor(reactor)
    return reactor


__all__ = [
 'install']
# okay decompiling out\aoslib.pygletreactor.pyc
