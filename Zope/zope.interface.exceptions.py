# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface.exceptions


class Invalid(Exception):
    pass


class DoesNotImplement(Invalid):

    def __init__(self, interface):
        self.interface = interface

    def __str__(self):
        return 'An object does not implement interface %(interface)s\n\n        ' % self.__dict__


class BrokenImplementation(Invalid):

    def __init__(self, interface, name):
        self.interface = interface
        self.name = name

    def __str__(self):
        return 'An object has failed to implement interface %(interface)s\n\n        The %(name)s attribute was not provided.\n        ' % self.__dict__


class BrokenMethodImplementation(Invalid):

    def __init__(self, method, mess):
        self.method = method
        self.mess = mess

    def __str__(self):
        return 'The implementation of %(method)s violates its contract\n        because %(mess)s.\n        ' % self.__dict__


class InvalidInterface(Exception):
    pass


class BadImplements(TypeError):
    pass
# okay decompiling out\zope.interface.exceptions.pyc
