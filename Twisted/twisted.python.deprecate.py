# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.deprecate
from __future__ import division, absolute_import
__all__ = [
 'deprecated', 
 'getDeprecationWarningString', 
 'getWarningMethod', 
 'setWarningMethod', 
 'deprecatedModuleAttribute']
import sys, inspect
from warnings import warn, warn_explicit
from dis import findlinestarts
from functools import wraps
from twisted.python.versions import getVersionString
DEPRECATION_WARNING_FORMAT = '%(fqpn)s was deprecated in %(version)s'

def _fullyQualifiedName(obj):
    try:
        name = obj.__qualname__
    except AttributeError:
        name = obj.__name__

    if inspect.isclass(obj) or inspect.isfunction(obj):
        moduleName = obj.__module__
        return '%s.%s' % (moduleName, name)
    if inspect.ismethod(obj):
        try:
            cls = obj.im_class
        except AttributeError:
            return '%s.%s' % (obj.__module__, obj.__qualname__)

        className = _fullyQualifiedName(cls)
        return '%s.%s' % (className, name)
    return name


_fullyQualifiedName.__module__ = 'twisted.python.reflect'
_fullyQualifiedName.__name__ = 'fullyQualifiedName'
_fullyQualifiedName.__qualname__ = 'fullyQualifiedName'

def _getReplacementString(replacement):
    if callable(replacement):
        replacement = _fullyQualifiedName(replacement)
    return 'please use %s instead' % (replacement,)


def _getDeprecationDocstring(version, replacement=None):
    doc = 'Deprecated in %s' % (getVersionString(version),)
    if replacement:
        doc = '%s; %s' % (doc, _getReplacementString(replacement))
    return doc + '.'


def _getDeprecationWarningString(fqpn, version, format=None, replacement=None):
    if format is None:
        format = DEPRECATION_WARNING_FORMAT
    warningString = format % {'fqpn': fqpn, 
       'version': getVersionString(version)}
    if replacement:
        warningString = '%s; %s' % (
         warningString, _getReplacementString(replacement))
    return warningString


def getDeprecationWarningString(callableThing, version, format=None, replacement=None):
    return _getDeprecationWarningString(_fullyQualifiedName(callableThing), version, format, replacement)


def _appendToDocstring(thingWithDoc, textToAppend):
    if thingWithDoc.__doc__:
        docstringLines = thingWithDoc.__doc__.splitlines()
    else:
        docstringLines = []
    if len(docstringLines) == 0:
        docstringLines.append(textToAppend)
    elif len(docstringLines) == 1:
        docstringLines.extend(['', textToAppend, ''])
    else:
        spaces = docstringLines.pop()
        docstringLines.extend(['',
         spaces + textToAppend,
         spaces])
    thingWithDoc.__doc__ = ('\n').join(docstringLines)


def deprecated(version, replacement=None):

    def deprecationDecorator(function):
        warningString = getDeprecationWarningString(function, version, None, replacement)

        @wraps(function)
        def deprecatedFunction(*args, **kwargs):
            global warn
            warn(warningString, DeprecationWarning, stacklevel=2)
            return function(*args, **kwargs)

        _appendToDocstring(deprecatedFunction, _getDeprecationDocstring(version, replacement))
        deprecatedFunction.deprecatedVersion = version
        return deprecatedFunction

    return deprecationDecorator


def getWarningMethod():
    return warn


def setWarningMethod(newMethod):
    global warn
    warn = newMethod


class _InternalState(object):

    def __init__(self, proxy):
        object.__setattr__(self, 'proxy', proxy)

    def __getattribute__(self, name):
        return object.__getattribute__(object.__getattribute__(self, 'proxy'), name)

    def __setattr__(self, name, value):
        return object.__setattr__(object.__getattribute__(self, 'proxy'), name, value)


class _ModuleProxy(object):

    def __init__(self, module):
        state = _InternalState(self)
        state._module = module
        state._deprecatedAttributes = {}
        state._lastWasPath = False

    def __repr__(self):
        state = _InternalState(self)
        return '<%s module=%r>' % (type(self).__name__, state._module)

    def __setattr__(self, name, value):
        state = _InternalState(self)
        state._lastWasPath = False
        setattr(state._module, name, value)

    def __getattribute__(self, name):
        state = _InternalState(self)
        if state._lastWasPath:
            deprecatedAttribute = None
        else:
            deprecatedAttribute = state._deprecatedAttributes.get(name)
        if deprecatedAttribute is not None:
            value = deprecatedAttribute.get()
        else:
            value = getattr(state._module, name)
        if name == '__path__':
            state._lastWasPath = True
        else:
            state._lastWasPath = False
        return value


class _DeprecatedAttribute(object):

    def __init__(self, module, name, version, message):
        self.module = module
        self.__name__ = name
        self.fqpn = module.__name__ + '.' + name
        self.version = version
        self.message = message

    def get(self):
        result = getattr(self.module, self.__name__)
        message = _getDeprecationWarningString(self.fqpn, self.version, DEPRECATION_WARNING_FORMAT + ': ' + self.message)
        warn(message, DeprecationWarning, stacklevel=3)
        return result


def _deprecateAttribute(proxy, name, version, message):
    _module = object.__getattribute__(proxy, '_module')
    attr = _DeprecatedAttribute(_module, name, version, message)
    _deprecatedAttributes = object.__getattribute__(proxy, '_deprecatedAttributes')
    _deprecatedAttributes[name] = attr


def deprecatedModuleAttribute(version, message, moduleName, name):
    module = sys.modules[moduleName]
    if not isinstance(module, _ModuleProxy):
        module = _ModuleProxy(module)
        sys.modules[moduleName] = module
    _deprecateAttribute(module, name, version, message)


def warnAboutFunction(offender, warningString):
    offenderModule = sys.modules[offender.__module__]
    filename = inspect.getabsfile(offenderModule)
    lineStarts = list(findlinestarts(offender.__code__))
    lastLineNo = lineStarts[-1][1]
    globals = offender.__globals__
    kwargs = dict(category=DeprecationWarning, filename=filename, lineno=lastLineNo, module=offenderModule.__name__, registry=globals.setdefault('__warningregistry__', {}), module_globals=None)
    warn_explicit(warningString, **kwargs)
    return


def _passed(argspec, positional, keyword):
    result = {}
    unpassed = len(argspec.args) - len(positional)
    if argspec.keywords is not None:
        kwargs = result[argspec.keywords] = {}
    if unpassed < 0:
        if argspec.varargs is None:
            raise TypeError('Too many arguments.')
        else:
            result[argspec.varargs] = positional[len(argspec.args):]
    for name, value in zip(argspec.args, positional):
        result[name] = value

    for name, value in keyword.items():
        if name in argspec.args:
            if name in result:
                raise TypeError('Already passed.')
            result[name] = value
        elif argspec.keywords is not None:
            kwargs[name] = value
        else:
            raise TypeError('no such param')

    return result


def _mutuallyExclusiveArguments(argumentPairs):

    def wrapper(wrappee):
        argspec = inspect.getargspec(wrappee)

        @wraps(wrappee)
        def wrapped(*args, **kwargs):
            arguments = _passed(argspec, args, kwargs)
            for this, that in argumentPairs:
                if this in arguments and that in arguments:
                    raise TypeError('nope')

            return wrappee(*args, **kwargs)

        return wrapped

    return wrapper
# okay decompiling out\twisted.python.deprecate.pyc
