# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.context
from __future__ import division, absolute_import
from threading import local
defaultContextDict = {}
setDefault = defaultContextDict.__setitem__

class ContextTracker:

    def __init__(self):
        self.contexts = [
         defaultContextDict]

    def callWithContext(self, newContext, func, *args, **kw):
        self.contexts.append(newContext)
        try:
            return func(*args, **kw)
        finally:
            self.contexts.pop()

    def getContext(self, key, default=None):
        for ctx in reversed(self.contexts):
            try:
                return ctx[key]
            except KeyError:
                pass

        return default


class ThreadedContextTracker(object):

    def __init__(self):
        self.storage = local()

    def currentContext(self):
        try:
            return self.storage.ct
        except AttributeError:
            ct = self.storage.ct = ContextTracker()
            return ct

    def callWithContext(self, ctx, func, *args, **kw):
        return self.currentContext().callWithContext(ctx, func, *args, **kw)

    def getContext(self, key, default=None):
        return self.currentContext().getContext(key, default)


def installContextTracker(ctr):
    global call
    global get
    global theContextTracker
    theContextTracker = ctr
    call = theContextTracker.callWithContext
    get = theContextTracker.getContext


installContextTracker(ThreadedContextTracker())
# okay decompiling out\twisted.python.context.pyc
