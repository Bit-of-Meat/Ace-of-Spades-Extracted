# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.endpoints
from __future__ import division, absolute_import
import os, re, socket, warnings
from socket import AF_INET6, AF_INET
from zope.interface import implementer, directlyProvides
from twisted.internet import interfaces, defer, error, fdesc, threads
from twisted.internet.abstract import isIPv6Address
from twisted.internet.address import _ProcessAddress, HostnameAddress
from twisted.internet.interfaces import IStreamServerEndpointStringParser, IStreamClientEndpointStringParser, IStreamClientEndpointStringParserWithReactor
from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import ProcessProtocol, Protocol
from twisted.internet.stdio import StandardIO, PipeAddress
from twisted.internet.task import LoopingCall
from twisted.plugin import IPlugin, getPlugins
from twisted.python import log
from twisted.python.compat import nativeString
from twisted.python.components import proxyForInterface
from twisted.python.constants import NamedConstant, Names
from twisted.python.failure import Failure
from twisted.python.filepath import FilePath
from twisted.python.systemd import ListenFDs
__all__ = [
 'clientFromString', 'serverFromString', 
 'TCP4ServerEndpoint', 'TCP6ServerEndpoint', 
 'TCP4ClientEndpoint', 
 'TCP6ClientEndpoint', 
 'UNIXServerEndpoint', 'UNIXClientEndpoint', 
 'SSL4ServerEndpoint', 
 'SSL4ClientEndpoint', 
 'AdoptedStreamServerEndpoint', 'StandardIOEndpoint', 
 'ProcessEndpoint', 
 'HostnameEndpoint', 
 'StandardErrorBehavior', 'connectProtocol']

class _WrappingProtocol(Protocol):

    def __init__(self, connectedDeferred, wrappedProtocol):
        self._connectedDeferred = connectedDeferred
        self._wrappedProtocol = wrappedProtocol
        for iface in [interfaces.IHalfCloseableProtocol,
         interfaces.IFileDescriptorReceiver]:
            if iface.providedBy(self._wrappedProtocol):
                directlyProvides(self, iface)

    def logPrefix(self):
        if interfaces.ILoggingContext.providedBy(self._wrappedProtocol):
            return self._wrappedProtocol.logPrefix()
        return self._wrappedProtocol.__class__.__name__

    def connectionMade(self):
        self._wrappedProtocol.makeConnection(self.transport)
        self._connectedDeferred.callback(self._wrappedProtocol)

    def dataReceived(self, data):
        return self._wrappedProtocol.dataReceived(data)

    def fileDescriptorReceived(self, descriptor):
        return self._wrappedProtocol.fileDescriptorReceived(descriptor)

    def connectionLost(self, reason):
        return self._wrappedProtocol.connectionLost(reason)

    def readConnectionLost(self):
        self._wrappedProtocol.readConnectionLost()

    def writeConnectionLost(self):
        self._wrappedProtocol.writeConnectionLost()


class _WrappingFactory(ClientFactory):
    protocol = _WrappingProtocol

    def __init__(self, wrappedFactory):
        self._wrappedFactory = wrappedFactory
        self._onConnection = defer.Deferred(canceller=self._canceller)

    def startedConnecting(self, connector):
        self._connector = connector

    def _canceller(self, deferred):
        deferred.errback(error.ConnectingCancelledError(self._connector.getDestination()))
        self._connector.stopConnecting()

    def doStart(self):
        self._wrappedFactory.doStart()

    def doStop(self):
        self._wrappedFactory.doStop()

    def buildProtocol(self, addr):
        try:
            proto = self._wrappedFactory.buildProtocol(addr)
            if proto is None:
                raise error.NoProtocol()
        except:
            self._onConnection.errback()
        else:
            return self.protocol(self._onConnection, proto)

        return

    def clientConnectionFailed(self, connector, reason):
        if not self._onConnection.called:
            self._onConnection.errback(reason)


@implementer(interfaces.IStreamServerEndpoint)
class StandardIOEndpoint(object):
    _stdio = StandardIO

    def __init__(self, reactor):
        self._reactor = reactor

    def listen(self, stdioProtocolFactory):
        return defer.execute(self._stdio, stdioProtocolFactory.buildProtocol(PipeAddress()), reactor=self._reactor)


class _IProcessTransportWithConsumerAndProducer(interfaces.IProcessTransport, interfaces.IConsumer, interfaces.IPushProducer):
    pass


class _ProcessEndpointTransport(proxyForInterface(_IProcessTransportWithConsumerAndProducer, '_process')):
    pass


class _WrapIProtocol(ProcessProtocol):

    def __init__(self, proto, executable, errFlag):
        self.protocol = proto
        self.errFlag = errFlag
        self.executable = executable

    def makeConnection(self, process):
        self.transport = _ProcessEndpointTransport(process)
        return self.protocol.makeConnection(self.transport)

    def childDataReceived(self, childFD, data):
        if childFD == 1:
            return self.protocol.dataReceived(data)
        if childFD == 2 and self.errFlag == StandardErrorBehavior.LOG:
            log.msg(format='Process %(executable)r wrote stderr unhandled by %(protocol)s: %(data)s', executable=self.executable, protocol=self.protocol, data=data)

    def processEnded(self, reason):
        if reason.check(error.ProcessDone) == error.ProcessDone and reason.value.status == 0:
            return self.protocol.connectionLost(Failure(error.ConnectionDone()))
        else:
            return self.protocol.connectionLost(reason)


class StandardErrorBehavior(Names):
    LOG = NamedConstant()
    DROP = NamedConstant()


@implementer(interfaces.IStreamClientEndpoint)
class ProcessEndpoint(object):

    def __init__(self, reactor, executable, args=(), env={}, path=None, uid=None, gid=None, usePTY=0, childFDs=None, errFlag=StandardErrorBehavior.LOG):
        self._reactor = reactor
        self._executable = executable
        self._args = args
        self._env = env
        self._path = path
        self._uid = uid
        self._gid = gid
        self._usePTY = usePTY
        self._childFDs = childFDs
        self._errFlag = errFlag
        self._spawnProcess = self._reactor.spawnProcess

    def connect(self, protocolFactory):
        proto = protocolFactory.buildProtocol(_ProcessAddress())
        try:
            self._spawnProcess(_WrapIProtocol(proto, self._executable, self._errFlag), self._executable, self._args, self._env, self._path, self._uid, self._gid, self._usePTY, self._childFDs)
        except:
            return defer.fail()

        return defer.succeed(proto)


@implementer(interfaces.IStreamServerEndpoint)
class _TCPServerEndpoint(object):

    def __init__(self, reactor, port, backlog, interface):
        self._reactor = reactor
        self._port = port
        self._backlog = backlog
        self._interface = interface

    def listen(self, protocolFactory):
        return defer.execute(self._reactor.listenTCP, self._port, protocolFactory, backlog=self._backlog, interface=self._interface)


class TCP4ServerEndpoint(_TCPServerEndpoint):

    def __init__(self, reactor, port, backlog=50, interface=''):
        _TCPServerEndpoint.__init__(self, reactor, port, backlog, interface)


class TCP6ServerEndpoint(_TCPServerEndpoint):

    def __init__(self, reactor, port, backlog=50, interface='::'):
        _TCPServerEndpoint.__init__(self, reactor, port, backlog, interface)


@implementer(interfaces.IStreamClientEndpoint)
class TCP4ClientEndpoint(object):

    def __init__(self, reactor, host, port, timeout=30, bindAddress=None):
        self._reactor = reactor
        self._host = host
        self._port = port
        self._timeout = timeout
        self._bindAddress = bindAddress

    def connect(self, protocolFactory):
        try:
            wf = _WrappingFactory(protocolFactory)
            self._reactor.connectTCP(self._host, self._port, wf, timeout=self._timeout, bindAddress=self._bindAddress)
            return wf._onConnection
        except:
            return defer.fail()


@implementer(interfaces.IStreamClientEndpoint)
class TCP6ClientEndpoint(object):
    _getaddrinfo = staticmethod(socket.getaddrinfo)
    _deferToThread = staticmethod(threads.deferToThread)
    _GAI_ADDRESS = 4
    _GAI_ADDRESS_HOST = 0

    def __init__(self, reactor, host, port, timeout=30, bindAddress=None):
        self._reactor = reactor
        self._host = host
        self._port = port
        self._timeout = timeout
        self._bindAddress = bindAddress

    def connect(self, protocolFactory):
        if isIPv6Address(self._host):
            d = self._resolvedHostConnect(self._host, protocolFactory)
        else:
            d = self._nameResolution(self._host)
            d.addCallback((lambda result: result[0][self._GAI_ADDRESS][self._GAI_ADDRESS_HOST]))
            d.addCallback(self._resolvedHostConnect, protocolFactory)
        return d

    def _nameResolution(self, host):
        return self._deferToThread(self._getaddrinfo, host, 0, socket.AF_INET6)

    def _resolvedHostConnect(self, resolvedHost, protocolFactory):
        try:
            wf = _WrappingFactory(protocolFactory)
            self._reactor.connectTCP(resolvedHost, self._port, wf, timeout=self._timeout, bindAddress=self._bindAddress)
            return wf._onConnection
        except:
            return defer.fail()


@implementer(interfaces.IStreamClientEndpoint)
class HostnameEndpoint(object):
    _getaddrinfo = staticmethod(socket.getaddrinfo)
    _deferToThread = staticmethod(threads.deferToThread)

    def __init__(self, reactor, host, port, timeout=30, bindAddress=None):
        self._reactor = reactor
        self._host = host
        self._port = port
        self._timeout = timeout
        self._bindAddress = bindAddress

    def connect(self, protocolFactory):
        wf = protocolFactory
        pending = []

        def _canceller(d):
            d.errback(error.ConnectingCancelledError(HostnameAddress(self._host, self._port)))
            for p in pending[:]:
                p.cancel()

        def errbackForGai(failure):
            return defer.fail(error.DNSLookupError("Couldn't find the hostname '%s'" % (self._host,)))

        def _endpoints(gaiResult):
            for family, socktype, proto, canonname, sockaddr in gaiResult:
                if family in [AF_INET6]:
                    yield TCP6ClientEndpoint(self._reactor, sockaddr[0], sockaddr[1], self._timeout, self._bindAddress)
                elif family in [AF_INET]:
                    yield TCP4ClientEndpoint(self._reactor, sockaddr[0], sockaddr[1], self._timeout, self._bindAddress)

        def attemptConnection(endpoints):
            endpointsListExhausted = []
            successful = []
            failures = []
            winner = defer.Deferred(canceller=_canceller)

            def usedEndpointRemoval(connResult, connAttempt):
                pending.remove(connAttempt)
                return connResult

            def afterConnectionAttempt(connResult):
                if lc.running:
                    lc.stop()
                successful.append(True)
                for p in pending[:]:
                    p.cancel()

                winner.callback(connResult)
                return

            def checkDone():
                if endpointsListExhausted and not pending and not successful:
                    winner.errback(failures.pop())

            def connectFailed(reason):
                failures.append(reason)
                checkDone()
                return

            def iterateEndpoint():
                try:
                    endpoint = next(endpoints)
                except StopIteration:
                    endpointsListExhausted.append(True)
                    lc.stop()
                    checkDone()
                else:
                    dconn = endpoint.connect(wf)
                    pending.append(dconn)
                    dconn.addBoth(usedEndpointRemoval, dconn)
                    dconn.addCallback(afterConnectionAttempt)
                    dconn.addErrback(connectFailed)

            lc = LoopingCall(iterateEndpoint)
            lc.clock = self._reactor
            lc.start(0.3)
            return winner

        d = self._nameResolution(self._host, self._port)
        d.addErrback(errbackForGai)
        d.addCallback(_endpoints)
        d.addCallback(attemptConnection)
        return d

    def _nameResolution(self, host, port):
        return self._deferToThread(self._getaddrinfo, host, port, 0, socket.SOCK_STREAM)


@implementer(interfaces.IStreamServerEndpoint)
class SSL4ServerEndpoint(object):

    def __init__(self, reactor, port, sslContextFactory, backlog=50, interface=''):
        self._reactor = reactor
        self._port = port
        self._sslContextFactory = sslContextFactory
        self._backlog = backlog
        self._interface = interface

    def listen(self, protocolFactory):
        return defer.execute(self._reactor.listenSSL, self._port, protocolFactory, contextFactory=self._sslContextFactory, backlog=self._backlog, interface=self._interface)


@implementer(interfaces.IStreamClientEndpoint)
class SSL4ClientEndpoint(object):

    def __init__(self, reactor, host, port, sslContextFactory, timeout=30, bindAddress=None):
        self._reactor = reactor
        self._host = host
        self._port = port
        self._sslContextFactory = sslContextFactory
        self._timeout = timeout
        self._bindAddress = bindAddress

    def connect(self, protocolFactory):
        try:
            wf = _WrappingFactory(protocolFactory)
            self._reactor.connectSSL(self._host, self._port, wf, self._sslContextFactory, timeout=self._timeout, bindAddress=self._bindAddress)
            return wf._onConnection
        except:
            return defer.fail()


@implementer(interfaces.IStreamServerEndpoint)
class UNIXServerEndpoint(object):

    def __init__(self, reactor, address, backlog=50, mode=438, wantPID=0):
        self._reactor = reactor
        self._address = address
        self._backlog = backlog
        self._mode = mode
        self._wantPID = wantPID

    def listen(self, protocolFactory):
        return defer.execute(self._reactor.listenUNIX, self._address, protocolFactory, backlog=self._backlog, mode=self._mode, wantPID=self._wantPID)


@implementer(interfaces.IStreamClientEndpoint)
class UNIXClientEndpoint(object):

    def __init__(self, reactor, path, timeout=30, checkPID=0):
        self._reactor = reactor
        self._path = path
        self._timeout = timeout
        self._checkPID = checkPID

    def connect(self, protocolFactory):
        try:
            wf = _WrappingFactory(protocolFactory)
            self._reactor.connectUNIX(self._path, wf, timeout=self._timeout, checkPID=self._checkPID)
            return wf._onConnection
        except:
            return defer.fail()


@implementer(interfaces.IStreamServerEndpoint)
class AdoptedStreamServerEndpoint(object):
    _close = os.close
    _setNonBlocking = staticmethod(fdesc.setNonBlocking)

    def __init__(self, reactor, fileno, addressFamily):
        self.reactor = reactor
        self.fileno = fileno
        self.addressFamily = addressFamily
        self._used = False

    def listen(self, factory):
        if self._used:
            return defer.fail(error.AlreadyListened())
        self._used = True
        try:
            self._setNonBlocking(self.fileno)
            port = self.reactor.adoptStreamPort(self.fileno, self.addressFamily, factory)
            self._close(self.fileno)
        except:
            return defer.fail()

        return defer.succeed(port)


def _parseTCP(factory, port, interface='', backlog=50):
    return (
     (
      int(port), factory),
     {'interface': interface, 'backlog': int(backlog)})


def _parseUNIX(factory, address, mode='666', backlog=50, lockfile=True):
    return (
     (
      address, factory),
     {'mode': int(mode, 8), 'backlog': int(backlog), 'wantPID': bool(int(lockfile))})


def _parseSSL(factory, port, privateKey='server.pem', certKey=None, sslmethod=None, interface='', backlog=50, extraCertChain=None, dhParameters=None):
    from twisted.internet import ssl
    if certKey is None:
        certKey = privateKey
    kw = {}
    if sslmethod is not None:
        kw['method'] = getattr(ssl.SSL, sslmethod)
    certPEM = FilePath(certKey).getContent()
    keyPEM = FilePath(privateKey).getContent()
    privateCertificate = ssl.PrivateCertificate.loadPEM(certPEM + keyPEM)
    if extraCertChain is not None:
        extraCertChain = FilePath(extraCertChain).getContent()
        matches = re.findall('(-----BEGIN CERTIFICATE-----\\n.+?\\n-----END CERTIFICATE-----)', nativeString(extraCertChain), flags=re.DOTALL)
        chainCertificates = [ ssl.Certificate.loadPEM(chainCertPEM).original for chainCertPEM in matches
                            ]
        if not chainCertificates:
            raise ValueError("Specified chain file '%s' doesn't contain any valid certificates in PEM format." % (
             extraCertChain,))
    else:
        chainCertificates = None
    if dhParameters is not None:
        dhParameters = ssl.DiffieHellmanParameters.fromFile(FilePath(dhParameters))
    cf = ssl.CertificateOptions(privateKey=privateCertificate.privateKey.original, certificate=privateCertificate.original, extraCertChain=chainCertificates, dhParameters=dhParameters, **kw)
    return (
     (
      int(port), factory, cf), {'interface': interface, 'backlog': int(backlog)})


@implementer(IPlugin, IStreamServerEndpointStringParser)
class _StandardIOParser(object):
    prefix = 'stdio'

    def _parseServer(self, reactor):
        return StandardIOEndpoint(reactor)

    def parseStreamServer(self, reactor, *args, **kwargs):
        return self._parseServer(reactor)


@implementer(IPlugin, IStreamServerEndpointStringParser)
class _SystemdParser(object):
    _sddaemon = ListenFDs.fromEnvironment()
    prefix = 'systemd'

    def _parseServer(self, reactor, domain, index):
        index = int(index)
        fileno = self._sddaemon.inheritedDescriptors()[index]
        addressFamily = getattr(socket, 'AF_' + domain)
        return AdoptedStreamServerEndpoint(reactor, fileno, addressFamily)

    def parseStreamServer(self, reactor, *args, **kwargs):
        return self._parseServer(reactor, *args, **kwargs)


@implementer(IPlugin, IStreamServerEndpointStringParser)
class _TCP6ServerParser(object):
    prefix = 'tcp6'

    def _parseServer(self, reactor, port, backlog=50, interface='::'):
        port = int(port)
        backlog = int(backlog)
        return TCP6ServerEndpoint(reactor, port, backlog, interface)

    def parseStreamServer(self, reactor, *args, **kwargs):
        return self._parseServer(reactor, *args, **kwargs)


_serverParsers = {'tcp': _parseTCP, 'unix': _parseUNIX, 
   'ssl': _parseSSL}
_OP, _STRING = range(2)

def _tokenize(description):
    current = ''
    ops = ':='
    nextOps = {':': ':=', '=': ':'}
    description = iter(description)
    for n in description:
        if n in ops:
            yield (
             _STRING, current)
            yield (_OP, n)
            current = ''
            ops = nextOps[n]
        elif n == '\\':
            current += next(description)
        else:
            current += n

    yield (
     _STRING, current)


def _parse(description):
    args, kw = [], {}

    def add(sofar):
        if len(sofar) == 1:
            args.append(sofar[0])
        else:
            kw[sofar[0]] = sofar[1]

    sofar = ()
    for type, value in _tokenize(description):
        if type is _STRING:
            sofar += (value,)
        elif value == ':':
            add(sofar)
            sofar = ()

    add(sofar)
    return (args, kw)


_endpointServerFactories = {'TCP': TCP4ServerEndpoint, 
   'SSL': SSL4ServerEndpoint, 
   'UNIX': UNIXServerEndpoint}
_endpointClientFactories = {'TCP': TCP4ClientEndpoint, 
   'SSL': SSL4ClientEndpoint, 
   'UNIX': UNIXClientEndpoint}
_NO_DEFAULT = object()

def _parseServer(description, factory, default=None):
    args, kw = _parse(description)
    if not args or len(args) == 1 and not kw:
        deprecationMessage = "Unqualified strport description passed to 'service'.Use qualified endpoint descriptions; for example, 'tcp:%s'." % (
         description,)
        if default is None:
            default = 'tcp'
            warnings.warn(deprecationMessage, category=DeprecationWarning, stacklevel=4)
        elif default is _NO_DEFAULT:
            raise ValueError(deprecationMessage)
        args[0:0] = [
         default]
    endpointType = args[0]
    parser = _serverParsers.get(endpointType)
    if parser is None:
        for plugin in getPlugins(IStreamServerEndpointStringParser):
            if plugin.prefix == endpointType:
                return (plugin, args[1:], kw)

        raise ValueError("Unknown endpoint type: '%s'" % (endpointType,))
    return (
     endpointType.upper(),) + parser(factory, *args[1:], **kw)


def _serverFromStringLegacy(reactor, description, default):
    nameOrPlugin, args, kw = _parseServer(description, None, default)
    if type(nameOrPlugin) is not str:
        plugin = nameOrPlugin
        return plugin.parseStreamServer(reactor, *args, **kw)
    else:
        name = nameOrPlugin
        args = args[:1] + args[2:]
        return _endpointServerFactories[name](reactor, *args, **kw)


def serverFromString(reactor, description):
    return _serverFromStringLegacy(reactor, description, _NO_DEFAULT)


def quoteStringArgument(argument):
    return argument.replace('\\', '\\\\').replace(':', '\\:')


def _parseClientTCP(*args, **kwargs):
    if len(args) == 2:
        kwargs['port'] = int(args[1])
        kwargs['host'] = args[0]
    else:
        if len(args) == 1:
            if 'host' in kwargs:
                kwargs['port'] = int(args[0])
            else:
                kwargs['host'] = args[0]
        try:
            kwargs['port'] = int(kwargs['port'])
        except KeyError:
            pass

        try:
            kwargs['timeout'] = int(kwargs['timeout'])
        except KeyError:
            pass

        try:
            kwargs['bindAddress'] = (kwargs['bindAddress'], 0)
        except KeyError:
            pass

    return kwargs


def _loadCAsFromDir(directoryPath):
    from twisted.internet import ssl
    caCerts = {}
    for child in directoryPath.children():
        if not child.basename().split('.')[-1].lower() == 'pem':
            continue
        try:
            data = child.getContent()
        except IOError:
            continue

        try:
            theCert = ssl.Certificate.loadPEM(data)
        except ssl.SSL.Error:
            pass
        else:
            caCerts[theCert.digest()] = theCert.original

    return caCerts.values()


def _parseClientSSL(*args, **kwargs):
    from twisted.internet import ssl
    kwargs = _parseClientTCP(*args, **kwargs)
    certKey = kwargs.pop('certKey', None)
    privateKey = kwargs.pop('privateKey', None)
    caCertsDir = kwargs.pop('caCertsDir', None)
    if certKey is not None:
        certx509 = ssl.Certificate.loadPEM(FilePath(certKey).getContent()).original
    else:
        certx509 = None
    if privateKey is not None:
        privateKey = ssl.PrivateCertificate.loadPEM(FilePath(privateKey).getContent()).privateKey.original
    else:
        privateKey = None
    if caCertsDir is not None:
        verify = True
        caCerts = _loadCAsFromDir(FilePath(caCertsDir))
    else:
        verify = False
        caCerts = None
    kwargs['sslContextFactory'] = ssl.CertificateOptions(certificate=certx509, privateKey=privateKey, verify=verify, caCerts=caCerts)
    return kwargs


def _parseClientUNIX(*args, **kwargs):
    if len(args) == 1:
        kwargs['path'] = args[0]
    try:
        kwargs['checkPID'] = bool(int(kwargs.pop('lockfile')))
    except KeyError:
        pass

    try:
        kwargs['timeout'] = int(kwargs['timeout'])
    except KeyError:
        pass

    return kwargs


_clientParsers = {'TCP': _parseClientTCP, 
   'SSL': _parseClientSSL, 
   'UNIX': _parseClientUNIX}

def clientFromString(reactor, description):
    args, kwargs = _parse(description)
    aname = args.pop(0)
    name = aname.upper()
    for plugin in getPlugins(IStreamClientEndpointStringParserWithReactor):
        if plugin.prefix.upper() == name:
            return plugin.parseStreamClient(reactor, *args, **kwargs)

    for plugin in getPlugins(IStreamClientEndpointStringParser):
        if plugin.prefix.upper() == name:
            return plugin.parseStreamClient(*args, **kwargs)

    if name not in _clientParsers:
        raise ValueError('Unknown endpoint type: %r' % (aname,))
    kwargs = _clientParsers[name](*args, **kwargs)
    return _endpointClientFactories[name](reactor, **kwargs)


def connectProtocol(endpoint, protocol):

    class OneShotFactory(Factory):

        def buildProtocol(self, addr):
            return protocol

    return endpoint.connect(OneShotFactory())
# okay decompiling out\twisted.internet.endpoints.pyc
