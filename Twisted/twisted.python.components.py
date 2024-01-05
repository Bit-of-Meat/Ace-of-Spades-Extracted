# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.components
from __future__ import division, absolute_import
from zope.interface import interface, declarations
from zope.interface.adapter import AdapterRegistry
from twisted.python.compat import NativeStringIO
from twisted.python import reflect
globalRegistry = AdapterRegistry()
ALLOW_DUPLICATES = 0
if getattr(AdapterRegistry, 'registered', None) is None:

    def _registered(registry, required, provided):
        return registry.get(required).selfImplied.get(provided, {}).get('')


else:

    def _registered(registry, required, provided):
        return registry.registered([required], provided)


def registerAdapter(adapterFactory, origInterface, *interfaceClasses):
    global ALLOW_DUPLICATES
    self = globalRegistry
    if not isinstance(origInterface, interface.InterfaceClass):
        origInterface = declarations.implementedBy(origInterface)
    for interfaceClass in interfaceClasses:
        factory = _registered(self, origInterface, interfaceClass)
        if factory is not None and not ALLOW_DUPLICATES:
            raise ValueError('an adapter (%s) was already registered.' % (factory,))

    for interfaceClass in interfaceClasses:
        self.register([origInterface], interfaceClass, '', adapterFactory)

    return


def getAdapterFactory(fromInterface, toInterface, default):
    self = globalRegistry
    if not isinstance(fromInterface, interface.InterfaceClass):
        fromInterface = declarations.implementedBy(fromInterface)
    factory = self.lookup1(fromInterface, toInterface)
    if factory is None:
        factory = default
    return factory


def _addHook(registry):
    lookup = registry.lookup1

    def _hook(iface, ob):
        factory = lookup(declarations.providedBy(ob), iface)
        if factory is None:
            return
        else:
            return factory(ob)
            return

    interface.adapter_hooks.append(_hook)
    return _hook


def _removeHook(hook):
    interface.adapter_hooks.remove(hook)


_addHook(globalRegistry)

def getRegistry():
    return globalRegistry


CannotAdapt = TypeError

class Adapter:
    temporaryAdapter = 0
    multiComponent = 1

    def __init__(self, original):
        self.original = original

    def __conform__(self, interface):
        if hasattr(self.original, '__conform__'):
            return self.original.__conform__(interface)
        else:
            return

    def isuper(self, iface, adapter):
        return self.original.isuper(iface, adapter)


class Componentized:
    persistenceVersion = 1

    def __init__(self):
        self._adapterCache = {}

    def locateAdapterClass(self, klass, interfaceClass, default):
        return getAdapterFactory(klass, interfaceClass, default)

    def setAdapter(self, interfaceClass, adapterClass):
        self.setComponent(interfaceClass, adapterClass(self))

    def addAdapter(self, adapterClass, ignoreClass=0):
        adapt = adapterClass(self)
        self.addComponent(adapt, ignoreClass)
        return adapt

    def setComponent(self, interfaceClass, component):
        self._adapterCache[reflect.qual(interfaceClass)] = component

    def addComponent(self, component, ignoreClass=0):
        for iface in declarations.providedBy(component):
            if ignoreClass or self.locateAdapterClass(self.__class__, iface, None) == component.__class__:
                self._adapterCache[reflect.qual(iface)] = component

        return

    def unsetComponent(self, interfaceClass):
        del self._adapterCache[reflect.qual(interfaceClass)]

    def removeComponent(self, component):
        l = []
        for k, v in list(self._adapterCache.items()):
            if v is component:
                del self._adapterCache[k]
                l.append(reflect.namedObject(k))

        return l

    def getComponent(self, interface, default=None):
        k = reflect.qual(interface)
        if k in self._adapterCache:
            return self._adapterCache[k]
        else:
            adapter = interface.__adapt__(self)
            if adapter is not None and not (hasattr(adapter, 'temporaryAdapter') and adapter.temporaryAdapter):
                self._adapterCache[k] = adapter
                if hasattr(adapter, 'multiComponent') and adapter.multiComponent:
                    self.addComponent(adapter)
            if adapter is None:
                return default
            return adapter
            return

    def __conform__(self, interface):
        return self.getComponent(interface)


class ReprableComponentized(Componentized):

    def __init__(self):
        Componentized.__init__(self)

    def __repr__(self):
        from pprint import pprint
        sio = NativeStringIO()
        pprint(self._adapterCache, sio)
        return sio.getvalue()


def proxyForInterface(iface, originalAttribute='original'):

    def __init__(self, original):
        setattr(self, originalAttribute, original)

    contents = {'__init__': __init__}
    for name in iface:
        contents[name] = _ProxyDescriptor(name, originalAttribute)

    proxy = type('(Proxy for %s)' % (
     reflect.qual(iface),), (object,), contents)
    declarations.classImplements(proxy, iface)
    return proxy


class _ProxiedClassMethod(object):

    def __init__(self, methodName, originalAttribute):
        self.methodName = self.__name__ = methodName
        self.originalAttribute = originalAttribute

    def __call__(self, oself, *args, **kw):
        original = getattr(oself, self.originalAttribute)
        actualMethod = getattr(original, self.methodName)
        return actualMethod(*args, **kw)


class _ProxyDescriptor(object):

    def __init__(self, attributeName, originalAttribute):
        self.attributeName = attributeName
        self.originalAttribute = originalAttribute

    def __get__(self, oself, type=None):
        if oself is None:
            return _ProxiedClassMethod(self.attributeName, self.originalAttribute)
        else:
            original = getattr(oself, self.originalAttribute)
            return getattr(original, self.attributeName)

    def __set__(self, oself, value):
        original = getattr(oself, self.originalAttribute)
        setattr(original, self.attributeName, value)

    def __delete__(self, oself):
        original = getattr(oself, self.originalAttribute)
        delattr(original, self.attributeName)


__all__ = [
 'registerAdapter', 'getAdapterFactory', 
 'Adapter', 'Componentized', 'ReprableComponentized', 
 'getRegistry', 
 'proxyForInterface']
# okay decompiling out\twisted.python.components.pyc
