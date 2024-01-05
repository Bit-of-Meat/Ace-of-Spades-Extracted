# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\dummy_thread
__all__ = [
 'error', 'start_new_thread', 'exit', 'get_ident', 'allocate_lock', 
 'interrupt_main', 
 'LockType']
import traceback as _traceback

class error(Exception):

    def __init__(self, *args):
        self.args = args


def start_new_thread(function, args, kwargs={}):
    global _interrupt
    global _main
    if type(args) != type(tuple()):
        raise TypeError('2nd arg must be a tuple')
    if type(kwargs) != type(dict()):
        raise TypeError('3rd arg must be a dict')
    _main = False
    try:
        function(*args, **kwargs)
    except SystemExit:
        pass
    except:
        _traceback.print_exc()

    _main = True
    if _interrupt:
        _interrupt = False
        raise KeyboardInterrupt


def exit():
    raise SystemExit


def get_ident():
    return -1


def allocate_lock():
    return LockType()


def stack_size(size=None):
    if size is not None:
        raise error('setting thread stack size not supported')
    return 0


class LockType(object):

    def __init__(self):
        self.locked_status = False

    def acquire(self, waitflag=None):
        if waitflag is None or waitflag:
            self.locked_status = True
            return True
        else:
            if not self.locked_status:
                self.locked_status = True
                return True
            else:
                return False

            return

    __enter__ = acquire

    def __exit__(self, typ, val, tb):
        self.release()

    def release(self):
        if not self.locked_status:
            raise error
        self.locked_status = False
        return True

    def locked(self):
        return self.locked_status


_interrupt = False
_main = True

def interrupt_main():
    global _interrupt
    if _main:
        raise KeyboardInterrupt
    else:
        _interrupt = True
# okay decompiling out\dummy_thread.pyc
