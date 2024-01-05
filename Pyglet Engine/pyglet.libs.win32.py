# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.win32
from ctypes import *
import pyglet, constants
from types import *
_debug_win32 = pyglet.options['debug_win32']
if _debug_win32:
    import traceback
    _GetLastError = windll.kernel32.GetLastError
    _SetLastError = windll.kernel32.SetLastError
    _FormatMessageA = windll.kernel32.FormatMessageA
    _log_win32 = open('debug_win32.log', 'w')

    def format_error(err):
        msg = create_string_buffer(256)
        _FormatMessageA(constants.FORMAT_MESSAGE_FROM_SYSTEM, c_void_p(), err, 0, msg, len(msg), c_void_p())
        return msg.value


    class DebugLibrary(object):

        def __init__(self, lib):
            self.lib = lib

        def __getattr__(self, name):
            fn = getattr(self.lib, name)

            def f(*args):
                _SetLastError(0)
                result = fn(*args)
                err = _GetLastError()
                if err != 0:
                    for entry in traceback.format_list(traceback.extract_stack()[:-1]):
                        _log_win32.write(entry)

                    print >> _log_win32, format_error(err)
                return result

            return f


else:
    DebugLibrary = lambda lib: lib
_gdi32 = DebugLibrary(windll.gdi32)
_kernel32 = DebugLibrary(windll.kernel32)
_user32 = DebugLibrary(windll.user32)
_user32.GetKeyState.restype = c_short
_gdi32.CreateDIBitmap.argtypes = [HDC, POINTER(BITMAPINFOHEADER), DWORD,
 c_void_p, POINTER(BITMAPINFO), c_uint]
_user32.MsgWaitForMultipleObjects.argtypes = [
 DWORD, POINTER(HANDLE), BOOL, DWORD, DWORD]
_user32.MsgWaitForMultipleObjects.restype = DWORD
_gdi32.SwapBuffers.restype = BOOL
_gdi32.SwapBuffers.argtypes = [HDC]
# okay decompiling out\pyglet.libs.win32.pyc
