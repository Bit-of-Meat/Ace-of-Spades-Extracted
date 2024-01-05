# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.default
from __future__ import division, absolute_import
__all__ = [
 'install']
from twisted.python.runtime import platform

def _getInstallFunction(platform):
    try:
        if platform.isLinux():
            try:
                from twisted.internet.epollreactor import install
            except ImportError:
                from twisted.internet.pollreactor import install

        elif platform.getType() == 'posix' and not platform.isMacOSX():
            from twisted.internet.pollreactor import install
        else:
            from twisted.internet.selectreactor import install
    except ImportError:
        from twisted.internet.selectreactor import install

    return install


install = _getInstallFunction(platform)
# okay decompiling out\twisted.internet.default.pyc
