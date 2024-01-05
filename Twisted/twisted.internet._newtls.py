# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._newtls
from __future__ import division, absolute_import
from zope.interface import implementer
from zope.interface import directlyProvides
from twisted.internet.interfaces import ITLSTransport, ISSLTransport
from twisted.internet.abstract import FileDescriptor
from twisted.protocols.tls import TLSMemoryBIOFactory, TLSMemoryBIOProtocol

class _BypassTLS(object):

    def __init__(self, base, connection):
        self._base = base
        self._connection = connection

    def __getattr__(self, name):
        return getattr(self._connection, name)

    def write(self, data):
        return self._base.write(self._connection, data)

    def writeSequence(self, iovec):
        return self._base.writeSequence(self._connection, iovec)

    def loseConnection(self, *args, **kwargs):
        return self._base.loseConnection(self._connection, *args, **kwargs)

    def registerProducer(self, producer, streaming):
        return self._base.registerProducer(self._connection, producer, streaming)

    def unregisterProducer(self):
        return self._base.unregisterProducer(self._connection)


def startTLS(transport, contextFactory, normal, bypass):
    if normal:
        client = transport._tlsClientDefault
    else:
        client = not transport._tlsClientDefault
    producer, streaming = (None, None)
    if transport.producer is not None:
        producer, streaming = transport.producer, transport.streamingProducer
        transport.unregisterProducer()
    tlsFactory = TLSMemoryBIOFactory(contextFactory, client, None)
    tlsProtocol = TLSMemoryBIOProtocol(tlsFactory, transport.protocol, False)
    transport.protocol = tlsProtocol
    transport.getHandle = tlsProtocol.getHandle
    transport.getPeerCertificate = tlsProtocol.getPeerCertificate
    directlyProvides(transport, ISSLTransport)
    transport.TLS = True
    transport.protocol.makeConnection(_BypassTLS(bypass, transport))
    if producer:
        transport.registerProducer(producer, streaming)
    return


@implementer(ITLSTransport)
class ConnectionMixin(object):
    TLS = False

    def startTLS(self, ctx, normal=True):
        startTLS(self, ctx, normal, FileDescriptor)

    def write(self, bytes):
        if self.TLS:
            if self.connected:
                self.protocol.write(bytes)
        else:
            FileDescriptor.write(self, bytes)

    def writeSequence(self, iovec):
        if self.TLS:
            if self.connected:
                self.protocol.writeSequence(iovec)
        else:
            FileDescriptor.writeSequence(self, iovec)

    def loseConnection(self):
        if self.TLS:
            if self.connected and not self.disconnecting:
                self.protocol.loseConnection()
        else:
            FileDescriptor.loseConnection(self)

    def registerProducer(self, producer, streaming):
        if self.TLS:
            self.protocol.registerProducer(producer, streaming)
        else:
            FileDescriptor.registerProducer(self, producer, streaming)

    def unregisterProducer(self):
        if self.TLS:
            self.protocol.unregisterProducer()
        else:
            FileDescriptor.unregisterProducer(self)


class ClientMixin(object):
    _tlsClientDefault = True


class ServerMixin(object):
    _tlsClientDefault = False
# okay decompiling out\twisted.internet._newtls.pyc
