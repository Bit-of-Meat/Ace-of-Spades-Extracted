# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.plugin
from __future__ import absolute_import, division
import os, sys
from zope.interface import Interface, providedBy

def _determinePickleModule():
    try:
        import cPickle
        return cPickle
    except ImportError:
        import pickle
        return pickle


pickle = _determinePickleModule()
from twisted.python.components import getAdapterFactory
from twisted.python.reflect import namedAny
from twisted.python import log
from twisted.python.modules import getModule
from twisted.python.compat import iteritems

class IPlugin(Interface):
    pass


class CachedPlugin(object):

    def __init__(self, dropin, name, description, provided):
        self.dropin = dropin
        self.name = name
        self.description = description
        self.provided = provided
        self.dropin.plugins.append(self)

    def __repr__(self):
        return '<CachedPlugin %r/%r (provides %r)>' % (
         self.name, self.dropin.moduleName,
         (', ').join([ i.__name__ for i in self.provided ]))

    def load(self):
        return namedAny(self.dropin.moduleName + '.' + self.name)

    def __conform__(self, interface, registry=None, default=None):
        for providedInterface in self.provided:
            if providedInterface.isOrExtends(interface):
                return self.load()
            if getAdapterFactory(providedInterface, interface, None) is not None:
                return interface(self.load(), default)

        return default

    getComponent = __conform__


class CachedDropin(object):

    def __init__(self, moduleName, description):
        self.moduleName = moduleName
        self.description = description
        self.plugins = []


def _generateCacheEntry(provider):
    dropin = CachedDropin(provider.__name__, provider.__doc__)
    for k, v in iteritems(provider.__dict__):
        plugin = IPlugin(v, None)
        if plugin is not None:
            CachedPlugin(dropin, k, v.__doc__, list(providedBy(plugin)))

    return dropin


try:
    fromkeys = dict.fromkeys
except AttributeError:

    def fromkeys(keys, value=None):
        d = {}
        for k in keys:
            d[k] = value

        return d


def getCache(module):
    allCachesCombined = {}
    mod = getModule(module.__name__)
    buckets = {}
    for plugmod in mod.iterModules():
        fpp = plugmod.filePath.parent()
        if fpp not in buckets:
            buckets[fpp] = []
        bucket = buckets[fpp]
        bucket.append(plugmod)

    for pseudoPackagePath, bucket in iteritems(buckets):
        dropinPath = pseudoPackagePath.child('dropin.cache')
        try:
            lastCached = dropinPath.getModificationTime()
            with dropinPath.open('r') as (f):
                dropinDotCache = pickle.load(f)
        except:
            dropinDotCache = {}
            lastCached = 0

        needsWrite = False
        existingKeys = {}
        for pluginModule in bucket:
            pluginKey = pluginModule.name.split('.')[-1]
            existingKeys[pluginKey] = True
            if pluginKey not in dropinDotCache or pluginModule.filePath.getModificationTime() >= lastCached:
                needsWrite = True
                try:
                    provider = pluginModule.load()
                except:
                    log.err()
                else:
                    entry = _generateCacheEntry(provider)
                    dropinDotCache[pluginKey] = entry

        for pluginKey in list(dropinDotCache.keys()):
            if pluginKey not in existingKeys:
                del dropinDotCache[pluginKey]
                needsWrite = True

        if needsWrite:
            try:
                dropinPath.setContent(pickle.dumps(dropinDotCache))
            except OSError as e:
                log.msg(format='Unable to write to plugin cache %(path)s: error number %(errno)d', path=dropinPath.path, errno=e.errno)
            except:
                log.err(None, 'Unexpected error while writing cache file')

        allCachesCombined.update(dropinDotCache)

    return allCachesCombined


def getPlugins(interface, package=None):
    if package is None:
        import twisted.plugins as package
    allDropins = getCache(package)
    for key, dropin in iteritems(allDropins):
        for plugin in dropin.plugins:
            try:
                adapted = interface(plugin, None)
            except:
                log.err()
            else:
                if adapted is not None:
                    yield adapted

    return


getPlugIns = getPlugins

def pluginPackagePaths(name):
    package = name.split('.')
    return [ os.path.abspath(os.path.join(x, *package)) for x in sys.path if not os.path.exists(os.path.join(x, *(package + ['__init__.py'])))
           ]


__all__ = [
 'getPlugins', 'pluginPackagePaths']
# okay decompiling out\twisted.plugin.pyc
