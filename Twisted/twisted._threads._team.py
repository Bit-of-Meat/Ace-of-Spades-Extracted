# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted._threads._team
from __future__ import absolute_import, division, print_function
from collections import deque
from zope.interface import implementer
from . import IWorker
from ._convenience import Quit

class Statistics(object):

    def __init__(self, idleWorkerCount, busyWorkerCount, backloggedWorkCount):
        self.idleWorkerCount = idleWorkerCount
        self.busyWorkerCount = busyWorkerCount
        self.backloggedWorkCount = backloggedWorkCount


@implementer(IWorker)
class Team(object):

    def __init__(self, coordinator, createWorker, logException):
        self._quit = Quit()
        self._coordinator = coordinator
        self._createWorker = createWorker
        self._logException = logException
        self._idle = set()
        self._busyCount = 0
        self._pending = deque()
        self._shouldQuitCoordinator = False
        self._toShrink = 0

    def statistics(self):
        return Statistics(len(self._idle), self._busyCount, len(self._pending))

    def grow(self, n):
        self._quit.check()

        @self._coordinator.do
        def createOneWorker():
            for x in range(n):
                worker = self._createWorker()
                if worker is None:
                    return
                self._recycleWorker(worker)

            return

    def shrink(self, n=None):
        self._quit.check()
        self._coordinator.do((lambda : self._quitIdlers(n)))

    def _quitIdlers(self, n=None):
        if n is None:
            n = len(self._idle) + self._busyCount
        for x in range(n):
            if self._idle:
                self._idle.pop().quit()
            else:
                self._toShrink += 1

        if self._shouldQuitCoordinator and self._busyCount == 0:
            self._coordinator.quit()
        return

    def do(self, task):
        self._quit.check()
        self._coordinator.do((lambda : self._coordinateThisTask(task)))

    def _coordinateThisTask(self, task):
        worker = self._idle.pop() if self._idle else self._createWorker()
        if worker is None:
            self._pending.append(task)
            return
        else:
            self._busyCount += 1

            @worker.do
            def doWork():
                try:
                    task()
                except:
                    self._logException()

                @self._coordinator.do
                def idleAndPending():
                    self._busyCount -= 1
                    self._recycleWorker(worker)

            return

    def _recycleWorker(self, worker):
        self._idle.add(worker)
        if self._pending:
            self._coordinateThisTask(self._pending.popleft())
        elif self._shouldQuitCoordinator:
            self._quitIdlers()
        elif self._toShrink > 0:
            self._toShrink -= 1
            self._idle.remove(worker)
            worker.quit()

    def quit(self):
        self._quit.set()

        @self._coordinator.do
        def startFinishing():
            self._shouldQuitCoordinator = True
            self._quitIdlers()
# okay decompiling out\twisted._threads._team.pyc
