# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted._threads._memory
from __future__ import absolute_import, division, print_function
from zope.interface import implementer
from . import IWorker
from ._convenience import Quit
NoMoreWork = object()

@implementer(IWorker)
class MemoryWorker(object):

    def __init__(self, pending=list):
        self._quit = Quit()
        self._pending = pending()

    def do(self, work):
        self._quit.check()
        self._pending.append(work)

    def quit(self):
        self._quit.set()
        self._pending.append(NoMoreWork)


def createMemoryWorker():

    def perform():
        if not worker._pending:
            return False
        if worker._pending[0] is NoMoreWork:
            return False
        worker._pending.pop(0)()
        return True

    worker = MemoryWorker()
    return (worker, perform)
# okay decompiling out\twisted._threads._memory.pyc
