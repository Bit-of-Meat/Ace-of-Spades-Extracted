# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.unix
from __future__ import division, absolute_import
import os, stat, socket, struct
from errno import EINTR, EMSGSIZE, EAGAIN, EWOULDBLOCK, ECONNREFUSED, ENOBUFS
from zope.interface import implementer, implementer_only, implementedBy
if not hasattr(socket, 'AF_UNIX'):
    raise ImportError('UNIX sockets not supported on this platform')
from twisted.internet import main, base, tcp, udp, error, interfaces
from twisted.internet import protocol, address
from twisted.python import lockfile, log, reflect, failure
from twisted.python.filepath import _coerceToFilesystemEncoding
from twisted.python.util import untilConcludes
from twisted.python.compat import lazyByteSlice
try:
    from twisted.python import sendmsg
except ImportError:
    sendmsg = None

def _ancillaryDescriptor(fd):
    packed = struct.pack('i', fd)
    return [(socket.SOL_SOCKET, sendmsg.SCM_RIGHTS, packed)]


@implementer(interfaces.IUNIXTransport)
class _SendmsgMixin(object):
    _writeSomeDataBase = None
    _fileDescriptorBufferSize = 64

    def __init__(self):
        self._sendmsgQueue = []

    def _isSendBufferFull(self):
        return len(self._sendmsgQueue) > self._fileDescriptorBufferSize or self._writeSomeDataBase._isSendBufferFull(self)

    def sendFileDescriptor(self, fileno):
        self._sendmsgQueue.append(fileno)
        self._maybePauseProducer()
        self.startWriting()

    def writeSomeData(self, data):
        if len(self._sendmsgQueue) > len(data):
            return error.FileDescriptorOverrun()
        index = 0
        try:
            while index < len(self._sendmsgQueue):
                fd = self._sendmsgQueue[index]
                try:
                    untilConcludes(sendmsg.sendmsg, self.socket, data[index:index + 1], _ancillaryDescriptor(fd))
                except socket.error as se:
                    if se.args[0] in (EWOULDBLOCK, ENOBUFS):
                        return index
                    else:
                        return main.CONNECTION_LOST

                else:
                    index += 1

        finally:
            del self._sendmsgQueue[:index]

        limitedData = lazyByteSlice(data, index)
        result = self._writeSomeDataBase.writeSomeData(self, limitedData)
        try:
            return index + result
        except TypeError:
            return result

    def doRead(self):
        try:
            data, ancillary, flags = untilConcludes(sendmsg.recvmsg, self.socket, self.bufferSize)
        except socket.error as se:
            if se.args[0] == EWOULDBLOCK:
                return
            else:
                return main.CONNECTION_LOST

        if ancillary:
            fd = struct.unpack('i', ancillary[0][2])[0]
            if interfaces.IFileDescriptorReceiver.providedBy(self.protocol):
                self.protocol.fileDescriptorReceived(fd)
            else:
                log.msg(format='%(protocolName)s (on %(hostAddress)r) does not provide IFileDescriptorReceiver; closing file descriptor received (from %(peerAddress)r).', hostAddress=self.getHost(), peerAddress=self.getPeer(), protocolName=self._getLogPrefix(self.protocol))
                os.close(fd)
        return self._dataReceived(data)


class _UnsupportedSendmsgMixin(object):
    pass


if sendmsg:
    _SendmsgMixin = _SendmsgMixin
else:
    _SendmsgMixin = _UnsupportedSendmsgMixin

class Server(_SendmsgMixin, tcp.Server):
    _writeSomeDataBase = tcp.Server

    def __init__(self, sock, protocol, client, server, sessionno, reactor):
        _SendmsgMixin.__init__(self)
        tcp.Server.__init__(self, sock, protocol, (client, None), server, sessionno, reactor)
        return

    def getHost(self):
        return address.UNIXAddress(self.socket.getsockname())

    def getPeer(self):
        return address.UNIXAddress(self.hostname or None)


def _inFilesystemNamespace(path):
    return path[:1] not in ('\x00', '\x00')


class _UNIXPort(object):

    def getHost(self):
        return address.UNIXAddress(self.socket.getsockname())


class Port(_UNIXPort, tcp.Port):
    addressFamily = socket.AF_UNIX
    socketType = socket.SOCK_STREAM
    transport = Server
    lockFile = None

    def __init__(self, fileName, factory, backlog=50, mode=438, reactor=None, wantPID=0):
        tcp.Port.__init__(self, self._buildAddr(fileName).name, factory, backlog, reactor=reactor)
        self.mode = mode
        self.wantPID = wantPID

    def __repr__(self):
        factoryName = reflect.qual(self.factory.__class__)
        if hasattr(self, 'socket'):
            return '<%s on %r>' % (
             factoryName, _coerceToFilesystemEncoding('', self.port))
        else:
            return '<%s (not listening)>' % (factoryName,)

    def _buildAddr(self, name):
        return address.UNIXAddress(name)

    def startListening(self):
        log.msg('%s starting on %r' % (
         self._getLogPrefix(self.factory),
         _coerceToFilesystemEncoding('', self.port)))
        if self.wantPID:
            self.lockFile = lockfile.FilesystemLock(self.port + '.lock')
            if not self.lockFile.lock():
                raise error.CannotListenError(None, self.port, 'Cannot acquire lock')
            elif not self.lockFile.clean:
                try:
                    if stat.S_ISSOCK(os.stat(self.port).st_mode):
                        os.remove(self.port)
                except:
                    pass

        self.factory.doStart()
        try:
            skt = self.createInternetSocket()
            skt.bind(self.port)
        except socket.error as le:
            raise error.CannotListenError(None, self.port, le)
        else:
            if _inFilesystemNamespace(self.port):
                os.chmod(self.port, self.mode)
            skt.listen(self.backlog)
            self.connected = True
            self.socket = skt
            self.fileno = self.socket.fileno
            self.numberAccepts = 100
            self.startReading()

        return

    def _logConnectionLostMsg(self):
        log.msg('(UNIX Port %s Closed)' % _coerceToFilesystemEncoding('', self.port))

    def connectionLost(self, reason):
        if _inFilesystemNamespace(self.port):
            os.unlink(self.port)
        if self.lockFile is not None:
            self.lockFile.unlock()
        tcp.Port.connectionLost(self, reason)
        return


class Client(_SendmsgMixin, tcp.BaseClient):
    addressFamily = socket.AF_UNIX
    socketType = socket.SOCK_STREAM
    _writeSomeDataBase = tcp.BaseClient

    def __init__(self, filename, connector, reactor=None, checkPID=0):
        _SendmsgMixin.__init__(self)
        filename = address.UNIXAddress(filename).name
        self.connector = connector
        self.realAddress = self.addr = filename
        if checkPID and not lockfile.isLocked(filename + '.lock'):
            self._finishInit(None, None, error.BadFileError(filename), reactor)
        self._finishInit(self.doConnect, self.createInternetSocket(), None, reactor)
        return

    def getPeer(self):
        return address.UNIXAddress(self.addr)

    def getHost(self):
        return address.UNIXAddress(None)


class Connector(base.BaseConnector):

    def __init__(self, address, factory, timeout, reactor, checkPID):
        base.BaseConnector.__init__(self, factory, timeout, reactor)
        self.address = address
        self.checkPID = checkPID

    def _makeTransport(self):
        return Client(self.address, self, self.reactor, self.checkPID)

    def getDestination(self):
        return address.UNIXAddress(self.address)


@implementer(interfaces.IUNIXDatagramTransport)
class DatagramPort(_UNIXPort, udp.Port):
    addressFamily = socket.AF_UNIX

    def __init__(self, addr, proto, maxPacketSize=8192, mode=438, reactor=None):
        udp.Port.__init__(self, addr, proto, maxPacketSize=maxPacketSize, reactor=reactor)
        self.mode = mode

    def __repr__(self):
        protocolName = reflect.qual(self.protocol.__class__)
        if hasattr(self, 'socket'):
            return '<%s on %r>' % (protocolName, self.port)
        else:
            return '<%s (not listening)>' % (protocolName,)

    def _bindSocket(self):
        log.msg('%s starting on %s' % (self.protocol.__class__, repr(self.port)))
        try:
            skt = self.createInternetSocket()
            if self.port:
                skt.bind(self.port)
        except socket.error as le:
            raise error.CannotListenError(None, self.port, le)

        if self.port and _inFilesystemNamespace(self.port):
            os.chmod(self.port, self.mode)
        self.connected = 1
        self.socket = skt
        self.fileno = self.socket.fileno
        return

    def write(self, datagram, address):
        try:
            return self.socket.sendto(datagram, address)
        except socket.error as se:
            no = se.args[0]
            if no == EINTR:
                return self.write(datagram, address)
            if no == EMSGSIZE:
                raise error.MessageLengthError('message too long')
            else:
                if no == EAGAIN:
                    pass
                else:
                    raise

    def connectionLost(self, reason=None):
        log.msg('(Port %s Closed)' % repr(self.port))
        base.BasePort.connectionLost(self, reason)
        if hasattr(self, 'protocol'):
            self.protocol.doStop()
        self.connected = 0
        self.socket.close()
        del self.socket
        del self.fileno
        if hasattr(self, 'd'):
            self.d.callback(None)
            del self.d
        return

    def setLogStr(self):
        self.logstr = reflect.qual(self.protocol.__class__) + ' (UDP)'


@implementer_only(interfaces.IUNIXDatagramConnectedTransport, *implementedBy(base.BasePort))
class ConnectedDatagramPort(DatagramPort):

    def __init__(self, addr, proto, maxPacketSize=8192, mode=438, bindAddress=None, reactor=None):
        DatagramPort.__init__(self, bindAddress, proto, maxPacketSize, mode, reactor)
        self.remoteaddr = addr

    def startListening(self):
        try:
            self._bindSocket()
            self.socket.connect(self.remoteaddr)
            self._connectToProtocol()
        except:
            self.connectionFailed(failure.Failure())

    def connectionFailed(self, reason):
        self.stopListening()
        self.protocol.connectionFailed(reason)
        del self.protocol

    def doRead(self):
        read = 0
        while read < self.maxThroughput:
            try:
                data, addr = self.socket.recvfrom(self.maxPacketSize)
                read += len(data)
                self.protocol.datagramReceived(data)
            except socket.error as se:
                no = se.args[0]
                if no in (EAGAIN, EINTR, EWOULDBLOCK):
                    return
                if no == ECONNREFUSED:
                    self.protocol.connectionRefused()
                else:
                    raise
            except:
                log.deferr()

    def write(self, data):
        try:
            return self.socket.send(data)
        except socket.error as se:
            no = se.args[0]
            if no == EINTR:
                return self.write(data)
            if no == EMSGSIZE:
                raise error.MessageLengthError('message too long')
            elif no == ECONNREFUSED:
                self.protocol.connectionRefused()
            else:
                if no == EAGAIN:
                    pass
                else:
                    raise

    def getPeer(self):
        return address.UNIXAddress(self.remoteaddr)
# okay decompiling out\twisted.internet.unix.pyc
