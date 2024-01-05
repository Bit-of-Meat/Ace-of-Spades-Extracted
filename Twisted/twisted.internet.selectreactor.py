# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.selectreactor
from __future__ import division, absolute_import
from time import sleep
import sys, select, socket
from errno import EINTR, EBADF
from zope.interface import implementer
from twisted.internet.interfaces import IReactorFDSet
from twisted.internet import posixbase
from twisted.python import log
from twisted.python.runtime import platformType

def win32select(r, w, e, timeout=None):
    if not (r or w):
        if timeout is None:
            timeout = 0.01
        else:
            timeout = min(timeout, 0.001)
        sleep(timeout)
        return ([], [], [])
    else:
        if timeout is None or timeout > 0.5:
            timeout = 0.5
        r, w, e = select.select(r, w, w, timeout)
        return (r, w + e, [])


if platformType == 'win32':
    _select = win32select
else:
    _select = select.select
try:
    from twisted.internet.win32eventreactor import _ThreadedWin32EventsMixin
except ImportError:
    _extraBase = object
else:
    _extraBase = _ThreadedWin32EventsMixin

@implementer(IReactorFDSet)
class SelectReactor(posixbase.PosixReactorBase, _extraBase):

    def __init__(self):
        self._reads = set()
        self._writes = set()
        posixbase.PosixReactorBase.__init__(self)

    def _preenDescriptors(self):
        log.msg('Malformed file descriptor found.  Preening lists.')
        readers = list(self._reads)
        writers = list(self._writes)
        self._reads.clear()
        self._writes.clear()
        for selSet, selList in ((self._reads, readers),
         (
          self._writes, writers)):
            for selectable in selList:
                try:
                    select.select([selectable], [selectable], [selectable], 0)
                except Exception as e:
                    log.msg('bad descriptor %s' % selectable)
                    self._disconnectSelectable(selectable, e, False)
                else:
                    selSet.add(selectable)

    def doSelect(self, timeout):
        try:
            r, w, ignored = _select(self._reads, self._writes, [], timeout)
        except ValueError:
            self._preenDescriptors()
            return
        except TypeError:
            log.err()
            self._preenDescriptors()
            return
        except (select.error, socket.error, IOError) as se:
            if se.args[0] in (0, 2):
                if not self._reads and not self._writes:
                    return
                raise
            else:
                if se.args[0] == EINTR:
                    return
                if se.args[0] == EBADF:
                    self._preenDescriptors()
                    return
                raise

        _drdw = self._doReadOrWrite
        _logrun = log.callWithLogger
        for selectables, method, fdset in ((r, 'doRead', self._reads),
         (
          w, 'doWrite', self._writes)):
            for selectable in selectables:
                if selectable not in fdset:
                    continue
                _logrun(selectable, _drdw, selectable, method)

    doIteration = doSelect

    def _doReadOrWrite(self, selectable, method):
        try:
            why = getattr(selectable, method)()
        except:
            why = sys.exc_info()[1]
            log.err()

        if why:
            self._disconnectSelectable(selectable, why, method == 'doRead')

    def addReader(self, reader):
        self._reads.add(reader)

    def addWriter(self, writer):
        self._writes.add(writer)

    def removeReader(self, reader):
        self._reads.discard(reader)

    def removeWriter(self, writer):
        self._writes.discard(writer)

    def removeAll(self):
        return self._removeAll(self._reads, self._writes)

    def getReaders(self):
        return list(self._reads)

    def getWriters(self):
        return list(self._writes)


def install():
    reactor = SelectReactor()
    from twisted.internet.main import installReactor
    installReactor(reactor)


__all__ = [
 'install']
# okay decompiling out\twisted.internet.selectreactor.pyc
