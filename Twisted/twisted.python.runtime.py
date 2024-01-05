# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.runtime
from __future__ import division, absolute_import
import os, sys, time, imp, warnings
from twisted.python import compat
if compat._PY3:
    _threadModule = '_thread'
else:
    _threadModule = 'thread'

def shortPythonVersion():
    return '%s.%s.%s' % sys.version_info[:3]


knownPlatforms = {'nt': 'win32', 
   'ce': 'win32', 
   'posix': 'posix', 
   'java': 'java', 
   'org.python.modules.os': 'java'}
_timeFunctions = {'win32': time.time}

class Platform:
    type = knownPlatforms.get(os.name)
    seconds = staticmethod(_timeFunctions.get(type, time.time))
    _platform = sys.platform

    def __init__(self, name=None, platform=None):
        if name is not None:
            self.type = knownPlatforms.get(name)
            self.seconds = _timeFunctions.get(self.type, time.time)
        if platform is not None:
            self._platform = platform
        return

    def isKnown(self):
        return self.type != None

    def getType(self):
        return self.type

    def isMacOSX(self):
        return self._platform == 'darwin'

    def isWinNT(self):
        warnings.warn('twisted.python.runtime.Platform.isWinNT was deprecated in Twisted 13.0. Use Platform.isWindows instead.', DeprecationWarning, stacklevel=2)
        return self.isWindows()

    def isWindows(self):
        return self.getType() == 'win32'

    def isVista(self):
        if getattr(sys, 'getwindowsversion', None) is not None:
            return sys.getwindowsversion()[0] == 6
        else:
            return False
            return

    def isLinux(self):
        return self._platform.startswith('linux')

    def isDocker(self, _initCGroupLocation='/proc/1/cgroup'):
        if not self.isLinux():
            return False
        from twisted.python.filepath import FilePath
        initCGroups = FilePath(_initCGroupLocation)
        if initCGroups.exists():
            controlGroups = [ x.split(':') for x in initCGroups.getContent().split('\n')
                            ]
            for group in controlGroups:
                if len(group) == 3 and group[2].startswith('/docker/'):
                    return True

        return False

    def supportsThreads(self):
        try:
            return imp.find_module(_threadModule)[0] is None
        except ImportError:
            return False

        return

    def supportsINotify(self):
        try:
            from twisted.python._inotify import INotifyError, init
        except ImportError:
            return False

        if self.isDocker():
            return False
        try:
            os.close(init())
        except INotifyError:
            return False

        return True


platform = Platform()
platformType = platform.getType()
seconds = platform.seconds
# okay decompiling out\twisted.python.runtime.pyc
