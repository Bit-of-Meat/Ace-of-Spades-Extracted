# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.ssl
from __future__ import division, absolute_import
from OpenSSL import SSL
supported = True
from zope.interface import implementer, implementer_only, implementedBy
from twisted.internet import tcp, interfaces

class ContextFactory:
    isClient = 0

    def getContext(self):
        raise NotImplementedError


class DefaultOpenSSLContextFactory(ContextFactory):
    _context = None

    def __init__(self, privateKeyFileName, certificateFileName, sslmethod=SSL.SSLv23_METHOD, _contextFactory=SSL.Context):
        self.privateKeyFileName = privateKeyFileName
        self.certificateFileName = certificateFileName
        self.sslmethod = sslmethod
        self._contextFactory = _contextFactory
        self.cacheContext()

    def cacheContext(self):
        if self._context is None:
            ctx = self._contextFactory(self.sslmethod)
            ctx.set_options(SSL.OP_NO_SSLv2)
            ctx.use_certificate_file(self.certificateFileName)
            ctx.use_privatekey_file(self.privateKeyFileName)
            self._context = ctx
        return

    def __getstate__(self):
        d = self.__dict__.copy()
        del d['_context']
        return d

    def __setstate__(self, state):
        self.__dict__ = state

    def getContext(self):
        return self._context


class ClientContextFactory:
    isClient = 1
    method = SSL.SSLv23_METHOD
    _contextFactory = SSL.Context

    def getContext(self):
        ctx = self._contextFactory(self.method)
        ctx.set_options(SSL.OP_NO_SSLv2)
        return ctx


@implementer_only(interfaces.ISSLTransport, *[ i for i in implementedBy(tcp.Client) if i != interfaces.ITLSTransport
                                             ])
class Client(tcp.Client):

    def __init__(self, host, port, bindAddress, ctxFactory, connector, reactor=None):
        self.ctxFactory = ctxFactory
        tcp.Client.__init__(self, host, port, bindAddress, connector, reactor)

    def _connectDone(self):
        self.startTLS(self.ctxFactory)
        self.startWriting()
        tcp.Client._connectDone(self)


@implementer(interfaces.ISSLTransport)
class Server(tcp.Server):

    def __init__(self, *args, **kwargs):
        tcp.Server.__init__(self, *args, **kwargs)
        self.startTLS(self.server.ctxFactory)


class Port(tcp.Port):
    transport = Server
    _type = 'TLS'

    def __init__(self, port, factory, ctxFactory, backlog=50, interface='', reactor=None):
        tcp.Port.__init__(self, port, factory, backlog, interface, reactor)
        self.ctxFactory = ctxFactory

    def _getLogPrefix(self, factory):
        return tcp.Port._getLogPrefix(self, factory) + ' (TLS)'


class Connector(tcp.Connector):

    def __init__(self, host, port, factory, contextFactory, timeout, bindAddress, reactor=None):
        self.contextFactory = contextFactory
        tcp.Connector.__init__(self, host, port, factory, timeout, bindAddress, reactor)
        contextFactory.getContext()

    def _makeTransport(self):
        return Client(self.host, self.port, self.bindAddress, self.contextFactory, self, self.reactor)


from twisted.internet._sslverify import KeyPair, DistinguishedName, DN, Certificate, CertificateRequest, PrivateCertificate, OpenSSLAcceptableCiphers as AcceptableCiphers, OpenSSLCertificateOptions as CertificateOptions, OpenSSLDiffieHellmanParameters as DiffieHellmanParameters, platformTrust, OpenSSLDefaultPaths, VerificationError, optionsForClientTLS
__all__ = [
 'ContextFactory', 'DefaultOpenSSLContextFactory', 'ClientContextFactory', 
 'DistinguishedName', 
 'DN', 
 'Certificate', 'CertificateRequest', 'PrivateCertificate', 
 'KeyPair', 
 'AcceptableCiphers', 
 'CertificateOptions', 'DiffieHellmanParameters', 
 'platformTrust', 'OpenSSLDefaultPaths', 
 'VerificationError', 
 'optionsForClientTLS']
# okay decompiling out\twisted.internet.ssl.pyc
