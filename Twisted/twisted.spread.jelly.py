# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.spread.jelly
import pickle, types, warnings, decimal
from functools import reduce
from types import StringType
from types import IntType
from types import TupleType
from types import ListType
from types import LongType
from types import FloatType
from types import FunctionType
from types import MethodType
from types import ModuleType
from types import DictionaryType
from types import InstanceType
from types import NoneType
from types import ClassType
import copy, datetime
from types import BooleanType
try:
    warnings.filterwarnings('ignore', category=DeprecationWarning, message='the sets module is deprecated', append=True)
    import sets as _sets
finally:
    warnings.filters.pop()

from zope.interface import implementer
from twisted.python.compat import unicode
from twisted.python.reflect import namedObject, qual
from twisted.persisted.crefutil import NotKnown, _Tuple, _InstanceMethod
from twisted.persisted.crefutil import _DictKeyAndValue, _Dereference
from twisted.persisted.crefutil import _Container
from twisted.spread.interfaces import IJellyable, IUnjellyable
from twisted.python.deprecate import deprecatedModuleAttribute
from twisted.python.versions import Version
DictTypes = (
 DictionaryType,)
None_atom = 'None'
class_atom = 'class'
module_atom = 'module'
function_atom = 'function'
dereference_atom = 'dereference'
persistent_atom = 'persistent'
reference_atom = 'reference'
dictionary_atom = 'dictionary'
list_atom = 'list'
set_atom = 'set'
tuple_atom = 'tuple'
instance_atom = 'instance'
frozenset_atom = 'frozenset'
deprecatedModuleAttribute(Version('Twisted', 15, 0, 0), 'instance_atom is unused within Twisted.', 'twisted.spread.jelly', 'instance_atom')
unpersistable_atom = 'unpersistable'
unjellyableRegistry = {}
unjellyableFactoryRegistry = {}
_NO_STATE = object()

def _newInstance(cls, state=_NO_STATE):
    if not isinstance(cls, types.ClassType):
        inst = cls.__new__(cls)
        if state is not _NO_STATE:
            inst.__dict__.update(state)
    elif state is not _NO_STATE:
        inst = InstanceType(cls, state)
    else:
        inst = InstanceType(cls)
    return inst


def _maybeClass(classnamep):
    try:
        object
    except NameError:
        isObject = 0
    else:
        isObject = isinstance(classnamep, type)

    if isinstance(classnamep, ClassType) or isObject:
        return qual(classnamep)
    return classnamep


def setUnjellyableForClass(classname, unjellyable):
    global unjellyableRegistry
    classname = _maybeClass(classname)
    unjellyableRegistry[classname] = unjellyable
    globalSecurity.allowTypes(classname)


def setUnjellyableFactoryForClass(classname, copyFactory):
    global unjellyableFactoryRegistry
    classname = _maybeClass(classname)
    unjellyableFactoryRegistry[classname] = copyFactory
    globalSecurity.allowTypes(classname)


def setUnjellyableForClassTree(module, baseClass, prefix=None):
    if prefix is None:
        prefix = module.__name__
    if prefix:
        prefix = '%s.' % prefix
    for i in dir(module):
        i_ = getattr(module, i)
        if type(i_) == types.ClassType:
            if issubclass(i_, baseClass):
                setUnjellyableForClass('%s%s' % (prefix, i), i_)

    return


def getInstanceState(inst, jellier):
    if hasattr(inst, '__getstate__'):
        state = inst.__getstate__()
    else:
        state = inst.__dict__
    sxp = jellier.prepare(inst)
    sxp.extend([qual(inst.__class__), jellier.jelly(state)])
    return jellier.preserve(inst, sxp)


def setInstanceState(inst, unjellier, jellyList):
    state = unjellier.unjelly(jellyList[1])
    if hasattr(inst, '__setstate__'):
        inst.__setstate__(state)
    else:
        inst.__dict__ = state
    return inst


class Unpersistable():

    def __init__(self, reason):
        self.reason = reason

    def __repr__(self):
        return 'Unpersistable(%s)' % repr(self.reason)


@implementer(IJellyable)
class Jellyable():

    def getStateFor(self, jellier):
        return self.__dict__

    def jellyFor(self, jellier):
        sxp = jellier.prepare(self)
        sxp.extend([
         qual(self.__class__),
         jellier.jelly(self.getStateFor(jellier))])
        return jellier.preserve(self, sxp)


@implementer(IUnjellyable)
class Unjellyable():

    def setStateFor(self, unjellier, state):
        self.__dict__ = state

    def unjellyFor(self, unjellier, jellyList):
        state = unjellier.unjelly(jellyList[1])
        self.setStateFor(unjellier, state)
        return self


class _Jellier():

    def __init__(self, taster, persistentStore, invoker):
        self.taster = taster
        self.preserved = {}
        self.cooked = {}
        self.cooker = {}
        self._ref_id = 1
        self.persistentStore = persistentStore
        self.invoker = invoker

    def _cook(self, object):
        aList = self.preserved[id(object)]
        newList = copy.copy(aList)
        refid = self._ref_id
        self._ref_id = self._ref_id + 1
        aList[:] = [
         reference_atom, refid, newList]
        self.cooked[id(object)] = [dereference_atom, refid]
        return aList

    def prepare(self, object):
        self.preserved[id(object)] = []
        self.cooker[id(object)] = object
        return []

    def preserve(self, object, sexp):
        if id(object) in self.cooked:
            self.preserved[id(object)][2] = sexp
            sexp = self.preserved[id(object)]
        else:
            self.preserved[id(object)] = sexp
        return sexp

    constantTypes = {types.StringType: 1, types.IntType: 1, types.FloatType: 1, 
       types.LongType: 1}

    def _checkMutable(self, obj):
        objId = id(obj)
        if objId in self.cooked:
            return self.cooked[objId]
        if objId in self.preserved:
            self._cook(obj)
            return self.cooked[objId]

    def jelly(self, obj):
        if isinstance(obj, Jellyable):
            preRef = self._checkMutable(obj)
            if preRef:
                return preRef
            return obj.jellyFor(self)
        else:
            objType = type(obj)
            if self.taster.isTypeAllowed(qual(objType)):
                if objType is StringType or objType is IntType or objType is LongType or objType is FloatType:
                    return obj
                if objType is MethodType:
                    return [
                     'method',
                     obj.im_func.__name__,
                     self.jelly(obj.im_self),
                     self.jelly(obj.im_class)]
                if objType is unicode:
                    return ['unicode', obj.encode('UTF-8')]
                if objType is NoneType:
                    return ['None']
                if objType is FunctionType:
                    name = obj.__name__
                    return [
                     'function',
                     str(pickle.whichmodule(obj, obj.__name__)) + '.' + name]
                if objType is ModuleType:
                    return ['module', obj.__name__]
                if objType is BooleanType:
                    return ['boolean', obj and 'true' or 'false']
                if objType is datetime.datetime:
                    if obj.tzinfo:
                        raise NotImplementedError("Currently can't jelly datetime objects with tzinfo")
                    return ['datetime',
                     '%s %s %s %s %s %s %s' % (
                      obj.year, obj.month, obj.day, obj.hour,
                      obj.minute, obj.second, obj.microsecond)]
                if objType is datetime.time:
                    if obj.tzinfo:
                        raise NotImplementedError("Currently can't jelly datetime objects with tzinfo")
                    return ['time',
                     '%s %s %s %s' % (obj.hour, obj.minute,
                      obj.second, obj.microsecond)]
                if objType is datetime.date:
                    return ['date', '%s %s %s' % (obj.year, obj.month, obj.day)]
                if objType is datetime.timedelta:
                    return ['timedelta',
                     '%s %s %s' % (obj.days, obj.seconds,
                      obj.microseconds)]
                if objType is ClassType or issubclass(objType, type):
                    return ['class', qual(obj)]
                if objType is decimal.Decimal:
                    return self.jelly_decimal(obj)
                preRef = self._checkMutable(obj)
                if preRef:
                    return preRef
                sxp = self.prepare(obj)
                if objType is ListType:
                    sxp.extend(self._jellyIterable(list_atom, obj))
                elif objType is TupleType:
                    sxp.extend(self._jellyIterable(tuple_atom, obj))
                elif objType in DictTypes:
                    sxp.append(dictionary_atom)
                    for key, val in obj.items():
                        sxp.append([self.jelly(key), self.jelly(val)])

                elif objType is set or objType is _sets.Set:
                    sxp.extend(self._jellyIterable(set_atom, obj))
                elif objType is frozenset or objType is _sets.ImmutableSet:
                    sxp.extend(self._jellyIterable(frozenset_atom, obj))
                else:
                    className = qual(obj.__class__)
                    persistent = None
                    if self.persistentStore:
                        persistent = self.persistentStore(obj, self)
                    if persistent is not None:
                        sxp.append(persistent_atom)
                        sxp.append(persistent)
                    elif self.taster.isClassAllowed(obj.__class__):
                        sxp.append(className)
                        if hasattr(obj, '__getstate__'):
                            state = obj.__getstate__()
                        else:
                            state = obj.__dict__
                        sxp.append(self.jelly(state))
                    else:
                        self.unpersistable('instance of class %s deemed insecure' % qual(obj.__class__), sxp)
                return self.preserve(obj, sxp)
            else:
                if objType is InstanceType:
                    raise InsecureJelly('Class not allowed for instance: %s %s' % (
                     obj.__class__, obj))
                raise InsecureJelly('Type not allowed for object: %s %s' % (
                 objType, obj))
            return

    def _jellyIterable(self, atom, obj):
        yield atom
        for item in obj:
            yield self.jelly(item)

    def jelly_decimal(self, d):
        sign, guts, exponent = d.as_tuple()
        value = reduce((lambda left, right: left * 10 + right), guts)
        if sign:
            value = -value
        return [
         'decimal', value, exponent]

    def unpersistable(self, reason, sxp=None):
        if sxp is None:
            sxp = []
        sxp.append(unpersistable_atom)
        sxp.append(reason)
        return sxp


class _Unjellier():

    def __init__(self, taster, persistentLoad, invoker):
        self.taster = taster
        self.persistentLoad = persistentLoad
        self.references = {}
        self.postCallbacks = []
        self.invoker = invoker

    def unjellyFull(self, obj):
        o = self.unjelly(obj)
        for m in self.postCallbacks:
            m()

        return o

    def unjelly(self, obj):
        if type(obj) is not types.ListType:
            return obj
        else:
            jelType = obj[0]
            if not self.taster.isTypeAllowed(jelType):
                raise InsecureJelly(jelType)
            regClass = unjellyableRegistry.get(jelType)
            if regClass is not None:
                if isinstance(regClass, ClassType):
                    inst = _Dummy()
                    inst.__class__ = regClass
                    method = inst.unjellyFor
                elif isinstance(regClass, type):
                    inst = regClass.__new__(regClass)
                    method = inst.unjellyFor
                else:
                    method = regClass
                val = method(self, obj)
                if hasattr(val, 'postUnjelly'):
                    self.postCallbacks.append(inst.postUnjelly)
                return val
            regFactory = unjellyableFactoryRegistry.get(jelType)
            if regFactory is not None:
                state = self.unjelly(obj[1])
                inst = regFactory(state)
                if hasattr(inst, 'postUnjelly'):
                    self.postCallbacks.append(inst.postUnjelly)
                return inst
            thunk = getattr(self, '_unjelly_%s' % jelType, None)
            if thunk is not None:
                ret = thunk(obj[1:])
            else:
                nameSplit = jelType.split('.')
                modName = ('.').join(nameSplit[:-1])
                if not self.taster.isModuleAllowed(modName):
                    raise InsecureJelly('Module %s not allowed (in type %s).' % (modName, jelType))
                clz = namedObject(jelType)
                if not self.taster.isClassAllowed(clz):
                    raise InsecureJelly('Class %s not allowed.' % jelType)
                if hasattr(clz, '__setstate__'):
                    ret = _newInstance(clz)
                    state = self.unjelly(obj[1])
                    ret.__setstate__(state)
                else:
                    state = self.unjelly(obj[1])
                    ret = _newInstance(clz, state)
                if hasattr(clz, 'postUnjelly'):
                    self.postCallbacks.append(ret.postUnjelly)
            return ret

    def _unjelly_None(self, exp):
        return

    def _unjelly_unicode(self, exp):
        return unicode(exp[0], 'UTF-8')

    def _unjelly_decimal(self, exp):
        value = exp[0]
        exponent = exp[1]
        if value < 0:
            sign = 1
        else:
            sign = 0
        guts = decimal.Decimal(value).as_tuple()[1]
        return decimal.Decimal((sign, guts, exponent))

    def _unjelly_boolean(self, exp):
        if BooleanType:
            return exp[0] == 'true'
        else:
            return Unpersistable('Could not unpersist boolean: %s' % (exp[0],))

    def _unjelly_datetime(self, exp):
        return datetime.datetime(*map(int, exp[0].split()))

    def _unjelly_date(self, exp):
        return datetime.date(*map(int, exp[0].split()))

    def _unjelly_time(self, exp):
        return datetime.time(*map(int, exp[0].split()))

    def _unjelly_timedelta(self, exp):
        days, seconds, microseconds = map(int, exp[0].split())
        return datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)

    def unjellyInto(self, obj, loc, jel):
        o = self.unjelly(jel)
        if isinstance(o, NotKnown):
            o.addDependant(obj, loc)
        obj[loc] = o
        return o

    def _unjelly_dereference(self, lst):
        refid = lst[0]
        x = self.references.get(refid)
        if x is not None:
            return x
        else:
            der = _Dereference(refid)
            self.references[refid] = der
            return der

    def _unjelly_reference(self, lst):
        refid = lst[0]
        exp = lst[1]
        o = self.unjelly(exp)
        ref = self.references.get(refid)
        if ref is None:
            self.references[refid] = o
        elif isinstance(ref, NotKnown):
            ref.resolveDependants(o)
            self.references[refid] = o
        return o

    def _unjelly_tuple(self, lst):
        l = range(len(lst))
        finished = 1
        for elem in l:
            if isinstance(self.unjellyInto(l, elem, lst[elem]), NotKnown):
                finished = 0

        if finished:
            return tuple(l)
        else:
            return _Tuple(l)

    def _unjelly_list(self, lst):
        l = range(len(lst))
        for elem in l:
            self.unjellyInto(l, elem, lst[elem])

        return l

    def _unjellySetOrFrozenset(self, lst, containerType):
        l = range(len(lst))
        finished = True
        for elem in l:
            data = self.unjellyInto(l, elem, lst[elem])
            if isinstance(data, NotKnown):
                finished = False

        if not finished:
            return _Container(l, containerType)
        else:
            return containerType(l)

    def _unjelly_set(self, lst):
        return self._unjellySetOrFrozenset(lst, set)

    def _unjelly_frozenset(self, lst):
        return self._unjellySetOrFrozenset(lst, frozenset)

    def _unjelly_dictionary(self, lst):
        d = {}
        for k, v in lst:
            kvd = _DictKeyAndValue(d)
            self.unjellyInto(kvd, 0, k)
            self.unjellyInto(kvd, 1, v)

        return d

    def _unjelly_module(self, rest):
        moduleName = rest[0]
        if type(moduleName) != types.StringType:
            raise InsecureJelly('Attempted to unjelly a module with a non-string name.')
        if not self.taster.isModuleAllowed(moduleName):
            raise InsecureJelly('Attempted to unjelly module named %r' % (moduleName,))
        mod = __import__(moduleName, {}, {}, 'x')
        return mod

    def _unjelly_class(self, rest):
        clist = rest[0].split('.')
        modName = ('.').join(clist[:-1])
        if not self.taster.isModuleAllowed(modName):
            raise InsecureJelly('module %s not allowed' % modName)
        klaus = namedObject(rest[0])
        objType = type(klaus)
        if objType not in (types.ClassType, types.TypeType):
            raise InsecureJelly("class %r unjellied to something that isn't a class: %r" % (
             rest[0], klaus))
        if not self.taster.isClassAllowed(klaus):
            raise InsecureJelly('class not allowed: %s' % qual(klaus))
        return klaus

    def _unjelly_function(self, rest):
        modSplit = rest[0].split('.')
        modName = ('.').join(modSplit[:-1])
        if not self.taster.isModuleAllowed(modName):
            raise InsecureJelly('Module not allowed: %s' % modName)
        function = namedObject(rest[0])
        return function

    def _unjelly_persistent(self, rest):
        if self.persistentLoad:
            pload = self.persistentLoad(rest[0], self)
            return pload
        else:
            return Unpersistable('Persistent callback not found')

    def _unjelly_instance(self, rest):
        warnings.warn_explicit('Unjelly support for the instance atom is deprecated since Twisted 15.0.0.  Upgrade peer for modern instance support.', category=DeprecationWarning, filename='', lineno=0)
        clz = self.unjelly(rest[0])
        if type(clz) is not types.ClassType:
            raise InsecureJelly('Instance found with non-class class.')
        if hasattr(clz, '__setstate__'):
            inst = _newInstance(clz, {})
            state = self.unjelly(rest[1])
            inst.__setstate__(state)
        else:
            state = self.unjelly(rest[1])
            inst = _newInstance(clz, state)
        if hasattr(clz, 'postUnjelly'):
            self.postCallbacks.append(inst.postUnjelly)
        return inst

    def _unjelly_unpersistable(self, rest):
        return Unpersistable('Unpersistable data: %s' % (rest[0],))

    def _unjelly_method(self, rest):
        im_name = rest[0]
        im_self = self.unjelly(rest[1])
        im_class = self.unjelly(rest[2])
        if type(im_class) is not types.ClassType:
            raise InsecureJelly('Method found with non-class class.')
        if im_name in im_class.__dict__:
            if im_self is None:
                im = getattr(im_class, im_name)
            else:
                if isinstance(im_self, NotKnown):
                    im = _InstanceMethod(im_name, im_self, im_class)
                else:
                    im = MethodType(im_class.__dict__[im_name], im_self, im_class)
        else:
            raise TypeError('instance method changed')
        return im


class _Dummy():
    pass


class _DummyNewStyle(object):
    pass


def _newDummyLike(instance):
    if isinstance(instance.__class__, type):
        dummy = _DummyNewStyle()
    else:
        dummy = _Dummy()
    dummy.__class__ = instance.__class__
    dummy.__dict__ = instance.__dict__
    return dummy


class InsecureJelly(Exception):
    pass


class DummySecurityOptions():

    def isModuleAllowed(self, moduleName):
        return 1

    def isClassAllowed(self, klass):
        return 1

    def isTypeAllowed(self, typeName):
        return 1


class SecurityOptions():
    basicTypes = [
     'dictionary', 'list', 'tuple', 
     'reference', 'dereference', 
     'unpersistable', 
     'persistent', 'long_int', 'long', 'dict']

    def __init__(self):
        self.allowedTypes = {'None': 1, 'bool': 1, 
           'boolean': 1, 
           'string': 1, 
           'str': 1, 
           'int': 1, 
           'float': 1, 
           'datetime': 1, 
           'time': 1, 
           'date': 1, 
           'timedelta': 1, 
           'NoneType': 1}
        self.allowedTypes['unicode'] = 1
        self.allowedTypes['decimal'] = 1
        self.allowedTypes['set'] = 1
        self.allowedTypes['frozenset'] = 1
        self.allowedModules = {}
        self.allowedClasses = {}

    def allowBasicTypes(self):
        self.allowTypes(*self.basicTypes)

    def allowTypes(self, *types):
        for typ in types:
            if not isinstance(typ, str):
                typ = qual(typ)
            self.allowedTypes[typ] = 1

    def allowInstancesOf(self, *classes):
        self.allowBasicTypes()
        self.allowTypes('instance', 'class', 'classobj', 'module')
        for klass in classes:
            self.allowTypes(qual(klass))
            self.allowModules(klass.__module__)
            self.allowedClasses[klass] = 1

    def allowModules(self, *modules):
        for module in modules:
            if type(module) == types.ModuleType:
                module = module.__name__
            self.allowedModules[module] = 1

    def isModuleAllowed(self, moduleName):
        return moduleName in self.allowedModules

    def isClassAllowed(self, klass):
        return klass in self.allowedClasses

    def isTypeAllowed(self, typeName):
        return typeName in self.allowedTypes or '.' in typeName


globalSecurity = SecurityOptions()
globalSecurity.allowBasicTypes()

def jelly(object, taster=DummySecurityOptions(), persistentStore=None, invoker=None):
    return _Jellier(taster, persistentStore, invoker).jelly(object)


def unjelly(sexp, taster=DummySecurityOptions(), persistentLoad=None, invoker=None):
    return _Unjellier(taster, persistentLoad, invoker).unjellyFull(sexp)
# okay decompiling out\twisted.spread.jelly.pyc
