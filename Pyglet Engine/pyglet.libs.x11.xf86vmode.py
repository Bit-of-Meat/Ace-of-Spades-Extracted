# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.x11.xf86vmode
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
import pyglet.lib
_lib = pyglet.lib.load_library('Xxf86vm')
_int_types = (
 c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t

class c_void(Structure):
    _fields_ = [
     (
      'dummy', c_int)]


import pyglet.libs.x11.xlib
X_XF86VidModeQueryVersion = 0
X_XF86VidModeGetModeLine = 1
X_XF86VidModeModModeLine = 2
X_XF86VidModeSwitchMode = 3
X_XF86VidModeGetMonitor = 4
X_XF86VidModeLockModeSwitch = 5
X_XF86VidModeGetAllModeLines = 6
X_XF86VidModeAddModeLine = 7
X_XF86VidModeDeleteModeLine = 8
X_XF86VidModeValidateModeLine = 9
X_XF86VidModeSwitchToMode = 10
X_XF86VidModeGetViewPort = 11
X_XF86VidModeSetViewPort = 12
X_XF86VidModeGetDotClocks = 13
X_XF86VidModeSetClientVersion = 14
X_XF86VidModeSetGamma = 15
X_XF86VidModeGetGamma = 16
X_XF86VidModeGetGammaRamp = 17
X_XF86VidModeSetGammaRamp = 18
X_XF86VidModeGetGammaRampSize = 19
X_XF86VidModeGetPermissions = 20
CLKFLAG_PROGRAMABLE = 1
XF86VidModeNumberEvents = 0
XF86VidModeBadClock = 0
XF86VidModeBadHTimings = 1
XF86VidModeBadVTimings = 2
XF86VidModeModeUnsuitable = 3
XF86VidModeExtensionDisabled = 4
XF86VidModeClientNotLocal = 5
XF86VidModeZoomLocked = 6
XF86VidModeNumberErrors = 7
XF86VM_READ_PERMISSION = 1
XF86VM_WRITE_PERMISSION = 2

class struct_anon_93(Structure):
    __slots__ = [
     'hdisplay', 
     'hsyncstart', 
     'hsyncend', 
     'htotal', 
     'hskew', 
     'vdisplay', 
     'vsyncstart', 
     'vsyncend', 
     'vtotal', 
     'flags', 
     'privsize', 
     'private']


INT32 = c_int
struct_anon_93._fields_ = [
 (
  'hdisplay', c_ushort),
 (
  'hsyncstart', c_ushort),
 (
  'hsyncend', c_ushort),
 (
  'htotal', c_ushort),
 (
  'hskew', c_ushort),
 (
  'vdisplay', c_ushort),
 (
  'vsyncstart', c_ushort),
 (
  'vsyncend', c_ushort),
 (
  'vtotal', c_ushort),
 (
  'flags', c_uint),
 (
  'privsize', c_int),
 (
  'private', POINTER(INT32))]
XF86VidModeModeLine = struct_anon_93

class struct_anon_94(Structure):
    __slots__ = [
     'dotclock', 
     'hdisplay', 
     'hsyncstart', 
     'hsyncend', 
     'htotal', 
     'hskew', 
     'vdisplay', 
     'vsyncstart', 
     'vsyncend', 
     'vtotal', 
     'flags', 
     'privsize', 
     'private']


struct_anon_94._fields_ = [
 (
  'dotclock', c_uint),
 (
  'hdisplay', c_ushort),
 (
  'hsyncstart', c_ushort),
 (
  'hsyncend', c_ushort),
 (
  'htotal', c_ushort),
 (
  'hskew', c_ushort),
 (
  'vdisplay', c_ushort),
 (
  'vsyncstart', c_ushort),
 (
  'vsyncend', c_ushort),
 (
  'vtotal', c_ushort),
 (
  'flags', c_uint),
 (
  'privsize', c_int),
 (
  'private', POINTER(INT32))]
XF86VidModeModeInfo = struct_anon_94

class struct_anon_95(Structure):
    __slots__ = [
     'hi',
     'lo']


struct_anon_95._fields_ = [
 (
  'hi', c_float),
 (
  'lo', c_float)]
XF86VidModeSyncRange = struct_anon_95

class struct_anon_96(Structure):
    __slots__ = [
     'vendor', 
     'model', 
     'EMPTY', 
     'nhsync', 
     'hsync', 
     'nvsync', 
     'vsync']


struct_anon_96._fields_ = [
 (
  'vendor', c_char_p),
 (
  'model', c_char_p),
 (
  'EMPTY', c_float),
 (
  'nhsync', c_ubyte),
 (
  'hsync', POINTER(XF86VidModeSyncRange)),
 (
  'nvsync', c_ubyte),
 (
  'vsync', POINTER(XF86VidModeSyncRange))]
XF86VidModeMonitor = struct_anon_96

class struct_anon_97(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'root', 
     'state', 
     'kind', 
     'forced', 
     'time']


Display = pyglet.libs.x11.xlib.Display
Window = pyglet.libs.x11.xlib.Window
Time = pyglet.libs.x11.xlib.Time
struct_anon_97._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'root', Window),
 (
  'state', c_int),
 (
  'kind', c_int),
 (
  'forced', c_int),
 (
  'time', Time)]
XF86VidModeNotifyEvent = struct_anon_97

class struct_anon_98(Structure):
    __slots__ = [
     'red',
     'green',
     'blue']


struct_anon_98._fields_ = [
 (
  'red', c_float),
 (
  'green', c_float),
 (
  'blue', c_float)]
XF86VidModeGamma = struct_anon_98
XF86VidModeQueryVersion = _lib.XF86VidModeQueryVersion
XF86VidModeQueryVersion.restype = c_int
XF86VidModeQueryVersion.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XF86VidModeQueryExtension = _lib.XF86VidModeQueryExtension
XF86VidModeQueryExtension.restype = c_int
XF86VidModeQueryExtension.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XF86VidModeSetClientVersion = _lib.XF86VidModeSetClientVersion
XF86VidModeSetClientVersion.restype = c_int
XF86VidModeSetClientVersion.argtypes = [POINTER(Display)]
XF86VidModeGetModeLine = _lib.XF86VidModeGetModeLine
XF86VidModeGetModeLine.restype = c_int
XF86VidModeGetModeLine.argtypes = [POINTER(Display), c_int, POINTER(c_int), POINTER(XF86VidModeModeLine)]
XF86VidModeGetAllModeLines = _lib.XF86VidModeGetAllModeLines
XF86VidModeGetAllModeLines.restype = c_int
XF86VidModeGetAllModeLines.argtypes = [POINTER(Display), c_int, POINTER(c_int), POINTER(POINTER(POINTER(XF86VidModeModeInfo)))]
XF86VidModeAddModeLine = _lib.XF86VidModeAddModeLine
XF86VidModeAddModeLine.restype = c_int
XF86VidModeAddModeLine.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeModeInfo), POINTER(XF86VidModeModeInfo)]
XF86VidModeDeleteModeLine = _lib.XF86VidModeDeleteModeLine
XF86VidModeDeleteModeLine.restype = c_int
XF86VidModeDeleteModeLine.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeModeInfo)]
XF86VidModeModModeLine = _lib.XF86VidModeModModeLine
XF86VidModeModModeLine.restype = c_int
XF86VidModeModModeLine.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeModeLine)]
XF86VidModeValidateModeLine = _lib.XF86VidModeValidateModeLine
XF86VidModeValidateModeLine.restype = c_int
XF86VidModeValidateModeLine.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeModeInfo)]
XF86VidModeSwitchMode = _lib.XF86VidModeSwitchMode
XF86VidModeSwitchMode.restype = c_int
XF86VidModeSwitchMode.argtypes = [POINTER(Display), c_int, c_int]
XF86VidModeSwitchToMode = _lib.XF86VidModeSwitchToMode
XF86VidModeSwitchToMode.restype = c_int
XF86VidModeSwitchToMode.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeModeInfo)]
XF86VidModeLockModeSwitch = _lib.XF86VidModeLockModeSwitch
XF86VidModeLockModeSwitch.restype = c_int
XF86VidModeLockModeSwitch.argtypes = [POINTER(Display), c_int, c_int]
XF86VidModeGetMonitor = _lib.XF86VidModeGetMonitor
XF86VidModeGetMonitor.restype = c_int
XF86VidModeGetMonitor.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeMonitor)]
XF86VidModeGetViewPort = _lib.XF86VidModeGetViewPort
XF86VidModeGetViewPort.restype = c_int
XF86VidModeGetViewPort.argtypes = [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)]
XF86VidModeSetViewPort = _lib.XF86VidModeSetViewPort
XF86VidModeSetViewPort.restype = c_int
XF86VidModeSetViewPort.argtypes = [POINTER(Display), c_int, c_int, c_int]
XF86VidModeGetDotClocks = _lib.XF86VidModeGetDotClocks
XF86VidModeGetDotClocks.restype = c_int
XF86VidModeGetDotClocks.argtypes = [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_int))]
XF86VidModeGetGamma = _lib.XF86VidModeGetGamma
XF86VidModeGetGamma.restype = c_int
XF86VidModeGetGamma.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeGamma)]
XF86VidModeSetGamma = _lib.XF86VidModeSetGamma
XF86VidModeSetGamma.restype = c_int
XF86VidModeSetGamma.argtypes = [POINTER(Display), c_int, POINTER(XF86VidModeGamma)]
XF86VidModeSetGammaRamp = _lib.XF86VidModeSetGammaRamp
XF86VidModeSetGammaRamp.restype = c_int
XF86VidModeSetGammaRamp.argtypes = [POINTER(Display), c_int, c_int, POINTER(c_ushort), POINTER(c_ushort), POINTER(c_ushort)]
XF86VidModeGetGammaRamp = _lib.XF86VidModeGetGammaRamp
XF86VidModeGetGammaRamp.restype = c_int
XF86VidModeGetGammaRamp.argtypes = [POINTER(Display), c_int, c_int, POINTER(c_ushort), POINTER(c_ushort), POINTER(c_ushort)]
XF86VidModeGetGammaRampSize = _lib.XF86VidModeGetGammaRampSize
XF86VidModeGetGammaRampSize.restype = c_int
XF86VidModeGetGammaRampSize.argtypes = [POINTER(Display), c_int, POINTER(c_int)]
XF86VidModeGetPermissions = _lib.XF86VidModeGetPermissions
XF86VidModeGetPermissions.restype = c_int
XF86VidModeGetPermissions.argtypes = [POINTER(Display), c_int, POINTER(c_int)]
__all__ = [
 'X_XF86VidModeQueryVersion', 'X_XF86VidModeGetModeLine', 
 'X_XF86VidModeModModeLine', 
 'X_XF86VidModeSwitchMode', 
 'X_XF86VidModeGetMonitor', 'X_XF86VidModeLockModeSwitch', 
 'X_XF86VidModeGetAllModeLines', 
 'X_XF86VidModeAddModeLine', 
 'X_XF86VidModeDeleteModeLine', 'X_XF86VidModeValidateModeLine', 
 'X_XF86VidModeSwitchToMode', 
 'X_XF86VidModeGetViewPort', 
 'X_XF86VidModeSetViewPort', 'X_XF86VidModeGetDotClocks', 
 'X_XF86VidModeSetClientVersion', 
 'X_XF86VidModeSetGamma', 
 'X_XF86VidModeGetGamma', 'X_XF86VidModeGetGammaRamp', 
 'X_XF86VidModeSetGammaRamp', 
 'X_XF86VidModeGetGammaRampSize', 
 'X_XF86VidModeGetPermissions', 'CLKFLAG_PROGRAMABLE', 
 'XF86VidModeNumberEvents', 
 'XF86VidModeBadClock', 'XF86VidModeBadHTimings', 
 'XF86VidModeBadVTimings', 
 'XF86VidModeModeUnsuitable', 
 'XF86VidModeExtensionDisabled', 'XF86VidModeClientNotLocal', 
 'XF86VidModeZoomLocked', 
 'XF86VidModeNumberErrors', 'XF86VM_READ_PERMISSION', 
 'XF86VM_WRITE_PERMISSION', 
 'XF86VidModeModeLine', 'XF86VidModeModeInfo', 
 'XF86VidModeSyncRange', 'XF86VidModeMonitor', 
 'XF86VidModeNotifyEvent', 
 'XF86VidModeGamma', 'XF86VidModeQueryVersion', 
 'XF86VidModeQueryExtension', 
 'XF86VidModeSetClientVersion', 'XF86VidModeGetModeLine', 
 'XF86VidModeGetAllModeLines', 
 'XF86VidModeAddModeLine', 
 'XF86VidModeDeleteModeLine', 'XF86VidModeModModeLine', 
 'XF86VidModeValidateModeLine', 
 'XF86VidModeSwitchMode', 
 'XF86VidModeSwitchToMode', 'XF86VidModeLockModeSwitch', 
 'XF86VidModeGetMonitor', 
 'XF86VidModeGetViewPort', 'XF86VidModeSetViewPort', 
 'XF86VidModeGetDotClocks', 
 'XF86VidModeGetGamma', 'XF86VidModeSetGamma', 
 'XF86VidModeSetGammaRamp', 
 'XF86VidModeGetGammaRamp', 
 'XF86VidModeGetGammaRampSize', 'XF86VidModeGetPermissions']
# okay decompiling out\pyglet.libs.x11.xf86vmode.pyc
