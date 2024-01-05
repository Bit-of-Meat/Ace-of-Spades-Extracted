# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.persisted.styles
from __future__ import division, absolute_import
import types
try:
    import copy_reg
except ImportError:
    import copyreg as copy_reg

import copy, inspect, sys
from twisted.python.compat import _PY3
from twisted.python import log
from twisted.python import reflect
oldModules = {}

def pickleMethod(method):
    if _PY3:
        return (unpickleMethod,
         (method.__name__,
          method.__self__,
          method.__self__.__class__))
    else:
        return (
         unpickleMethod,
         (method.im_func.__name__,
          method.im_self,
          method.im_class))


def _methodFunction(classObject, methodName):
    methodObject = getattr(classObject, methodName)
    if _PY3:
        return methodObject
    return methodObject.im_func


def unpickleMethod(im_name, im_self, im_class):
    if im_self is None:
        return getattr(im_class, im_name)
    else:
        try:
            methodFunction = _methodFunction(im_class, im_name)
        except AttributeError:
            log.msg('Method', im_name, 'not on class', im_class)
            if im_self.__class__ is im_class:
                raise
            return unpickleMethod(im_name, im_self, im_self.__class__)

        if _PY3:
            maybeClass = ()
        else:
            maybeClass = tuple([im_class])
        bound = types.MethodType(methodFunction, im_self, *maybeClass)
        return bound
        return


copy_reg.pickle(types.MethodType, pickleMethod, unpickleMethod)

def _pickleFunction(f):
    if f.__name__ == '<lambda>':
        return None
    else:
        return (
         _unpickleFunction,
         tuple([('.').join([f.__module__, f.__qualname__])]))


def _unpickleFunction(fullyQualifiedName):
    from twisted.python.reflect import namedAny
    return namedAny(fullyQualifiedName)


copy_reg.pickle(types.FunctionType, _pickleFunction, _unpickleFunction)

def pickleModule(module):
    return (
     unpickleModule, (module.__name__,))


def unpickleModule(name):
    if name in oldModules:
        log.msg('Module has moved: %s' % name)
        name = oldModules[name]
        log.msg(name)
    return __import__(name, {}, {}, 'x')


copy_reg.pickle(types.ModuleType, pickleModule, unpickleModule)

def pickleStringO(stringo):
    return (
     unpickleStringO, (stringo.getvalue(), stringo.tell()))


def unpickleStringO(val, sek):
    x = _cStringIO()
    x.write(val)
    x.seek(sek)
    return x


def pickleStringI(stringi):
    return (
     unpickleStringI, (stringi.getvalue(), stringi.tell()))


def unpickleStringI(val, sek):
    x = _cStringIO(val)
    x.seek(sek)
    return x


try:
    from cStringIO import InputType, OutputType, StringIO as _cStringIO
except ImportError:
    from io import StringIO as _cStringIO
else:
    copy_reg.pickle(OutputType, pickleStringO, unpickleStringO)
    copy_reg.pickle(InputType, pickleStringI, unpickleStringI)

class Ephemeral:

    def __reduce__(self):
        return (
         Ephemeral, ())

    def __getstate__(self):
        log.msg('WARNING: serializing ephemeral %s' % self)
        import gc
        if '__pypy__' not in sys.builtin_module_names:
            if getattr(gc, 'get_referrers', None):
                for r in gc.get_referrers(self):
                    log.msg(' referred to by %s' % (r,))

        return

    def __setstate__(self, state):
        log.msg('WARNING: unserializing ephemeral %s' % self.__class__)
        self.__class__ = Ephemeral


versionedsToUpgrade = {}
upgraded = {}

def doUpgrade():
    global upgraded
    global versionedsToUpgrade
    for versioned in list(versionedsToUpgrade.values()):
        requireUpgrade(versioned)

    versionedsToUpgrade = {}
    upgraded = {}


def requireUpgrade(obj):
    objID = id(obj)
    if objID in versionedsToUpgrade and objID not in upgraded:
        upgraded[objID] = 1
        obj.versionUpgrade()
        return obj


def _aybabtu(c):
    l = [
     c, Versioned]
    for b in inspect.getmro(c):
        if b not in l and issubclass(b, Versioned):
            l.append(b)

    return l[2:]


class Versioned:
    persistenceVersion = 0
    persistenceForgets = ()

    def __setstate__(self, state):
        versionedsToUpgrade[id(self)] = self
        self.__dict__ = state

    def __getstate__(self, dict=None):
        dct = copy.copy(dict or self.__dict__)
        bases = _aybabtu(self.__class__)
        bases.reverse()
        bases.append(self.__class__)
        for base in bases:
            if 'persistenceForgets' in base.__dict__:
                for slot in base.persistenceForgets:
                    if slot in dct:
                        del dct[slot]

            if 'persistenceVersion' in base.__dict__:
                dct['%s.persistenceVersion' % reflect.qual(base)] = base.persistenceVersion

        return dct

    def versionUpgrade(self):
        bases = _aybabtu(self.__class__)
        bases.reverse()
        bases.append(self.__class__)
        if 'persistenceVersion' in self.__dict__:
            pver = self.__dict__['persistenceVersion']
            del self.__dict__['persistenceVersion']
            highestVersion = 0
            highestBase = None
            for base in bases:
                if not base.__dict__.has_key('persistenceVersion'):
                    continue
                if base.persistenceVersion > highestVersion:
                    highestBase = base
                    highestVersion = base.persistenceVersion

            if highestBase:
                self.__dict__['%s.persistenceVersion' % reflect.qual(highestBase)] = pver
        for base in bases:
            if Versioned not in base.__bases__ and 'persistenceVersion' not in base.__dict__:
                continue
            currentVers = base.persistenceVersion
            pverName = '%s.persistenceVersion' % reflect.qual(base)
            persistVers = self.__dict__.get(pverName) or 0
            if persistVers:
                del self.__dict__[pverName]
            while persistVers < currentVers:
                persistVers = persistVers + 1
                method = base.__dict__.get('upgradeToVersion%s' % persistVers, None)
                if method:
                    log.msg('Upgrading %s (of %s @ %s) to version %s' % (reflect.qual(base), reflect.qual(self.__class__), id(self), persistVers))
                    method(self)
                else:
                    log.msg('Warning: cannot upgrade %s to version %s' % (base, persistVers))

        return
# okay decompiling out\twisted.persisted.styles.pyc
