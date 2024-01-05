# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.epollreactor
from __future__ import division, absolute_import
from select import epoll, EPOLLHUP, EPOLLERR, EPOLLIN, EPOLLOUT
import errno
from zope.interface import implementer
from twisted.internet.interfaces import IReactorFDSet
from twisted.python import log
from twisted.internet import posixbase

@implementer(IReactorFDSet)
class _ContinuousPolling(posixbase._PollLikeMixin, posixbase._DisconnectSelectableMixin):
    _POLL_DISCONNECTED = 1
    _POLL_IN = 2
    _POLL_OUT = 4

    def __init__(self, reactor):
        self._reactor = reactor
        self._loop = None
        self._readers = set()
        self._writers = set()
        return

    def _checkLoop(self):
        if self._readers or self._writers:
            if self._loop is None:
                from twisted.internet.task import LoopingCall, _EPSILON
                self._loop = LoopingCall(self.iterate)
                self._loop.clock = self._reactor
                self._loop.start(_EPSILON, now=False)
        elif self._loop:
            self._loop.stop()
            self._loop = None
        return

    def iterate(self):
        for reader in list(self._readers):
            self._doReadOrWrite(reader, reader, self._POLL_IN)

        for reader in list(self._writers):
            self._doReadOrWrite(reader, reader, self._POLL_OUT)

    def addReader(self, reader):
        self._readers.add(reader)
        self._checkLoop()

    def addWriter(self, writer):
        self._writers.add(writer)
        self._checkLoop()

    def removeReader(self, reader):
        try:
            self._readers.remove(reader)
        except KeyError:
            return

        self._checkLoop()

    def removeWriter(self, writer):
        try:
            self._writers.remove(writer)
        except KeyError:
            return

        self._checkLoop()

    def removeAll(self):
        result = list(self._readers | self._writers)
        self._readers.clear()
        self._writers.clear()
        return result

    def getReaders(self):
        return list(self._readers)

    def getWriters(self):
        return list(self._writers)

    def isReading(self, fd):
        return fd in self._readers

    def isWriting(self, fd):
        return fd in self._writers


@implementer(IReactorFDSet)
class EPollReactor(posixbase.PosixReactorBase, posixbase._PollLikeMixin):
    _POLL_DISCONNECTED = EPOLLHUP | EPOLLERR
    _POLL_IN = EPOLLIN
    _POLL_OUT = EPOLLOUT

    def __init__(self):
        self._poller = epoll(1024)
        self._reads = set()
        self._writes = set()
        self._selectables = {}
        self._continuousPolling = _ContinuousPolling(self)
        posixbase.PosixReactorBase.__init__(self)

    def _add(self, xer, primary, other, selectables, event, antievent):
        fd = xer.fileno()
        if fd not in primary:
            flags = event
            if fd in other:
                flags |= antievent
                self._poller.modify(fd, flags)
            else:
                self._poller.register(fd, flags)
            primary.add(fd)
            selectables[fd] = xer

    def addReader(self, reader):
        try:
            self._add(reader, self._reads, self._writes, self._selectables, EPOLLIN, EPOLLOUT)
        except IOError as e:
            if e.errno == errno.EPERM:
                self._continuousPolling.addReader(reader)
            else:
                raise

    def addWriter(self, writer):
        try:
            self._add(writer, self._writes, self._reads, self._selectables, EPOLLOUT, EPOLLIN)
        except IOError as e:
            if e.errno == errno.EPERM:
                self._continuousPolling.addWriter(writer)
            else:
                raise

    def _remove(self, xer, primary, other, selectables, event, antievent):
        fd = xer.fileno()
        if fd == -1:
            for fd, fdes in selectables.items():
                if xer is fdes:
                    break
            else:
                return

        if fd in primary:
            if fd in other:
                flags = antievent
                self._poller.modify(fd, flags)
            else:
                del selectables[fd]
                self._poller.unregister(fd)
            primary.remove(fd)

    def removeReader(self, reader):
        if self._continuousPolling.isReading(reader):
            self._continuousPolling.removeReader(reader)
            return
        self._remove(reader, self._reads, self._writes, self._selectables, EPOLLIN, EPOLLOUT)

    def removeWriter(self, writer):
        if self._continuousPolling.isWriting(writer):
            self._continuousPolling.removeWriter(writer)
            return
        self._remove(writer, self._writes, self._reads, self._selectables, EPOLLOUT, EPOLLIN)

    def removeAll(self):
        return self._removeAll([ self._selectables[fd] for fd in self._reads ], [ self._selectables[fd] for fd in self._writes ]) + self._continuousPolling.removeAll()

    def getReaders(self):
        return [ self._selectables[fd] for fd in self._reads ] + self._continuousPolling.getReaders()

    def getWriters(self):
        return [ self._selectables[fd] for fd in self._writes ] + self._continuousPolling.getWriters()

    def doPoll(self, timeout):
        if timeout is None:
            timeout = -1
        try:
            l = self._poller.poll(timeout, len(self._selectables))
        except IOError as err:
            if err.errno == errno.EINTR:
                return
            raise

        _drdw = self._doReadOrWrite
        for fd, event in l:
            try:
                selectable = self._selectables[fd]
            except KeyError:
                pass
            else:
                log.callWithLogger(selectable, _drdw, selectable, fd, event)

        return

    doIteration = doPoll


def install():
    p = EPollReactor()
    from twisted.internet.main import installReactor
    installReactor(p)


__all__ = [
 'EPollReactor', 'install']
# okay decompiling out\twisted.internet.epollreactor.pyc
