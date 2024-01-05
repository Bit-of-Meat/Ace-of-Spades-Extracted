# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._global
import sys, warnings
from twisted.python.compat import currentframe
from twisted.python.reflect import qual
from ._buffer import LimitedHistoryLogObserver
from ._observer import LogPublisher
from ._filter import FilteringLogObserver, LogLevelFilterPredicate
from ._logger import Logger
from ._format import formatEvent
from ._levels import LogLevel
from ._io import LoggingFile
from ._file import FileLogObserver
MORE_THAN_ONCE_WARNING = 'Warning: primary log target selected twice at <{fileNow}:{lineNow}> - previously selected at <{fileThen}:{lineThen}>.  Remove one of the calls to beginLoggingTo.'

class LogBeginner(object):

    def __init__(self, publisher, errorStream, stdio, warningsModule):
        self._initialBuffer = LimitedHistoryLogObserver()
        self._publisher = publisher
        self._log = Logger(observer=publisher)
        self._stdio = stdio
        self._warningsModule = warningsModule
        self._temporaryObserver = LogPublisher(self._initialBuffer, FilteringLogObserver(FileLogObserver(errorStream, (lambda event: formatEvent(event) + '\n')), [
         LogLevelFilterPredicate(defaultLogLevel=LogLevel.critical)]))
        publisher.addObserver(self._temporaryObserver)
        self._oldshowwarning = warningsModule.showwarning

    def beginLoggingTo(self, observers, discardBuffer=False, redirectStandardIO=True):
        caller = currentframe(1)
        filename, lineno = caller.f_code.co_filename, caller.f_lineno
        for observer in observers:
            self._publisher.addObserver(observer)

        if self._temporaryObserver is not None:
            self._publisher.removeObserver(self._temporaryObserver)
            if not discardBuffer:
                self._initialBuffer.replayTo(self._publisher)
            self._temporaryObserver = None
            self._warningsModule.showwarning = self.showwarning
        else:
            previousFile, previousLine = self._previousBegin
            self._log.warn(MORE_THAN_ONCE_WARNING, fileNow=filename, lineNow=lineno, fileThen=previousFile, lineThen=previousLine)
        self._previousBegin = (
         filename, lineno)
        if redirectStandardIO:
            streams = [
             (
              'stdout', LogLevel.info), ('stderr', LogLevel.error)]
        else:
            streams = []
        for stream, level in streams:
            oldStream = getattr(self._stdio, stream)
            loggingFile = LoggingFile(logger=Logger(namespace=stream, observer=self._publisher), level=level, encoding=getattr(oldStream, 'encoding', None))
            setattr(self._stdio, stream, loggingFile)

        return

    def showwarning(self, message, category, filename, lineno, file=None, line=None):
        if file is None:
            self._log.warn('{filename}:{lineno}: {category}: {warning}', warning=message, category=qual(category), filename=filename, lineno=lineno)
        elif sys.version_info < (2, 6):
            self._oldshowwarning(message, category, filename, lineno, file)
        else:
            self._oldshowwarning(message, category, filename, lineno, file, line)
        return


globalLogPublisher = LogPublisher()
globalLogBeginner = LogBeginner(globalLogPublisher, sys.stderr, sys, warnings)
# okay decompiling out\twisted.logger._global.pyc
