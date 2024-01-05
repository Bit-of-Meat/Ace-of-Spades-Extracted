# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.protocol
from __future__ import division, absolute_import
import random
from zope.interface import implementer
from twisted.python import log, failure, components
from twisted.internet import interfaces, error, defer
from twisted.logger import Logger
_log = Logger()
_logFor = lambda _: _log.__get__(_, _.__class__)

@implementer(interfaces.IProtocolFactory, interfaces.ILoggingContext)
class Factory:
    protocol = None
    numPorts = 0
    noisy = True

    @classmethod
    def forProtocol(cls, protocol, *args, **kwargs):
        factory = cls(*args, **kwargs)
        factory.protocol = protocol
        return factory

    def logPrefix(self):
        return self.__class__.__name__

    def doStart(self):
        if not self.numPorts:
            if self.noisy:
                _logFor(self).info('Starting factory {factory!r}', factory=self)
            self.startFactory()
        self.numPorts = self.numPorts + 1

    def doStop(self):
        if self.numPorts == 0:
            return
        self.numPorts = self.numPorts - 1
        if not self.numPorts:
            if self.noisy:
                _logFor(self).info('Stopping factory {factory!r}', factory=self)
            self.stopFactory()

    def startFactory(self):
        pass

    def stopFactory(self):
        pass

    def buildProtocol(self, addr):
        p = self.protocol()
        p.factory = self
        return p


class ClientFactory(Factory):

    def startedConnecting(self, connector):
        pass

    def clientConnectionFailed(self, connector, reason):
        pass

    def clientConnectionLost(self, connector, reason):
        pass


class _InstanceFactory(ClientFactory):
    noisy = False
    pending = None

    def __init__(self, reactor, instance, deferred):
        self.reactor = reactor
        self.instance = instance
        self.deferred = deferred

    def __repr__(self):
        return '<ClientCreator factory: %r>' % (self.instance,)

    def buildProtocol(self, addr):
        self.pending = self.reactor.callLater(0, self.fire, self.deferred.callback, self.instance)
        self.deferred = None
        return self.instance

    def clientConnectionFailed(self, connector, reason):
        self.pending = self.reactor.callLater(0, self.fire, self.deferred.errback, reason)
        self.deferred = None
        return

    def fire(self, func, value):
        self.pending = None
        func(value)
        return


class ClientCreator:

    def __init__(self, reactor, protocolClass, *args, **kwargs):
        self.reactor = reactor
        self.protocolClass = protocolClass
        self.args = args
        self.kwargs = kwargs

    def _connect(self, method, *args, **kwargs):

        def cancelConnect(deferred):
            connector.disconnect()
            if f.pending is not None:
                f.pending.cancel()
            return

        d = defer.Deferred(cancelConnect)
        f = _InstanceFactory(self.reactor, self.protocolClass(*self.args, **self.kwargs), d)
        connector = method(factory=f, *args, **kwargs)
        return d

    def connectTCP(self, host, port, timeout=30, bindAddress=None):
        return self._connect(self.reactor.connectTCP, host, port, timeout=timeout, bindAddress=bindAddress)

    def connectUNIX(self, address, timeout=30, checkPID=False):
        return self._connect(self.reactor.connectUNIX, address, timeout=timeout, checkPID=checkPID)

    def connectSSL(self, host, port, contextFactory, timeout=30, bindAddress=None):
        return self._connect(self.reactor.connectSSL, host, port, contextFactory=contextFactory, timeout=timeout, bindAddress=bindAddress)


class ReconnectingClientFactory(ClientFactory):
    maxDelay = 3600
    initialDelay = 1.0
    factor = 2.718281828459045
    jitter = 0.11962656472
    delay = initialDelay
    retries = 0
    maxRetries = None
    _callID = None
    connector = None
    clock = None
    continueTrying = 1

    def clientConnectionFailed(self, connector, reason):
        if self.continueTrying:
            self.connector = connector
            self.retry()

    def clientConnectionLost(self, connector, unused_reason):
        if self.continueTrying:
            self.connector = connector
            self.retry()

    def retry(self, connector=None):
        if not self.continueTrying:
            if self.noisy:
                log.msg('Abandoning %s on explicit request' % (connector,))
            return
        if connector is None:
            if self.connector is None:
                raise ValueError('no connector to retry')
            else:
                connector = self.connector
        self.retries += 1
        if self.maxRetries is not None and self.retries > self.maxRetries:
            if self.noisy:
                log.msg('Abandoning %s after %d retries.' % (
                 connector, self.retries))
            return
        self.delay = min(self.delay * self.factor, self.maxDelay)
        if self.jitter:
            self.delay = random.normalvariate(self.delay, self.delay * self.jitter)
        if self.noisy:
            log.msg('%s will retry in %d seconds' % (connector, self.delay))

        def reconnector():
            self._callID = None
            connector.connect()
            return

        if self.clock is None:
            from twisted.internet import reactor
            self.clock = reactor
        self._callID = self.clock.callLater(self.delay, reconnector)
        return

    def stopTrying(self):
        if self._callID:
            self._callID.cancel()
            self._callID = None
        self.continueTrying = 0
        if self.connector:
            try:
                self.connector.stopConnecting()
            except error.NotConnectingError:
                pass

        return

    def resetDelay(self):
        self.delay = self.initialDelay
        self.retries = 0
        self._callID = None
        self.continueTrying = 1
        return

    def __getstate__(self):
        state = self.__dict__.copy()
        for key in ['connector', 'retries', 'delay', 
         'continueTrying', 
         '_callID', 'clock']:
            if key in state:
                del state[key]

        return state


class ServerFactory(Factory):
    pass


class BaseProtocol:
    connected = 0
    transport = None

    def makeConnection(self, transport):
        self.connected = 1
        self.transport = transport
        self.connectionMade()

    def connectionMade(self):
        pass


connectionDone = failure.Failure(error.ConnectionDone())
connectionDone.cleanFailure()

@implementer(interfaces.IProtocol, interfaces.ILoggingContext)
class Protocol(BaseProtocol):

    def logPrefix(self):
        return self.__class__.__name__

    def dataReceived(self, data):
        pass

    def connectionLost(self, reason=connectionDone):
        pass


@implementer(interfaces.IConsumer)
class ProtocolToConsumerAdapter(components.Adapter):

    def write(self, data):
        self.original.dataReceived(data)

    def registerProducer(self, producer, streaming):
        pass

    def unregisterProducer(self):
        pass


components.registerAdapter(ProtocolToConsumerAdapter, interfaces.IProtocol, interfaces.IConsumer)

@implementer(interfaces.IProtocol)
class ConsumerToProtocolAdapter(components.Adapter):

    def dataReceived(self, data):
        self.original.write(data)

    def connectionLost(self, reason):
        pass

    def makeConnection(self, transport):
        pass

    def connectionMade(self):
        pass


components.registerAdapter(ConsumerToProtocolAdapter, interfaces.IConsumer, interfaces.IProtocol)

@implementer(interfaces.IProcessProtocol)
class ProcessProtocol(BaseProtocol):

    def childDataReceived(self, childFD, data):
        if childFD == 1:
            self.outReceived(data)
        elif childFD == 2:
            self.errReceived(data)

    def outReceived(self, data):
        pass

    def errReceived(self, data):
        pass

    def childConnectionLost(self, childFD):
        if childFD == 0:
            self.inConnectionLost()
        elif childFD == 1:
            self.outConnectionLost()
        elif childFD == 2:
            self.errConnectionLost()

    def inConnectionLost(self):
        pass

    def outConnectionLost(self):
        pass

    def errConnectionLost(self):
        pass

    def processExited(self, reason):
        pass

    def processEnded(self, reason):
        pass


class AbstractDatagramProtocol:
    transport = None
    numPorts = 0
    noisy = True

    def __getstate__(self):
        d = self.__dict__.copy()
        d['transport'] = None
        return d

    def doStart(self):
        if not self.numPorts:
            if self.noisy:
                log.msg('Starting protocol %s' % self)
            self.startProtocol()
        self.numPorts = self.numPorts + 1

    def doStop(self):
        self.numPorts = self.numPorts - 1
        self.transport = None
        if not self.numPorts:
            if self.noisy:
                log.msg('Stopping protocol %s' % self)
            self.stopProtocol()
        return

    def startProtocol(self):
        pass

    def stopProtocol(self):
        pass

    def makeConnection(self, transport):
        self.transport = transport
        self.doStart()

    def datagramReceived(self, datagram, addr):
        pass


@implementer(interfaces.ILoggingContext)
class DatagramProtocol(AbstractDatagramProtocol):

    def logPrefix(self):
        return self.__class__.__name__

    def connectionRefused(self):
        pass


class ConnectedDatagramProtocol(DatagramProtocol):

    def datagramReceived(self, datagram):
        pass

    def connectionFailed(self, failure):
        pass


@implementer(interfaces.ITransport)
class FileWrapper:
    closed = 0
    disconnecting = 0
    producer = None
    streamingProducer = 0

    def __init__(self, file):
        self.file = file

    def write(self, data):
        try:
            self.file.write(data)
        except:
            self.handleException()

    def _checkProducer(self):
        if self.producer:
            self.producer.resumeProducing()

    def registerProducer(self, producer, streaming):
        self.producer = producer
        self.streamingProducer = streaming
        if not streaming:
            producer.resumeProducing()

    def unregisterProducer(self):
        self.producer = None
        return

    def stopConsuming(self):
        self.unregisterProducer()
        self.loseConnection()

    def writeSequence(self, iovec):
        self.write(('').join(iovec))

    def loseConnection(self):
        self.closed = 1
        try:
            self.file.close()
        except (IOError, OSError):
            self.handleException()

    def getPeer(self):
        return ('file', 'file')

    def getHost(self):
        return 'file'

    def handleException(self):
        pass

    def resumeProducing(self):
        pass

    def pauseProducing(self):
        pass

    def stopProducing(self):
        self.loseConnection()


__all__ = [
 'Factory', 'ClientFactory', 'ReconnectingClientFactory', 'connectionDone', 
 'Protocol', 
 'ProcessProtocol', 'FileWrapper', 'ServerFactory', 
 'AbstractDatagramProtocol', 
 'DatagramProtocol', 'ConnectedDatagramProtocol', 
 'ClientCreator']
# okay decompiling out\twisted.internet.protocol.pyc
