# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._posixstdio
from zope.interface import implementer
from twisted.internet import process, error, interfaces
from twisted.python import log, failure

@implementer(interfaces.IAddress)
class PipeAddress(object):
    pass


@implementer(interfaces.ITransport, interfaces.IProducer, interfaces.IConsumer, interfaces.IHalfCloseableDescriptor)
class StandardIO(object):
    _reader = None
    _writer = None
    disconnected = False
    disconnecting = False

    def __init__(self, proto, stdin=0, stdout=1, reactor=None):
        if reactor is None:
            from twisted.internet import reactor
        self.protocol = proto
        self._writer = process.ProcessWriter(reactor, self, 'write', stdout)
        self._reader = process.ProcessReader(reactor, self, 'read', stdin)
        self._reader.startReading()
        self.protocol.makeConnection(self)
        return

    def loseWriteConnection(self):
        if self._writer is not None:
            self._writer.loseConnection()
        return

    def write(self, data):
        if self._writer is not None:
            self._writer.write(data)
        return

    def writeSequence(self, data):
        if self._writer is not None:
            self._writer.writeSequence(data)
        return

    def loseConnection(self):
        self.disconnecting = True
        if self._writer is not None:
            self._writer.loseConnection()
        if self._reader is not None:
            self._reader.stopReading()
        return

    def getPeer(self):
        return PipeAddress()

    def getHost(self):
        return PipeAddress()

    def childDataReceived(self, fd, data):
        self.protocol.dataReceived(data)

    def childConnectionLost(self, fd, reason):
        if self.disconnected:
            return
        if reason.value.__class__ == error.ConnectionDone:
            if fd == 'read':
                self._readConnectionLost(reason)
            else:
                self._writeConnectionLost(reason)
        else:
            self.connectionLost(reason)

    def connectionLost(self, reason):
        self.disconnected = True
        _reader = self._reader
        _writer = self._writer
        protocol = self.protocol
        self._reader = self._writer = None
        self.protocol = None
        if _writer is not None and not _writer.disconnected:
            _writer.connectionLost(reason)
        if _reader is not None and not _reader.disconnected:
            _reader.connectionLost(reason)
        try:
            protocol.connectionLost(reason)
        except:
            log.err()

        return

    def _writeConnectionLost(self, reason):
        self._writer = None
        if self.disconnecting:
            self.connectionLost(reason)
            return
        else:
            p = interfaces.IHalfCloseableProtocol(self.protocol, None)
            if p:
                try:
                    p.writeConnectionLost()
                except:
                    log.err()
                    self.connectionLost(failure.Failure())

            return

    def _readConnectionLost(self, reason):
        self._reader = None
        p = interfaces.IHalfCloseableProtocol(self.protocol, None)
        if p:
            try:
                p.readConnectionLost()
            except:
                log.err()
                self.connectionLost(failure.Failure())

        else:
            self.connectionLost(reason)
        return

    def registerProducer(self, producer, streaming):
        if self._writer is None:
            producer.stopProducing()
        else:
            self._writer.registerProducer(producer, streaming)
        return

    def unregisterProducer(self):
        if self._writer is not None:
            self._writer.unregisterProducer()
        return

    def stopProducing(self):
        self.loseConnection()

    def pauseProducing(self):
        if self._reader is not None:
            self._reader.pauseProducing()
        return

    def resumeProducing(self):
        if self._reader is not None:
            self._reader.resumeProducing()
        return

    def stopReading(self):
        self.pauseProducing()

    def startReading(self):
        self.resumeProducing()
# okay decompiling out\twisted.internet._posixstdio.pyc
