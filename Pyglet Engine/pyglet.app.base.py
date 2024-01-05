# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.app.base
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import sys, threading, Queue
from pyglet import app
from pyglet import clock
from pyglet import event
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

class PlatformEventLoop(object):

    def __init__(self):
        self._event_queue = Queue.Queue()
        self._is_running = threading.Event()
        self._is_running.clear()

    def is_running(self):
        return self._is_running.is_set()

    def post_event(self, dispatcher, event, *args):
        self._event_queue.put((dispatcher, event, args))
        self.notify()

    def dispatch_posted_events(self):
        while True:
            try:
                dispatcher, event, args = self._event_queue.get(False)
            except Queue.Empty:
                break

            dispatcher.dispatch_event(event, *args)

    def notify(self):
        raise NotImplementedError('abstract')

    def start(self):
        pass

    def step(self, timeout=None):
        raise NotImplementedError('abstract')

    def set_timer(self, func, interval):
        raise NotImplementedError('abstract')

    def stop(self):
        pass


class EventLoop(event.EventDispatcher):
    _has_exit_condition = None
    _has_exit = False

    def __init__(self):
        self._has_exit_condition = threading.Condition()
        self.clock = clock.get_default()

    def run(self):
        self.has_exit = False
        self._legacy_setup()
        platform_event_loop = app.platform_event_loop
        platform_event_loop.start()
        self.dispatch_event('on_enter')
        if True:
            self._run_estimated()
        else:
            self._run()
        self.dispatch_event('on_exit')
        platform_event_loop.stop()

    def _run(self):
        platform_event_loop = app.platform_event_loop
        while not self.has_exit:
            timeout = self.idle()
            platform_event_loop.step(timeout)

    def _run_estimated(self):
        platform_event_loop = app.platform_event_loop
        predictor = self._least_squares()
        gradient, offset = predictor.next()
        time = self.clock.time
        while not self.has_exit:
            timeout = self.idle()
            if timeout is None:
                estimate = None
            else:
                estimate = max(gradient * timeout + offset, 0.0)
            if False:
                print 'Gradient = %f, Offset = %f' % (gradient, offset)
                print 'Timeout = %f, Estimate = %f' % (timeout, estimate)
            t = time()
            if not platform_event_loop.step(estimate) and estimate != 0.0 and estimate is not None:
                dt = time() - t
                gradient, offset = predictor.send((dt, estimate))

        return

    @staticmethod
    def _least_squares(gradient=1, offset=0):
        X = 0
        Y = 0
        XX = 0
        XY = 0
        n = 0
        x, y = yield (
         gradient, offset)
        X += x
        Y += y
        XX += x * x
        XY += x * y
        n += 1
        while True:
            x, y = yield (gradient, offset)
            X += x
            Y += y
            XX += x * x
            XY += x * y
            n += 1
            try:
                gradient = (n * XY - X * Y) / (n * XX - X * X)
                offset = (Y - gradient * X) / n
            except ZeroDivisionError:
                pass

    def _legacy_setup(self):
        from pyglet.window import Window
        Window._enable_event_queue = False
        for window in app.windows:
            window.switch_to()
            window.dispatch_pending_events()

    def enter_blocking(self):
        timeout = self.idle()
        app.platform_event_loop.set_timer(self._blocking_timer, timeout)

    def exit_blocking(self):
        app.platform_event_loop.set_timer(None, None)
        return

    def _blocking_timer(self):
        timeout = self.idle()
        app.platform_event_loop.set_timer(self._blocking_timer, timeout)

    def idle(self):
        dt = self.clock.update_time()
        self.clock.call_scheduled_functions(dt)
        sleep_time = self.clock.get_sleep_time(True)
        return sleep_time

    def _get_has_exit(self):
        self._has_exit_condition.acquire()
        result = self._has_exit
        self._has_exit_condition.release()
        return result

    def _set_has_exit(self, value):
        self._has_exit_condition.acquire()
        self._has_exit = value
        self._has_exit_condition.notify()
        self._has_exit_condition.release()

    has_exit = property(_get_has_exit, _set_has_exit, doc='Flag indicating if the event loop will exit in\n    the next iteration.  When set, all waiting threads are interrupted (see\n    `sleep`).\n    \n    Thread-safe since pyglet 1.2.\n\n    :see: `exit`\n    :type: bool\n    ')

    def exit(self):
        self._set_has_exit(True)
        app.platform_event_loop.notify()

    def sleep(self, timeout):
        self._has_exit_condition.acquire()
        self._has_exit_condition.wait(timeout)
        result = self._has_exit
        self._has_exit_condition.release()
        return result

    def on_window_close(self, window):
        if not app.windows:
            self.exit()

    if _is_epydoc:

        def on_window_close(self, window):
            pass

        def on_enter(self):
            pass

        def on_exit(self):
            pass


EventLoop.register_event_type('on_window_close')
EventLoop.register_event_type('on_enter')
EventLoop.register_event_type('on_exit')
# okay decompiling out\pyglet.app.base.pyc
