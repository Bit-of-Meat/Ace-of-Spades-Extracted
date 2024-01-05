# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python._tzhelper
from datetime import datetime, timedelta, tzinfo
__all__ = [
 'FixedOffsetTimeZone',
 'UTC']

class FixedOffsetTimeZone(tzinfo):

    def __init__(self, offset, name=None):
        self.offset = offset
        self.name = name

    @classmethod
    def fromSignHoursMinutes(cls, sign, hours, minutes):
        name = '%s%02i:%02i' % (sign, hours, minutes)
        if sign == '-':
            hours = -hours
            minutes = -minutes
        elif sign != '+':
            raise ValueError('Invalid sign for timezone %r' % (sign,))
        return cls(timedelta(hours=hours, minutes=minutes), name)

    @classmethod
    def fromLocalTimeStamp(cls, timeStamp):
        offset = datetime.fromtimestamp(timeStamp) - datetime.utcfromtimestamp(timeStamp)
        return cls(offset)

    def utcoffset(self, dt):
        return self.offset

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        if self.name is not None:
            return self.name
        else:
            dt = datetime.fromtimestamp(0, self)
            return dt.strftime('UTC%z')


UTC = FixedOffsetTimeZone.fromSignHoursMinutes('+', 0, 0)
# okay decompiling out\twisted.python._tzhelper.pyc
