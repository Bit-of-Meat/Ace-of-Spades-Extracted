# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.defer
from __future__ import division, absolute_import
import traceback, types, warnings
from sys import exc_info
from functools import wraps
from twisted.python.compat import cmp, comparable
from twisted.python import lockfile, failure
from twisted.logger import Logger
from twisted.python.deprecate import warnAboutFunction, deprecated
from twisted.python.versions import Version
log = Logger()

class AlreadyCalledError(Exception):
    pass


class CancelledError(Exception):
    pass


class TimeoutError(Exception):
    pass


def logError(err):
    log.failure(None, err)
    return err


def succeed(result):
    d = Deferred()
    d.callback(result)
    return d


def fail(result=None):
    d = Deferred()
    d.errback(result)
    return d


def execute(callable, *args, **kw):
    try:
        result = callable(*args, **kw)
    except:
        return fail()

    return succeed(result)


def maybeDeferred(f, *args, **kw):
    try:
        result = f(*args, **kw)
    except:
        return fail(failure.Failure(captureVars=Deferred.debug))

    if isinstance(result, Deferred):
        return result
    else:
        if isinstance(result, failure.Failure):
            return fail(result)
        return succeed(result)


def timeout(deferred):
    deferred.errback(failure.Failure(TimeoutError('Callback timed out')))


def passthru(arg):
    return arg


def setDebugging(on):
    Deferred.debug = bool(on)


def getDebugging():
    return Deferred.debug


_NO_RESULT = object()
_CONTINUE = object()

class Deferred():
    called = False
    paused = 0
    _debugInfo = None
    _suppressAlreadyCalled = False
    _runningCallbacks = False
    debug = False
    _chainedTo = None

    def __init__(self, canceller=None):
        self.callbacks = []
        self._canceller = canceller
        if self.debug:
            self._debugInfo = DebugInfo()
            self._debugInfo.creator = traceback.format_stack()[:-1]

    def addCallbacks(self, callback, errback=None, callbackArgs=None, callbackKeywords=None, errbackArgs=None, errbackKeywords=None):
        cbs = (
         (
          callback, callbackArgs, callbackKeywords),
         (
          errback or passthru, errbackArgs, errbackKeywords))
        self.callbacks.append(cbs)
        if self.called:
            self._runCallbacks()
        return self

    def addCallback(self, callback, *args, **kw):
        return self.addCallbacks(callback, callbackArgs=args, callbackKeywords=kw)

    def addErrback(self, errback, *args, **kw):
        return self.addCallbacks(passthru, errback, errbackArgs=args, errbackKeywords=kw)

    def addBoth(self, callback, *args, **kw):
        return self.addCallbacks(callback, callback, callbackArgs=args, errbackArgs=args, callbackKeywords=kw, errbackKeywords=kw)

    def chainDeferred(self, d):
        d._chainedTo = self
        return self.addCallbacks(d.callback, d.errback)

    def callback(self, result):
        self._startRunCallbacks(result)

    def errback(self, fail=None):
        if fail is None:
            fail = failure.Failure(captureVars=self.debug)
        elif not isinstance(fail, failure.Failure):
            fail = failure.Failure(fail)
        self._startRunCallbacks(fail)
        return

    def pause(self):
        self.paused = self.paused + 1

    def unpause(self):
        self.paused = self.paused - 1
        if self.paused:
            return
        if self.called:
            self._runCallbacks()

    def cancel(self):
        if not self.called:
            canceller = self._canceller
            if canceller:
                canceller(self)
            else:
                self._suppressAlreadyCalled = True
            if not self.called:
                self.errback(failure.Failure(CancelledError()))
        elif isinstance(self.result, Deferred):
            self.result.cancel()

    def _startRunCallbacks(self, result):
        if self.called:
            if self._suppressAlreadyCalled:
                self._suppressAlreadyCalled = False
                return
            if self.debug:
                if self._debugInfo is None:
                    self._debugInfo = DebugInfo()
                extra = '\n' + self._debugInfo._getDebugTracebacks()
                raise AlreadyCalledError(extra)
            raise AlreadyCalledError
        if self.debug:
            if self._debugInfo is None:
                self._debugInfo = DebugInfo()
            self._debugInfo.invoker = traceback.format_stack()[:-2]
        self.called = True
        self.result = result
        self._runCallbacks()
        return

    def _continuation(self):
        return (
         (
          _CONTINUE, (self,), None),
         (
          _CONTINUE, (self,), None))

    def _runCallbacks(self):
        if self._runningCallbacks:
            return
        else:
            chain = [
             self]
            while chain:
                current = chain[-1]
                if current.paused:
                    return
                finished = True
                current._chainedTo = None
                while current.callbacks:
                    item = current.callbacks.pop(0)
                    callback, args, kw = item[isinstance(current.result, failure.Failure)]
                    args = args or ()
                    kw = kw or {}
                    if callback is _CONTINUE:
                        chainee = args[0]
                        chainee.result = current.result
                        current.result = None
                        if current._debugInfo is not None:
                            current._debugInfo.failResult = None
                        chainee.paused -= 1
                        chain.append(chainee)
                        finished = False
                        break
                    try:
                        current._runningCallbacks = True
                        try:
                            current.result = callback(current.result, *args, **kw)
                            if current.result is current:
                                warnAboutFunction(callback, 'Callback returned the Deferred it was attached to; this breaks the callback chain and will raise an exception in the future.')
                        finally:
                            current._runningCallbacks = False

                    except:
                        current.result = failure.Failure(captureVars=self.debug)
                    else:
                        if isinstance(current.result, Deferred):
                            resultResult = getattr(current.result, 'result', _NO_RESULT)
                            if resultResult is _NO_RESULT or isinstance(resultResult, Deferred) or current.result.paused:
                                current.pause()
                                current._chainedTo = current.result
                                current.result.callbacks.append(current._continuation())
                                break
                            else:
                                current.result.result = None
                                if current.result._debugInfo is not None:
                                    current.result._debugInfo.failResult = None
                                current.result = resultResult

                if finished:
                    if isinstance(current.result, failure.Failure):
                        current.result.cleanFailure()
                        if current._debugInfo is None:
                            current._debugInfo = DebugInfo()
                        current._debugInfo.failResult = current.result
                    elif current._debugInfo is not None:
                        current._debugInfo.failResult = None
                    chain.pop()

            return

    def __str__(self):
        cname = self.__class__.__name__
        result = getattr(self, 'result', _NO_RESULT)
        myID = id(self)
        if self._chainedTo is not None:
            result = ' waiting on Deferred at 0x%x' % (id(self._chainedTo),)
        elif result is _NO_RESULT:
            result = ''
        else:
            result = ' current result: %r' % (result,)
        return '<%s at 0x%x%s>' % (cname, myID, result)

    __repr__ = __str__


class DebugInfo():
    failResult = None

    def _getDebugTracebacks(self):
        info = ''
        if hasattr(self, 'creator'):
            info += ' C: Deferred was created:\n C:'
            info += ('').join(self.creator).rstrip().replace('\n', '\n C:')
            info += '\n'
        if hasattr(self, 'invoker'):
            info += ' I: First Invoker was:\n I:'
            info += ('').join(self.invoker).rstrip().replace('\n', '\n I:')
            info += '\n'
        return info

    def __del__(self):
        if self.failResult is not None:
            log.critical('Unhandled error in Deferred:', isError=True)
            debugInfo = self._getDebugTracebacks()
            if debugInfo:
                format = '(debug: {debugInfo})'
            else:
                format = None
            log.failure(format, self.failResult, debugInfo=debugInfo)
        return


@comparable
class FirstError(Exception):

    def __init__(self, failure, index):
        Exception.__init__(self, failure, index)
        self.subFailure = failure
        self.index = index

    def __repr__(self):
        return 'FirstError[#%d, %r]' % (self.index, self.subFailure.value)

    def __str__(self):
        return 'FirstError[#%d, %s]' % (self.index, self.subFailure)

    def __cmp__(self, other):
        if isinstance(other, FirstError):
            return cmp((
             self.index, self.subFailure), (
             other.index, other.subFailure))
        return -1


class DeferredList(Deferred):
    fireOnOneCallback = False
    fireOnOneErrback = False

    def __init__(self, deferredList, fireOnOneCallback=False, fireOnOneErrback=False, consumeErrors=False):
        self._deferredList = list(deferredList)
        self.resultList = [None] * len(self._deferredList)
        Deferred.__init__(self)
        if len(self._deferredList) == 0 and not fireOnOneCallback:
            self.callback(self.resultList)
        self.fireOnOneCallback = fireOnOneCallback
        self.fireOnOneErrback = fireOnOneErrback
        self.consumeErrors = consumeErrors
        self.finishedCount = 0
        index = 0
        for deferred in self._deferredList:
            deferred.addCallbacks(self._cbDeferred, self._cbDeferred, callbackArgs=(
             index, SUCCESS), errbackArgs=(
             index, FAILURE))
            index = index + 1

        return

    def _cbDeferred(self, result, index, succeeded):
        self.resultList[index] = (
         succeeded, result)
        self.finishedCount += 1
        if not self.called:
            if succeeded == SUCCESS and self.fireOnOneCallback:
                self.callback((result, index))
            else:
                if succeeded == FAILURE and self.fireOnOneErrback:
                    self.errback(failure.Failure(FirstError(result, index)))
                elif self.finishedCount == len(self.resultList):
                    self.callback(self.resultList)
        if succeeded == FAILURE and self.consumeErrors:
            result = None
        return result

    def cancel(self):
        if not self.called:
            for deferred in self._deferredList:
                try:
                    deferred.cancel()
                except:
                    log.failure('Exception raised from user supplied canceller')


def _parseDListResult(l, fireOnOneErrback=False):
    return [ x[1] for x in l ]


def gatherResults(deferredList, consumeErrors=False):
    d = DeferredList(deferredList, fireOnOneErrback=True, consumeErrors=consumeErrors)
    d.addCallback(_parseDListResult)
    return d


SUCCESS = True
FAILURE = False

class waitForDeferred():

    def __init__(self, d):
        warnings.warn('twisted.internet.defer.waitForDeferred was deprecated in Twisted 15.0.0; please use twisted.internet.defer.inlineCallbacks instead', DeprecationWarning, stacklevel=2)
        if not isinstance(d, Deferred):
            raise TypeError('You must give waitForDeferred a Deferred. You gave it %r.' % (d,))
        self.d = d

    def getResult(self):
        if isinstance(self.result, failure.Failure):
            self.result.raiseException()
        return self.result


def _deferGenerator(g, deferred):
    result = None
    waiting = [
     True,
     None]
    while 1:
        try:
            result = next(g)
        except StopIteration:
            deferred.callback(result)
            return deferred
        except:
            deferred.errback()
            return deferred

        if isinstance(result, Deferred):
            return fail(TypeError('Yield waitForDeferred(d), not d!'))
        if isinstance(result, waitForDeferred):

            def gotResult(r, result=result):
                result.result = r
                if waiting[0]:
                    waiting[0] = False
                    waiting[1] = r
                else:
                    _deferGenerator(g, deferred)

            result.d.addBoth(gotResult)
            if waiting[0]:
                waiting[0] = False
                return deferred
            waiting[0] = True
            waiting[1] = None
            result = None

    return


@deprecated(Version('Twisted', 15, 0, 0), 'twisted.internet.defer.inlineCallbacks')
def deferredGenerator(f):

    @wraps(f)
    def unwindGenerator(*args, **kwargs):
        return _deferGenerator(f(*args, **kwargs), Deferred())

    return unwindGenerator


class _DefGen_Return(BaseException):

    def __init__(self, value):
        self.value = value


def returnValue(val):
    raise _DefGen_Return(val)


def _inlineCallbacks(result, g, deferred):
    waiting = [
     True,
     None]
    while 1:
        try:
            isFailure = isinstance(result, failure.Failure)
            if isFailure:
                result = result.throwExceptionIntoGenerator(g)
            else:
                result = g.send(result)
        except StopIteration as e:
            deferred.callback(getattr(e, 'value', None))
            return deferred
        except _DefGen_Return as e:
            appCodeTrace = exc_info()[2].tb_next
            if isFailure:
                appCodeTrace = appCodeTrace.tb_next
            if appCodeTrace.tb_next.tb_next:
                ultimateTrace = appCodeTrace
                while ultimateTrace.tb_next.tb_next:
                    ultimateTrace = ultimateTrace.tb_next

                filename = ultimateTrace.tb_frame.f_code.co_filename
                lineno = ultimateTrace.tb_lineno
                warnings.warn_explicit('returnValue() in %r causing %r to exit: returnValue should only be invoked by functions decorated with inlineCallbacks' % (
                 ultimateTrace.tb_frame.f_code.co_name,
                 appCodeTrace.tb_frame.f_code.co_name), DeprecationWarning, filename, lineno)
            deferred.callback(e.value)
            return deferred
        except:
            deferred.errback()
            return deferred

        if isinstance(result, Deferred):

            def gotResult(r):
                if waiting[0]:
                    waiting[0] = False
                    waiting[1] = r
                else:
                    _inlineCallbacks(r, g, deferred)

            result.addBoth(gotResult)
            if waiting[0]:
                waiting[0] = False
                return deferred
            result = waiting[1]
            waiting[0] = True
            waiting[1] = None

    return deferred


def inlineCallbacks(f):

    @wraps(f)
    def unwindGenerator(*args, **kwargs):
        try:
            gen = f(*args, **kwargs)
        except _DefGen_Return:
            raise TypeError('inlineCallbacks requires %r to produce a generator; insteadcaught returnValue being used in a non-generator' % (
             f,))

        if not isinstance(gen, types.GeneratorType):
            raise TypeError('inlineCallbacks requires %r to produce a generator; instead got %r' % (
             f, gen))
        return _inlineCallbacks(None, gen, Deferred())

    return unwindGenerator


class _ConcurrencyPrimitive(object):

    def __init__(self):
        self.waiting = []

    def _releaseAndReturn(self, r):
        self.release()
        return r

    def run(*args, **kwargs):
        if len(args) < 2:
            if not args:
                raise TypeError('run() takes at least 2 arguments, none given.')
            raise TypeError('%s.run() takes at least 2 arguments, 1 given' % (
             args[0].__class__.__name__,))
        self, f = args[:2]
        args = args[2:]

        def execute(ignoredResult):
            d = maybeDeferred(f, *args, **kwargs)
            d.addBoth(self._releaseAndReturn)
            return d

        d = self.acquire()
        d.addCallback(execute)
        return d


class DeferredLock(_ConcurrencyPrimitive):
    locked = False

    def _cancelAcquire(self, d):
        self.waiting.remove(d)

    def acquire(self):
        d = Deferred(canceller=self._cancelAcquire)
        if self.locked:
            self.waiting.append(d)
        else:
            self.locked = True
            d.callback(self)
        return d

    def release(self):
        self.locked = False
        if self.waiting:
            self.locked = True
            d = self.waiting.pop(0)
            d.callback(self)


class DeferredSemaphore(_ConcurrencyPrimitive):

    def __init__(self, tokens):
        _ConcurrencyPrimitive.__init__(self)
        if tokens < 1:
            raise ValueError('DeferredSemaphore requires tokens >= 1')
        self.tokens = tokens
        self.limit = tokens

    def _cancelAcquire(self, d):
        self.waiting.remove(d)

    def acquire(self):
        d = Deferred(canceller=self._cancelAcquire)
        if not self.tokens:
            self.waiting.append(d)
        else:
            self.tokens = self.tokens - 1
            d.callback(self)
        return d

    def release(self):
        self.tokens = self.tokens + 1
        if self.waiting:
            self.tokens = self.tokens - 1
            d = self.waiting.pop(0)
            d.callback(self)


class QueueOverflow(Exception):
    pass


class QueueUnderflow(Exception):
    pass


class DeferredQueue(object):

    def __init__(self, size=None, backlog=None):
        self.waiting = []
        self.pending = []
        self.size = size
        self.backlog = backlog

    def _cancelGet(self, d):
        self.waiting.remove(d)

    def put(self, obj):
        if self.waiting:
            self.waiting.pop(0).callback(obj)
        elif self.size is None or len(self.pending) < self.size:
            self.pending.append(obj)
        else:
            raise QueueOverflow()
        return

    def get(self):
        if self.pending:
            return succeed(self.pending.pop(0))
        else:
            if self.backlog is None or len(self.waiting) < self.backlog:
                d = Deferred(canceller=self._cancelGet)
                self.waiting.append(d)
                return d
            raise QueueUnderflow()
            return


class AlreadyTryingToLockError(Exception):
    pass


class DeferredFilesystemLock(lockfile.FilesystemLock):
    _interval = 1
    _tryLockCall = None
    _timeoutCall = None

    def __init__(self, name, scheduler=None):
        lockfile.FilesystemLock.__init__(self, name)
        if scheduler is None:
            from twisted.internet import reactor
            scheduler = reactor
        self._scheduler = scheduler
        return

    def deferUntilLocked(self, timeout=None):
        if self._tryLockCall is not None:
            return fail(AlreadyTryingToLockError("deferUntilLocked isn't safe for concurrent use."))
        else:

            def _cancelLock(reason):
                self._tryLockCall.cancel()
                self._tryLockCall = None
                if self._timeoutCall is not None and self._timeoutCall.active():
                    self._timeoutCall.cancel()
                    self._timeoutCall = None
                if self.lock():
                    d.callback(None)
                else:
                    d.errback(reason)
                return

            d = Deferred((lambda deferred: _cancelLock(CancelledError())))

            def _tryLock():
                if self.lock():
                    if self._timeoutCall is not None:
                        self._timeoutCall.cancel()
                        self._timeoutCall = None
                    self._tryLockCall = None
                    d.callback(None)
                else:
                    if timeout is not None and self._timeoutCall is None:
                        reason = failure.Failure(TimeoutError('Timed out acquiring lock: %s after %fs' % (
                         self.name,
                         timeout)))
                        self._timeoutCall = self._scheduler.callLater(timeout, _cancelLock, reason)
                    self._tryLockCall = self._scheduler.callLater(self._interval, _tryLock)
                return

            _tryLock()
            return d


__all__ = [
 'Deferred', 'DeferredList', 'succeed', 'fail', 'FAILURE', 'SUCCESS', 
 'AlreadyCalledError', 
 'TimeoutError', 'gatherResults', 
 'maybeDeferred', 
 'waitForDeferred', 
 'deferredGenerator', 'inlineCallbacks', 
 'returnValue', 
 'DeferredLock', 
 'DeferredSemaphore', 'DeferredQueue', 
 'DeferredFilesystemLock', 'AlreadyTryingToLockError']
# okay decompiling out\twisted.internet.defer.pyc
