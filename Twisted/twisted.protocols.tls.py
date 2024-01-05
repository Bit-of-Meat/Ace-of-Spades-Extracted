# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.protocols.tls
from __future__ import division, absolute_import
from OpenSSL.SSL import Error, ZeroReturnError, WantReadError
from OpenSSL.SSL import TLSv1_METHOD, Context, Connection
try:
    Connection(Context(TLSv1_METHOD), None)
except TypeError as e:
    if str(e) != 'argument must be an int, or have a fileno() method.':
        raise
    raise ImportError('twisted.protocols.tls requires pyOpenSSL 0.10 or newer.')

from zope.interface import implementer, providedBy, directlyProvides
from twisted.python.compat import unicode
from twisted.python.failure import Failure
from twisted.python import log
from twisted.python.reflect import safe_str
from twisted.internet.interfaces import ISystemHandle, ISSLTransport, IPushProducer, ILoggingContext, IOpenSSLServerConnectionCreator, IOpenSSLClientConnectionCreator
from twisted.internet.main import CONNECTION_LOST
from twisted.internet.protocol import Protocol
from twisted.internet.task import cooperate
from twisted.protocols.policies import ProtocolWrapper, WrappingFactory

@implementer(IPushProducer)
class _PullToPush(object):
    _finished = False

    def __init__(self, pullProducer, consumer):
        self._producer = pullProducer
        self._consumer = consumer

    def _pull(self):
        while True:
            try:
                self._producer.resumeProducing()
            except:
                log.err(None, '%s failed, producing will be stopped:' % (
                 safe_str(self._producer),))
                try:
                    self._consumer.unregisterProducer()
                except:
                    log.err(None, '%s failed to unregister producer:' % (
                     safe_str(self._consumer),))
                    self._finished = True
                    return

            yield

        return

    def startStreaming(self):
        self._coopTask = cooperate(self._pull())

    def stopStreaming(self):
        if self._finished:
            return
        self._finished = True
        self._coopTask.stop()

    def pauseProducing(self):
        self._coopTask.pause()

    def resumeProducing(self):
        self._coopTask.resume()

    def stopProducing(self):
        self.stopStreaming()
        self._producer.stopProducing()


@implementer(IPushProducer)
class _ProducerMembrane(object):
    _producerPaused = False

    def __init__(self, producer):
        self._producer = producer

    def pauseProducing(self):
        if self._producerPaused:
            return
        self._producerPaused = True
        self._producer.pauseProducing()

    def resumeProducing(self):
        if not self._producerPaused:
            return
        self._producerPaused = False
        self._producer.resumeProducing()

    def stopProducing(self):
        self._producer.stopProducing()


@implementer(ISystemHandle, ISSLTransport)
class TLSMemoryBIOProtocol(ProtocolWrapper):
    _reason = None
    _handshakeDone = False
    _lostTLSConnection = False
    _writeBlockedOnRead = False
    _producer = None
    _aborted = False

    def __init__(self, factory, wrappedProtocol, _connectWrapped=True):
        ProtocolWrapper.__init__(self, factory, wrappedProtocol)
        self._connectWrapped = _connectWrapped

    def getHandle(self):
        return self._tlsConnection

    def makeConnection(self, transport):
        self._tlsConnection = self.factory._createConnection(self)
        self._appSendBuffer = []
        for interface in providedBy(transport):
            directlyProvides(self, interface)

        Protocol.makeConnection(self, transport)
        self.factory.registerProtocol(self)
        if self._connectWrapped:
            ProtocolWrapper.makeConnection(self, transport)
        try:
            self._tlsConnection.do_handshake()
        except WantReadError:
            self._flushSendBIO()

    def _flushSendBIO(self):
        try:
            bytes = self._tlsConnection.bio_read(32768)
        except WantReadError:
            pass
        else:
            self.transport.write(bytes)

    def _flushReceiveBIO(self):
        while not self._lostTLSConnection:
            try:
                bytes = self._tlsConnection.recv(32768)
            except WantReadError:
                break
            except ZeroReturnError:
                self._shutdownTLS()
                self._tlsShutdownFinished(None)
            except Error as e:
                if e.args[0] == -1 and e.args[1] == 'Unexpected EOF':
                    failure = Failure(CONNECTION_LOST)
                else:
                    failure = Failure()
                self._flushSendBIO()
                self._tlsShutdownFinished(failure)
            else:
                self._handshakeDone = True
                if not self._aborted:
                    ProtocolWrapper.dataReceived(self, bytes)

        self._flushSendBIO()
        return

    def dataReceived(self, bytes):
        self._tlsConnection.bio_write(bytes)
        if self._writeBlockedOnRead:
            self._writeBlockedOnRead = False
            appSendBuffer = self._appSendBuffer
            self._appSendBuffer = []
            for bytes in appSendBuffer:
                self._write(bytes)

            if not self._writeBlockedOnRead and self.disconnecting and self.producer is None:
                self._shutdownTLS()
            if self._producer is not None:
                self._producer.resumeProducing()
        self._flushReceiveBIO()
        return

    def _shutdownTLS(self):
        try:
            shutdownSuccess = self._tlsConnection.shutdown()
        except Error:
            shutdownSuccess = False

        self._flushSendBIO()
        if shutdownSuccess:
            self.transport.loseConnection()

    def _tlsShutdownFinished(self, reason):
        if self._reason is None:
            self._reason = reason
        self._lostTLSConnection = True
        self.transport.loseConnection()
        return

    def connectionLost(self, reason):
        if not self._lostTLSConnection:
            self._tlsConnection.bio_shutdown()
            self._flushReceiveBIO()
            self._lostTLSConnection = True
        reason = self._reason or reason
        self._reason = None
        ProtocolWrapper.connectionLost(self, reason)
        return

    def loseConnection(self):
        if self.disconnecting:
            return
        else:
            self.disconnecting = True
            if not self._writeBlockedOnRead and self._producer is None:
                self._shutdownTLS()
            return

    def abortConnection(self):
        self._aborted = True
        self.disconnecting = True
        self._shutdownTLS()
        self.transport.abortConnection()

    def failVerification(self, reason):
        self._reason = reason
        self.abortConnection()

    def write(self, bytes):
        if isinstance(bytes, unicode):
            raise TypeError('Must write bytes to a TLS transport, not unicode.')
        if self.disconnecting and self._producer is None:
            return
        else:
            self._write(bytes)
            return

    def _write(self, bytes):
        if self._lostTLSConnection:
            return
        else:
            bufferSize = 65536
            alreadySent = 0
            while alreadySent < len(bytes):
                toSend = bytes[alreadySent:alreadySent + bufferSize]
                try:
                    sent = self._tlsConnection.send(toSend)
                except WantReadError:
                    self._writeBlockedOnRead = True
                    self._appSendBuffer.append(bytes[alreadySent:])
                    if self._producer is not None:
                        self._producer.pauseProducing()
                    break
                except Error:
                    self._tlsShutdownFinished(Failure())
                    break
                else:
                    self._handshakeDone = True
                    self._flushSendBIO()
                    alreadySent += sent

            return

    def writeSequence(self, iovec):
        self.write(('').join(iovec))

    def getPeerCertificate(self):
        return self._tlsConnection.get_peer_certificate()

    def registerProducer(self, producer, streaming):
        if self._lostTLSConnection:
            producer.stopProducing()
            return
        if not streaming:
            producer = streamingProducer = _PullToPush(producer, self)
        producer = _ProducerMembrane(producer)
        self.transport.registerProducer(producer, True)
        self._producer = producer
        if not streaming:
            streamingProducer.startStreaming()

    def unregisterProducer(self):
        if isinstance(self._producer._producer, _PullToPush):
            self._producer._producer.stopStreaming()
        self._producer = None
        self._producerPaused = False
        self.transport.unregisterProducer()
        if self.disconnecting and not self._writeBlockedOnRead:
            self._shutdownTLS()
        return


@implementer(IOpenSSLClientConnectionCreator, IOpenSSLServerConnectionCreator)
class _ContextFactoryToConnectionFactory(object):

    def __init__(self, oldStyleContextFactory):
        oldStyleContextFactory.getContext()
        self._oldStyleContextFactory = oldStyleContextFactory

    def _connectionForTLS(self, protocol):
        context = self._oldStyleContextFactory.getContext()
        return Connection(context, None)

    def serverConnectionForTLS(self, protocol):
        return self._connectionForTLS(protocol)

    def clientConnectionForTLS(self, protocol):
        return self._connectionForTLS(protocol)


class TLSMemoryBIOFactory(WrappingFactory):
    protocol = TLSMemoryBIOProtocol
    noisy = False

    def __init__(self, contextFactory, isClient, wrappedFactory):
        WrappingFactory.__init__(self, wrappedFactory)
        if isClient:
            creatorInterface = IOpenSSLClientConnectionCreator
        else:
            creatorInterface = IOpenSSLServerConnectionCreator
        self._creatorInterface = creatorInterface
        if not creatorInterface.providedBy(contextFactory):
            contextFactory = _ContextFactoryToConnectionFactory(contextFactory)
        self._connectionCreator = contextFactory

    def logPrefix(self):
        if ILoggingContext.providedBy(self.wrappedFactory):
            logPrefix = self.wrappedFactory.logPrefix()
        else:
            logPrefix = self.wrappedFactory.__class__.__name__
        return '%s (TLS)' % (logPrefix,)

    def _createConnection(self, tlsProtocol):
        connectionCreator = self._connectionCreator
        if self._creatorInterface is IOpenSSLClientConnectionCreator:
            connection = connectionCreator.clientConnectionForTLS(tlsProtocol)
            connection.set_connect_state()
        else:
            connection = connectionCreator.serverConnectionForTLS(tlsProtocol)
            connection.set_accept_state()
        return connection
# okay decompiling out\twisted.protocols.tls.pyc
