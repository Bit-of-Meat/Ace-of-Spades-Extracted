# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.fdesc
import os, errno
try:
    import fcntl
except ImportError:
    fcntl = None

from twisted.internet.main import CONNECTION_LOST, CONNECTION_DONE

def setNonBlocking(fd):
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    flags = flags | os.O_NONBLOCK
    fcntl.fcntl(fd, fcntl.F_SETFL, flags)


def setBlocking(fd):
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    flags = flags & ~os.O_NONBLOCK
    fcntl.fcntl(fd, fcntl.F_SETFL, flags)


if fcntl is None:
    _setCloseOnExec = _unsetCloseOnExec = lambda fd: None
else:

    def _setCloseOnExec(fd):
        flags = fcntl.fcntl(fd, fcntl.F_GETFD)
        flags = flags | fcntl.FD_CLOEXEC
        fcntl.fcntl(fd, fcntl.F_SETFD, flags)


    def _unsetCloseOnExec(fd):
        flags = fcntl.fcntl(fd, fcntl.F_GETFD)
        flags = flags & ~fcntl.FD_CLOEXEC
        fcntl.fcntl(fd, fcntl.F_SETFD, flags)


def readFromFD(fd, callback):
    try:
        output = os.read(fd, 8192)
    except (OSError, IOError) as ioe:
        if ioe.args[0] in (errno.EAGAIN, errno.EINTR):
            return
        else:
            return CONNECTION_LOST

    if not output:
        return CONNECTION_DONE
    callback(output)


def writeToFD(fd, data):
    try:
        return os.write(fd, data)
    except (OSError, IOError) as io:
        if io.errno in (errno.EAGAIN, errno.EINTR):
            return 0
        return CONNECTION_LOST


__all__ = [
 'setNonBlocking', 'setBlocking', 'readFromFD', 'writeToFD']
# okay decompiling out\twisted.internet.fdesc.pyc
