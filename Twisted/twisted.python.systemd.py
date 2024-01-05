# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.systemd
from __future__ import division, absolute_import
__all__ = [
 'ListenFDs']
from os import getpid

class ListenFDs(object):
    _START = 3

    def __init__(self, descriptors):
        self._descriptors = descriptors

    @classmethod
    def fromEnvironment(cls, environ=None, start=None):
        if environ is None:
            from os import environ
        if start is None:
            start = cls._START
        descriptors = []
        try:
            pid = int(environ['LISTEN_PID'])
        except (KeyError, ValueError):
            pass

        if pid == getpid():
            try:
                count = int(environ['LISTEN_FDS'])
            except (KeyError, ValueError):
                pass
            else:
                descriptors = range(start, start + count)
                del environ['LISTEN_PID']
                del environ['LISTEN_FDS']

        return cls(descriptors)

    def inheritedDescriptors(self):
        return list(self._descriptors)
# okay decompiling out\twisted.python.systemd.pyc
