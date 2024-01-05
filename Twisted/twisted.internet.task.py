# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.task
from __future__ import division, absolute_import
__metaclass__ = type
import sys, time
from zope.interface import implementer
from twisted.python import log
from twisted.python import reflect
from twisted.python.failure import Failure
from twisted.internet import base, defer
from twisted.internet.interfaces import IReactorTime
from twisted.internet.error import ReactorNotRunning

class LoopingCall:
    call = None
    running = False
    deferred = None
    interval = None
    _runAtStart = False
    starttime = None

    def __init__(self, f, *a, **kw):
        self.f = f
        self.a = a
        self.kw = kw
        from twisted.internet import reactor
        self.clock = reactor

    def withCount(cls, countCallable):

        def counter():
            now = self.clock.seconds()
            lastTime = self._realLastTime
            if lastTime is None:
                lastTime = self.starttime
                if self._runAtStart:
                    lastTime -= self.interval
            lastInterval = self._intervalOf(lastTime)
            thisInterval = self._intervalOf(now)
            count = thisInterval - lastInterval
            if count > 0:
                self._realLastTime = now
                return countCallable(count)
            else:
                return

        self = cls(counter)
        self._realLastTime = None
        return self

    withCount = classmethod(withCount)

    def _intervalOf(self, t):
        elapsedTime = t - self.starttime
        intervalNum = int(elapsedTime / self.interval)
        return intervalNum

    def start(self, interval, now=True):
        if interval < 0:
            raise ValueError('interval must be >= 0')
        self.running = True
        d = self.deferred = defer.Deferred()
        self.starttime = self.clock.seconds()
        self.interval = interval
        self._runAtStart = now
        if now:
            self()
        else:
            self._scheduleFrom(self.starttime)
        return d

    def stop(self):
        self.running = False
        if self.call is not None:
            self.call.cancel()
            self.call = None
            d, self.deferred = self.deferred, None
            d.callback(self)
        return

    def reset(self):
        if self.call is not None:
            self.call.cancel()
            self.call = None
            self.starttime = self.clock.seconds()
            self._scheduleFrom(self.starttime)
        return

    def __call__(self):

        def cb(result):
            if self.running:
                self._scheduleFrom(self.clock.seconds())
            else:
                d, self.deferred = self.deferred, None
                d.callback(self)
            return

        def eb(failure):
            self.running = False
            d, self.deferred = self.deferred, None
            d.errback(failure)
            return

        self.call = None
        d = defer.maybeDeferred(self.f, *self.a, **self.kw)
        d.addCallback(cb)
        d.addErrback(eb)
        return

    def _scheduleFrom(self, when):

        def howLong():
            if self.interval == 0:
                return 0
            runningFor = when - self.starttime
            untilNextInterval = self.interval - runningFor % self.interval
            if when == when + untilNextInterval:
                return self.interval
            return untilNextInterval

        self.call = self.clock.callLater(howLong(), self)

    def __repr__(self):
        if hasattr(self.f, '__qualname__'):
            func = self.f.__qualname__
        elif hasattr(self.f, '__name__'):
            func = self.f.__name__
            if hasattr(self.f, 'im_class'):
                func = self.f.im_class.__name__ + '.' + func
        else:
            func = reflect.safe_repr(self.f)
        return 'LoopingCall<%r>(%s, *%s, **%s)' % (
         self.interval, func, reflect.safe_repr(self.a),
         reflect.safe_repr(self.kw))


class SchedulerError(Exception):
    pass


class SchedulerStopped(SchedulerError):
    pass


class TaskFinished(SchedulerError):
    pass


class TaskDone(TaskFinished):
    pass


class TaskStopped(TaskFinished):
    pass


class TaskFailed(TaskFinished):
    pass


class NotPaused(SchedulerError):
    pass


class _Timer(object):
    MAX_SLICE = 0.01

    def __init__(self):
        self.end = time.time() + self.MAX_SLICE

    def __call__(self):
        return time.time() >= self.end


_EPSILON = 1e-08

def _defaultScheduler(x):
    from twisted.internet import reactor
    return reactor.callLater(_EPSILON, x)


class CooperativeTask(object):

    def __init__(self, iterator, cooperator):
        self._iterator = iterator
        self._cooperator = cooperator
        self._deferreds = []
        self._pauseCount = 0
        self._completionState = None
        self._completionResult = None
        cooperator._addTask(self)
        return

    def whenDone(self):
        d = defer.Deferred()
        if self._completionState is None:
            self._deferreds.append(d)
        else:
            d.callback(self._completionResult)
        return d

    def pause(self):
        self._checkFinish()
        self._pauseCount += 1
        if self._pauseCount == 1:
            self._cooperator._removeTask(self)

    def resume(self):
        if self._pauseCount == 0:
            raise NotPaused()
        self._pauseCount -= 1
        if self._pauseCount == 0 and self._completionState is None:
            self._cooperator._addTask(self)
        return

    def _completeWith(self, completionState, deferredResult):
        self._completionState = completionState
        self._completionResult = deferredResult
        if not self._pauseCount:
            self._cooperator._removeTask(self)
        for d in self._deferreds:
            d.callback(deferredResult)

    def stop(self):
        self._checkFinish()
        self._completeWith(TaskStopped(), Failure(TaskStopped()))

    def _checkFinish(self):
        if self._completionState is not None:
            raise self._completionState
        return

    def _oneWorkUnit(self):
        try:
            result = next(self._iterator)
        except StopIteration:
            self._completeWith(TaskDone(), self._iterator)
        except:
            self._completeWith(TaskFailed(), Failure())

        if isinstance(result, defer.Deferred):
            self.pause()

            def failLater(f):
                self._completeWith(TaskFailed(), f)

            result.addCallbacks((lambda result: self.resume()), failLater)


class Cooperator(object):

    def __init__(self, terminationPredicateFactory=_Timer, scheduler=_defaultScheduler, started=True):
        self._tasks = []
        self._metarator = iter(())
        self._terminationPredicateFactory = terminationPredicateFactory
        self._scheduler = scheduler
        self._delayedCall = None
        self._stopped = False
        self._started = started
        return

    def coiterate(self, iterator, doneDeferred=None):
        if doneDeferred is None:
            doneDeferred = defer.Deferred()
        CooperativeTask(iterator, self).whenDone().chainDeferred(doneDeferred)
        return doneDeferred

    def cooperate(self, iterator):
        return CooperativeTask(iterator, self)

    def _addTask(self, task):
        if self._stopped:
            self._tasks.append(task)
            task._completeWith(SchedulerStopped(), Failure(SchedulerStopped()))
        else:
            self._tasks.append(task)
            self._reschedule()

    def _removeTask(self, task):
        self._tasks.remove(task)
        if not self._tasks and self._delayedCall:
            self._delayedCall.cancel()
            self._delayedCall = None
        return

    def _tasksWhileNotStopped(self):
        terminator = self._terminationPredicateFactory()
        while self._tasks:
            for t in self._metarator:
                yield t
                if terminator():
                    return

            self._metarator = iter(self._tasks)

    def _tick(self):
        self._delayedCall = None
        for taskObj in self._tasksWhileNotStopped():
            taskObj._oneWorkUnit()

        self._reschedule()
        return

    _mustScheduleOnStart = False

    def _reschedule(self):
        if not self._started:
            self._mustScheduleOnStart = True
            return
        else:
            if self._delayedCall is None and self._tasks:
                self._delayedCall = self._scheduler(self._tick)
            return

    def start(self):
        self._stopped = False
        self._started = True
        if self._mustScheduleOnStart:
            del self._mustScheduleOnStart
            self._reschedule()

    def stop(self):
        self._stopped = True
        for taskObj in self._tasks:
            taskObj._completeWith(SchedulerStopped(), Failure(SchedulerStopped()))

        self._tasks = []
        if self._delayedCall is not None:
            self._delayedCall.cancel()
            self._delayedCall = None
        return

    @property
    def running(self):
        return self._started and not self._stopped


_theCooperator = Cooperator()

def coiterate(iterator):
    return _theCooperator.coiterate(iterator)


def cooperate(iterator):
    return _theCooperator.cooperate(iterator)


@implementer(IReactorTime)
class Clock:
    rightNow = 0.0

    def __init__(self):
        self.calls = []

    def seconds(self):
        return self.rightNow

    def _sortCalls(self):
        self.calls.sort(key=(lambda a: a.getTime()))

    def callLater(self, when, what, *a, **kw):
        dc = base.DelayedCall(self.seconds() + when, what, a, kw, self.calls.remove, (lambda c: None), self.seconds)
        self.calls.append(dc)
        self._sortCalls()
        return dc

    def getDelayedCalls(self):
        return self.calls

    def advance(self, amount):
        self.rightNow += amount
        self._sortCalls()
        while self.calls and self.calls[0].getTime() <= self.seconds():
            call = self.calls.pop(0)
            call.called = 1
            call.func(*call.args, **call.kw)
            self._sortCalls()

    def pump(self, timings):
        for amount in timings:
            self.advance(amount)


def deferLater(clock, delay, callable, *args, **kw):

    def deferLaterCancel(deferred):
        delayedCall.cancel()

    d = defer.Deferred(deferLaterCancel)
    d.addCallback((lambda ignored: callable(*args, **kw)))
    delayedCall = clock.callLater(delay, d.callback, None)
    return d


def react(main, argv=(), _reactor=None):
    if _reactor is None:
        from twisted.internet import reactor as _reactor
    finished = main(_reactor, *argv)
    codes = [0]
    stopping = []
    _reactor.addSystemEventTrigger('before', 'shutdown', stopping.append, True)

    def stop(result, stopReactor):
        if stopReactor:
            try:
                _reactor.stop()
            except ReactorNotRunning:
                pass

        if isinstance(result, Failure):
            if result.check(SystemExit) is not None:
                code = result.value.code
            else:
                log.err(result, 'main function encountered error')
                code = 1
            codes[0] = code
        return

    def cbFinish(result):
        if stopping:
            stop(result, False)
        else:
            _reactor.callWhenRunning(stop, result, True)

    finished.addBoth(cbFinish)
    _reactor.run()
    sys.exit(codes[0])
    return


__all__ = [
 'LoopingCall', 
 'Clock', 
 'SchedulerStopped', 'Cooperator', 'coiterate', 
 'deferLater', 
 'react']
# okay decompiling out\twisted.internet.task.pyc
