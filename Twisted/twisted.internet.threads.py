# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.threads
from __future__ import division, absolute_import
from twisted.python.compat import _PY3
if not _PY3:
    import Queue
else:
    import queue as Queue
from twisted.python import failure
from twisted.internet import defer

def deferToThreadPool(reactor, threadpool, f, *args, **kwargs):
    d = defer.Deferred()

    def onResult(success, result):
        if success:
            reactor.callFromThread(d.callback, result)
        else:
            reactor.callFromThread(d.errback, result)

    threadpool.callInThreadWithCallback(onResult, f, *args, **kwargs)
    return d


def deferToThread(f, *args, **kwargs):
    from twisted.internet import reactor
    return deferToThreadPool(reactor, reactor.getThreadPool(), f, *args, **kwargs)


def _runMultiple(tupleList):
    for f, args, kwargs in tupleList:
        f(*args, **kwargs)


def callMultipleInThread(tupleList):
    from twisted.internet import reactor
    reactor.callInThread(_runMultiple, tupleList)


def blockingCallFromThread(reactor, f, *a, **kw):
    queue = Queue.Queue()

    def _callFromThread():
        result = defer.maybeDeferred(f, *a, **kw)
        result.addBoth(queue.put)

    reactor.callFromThread(_callFromThread)
    result = queue.get()
    if isinstance(result, failure.Failure):
        result.raiseException()
    return result


__all__ = [
 'deferToThread', 'deferToThreadPool', 'callMultipleInThread',
 'blockingCallFromThread']
# okay decompiling out\twisted.internet.threads.pyc
