# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.stdio
from __future__ import absolute_import, division
from twisted.python.runtime import platform
if platform.isWindows():
    from twisted.internet import _win32stdio
    StandardIO = _win32stdio.StandardIO
    PipeAddress = _win32stdio.Win32PipeAddress
else:
    from twisted.internet._posixstdio import StandardIO, PipeAddress
__all__ = [
 'StandardIO', 'PipeAddress']
# okay decompiling out\twisted.internet.stdio.pyc
