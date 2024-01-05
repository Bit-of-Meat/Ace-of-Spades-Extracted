# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.app.carbon
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes
from pyglet import app
from pyglet.app.base import PlatformEventLoop
from ..pyglet.libs.darwin import *
EventLoopTimerProc = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

class CarbonEventLoop(PlatformEventLoop):

    def __init__(self):
        self._event_loop = carbon.GetMainEventLoop()
        self._timer = ctypes.c_void_p()
        self._timer_func = None
        self._timer_func_proc = EventLoopTimerProc(self._timer_proc)
        super(CarbonEventLoop, self).__init__()
        return

    def notify(self):
        carbon.SetEventLoopTimerNextFireTime(self._timer, ctypes.c_double(0.0))

    def start(self):
        timer = self._timer
        carbon.InstallEventLoopTimer(self._event_loop, ctypes.c_double(0.1), ctypes.c_double(kEventDurationForever), self._timer_func_proc, None, ctypes.byref(timer))
        return

    def stop(self):
        carbon.RemoveEventLoopTimer(self._timer)

    def step(self, timeout=None):
        self.dispatch_posted_events()
        event_dispatcher = carbon.GetEventDispatcherTarget()
        e = ctypes.c_void_p()
        if timeout is None:
            timeout = kEventDurationForever
        self._is_running.set()
        if carbon.ReceiveNextEvent(0, None, ctypes.c_double(timeout), True, ctypes.byref(e)) == 0:
            carbon.SendEventToEventTarget(e, event_dispatcher)
            carbon.ReleaseEvent(e)
            timed_out = False
        else:
            timed_out = True
        self._is_running.clear()
        return not timed_out

    def set_timer(self, func, interval):
        if interval is None or func is None:
            interval = kEventDurationForever
        self._timer_func = func
        carbon.SetEventLoopTimerNextFireTime(self._timer, ctypes.c_double(interval))
        return

    def _timer_proc(self, timer, data):
        if self._timer_func:
            self._timer_func()
# okay decompiling out\pyglet.app.carbon.pyc
