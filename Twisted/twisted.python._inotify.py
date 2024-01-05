# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python._inotify
import ctypes, ctypes.util

class INotifyError(Exception):
    pass


def init():
    fd = libc.inotify_init()
    if fd < 0:
        raise INotifyError('INotify initialization error.')
    return fd


def add(fd, path, mask):
    wd = libc.inotify_add_watch(fd, path, mask)
    if wd < 0:
        raise INotifyError("Failed to add watch on '%r' - (%r)" % (path, wd))
    return wd


def remove(fd, wd):
    libc.inotify_rm_watch(fd, wd)


def initializeModule(libc):
    for function in ('inotify_add_watch', 'inotify_init', 'inotify_rm_watch'):
        if getattr(libc, function, None) is None:
            raise ImportError('libc6 2.4 or higher needed')

    libc.inotify_init.argtypes = []
    libc.inotify_init.restype = ctypes.c_int
    libc.inotify_rm_watch.argtypes = [
     ctypes.c_int, ctypes.c_int]
    libc.inotify_rm_watch.restype = ctypes.c_int
    libc.inotify_add_watch.argtypes = [
     ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32]
    libc.inotify_add_watch.restype = ctypes.c_int
    return


name = ctypes.util.find_library('c')
if not name:
    raise ImportError("Can't find C library.")
libc = ctypes.cdll.LoadLibrary(name)
initializeModule(libc)
# okay decompiling out\twisted.python._inotify.pyc
