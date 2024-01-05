# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.threadpool
from __future__ import division, absolute_import
import threading
from twisted._threads import pool as _pool
from twisted.python import log, context
from twisted.python.failure import Failure
WorkerStop = object()

class ThreadPool:
    min = 5
    max = 20
    joined = False
    started = False
    workers = 0
    name = None
    threadFactory = threading.Thread
    currentThread = staticmethod(threading.currentThread)

    def __init__(self, minthreads=5, maxthreads=20, name=None):
        self.min = minthreads
        self.max = maxthreads
        self.name = name
        self.threads = []

        def trackingThreadFactory(*a, **kw):
            thread = self.threadFactory(name=self._generateName(), *a, **kw)
            self.threads.append(thread)
            return thread

        def currentLimit():
            if not self.started:
                return 0
            return self.max

        self._team = _pool(currentLimit, trackingThreadFactory)

    @property
    def workers(self):
        stats = self._team.statistics()
        return stats.idleWorkerCount + stats.busyWorkerCount

    @property
    def working(self):
        return [
         None] * self._team.statistics().busyWorkerCount

    @property
    def waiters(self):
        return [
         None] * self._team.statistics().idleWorkerCount

    @property
    def _queue(self):

        class NotAQueue(object):

            def qsize(q):
                return self._team.statistics().backloggedWorkCount

        return NotAQueue()

    q = _queue

    def start(self):
        self.joined = False
        self.started = True
        self.adjustPoolsize()
        if self._team.statistics().backloggedWorkCount:
            self._team.grow(1)

    def startAWorker(self):
        self._team.grow(1)

    def _generateName(self):
        return 'PoolThread-%s-%s' % (self.name or id(self), self.workers)

    def stopAWorker(self):
        self._team.shrink(1)

    def __setstate__(self, state):
        setattr(self, '__dict__', state)
        ThreadPool.__init__(self, self.min, self.max)

    def __getstate__(self):
        state = {}
        state['min'] = self.min
        state['max'] = self.max
        return state

    def callInThread(self, func, *args, **kw):
        self.callInThreadWithCallback(None, func, *args, **kw)
        return

    def callInThreadWithCallback(self, onResult, func, *args, **kw):
        if self.joined:
            return
        ctx = context.theContextTracker.currentContext().contexts[-1]

        def inContext():
            try:
                result = inContext.theWork()
                ok = True
            except:
                result = Failure()
                ok = False

            inContext.theWork = None
            if inContext.onResult is not None:
                inContext.onResult(ok, result)
                inContext.onResult = None
            elif not ok:
                log.err(result)
            return

        inContext.theWork = lambda : context.call(ctx, func, *args, **kw)
        inContext.onResult = onResult
        self._team.do(inContext)

    def stop(self):
        self.joined = True
        self.started = False
        self._team.quit()
        for thread in self.threads:
            thread.join()

    def adjustPoolsize(self, minthreads=None, maxthreads=None):
        if minthreads is None:
            minthreads = self.min
        if maxthreads is None:
            maxthreads = self.max
        self.min = minthreads
        self.max = maxthreads
        if not self.started:
            return
        else:
            if self.workers > self.max:
                self._team.shrink(self.workers - self.max)
            if self.workers < self.min:
                self._team.grow(self.min - self.workers)
            return

    def dumpStats(self):
        log.msg('waiters: %s' % (self.waiters,))
        log.msg('workers: %s' % (self.working,))
        log.msg('total: %s' % (self.threads,))
# okay decompiling out\twisted.python.threadpool.pyc
