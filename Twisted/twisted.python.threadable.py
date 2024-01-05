# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.threadable
from __future__ import division, absolute_import
from functools import wraps

class DummyLock(object):

    def __reduce__(self):
        return (
         unpickle_lock, ())


def unpickle_lock():
    global XLock
    if threadingmodule is not None:
        return XLock()
    else:
        return DummyLock()
        return


unpickle_lock.__safe_for_unpickling__ = True

def _synchPre(self):
    global _synchLockCreator
    if '_threadable_lock' not in self.__dict__:
        _synchLockCreator.acquire()
        if '_threadable_lock' not in self.__dict__:
            self.__dict__['_threadable_lock'] = XLock()
        _synchLockCreator.release()
    self._threadable_lock.acquire()


def _synchPost(self):
    self._threadable_lock.release()


def _sync(klass, function):

    @wraps(function)
    def sync(self, *args, **kwargs):
        _synchPre(self)
        try:
            return function(self, *args, **kwargs)
        finally:
            _synchPost(self)

    return sync


def synchronize(*klasses):
    if threadingmodule is not None:
        for klass in klasses:
            for methodName in klass.synchronized:
                sync = _sync(klass, klass.__dict__[methodName])
                setattr(klass, methodName, sync)

    return


def init(with_threads=1):
    global XLock
    global _synchLockCreator
    global threaded
    if with_threads:
        if not threaded:
            if threadingmodule is not None:
                threaded = True

                class XLock(threadingmodule._RLock, object):

                    def __reduce__(self):
                        return (
                         unpickle_lock, ())

                _synchLockCreator = XLock()
            else:
                raise RuntimeError('Cannot initialize threading, platform lacks thread support')
    elif threaded:
        raise RuntimeError('Cannot uninitialize threads')
    return


_dummyID = object()

def getThreadID():
    if threadingmodule is None:
        return _dummyID
    else:
        return threadingmodule.currentThread().ident


def isInIOThread():
    global ioThread
    return ioThread == getThreadID()


def registerAsIOThread():
    global ioThread
    ioThread = getThreadID()


ioThread = None
threaded = False
_synchLockCreator = None
XLock = None
try:
    import threading as threadingmodule
except ImportError:
    threadingmodule = None
else:
    init(True)

__all__ = [
 'isInIOThread', 'registerAsIOThread', 'getThreadID', 'XLock']
# okay decompiling out\twisted.python.threadable.pyc
