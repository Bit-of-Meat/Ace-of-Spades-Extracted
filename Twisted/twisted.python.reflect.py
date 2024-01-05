# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.reflect
from __future__ import division, absolute_import, print_function
import sys, types, os, pickle, weakref, re, traceback, warnings
from collections import deque
RegexType = type(re.compile(''))
from twisted.python.compat import reraise, nativeString, NativeStringIO
from twisted.python.compat import _PY3
from twisted.python.deprecate import deprecated
from twisted.python import compat
from twisted.python.deprecate import _fullyQualifiedName as fullyQualifiedName
from twisted.python.versions import Version

def prefixedMethodNames(classObj, prefix):
    dct = {}
    addMethodNamesToDict(classObj, dct, prefix)
    return list(dct.keys())


def addMethodNamesToDict(classObj, dict, prefix, baseClass=None):
    for base in classObj.__bases__:
        addMethodNamesToDict(base, dict, prefix, baseClass)

    if baseClass is None or baseClass in classObj.__bases__:
        for name, method in classObj.__dict__.items():
            optName = name[len(prefix):]
            if type(method) is types.FunctionType and name[:len(prefix)] == prefix and len(optName):
                dict[optName] = 1

    return


def prefixedMethods(obj, prefix=''):
    dct = {}
    accumulateMethods(obj, dct, prefix)
    return list(dct.values())


def accumulateMethods(obj, dict, prefix='', curClass=None):
    if not curClass:
        curClass = obj.__class__
    for base in curClass.__bases__:
        accumulateMethods(obj, dict, prefix, base)

    for name, method in curClass.__dict__.items():
        optName = name[len(prefix):]
        if type(method) is types.FunctionType and name[:len(prefix)] == prefix and len(optName):
            dict[optName] = getattr(obj, name)


def namedModule(name):
    topLevel = __import__(name)
    packages = name.split('.')[1:]
    m = topLevel
    for p in packages:
        m = getattr(m, p)

    return m


def namedObject(name):
    classSplit = name.split('.')
    module = namedModule(('.').join(classSplit[:-1]))
    return getattr(module, classSplit[-1])


namedClass = namedObject

def requireModule(name, default=None):
    try:
        return namedModule(name)
    except ImportError:
        return default


class _NoModuleFound(Exception):
    pass


class InvalidName(ValueError):
    pass


class ModuleNotFound(InvalidName):
    pass


class ObjectNotFound(InvalidName):
    pass


def _importAndCheckStack(importName):
    try:
        return __import__(importName)
    except ImportError:
        excType, excValue, excTraceback = sys.exc_info()
        while excTraceback:
            execName = excTraceback.tb_frame.f_globals['__name__']
            if execName is None or execName == importName:
                reraise(excValue, excTraceback)
            excTraceback = excTraceback.tb_next

        raise _NoModuleFound()

    return


def namedAny(name):
    if not name:
        raise InvalidName('Empty module name')
    names = name.split('.')
    if '' in names:
        raise InvalidName("name must be a string giving a '.'-separated list of Python identifiers, not %r" % (
         name,))
    topLevelPackage = None
    moduleNames = names[:]
    while not topLevelPackage:
        if moduleNames:
            trialname = ('.').join(moduleNames)
            try:
                topLevelPackage = _importAndCheckStack(trialname)
            except _NoModuleFound:
                moduleNames.pop()

        elif len(names) == 1:
            raise ModuleNotFound('No module named %r' % (name,))
        else:
            raise ObjectNotFound('%r does not name an object' % (name,))

    obj = topLevelPackage
    for n in names[1:]:
        obj = getattr(obj, n)

    return obj


def filenameToModuleName(fn):
    if isinstance(fn, bytes):
        initPy = '__init__.py'
    else:
        initPy = '__init__.py'
    fullName = os.path.abspath(fn)
    base = os.path.basename(fn)
    if not base:
        base = os.path.basename(fn[:-1])
    modName = nativeString(os.path.splitext(base)[0])
    while 1:
        fullName = os.path.dirname(fullName)
        if os.path.exists(os.path.join(fullName, initPy)):
            modName = '%s.%s' % (
             nativeString(os.path.basename(fullName)),
             nativeString(modName))
        else:
            break

    return modName


def qual(clazz):
    return clazz.__module__ + '.' + clazz.__name__


def _determineClass(x):
    try:
        return x.__class__
    except:
        return type(x)


def _determineClassName(x):
    c = _determineClass(x)
    try:
        return c.__name__
    except:
        try:
            return str(c)
        except:
            return '<BROKEN CLASS AT 0x%x>' % id(c)


def _safeFormat(formatter, o):
    io = NativeStringIO()
    traceback.print_exc(file=io)
    className = _determineClassName(o)
    tbValue = io.getvalue()
    return '<%s instance at 0x%x with %s error:\n %s>' % (
     className, id(o), formatter.__name__, tbValue)


def safe_repr(o):
    try:
        return repr(o)
    except:
        return _safeFormat(repr, o)


def safe_str(o):
    if _PY3 and isinstance(o, bytes):
        try:
            return o.decode('utf-8')
        except:
            pass

    try:
        return str(o)
    except:
        return _safeFormat(str, o)


class QueueMethod:

    def __init__(self, name, calls):
        self.name = name
        self.calls = calls

    def __call__(self, *args):
        self.calls.append((self.name, args))


def funcinfo(function):
    warnings.warn('[v2.5] Use inspect.getargspec instead of twisted.python.reflect.funcinfo', DeprecationWarning, stacklevel=2)
    code = function.func_code
    name = function.func_name
    argc = code.co_argcount
    argv = code.co_varnames[:argc]
    defaults = function.func_defaults
    out = []
    out.append('The function %s accepts %s arguments' % (name, argc))
    if defaults:
        required = argc - len(defaults)
        out.append('It requires %s arguments' % required)
        out.append('The arguments required are: %s' % argv[:required])
        out.append('additional arguments are:')
        for i in range(argc - required):
            j = i + required
            out.append('%s which has a default of' % (argv[j], defaults[i]))

    return out


ISNT = 0
WAS = 1
IS = 2

def fullFuncName(func):
    qualName = str(pickle.whichmodule(func, func.__name__)) + '.' + func.__name__
    if namedObject(qualName) is not func:
        raise Exception("Couldn't find %s as %s." % (func, qualName))
    return qualName


def getClass(obj):
    if hasattr(obj, '__class__'):
        return obj.__class__
    else:
        return type(obj)


if not _PY3:

    @deprecated(Version('Twisted', 14, 0, 0))
    def getcurrent(clazz):
        module = namedModule(clazz.__module__)
        currclass = getattr(module, clazz.__name__, None)
        if currclass is None:
            return clazz
        else:
            return currclass


    @deprecated(Version('Twisted', 14, 0, 0), 'isinstance')
    def isinst(inst, clazz):
        if type(inst) != compat.InstanceType or type(clazz) != types.ClassType:
            return isinstance(inst, clazz)
        cl = inst.__class__
        cl2 = getcurrent(cl)
        clazz = getcurrent(clazz)
        if issubclass(cl2, clazz):
            if cl == cl2:
                return WAS
            else:
                inst.__class__ = cl2
                return IS

        else:
            return ISNT


    @deprecated(Version('Twisted', 11, 0, 0), 'inspect.getmro')
    def allYourBase(classObj, baseClass=None):
        l = []
        _accumulateBases(classObj, l, baseClass)
        return l


    @deprecated(Version('Twisted', 11, 0, 0), 'inspect.getmro')
    def accumulateBases(classObj, l, baseClass=None):
        _accumulateBases(classObj, l, baseClass)


    def _accumulateBases(classObj, l, baseClass=None):
        for base in classObj.__bases__:
            if baseClass is None or issubclass(base, baseClass):
                l.append(base)
            _accumulateBases(base, l, baseClass)

        return


def accumulateClassDict(classObj, attr, adict, baseClass=None):
    for base in classObj.__bases__:
        accumulateClassDict(base, attr, adict)

    if baseClass is None or baseClass in classObj.__bases__:
        adict.update(classObj.__dict__.get(attr, {}))
    return


def accumulateClassList(classObj, attr, listObj, baseClass=None):
    for base in classObj.__bases__:
        accumulateClassList(base, attr, listObj)

    if baseClass is None or baseClass in classObj.__bases__:
        listObj.extend(classObj.__dict__.get(attr, []))
    return


def isSame(a, b):
    return a is b


def isLike(a, b):
    return a == b


def modgrep(goal):
    return objgrep(sys.modules, goal, isLike, 'sys.modules')


def isOfType(start, goal):
    return type(start) is goal or isinstance(start, compat.InstanceType) and start.__class__ is goal


def findInstances(start, t):
    return objgrep(start, t, isOfType)


if not _PY3:

    def objgrep(start, goal, eq=isLike, path='', paths=None, seen=None, showUnknowns=0, maxDepth=None):
        if paths is None:
            paths = []
        if seen is None:
            seen = {}
        if eq(start, goal):
            paths.append(path)
        if id(start) in seen:
            if seen[id(start)] is start:
                return
        if maxDepth is not None:
            if maxDepth == 0:
                return
            maxDepth -= 1
        seen[id(start)] = start
        args = (
         paths, seen, showUnknowns, maxDepth)
        if isinstance(start, dict):
            for k, v in start.items():
                objgrep(k, goal, eq, (path + '{' + repr(v) + '}'), *args)
                objgrep(v, goal, eq, (path + '[' + repr(k) + ']'), *args)

        elif isinstance(start, (list, tuple, deque)):
            for idx, _elem in enumerate(start):
                objgrep(start[idx], goal, eq, (path + '[' + str(idx) + ']'), *args)

        elif isinstance(start, types.MethodType):
            objgrep(start.__self__, goal, eq, (path + '.__self__'), *args)
            objgrep(start.__func__, goal, eq, (path + '.__func__'), *args)
            objgrep(start.__self__.__class__, goal, eq, (path + '.__self__.__class__'), *args)
        elif hasattr(start, '__dict__'):
            for k, v in start.__dict__.items():
                objgrep(v, goal, eq, (path + '.' + k), *args)

            if isinstance(start, compat.InstanceType):
                objgrep(start.__class__, goal, eq, (path + '.__class__'), *args)
        elif isinstance(start, weakref.ReferenceType):
            objgrep(start(), goal, eq, (path + '()'), *args)
        elif isinstance(start, (compat.StringType,
         int, types.FunctionType,
         types.BuiltinMethodType, RegexType, float,
         type(None), compat.FileType)) or type(start).__name__ in ('wrapper_descriptor',
                                                                   'method_descriptor',
                                                                   'member_descriptor',
                                                                   'getset_descriptor'):
            pass
        elif showUnknowns:
            print('unknown type', type(start), start)
        return paths


__all__ = [
 'InvalidName', 'ModuleNotFound', 'ObjectNotFound', 
 'ISNT', 'WAS', 'IS', 
 'QueueMethod', 
 'funcinfo', 
 'fullFuncName', 'qual', 'getcurrent', 'getClass', 'isinst', 
 'namedModule', 
 'namedObject', 'namedClass', 'namedAny', 'requireModule', 
 'safe_repr', 
 'safe_str', 'allYourBase', 'accumulateBases', 
 'prefixedMethodNames', 'addMethodNamesToDict', 
 'prefixedMethods', 
 'accumulateMethods', 
 'accumulateClassDict', 'accumulateClassList', 
 'isSame', 'isLike', 
 'modgrep', 'isOfType', 'findInstances', 'objgrep', 
 'filenameToModuleName', 
 'fullyQualifiedName']
if _PY3:
    __all__.remove('objgrep')
# okay decompiling out\twisted.python.reflect.pyc
