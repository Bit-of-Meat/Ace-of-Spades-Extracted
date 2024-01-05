# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.spread.pb
import random, types
from hashlib import md5
from zope.interface import implementer, Interface
from twisted.python import log, failure, reflect
from twisted.internet import defer, protocol
from twisted.cred.portal import Portal
from twisted.cred.credentials import IAnonymous, ICredentials
from twisted.cred.credentials import IUsernameHashedPassword, Anonymous
from twisted.persisted import styles
from twisted.python.components import registerAdapter
from twisted.spread.interfaces import IJellyable, IUnjellyable
from twisted.spread.jelly import jelly, unjelly, globalSecurity
from twisted.spread import banana
from twisted.spread.flavors import Serializable
from twisted.spread.flavors import Referenceable, NoSuchMethod
from twisted.spread.flavors import Root, IPBRoot
from twisted.spread.flavors import ViewPoint
from twisted.spread.flavors import Viewable
from twisted.spread.flavors import Copyable
from twisted.spread.flavors import Jellyable
from twisted.spread.flavors import Cacheable
from twisted.spread.flavors import RemoteCopy
from twisted.spread.flavors import RemoteCache
from twisted.spread.flavors import RemoteCacheObserver
from twisted.spread.flavors import copyTags
from twisted.spread.flavors import setUnjellyableForClass
from twisted.spread.flavors import setUnjellyableFactoryForClass
from twisted.spread.flavors import setUnjellyableForClassTree
from twisted.spread.flavors import setCopierForClass
from twisted.spread.flavors import setFactoryForClass
from twisted.spread.flavors import setCopierForClassTree
MAX_BROKER_REFS = 1024
portno = 8787

class ProtocolError(Exception):
    pass


class DeadReferenceError(ProtocolError):
    pass


class Error(Exception):
    pass


class RemoteError(Exception):

    def __init__(self, remoteType, value, remoteTraceback):
        Exception.__init__(self, value)
        self.remoteType = remoteType
        self.remoteTraceback = remoteTraceback


class RemoteMethod():

    def __init__(self, obj, name):
        self.obj = obj
        self.name = name

    def __cmp__(self, other):
        return cmp((self.obj, self.name), other)

    def __hash__(self):
        return hash((self.obj, self.name))

    def __call__(self, *args, **kw):
        return self.obj.broker._sendMessage('', self.obj.perspective, self.obj.luid, self.name, args, kw)


class PBConnectionLost(Exception):
    pass


class IPerspective(Interface):

    def perspectiveMessageReceived(broker, message, args, kwargs):
        pass


@implementer(IPerspective)
class Avatar():

    def perspectiveMessageReceived(self, broker, message, args, kw):
        args = broker.unserialize(args, self)
        kw = broker.unserialize(kw, self)
        method = getattr(self, 'perspective_%s' % message)
        try:
            state = method(*args, **kw)
        except TypeError:
            log.msg("%s didn't accept %s and %s" % (method, args, kw))
            raise

        return broker.serialize(state, self, method, args, kw)


class AsReferenceable(Referenceable):

    def __init__(self, object, messageType='remote'):
        self.remoteMessageReceived = getattr(object, messageType + 'MessageReceived')


@implementer(IUnjellyable)
class RemoteReference(Serializable, styles.Ephemeral):

    def __init__(self, perspective, broker, luid, doRefCount):
        self.luid = luid
        self.broker = broker
        self.doRefCount = doRefCount
        self.perspective = perspective
        self.disconnectCallbacks = []

    def notifyOnDisconnect(self, callback):
        self.disconnectCallbacks.append(callback)
        if len(self.disconnectCallbacks) == 1:
            self.broker.notifyOnDisconnect(self._disconnected)

    def dontNotifyOnDisconnect(self, callback):
        self.disconnectCallbacks.remove(callback)
        if not self.disconnectCallbacks:
            self.broker.dontNotifyOnDisconnect(self._disconnected)

    def _disconnected(self):
        for callback in self.disconnectCallbacks:
            callback(self)

        self.disconnectCallbacks = None
        return

    def jellyFor(self, jellier):
        if jellier.invoker:
            return (
             'local', self.luid)
        else:
            return ('unpersistable', 'References cannot be serialized')

    def unjellyFor(self, unjellier, unjellyList):
        self.__init__(unjellier.invoker.unserializingPerspective, unjellier.invoker, unjellyList[1], 1)
        return self

    def callRemote(self, _name, *args, **kw):
        return self.broker._sendMessage('', self.perspective, self.luid, _name, args, kw)

    def remoteMethod(self, key):
        return RemoteMethod(self, key)

    def __cmp__(self, other):
        if isinstance(other, RemoteReference):
            if other.broker == self.broker:
                return cmp(self.luid, other.luid)
        return cmp(self.broker, other)

    def __hash__(self):
        return self.luid

    def __del__(self):
        if self.doRefCount:
            self.broker.sendDecRef(self.luid)


setUnjellyableForClass('remote', RemoteReference)

class Local():

    def __init__(self, object, perspective=None):
        self.object = object
        self.perspective = perspective
        self.refcount = 1

    def __repr__(self):
        return '<pb.Local %r ref:%s>' % (self.object, self.refcount)

    def incref(self):
        self.refcount = self.refcount + 1
        return self.refcount

    def decref(self):
        self.refcount = self.refcount - 1
        return self.refcount


class CopyableFailure(failure.Failure, Copyable):
    unsafeTracebacks = 0

    def getStateToCopy(self):
        state = self.__dict__.copy()
        state['tb'] = None
        state['frames'] = []
        state['stack'] = []
        state['value'] = str(self.value)
        if isinstance(self.type, str):
            state['type'] = self.type
        else:
            state['type'] = reflect.qual(self.type)
        if self.unsafeTracebacks:
            state['traceback'] = self.getTraceback()
        else:
            state['traceback'] = 'Traceback unavailable\n'
        return state


class CopiedFailure(RemoteCopy, failure.Failure):

    def printTraceback(self, file=None, elideFrameworkCode=0, detail='default'):
        if file is None:
            file = log.logfile
        file.write('Traceback from remote host -- ')
        file.write(self.traceback)
        file.write(self.type + ': ' + self.value)
        file.write('\n')
        return

    def throwExceptionIntoGenerator(self, g):
        return g.throw(RemoteError(self.type, self.value, self.traceback))

    printBriefTraceback = printTraceback
    printDetailedTraceback = printTraceback


setUnjellyableForClass(CopyableFailure, CopiedFailure)

def failure2Copyable(fail, unsafeTracebacks=0):
    f = types.InstanceType(CopyableFailure, fail.__dict__)
    f.unsafeTracebacks = unsafeTracebacks
    return f


class Broker(banana.Banana):
    version = 6
    username = None
    factory = None

    def __init__(self, isClient=1, security=globalSecurity):
        banana.Banana.__init__(self, isClient)
        self.disconnected = 0
        self.disconnects = []
        self.failures = []
        self.connects = []
        self.localObjects = {}
        self.security = security
        self.pageProducers = []
        self.currentRequestID = 0
        self.currentLocalID = 0
        self.unserializingPerspective = None
        self.luids = {}
        self.remotelyCachedObjects = {}
        self.remotelyCachedLUIDs = {}
        self.locallyCachedObjects = {}
        self.waitingForAnswers = {}
        self._localCleanup = {}
        return

    def resumeProducing(self):
        for pageridx in xrange(len(self.pageProducers) - 1, -1, -1):
            pager = self.pageProducers[pageridx]
            pager.sendNextPage()
            if not pager.stillPaging():
                del self.pageProducers[pageridx]

        if not self.pageProducers:
            self.transport.unregisterProducer()

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass

    def registerPageProducer(self, pager):
        self.pageProducers.append(pager)
        if len(self.pageProducers) == 1:
            self.transport.registerProducer(self, 0)

    def expressionReceived(self, sexp):
        if isinstance(sexp, types.ListType):
            command = sexp[0]
            methodName = 'proto_%s' % command
            method = getattr(self, methodName, None)
            if method:
                method(*sexp[1:])
            else:
                self.sendCall('didNotUnderstand', command)
        else:
            raise ProtocolError('Non-list expression received.')
        return

    def proto_version(self, vnum):
        if vnum != self.version:
            raise ProtocolError('Version Incompatibility: %s %s' % (self.version, vnum))

    def sendCall(self, *exp):
        self.sendEncoded(exp)

    def proto_didNotUnderstand(self, command):
        log.msg("Didn't understand command: %r" % command)

    def connectionReady(self):
        self.sendCall('version', self.version)
        for notifier in self.connects:
            try:
                notifier()
            except:
                log.deferr()

        self.connects = None
        if self.factory:
            self.factory.clientConnectionMade(self)
        return

    def connectionFailed(self):
        for notifier in self.failures:
            try:
                notifier()
            except:
                log.deferr()

        self.failures = None
        return

    waitingForAnswers = None

    def connectionLost(self, reason):
        self.disconnected = 1
        self.luids = None
        if self.waitingForAnswers:
            for d in self.waitingForAnswers.values():
                try:
                    d.errback(failure.Failure(PBConnectionLost(reason)))
                except:
                    log.deferr()

        for lobj in self.remotelyCachedObjects.values():
            cacheable = lobj.object
            perspective = lobj.perspective
            try:
                cacheable.stoppedObserving(perspective, RemoteCacheObserver(self, cacheable, perspective))
            except:
                log.deferr()

        for notifier in self.disconnects[:]:
            try:
                notifier()
            except:
                log.deferr()

        self.disconnects = None
        self.waitingForAnswers = None
        self.localSecurity = None
        self.remoteSecurity = None
        self.remotelyCachedObjects = None
        self.remotelyCachedLUIDs = None
        self.locallyCachedObjects = None
        self.localObjects = None
        return

    def notifyOnDisconnect(self, notifier):
        self.disconnects.append(notifier)

    def notifyOnFail(self, notifier):
        self.failures.append(notifier)

    def notifyOnConnect(self, notifier):
        if self.connects is None:
            try:
                notifier()
            except:
                log.err()

        else:
            self.connects.append(notifier)
        return

    def dontNotifyOnDisconnect(self, notifier):
        try:
            self.disconnects.remove(notifier)
        except ValueError:
            pass

    def localObjectForID(self, luid):
        lob = self.localObjects.get(luid)
        if lob is None:
            return
        else:
            return lob.object

    maxBrokerRefsViolations = 0

    def registerReference(self, object):
        puid = object.processUniqueID()
        luid = self.luids.get(puid)
        if luid is None:
            if len(self.localObjects) > MAX_BROKER_REFS:
                self.maxBrokerRefsViolations = self.maxBrokerRefsViolations + 1
                if self.maxBrokerRefsViolations > 3:
                    self.transport.loseConnection()
                    raise Error('Maximum PB reference count exceeded.  Goodbye.')
                raise Error('Maximum PB reference count exceeded.')
            luid = self.newLocalID()
            self.localObjects[luid] = Local(object)
            self.luids[puid] = luid
        else:
            self.localObjects[luid].incref()
        return luid

    def setNameForLocal(self, name, object):
        self.localObjects[name] = Local(object)

    def remoteForName(self, name):
        return RemoteReference(None, self, name, 0)

    def cachedRemotelyAs(self, instance, incref=0):
        puid = instance.processUniqueID()
        luid = self.remotelyCachedLUIDs.get(puid)
        if luid is not None and incref:
            self.remotelyCachedObjects[luid].incref()
        return luid

    def remotelyCachedForLUID(self, luid):
        return self.remotelyCachedObjects[luid].object

    def cacheRemotely(self, instance):
        puid = instance.processUniqueID()
        luid = self.newLocalID()
        if len(self.remotelyCachedObjects) > MAX_BROKER_REFS:
            self.maxBrokerRefsViolations = self.maxBrokerRefsViolations + 1
            if self.maxBrokerRefsViolations > 3:
                self.transport.loseConnection()
                raise Error('Maximum PB cache count exceeded.  Goodbye.')
            raise Error('Maximum PB cache count exceeded.')
        self.remotelyCachedLUIDs[puid] = luid
        self.remotelyCachedObjects[luid] = Local(instance, self.serializingPerspective)
        return luid

    def cacheLocally(self, cid, instance):
        self.locallyCachedObjects[cid] = instance

    def cachedLocallyAs(self, cid):
        instance = self.locallyCachedObjects[cid]
        return instance

    def serialize(self, object, perspective=None, method=None, args=None, kw=None):
        if isinstance(object, defer.Deferred):
            object.addCallbacks(self.serialize, (lambda x: x), callbackKeywords={'perspective': perspective, 
               'method': method, 
               'args': args, 
               'kw': kw})
            return object
        else:
            self.serializingPerspective = perspective
            self.jellyMethod = method
            self.jellyArgs = args
            self.jellyKw = kw
            try:
                return jelly(object, self.security, None, self)
            finally:
                self.serializingPerspective = None
                self.jellyMethod = None
                self.jellyArgs = None
                self.jellyKw = None

            return

    def unserialize(self, sexp, perspective=None):
        self.unserializingPerspective = perspective
        try:
            return unjelly(sexp, self.security, None, self)
        finally:
            self.unserializingPerspective = None

        return

    def newLocalID(self):
        self.currentLocalID = self.currentLocalID + 1
        return self.currentLocalID

    def newRequestID(self):
        self.currentRequestID = self.currentRequestID + 1
        return self.currentRequestID

    def _sendMessage(self, prefix, perspective, objectID, message, args, kw):
        pbc = None
        pbe = None
        answerRequired = 1
        if 'pbcallback' in kw:
            pbc = kw['pbcallback']
            del kw['pbcallback']
        if 'pberrback' in kw:
            pbe = kw['pberrback']
            del kw['pberrback']
        if 'pbanswer' in kw:
            answerRequired = kw['pbanswer']
            del kw['pbanswer']
        if self.disconnected:
            raise DeadReferenceError('Calling Stale Broker')
        try:
            netArgs = self.serialize(args, perspective=perspective, method=message)
            netKw = self.serialize(kw, perspective=perspective, method=message)
        except:
            return defer.fail(failure.Failure())

        requestID = self.newRequestID()
        if answerRequired:
            rval = defer.Deferred()
            self.waitingForAnswers[requestID] = rval
            if pbc or pbe:
                log.msg('warning! using deprecated "pbcallback"')
                rval.addCallbacks(pbc, pbe)
        else:
            rval = None
        self.sendCall(prefix + 'message', requestID, objectID, message, answerRequired, netArgs, netKw)
        return rval

    def proto_message(self, requestID, objectID, message, answerRequired, netArgs, netKw):
        self._recvMessage(self.localObjectForID, requestID, objectID, message, answerRequired, netArgs, netKw)

    def proto_cachemessage(self, requestID, objectID, message, answerRequired, netArgs, netKw):
        self._recvMessage(self.cachedLocallyAs, requestID, objectID, message, answerRequired, netArgs, netKw)

    def _recvMessage(self, findObjMethod, requestID, objectID, message, answerRequired, netArgs, netKw):
        try:
            object = findObjMethod(objectID)
            if object is None:
                raise Error('Invalid Object ID')
            netResult = object.remoteMessageReceived(self, message, netArgs, netKw)
        except Error as e:
            if answerRequired:
                if isinstance(e, Jellyable) or self.security.isClassAllowed(e.__class__):
                    self._sendError(e, requestID)
                else:
                    self._sendError(CopyableFailure(e), requestID)
        except:
            if answerRequired:
                log.msg('Peer will receive following PB traceback:', isError=True)
                f = CopyableFailure()
                self._sendError(f, requestID)
            log.err()

        if answerRequired:
            if isinstance(netResult, defer.Deferred):
                args = (
                 requestID,)
                netResult.addCallbacks(self._sendAnswer, self._sendFailureOrError, callbackArgs=args, errbackArgs=args)
            else:
                self._sendAnswer(netResult, requestID)
        return

    def _sendAnswer(self, netResult, requestID):
        self.sendCall('answer', requestID, netResult)

    def proto_answer(self, requestID, netResult):
        d = self.waitingForAnswers[requestID]
        del self.waitingForAnswers[requestID]
        d.callback(self.unserialize(netResult))

    def _sendFailureOrError(self, fail, requestID):
        if fail.check(Error) is None:
            self._sendFailure(fail, requestID)
        else:
            self._sendError(fail, requestID)
        return

    def _sendFailure(self, fail, requestID):
        log.msg('Peer will receive following PB traceback:')
        log.err(fail)
        self._sendError(fail, requestID)

    def _sendError(self, fail, requestID):
        if isinstance(fail, failure.Failure):
            if isinstance(fail.value, Jellyable) or self.security.isClassAllowed(fail.value.__class__):
                fail = fail.value
            elif not isinstance(fail, CopyableFailure):
                fail = failure2Copyable(fail, self.factory.unsafeTracebacks)
        if isinstance(fail, CopyableFailure):
            fail.unsafeTracebacks = self.factory.unsafeTracebacks
        self.sendCall('error', requestID, self.serialize(fail))

    def proto_error(self, requestID, fail):
        d = self.waitingForAnswers[requestID]
        del self.waitingForAnswers[requestID]
        d.errback(self.unserialize(fail))

    def sendDecRef(self, objectID):
        self.sendCall('decref', objectID)

    def proto_decref(self, objectID):
        refs = self.localObjects[objectID].decref()
        if refs == 0:
            puid = self.localObjects[objectID].object.processUniqueID()
            del self.luids[puid]
            del self.localObjects[objectID]
            self._localCleanup.pop(puid, (lambda : None))()

    def decCacheRef(self, objectID):
        self.sendCall('decache', objectID)

    def proto_decache(self, objectID):
        refs = self.remotelyCachedObjects[objectID].decref()
        if refs == 0:
            lobj = self.remotelyCachedObjects[objectID]
            cacheable = lobj.object
            perspective = lobj.perspective
            try:
                cacheable.stoppedObserving(perspective, RemoteCacheObserver(self, cacheable, perspective))
            except:
                log.deferr()

            puid = cacheable.processUniqueID()
            del self.remotelyCachedLUIDs[puid]
            del self.remotelyCachedObjects[objectID]
            self.sendCall('uncache', objectID)

    def proto_uncache(self, objectID):
        obj = self.locallyCachedObjects[objectID]
        obj.broker = None
        del self.locallyCachedObjects[objectID]
        return


def respond(challenge, password):
    m = md5()
    m.update(password)
    hashedPassword = m.digest()
    m = md5()
    m.update(hashedPassword)
    m.update(challenge)
    doubleHashedPassword = m.digest()
    return doubleHashedPassword


def challenge():
    crap = ''
    for x in range(random.randrange(15, 25)):
        crap = crap + chr(random.randint(65, 90))

    crap = md5(crap).digest()
    return crap


class PBClientFactory(protocol.ClientFactory):
    protocol = Broker
    unsafeTracebacks = False

    def __init__(self, unsafeTracebacks=False, security=globalSecurity):
        self.unsafeTracebacks = unsafeTracebacks
        self.security = security
        self._reset()

    def buildProtocol(self, addr):
        p = self.protocol(isClient=True, security=self.security)
        p.factory = self
        return p

    def _reset(self):
        self.rootObjectRequests = []
        self._broker = None
        self._root = None
        return

    def _failAll(self, reason):
        deferreds = self.rootObjectRequests
        self._reset()
        for d in deferreds:
            d.errback(reason)

    def clientConnectionFailed(self, connector, reason):
        self._failAll(reason)

    def clientConnectionLost(self, connector, reason, reconnecting=0):
        if reconnecting:
            self._broker = None
            self._root = None
        else:
            self._failAll(reason)
        return

    def clientConnectionMade(self, broker):
        self._broker = broker
        self._root = broker.remoteForName('root')
        ds = self.rootObjectRequests
        self.rootObjectRequests = []
        for d in ds:
            d.callback(self._root)

    def getRootObject(self):
        if self._broker and not self._broker.disconnected:
            return defer.succeed(self._root)
        d = defer.Deferred()
        self.rootObjectRequests.append(d)
        return d

    def disconnect(self):
        if self._broker:
            self._broker.transport.loseConnection()

    def _cbSendUsername(self, root, username, password, client):
        return root.callRemote('login', username).addCallback(self._cbResponse, password, client)

    def _cbResponse(self, (challenge, challenger), password, client):
        return challenger.callRemote('respond', respond(challenge, password), client)

    def _cbLoginAnonymous(self, root, client):
        return root.callRemote('loginAnonymous', client)

    def login(self, credentials, client=None):
        d = self.getRootObject()
        if IAnonymous.providedBy(credentials):
            d.addCallback(self._cbLoginAnonymous, client)
        else:
            d.addCallback(self._cbSendUsername, credentials.username, credentials.password, client)
        return d


class PBServerFactory(protocol.ServerFactory):
    unsafeTracebacks = False
    protocol = Broker

    def __init__(self, root, unsafeTracebacks=False, security=globalSecurity):
        self.root = IPBRoot(root)
        self.unsafeTracebacks = unsafeTracebacks
        self.security = security

    def buildProtocol(self, addr):
        proto = self.protocol(isClient=False, security=self.security)
        proto.factory = self
        proto.setNameForLocal('root', self.root.rootObject(proto))
        return proto

    def clientConnectionMade(self, protocol):
        pass


class IUsernameMD5Password(ICredentials):

    def checkPassword(password):
        pass

    def checkMD5Password(password):
        pass


@implementer(IPBRoot)
class _PortalRoot():

    def __init__(self, portal):
        self.portal = portal

    def rootObject(self, broker):
        return _PortalWrapper(self.portal, broker)


registerAdapter(_PortalRoot, Portal, IPBRoot)

class _JellyableAvatarMixin():

    def _cbLogin(self, (interface, avatar, logout)):
        if not IJellyable.providedBy(avatar):
            avatar = AsReferenceable(avatar, 'perspective')
        puid = avatar.processUniqueID()
        logout = [
         logout]

        def maybeLogout():
            if not logout:
                return
            fn = logout[0]
            del logout[0]
            fn()

        self.broker._localCleanup[puid] = maybeLogout
        self.broker.notifyOnDisconnect(maybeLogout)
        return avatar


class _PortalWrapper(Referenceable, _JellyableAvatarMixin):

    def __init__(self, portal, broker):
        self.portal = portal
        self.broker = broker

    def remote_login(self, username):
        c = challenge()
        return (c, _PortalAuthChallenger(self.portal, self.broker, username, c))

    def remote_loginAnonymous(self, mind):
        d = self.portal.login(Anonymous(), mind, IPerspective)
        d.addCallback(self._cbLogin)
        return d


@implementer(IUsernameHashedPassword, IUsernameMD5Password)
class _PortalAuthChallenger(Referenceable, _JellyableAvatarMixin):

    def __init__(self, portal, broker, username, challenge):
        self.portal = portal
        self.broker = broker
        self.username = username
        self.challenge = challenge

    def remote_respond(self, response, mind):
        self.response = response
        d = self.portal.login(self, mind, IPerspective)
        d.addCallback(self._cbLogin)
        return d

    def checkPassword(self, password):
        return self.checkMD5Password(md5(password).digest())

    def checkMD5Password(self, md5Password):
        md = md5()
        md.update(md5Password)
        md.update(self.challenge)
        correct = md.digest()
        return self.response == correct


__all__ = [
 'IPBRoot', 'Serializable', 'Referenceable', 'NoSuchMethod', 'Root', 
 'ViewPoint', 
 'Viewable', 'Copyable', 'Jellyable', 'Cacheable', 
 'RemoteCopy', 'RemoteCache', 
 'RemoteCacheObserver', 'copyTags', 
 'setUnjellyableForClass', 'setUnjellyableFactoryForClass', 
 'setUnjellyableForClassTree', 
 'setCopierForClass', 
 'setFactoryForClass', 'setCopierForClassTree', 
 'MAX_BROKER_REFS', 'portno', 
 'ProtocolError', 
 'DeadReferenceError', 'Error', 'PBConnectionLost', 
 'RemoteMethod', 'IPerspective', 
 'Avatar', 'AsReferenceable', 
 'RemoteReference', 'CopyableFailure', 'CopiedFailure', 
 'failure2Copyable', 
 'Broker', 'respond', 'challenge', 'PBClientFactory', 
 'PBServerFactory', 
 'IUsernameMD5Password']
# okay decompiling out\twisted.spread.pb.pyc
