# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._signals
from __future__ import division, absolute_import
import signal

def installHandler(fd):
    if fd == -1:
        signal.signal(signal.SIGCHLD, signal.SIG_DFL)
    else:

        def noopSignalHandler(*args):
            pass

        signal.signal(signal.SIGCHLD, noopSignalHandler)
        signal.siginterrupt(signal.SIGCHLD, False)
    return signal.set_wakeup_fd(fd)


def isDefaultHandler():
    return signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL
# okay decompiling out\twisted.internet._signals.pyc
