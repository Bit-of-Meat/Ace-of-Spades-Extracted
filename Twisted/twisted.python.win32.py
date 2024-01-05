# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.win32
from __future__ import division, absolute_import
import re, os
try:
    import win32api, win32con
except ImportError:
    pass

from twisted.python.deprecate import deprecated
from twisted.python.runtime import platform
from twisted.python.versions import Version
ERROR_FILE_NOT_FOUND = 2
ERROR_PATH_NOT_FOUND = 3
ERROR_INVALID_NAME = 123
ERROR_DIRECTORY = 267
O_BINARY = getattr(os, 'O_BINARY', 0)

class FakeWindowsError(OSError):
    pass


try:
    WindowsError = WindowsError
except NameError:
    WindowsError = FakeWindowsError

@deprecated(Version('Twisted', 15, 3, 0))
def getProgramsMenuPath():
    if not platform.isWindows():
        return 'C:\\Windows\\Start Menu\\Programs'
    keyname = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders'
    hShellFolders = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, keyname, 0, win32con.KEY_READ)
    return win32api.RegQueryValueEx(hShellFolders, 'Common Programs')[0]


@deprecated(Version('Twisted', 15, 3, 0))
def getProgramFilesPath():
    keyname = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion'
    currentV = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, keyname, 0, win32con.KEY_READ)
    return win32api.RegQueryValueEx(currentV, 'ProgramFilesDir')[0]


_cmdLineQuoteRe = re.compile('(\\\\*)"')
_cmdLineQuoteRe2 = re.compile('(\\\\+)\\Z')

def cmdLineQuote(s):
    quote = (' ' in s or '\t' in s or '"' in s or s == '') and '"' or ''
    return quote + _cmdLineQuoteRe2.sub('\\1\\1', _cmdLineQuoteRe.sub('\\1\\1\\\\"', s)) + quote


def quoteArguments(arguments):
    return (' ').join([ cmdLineQuote(a) for a in arguments ])


class _ErrorFormatter(object):

    def __init__(self, WinError, FormatMessage, errorTab):
        self.winError = WinError
        self.formatMessage = FormatMessage
        self.errorTab = errorTab

    def fromEnvironment(cls):
        try:
            from ctypes import WinError
        except ImportError:
            WinError = None

        try:
            from win32api import FormatMessage
        except ImportError:
            FormatMessage = None

        try:
            from socket import errorTab
        except ImportError:
            errorTab = None

        return cls(WinError, FormatMessage, errorTab)

    fromEnvironment = classmethod(fromEnvironment)

    def formatError(self, errorcode):
        if self.winError is not None:
            return self.winError(errorcode).strerror
        else:
            if self.formatMessage is not None:
                return self.formatMessage(errorcode)
            if self.errorTab is not None:
                result = self.errorTab.get(errorcode)
                if result is not None:
                    return result
            return os.strerror(errorcode)


formatError = _ErrorFormatter.fromEnvironment().formatError
# okay decompiling out\twisted.python.win32.pyc
