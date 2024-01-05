# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.app.win32
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes
from pyglet import app
from base import PlatformEventLoop
from pyglet.libs.win32 import _kernel32, _user32, types, constants
from ..pyglet.libs.win32.constants import *
from ..pyglet.libs.win32.types import *

class Win32EventLoop(PlatformEventLoop):

    def __init__(self):
        super(Win32EventLoop, self).__init__()
        self._next_idle_time = None
        msg = types.MSG()
        _user32.PeekMessageW(ctypes.byref(msg), 0, constants.WM_USER, constants.WM_USER, constants.PM_NOREMOVE)
        self._event_thread = _kernel32.GetCurrentThreadId()
        self._wait_objects = []
        self._recreate_wait_objects_array()
        return

    def add_wait_object(self, object, func):
        self._wait_objects.append((object, func))
        self._recreate_wait_objects_array()

    def remove_wait_object(self, object):
        for i, (_object, _) in enumerate(self._wait_objects):
            if object == _object:
                del self._wait_objects[i]
                break

        self._recreate_wait_objects_array()

    def _recreate_wait_objects_array(self):
        if not self._wait_objects:
            self._wait_objects_n = 0
            self._wait_objects_array = None
            return
        else:
            self._wait_objects_n = len(self._wait_objects)
            self._wait_objects_array = (HANDLE * self._wait_objects_n)(*[ o for o, f in self._wait_objects ])
            return

    def start(self):
        if _kernel32.GetCurrentThreadId() != self._event_thread:
            raise RuntimeError('EventLoop.run() must be called from the same ' + 'thread that imports pyglet.app')
        self._timer_proc = types.TIMERPROC(self._timer_proc_func)
        self._timer = _user32.SetTimer(0, 0, constants.USER_TIMER_MAXIMUM, self._timer_proc)
        self._timer_func = None
        self._polling = False
        self._allow_polling = True
        return

    def step(self, timeout=None):
        self.dispatch_posted_events()
        msg = types.MSG()
        if timeout is None:
            timeout = constants.INFINITE
        else:
            timeout = int(timeout * 1000)
        result = _user32.MsgWaitForMultipleObjects(self._wait_objects_n, self._wait_objects_array, False, timeout, constants.QS_ALLINPUT)
        result -= constants.WAIT_OBJECT_0
        if result == self._wait_objects_n:
            while _user32.PeekMessageW(ctypes.byref(msg), 0, 0, 0, constants.PM_REMOVE):
                _user32.TranslateMessage(ctypes.byref(msg))
                _user32.DispatchMessageW(ctypes.byref(msg))

        elif 0 <= result < self._wait_objects_n:
            object, func = self._wait_objects[result]
            func()
        return result <= self._wait_objects_n

    def notify(self):
        _user32.PostThreadMessageW(self._event_thread, constants.WM_USER, 0, 0)

    def set_timer(self, func, interval):
        if func is None or interval is None:
            interval = constants.USER_TIMER_MAXIMUM
        else:
            interval = int(interval * 1000)
        self._timer_func = func
        _user32.SetTimer(0, self._timer, interval, self._timer_proc)
        return

    def _timer_proc_func(self, hwnd, msg, timer, t):
        if self._timer_func:
            self._timer_func()
# okay decompiling out\pyglet.app.win32.pyc
