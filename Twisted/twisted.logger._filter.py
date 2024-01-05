# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._filter
from functools import partial
from zope.interface import Interface, implementer
from twisted.python.constants import NamedConstant, Names
from ._levels import InvalidLogLevelError, LogLevel
from ._observer import ILogObserver

class PredicateResult(Names):
    yes = NamedConstant()
    no = NamedConstant()
    maybe = NamedConstant()


class ILogFilterPredicate(Interface):

    def __call__(event):
        pass


def shouldLogEvent(predicates, event):
    for predicate in predicates:
        result = predicate(event)
        if result == PredicateResult.yes:
            return True
        if result == PredicateResult.no:
            return False
        if result == PredicateResult.maybe:
            continue
        raise TypeError(('Invalid predicate result: {0!r}').format(result))

    return True


@implementer(ILogObserver)
class FilteringLogObserver(object):

    def __init__(self, observer, predicates, negativeObserver=(lambda event: None)):
        self._observer = observer
        self._shouldLogEvent = partial(shouldLogEvent, list(predicates))
        self._negativeObserver = negativeObserver

    def __call__(self, event):
        if self._shouldLogEvent(event):
            if 'log_trace' in event:
                event['log_trace'].append((self, self.observer))
            self._observer(event)
        else:
            self._negativeObserver(event)


@implementer(ILogFilterPredicate)
class LogLevelFilterPredicate(object):

    def __init__(self, defaultLogLevel=LogLevel.info):
        self._logLevelsByNamespace = {}
        self.defaultLogLevel = defaultLogLevel
        self.clearLogLevels()

    def logLevelForNamespace(self, namespace):
        if not namespace:
            return self._logLevelsByNamespace[None]
        else:
            if namespace in self._logLevelsByNamespace:
                return self._logLevelsByNamespace[namespace]
            segments = namespace.split('.')
            index = len(segments) - 1
            while index > 0:
                namespace = ('.').join(segments[:index])
                if namespace in self._logLevelsByNamespace:
                    return self._logLevelsByNamespace[namespace]
                index -= 1

            return self._logLevelsByNamespace[None]

    def setLogLevelForNamespace(self, namespace, level):
        if level not in LogLevel.iterconstants():
            raise InvalidLogLevelError(level)
        if namespace:
            self._logLevelsByNamespace[namespace] = level
        else:
            self._logLevelsByNamespace[None] = level
        return

    def clearLogLevels(self):
        self._logLevelsByNamespace.clear()
        self._logLevelsByNamespace[None] = self.defaultLogLevel
        return

    def __call__(self, event):
        eventLevel = event.get('log_level', None)
        namespace = event.get('log_namespace', None)
        namespaceLevel = self.logLevelForNamespace(namespace)
        if eventLevel is None or namespace is None or LogLevel._priorityForLevel(eventLevel) < LogLevel._priorityForLevel(namespaceLevel):
            return PredicateResult.no
        else:
            return PredicateResult.maybe
# okay decompiling out\twisted.logger._filter.pyc
