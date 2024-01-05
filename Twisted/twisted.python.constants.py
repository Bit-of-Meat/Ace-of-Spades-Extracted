# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.constants
from __future__ import division, absolute_import
__all__ = [
 'NamedConstant', 'ValueConstant', 'FlagConstant', 
 'Names', 'Values', 'Flags']
from functools import partial
from itertools import count
from operator import and_, or_, xor
_unspecified = object()
_constantOrder = partial(next, count())

class _Constant(object):

    def __init__(self):
        self._container = None
        self._index = _constantOrder()
        return

    def __repr__(self):
        return '<%s=%s>' % (self._container.__name__, self.name)

    def __lt__(self, other):
        if not isinstance(other, self.__class__) or not self._container == other._container:
            return NotImplemented
        return self._index < other._index

    def __le__(self, other):
        if not isinstance(other, self.__class__) or not self._container == other._container:
            return NotImplemented
        return self is other or self._index < other._index

    def __gt__(self, other):
        if not isinstance(other, self.__class__) or not self._container == other._container:
            return NotImplemented
        return self._index > other._index

    def __ge__(self, other):
        if not isinstance(other, self.__class__) or not self._container == other._container:
            return NotImplemented
        return self is other or self._index > other._index

    def _realize(self, container, name, value):
        self._container = container
        self.name = name


class _ConstantsContainerType(type):

    def __new__(self, name, bases, attributes):
        cls = super(_ConstantsContainerType, self).__new__(self, name, bases, attributes)
        constantType = getattr(cls, '_constantType', None)
        if constantType is None:
            return cls
        else:
            constants = []
            for name, descriptor in attributes.items():
                if isinstance(descriptor, cls._constantType):
                    if descriptor._container is not None:
                        raise ValueError('Cannot use %s as the value of an attribute on %s' % (
                         descriptor, cls.__name__))
                    constants.append((descriptor._index, name, descriptor))

            enumerants = {}
            for index, enumerant, descriptor in sorted(constants):
                value = cls._constantFactory(enumerant, descriptor)
                descriptor._realize(cls, enumerant, value)
                enumerants[enumerant] = descriptor

            cls._enumerants = enumerants
            return cls


class _ConstantsContainer(_ConstantsContainerType('', (object,), {})):
    _constantType = None

    def __new__(cls):
        raise TypeError('%s may not be instantiated.' % (cls.__name__,))

    @classmethod
    def _constantFactory(cls, name, descriptor):
        return _unspecified

    @classmethod
    def lookupByName(cls, name):
        if name in cls._enumerants:
            return getattr(cls, name)
        raise ValueError(name)

    @classmethod
    def iterconstants(cls):
        constants = cls._enumerants.values()
        return iter(sorted(constants, key=(lambda descriptor: descriptor._index)))


class NamedConstant(_Constant):
    pass


class Names(_ConstantsContainer):
    _constantType = NamedConstant


class ValueConstant(_Constant):

    def __init__(self, value):
        _Constant.__init__(self)
        self.value = value


class Values(_ConstantsContainer):
    _constantType = ValueConstant

    @classmethod
    def lookupByValue(cls, value):
        for constant in cls.iterconstants():
            if constant.value == value:
                return constant

        raise ValueError(value)


def _flagOp(op, left, right):
    value = op(left.value, right.value)
    names = op(left.names, right.names)
    result = FlagConstant()
    result._realize(left._container, names, value)
    return result


class FlagConstant(_Constant):

    def __init__(self, value=_unspecified):
        _Constant.__init__(self)
        self.value = value

    def _realize(self, container, names, value):
        if isinstance(names, str):
            name = names
            names = set([names])
        elif len(names) == 1:
            name, = names
        else:
            name = '{' + (',').join(sorted(names)) + '}'
        _Constant._realize(self, container, name, value)
        self.value = value
        self.names = names

    def __or__(self, other):
        return _flagOp(or_, self, other)

    def __and__(self, other):
        return _flagOp(and_, self, other)

    def __xor__(self, other):
        return _flagOp(xor, self, other)

    def __invert__(self):
        result = FlagConstant()
        result._realize(self._container, set(), 0)
        for flag in self._container.iterconstants():
            if flag.value & self.value == 0:
                result |= flag

        return result

    def __iter__(self):
        return (self._container.lookupByName(name) for name in self.names)

    def __contains__(self, flag):
        return bool(flag & self)

    def __nonzero__(self):
        return bool(self.value)

    __bool__ = __nonzero__


class Flags(Values):
    _constantType = FlagConstant
    _value = 1

    @classmethod
    def _constantFactory(cls, name, descriptor):
        if descriptor.value is _unspecified:
            value = cls._value
            cls._value <<= 1
        else:
            value = descriptor.value
            cls._value = value << 1
        return value
# okay decompiling out\twisted.python.constants.pyc
