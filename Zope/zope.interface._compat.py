# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface._compat
import sys, types
if sys.version_info[0] < 3:

    def _u(s):
        return unicode(s, 'unicode_escape')


    def _normalize_name(name):
        if isinstance(name, basestring):
            return unicode(name)
        raise TypeError('name must be a regular or unicode string')


    CLASS_TYPES = (
     type, types.ClassType)
    STRING_TYPES = (basestring,)
    _BUILTINS = '__builtin__'
    PYTHON3 = False
    PYTHON2 = True
else:

    def _u(s):
        return s


    def _normalize_name(name):
        if isinstance(name, bytes):
            name = str(name, 'ascii')
        if isinstance(name, str):
            return name
        raise TypeError('name must be a string or ASCII-only bytes')


    CLASS_TYPES = (
     type,)
    STRING_TYPES = (str,)
    _BUILTINS = 'builtins'
    PYTHON3 = True
    PYTHON2 = False

def _skip_under_py3k(test_method):
    if sys.version_info[0] < 3:
        return test_method

    def _dummy(*args):
        pass

    return _dummy


def _skip_under_py2(test_method):
    if sys.version_info[0] > 2:
        return test_method

    def _dummy(*args):
        pass

    return _dummy
# okay decompiling out\zope.interface._compat.pyc
