# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted._threads._ithreads
from __future__ import absolute_import, division, print_function
from zope.interface import Interface

class AlreadyQuit(Exception):
    pass


class IWorker(Interface):

    def do(task):
        pass

    def quit():
        pass


class IExclusiveWorker(IWorker):
    pass
# okay decompiling out\twisted._threads._ithreads.pyc
