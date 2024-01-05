# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted._threads._threadworker
from __future__ import absolute_import, division, print_function
from zope.interface import implementer
from ._ithreads import IExclusiveWorker
from ._convenience import Quit
_stop = object()

@implementer(IExclusiveWorker)
class ThreadWorker(object):

    def __init__(self, startThread, queue):
        self._q = queue
        self._hasQuit = Quit()

        def work():
            for task in iter(queue.get, _stop):
                task()

        startThread(work)

    def do(self, task):
        self._hasQuit.check()
        self._q.put(task)

    def quit(self):
        self._hasQuit.set()
        self._q.put(_stop)


@implementer(IExclusiveWorker)
class LockWorker(object):

    def __init__(self, lock, local):
        self._quit = Quit()
        self._lock = lock
        self._local = local

    def do(self, work):
        lock = self._lock
        local = self._local
        self._quit.check()
        working = getattr(local, 'working', None)
        if working is None:
            working = local.working = []
            working.append(work)
            lock.acquire()
            try:
                while working:
                    working.pop(0)()

            finally:
                lock.release()
                local.working = None

        else:
            working.append(work)
        return

    def quit(self):
        self._quit.set()
        self._lock = None
        return
# okay decompiling out\twisted._threads._threadworker.pyc
