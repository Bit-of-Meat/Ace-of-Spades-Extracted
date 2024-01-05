# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.interfaces
from __future__ import division, absolute_import
from zope.interface import Interface, Attribute
from twisted.python import deprecate
from twisted.python.versions import Version

class IAddress(Interface):
    pass


class IConnector(Interface):

    def stopConnecting():
        pass

    def disconnect():
        pass

    def connect():
        pass

    def getDestination():
        pass


class IResolverSimple(Interface):

    def getHostByName(name, timeout=(1, 3, 11, 45)):
        pass


class IResolver(IResolverSimple):

    def query(query, timeout=None):
        pass

    def lookupAddress(name, timeout=None):
        pass

    def lookupAddress6(name, timeout=None):
        pass

    def lookupIPV6Address(name, timeout=None):
        pass

    def lookupMailExchange(name, timeout=None):
        pass

    def lookupNameservers(name, timeout=None):
        pass

    def lookupCanonicalName(name, timeout=None):
        pass

    def lookupMailBox(name, timeout=None):
        pass

    def lookupMailGroup(name, timeout=None):
        pass

    def lookupMailRename(name, timeout=None):
        pass

    def lookupPointer(name, timeout=None):
        pass

    def lookupAuthority(name, timeout=None):
        pass

    def lookupNull(name, timeout=None):
        pass

    def lookupWellKnownServices(name, timeout=None):
        pass

    def lookupHostInfo(name, timeout=None):
        pass

    def lookupMailboxInfo(name, timeout=None):
        pass

    def lookupText(name, timeout=None):
        pass

    def lookupResponsibility(name, timeout=None):
        pass

    def lookupAFSDatabase(name, timeout=None):
        pass

    def lookupService(name, timeout=None):
        pass

    def lookupAllRecords(name, timeout=None):
        pass

    def lookupSenderPolicy(name, timeout=10):
        pass

    def lookupNamingAuthorityPointer(name, timeout=None):
        pass

    def lookupZone(name, timeout=None):
        pass


class IReactorTCP(Interface):

    def listenTCP(port, factory, backlog=50, interface=''):
        pass

    def connectTCP(host, port, factory, timeout=30, bindAddress=None):
        pass


class IReactorSSL(Interface):

    def connectSSL(host, port, factory, contextFactory, timeout=30, bindAddress=None):
        pass

    def listenSSL(port, factory, contextFactory, backlog=50, interface=''):
        pass


class IReactorUNIX(Interface):

    def connectUNIX(address, factory, timeout=30, checkPID=0):
        pass

    def listenUNIX(address, factory, backlog=50, mode=438, wantPID=0):
        pass


class IReactorUNIXDatagram(Interface):

    def connectUNIXDatagram(address, protocol, maxPacketSize=8192, mode=438, bindAddress=None):
        pass

    def listenUNIXDatagram(address, protocol, maxPacketSize=8192, mode=438):
        pass


class IReactorWin32Events(Interface):

    def addEvent(event, fd, action):
        pass

    def removeEvent(event):
        pass


class IReactorUDP(Interface):

    def listenUDP(port, protocol, interface='', maxPacketSize=8192):
        pass


class IReactorMulticast(Interface):

    def listenMulticast(port, protocol, interface='', maxPacketSize=8192, listenMultiple=False):
        pass


class IReactorSocket(Interface):

    def adoptStreamPort(fileDescriptor, addressFamily, factory):
        pass

    def adoptStreamConnection(fileDescriptor, addressFamily, factory):
        pass

    def adoptDatagramPort(fileDescriptor, addressFamily, protocol, maxPacketSize=8192):
        pass


class IReactorProcess(Interface):

    def spawnProcess(processProtocol, executable, args=(), env={}, path=None, uid=None, gid=None, usePTY=0, childFDs=None):
        pass


class IReactorTime(Interface):

    def seconds():
        pass

    def callLater(delay, callable, *args, **kw):
        pass

    def getDelayedCalls():
        pass


class IDelayedCall(Interface):

    def getTime():
        pass

    def cancel():
        pass

    def delay(secondsLater):
        pass

    def reset(secondsFromNow):
        pass

    def active():
        pass


class IReactorFromThreads(Interface):

    def callFromThread(callable, *args, **kw):
        pass


class IReactorInThreads(Interface):

    def callInThread(callable, *args, **kwargs):
        pass


class IReactorThreads(IReactorFromThreads, IReactorInThreads):

    def getThreadPool():
        pass

    def suggestThreadPoolSize(size):
        pass


class IReactorCore(Interface):
    running = Attribute('A C{bool} which is C{True} from I{during startup} to I{during shutdown} and C{False} the rest of the time.')

    def resolve(name, timeout=10):
        pass

    def run():
        pass

    def stop():
        pass

    def crash():
        pass

    def iterate(delay=0):
        pass

    def fireSystemEvent(eventType):
        pass

    def addSystemEventTrigger(phase, eventType, callable, *args, **kw):
        pass

    def removeSystemEventTrigger(triggerID):
        pass

    def callWhenRunning(callable, *args, **kw):
        pass


class IReactorPluggableResolver(Interface):

    def installResolver(resolver):
        pass


class IReactorDaemonize(Interface):

    def beforeDaemonize():
        pass

    def afterDaemonize():
        pass


class IReactorFDSet(Interface):

    def addReader(reader):
        pass

    def addWriter(writer):
        pass

    def removeReader(reader):
        pass

    def removeWriter(writer):
        pass

    def removeAll():
        pass

    def getReaders():
        pass

    def getWriters():
        pass


class IListeningPort(Interface):

    def startListening():
        pass

    def stopListening():
        pass

    def getHost():
        pass


class ILoggingContext(Interface):

    def logPrefix():
        pass


class IFileDescriptor(ILoggingContext):

    def fileno():
        pass

    def connectionLost(reason):
        pass


class IReadDescriptor(IFileDescriptor):

    def doRead():
        pass


class IWriteDescriptor(IFileDescriptor):

    def doWrite():
        pass


class IReadWriteDescriptor(IReadDescriptor, IWriteDescriptor):
    pass


class IHalfCloseableDescriptor(Interface):

    def writeConnectionLost(reason):
        pass

    def readConnectionLost(reason):
        pass


class ISystemHandle(Interface):

    def getHandle():
        pass


class IConsumer(Interface):

    def registerProducer(producer, streaming):
        pass

    def unregisterProducer():
        pass

    def write(data):
        pass


class IProducer(Interface):

    def stopProducing():
        pass


class IPushProducer(IProducer):

    def pauseProducing():
        pass

    def resumeProducing():
        pass


class IPullProducer(IProducer):

    def resumeProducing():
        pass


class IProtocol(Interface):

    def dataReceived(data):
        pass

    def connectionLost(reason):
        pass

    def makeConnection(transport):
        pass

    def connectionMade():
        pass


class IProcessProtocol(Interface):

    def makeConnection(process):
        pass

    def childDataReceived(childFD, data):
        pass

    def childConnectionLost(childFD):
        pass

    def processExited(reason):
        pass

    def processEnded(reason):
        pass


class IHalfCloseableProtocol(Interface):

    def readConnectionLost():
        pass

    def writeConnectionLost():
        pass


class IFileDescriptorReceiver(Interface):

    def fileDescriptorReceived(descriptor):
        pass


class IProtocolFactory(Interface):

    def buildProtocol(addr):
        pass

    def doStart():
        pass

    def doStop():
        pass


class ITransport(Interface):

    def write(data):
        pass

    def writeSequence(data):
        pass

    def loseConnection():
        pass

    def getPeer():
        pass

    def getHost():
        pass


class ITCPTransport(ITransport):

    def loseWriteConnection():
        pass

    def abortConnection():
        pass

    def getTcpNoDelay():
        pass

    def setTcpNoDelay(enabled):
        pass

    def getTcpKeepAlive():
        pass

    def setTcpKeepAlive(enabled):
        pass

    def getHost():
        pass

    def getPeer():
        pass


class IUNIXTransport(ITransport):

    def sendFileDescriptor(descriptor):
        pass


class IOpenSSLServerConnectionCreator(Interface):

    def serverConnectionForTLS(tlsProtocol):
        pass


class IOpenSSLClientConnectionCreator(Interface):

    def clientConnectionForTLS(tlsProtocol):
        pass


class ITLSTransport(ITCPTransport):

    def startTLS(contextFactory):
        pass


class ISSLTransport(ITCPTransport):

    def getPeerCertificate():
        pass


class ICipher(Interface):
    fullName = Attribute('The fully qualified name of the cipher in L{unicode}.')


class IAcceptableCiphers(Interface):

    def selectCiphers(availableCiphers):
        pass


class IProcessTransport(ITransport):
    pid = Attribute('From before L{IProcessProtocol.makeConnection} is called to before L{IProcessProtocol.processEnded} is called, C{pid} is an L{int} giving the platform process ID of this process.  C{pid} is L{None} at all other times.')

    def closeStdin():
        pass

    def closeStdout():
        pass

    def closeStderr():
        pass

    def closeChildFD(descriptor):
        pass

    def writeToChild(childFD, data):
        pass

    def loseConnection():
        pass

    def signalProcess(signalID):
        pass


class IServiceCollection(Interface):

    def getServiceNamed(serviceName):
        pass

    def addService(service):
        pass

    def removeService(service):
        pass


class IUDPTransport(Interface):

    def write(packet, addr=None):
        pass

    def connect(host, port):
        pass

    def getHost():
        pass

    def stopListening():
        pass

    def setBroadcastAllowed(enabled):
        pass

    def getBroadcastAllowed():
        pass


class IUNIXDatagramTransport(Interface):

    def write(packet, address):
        pass

    def getHost():
        pass


class IUNIXDatagramConnectedTransport(Interface):

    def write(packet):
        pass

    def getHost():
        pass

    def getPeer():
        pass


class IMulticastTransport(Interface):

    def getOutgoingInterface():
        pass

    def setOutgoingInterface(addr):
        pass

    def getLoopbackMode():
        pass

    def setLoopbackMode(mode):
        pass

    def getTTL():
        pass

    def setTTL(ttl):
        pass

    def joinGroup(addr, interface=''):
        pass

    def leaveGroup(addr, interface=''):
        pass


class IStreamClientEndpoint(Interface):

    def connect(protocolFactory):
        pass


class IStreamServerEndpoint(Interface):

    def listen(protocolFactory):
        pass


class IStreamServerEndpointStringParser(Interface):
    prefix = Attribute('\n        @see: L{IStreamClientEndpointStringParser.prefix}\n        ')

    def parseStreamServer(reactor, *args, **kwargs):
        pass


class IStreamClientEndpointStringParser(Interface):
    prefix = Attribute('\n        A C{str}, the description prefix to respond to.  For example, an\n        L{IStreamClientEndpointStringParser} plugin which had C{"foo"} for its\n        C{prefix} attribute would be called for endpoint descriptions like\n        C{"foo:bar:baz"} or C{"foo:"}.\n        ')

    def parseStreamClient(*args, **kwargs):
        pass


deprecate.deprecatedModuleAttribute(Version('Twisted', 14, 0, 0), 'This interface has been superseded by IStreamClientEndpointStringParserWithReactor.', __name__, 'IStreamClientEndpointStringParser')

class IStreamClientEndpointStringParserWithReactor(Interface):
    prefix = Attribute('\n        L{bytes}, the description prefix to respond to.  For example, an\n        L{IStreamClientEndpointStringParserWithReactor} plugin which had\n        C{b"foo"} for its C{prefix} attribute would be called for endpoint\n        descriptions like C{b"foo:bar:baz"} or C{b"foo:"}.\n        ')

    def parseStreamClient(reactor, *args, **kwargs):
        pass
# okay decompiling out\twisted.internet.interfaces.pyc
