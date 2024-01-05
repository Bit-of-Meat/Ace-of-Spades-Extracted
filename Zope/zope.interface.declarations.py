# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface.declarations
__docformat__ = 'restructuredtext'
import sys
from types import FunctionType
from types import MethodType
from types import ModuleType
import warnings, weakref
from zope.interface.advice import addClassAdvisor
from zope.interface.interface import InterfaceClass
from zope.interface.interface import SpecificationBase
from zope.interface.interface import Specification
from zope.interface._compat import CLASS_TYPES as DescriptorAwareMetaClasses
from zope.interface._compat import PYTHON3
BuiltinImplementationSpecifications = {}
_ADVICE_ERROR = 'Class advice impossible in Python3.  Use the @%s class decorator instead.'
_ADVICE_WARNING = 'The %s API is deprecated, and will not work in Python3  Use the @%s class decorator instead.'

class named(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, ob):
        ob.__component_name__ = self.name
        return ob


class Declaration(Specification):

    def __init__(self, *interfaces):
        Specification.__init__(self, _normalizeargs(interfaces))

    def changed(self, originally_changed):
        Specification.changed(self, originally_changed)
        try:
            del self._v_attrs
        except AttributeError:
            pass

    def __contains__(self, interface):
        return self.extends(interface) and interface in self.interfaces()

    def __iter__(self):
        return self.interfaces()

    def flattened(self):
        return iter(self.__iro__)

    def __sub__(self, other):
        return Declaration(*[ i for i in self.interfaces() if not [ j for j in other.interfaces() if i.extends(j, 0)
                                                                  ]
                            ])

    def __add__(self, other):
        seen = {}
        result = []
        for i in self.interfaces():
            seen[i] = 1
            result.append(i)

        for i in other.interfaces():
            if i not in seen:
                seen[i] = 1
                result.append(i)

        return Declaration(*result)

    __radd__ = __add__


class Implements(Declaration):
    inherit = None
    declared = ()
    __name__ = '?'

    def __repr__(self):
        return '<implementedBy %s>' % self.__name__

    def __reduce__(self):
        return (
         implementedBy, (self.inherit,))


def implementedByFallback(cls):
    try:
        spec = cls.__dict__.get('__implemented__')
    except AttributeError:
        spec = getattr(cls, '__implemented__', None)
        if spec is None:
            spec = BuiltinImplementationSpecifications.get(cls)
            if spec is not None:
                return spec
            return _empty
        if spec.__class__ == Implements:
            return spec
        return Declaration(*_normalizeargs((spec,)))

    if isinstance(spec, Implements):
        return spec
    else:
        if spec is None:
            spec = BuiltinImplementationSpecifications.get(cls)
            if spec is not None:
                return spec
        if spec is not None:
            spec = (spec,)
            spec = Implements(*_normalizeargs(spec))
            spec.inherit = None
            del cls.__implemented__
        else:
            try:
                bases = cls.__bases__
            except AttributeError:
                if not callable(cls):
                    raise TypeError('ImplementedBy called for non-factory', cls)
                bases = ()

            spec = Implements(*[ implementedBy(c) for c in bases ])
            spec.inherit = cls
        spec.__name__ = (getattr(cls, '__module__', '?') or '?') + '.' + (getattr(cls, '__name__', '?') or '?')
        try:
            cls.__implemented__ = spec
            if not hasattr(cls, '__providedBy__'):
                cls.__providedBy__ = objectSpecificationDescriptor
            if isinstance(cls, DescriptorAwareMetaClasses) and '__provides__' not in cls.__dict__:
                cls.__provides__ = ClassProvides(cls, getattr(cls, '__class__', type(cls)))
        except TypeError:
            if not isinstance(cls, type):
                raise TypeError('ImplementedBy called for non-type', cls)
            BuiltinImplementationSpecifications[cls] = spec

        return spec


implementedBy = implementedByFallback

def classImplementsOnly(cls, *interfaces):
    spec = implementedBy(cls)
    spec.declared = ()
    spec.inherit = None
    classImplements(cls, *interfaces)
    return


def classImplements(cls, *interfaces):
    spec = implementedBy(cls)
    spec.declared += tuple(_normalizeargs(interfaces))
    bases = []
    seen = {}
    for b in spec.declared:
        if b not in seen:
            seen[b] = 1
            bases.append(b)

    if spec.inherit is not None:
        for c in spec.inherit.__bases__:
            b = implementedBy(c)
            if b not in seen:
                seen[b] = 1
                bases.append(b)

    spec.__bases__ = tuple(bases)
    return


def _implements_advice(cls):
    interfaces, classImplements = cls.__dict__['__implements_advice_data__']
    del cls.__implements_advice_data__
    classImplements(cls, *interfaces)
    return cls


class implementer:

    def __init__(self, *interfaces):
        self.interfaces = interfaces

    def __call__(self, ob):
        if isinstance(ob, DescriptorAwareMetaClasses):
            classImplements(ob, *self.interfaces)
            return ob
        spec = Implements(*self.interfaces)
        try:
            ob.__implemented__ = spec
        except AttributeError:
            raise TypeError("Can't declare implements", ob)

        return ob


class implementer_only:

    def __init__(self, *interfaces):
        self.interfaces = interfaces

    def __call__(self, ob):
        if isinstance(ob, (FunctionType, MethodType)):
            raise ValueError('The implementer_only decorator is not supported for methods or functions.')
        else:
            classImplementsOnly(ob, *self.interfaces)
            return ob


def _implements(name, interfaces, classImplements):
    if PYTHON3:
        raise TypeError('Class advice impossible in Python3')
    frame = sys._getframe(2)
    locals = frame.f_locals
    if locals is frame.f_globals or '__module__' not in locals:
        raise TypeError(name + ' can be used only from a class definition.')
    if '__implements_advice_data__' in locals:
        raise TypeError(name + ' can be used only once in a class definition.')
    locals['__implements_advice_data__'] = (interfaces, classImplements)
    addClassAdvisor(_implements_advice, depth=3)


def implements(*interfaces):
    if PYTHON3:
        raise TypeError(_ADVICE_ERROR % 'implementer')
    _implements('implements', interfaces, classImplements)


def implementsOnly(*interfaces):
    if PYTHON3:
        raise TypeError(_ADVICE_ERROR % 'implementer_only')
    _implements('implementsOnly', interfaces, classImplementsOnly)


class Provides(Declaration):

    def __init__(self, cls, *interfaces):
        self.__args = (
         cls,) + interfaces
        self._cls = cls
        Declaration.__init__(self, *(interfaces + (implementedBy(cls),)))

    def __reduce__(self):
        return (
         Provides, self.__args)

    __module__ = 'zope.interface'

    def __get__(self, inst, cls):
        if inst is None and cls is self._cls:
            return self
        else:
            raise AttributeError('__provides__')
            return


ProvidesClass = Provides
InstanceDeclarations = weakref.WeakValueDictionary()

def Provides(*interfaces):
    spec = InstanceDeclarations.get(interfaces)
    if spec is None:
        spec = ProvidesClass(*interfaces)
        InstanceDeclarations[interfaces] = spec
    return spec


Provides.__safe_for_unpickling__ = True

def directlyProvides(object, *interfaces):
    cls = getattr(object, '__class__', None)
    if cls is not None and getattr(cls, '__class__', None) is cls:
        if not isinstance(object, DescriptorAwareMetaClasses):
            raise TypeError('Attempt to make an interface declaration on a non-descriptor-aware class')
    interfaces = _normalizeargs(interfaces)
    if cls is None:
        cls = type(object)
    issub = False
    for damc in DescriptorAwareMetaClasses:
        if issubclass(cls, damc):
            issub = True
            break

    if issub:
        object.__provides__ = ClassProvides(object, cls, *interfaces)
    else:
        object.__provides__ = Provides(cls, *interfaces)
    return


def alsoProvides(object, *interfaces):
    directlyProvides(object, directlyProvidedBy(object), *interfaces)


def noLongerProvides(object, interface):
    directlyProvides(object, directlyProvidedBy(object) - interface)
    if interface.providedBy(object):
        raise ValueError('Can only remove directly provided interfaces.')


class ClassProvidesBaseFallback(object):

    def __get__(self, inst, cls):
        if cls is self._cls:
            if inst is None:
                return self
            return self._implements
        else:
            raise AttributeError('__provides__')
            return


ClassProvidesBasePy = ClassProvidesBaseFallback
ClassProvidesBase = ClassProvidesBaseFallback
try:
    import _zope_interface_coptimizations
except ImportError:
    pass
else:
    from _zope_interface_coptimizations import ClassProvidesBase

class ClassProvides(Declaration, ClassProvidesBase):

    def __init__(self, cls, metacls, *interfaces):
        self._cls = cls
        self._implements = implementedBy(cls)
        self.__args = (cls, metacls) + interfaces
        Declaration.__init__(self, *(interfaces + (implementedBy(metacls),)))

    def __reduce__(self):
        return (
         self.__class__, self.__args)

    __get__ = ClassProvidesBase.__get__


def directlyProvidedBy(object):
    provides = getattr(object, '__provides__', None)
    if provides is None or isinstance(provides, Implements):
        return _empty
    return Declaration(provides.__bases__[:-1])


def classProvides(*interfaces):
    if PYTHON3:
        raise TypeError(_ADVICE_ERROR % 'provider')
    frame = sys._getframe(1)
    locals = frame.f_locals
    if locals is frame.f_globals or '__module__' not in locals:
        raise TypeError('classProvides can be used only from a class definition.')
    if '__provides__' in locals:
        raise TypeError('classProvides can only be used once in a class definition.')
    locals['__provides__'] = _normalizeargs(interfaces)
    addClassAdvisor(_classProvides_advice, depth=2)


def _classProvides_advice(cls):
    interfaces = cls.__dict__['__provides__']
    del cls.__provides__
    directlyProvides(cls, *interfaces)
    return cls


class provider:

    def __init__(self, *interfaces):
        self.interfaces = interfaces

    def __call__(self, ob):
        directlyProvides(ob, *self.interfaces)
        return ob


def moduleProvides(*interfaces):
    frame = sys._getframe(1)
    locals = frame.f_locals
    if locals is not frame.f_globals or '__name__' not in locals:
        raise TypeError('moduleProvides can only be used from a module definition.')
    if '__provides__' in locals:
        raise TypeError('moduleProvides can only be used once in a module definition.')
    locals['__provides__'] = Provides(ModuleType, *_normalizeargs(interfaces))


def ObjectSpecification(direct, cls):
    return Provides(cls, direct)


def getObjectSpecificationFallback(ob):
    provides = getattr(ob, '__provides__', None)
    if provides is not None:
        if isinstance(provides, SpecificationBase):
            return provides
    try:
        cls = ob.__class__
    except AttributeError:
        return _empty

    return implementedBy(cls)


getObjectSpecification = getObjectSpecificationFallback

def providedByFallback(ob):
    try:
        r = ob.__providedBy__
    except AttributeError:
        return getObjectSpecification(ob)

    try:
        r.extends
    except AttributeError:
        try:
            r = ob.__provides__
        except AttributeError:
            return implementedBy(ob.__class__)

        try:
            cp = ob.__class__.__provides__
        except AttributeError:
            return r

        if r is cp:
            return implementedBy(ob.__class__)

    return r


providedBy = providedByFallback

class ObjectSpecificationDescriptorFallback(object):

    def __get__(self, inst, cls):
        if inst is None:
            return getObjectSpecification(cls)
        else:
            provides = getattr(inst, '__provides__', None)
            if provides is not None:
                return provides
            return implementedBy(cls)


ObjectSpecificationDescriptor = ObjectSpecificationDescriptorFallback

def _normalizeargs(sequence, output=None):
    if output is None:
        output = []
    cls = sequence.__class__
    if InterfaceClass in cls.__mro__ or Implements in cls.__mro__:
        output.append(sequence)
    else:
        for v in sequence:
            _normalizeargs(v, output)

    return output


_empty = Declaration()
try:
    import _zope_interface_coptimizations
except ImportError:
    pass
else:
    from _zope_interface_coptimizations import implementedBy
    from _zope_interface_coptimizations import providedBy
    from _zope_interface_coptimizations import getObjectSpecification
    from _zope_interface_coptimizations import ObjectSpecificationDescriptor

objectSpecificationDescriptor = ObjectSpecificationDescriptor()
# okay decompiling out\zope.interface.declarations.pyc
