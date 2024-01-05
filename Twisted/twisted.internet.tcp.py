# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.tcp
from __future__ import division, absolute_import
import types, socket, sys, operator, struct
from zope.interface import implementer
from twisted.python.compat import _PY3, lazyByteSlice
from twisted.python.runtime import platformType
from twisted.python import versions, deprecate
try:
    from twisted.internet._newtls import ConnectionMixin as _TLSConnectionMixin, ClientMixin as _TLSClientMixin, ServerMixin as _TLSServerMixin
except ImportError:

    class _TLSConnectionMixin(object):
        TLS = False


    class _TLSClientMixin(object):
        pass


    class _TLSServerMixin(object):
        pass


if platformType == 'win32':
    EPERM = object()
    from errno import WSAEINVAL as EINVAL
    from errno import WSAEWOULDBLOCK as EWOULDBLOCK
    from errno import WSAEINPROGRESS as EINPROGRESS
    from errno import WSAEALREADY as EALREADY
    from errno import WSAEISCONN as EISCONN
    from errno import WSAENOBUFS as ENOBUFS
    from errno import WSAEMFILE as EMFILE
    ENFILE = object()
    ENOMEM = object()
    EAGAIN = EWOULDBLOCK
    from errno import WSAECONNRESET as ECONNABORTED
    from twisted.python.win32 import formatError as strerror
else:
    from errno import EPERM
    from errno import EINVAL
    from errno import EWOULDBLOCK
    from errno import EINPROGRESS
    from errno import EALREADY
    from errno import EISCONN
    from errno import ENOBUFS
    from errno import EMFILE
    from errno import ENFILE
    from errno import ENOMEM
    from errno import EAGAIN
    from errno import ECONNABORTED
    from os import strerror
from errno import errorcode
from twisted.internet import base, address, fdesc
from twisted.internet.task import deferLater
from twisted.python import log, failure, reflect
from twisted.python.util import untilConcludes
from twisted.internet.error import CannotListenError
from twisted.internet import abstract, main, interfaces, error
from twisted.internet.protocol import Protocol
_AI_NUMERICSERV = getattr(socket, 'AI_NUMERICSERV', 0)
if _PY3:
    _portNameType = str
else:
    _portNameType = types.StringTypes

class _SocketCloser(object):
    _shouldShutdown = True

    def _closeSocket(self, orderly):
        skt = self.socket
        try:
            if orderly:
                if self._shouldShutdown:
                    skt.shutdown(2)
            else:
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        except socket.error:
            pass

        try:
            skt.close()
        except socket.error:
            pass


class _AbortingMixin(object):
    _aborting = False

    def abortConnection(self):
        if self.disconnected or self._aborting:
            return
        self._aborting = True
        self.stopReading()
        self.stopWriting()
        self.doRead = lambda *args, **kwargs: None
        self.doWrite = lambda *args, **kwargs: None
        self.reactor.callLater(0, self.connectionLost, failure.Failure(error.ConnectionAborted()))


@implementer(interfaces.ITCPTransport, interfaces.ISystemHandle)
class Connection(_TLSConnectionMixin, abstract.FileDescriptor, _SocketCloser, _AbortingMixin):

    def __init__(self, skt, protocol, reactor=None):
        abstract.FileDescriptor.__init__(self, reactor=reactor)
        self.socket = skt
        self.socket.setblocking(0)
        self.fileno = skt.fileno
        self.protocol = protocol

    def getHandle(self):
        return self.socket

    def doRead(self):
        try:
            data = self.socket.recv(self.bufferSize)
        except socket.error as se:
            if se.args[0] == EWOULDBLOCK:
                return
            else:
                return main.CONNECTION_LOST

        return self._dataReceived(data)

    def _dataReceived(self, data):
        if not data:
            return main.CONNECTION_DONE
        else:
            rval = self.protocol.dataReceived(data)
            if rval is not None:
                offender = self.protocol.dataReceived
                warningFormat = 'Returning a value other than None from %(fqpn)s is deprecated since %(version)s.'
                warningString = deprecate.getDeprecationWarningString(offender, versions.Version('Twisted', 11, 0, 0), format=warningFormat)
                deprecate.warnAboutFunction(offender, warningString)
            return rval

    def writeSomeData(self, data):
        limitedData = lazyByteSlice(data, 0, self.SEND_LIMIT)
        try:
            return untilConcludes(self.socket.send, limitedData)
        except socket.error as se:
            if se.args[0] in (EWOULDBLOCK, ENOBUFS):
                return 0
            else:
                return main.CONNECTION_LOST

    def _closeWriteConnection(self):
        try:
            self.socket.shutdown(1)
        except socket.error:
            pass

        p = interfaces.IHalfCloseableProtocol(self.protocol, None)
        if p:
            try:
                p.writeConnectionLost()
            except:
                f = failure.Failure()
                log.err()
                self.connectionLost(f)

        return

    def readConnectionLost(self, reason):
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

    def connectionLost(self, reason):
        if not hasattr(self, 'socket'):
            return
        abstract.FileDescriptor.connectionLost(self, reason)
        self._closeSocket(not reason.check(error.ConnectionAborted))
        protocol = self.protocol
        del self.protocol
        del self.socket
        del self.fileno
        protocol.connectionLost(reason)

    logstr = 'Uninitialized'

    def logPrefix(self):
        return self.logstr

    def getTcpNoDelay(self):
        return operator.truth(self.socket.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

    def setTcpNoDelay(self, enabled):
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, enabled)

    def getTcpKeepAlive(self):
        return operator.truth(self.socket.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE))

    def setTcpKeepAlive(self, enabled):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, enabled)


class _BaseBaseClient(object):
    addressFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM

    def _finishInit(self, whenDone, skt, error, reactor):
        if whenDone:
            self._commonConnection.__init__(self, skt, None, reactor)
            reactor.callLater(0, whenDone)
        else:
            reactor.callLater(0, self.failIfNotConnected, error)
        return

    def resolveAddress(self):
        if self._requiresResolution:
            d = self.reactor.resolve(self.addr[0])
            d.addCallback((lambda n: (n,) + self.addr[1:]))
            d.addCallbacks(self._setRealAddress, self.failIfNotConnected)
        else:
            self._setRealAddress(self.addr)

    def _setRealAddress(self, address):
        self.realAddress = address
        self.doConnect()

    def failIfNotConnected(self, err):
        if self.connected or self.disconnected or not hasattr(self, 'connector'):
            return
        self._stopReadingAndWriting()
        try:
            self._closeSocket(True)
        except AttributeError:
            pass
        else:
            self._collectSocketDetails()

        self.connector.connectionFailed(failure.Failure(err))
        del self.connector

    def stopConnecting(self):
        self.failIfNotConnected(error.UserError())

    def connectionLost(self, reason):
        if not self.connected:
            self.failIfNotConnected(error.ConnectError(string=reason))
        else:
            self._commonConnection.connectionLost(self, reason)
            self.connector.connectionLost(reason)


class BaseClient(_BaseBaseClient, _TLSClientMixin, Connection):
    _base = Connection
    _commonConnection = Connection

    def _stopReadingAndWriting(self):
        if hasattr(self, 'reactor'):
            self.stopReading()
            self.stopWriting()

    def _collectSocketDetails(self):
        del self.socket
        del self.fileno

    def createInternetSocket(self):
        s = socket.socket(self.addressFamily, self.socketType)
        s.setblocking(0)
        fdesc._setCloseOnExec(s.fileno())
        return s

    def doConnect(self):
        self.doWrite = self.doConnect
        self.doRead = self.doConnect
        if not hasattr(self, 'connector'):
            return
        err = self.socket.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        if err:
            self.failIfNotConnected(error.getConnectError((err, strerror(err))))
            return
        try:
            connectResult = self.socket.connect_ex(self.realAddress)
        except socket.error as se:
            connectResult = se.args[0]

        if connectResult:
            if connectResult == EISCONN:
                pass
            else:
                if connectResult in (EWOULDBLOCK, EINPROGRESS, EALREADY) or connectResult == EINVAL and platformType == 'win32':
                    self.startReading()
                    self.startWriting()
                    return
                else:
                    self.failIfNotConnected(error.getConnectError((connectResult, strerror(connectResult))))
                    return

        del self.doWrite
        del self.doRead
        self.stopReading()
        self.stopWriting()
        self._connectDone()

    def _connectDone(self):
        self.protocol = self.connector.buildProtocol(self.getPeer())
        self.connected = 1
        logPrefix = self._getLogPrefix(self.protocol)
        self.logstr = '%s,client' % logPrefix
        if self.protocol is None:
            self.protocol = Protocol()
            self.loseConnection()
        else:
            self.startReading()
            self.protocol.makeConnection(self)
        return


_NUMERIC_ONLY = socket.AI_NUMERICHOST | _AI_NUMERICSERV

def _resolveIPv6(ip, port):
    return socket.getaddrinfo(ip, port, 0, 0, 0, _NUMERIC_ONLY)[0][4]


class _BaseTCPClient(object):
    _addressType = address.IPv4Address

    def __init__(self, host, port, bindAddress, connector, reactor=None):
        self.connector = connector
        self.addr = (host, port)
        whenDone = self.resolveAddress
        err = None
        skt = None
        if abstract.isIPAddress(host):
            self._requiresResolution = False
        else:
            if abstract.isIPv6Address(host):
                self._requiresResolution = False
                self.addr = _resolveIPv6(host, port)
                self.addressFamily = socket.AF_INET6
                self._addressType = address.IPv6Address
            else:
                self._requiresResolution = True
            try:
                skt = self.createInternetSocket()
            except socket.error as se:
                err = error.ConnectBindError(se.args[0], se.args[1])
                whenDone = None

        if whenDone and bindAddress is not None:
            try:
                if abstract.isIPv6Address(bindAddress[0]):
                    bindinfo = _resolveIPv6(*bindAddress)
                else:
                    bindinfo = bindAddress
                skt.bind(bindinfo)
            except socket.error as se:
                err = error.ConnectBindError(se.args[0], se.args[1])
                whenDone = None

        self._finishInit(whenDone, skt, err, reactor)
        return

    def getHost(self):
        return self._addressType('TCP', *self.socket.getsockname()[:2])

    def getPeer(self):
        return self._addressType('TCP', *self.realAddress[:2])

    def __repr__(self):
        s = '<%s to %s at %x>' % (self.__class__, self.addr, id(self))
        return s


class Client(_BaseTCPClient, BaseClient):
    pass


class Server(_TLSServerMixin, Connection):
    _base = Connection
    _addressType = address.IPv4Address

    def __init__(self, sock, protocol, client, server, sessionno, reactor):
        Connection.__init__(self, sock, protocol, reactor)
        if len(client) != 2:
            self._addressType = address.IPv6Address
        self.server = server
        self.client = client
        self.sessionno = sessionno
        self.hostname = client[0]
        logPrefix = self._getLogPrefix(self.protocol)
        self.logstr = '%s,%s,%s' % (logPrefix,
         sessionno,
         self.hostname)
        if self.server is not None:
            self.repstr = '<%s #%s on %s>' % (self.protocol.__class__.__name__,
             self.sessionno,
             self.server._realPortNumber)
        self.startReading()
        self.connected = 1
        return

    def __repr__(self):
        return self.repstr

    @classmethod
    def _fromConnectedSocket(cls, fileDescriptor, addressFamily, factory, reactor):
        addressType = address.IPv4Address
        if addressFamily == socket.AF_INET6:
            addressType = address.IPv6Address
        skt = socket.fromfd(fileDescriptor, addressFamily, socket.SOCK_STREAM)
        addr = skt.getpeername()
        protocolAddr = addressType('TCP', addr[0], addr[1])
        localPort = skt.getsockname()[1]
        protocol = factory.buildProtocol(protocolAddr)
        if protocol is None:
            skt.close()
            return
        else:
            self = cls(skt, protocol, addr, None, addr[1], reactor)
            self.repstr = '<%s #%s on %s>' % (
             self.protocol.__class__.__name__, self.sessionno, localPort)
            protocol.makeConnection(self)
            return self

    def getHost(self):
        host, port = self.socket.getsockname()[:2]
        return self._addressType('TCP', host, port)

    def getPeer(self):
        return self._addressType('TCP', *self.client[:2])


@implementer(interfaces.IListeningPort)
class Port(base.BasePort, _SocketCloser):
    socketType = socket.SOCK_STREAM
    transport = Server
    sessionno = 0
    interface = ''
    backlog = 50
    _type = 'TCP'
    _realPortNumber = None
    _preexistingSocket = None
    addressFamily = socket.AF_INET
    _addressType = address.IPv4Address

    def __init__(self, port, factory, backlog=50, interface='', reactor=None):
        base.BasePort.__init__(self, reactor=reactor)
        self.port = port
        self.factory = factory
        self.backlog = backlog
        if abstract.isIPv6Address(interface):
            self.addressFamily = socket.AF_INET6
            self._addressType = address.IPv6Address
        self.interface = interface

    @classmethod
    def _fromListeningDescriptor(cls, reactor, fd, addressFamily, factory):
        port = socket.fromfd(fd, addressFamily, cls.socketType)
        interface = port.getsockname()[0]
        self = cls(None, factory, None, interface, reactor)
        self._preexistingSocket = port
        return self

    def __repr__(self):
        if self._realPortNumber is not None:
            return '<%s of %s on %s>' % (self.__class__,
             self.factory.__class__, self._realPortNumber)
        else:
            return '<%s of %s (not listening)>' % (self.__class__, self.factory.__class__)
            return

    def createInternetSocket(self):
        s = base.BasePort.createInternetSocket(self)
        if platformType == 'posix' and sys.platform != 'cygwin':
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s

    def startListening(self):
        if self._preexistingSocket is None:
            try:
                skt = self.createInternetSocket()
                if self.addressFamily == socket.AF_INET6:
                    addr = _resolveIPv6(self.interface, self.port)
                else:
                    addr = (
                     self.interface, self.port)
                skt.bind(addr)
            except socket.error as le:
                raise CannotListenError(self.interface, self.port, le)

            skt.listen(self.backlog)
        else:
            skt = self._preexistingSocket
            self._preexistingSocket = None
            self._shouldShutdown = False
        self._realPortNumber = skt.getsockname()[1]
        log.msg('%s starting on %s' % (
         self._getLogPrefix(self.factory), self._realPortNumber))
        self.factory.doStart()
        self.connected = True
        self.socket = skt
        self.fileno = self.socket.fileno
        self.numberAccepts = 100
        self.startReading()
        return

    def _buildAddr(self, address):
        host, port = address[:2]
        return self._addressType('TCP', host, port)

    def doRead(self):
        try:
            if platformType == 'posix':
                numAccepts = self.numberAccepts
            else:
                numAccepts = 1
            for i in range(numAccepts):
                if self.disconnecting:
                    return
                try:
                    skt, addr = self.socket.accept()
                except socket.error as e:
                    if e.args[0] in (EWOULDBLOCK, EAGAIN):
                        self.numberAccepts = i
                        break
                    elif e.args[0] == EPERM:
                        continue
                    elif e.args[0] in (EMFILE, ENOBUFS, ENFILE, ENOMEM, ECONNABORTED):
                        log.msg('Could not accept new connection (%s)' % (
                         errorcode[e.args[0]],))
                        break
                    raise

                fdesc._setCloseOnExec(skt.fileno())
                protocol = self.factory.buildProtocol(self._buildAddr(addr))
                if protocol is None:
                    skt.close()
                    continue
                s = self.sessionno
                self.sessionno = s + 1
                transport = self.transport(skt, protocol, addr, self, s, self.reactor)
                protocol.makeConnection(transport)
            else:
                self.numberAccepts = self.numberAccepts + 20

        except:
            log.deferr()

        return

    def loseConnection(self, connDone=failure.Failure(main.CONNECTION_DONE)):
        self.disconnecting = True
        self.stopReading()
        if self.connected:
            self.deferred = deferLater(self.reactor, 0, self.connectionLost, connDone)
            return self.deferred

    stopListening = loseConnection

    def _logConnectionLostMsg(self):
        log.msg('(%s Port %s Closed)' % (self._type, self._realPortNumber))

    def connectionLost(self, reason):
        self._logConnectionLostMsg()
        self._realPortNumber = None
        base.BasePort.connectionLost(self, reason)
        self.connected = False
        self._closeSocket(True)
        del self.socket
        del self.fileno
        try:
            self.factory.doStop()
        finally:
            self.disconnecting = False

        return

    def logPrefix(self):
        return reflect.qual(self.factory.__class__)

    def getHost(self):
        host, port = self.socket.getsockname()[:2]
        return self._addressType('TCP', host, port)


class Connector(base.BaseConnector):
    _addressType = address.IPv4Address

    def __init__(self, host, port, factory, timeout, bindAddress, reactor=None):
        if isinstance(port, _portNameType):
            try:
                port = socket.getservbyname(port, 'tcp')
            except socket.error as e:
                raise error.ServiceNameUnknownError(string='%s (%r)' % (e, port))

        self.host, self.port = host, port
        if abstract.isIPv6Address(host):
            self._addressType = address.IPv6Address
        self.bindAddress = bindAddress
        base.BaseConnector.__init__(self, factory, timeout, reactor)

    def _makeTransport(self):
        return Client(self.host, self.port, self.bindAddress, self, self.reactor)

    def getDestination(self):
        return self._addressType('TCP', self.host, self.port)
# okay decompiling out\twisted.internet.tcp.pyc
