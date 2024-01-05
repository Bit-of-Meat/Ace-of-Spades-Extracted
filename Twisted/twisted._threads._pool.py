# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted._threads._pool
from __future__ import absolute_import, division, print_function
from threading import Thread, Lock, local as LocalStorage
try:
    from Queue import Queue
except ImportError:
    from queue import Queue

from twisted.python.log import err
from ._threadworker import LockWorker
from ._team import Team
from ._threadworker import ThreadWorker

def pool(currentLimit, threadFactory=Thread):

    def startThread(target):
        return threadFactory(target=target).start()

    def limitedWorkerCreator():
        stats = team.statistics()
        if stats.busyWorkerCount + stats.idleWorkerCount >= currentLimit():
            return None
        else:
            return ThreadWorker(startThread, Queue())

    team = Team(coordinator=LockWorker(Lock(), LocalStorage()), createWorker=limitedWorkerCreator, logException=err)
    return team
# okay decompiling out\twisted._threads._pool.pyc
