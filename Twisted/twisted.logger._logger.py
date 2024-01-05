# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._logger
from time import time
from twisted.python.compat import currentframe
from twisted.python.failure import Failure
from ._levels import InvalidLogLevelError, LogLevel

class Logger(object):

    @staticmethod
    def _namespaceFromCallingContext():
        return currentframe(2).f_globals['__name__']

    def __init__(self, namespace=None, source=None, observer=None):
        if namespace is None:
            namespace = self._namespaceFromCallingContext()
        self.namespace = namespace
        self.source = source
        if observer is None:
            from ._global import globalLogPublisher
            self.observer = globalLogPublisher
        else:
            self.observer = observer
        return

    def __get__(self, oself, type=None):
        if oself is None:
            source = type
        else:
            source = oself
        return self.__class__(('.').join([type.__module__, type.__name__]), source, observer=self.observer)

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.namespace)

    def emit(self, level, format=None, **kwargs):
        if level not in LogLevel.iterconstants():
            self.failure('Got invalid log level {invalidLevel!r} in {logger}.emit().', Failure(InvalidLogLevelError(level)), invalidLevel=level, logger=self)
            return
        event = kwargs
        event.update(log_logger=self, log_level=level, log_namespace=self.namespace, log_source=self.source, log_format=format, log_time=time())
        if 'log_trace' in event:
            event['log_trace'].append((self, self.observer))
        self.observer(event)

    def failure(self, format, failure=None, level=LogLevel.critical, **kwargs):
        if failure is None:
            failure = Failure()
        self.emit(level, format, log_failure=failure, **kwargs)
        return

    def debug(self, format=None, **kwargs):
        self.emit(LogLevel.debug, format, **kwargs)

    def info(self, format=None, **kwargs):
        self.emit(LogLevel.info, format, **kwargs)

    def warn(self, format=None, **kwargs):
        self.emit(LogLevel.warn, format, **kwargs)

    def error(self, format=None, **kwargs):
        self.emit(LogLevel.error, format, **kwargs)

    def critical(self, format=None, **kwargs):
        self.emit(LogLevel.critical, format, **kwargs)
# okay decompiling out\twisted.logger._logger.pyc
