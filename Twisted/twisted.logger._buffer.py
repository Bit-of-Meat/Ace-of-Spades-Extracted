# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._buffer
from collections import deque
from zope.interface import implementer
from ._observer import ILogObserver
_DEFAULT_BUFFER_MAXIMUM = 65536

@implementer(ILogObserver)
class LimitedHistoryLogObserver(object):

    def __init__(self, size=_DEFAULT_BUFFER_MAXIMUM):
        self._buffer = deque(maxlen=size)

    def __call__(self, event):
        self._buffer.append(event)

    def replayTo(self, otherObserver):
        for event in self._buffer:
            otherObserver(event)
# okay decompiling out\twisted.logger._buffer.pyc
