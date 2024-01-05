# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.media.drivers.openal.lib_alc
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
import sys, pyglet.lib
_lib = pyglet.lib.load_library('openal', win32='openal32', framework='/System/Library/Frameworks/OpenAL.framework')
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


ALC_API = 0
ALCAPI = 0
ALC_INVALID = 0
ALC_VERSION_0_1 = 1

class struct_ALCdevice_struct(Structure):
    __slots__ = []


struct_ALCdevice_struct._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct_ALCdevice_struct(Structure):
    __slots__ = []


struct_ALCdevice_struct._fields_ = [
 (
  '_opaque_struct', c_int)]
ALCdevice = struct_ALCdevice_struct

class struct_ALCcontext_struct(Structure):
    __slots__ = []


struct_ALCcontext_struct._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct_ALCcontext_struct(Structure):
    __slots__ = []


struct_ALCcontext_struct._fields_ = [
 (
  '_opaque_struct', c_int)]
ALCcontext = struct_ALCcontext_struct
ALCboolean = c_char
ALCchar = c_char
ALCbyte = c_char
ALCubyte = c_ubyte
ALCshort = c_short
ALCushort = c_ushort
ALCint = c_int
ALCuint = c_uint
ALCsizei = c_int
ALCenum = c_int
ALCfloat = c_float
ALCdouble = c_double
ALCvoid = None
ALC_FALSE = 0
ALC_TRUE = 1
ALC_FREQUENCY = 4103
ALC_REFRESH = 4104
ALC_SYNC = 4105
ALC_MONO_SOURCES = 4112
ALC_STEREO_SOURCES = 4113
ALC_NO_ERROR = 0
ALC_INVALID_DEVICE = 40961
ALC_INVALID_CONTEXT = 40962
ALC_INVALID_ENUM = 40963
ALC_INVALID_VALUE = 40964
ALC_OUT_OF_MEMORY = 40965
ALC_DEFAULT_DEVICE_SPECIFIER = 4100
ALC_DEVICE_SPECIFIER = 4101
ALC_EXTENSIONS = 4102
ALC_MAJOR_VERSION = 4096
ALC_MINOR_VERSION = 4097
ALC_ATTRIBUTES_SIZE = 4098
ALC_ALL_ATTRIBUTES = 4099
ALC_CAPTURE_DEVICE_SPECIFIER = 784
ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER = 785
ALC_CAPTURE_SAMPLES = 786
alcCreateContext = _lib.alcCreateContext
alcCreateContext.restype = POINTER(ALCcontext)
alcCreateContext.argtypes = [POINTER(ALCdevice), POINTER(ALCint)]
alcMakeContextCurrent = _lib.alcMakeContextCurrent
alcMakeContextCurrent.restype = ALCboolean
alcMakeContextCurrent.argtypes = [POINTER(ALCcontext)]
alcProcessContext = _lib.alcProcessContext
alcProcessContext.restype = None
alcProcessContext.argtypes = [POINTER(ALCcontext)]
alcSuspendContext = _lib.alcSuspendContext
alcSuspendContext.restype = None
alcSuspendContext.argtypes = [POINTER(ALCcontext)]
alcDestroyContext = _lib.alcDestroyContext
alcDestroyContext.restype = None
alcDestroyContext.argtypes = [POINTER(ALCcontext)]
alcGetCurrentContext = _lib.alcGetCurrentContext
alcGetCurrentContext.restype = POINTER(ALCcontext)
alcGetCurrentContext.argtypes = []
alcGetContextsDevice = _lib.alcGetContextsDevice
alcGetContextsDevice.restype = POINTER(ALCdevice)
alcGetContextsDevice.argtypes = [POINTER(ALCcontext)]
alcOpenDevice = _lib.alcOpenDevice
alcOpenDevice.restype = POINTER(ALCdevice)
alcOpenDevice.argtypes = [POINTER(ALCchar)]
alcCloseDevice = _lib.alcCloseDevice
alcCloseDevice.restype = ALCboolean
alcCloseDevice.argtypes = [POINTER(ALCdevice)]
alcGetError = _lib.alcGetError
alcGetError.restype = ALCenum
alcGetError.argtypes = [POINTER(ALCdevice)]
alcIsExtensionPresent = _lib.alcIsExtensionPresent
alcIsExtensionPresent.restype = ALCboolean
alcIsExtensionPresent.argtypes = [POINTER(ALCdevice), POINTER(ALCchar)]
alcGetProcAddress = _lib.alcGetProcAddress
alcGetProcAddress.restype = POINTER(c_void)
alcGetProcAddress.argtypes = [POINTER(ALCdevice), POINTER(ALCchar)]
alcGetEnumValue = _lib.alcGetEnumValue
alcGetEnumValue.restype = ALCenum
alcGetEnumValue.argtypes = [POINTER(ALCdevice), POINTER(ALCchar)]
alcGetString = _lib.alcGetString
alcGetString.restype = POINTER(ALCchar)
alcGetString.argtypes = [POINTER(ALCdevice), ALCenum]
alcGetIntegerv = _lib.alcGetIntegerv
alcGetIntegerv.restype = None
alcGetIntegerv.argtypes = [POINTER(ALCdevice), ALCenum, ALCsizei, POINTER(ALCint)]
alcCaptureOpenDevice = _lib.alcCaptureOpenDevice
alcCaptureOpenDevice.restype = POINTER(ALCdevice)
alcCaptureOpenDevice.argtypes = [POINTER(ALCchar), ALCuint, ALCenum, ALCsizei]
alcCaptureCloseDevice = _lib.alcCaptureCloseDevice
alcCaptureCloseDevice.restype = ALCboolean
alcCaptureCloseDevice.argtypes = [POINTER(ALCdevice)]
alcCaptureStart = _lib.alcCaptureStart
alcCaptureStart.restype = None
alcCaptureStart.argtypes = [POINTER(ALCdevice)]
alcCaptureStop = _lib.alcCaptureStop
alcCaptureStop.restype = None
alcCaptureStop.argtypes = [POINTER(ALCdevice)]
alcCaptureSamples = _lib.alcCaptureSamples
alcCaptureSamples.restype = None
alcCaptureSamples.argtypes = [POINTER(ALCdevice), POINTER(ALCvoid), ALCsizei]
LPALCCREATECONTEXT = CFUNCTYPE(POINTER(ALCcontext), POINTER(ALCdevice), POINTER(ALCint))
LPALCMAKECONTEXTCURRENT = CFUNCTYPE(ALCboolean, POINTER(ALCcontext))
LPALCPROCESSCONTEXT = CFUNCTYPE(None, POINTER(ALCcontext))
LPALCSUSPENDCONTEXT = CFUNCTYPE(None, POINTER(ALCcontext))
LPALCDESTROYCONTEXT = CFUNCTYPE(None, POINTER(ALCcontext))
LPALCGETCURRENTCONTEXT = CFUNCTYPE(POINTER(ALCcontext))
LPALCGETCONTEXTSDEVICE = CFUNCTYPE(POINTER(ALCdevice), POINTER(ALCcontext))
LPALCOPENDEVICE = CFUNCTYPE(POINTER(ALCdevice), POINTER(ALCchar))
LPALCCLOSEDEVICE = CFUNCTYPE(ALCboolean, POINTER(ALCdevice))
LPALCGETERROR = CFUNCTYPE(ALCenum, POINTER(ALCdevice))
LPALCISEXTENSIONPRESENT = CFUNCTYPE(ALCboolean, POINTER(ALCdevice), POINTER(ALCchar))
LPALCGETPROCADDRESS = CFUNCTYPE(POINTER(c_void), POINTER(ALCdevice), POINTER(ALCchar))
LPALCGETENUMVALUE = CFUNCTYPE(ALCenum, POINTER(ALCdevice), POINTER(ALCchar))
LPALCGETSTRING = CFUNCTYPE(POINTER(ALCchar), POINTER(ALCdevice), ALCenum)
LPALCGETINTEGERV = CFUNCTYPE(None, POINTER(ALCdevice), ALCenum, ALCsizei, POINTER(ALCint))
LPALCCAPTUREOPENDEVICE = CFUNCTYPE(POINTER(ALCdevice), POINTER(ALCchar), ALCuint, ALCenum, ALCsizei)
LPALCCAPTURECLOSEDEVICE = CFUNCTYPE(ALCboolean, POINTER(ALCdevice))
LPALCCAPTURESTART = CFUNCTYPE(None, POINTER(ALCdevice))
LPALCCAPTURESTOP = CFUNCTYPE(None, POINTER(ALCdevice))
LPALCCAPTURESAMPLES = CFUNCTYPE(None, POINTER(ALCdevice), POINTER(ALCvoid), ALCsizei)
__all__ = [
 'ALC_API', 'ALCAPI', 'ALC_INVALID', 'ALC_VERSION_0_1', 'ALCdevice', 
 'ALCcontext', 
 'ALCboolean', 'ALCchar', 'ALCbyte', 'ALCubyte', 'ALCshort', 
 'ALCushort', 
 'ALCint', 'ALCuint', 'ALCsizei', 'ALCenum', 'ALCfloat', 
 'ALCdouble', 
 'ALCvoid', 'ALC_FALSE', 'ALC_TRUE', 'ALC_FREQUENCY', 
 'ALC_REFRESH', 'ALC_SYNC', 
 'ALC_MONO_SOURCES', 'ALC_STEREO_SOURCES', 
 'ALC_NO_ERROR', 'ALC_INVALID_DEVICE', 
 'ALC_INVALID_CONTEXT', 
 'ALC_INVALID_ENUM', 'ALC_INVALID_VALUE', 'ALC_OUT_OF_MEMORY', 
 'ALC_DEFAULT_DEVICE_SPECIFIER', 
 'ALC_DEVICE_SPECIFIER', 'ALC_EXTENSIONS', 
 'ALC_MAJOR_VERSION', 'ALC_MINOR_VERSION', 
 'ALC_ATTRIBUTES_SIZE', 
 'ALC_ALL_ATTRIBUTES', 'ALC_CAPTURE_DEVICE_SPECIFIER', 
 'ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER', 
 'ALC_CAPTURE_SAMPLES', 
 'alcCreateContext', 'alcMakeContextCurrent', 'alcProcessContext', 
 'alcSuspendContext', 
 'alcDestroyContext', 'alcGetCurrentContext', 
 'alcGetContextsDevice', 'alcOpenDevice', 
 'alcCloseDevice', 'alcGetError', 
 'alcIsExtensionPresent', 'alcGetProcAddress', 
 'alcGetEnumValue', 
 'alcGetString', 'alcGetIntegerv', 'alcCaptureOpenDevice', 
 'alcCaptureCloseDevice', 
 'alcCaptureStart', 'alcCaptureStop', 
 'alcCaptureSamples', 'LPALCCREATECONTEXT', 
 'LPALCMAKECONTEXTCURRENT', 
 'LPALCPROCESSCONTEXT', 'LPALCSUSPENDCONTEXT', 
 'LPALCDESTROYCONTEXT', 
 'LPALCGETCURRENTCONTEXT', 'LPALCGETCONTEXTSDEVICE', 
 'LPALCOPENDEVICE', 
 'LPALCCLOSEDEVICE', 'LPALCGETERROR', 'LPALCISEXTENSIONPRESENT', 
 'LPALCGETPROCADDRESS', 
 'LPALCGETENUMVALUE', 'LPALCGETSTRING', 
 'LPALCGETINTEGERV', 'LPALCCAPTUREOPENDEVICE', 
 'LPALCCAPTURECLOSEDEVICE', 
 'LPALCCAPTURESTART', 'LPALCCAPTURESTOP', 'LPALCCAPTURESAMPLES']
# okay decompiling out\pyglet.media.drivers.openal.lib_alc.pyc
