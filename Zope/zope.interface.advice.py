# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface.advice
from types import FunctionType
try:
    from types import ClassType
except ImportError:
    __python3 = True
else:
    __python3 = False

import sys

def getFrameInfo(frame):
    f_locals = frame.f_locals
    f_globals = frame.f_globals
    sameNamespace = f_locals is f_globals
    hasModule = '__module__' in f_locals
    hasName = '__name__' in f_globals
    sameName = hasModule and hasName
    sameName = sameName and f_globals['__name__'] == f_locals['__module__']
    module = hasName and sys.modules.get(f_globals['__name__']) or None
    namespaceIsModule = module and module.__dict__ is f_globals
    if not namespaceIsModule:
        kind = 'exec'
    elif sameNamespace and not hasModule:
        kind = 'module'
    elif sameName and not sameNamespace:
        kind = 'class'
    elif not sameNamespace:
        kind = 'function call'
    else:
        kind = 'unknown'
    return (
     kind, module, f_locals, f_globals)


def addClassAdvisor(callback, depth=2):
    if __python3:
        raise TypeError('Class advice impossible in Python3')
    frame = sys._getframe(depth)
    kind, module, caller_locals, caller_globals = getFrameInfo(frame)
    previousMetaclass = caller_locals.get('__metaclass__')
    if __python3:
        defaultMetaclass = caller_globals.get('__metaclass__', type)
    else:
        defaultMetaclass = caller_globals.get('__metaclass__', ClassType)

    def advise(name, bases, cdict):
        if '__metaclass__' in cdict:
            del cdict['__metaclass__']
        if previousMetaclass is None:
            if bases:
                meta = determineMetaclass(bases)
            else:
                meta = defaultMetaclass
        elif isClassAdvisor(previousMetaclass):
            meta = previousMetaclass
        else:
            meta = determineMetaclass(bases, previousMetaclass)
        newClass = meta(name, bases, cdict)
        return callback(newClass)

    advise.previousMetaclass = previousMetaclass
    advise.callback = callback
    caller_locals['__metaclass__'] = advise


def isClassAdvisor(ob):
    return isinstance(ob, FunctionType) and hasattr(ob, 'previousMetaclass')


def determineMetaclass(bases, explicit_mc=None):
    meta = [ getattr(b, '__class__', type(b)) for b in bases ]
    if explicit_mc is not None:
        meta.append(explicit_mc)
    if len(meta) == 1:
        return meta[0]
    else:
        candidates = minimalBases(meta)
        if not candidates:
            return ClassType
        if len(candidates) > 1:
            raise TypeError('Incompatible metatypes', bases)
        return candidates[0]


def minimalBases(classes):
    if not __python3:
        classes = [ c for c in classes if c is not ClassType ]
    candidates = []
    for m in classes:
        for n in classes:
            if issubclass(n, m) and m is not n:
                break
        else:
            if m in candidates:
                candidates.remove(m)
            candidates.append(m)

    return candidates
# okay decompiling out\zope.interface.advice.pyc
