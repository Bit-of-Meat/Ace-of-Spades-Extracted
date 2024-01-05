# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.udp
from __future__ import division, absolute_import
import socket, operator, struct, warnings
from zope.interface import implementer
from twisted.python.runtime import platformType
if platformType == 'win32':
    from errno import WSAEWOULDBLOCK
    from errno import WSAEINTR, WSAEMSGSIZE, WSAETIMEDOUT
    from errno import WSAECONNREFUSED, WSAECONNRESET, WSAENETRESET
    from errno import WSAEINPROGRESS
    from errno import WSAENOPROTOOPT as ENOPROTOOPT
    _sockErrReadIgnore = [
     WSAEINTR, WSAEWOULDBLOCK, WSAEMSGSIZE, WSAEINPROGRESS]
    _sockErrReadRefuse = [WSAECONNREFUSED, WSAECONNRESET, WSAENETRESET,
     WSAETIMEDOUT]
    EMSGSIZE = WSAEMSGSIZE
    ECONNREFUSED = WSAECONNREFUSED
    EAGAIN = WSAEWOULDBLOCK
    EINTR = WSAEINTR
else:
    from errno import EWOULDBLOCK, EINTR, EMSGSIZE, ECONNREFUSED, EAGAIN
    from errno import ENOPROTOOPT
    _sockErrReadIgnore = [
     EAGAIN, EINTR, EWOULDBLOCK]
    _sockErrReadRefuse = [ECONNREFUSED]
from twisted.internet import base, defer, address
from twisted.python import log, failure
from twisted.internet import abstract, error, interfaces

@implementer(interfaces.IListeningPort, interfaces.IUDPTransport, interfaces.ISystemHandle)
class Port(base.BasePort):
    addressFamily = socket.AF_INET
    socketType = socket.SOCK_DGRAM
    maxThroughput = 262144
    _realPortNumber = None
    _preexistingSocket = None

    def __init__(self, port, proto, interface='', maxPacketSize=8192, reactor=None):
        base.BasePort.__init__(self, reactor)
        self.port = port
        self.protocol = proto
        self.maxPacketSize = maxPacketSize
        self.interface = interface
        self.setLogStr()
        self._connectedAddr = None
        self._setAddressFamily()
        return

    @classmethod
    def _fromListeningDescriptor(cls, reactor, fd, addressFamily, protocol, maxPacketSize):
        port = socket.fromfd(fd, addressFamily, cls.socketType)
        interface = port.getsockname()[0]
        self = cls(None, protocol, interface=interface, reactor=reactor, maxPacketSize=maxPacketSize)
        self._preexistingSocket = port
        return self

    def __repr__(self):
        if self._realPortNumber is not None:
            return '<%s on %s>' % (self.protocol.__class__, self._realPortNumber)
        else:
            return '<%s not connected>' % (self.protocol.__class__,)
            return

    def getHandle(self):
        return self.socket

    def startListening(self):
        self._bindSocket()
        self._connectToProtocol()

    def _bindSocket(self):
        if self._preexistingSocket is None:
            try:
                skt = self.createInternetSocket()
                skt.bind((self.interface, self.port))
            except socket.error as le:
                raise error.CannotListenError(self.interface, self.port, le)

        else:
            skt = self._preexistingSocket
            self._preexistingSocket = None
        self._realPortNumber = skt.getsockname()[1]
        log.msg('%s starting on %s' % (
         self._getLogPrefix(self.protocol), self._realPortNumber))
        self.connected = 1
        self.socket = skt
        self.fileno = self.socket.fileno
        return

    def _connectToProtocol(self):
        self.protocol.makeConnection(self)
        self.startReading()

    def doRead(self):
        read = 0
        while read < self.maxThroughput:
            try:
                data, addr = self.socket.recvfrom(self.maxPacketSize)
            except socket.error as se:
                no = se.args[0]
                if no in _sockErrReadIgnore:
                    return
                if no in _sockErrReadRefuse:
                    if self._connectedAddr:
                        self.protocol.connectionRefused()
                    return
                raise
            else:
                read += len(data)
                if self.addressFamily == socket.AF_INET6:
                    addr = addr[:2]
                try:
                    self.protocol.datagramReceived(data, addr)
                except:
                    log.err()

    def write(self, datagram, addr=None):
        if self._connectedAddr:
            try:
                return self.socket.send(datagram)
            except socket.error as se:
                no = se.args[0]
                if no == EINTR:
                    return self.write(datagram)
                if no == EMSGSIZE:
                    raise error.MessageLengthError('message too long')
                else:
                    if no == ECONNREFUSED:
                        self.protocol.connectionRefused()
                    else:
                        raise

        else:
            if not abstract.isIPAddress(addr[0]) and not abstract.isIPv6Address(addr[0]) and addr[0] != '<broadcast>':
                raise error.InvalidAddressError(addr[0], 'write() only accepts IP addresses, not hostnames')
            if (abstract.isIPAddress(addr[0]) or addr[0] == '<broadcast>') and self.addressFamily == socket.AF_INET6:
                raise error.InvalidAddressError(addr[0], 'IPv6 port write() called with IPv4 or broadcast address')
            if abstract.isIPv6Address(addr[0]) and self.addressFamily == socket.AF_INET:
                raise error.InvalidAddressError(addr[0], 'IPv4 port write() called with IPv6 address')
            try:
                return self.socket.sendto(datagram, addr)
            except socket.error as se:
                no = se.args[0]
                if no == EINTR:
                    return self.write(datagram, addr)
                if no == EMSGSIZE:
                    raise error.MessageLengthError('message too long')
                else:
                    if no == ECONNREFUSED:
                        return
                    raise

    def writeSequence(self, seq, addr):
        self.write(('').join(seq), addr)

    def connect(self, host, port):
        if self._connectedAddr:
            raise RuntimeError('already connected, reconnecting is not currently supported')
        if not abstract.isIPAddress(host) and not abstract.isIPv6Address(host):
            raise error.InvalidAddressError(host, 'not an IPv4 or IPv6 address.')
        self._connectedAddr = (
         host, port)
        self.socket.connect((host, port))

    def _loseConnection(self):
        self.stopReading()
        if self.connected:
            self.reactor.callLater(0, self.connectionLost)

    def stopListening(self):
        if self.connected:
            result = self.d = defer.Deferred()
        else:
            result = None
        self._loseConnection()
        return result

    def loseConnection(self):
        warnings.warn('Please use stopListening() to disconnect port', DeprecationWarning, stacklevel=2)
        self.stopListening()

    def connectionLost(self, reason=None):
        log.msg('(UDP Port %s Closed)' % self._realPortNumber)
        self._realPortNumber = None
        base.BasePort.connectionLost(self, reason)
        self.protocol.doStop()
        self.socket.close()
        del self.socket
        del self.fileno
        if hasattr(self, 'd'):
            self.d.callback(None)
            del self.d
        return

    def setLogStr(self):
        logPrefix = self._getLogPrefix(self.protocol)
        self.logstr = '%s (UDP)' % logPrefix

    def _setAddressFamily(self):
        if abstract.isIPv6Address(self.interface):
            self.addressFamily = socket.AF_INET6
        elif abstract.isIPAddress(self.interface):
            self.addressFamily = socket.AF_INET
        elif self.interface:
            raise error.InvalidAddressError(self.interface, 'not an IPv4 or IPv6 address.')

    def logPrefix(self):
        return self.logstr

    def getHost(self):
        addr = self.socket.getsockname()
        if self.addressFamily == socket.AF_INET:
            return address.IPv4Address('UDP', *addr)
        if self.addressFamily == socket.AF_INET6:
            return address.IPv6Address('UDP', *addr[:2])

    def setBroadcastAllowed(self, enabled):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, enabled)

    def getBroadcastAllowed(self):
        return operator.truth(self.socket.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST))


class MulticastMixin():

    def getOutgoingInterface(self):
        i = self.socket.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF)
        return socket.inet_ntoa(struct.pack('@i', i))

    def setOutgoingInterface(self, addr):
        return self.reactor.resolve(addr).addCallback(self._setInterface)

    def _setInterface(self, addr):
        i = socket.inet_aton(addr)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, i)
        return 1

    def getLoopbackMode(self):
        return self.socket.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP)

    def setLoopbackMode(self, mode):
        mode = struct.pack('b', operator.truth(mode))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, mode)

    def getTTL(self):
        return self.socket.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL)

    def setTTL(self, ttl):
        ttl = struct.pack('B', ttl)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def joinGroup(self, addr, interface=''):
        return self.reactor.resolve(addr).addCallback(self._joinAddr1, interface, 1)

    def _joinAddr1(self, addr, interface, join):
        return self.reactor.resolve(interface).addCallback(self._joinAddr2, addr, join)

    def _joinAddr2(self, interface, addr, join):
        addr = socket.inet_aton(addr)
        interface = socket.inet_aton(interface)
        if join:
            cmd = socket.IP_ADD_MEMBERSHIP
        else:
            cmd = socket.IP_DROP_MEMBERSHIP
        try:
            self.socket.setsockopt(socket.IPPROTO_IP, cmd, addr + interface)
        except socket.error as e:
            return failure.Failure(error.MulticastJoinError(addr, interface, *e.args))

    def leaveGroup(self, addr, interface=''):
        return self.reactor.resolve(addr).addCallback(self._joinAddr1, interface, 0)


@implementer(interfaces.IMulticastTransport)
class MulticastPort(MulticastMixin, Port):

    def __init__(self, port, proto, interface='', maxPacketSize=8192, reactor=None, listenMultiple=False):
        Port.__init__(self, port, proto, interface, maxPacketSize, reactor)
        self.listenMultiple = listenMultiple

    def createInternetSocket(self):
        skt = Port.createInternetSocket(self)
        if self.listenMultiple:
            skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if hasattr(socket, 'SO_REUSEPORT'):
                try:
                    skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
                except socket.error as le:
                    if le.errno == ENOPROTOOPT:
                        pass
                    else:
                        raise

        return skt
# okay decompiling out\twisted.internet.udp.pyc
