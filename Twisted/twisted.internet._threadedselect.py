# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._threadedselect
from threading import Thread
from Queue import Queue, Empty
import sys
from zope.interface import implements
from twisted.internet.interfaces import IReactorFDSet
from twisted.internet import posixbase
from twisted.internet.posixbase import _NO_FILENO, _NO_FILEDESC
from twisted.python import log, failure, threadable
import select
from errno import EINTR, EBADF
from twisted.internet.selectreactor import _select

def dictRemove(dct, value):
    try:
        del dct[value]
    except KeyError:
        pass


def raiseException(e):
    raise e


class ThreadedSelectReactor(posixbase.PosixReactorBase):
    implements(IReactorFDSet)

    def __init__(self):
        threadable.init(1)
        self.reads = {}
        self.writes = {}
        self.toThreadQueue = Queue()
        self.toMainThread = Queue()
        self.workerThread = None
        self.mainWaker = None
        posixbase.PosixReactorBase.__init__(self)
        self.addSystemEventTrigger('after', 'shutdown', self._mainLoopShutdown)
        return

    def wakeUp(self):
        self.waker.wakeUp()

    def callLater(self, *args, **kw):
        tple = posixbase.PosixReactorBase.callLater(self, *args, **kw)
        self.wakeUp()
        return tple

    def _sendToMain(self, msg, *args):
        self.toMainThread.put((msg, args))
        if self.mainWaker is not None:
            self.mainWaker()
        return

    def _sendToThread(self, fn, *args):
        self.toThreadQueue.put((fn, args))

    def _preenDescriptorsInThread(self):
        log.msg('Malformed file descriptor found.  Preening lists.')
        readers = self.reads.keys()
        writers = self.writes.keys()
        self.reads.clear()
        self.writes.clear()
        for selDict, selList in ((self.reads, readers), (self.writes, writers)):
            for selectable in selList:
                try:
                    select.select([selectable], [selectable], [selectable], 0)
                except:
                    log.msg('bad descriptor %s' % selectable)
                else:
                    selDict[selectable] = 1

    def _workerInThread(self):
        try:
            while 1:
                fn, args = self.toThreadQueue.get()
                fn(*args)

        except SystemExit:
            pass
        except:
            f = failure.Failure()
            self._sendToMain('Failure', f)

    def _doSelectInThread(self, timeout):
        reads = self.reads
        writes = self.writes
        while 1:
            try:
                r, w, ignored = _select(reads.keys(), writes.keys(), [], timeout)
                break
            except ValueError:
                log.err()
                self._preenDescriptorsInThread()
            except TypeError:
                log.err()
                self._preenDescriptorsInThread()
            except (select.error, IOError) as se:
                if se.args[0] in (0, 2):
                    if not reads and not writes:
                        return
                    raise
                else:
                    if se.args[0] == EINTR:
                        return
                    if se.args[0] == EBADF:
                        self._preenDescriptorsInThread()
                    else:
                        raise

        self._sendToMain('Notify', r, w)

    def _process_Notify(self, r, w):
        reads = self.reads
        writes = self.writes
        _drdw = self._doReadOrWrite
        _logrun = log.callWithLogger
        for selectables, method, dct in ((r, 'doRead', reads), (w, 'doWrite', writes)):
            for selectable in selectables:
                if selectable not in dct:
                    continue
                _logrun(selectable, _drdw, selectable, method, dct)

    def _process_Failure(self, f):
        f.raiseException()

    _doIterationInThread = _doSelectInThread

    def ensureWorkerThread(self):
        if self.workerThread is None or not self.workerThread.isAlive():
            self.workerThread = Thread(target=self._workerInThread)
            self.workerThread.start()
        return

    def doThreadIteration(self, timeout):
        self._sendToThread(self._doIterationInThread, timeout)
        self.ensureWorkerThread()
        msg, args = self.toMainThread.get()
        getattr(self, '_process_' + msg)(*args)

    doIteration = doThreadIteration

    def _interleave(self):
        while self.running:
            self.runUntilCurrent()
            t2 = self.timeout()
            t = self.running and t2
            self._sendToThread(self._doIterationInThread, t)
            yield
            msg, args = self.toMainThread.get_nowait()
            getattr(self, '_process_' + msg)(*args)

        return

    def interleave(self, waker, *args, **kw):
        self.startRunning(*args, **kw)
        loop = self._interleave()

        def mainWaker(waker=waker, loop=loop):
            waker(loop.next)

        self.mainWaker = mainWaker
        loop.next()
        self.ensureWorkerThread()

    def _mainLoopShutdown(self):
        self.mainWaker = None
        if self.workerThread is not None:
            self._sendToThread(raiseException, SystemExit)
            self.wakeUp()
            try:
                while 1:
                    msg, args = self.toMainThread.get_nowait()

            except Empty:
                pass

            self.workerThread.join()
            self.workerThread = None
        try:
            while 1:
                fn, args = self.toThreadQueue.get_nowait()
                if fn is self._doIterationInThread:
                    log.msg('Iteration is still in the thread queue!')
                elif fn is raiseException and args[0] is SystemExit:
                    pass
                else:
                    fn(*args)

        except Empty:
            pass

        return

    def _doReadOrWrite(self, selectable, method, dict):
        try:
            why = getattr(selectable, method)()
            handfn = getattr(selectable, 'fileno', None)
            if not handfn:
                why = _NO_FILENO
            elif handfn() == -1:
                why = _NO_FILEDESC
        except:
            why = sys.exc_info()[1]
            log.err()

        if why:
            self._disconnectSelectable(selectable, why, method == 'doRead')
        return

    def addReader(self, reader):
        self._sendToThread(self.reads.__setitem__, reader, 1)
        self.wakeUp()

    def addWriter(self, writer):
        self._sendToThread(self.writes.__setitem__, writer, 1)
        self.wakeUp()

    def removeReader(self, reader):
        self._sendToThread(dictRemove, self.reads, reader)

    def removeWriter(self, writer):
        self._sendToThread(dictRemove, self.writes, writer)

    def removeAll(self):
        return self._removeAll(self.reads, self.writes)

    def getReaders(self):
        return self.reads.keys()

    def getWriters(self):
        return self.writes.keys()

    def stop(self):
        posixbase.PosixReactorBase.stop(self)
        self.wakeUp()

    def run(self, installSignalHandlers=1):
        self.startRunning(installSignalHandlers=installSignalHandlers)
        self.mainLoop()

    def mainLoop(self):
        q = Queue()
        self.interleave(q.put)
        while self.running:
            try:
                q.get()()
            except StopIteration:
                break


def install():
    reactor = ThreadedSelectReactor()
    from twisted.internet.main import installReactor
    installReactor(reactor)
    return reactor


__all__ = [
 'install']
# okay decompiling out\twisted.internet._threadedselect.pyc
