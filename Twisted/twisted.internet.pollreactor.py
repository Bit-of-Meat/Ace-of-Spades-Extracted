# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.pollreactor
from __future__ import division, absolute_import
import errno
from select import error as SelectError, poll
from select import POLLIN, POLLOUT, POLLHUP, POLLERR, POLLNVAL
from zope.interface import implementer
from twisted.python import log
from twisted.internet import posixbase
from twisted.internet.interfaces import IReactorFDSet

@implementer(IReactorFDSet)
class PollReactor(posixbase.PosixReactorBase, posixbase._PollLikeMixin):
    _POLL_DISCONNECTED = POLLHUP | POLLERR | POLLNVAL
    _POLL_IN = POLLIN
    _POLL_OUT = POLLOUT

    def __init__(self):
        self._poller = poll()
        self._selectables = {}
        self._reads = {}
        self._writes = {}
        posixbase.PosixReactorBase.__init__(self)

    def _updateRegistration(self, fd):
        try:
            self._poller.unregister(fd)
        except KeyError:
            pass

        mask = 0
        if fd in self._reads:
            mask = mask | POLLIN
        if fd in self._writes:
            mask = mask | POLLOUT
        if mask != 0:
            self._poller.register(fd, mask)
        elif fd in self._selectables:
            del self._selectables[fd]

    def _dictRemove(self, selectable, mdict):
        try:
            fd = selectable.fileno()
            mdict[fd]
        except:
            for fd, fdes in self._selectables.items():
                if selectable is fdes:
                    break
            else:
                return

        if fd in mdict:
            del mdict[fd]
            self._updateRegistration(fd)

    def addReader(self, reader):
        fd = reader.fileno()
        if fd not in self._reads:
            self._selectables[fd] = reader
            self._reads[fd] = 1
            self._updateRegistration(fd)

    def addWriter(self, writer):
        fd = writer.fileno()
        if fd not in self._writes:
            self._selectables[fd] = writer
            self._writes[fd] = 1
            self._updateRegistration(fd)

    def removeReader(self, reader):
        return self._dictRemove(reader, self._reads)

    def removeWriter(self, writer):
        return self._dictRemove(writer, self._writes)

    def removeAll(self):
        return self._removeAll([ self._selectables[fd] for fd in self._reads ], [ self._selectables[fd] for fd in self._writes ])

    def doPoll(self, timeout):
        if timeout is not None:
            timeout = int(timeout * 1000)
        try:
            l = self._poller.poll(timeout)
        except SelectError as e:
            if e.args[0] == errno.EINTR:
                return
            raise

        _drdw = self._doReadOrWrite
        for fd, event in l:
            try:
                selectable = self._selectables[fd]
            except KeyError:
                continue

            log.callWithLogger(selectable, _drdw, selectable, fd, event)

        return

    doIteration = doPoll

    def getReaders(self):
        return [ self._selectables[fd] for fd in self._reads ]

    def getWriters(self):
        return [ self._selectables[fd] for fd in self._writes ]


def install():
    p = PollReactor()
    from twisted.internet.main import installReactor
    installReactor(p)


__all__ = [
 'PollReactor', 'install']
# okay decompiling out\twisted.internet.pollreactor.pyc
