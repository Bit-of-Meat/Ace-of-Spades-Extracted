# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._baseprocess
from twisted.python.reflect import qual
from twisted.python.deprecate import getWarningMethod
from twisted.python.failure import Failure
from twisted.python.log import err
_missingProcessExited = 'Since Twisted 8.2, IProcessProtocol.processExited is required.  %s must implement it.'

class BaseProcess(object):
    pid = None
    status = None
    lostProcess = 0
    proto = None

    def __init__(self, protocol):
        self.proto = protocol

    def _callProcessExited(self, reason):
        default = object()
        processExited = getattr(self.proto, 'processExited', default)
        if processExited is default:
            getWarningMethod()(_missingProcessExited % (qual(self.proto.__class__),), DeprecationWarning, stacklevel=0)
        else:
            try:
                processExited(Failure(reason))
            except:
                err(None, 'unexpected error in processExited')

        return

    def processEnded(self, status):
        self.status = status
        self.lostProcess += 1
        self.pid = None
        self._callProcessExited(self._getReason(status))
        self.maybeCallProcessEnded()
        return

    def maybeCallProcessEnded(self):
        if self.proto is not None:
            reason = self._getReason(self.status)
            proto = self.proto
            self.proto = None
            try:
                proto.processEnded(Failure(reason))
            except:
                err(None, 'unexpected error in processEnded')

        return
# okay decompiling out\twisted.internet._baseprocess.pyc
