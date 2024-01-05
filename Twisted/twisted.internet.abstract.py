# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.abstract
from __future__ import division, absolute_import
from socket import AF_INET6, inet_pton, error
from zope.interface import implementer
from twisted.python.compat import _PY3, unicode, lazyByteSlice
from twisted.python import reflect, failure
from twisted.internet import interfaces, main
if _PY3:

    def _concatenate(bObj, offset, bArray):
        return bObj[offset:] + ('').join(bArray)


else:

    def _concatenate(bObj, offset, bArray):
        return buffer(bObj, offset) + ('').join(bArray)


class _ConsumerMixin(object):
    producer = None
    producerPaused = False
    streamingProducer = False

    def startWriting(self):
        raise NotImplementedError('%r did not implement startWriting')

    def registerProducer(self, producer, streaming):
        if self.producer is not None:
            raise RuntimeError('Cannot register producer %s, because producer %s was never unregistered.' % (
             producer, self.producer))
        if self.disconnected:
            producer.stopProducing()
        else:
            self.producer = producer
            self.streamingProducer = streaming
            if not streaming:
                producer.resumeProducing()
        return

    def unregisterProducer(self):
        self.producer = None
        if self.connected and self.disconnecting:
            self.startWriting()
        return


@implementer(interfaces.ILoggingContext)
class _LogOwner(object):

    def _getLogPrefix(self, applicationObject):
        if interfaces.ILoggingContext.providedBy(applicationObject):
            return applicationObject.logPrefix()
        return applicationObject.__class__.__name__

    def logPrefix(self):
        return '-'


@implementer(interfaces.IPushProducer, interfaces.IReadWriteDescriptor, interfaces.IConsumer, interfaces.ITransport, interfaces.IHalfCloseableDescriptor)
class FileDescriptor(_ConsumerMixin, _LogOwner):
    connected = 0
    disconnected = 0
    disconnecting = 0
    _writeDisconnecting = False
    _writeDisconnected = False
    dataBuffer = ''
    offset = 0
    SEND_LIMIT = 131072

    def __init__(self, reactor=None):
        if not reactor:
            from twisted.internet import reactor
        self.reactor = reactor
        self._tempDataBuffer = []
        self._tempDataLen = 0

    def connectionLost(self, reason):
        self.disconnected = 1
        self.connected = 0
        if self.producer is not None:
            self.producer.stopProducing()
            self.producer = None
        self.stopReading()
        self.stopWriting()
        return

    def writeSomeData(self, data):
        raise NotImplementedError('%s does not implement writeSomeData' % reflect.qual(self.__class__))

    def doRead(self):
        raise NotImplementedError('%s does not implement doRead' % reflect.qual(self.__class__))

    def doWrite(self):
        if len(self.dataBuffer) - self.offset < self.SEND_LIMIT:
            self.dataBuffer = _concatenate(self.dataBuffer, self.offset, self._tempDataBuffer)
            self.offset = 0
            self._tempDataBuffer = []
            self._tempDataLen = 0
        if self.offset:
            l = self.writeSomeData(lazyByteSlice(self.dataBuffer, self.offset))
        else:
            l = self.writeSomeData(self.dataBuffer)
        if isinstance(l, Exception) or l < 0:
            return l
        self.offset += l
        if self.offset == len(self.dataBuffer) and not self._tempDataLen:
            self.dataBuffer = ''
            self.offset = 0
            self.stopWriting()
            if self.producer is not None and (not self.streamingProducer or self.producerPaused):
                self.producerPaused = False
                self.producer.resumeProducing()
            else:
                if self.disconnecting:
                    return self._postLoseConnection()
                if self._writeDisconnecting:
                    self._writeDisconnected = True
                    result = self._closeWriteConnection()
                    return result
        return

    def _postLoseConnection(self):
        return main.CONNECTION_DONE

    def _closeWriteConnection(self):
        pass

    def writeConnectionLost(self, reason):
        self.connectionLost(reason)

    def readConnectionLost(self, reason):
        self.connectionLost(reason)

    def _isSendBufferFull(self):
        return len(self.dataBuffer) + self._tempDataLen > self.bufferSize

    def _maybePauseProducer(self):
        if self.producer is not None and self.streamingProducer:
            if self._isSendBufferFull():
                self.producerPaused = True
                self.producer.pauseProducing()
        return

    def write(self, data):
        if isinstance(data, unicode):
            raise TypeError('Data must not be unicode')
        if not self.connected or self._writeDisconnected:
            return
        if data:
            self._tempDataBuffer.append(data)
            self._tempDataLen += len(data)
            self._maybePauseProducer()
            self.startWriting()

    def writeSequence(self, iovec):
        for i in iovec:
            if isinstance(i, unicode):
                raise TypeError('Data must not be unicode')

        if not self.connected or not iovec or self._writeDisconnected:
            return
        self._tempDataBuffer.extend(iovec)
        for i in iovec:
            self._tempDataLen += len(i)

        self._maybePauseProducer()
        self.startWriting()

    def loseConnection(self, _connDone=failure.Failure(main.CONNECTION_DONE)):
        if self.connected and not self.disconnecting:
            if self._writeDisconnected:
                self.stopReading()
                self.stopWriting()
                self.connectionLost(_connDone)
            else:
                self.stopReading()
                self.startWriting()
                self.disconnecting = 1

    def loseWriteConnection(self):
        self._writeDisconnecting = True
        self.startWriting()

    def stopReading(self):
        self.reactor.removeReader(self)

    def stopWriting(self):
        self.reactor.removeWriter(self)

    def startReading(self):
        self.reactor.addReader(self)

    def startWriting(self):
        self.reactor.addWriter(self)

    producer = None
    bufferSize = 2 ** (2 ** 4)

    def stopConsuming(self):
        self.unregisterProducer()
        self.loseConnection()

    def resumeProducing(self):
        if self.connected and not self.disconnecting:
            self.startReading()

    def pauseProducing(self):
        self.stopReading()

    def stopProducing(self):
        self.loseConnection()

    def fileno(self):
        return -1


def isIPAddress(addr):
    dottedParts = addr.split('.')
    if len(dottedParts) == 4:
        for octet in dottedParts:
            try:
                value = int(octet)
            except ValueError:
                return False

            if value < 0 or value > 255:
                return False

        return True
    return False


def isIPv6Address(addr):
    if '%' in addr:
        addr = addr.split('%', 1)[0]
    if not addr:
        return False
    try:
        inet_pton(AF_INET6, addr)
    except (ValueError, error):
        return False

    return True


__all__ = [
 'FileDescriptor', 'isIPAddress', 'isIPv6Address']
# okay decompiling out\twisted.internet.abstract.pyc
