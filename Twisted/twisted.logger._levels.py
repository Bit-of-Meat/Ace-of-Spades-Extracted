# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._levels
from twisted.python.constants import NamedConstant, Names

class InvalidLogLevelError(Exception):

    def __init__(self, level):
        super(InvalidLogLevelError, self).__init__(str(level))
        self.level = level


class LogLevel(Names):
    debug = NamedConstant()
    info = NamedConstant()
    warn = NamedConstant()
    error = NamedConstant()
    critical = NamedConstant()

    @classmethod
    def levelWithName(cls, name):
        try:
            return cls.lookupByName(name)
        except ValueError:
            raise InvalidLogLevelError(name)

    @classmethod
    def _priorityForLevel(cls, level):
        return cls._levelPriorities[level]


LogLevel._levelPriorities = dict((level, index) for index, level in enumerate(LogLevel.iterconstants()))
# okay decompiling out\twisted.logger._levels.pyc
