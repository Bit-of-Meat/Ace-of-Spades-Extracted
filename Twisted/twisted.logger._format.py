# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._format
from datetime import datetime as DateTime
from twisted.python.compat import unicode
from twisted.python.failure import Failure
from twisted.python.reflect import safe_repr
from twisted.python._tzhelper import FixedOffsetTimeZone
from ._flatten import flatFormat, aFormatter
timeFormatRFC3339 = '%Y-%m-%dT%H:%M:%S%z'

def formatEvent(event):
    try:
        if 'log_flattened' in event:
            return flatFormat(event)
        else:
            format = event.get('log_format', None)
            if format is None:
                return ''
            if isinstance(format, bytes):
                format = format.decode('utf-8')
            elif not isinstance(format, unicode):
                raise TypeError(('Log format must be unicode or bytes, not {0!r}').format(format))
            return formatWithCall(format, event)

    except Exception as e:
        return formatUnformattableEvent(event, e)

    return


def formatUnformattableEvent(event, error):
    try:
        return ('Unable to format event {event!r}: {error}').format(event=event, error=error)
    except BaseException:
        failure = Failure()
        text = (', ').join((' = ').join((safe_repr(key), safe_repr(value))) for key, value in event.items())
        return ('MESSAGE LOST: unformattable object logged: {error}\nRecoverable data: {text}\nException during formatting:\n{failure}').format(error=safe_repr(error), failure=failure, text=text)


def formatTime(when, timeFormat=timeFormatRFC3339, default='-'):
    if timeFormat is None or when is None:
        return default
    tz = FixedOffsetTimeZone.fromLocalTimeStamp(when)
    datetime = DateTime.fromtimestamp(when, tz)
    return unicode(datetime.strftime(timeFormat))
    return


def formatEventAsClassicLogText(event, formatTime=formatTime):
    eventText = formatEvent(event)
    if not eventText:
        return
    else:
        eventText = eventText.replace('\n', '\n\t')
        timeStamp = formatTime(event.get('log_time', None))
        system = event.get('log_system', None)
        if system is None:
            level = event.get('log_level', None)
            if level is None:
                levelName = '-'
            else:
                levelName = level.name
            system = ('{namespace}#{level}').format(namespace=event.get('log_namespace', '-'), level=levelName)
        else:
            try:
                system = unicode(system)
            except Exception:
                system = 'UNFORMATTABLE'

        return ('{timeStamp} [{system}] {event}\n').format(timeStamp=timeStamp, system=system, event=eventText)


class CallMapping(object):

    def __init__(self, submapping):
        self._submapping = submapping

    def __getitem__(self, key):
        callit = key.endswith('()')
        realKey = key[:-2] if callit else key
        value = self._submapping[realKey]
        if callit:
            value = value()
        return value


def formatWithCall(formatString, mapping):
    return unicode(aFormatter.vformat(formatString, (), CallMapping(mapping)))
# okay decompiling out\twisted.logger._format.pyc
