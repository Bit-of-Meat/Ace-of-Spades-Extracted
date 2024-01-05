# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.clock
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import time, sys, ctypes, pyglet.lib
if sys.platform in ('win32', 'cygwin'):
    _kernel32 = ctypes.windll.kernel32

    class _ClockBase(object):

        def __init__(self):
            self._timer = _kernel32.CreateWaitableTimerA(ctypes.c_void_p(), True, ctypes.c_void_p())

        def sleep(self, microseconds):
            delay = ctypes.c_longlong(int(-microseconds * 10))
            _kernel32.SetWaitableTimer(self._timer, ctypes.byref(delay), 0, ctypes.c_void_p(), ctypes.c_void_p(), False)
            _kernel32.WaitForSingleObject(self._timer, 4294967295)


    _default_time_function = time.clock
else:
    _c = pyglet.lib.load_library('c', darwin='/usr/lib/libc.dylib')
    _c.usleep.argtypes = [ctypes.c_ulong]

    class _ClockBase(object):

        def sleep(self, microseconds):
            _c.usleep(int(microseconds))


    _default_time_function = time.time

class _ScheduledItem(object):
    __slots__ = [
     'func', 'args', 'kwargs']

    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


class _ScheduledIntervalItem(object):
    __slots__ = [
     'func', 'interval', 'last_ts', 'next_ts', 
     'args', 'kwargs']

    def __init__(self, func, interval, last_ts, next_ts, args, kwargs):
        self.func = func
        self.interval = interval
        self.last_ts = last_ts
        self.next_ts = next_ts
        self.args = args
        self.kwargs = kwargs


def _dummy_schedule_func(*args, **kwargs):
    pass


class Clock(_ClockBase):
    MIN_SLEEP = 0.005
    SLEEP_UNDERSHOOT = MIN_SLEEP - 0.001
    _schedule_items = None
    _schedule_interval_items = None
    _force_sleep = False

    def __init__(self, fps_limit=None, time_function=_default_time_function):
        super(Clock, self).__init__()
        self.time = time_function
        self.next_ts = self.time()
        self.last_ts = None
        self.times = []
        self.set_fps_limit(fps_limit)
        self.cumulative_time = 0
        self._schedule_items = []
        self._schedule_interval_items = []
        return

    def update_time(self):
        ts = self.time()
        if self.last_ts is None:
            delta_t = 0
        else:
            delta_t = ts - self.last_ts
            self.times.insert(0, delta_t)
            if len(self.times) > self.window_size:
                self.cumulative_time -= self.times.pop()
        self.cumulative_time += delta_t
        self.last_ts = ts
        return delta_t

    def call_scheduled_functions(self, dt):
        ts = self.last_ts
        result = False
        for item in list(self._schedule_items):
            result = True
            item.func(dt, *item.args, **item.kwargs)

        need_resort = False
        for item in list(self._schedule_interval_items):
            if item.next_ts > ts:
                break
            result = True
            item.func((ts - item.last_ts), *item.args, **item.kwargs)
            if item.interval:
                item.next_ts = item.last_ts + item.interval
                item.last_ts = ts
                if item.next_ts <= ts:
                    if ts - item.next_ts < 0.05:
                        item.next_ts = ts + item.interval
                    else:
                        item.next_ts = self._get_soft_next_ts(ts, item.interval)
                        item.last_ts = item.next_ts - item.interval
                need_resort = True
            else:
                item.next_ts = None

        self._schedule_interval_items = [ item for item in self._schedule_interval_items if item.next_ts is not None
                                        ]
        if need_resort:
            self._schedule_interval_items.sort(key=(lambda a: a.next_ts))
        return result

    def tick(self, poll=False):
        if poll:
            if self.period_limit:
                self.next_ts = self.next_ts + self.period_limit
        else:
            if self.period_limit:
                self._limit()
            if self._force_sleep:
                self.sleep(0)
        delta_t = self.update_time()
        self.call_scheduled_functions(delta_t)
        return delta_t

    def _limit(self):
        ts = self.time()
        sleeptime = self.get_sleep_time(False)
        while sleeptime - self.SLEEP_UNDERSHOOT > self.MIN_SLEEP:
            self.sleep(1000000 * (sleeptime - self.SLEEP_UNDERSHOOT))
            sleeptime = self.get_sleep_time(False)

        sleeptime = self.next_ts - self.time()
        while sleeptime > 0:
            sleeptime = self.next_ts - self.time()

        if sleeptime < -2 * self.period_limit:
            self.next_ts = ts + 2 * self.period_limit
        else:
            self.next_ts = self.next_ts + self.period_limit

    def get_sleep_time(self, sleep_idle):
        if self._schedule_items or not sleep_idle:
            if not self.period_limit:
                return 0.0
            else:
                wake_time = self.next_ts
                if self._schedule_interval_items:
                    wake_time = min(wake_time, self._schedule_interval_items[0].next_ts)
                return max(wake_time - self.time(), 0.0)

        if self._schedule_interval_items:
            return max(self._schedule_interval_items[0].next_ts - self.time(), 0)
        else:
            return

    def set_fps_limit(self, fps_limit):
        if not fps_limit:
            self.period_limit = None
        else:
            self.period_limit = 1.0 / fps_limit
        self.window_size = fps_limit or 60
        return

    def get_fps_limit(self):
        if self.period_limit:
            return 1.0 / self.period_limit
        else:
            return 0

    def get_fps(self):
        if not self.cumulative_time:
            return 0
        return len(self.times) / self.cumulative_time

    def schedule(self, func, *args, **kwargs):
        item = _ScheduledItem(func, args, kwargs)
        self._schedule_items.append(item)

    def _schedule_item(self, func, last_ts, next_ts, interval, *args, **kwargs):
        item = _ScheduledIntervalItem(func, interval, last_ts, next_ts, args, kwargs)
        for i, other in enumerate(self._schedule_interval_items):
            if other.next_ts is not None and other.next_ts > next_ts:
                self._schedule_interval_items.insert(i, item)
                break
        else:
            self._schedule_interval_items.append(item)

        return

    def schedule_interval(self, func, interval, *args, **kwargs):
        last_ts = self.last_ts or self.next_ts
        ts = self.time()
        if ts - last_ts > 0.2:
            last_ts = ts
        next_ts = last_ts + interval
        self._schedule_item(func, last_ts, next_ts, interval, *args, **kwargs)

    def schedule_interval_soft(self, func, interval, *args, **kwargs):
        last_ts = self.last_ts or self.next_ts
        ts = self.time()
        if ts - last_ts > 0.2:
            last_ts = ts
        next_ts = self._get_soft_next_ts(last_ts, interval)
        last_ts = next_ts - interval
        self._schedule_item(func, last_ts, next_ts, interval, *args, **kwargs)

    def _get_soft_next_ts(self, last_ts, interval):

        def taken(ts, e):
            for item in self._schedule_interval_items:
                if item.next_ts is None:
                    pass
                else:
                    if abs(item.next_ts - ts) <= e:
                        return True
                    if item.next_ts > ts + e:
                        return False

            return False

        next_ts = last_ts + interval
        if not taken(next_ts, interval / 4):
            return next_ts
        dt = interval
        divs = 1
        while True:
            next_ts = last_ts
            for i in range(divs - 1):
                next_ts += dt
                if not taken(next_ts, dt / 4):
                    return next_ts

            dt /= 2
            divs *= 2
            if divs > 16:
                return next_ts

    def schedule_once(self, func, delay, *args, **kwargs):
        last_ts = self.last_ts or self.next_ts
        ts = self.time()
        if ts - last_ts > 0.2:
            last_ts = ts
        next_ts = last_ts + delay
        self._schedule_item(func, last_ts, next_ts, 0, *args, **kwargs)

    def unschedule(self, func):
        for item in self._schedule_items:
            if item.func == func:
                item.func = _dummy_schedule_func

        for item in self._schedule_interval_items:
            if item.func == func:
                item.func = _dummy_schedule_func

        self._schedule_items = [ item for item in self._schedule_items if item.func is not _dummy_schedule_func
                               ]
        self._schedule_interval_items = [ item for item in self._schedule_interval_items if item.func is not _dummy_schedule_func
                                        ]


_default = Clock()

def set_default(default):
    global _default
    _default = default


def get_default():
    return _default


def tick(poll=False):
    return _default.tick(poll)


def get_sleep_time(sleep_idle):
    return _default.get_sleep_time(sleep_idle)


def get_fps():
    return _default.get_fps()


def set_fps_limit(fps_limit):
    _default.set_fps_limit(fps_limit)


def get_fps_limit():
    return _default.get_fps_limit()


def schedule(func, *args, **kwargs):
    _default.schedule(func, *args, **kwargs)


def schedule_interval(func, interval, *args, **kwargs):
    _default.schedule_interval(func, interval, *args, **kwargs)


def schedule_interval_soft(func, interval, *args, **kwargs):
    _default.schedule_interval_soft(func, interval, *args, **kwargs)


def schedule_once(func, delay, *args, **kwargs):
    _default.schedule_once(func, delay, *args, **kwargs)


def unschedule(func):
    _default.unschedule(func)


class ClockDisplay(object):

    def __init__(self, font=None, interval=0.25, format='%(fps).2f', color=(0.5, 0.5, 0.5, 0.5), clock=None):
        if clock is None:
            clock = _default
        self.clock = clock
        self.clock.schedule_interval(self.update_text, interval)
        if not font:
            from pyglet.font import load as load_font
            font = load_font('', 36, bold=True)
        import pyglet.font
        self.label = pyglet.font.Text(font, '', color=color, x=10, y=10)
        self.format = format
        return

    def unschedule(self):
        self.clock.unschedule(self.update_text)

    def update_text(self, dt=0):
        fps = self.clock.get_fps()
        self.label.text = self.format % {'fps': fps}

    def draw(self):
        self.label.draw()


def test_clock():
    import getopt
    test_seconds = 1
    test_fps = 60
    show_fps = False
    options, args = getopt.getopt(sys.argv[1:], 'vht:f:', [
     'time=', 'fps=', 'help'])
    for key, value in options:
        if key in ('-t', '--time'):
            test_seconds = float(value)
        elif key in ('-f', '--fps'):
            test_fps = float(value)
        elif key in '-v':
            show_fps = True
        elif key in ('-h', '--help'):
            print 'Usage: clock.py <options>\n\nOptions:\n  -t   --time       Number of seconds to run for.\n  -f   --fps        Target FPS.\n\nTests the clock module by measuring how close we can\nget to the desired FPS by sleeping and busy-waiting.'
            sys.exit(0)

    set_fps_limit(test_fps)
    start = time.time()
    n_frames = int(test_seconds * test_fps + 1)
    print 'Testing %f FPS for %f seconds...' % (test_fps, test_seconds)
    for i in xrange(n_frames):
        tick()
        if show_fps:
            print get_fps()

    total_time = time.time() - start
    total_error = total_time - test_seconds
    print 'Total clock error: %f secs' % total_error
    print 'Total clock error / secs: %f secs/secs' % (total_error / test_seconds)
    print 'Average FPS: %f' % ((n_frames - 1) / total_time)


if __name__ == '__main__':
    test_clock()
# okay decompiling out\pyglet.clock.pyc
