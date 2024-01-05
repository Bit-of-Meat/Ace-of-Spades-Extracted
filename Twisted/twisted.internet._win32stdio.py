# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._win32stdio
import win32api, os, msvcrt
from zope.interface import implements
from twisted.internet.interfaces import IHalfCloseableProtocol, ITransport, IAddress
from twisted.internet.interfaces import IConsumer, IPushProducer
from twisted.internet import _pollingfile, main
from twisted.python.failure import Failure

class Win32PipeAddress(object):
    implements(IAddress)


class StandardIO(_pollingfile._PollingTimer):
    implements(ITransport, IConsumer, IPushProducer)
    disconnecting = False
    disconnected = False

    def __init__(self, proto, reactor=None):
        if reactor is None:
            from twisted.internet import reactor
        for stdfd in range(0, 1, 2):
            msvcrt.setmode(stdfd, os.O_BINARY)

        _pollingfile._PollingTimer.__init__(self, reactor)
        self.proto = proto
        hstdin = win32api.GetStdHandle(win32api.STD_INPUT_HANDLE)
        hstdout = win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE)
        self.stdin = _pollingfile._PollableReadPipe(hstdin, self.dataReceived, self.readConnectionLost)
        self.stdout = _pollingfile._PollableWritePipe(hstdout, self.writeConnectionLost)
        self._addPollableResource(self.stdin)
        self._addPollableResource(self.stdout)
        self.proto.makeConnection(self)
        return

    def dataReceived(self, data):
        self.proto.dataReceived(data)

    def readConnectionLost(self):
        if IHalfCloseableProtocol.providedBy(self.proto):
            self.proto.readConnectionLost()
        self.checkConnLost()

    def writeConnectionLost(self):
        if IHalfCloseableProtocol.providedBy(self.proto):
            self.proto.writeConnectionLost()
        self.checkConnLost()

    connsLost = 0

    def checkConnLost(self):
        self.connsLost += 1
        if self.connsLost >= 2:
            self.disconnecting = True
            self.disconnected = True
            self.proto.connectionLost(Failure(main.CONNECTION_DONE))

    def write(self, data):
        self.stdout.write(data)

    def writeSequence(self, seq):
        self.stdout.write(('').join(seq))

    def loseConnection(self):
        self.disconnecting = True
        self.stdin.close()
        self.stdout.close()

    def getPeer(self):
        return Win32PipeAddress()

    def getHost(self):
        return Win32PipeAddress()

    def registerProducer(self, producer, streaming):
        return self.stdout.registerProducer(producer, streaming)

    def unregisterProducer(self):
        return self.stdout.unregisterProducer()

    def stopProducing(self):
        self.stdin.stopProducing()

    def pauseProducing(self):
        self.stdin.pauseProducing()

    def resumeProducing(self):
        self.stdin.resumeProducing()
# okay decompiling out\twisted.internet._win32stdio.pyc
