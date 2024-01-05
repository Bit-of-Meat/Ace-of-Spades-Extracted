# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted


def _checkRequirements():
    import sys
    version = getattr(sys, 'version_info', (0, ))
    if version < (2, 6):
        raise ImportError('Twisted requires Python 2.6 or later.')
    if version < (3, 0):
        required = '3.6.0'
    else:
        required = '4.0.0'
    if 'setuptools' in sys.modules and getattr(sys.modules['setuptools'], '_TWISTED_NO_CHECK_REQUIREMENTS', None) is not None:
        return
    else:
        required = 'Twisted requires zope.interface %s or later' % (required,)
        try:
            from zope import interface
        except ImportError:
            raise ImportError(required + ': no module named zope.interface.')
        except:
            raise ImportError(required + '.')

        try:

            class IDummy(interface.Interface):
                pass

            @interface.implementer(IDummy)
            class Dummy(object):
                pass

        except TypeError:
            raise ImportError(required + '.')

        return


_checkRequirements()
from twisted.python import compat
from twisted._version import version
__version__ = version.short()
del compat
# okay decompiling out\twisted.pyc
