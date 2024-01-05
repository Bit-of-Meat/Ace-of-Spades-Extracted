# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.persisted.crefutil
from __future__ import division, absolute_import
from twisted.python import log, reflect
from twisted.python.compat import xrange, _constructMethod

class NotKnown:

    def __init__(self):
        self.dependants = []
        self.resolved = 0

    def addDependant(self, mutableObject, key):
        self.dependants.append((mutableObject, key))

    resolvedObject = None

    def resolveDependants(self, newObject):
        self.resolved = 1
        self.resolvedObject = newObject
        for mut, key in self.dependants:
            mut[key] = newObject

    def __hash__(self):
        pass


class _Container(NotKnown):

    def __init__(self, l, containerType):
        NotKnown.__init__(self)
        self.containerType = containerType
        self.l = l
        self.locs = list(xrange(len(l)))
        for idx in xrange(len(l)):
            if not isinstance(l[idx], NotKnown):
                self.locs.remove(idx)
            else:
                l[idx].addDependant(self, idx)

        if not self.locs:
            self.resolveDependants(self.containerType(self.l))

    def __setitem__(self, n, obj):
        self.l[n] = obj
        if not isinstance(obj, NotKnown):
            self.locs.remove(n)
            if not self.locs:
                self.resolveDependants(self.containerType(self.l))


class _Tuple(_Container):

    def __init__(self, l):
        _Container.__init__(self, l, tuple)


class _InstanceMethod(NotKnown):

    def __init__(self, im_name, im_self, im_class):
        NotKnown.__init__(self)
        self.my_class = im_class
        self.name = im_name
        im_self.addDependant(self, 0)

    def __call__(self, *args, **kw):
        import traceback
        log.msg('instance method %s.%s' % (reflect.qual(self.my_class), self.name))
        log.msg('being called with %r %r' % (args, kw))
        traceback.print_stack(file=log.logfile)

    def __setitem__(self, n, obj):
        if not isinstance(obj, NotKnown):
            method = _constructMethod(self.my_class, self.name, obj)
            self.resolveDependants(method)


class _DictKeyAndValue:

    def __init__(self, dict):
        self.dict = dict

    def __setitem__(self, n, obj):
        if n not in (1, 0):
            raise RuntimeError('DictKeyAndValue should only ever be called with 0 or 1')
        if n:
            self.value = obj
        else:
            self.key = obj
        if hasattr(self, 'key') and hasattr(self, 'value'):
            self.dict[self.key] = self.value


class _Dereference(NotKnown):

    def __init__(self, id):
        NotKnown.__init__(self)
        self.id = id


from twisted.internet.defer import Deferred

class _Defer(Deferred, NotKnown):

    def __init__(self):
        Deferred.__init__(self)
        NotKnown.__init__(self)
        self.pause()

    wasset = 0

    def __setitem__(self, n, obj):
        if self.wasset:
            raise RuntimeError('setitem should only be called once, setting %r to %r' % (n, obj))
        else:
            self.wasset = 1
        self.callback(obj)

    def addDependant(self, dep, key):
        NotKnown.addDependant(self, dep, key)
        self.unpause()
        resovd = self.result
        self.resolveDependants(resovd)
# okay decompiling out\twisted.persisted.crefutil.pyc
