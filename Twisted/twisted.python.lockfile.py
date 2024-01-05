# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.lockfile
__metaclass__ = type
import errno, os
from time import time as _uniquefloat
from twisted.python.runtime import platform

def unique():
    return str(int(_uniquefloat() * 1000))


from os import rename
if not platform.isWindows():
    from os import kill
    from os import symlink
    from os import readlink
    from os import remove as rmlink
    _windows = False
else:
    _windows = True
    try:
        from win32api import OpenProcess
        import pywintypes
    except ImportError:
        kill = None
    else:
        ERROR_ACCESS_DENIED = 5
        ERROR_INVALID_PARAMETER = 87

        def kill(pid, signal):
            try:
                OpenProcess(0, 0, pid)
            except pywintypes.error as e:
                if e.args[0] == ERROR_ACCESS_DENIED:
                    return
                if e.args[0] == ERROR_INVALID_PARAMETER:
                    raise OSError(errno.ESRCH, None)
                raise
            else:
                raise RuntimeError('OpenProcess is required to fail.')

            return


    _open = file

    def symlink(value, filename):
        newlinkname = filename + '.' + unique() + '.newlink'
        newvalname = os.path.join(newlinkname, 'symlink')
        os.mkdir(newlinkname)
        f = _open(newvalname, 'wcb')
        f.write(value)
        f.flush()
        f.close()
        try:
            rename(newlinkname, filename)
        except:
            os.remove(newvalname)
            os.rmdir(newlinkname)
            raise


    def readlink(filename):
        try:
            fObj = _open(os.path.join(filename, 'symlink'), 'rb')
        except IOError as e:
            if e.errno == errno.ENOENT or e.errno == errno.EIO:
                raise OSError(e.errno, None)
            raise
        else:
            result = fObj.read()
            fObj.close()
            return result

        return


    def rmlink(filename):
        os.remove(os.path.join(filename, 'symlink'))
        os.rmdir(filename)


class FilesystemLock:
    clean = None
    locked = False

    def __init__(self, name):
        self.name = name

    def lock(self):
        clean = True
        while True:
            try:
                symlink(str(os.getpid()), self.name)
            except OSError as e:
                if _windows and e.errno in (errno.EACCES, errno.EIO):
                    return False
                if e.errno == errno.EEXIST:
                    try:
                        pid = readlink(self.name)
                    except OSError as e:
                        if e.errno == errno.ENOENT:
                            continue
                        raise
                    except IOError as e:
                        if _windows and e.errno == errno.EACCES:
                            return False
                        raise

                    try:
                        if kill is not None:
                            kill(int(pid), 0)
                    except OSError as e:
                        if e.errno == errno.ESRCH:
                            try:
                                rmlink(self.name)
                            except OSError as e:
                                if e.errno == errno.ENOENT:
                                    continue
                                raise

                            clean = False
                            continue
                        raise

                    return False
                raise

            self.locked = True
            self.clean = clean
            return True

        return

    def unlock(self):
        pid = readlink(self.name)
        if int(pid) != os.getpid():
            raise ValueError('Lock %r not owned by this process' % (self.name,))
        rmlink(self.name)
        self.locked = False


def isLocked(name):
    l = FilesystemLock(name)
    result = None
    try:
        result = l.lock()
    finally:
        if result:
            l.unlock()

    return not result


__all__ = [
 'FilesystemLock', 'isLocked']
# okay decompiling out\twisted.python.lockfile.pyc
