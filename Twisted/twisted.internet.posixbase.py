# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.posixbase
from __future__ import division, absolute_import
import socket, errno, os, sys
from zope.interface import implementer, classImplements
from twisted.internet import error, udp, tcp
from twisted.internet.base import ReactorBase, _SignalReactorMixin
from twisted.internet.main import CONNECTION_DONE, CONNECTION_LOST
from twisted.internet.interfaces import IReactorUNIX, IReactorUNIXDatagram
from twisted.internet.interfaces import IReactorTCP, IReactorUDP, IReactorSSL
from twisted.internet.interfaces import IReactorSocket, IHalfCloseableDescriptor
from twisted.internet.interfaces import IReactorProcess, IReactorMulticast
from twisted.python import log, failure, util
from twisted.python.runtime import platformType, platform
_NO_FILENO = error.ConnectionFdescWentAway('Handler has no fileno method')
_NO_FILEDESC = error.ConnectionFdescWentAway('File descriptor lost')
try:
    from twisted.protocols import tls
except ImportError:
    tls = None
    try:
        from twisted.internet import ssl
    except ImportError:
        ssl = None

unixEnabled = platformType == 'posix'
processEnabled = False
if unixEnabled:
    from twisted.internet import fdesc, unix
    from twisted.internet import process, _signals
    processEnabled = True
if platform.isWindows():
    try:
        import win32process
        processEnabled = True
    except ImportError:
        win32process = None

class _SocketWaker(log.Logger):
    disconnected = 0

    def __init__(self, reactor):
        self.reactor = reactor
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        server.bind(('127.0.0.1', 0))
        server.listen(1)
        client.connect(server.getsockname())
        reader, clientaddr = server.accept()
        client.setblocking(0)
        reader.setblocking(0)
        self.r = reader
        self.w = client
        self.fileno = self.r.fileno

    def wakeUp(self):
        try:
            util.untilConcludes(self.w.send, 'x')
        except socket.error as e:
            if e.args[0] != errno.WSAEWOULDBLOCK:
                raise

    def doRead(self):
        try:
            self.r.recv(8192)
        except socket.error:
            pass

    def connectionLost(self, reason):
        self.r.close()
        self.w.close()


class _FDWaker(log.Logger, object):
    disconnected = 0
    i = None
    o = None

    def __init__(self, reactor):
        self.reactor = reactor
        self.i, self.o = os.pipe()
        fdesc.setNonBlocking(self.i)
        fdesc._setCloseOnExec(self.i)
        fdesc.setNonBlocking(self.o)
        fdesc._setCloseOnExec(self.o)
        self.fileno = lambda : self.i

    def doRead(self):
        fdesc.readFromFD(self.fileno(), (lambda data: None))

    def connectionLost(self, reason):
        if not hasattr(self, 'o'):
            return
        for fd in (self.i, self.o):
            try:
                os.close(fd)
            except IOError:
                pass

        del self.i
        del self.o


class _UnixWaker(_FDWaker):

    def wakeUp(self):
        if self.o is not None:
            try:
                util.untilConcludes(os.write, self.o, 'x')
            except OSError as e:
                if e.errno != errno.EAGAIN:
                    raise

        return


if platformType == 'posix':
    _Waker = _UnixWaker
else:
    _Waker = _SocketWaker

class _SIGCHLDWaker(_FDWaker):

    def __init__(self, reactor):
        _FDWaker.__init__(self, reactor)

    def install(self):
        _signals.installHandler(self.o)

    def uninstall(self):
        _signals.installHandler(-1)

    def doRead(self):
        _FDWaker.doRead(self)
        process.reapAllProcesses()


class _DisconnectSelectableMixin(object):

    def _disconnectSelectable(self, selectable, why, isRead, faildict={error.ConnectionDone: failure.Failure(error.ConnectionDone()), 
   error.ConnectionLost: failure.Failure(error.ConnectionLost())}):
        self.removeReader(selectable)
        f = faildict.get(why.__class__)
        if f:
            if isRead and why.__class__ == error.ConnectionDone and IHalfCloseableDescriptor.providedBy(selectable):
                selectable.readConnectionLost(f)
            else:
                self.removeWriter(selectable)
                selectable.connectionLost(f)
        else:
            self.removeWriter(selectable)
            selectable.connectionLost(failure.Failure(why))


@implementer(IReactorTCP, IReactorUDP, IReactorMulticast)
class PosixReactorBase(_SignalReactorMixin, _DisconnectSelectableMixin, ReactorBase):
    _wakerFactory = _Waker

    def installWaker(self):
        if not self.waker:
            self.waker = self._wakerFactory(self)
            self._internalReaders.add(self.waker)
            self.addReader(self.waker)

    _childWaker = None

    def _handleSignals(self):
        _SignalReactorMixin._handleSignals(self)
        if platformType == 'posix' and processEnabled:
            if not self._childWaker:
                self._childWaker = _SIGCHLDWaker(self)
                self._internalReaders.add(self._childWaker)
                self.addReader(self._childWaker)
            self._childWaker.install()
            process.reapAllProcesses()

    def _uninstallHandler(self):
        if self._childWaker:
            self._childWaker.uninstall()

    def spawnProcess(self, processProtocol, executable, args=(), env={}, path=None, uid=None, gid=None, usePTY=0, childFDs=None):
        args, env = self._checkProcessArgs(args, env)
        if platformType == 'posix':
            if usePTY:
                if childFDs is not None:
                    raise ValueError('Using childFDs is not supported with usePTY=True.')
                return process.PTYProcess(self, executable, args, env, path, processProtocol, uid, gid, usePTY)
            else:
                return process.Process(self, executable, args, env, path, processProtocol, uid, gid, childFDs)

        elif platformType == 'win32':
            if uid is not None:
                raise ValueError('Setting UID is unsupported on this platform.')
            if gid is not None:
                raise ValueError('Setting GID is unsupported on this platform.')
            if usePTY:
                raise ValueError('The usePTY parameter is not supported on Windows.')
            if childFDs:
                raise ValueError('Customizing childFDs is not supported on Windows.')
            if win32process:
                from twisted.internet._dumbwin32proc import Process
                return Process(self, processProtocol, executable, args, env, path)
            raise NotImplementedError('spawnProcess not available since pywin32 is not installed.')
        else:
            raise NotImplementedError('spawnProcess only available on Windows or POSIX.')
        return

    def listenUDP(self, port, protocol, interface='', maxPacketSize=8192):
        p = udp.Port(port, protocol, interface, maxPacketSize, self)
        p.startListening()
        return p

    def listenMulticast(self, port, protocol, interface='', maxPacketSize=8192, listenMultiple=False):
        p = udp.MulticastPort(port, protocol, interface, maxPacketSize, self, listenMultiple)
        p.startListening()
        return p

    def connectUNIX(self, address, factory, timeout=30, checkPID=0):
        c = unix.Connector(address, factory, timeout, self, checkPID)
        c.connect()
        return c

    def listenUNIX(self, address, factory, backlog=50, mode=438, wantPID=0):
        p = unix.Port(address, factory, backlog, mode, self, wantPID)
        p.startListening()
        return p

    def listenUNIXDatagram(self, address, protocol, maxPacketSize=8192, mode=438):
        p = unix.DatagramPort(address, protocol, maxPacketSize, mode, self)
        p.startListening()
        return p

    def connectUNIXDatagram(self, address, protocol, maxPacketSize=8192, mode=438, bindAddress=None):
        p = unix.ConnectedDatagramPort(address, protocol, maxPacketSize, mode, bindAddress, self)
        p.startListening()
        return p

    def adoptStreamPort(self, fileDescriptor, addressFamily, factory):
        if addressFamily not in (socket.AF_INET, socket.AF_INET6):
            raise error.UnsupportedAddressFamily(addressFamily)
        p = tcp.Port._fromListeningDescriptor(self, fileDescriptor, addressFamily, factory)
        p.startListening()
        return p

    def adoptStreamConnection(self, fileDescriptor, addressFamily, factory):
        if addressFamily not in (socket.AF_INET, socket.AF_INET6):
            raise error.UnsupportedAddressFamily(addressFamily)
        return tcp.Server._fromConnectedSocket(fileDescriptor, addressFamily, factory, self)

    def adoptDatagramPort(self, fileDescriptor, addressFamily, protocol, maxPacketSize=8192):
        if addressFamily not in (socket.AF_INET, socket.AF_INET6):
            raise error.UnsupportedAddressFamily(addressFamily)
        p = udp.Port._fromListeningDescriptor(self, fileDescriptor, addressFamily, protocol, maxPacketSize=maxPacketSize)
        p.startListening()
        return p

    def listenTCP(self, port, factory, backlog=50, interface=''):
        p = tcp.Port(port, factory, backlog, interface, self)
        p.startListening()
        return p

    def connectTCP(self, host, port, factory, timeout=30, bindAddress=None):
        c = tcp.Connector(host, port, factory, timeout, bindAddress, self)
        c.connect()
        return c

    def connectSSL(self, host, port, factory, contextFactory, timeout=30, bindAddress=None):
        if tls is not None:
            tlsFactory = tls.TLSMemoryBIOFactory(contextFactory, True, factory)
            return self.connectTCP(host, port, tlsFactory, timeout, bindAddress)
        else:
            if ssl is not None:
                c = ssl.Connector(host, port, factory, contextFactory, timeout, bindAddress, self)
                c.connect()
                return c
            return

    def listenSSL(self, port, factory, contextFactory, backlog=50, interface=''):
        if tls is not None:
            tlsFactory = tls.TLSMemoryBIOFactory(contextFactory, False, factory)
            port = self.listenTCP(port, tlsFactory, backlog, interface)
            port._type = 'TLS'
            return port
        else:
            if ssl is not None:
                p = ssl.Port(port, factory, contextFactory, backlog, interface, self)
                p.startListening()
                return p
            return

    def _removeAll(self, readers, writers):
        removedReaders = set(readers) - self._internalReaders
        for reader in removedReaders:
            self.removeReader(reader)

        removedWriters = set(writers)
        for writer in removedWriters:
            self.removeWriter(writer)

        return list(removedReaders | removedWriters)


class _PollLikeMixin(object):

    def _doReadOrWrite(self, selectable, fd, event):
        why = None
        inRead = False
        if event & self._POLL_DISCONNECTED and not event & self._POLL_IN:
            if fd in self._reads:
                inRead = True
                why = CONNECTION_DONE
            else:
                why = CONNECTION_LOST
        else:
            try:
                if selectable.fileno() == -1:
                    why = _NO_FILEDESC
                else:
                    if event & self._POLL_IN:
                        why = selectable.doRead()
                        inRead = True
                    if not why and event & self._POLL_OUT:
                        why = selectable.doWrite()
                        inRead = False
            except:
                why = sys.exc_info()[1]
                log.err()

        if why:
            self._disconnectSelectable(selectable, why, inRead)
        return


if tls is not None or ssl is not None:
    classImplements(PosixReactorBase, IReactorSSL)
if unixEnabled:
    classImplements(PosixReactorBase, IReactorUNIX, IReactorUNIXDatagram)
if processEnabled:
    classImplements(PosixReactorBase, IReactorProcess)
if getattr(socket, 'fromfd', None) is not None:
    classImplements(PosixReactorBase, IReactorSocket)
__all__ = ['PosixReactorBase']
# okay decompiling out\twisted.internet.posixbase.pyc
