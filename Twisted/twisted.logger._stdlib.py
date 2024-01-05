# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._stdlib
import logging as stdlibLogging
from zope.interface import implementer
from twisted.python.compat import _PY3, currentframe, unicode
from ._levels import LogLevel
from ._format import formatEvent
from ._observer import ILogObserver
toStdlibLogLevelMapping = {LogLevel.debug: stdlibLogging.DEBUG, 
   LogLevel.info: stdlibLogging.INFO, 
   LogLevel.warn: stdlibLogging.WARNING, 
   LogLevel.error: stdlibLogging.ERROR, 
   LogLevel.critical: stdlibLogging.CRITICAL}

def _reverseLogLevelMapping():
    mapping = {}
    for logLevel, pyLogLevel in toStdlibLogLevelMapping.items():
        mapping[pyLogLevel] = logLevel
        mapping[stdlibLogging.getLevelName(pyLogLevel)] = logLevel

    return mapping


fromStdlibLogLevelMapping = _reverseLogLevelMapping()

@implementer(ILogObserver)
class STDLibLogObserver(object):
    defaultStackDepth = 4

    def __init__(self, name='twisted', stackDepth=defaultStackDepth):
        self.logger = stdlibLogging.getLogger(name)
        self.logger.findCaller = self._findCaller
        self.stackDepth = stackDepth

    def _findCaller(self, stackInfo=False):
        f = currentframe(self.stackDepth)
        co = f.f_code
        if _PY3:
            extra = (None, )
        else:
            extra = ()
        return (
         co.co_filename, f.f_lineno, co.co_name) + extra

    def __call__(self, event):
        level = event.get('log_level', LogLevel.info)
        stdlibLevel = toStdlibLogLevelMapping.get(level, stdlibLogging.INFO)
        self.logger.log(stdlibLevel, StringifiableFromEvent(event))


class StringifiableFromEvent(object):

    def __init__(self, event):
        self.event = event

    def __unicode__(self):
        return formatEvent(self.event)

    def __bytes__(self):
        return unicode(self).encode('utf-8')

    if _PY3:
        __str__ = __unicode__
    else:
        __str__ = __bytes__
# okay decompiling out\twisted.logger._stdlib.pyc
