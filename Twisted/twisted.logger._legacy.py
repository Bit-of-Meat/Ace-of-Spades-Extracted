# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._legacy
from zope.interface import implementer
from ._levels import LogLevel
from ._format import formatEvent
from ._observer import ILogObserver
from ._stdlib import fromStdlibLogLevelMapping, StringifiableFromEvent

@implementer(ILogObserver)
class LegacyLogObserverWrapper(object):

    def __init__(self, legacyObserver):
        self.legacyObserver = legacyObserver

    def __repr__(self):
        return ('{self.__class__.__name__}({self.legacyObserver})').format(self=self)

    def __call__(self, event):
        if 'message' not in event:
            event['message'] = ()
        if 'time' not in event:
            event['time'] = event['log_time']
        if 'system' not in event:
            event['system'] = event.get('log_system', '-')
        if 'format' not in event and event.get('log_format', None) is not None:
            event['format'] = '%(log_legacy)s'
            event['log_legacy'] = StringifiableFromEvent(event.copy())
            if not isinstance(event['message'], tuple):
                event['message'] = ()
        if 'log_failure' in event:
            if 'failure' not in event:
                event['failure'] = event['log_failure']
            if 'isError' not in event:
                event['isError'] = 1
            if 'why' not in event:
                event['why'] = formatEvent(event)
        elif 'isError' not in event:
            if event['log_level'] in (LogLevel.error, LogLevel.critical):
                event['isError'] = 1
            else:
                event['isError'] = 0
        self.legacyObserver(event)
        return


def publishToNewObserver(observer, eventDict, textFromEventDict):
    if 'log_time' not in eventDict:
        eventDict['log_time'] = eventDict['time']
    if 'log_format' not in eventDict:
        text = textFromEventDict(eventDict)
        if text is not None:
            eventDict['log_text'] = text
            eventDict['log_format'] = '{log_text}'
    if 'log_level' not in eventDict:
        if 'logLevel' in eventDict:
            try:
                level = fromStdlibLogLevelMapping[eventDict['logLevel']]
            except KeyError:
                level = None

        elif 'isError' in eventDict:
            if eventDict['isError']:
                level = LogLevel.critical
            else:
                level = LogLevel.info
        else:
            level = LogLevel.info
        if level is not None:
            eventDict['log_level'] = level
    if 'log_namespace' not in eventDict:
        eventDict['log_namespace'] = 'log_legacy'
    if 'log_system' not in eventDict and 'system' in eventDict:
        eventDict['log_system'] = eventDict['system']
    observer(eventDict)
    return
# okay decompiling out\twisted.logger._legacy.pyc
