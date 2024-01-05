# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.win32eventreactor
import time, sys
from threading import Thread
from weakref import WeakKeyDictionary
from zope.interface import implements
from win32file import FD_READ, FD_CLOSE, FD_ACCEPT, FD_CONNECT, WSAEventSelect
try:
    from win32file import WSAEnumNetworkEvents
except ImportError:
    import warnings
    warnings.warn('Reliable disconnection notification requires pywin32 215 or later', category=UserWarning)

    def WSAEnumNetworkEvents(fd, event):
        return set([FD_READ])


from win32event import CreateEvent, MsgWaitForMultipleObjects
from win32event import WAIT_OBJECT_0, WAIT_TIMEOUT, QS_ALLINPUT
import win32gui
from twisted.internet import posixbase
from twisted.python import log, threadable, failure
from twisted.internet.interfaces import IReactorFDSet
from twisted.internet.interfaces import IReactorWin32Events
from twisted.internet.threads import blockingCallFromThread

class Win32Reactor(posixbase.PosixReactorBase):
    implements(IReactorFDSet, IReactorWin32Events)
    dummyEvent = CreateEvent(None, 0, 0, None)

    def __init__(self):
        self._reads = {}
        self._writes = {}
        self._events = {}
        self._closedAndReading = {}
        self._closedAndNotReading = WeakKeyDictionary()
        posixbase.PosixReactorBase.__init__(self)

    def _makeSocketEvent(self, fd, action, why):
        event = CreateEvent(None, 0, 0, None)
        WSAEventSelect(fd, event, why)
        self._events[event] = (fd, action)
        return event

    def addEvent(self, event, fd, action):
        self._events[event] = (
         fd, action)

    def removeEvent(self, event):
        del self._events[event]

    def addReader(self, reader):
        if reader not in self._reads:
            self._reads[reader] = self._makeSocketEvent(reader, 'doRead', FD_READ | FD_ACCEPT | FD_CONNECT | FD_CLOSE)
            if reader in self._closedAndNotReading:
                self._closedAndReading[reader] = True
                del self._closedAndNotReading[reader]

    def addWriter(self, writer):
        if writer not in self._writes:
            self._writes[writer] = 1

    def removeReader(self, reader):
        if reader in self._reads:
            del self._events[self._reads[reader]]
            del self._reads[reader]
            if reader in self._closedAndReading:
                self._closedAndNotReading[reader] = True
                del self._closedAndReading[reader]

    def removeWriter(self, writer):
        if writer in self._writes:
            del self._writes[writer]

    def removeAll(self):
        return self._removeAll(self._reads, self._writes)

    def getReaders(self):
        return self._reads.keys()

    def getWriters(self):
        return self._writes.keys()

    def doWaitForMultipleEvents(self, timeout):
        log.msg(channel='system', event='iteration', reactor=self)
        if timeout is None:
            timeout = 100
        ranUserCode = False
        for reader in self._closedAndReading.keys():
            ranUserCode = True
            self._runAction('doRead', reader)

        for fd in self._writes.keys():
            ranUserCode = True
            log.callWithLogger(fd, self._runWrite, fd)

        if ranUserCode:
            timeout = 0
        if not (self._events or self._writes):
            time.sleep(timeout)
            return
        else:
            handles = self._events.keys() or [self.dummyEvent]
            timeout = int(timeout * 1000)
            val = MsgWaitForMultipleObjects(handles, 0, timeout, QS_ALLINPUT)
            if val == WAIT_TIMEOUT:
                return
            if val == WAIT_OBJECT_0 + len(handles):
                exit = win32gui.PumpWaitingMessages()
                if exit:
                    self.callLater(0, self.stop)
                    return
            elif val >= WAIT_OBJECT_0 and val < WAIT_OBJECT_0 + len(handles):
                event = handles[val - WAIT_OBJECT_0]
                fd, action = self._events[event]
                if fd in self._reads:
                    fileno = fd.fileno()
                    if fileno == -1:
                        self._disconnectSelectable(fd, posixbase._NO_FILEDESC, False)
                        return
                    events = WSAEnumNetworkEvents(fileno, event)
                    if FD_CLOSE in events:
                        self._closedAndReading[fd] = True
                log.callWithLogger(fd, self._runAction, action, fd)
            return

    def _runWrite(self, fd):
        closed = 0
        try:
            closed = fd.doWrite()
        except:
            closed = sys.exc_info()[1]
            log.deferr()

        if closed:
            self.removeReader(fd)
            self.removeWriter(fd)
            try:
                fd.connectionLost(failure.Failure(closed))
            except:
                log.deferr()

        elif closed is None:
            return 1
        return

    def _runAction(self, action, fd):
        try:
            closed = getattr(fd, action)()
        except:
            closed = sys.exc_info()[1]
            log.deferr()

        if closed:
            self._disconnectSelectable(fd, closed, action == 'doRead')

    doIteration = doWaitForMultipleEvents


class _ThreadFDWrapper(object):

    def __init__(self, reactor, fd, action, logPrefix):
        self._reactor = reactor
        self._fd = fd
        self._action = action
        self._logPrefix = logPrefix

    def logPrefix(self):
        return self._logPrefix

    def _execute(self):
        return blockingCallFromThread(self._reactor, (lambda : getattr(self._fd, self._action)()))

    def connectionLost(self, reason):
        self._reactor.callFromThread(self._fd.connectionLost, reason)


class _ThreadedWin32EventsMixin(object):
    implements(IReactorWin32Events)
    _reactor = None
    _reactorThread = None

    def _unmakeHelperReactor(self):
        self._reactor.callFromThread(self._reactor.stop)
        self._reactor = None
        return

    def _makeHelperReactor(self):
        self._reactor = Win32Reactor()
        self._reactor._registerAsIOThread = False
        self._reactorThread = Thread(target=self._reactor.run, args=(False,))
        self.addSystemEventTrigger('after', 'shutdown', self._unmakeHelperReactor)
        self._reactorThread.start()

    def addEvent(self, event, fd, action):
        if self._reactor is None:
            self._makeHelperReactor()
        self._reactor.callFromThread(self._reactor.addEvent, event, _ThreadFDWrapper(self, fd, action, fd.logPrefix()), '_execute')
        return

    def removeEvent(self, event):
        self._reactor.callFromThread(self._reactor.removeEvent, event)


def install():
    threadable.init(1)
    r = Win32Reactor()
    import main
    main.installReactor(r)


__all__ = [
 'Win32Reactor', 'install']
# okay decompiling out\twisted.internet.win32eventreactor.pyc
