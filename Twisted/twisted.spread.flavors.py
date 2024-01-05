# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.spread.flavors
import sys
from zope.interface import implementer, Interface
from twisted.python import log, reflect
from jelly import setUnjellyableForClass, setUnjellyableForClassTree, setUnjellyableFactoryForClass, unjellyableRegistry
from jelly import Jellyable, Unjellyable, _newDummyLike
from jelly import setInstanceState, getInstanceState
setCopierForClass = setUnjellyableForClass
setCopierForClassTree = setUnjellyableForClassTree
setFactoryForClass = setUnjellyableFactoryForClass
copyTags = unjellyableRegistry
copy_atom = 'copy'
cache_atom = 'cache'
cached_atom = 'cached'
remote_atom = 'remote'

class NoSuchMethod(AttributeError):
    pass


class IPBRoot(Interface):

    def rootObject(broker):
        pass


class Serializable(Jellyable):

    def processUniqueID(self):
        return id(self)


class Referenceable(Serializable):
    perspective = None

    def remoteMessageReceived(self, broker, message, args, kw):
        args = broker.unserialize(args)
        kw = broker.unserialize(kw)
        method = getattr(self, 'remote_%s' % message, None)
        if method is None:
            raise NoSuchMethod('No such method: remote_%s' % (message,))
        try:
            state = method(*args, **kw)
        except TypeError:
            log.msg("%s didn't accept %s and %s" % (method, args, kw))
            raise

        return broker.serialize(state, self.perspective)

    def jellyFor(self, jellier):
        return [
         'remote', jellier.invoker.registerReference(self)]


@implementer(IPBRoot)
class Root(Referenceable):

    def rootObject(self, broker):
        return self


class ViewPoint(Referenceable):

    def __init__(self, perspective, object):
        self.perspective = perspective
        self.object = object

    def processUniqueID(self):
        return (
         id(self.perspective), id(self.object))

    def remoteMessageReceived(self, broker, message, args, kw):
        args = broker.unserialize(args, self.perspective)
        kw = broker.unserialize(kw, self.perspective)
        method = getattr(self.object, 'view_%s' % message)
        try:
            state = method(*((self.perspective,) + args), **kw)
        except TypeError:
            log.msg("%s didn't accept %s and %s" % (method, args, kw))
            raise

        rv = broker.serialize(state, self.perspective, method, args, kw)
        return rv


class Viewable(Serializable):

    def jellyFor(self, jellier):
        return ViewPoint(jellier.invoker.serializingPerspective, self).jellyFor(jellier)


class Copyable(Serializable):

    def getStateToCopy(self):
        return self.__dict__

    def getStateToCopyFor(self, perspective):
        return self.getStateToCopy()

    def getTypeToCopy(self):
        return reflect.qual(self.__class__)

    def getTypeToCopyFor(self, perspective):
        return self.getTypeToCopy()

    def jellyFor(self, jellier):
        if jellier.invoker is None:
            return getInstanceState(self, jellier)
        else:
            p = jellier.invoker.serializingPerspective
            t = self.getTypeToCopyFor(p)
            state = self.getStateToCopyFor(p)
            sxp = jellier.prepare(self)
            sxp.extend([t, jellier.jelly(state)])
            return jellier.preserve(self, sxp)


class Cacheable(Copyable):

    def getStateToCacheAndObserveFor(self, perspective, observer):
        return self.getStateToCopyFor(perspective)

    def jellyFor(self, jellier):
        if jellier.invoker is None:
            return getInstanceState(self, jellier)
        else:
            luid = jellier.invoker.cachedRemotelyAs(self, 1)
            if luid is None:
                luid = jellier.invoker.cacheRemotely(self)
                p = jellier.invoker.serializingPerspective
                type_ = self.getTypeToCopyFor(p)
                observer = RemoteCacheObserver(jellier.invoker, self, p)
                state = self.getStateToCacheAndObserveFor(p, observer)
                l = jellier.prepare(self)
                jstate = jellier.jelly(state)
                l.extend([type_, luid, jstate])
                return jellier.preserve(self, l)
            return (cached_atom, luid)
            return

    def stoppedObserving(self, perspective, observer):
        pass


class RemoteCopy(Unjellyable):

    def setCopyableState(self, state):
        self.__dict__ = state

    def unjellyFor(self, unjellier, jellyList):
        if unjellier.invoker is None:
            return setInstanceState(self, unjellier, jellyList)
        else:
            self.setCopyableState(unjellier.unjelly(jellyList[1]))
            return self


class RemoteCache(RemoteCopy, Serializable):

    def remoteMessageReceived(self, broker, message, args, kw):
        args = broker.unserialize(args)
        kw = broker.unserialize(kw)
        method = getattr(self, 'observe_%s' % message)
        try:
            state = method(*args, **kw)
        except TypeError:
            log.msg("%s didn't accept %s and %s" % (method, args, kw))
            raise

        return broker.serialize(state, None, method, args, kw)

    def jellyFor(self, jellier):
        if jellier.invoker is None:
            return getInstanceState(self, jellier)
        else:
            return (
             'lcache', self.luid)

    def unjellyFor(self, unjellier, jellyList):
        if unjellier.invoker is None:
            return setInstanceState(self, unjellier, jellyList)
        else:
            self.broker = unjellier.invoker
            self.luid = jellyList[1]
            cProxy = _newDummyLike(self)
            init = getattr(cProxy, '__init__', None)
            if init:
                init()
            unjellier.invoker.cacheLocally(jellyList[1], self)
            cProxy.setCopyableState(unjellier.unjelly(jellyList[2]))
            self.__dict__ = cProxy.__dict__
            self.broker = unjellier.invoker
            self.luid = jellyList[1]
            return cProxy

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(id(self.__dict__), id(other.__dict__))
        else:
            return cmp(id(self.__dict__), other)

    def __hash__(self):
        return int(id(self.__dict__) % sys.maxint)

    broker = None
    luid = None

    def __del__(self):
        try:
            if self.broker:
                self.broker.decCacheRef(self.luid)
        except:
            log.deferr()


def unjellyCached(unjellier, unjellyList):
    luid = unjellyList[1]
    cNotProxy = unjellier.invoker.cachedLocallyAs(luid)
    cProxy = _newDummyLike(cNotProxy)
    return cProxy


setUnjellyableForClass('cached', unjellyCached)

def unjellyLCache(unjellier, unjellyList):
    luid = unjellyList[1]
    obj = unjellier.invoker.remotelyCachedForLUID(luid)
    return obj


setUnjellyableForClass('lcache', unjellyLCache)

def unjellyLocal(unjellier, unjellyList):
    obj = unjellier.invoker.localObjectForID(unjellyList[1])
    return obj


setUnjellyableForClass('local', unjellyLocal)

class RemoteCacheMethod:

    def __init__(self, name, broker, cached, perspective):
        self.name = name
        self.broker = broker
        self.perspective = perspective
        self.cached = cached

    def __cmp__(self, other):
        return cmp((self.name, self.broker, self.perspective, self.cached), other)

    def __hash__(self):
        return hash((self.name, self.broker, self.perspective, self.cached))

    def __call__(self, *args, **kw):
        cacheID = self.broker.cachedRemotelyAs(self.cached)
        if cacheID is None:
            from pb import ProtocolError
            raise ProtocolError("You can't call a cached method when the object hasn't been given to the peer yet.")
        return self.broker._sendMessage('cache', self.perspective, cacheID, self.name, args, kw)


class RemoteCacheObserver:

    def __init__(self, broker, cached, perspective):
        self.broker = broker
        self.cached = cached
        self.perspective = perspective

    def __repr__(self):
        return '<RemoteCacheObserver(%s, %s, %s) at %s>' % (
         self.broker, self.cached, self.perspective, id(self))

    def __hash__(self):
        return hash(self.broker) % 1024 + hash(self.perspective) % 1024 + hash(self.cached) % 1024

    def __cmp__(self, other):
        return cmp((self.broker, self.perspective, self.cached), other)

    def callRemote(self, _name, *args, **kw):
        cacheID = self.broker.cachedRemotelyAs(self.cached)
        if cacheID is None:
            from pb import ProtocolError
            raise ProtocolError("You can't call a cached method when the object hasn't been given to the peer yet.")
        return self.broker._sendMessage('cache', self.perspective, cacheID, _name, args, kw)

    def remoteMethod(self, key):
        return RemoteCacheMethod(key, self.broker, self.cached, self.perspective)
# okay decompiling out\twisted.spread.flavors.pyc
