# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.sendmsg
from __future__ import absolute_import, division
from collections import namedtuple
from twisted.python.compat import _PY3
__all__ = [
 'sendmsg', 'recvmsg', 'getSocketFamily', 'SCM_RIGHTS']
if not _PY3:
    from twisted.python._sendmsg import send1msg, recv1msg
    from twisted.python._sendmsg import getsockfam, SCM_RIGHTS
    __all__ += ['send1msg', 'recv1msg', 'getsockfam']
else:
    from socket import SCM_RIGHTS, CMSG_SPACE
RecievedMessage = namedtuple('RecievedMessage', ['data', 'ancillary', 'flags'])

def sendmsg(socket, data, ancillary=[], flags=0):
    if _PY3:
        return socket.sendmsg([data], ancillary, flags)
    else:
        return send1msg(socket.fileno(), data, flags, ancillary)


def recvmsg(socket, maxSize=8192, cmsgSize=4096, flags=0):
    if _PY3:
        data, ancillary, flags = socket.recvmsg(maxSize, CMSG_SPACE(cmsgSize), flags)[0:3]
    else:
        data, flags, ancillary = recv1msg(socket.fileno(), flags, maxSize, cmsgSize)
    return RecievedMessage(data=data, ancillary=ancillary, flags=flags)


def getSocketFamily(socket):
    if _PY3:
        return socket.family
    else:
        return getsockfam(socket.fileno())
# okay decompiling out\twisted.python.sendmsg.pyc
