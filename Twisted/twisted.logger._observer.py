# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._observer
from zope.interface import Interface, implementer
from twisted.python.failure import Failure
from ._logger import Logger
OBSERVER_DISABLED = 'Temporarily disabling observer {observer} due to exception: {log_failure}'

class ILogObserver(Interface):

    def __call__(event):
        pass


@implementer(ILogObserver)
class LogPublisher(object):

    def __init__(self, *observers):
        self._observers = list(observers)
        self.log = Logger(observer=self)

    def addObserver(self, observer):
        if not callable(observer):
            raise TypeError(('Observer is not callable: {0!r}').format(observer))
        if observer not in self._observers:
            self._observers.append(observer)

    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def __call__(self, event):
        if 'log_trace' in event:

            def trace(observer):
                event['log_trace'].append((self, observer))

        else:
            trace = None
        brokenObservers = []
        for observer in self._observers:
            if trace is not None:
                trace(observer)
            try:
                observer(event)
            except Exception:
                brokenObservers.append((observer, Failure()))

        for brokenObserver, failure in brokenObservers:
            errorLogger = self._errorLoggerForObserver(brokenObserver)
            errorLogger.failure(OBSERVER_DISABLED, failure=failure, observer=brokenObserver)

        return

    def _errorLoggerForObserver(self, observer):
        errorPublisher = LogPublisher(*[ obs for obs in self._observers if obs is not observer
                                       ])
        return Logger(observer=errorPublisher)
# okay decompiling out\twisted.logger._observer.pyc
