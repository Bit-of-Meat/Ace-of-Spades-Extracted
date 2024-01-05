# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.media.drivers.openal.lib_openal
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


AL_API = 0
ALAPI = 0
AL_INVALID = -1
AL_ILLEGAL_ENUM = 0
AL_ILLEGAL_COMMAND = 0
ALboolean = c_int
ALchar = c_char
ALbyte = c_char
ALubyte = c_ubyte
ALshort = c_short
ALushort = c_ushort
ALint = c_int
ALuint = c_uint
ALsizei = c_int
ALenum = c_int
ALfloat = c_float
ALdouble = c_double
ALvoid = None
AL_NONE = 0
AL_FALSE = 0
AL_TRUE = 1
AL_SOURCE_RELATIVE = 514
AL_CONE_INNER_ANGLE = 4097
AL_CONE_OUTER_ANGLE = 4098
AL_PITCH = 4099
AL_POSITION = 4100
AL_DIRECTION = 4101
AL_VELOCITY = 4102
AL_LOOPING = 4103
AL_BUFFER = 4105
AL_GAIN = 4106
AL_MIN_GAIN = 4109
AL_MAX_GAIN = 4110
AL_ORIENTATION = 4111
AL_SOURCE_STATE = 4112
AL_INITIAL = 4113
AL_PLAYING = 4114
AL_PAUSED = 4115
AL_STOPPED = 4116
AL_BUFFERS_QUEUED = 4117
AL_BUFFERS_PROCESSED = 4118
AL_SEC_OFFSET = 4132
AL_SAMPLE_OFFSET = 4133
AL_BYTE_OFFSET = 4134
AL_SOURCE_TYPE = 4135
AL_STATIC = 4136
AL_STREAMING = 4137
AL_UNDETERMINED = 4144
AL_FORMAT_MONO8 = 4352
AL_FORMAT_MONO16 = 4353
AL_FORMAT_STEREO8 = 4354
AL_FORMAT_STEREO16 = 4355
AL_REFERENCE_DISTANCE = 4128
AL_ROLLOFF_FACTOR = 4129
AL_CONE_OUTER_GAIN = 4130
AL_MAX_DISTANCE = 4131
AL_FREQUENCY = 8193
AL_BITS = 8194
AL_CHANNELS = 8195
AL_SIZE = 8196
AL_UNUSED = 8208
AL_PENDING = 8209
AL_PROCESSED = 8210
AL_NO_ERROR = 0
AL_INVALID_NAME = 40961
AL_INVALID_ENUM = 40962
AL_INVALID_VALUE = 40963
AL_INVALID_OPERATION = 40964
AL_OUT_OF_MEMORY = 40965
AL_VENDOR = 45057
AL_VERSION = 45058
AL_RENDERER = 45059
AL_EXTENSIONS = 45060
AL_DOPPLER_FACTOR = 49152
AL_DOPPLER_VELOCITY = 49153
AL_SPEED_OF_SOUND = 49155
AL_DISTANCE_MODEL = 53248
AL_INVERSE_DISTANCE = 53249
AL_INVERSE_DISTANCE_CLAMPED = 53250
AL_LINEAR_DISTANCE = 53251
AL_LINEAR_DISTANCE_CLAMPED = 53252
AL_EXPONENT_DISTANCE = 53253
AL_EXPONENT_DISTANCE_CLAMPED = 53254
alEnable = _lib.alEnable
alEnable.restype = None
alEnable.argtypes = [ALenum]
alDisable = _lib.alDisable
alDisable.restype = None
alDisable.argtypes = [ALenum]
alIsEnabled = _lib.alIsEnabled
alIsEnabled.restype = ALboolean
alIsEnabled.argtypes = [ALenum]
alGetString = _lib.alGetString
alGetString.restype = POINTER(ALchar)
alGetString.argtypes = [ALenum]
alGetBooleanv = _lib.alGetBooleanv
alGetBooleanv.restype = None
alGetBooleanv.argtypes = [ALenum, POINTER(ALboolean)]
alGetIntegerv = _lib.alGetIntegerv
alGetIntegerv.restype = None
alGetIntegerv.argtypes = [ALenum, POINTER(ALint)]
alGetFloatv = _lib.alGetFloatv
alGetFloatv.restype = None
alGetFloatv.argtypes = [ALenum, POINTER(ALfloat)]
alGetDoublev = _lib.alGetDoublev
alGetDoublev.restype = None
alGetDoublev.argtypes = [ALenum, POINTER(ALdouble)]
alGetBoolean = _lib.alGetBoolean
alGetBoolean.restype = ALboolean
alGetBoolean.argtypes = [ALenum]
alGetInteger = _lib.alGetInteger
alGetInteger.restype = ALint
alGetInteger.argtypes = [ALenum]
alGetFloat = _lib.alGetFloat
alGetFloat.restype = ALfloat
alGetFloat.argtypes = [ALenum]
alGetDouble = _lib.alGetDouble
alGetDouble.restype = ALdouble
alGetDouble.argtypes = [ALenum]
alGetError = _lib.alGetError
alGetError.restype = ALenum
alGetError.argtypes = []
alIsExtensionPresent = _lib.alIsExtensionPresent
alIsExtensionPresent.restype = ALboolean
alIsExtensionPresent.argtypes = [POINTER(ALchar)]
alGetProcAddress = _lib.alGetProcAddress
alGetProcAddress.restype = POINTER(c_void)
alGetProcAddress.argtypes = [POINTER(ALchar)]
alGetEnumValue = _lib.alGetEnumValue
alGetEnumValue.restype = ALenum
alGetEnumValue.argtypes = [POINTER(ALchar)]
alListenerf = _lib.alListenerf
alListenerf.restype = None
alListenerf.argtypes = [ALenum, ALfloat]
alListener3f = _lib.alListener3f
alListener3f.restype = None
alListener3f.argtypes = [ALenum, ALfloat, ALfloat, ALfloat]
alListenerfv = _lib.alListenerfv
alListenerfv.restype = None
alListenerfv.argtypes = [ALenum, POINTER(ALfloat)]
alListeneri = _lib.alListeneri
alListeneri.restype = None
alListeneri.argtypes = [ALenum, ALint]
alGetListenerf = _lib.alGetListenerf
alGetListenerf.restype = None
alGetListenerf.argtypes = [ALenum, POINTER(ALfloat)]
alGetListener3f = _lib.alGetListener3f
alGetListener3f.restype = None
alGetListener3f.argtypes = [ALenum, POINTER(ALfloat), POINTER(ALfloat), POINTER(ALfloat)]
alGetListenerfv = _lib.alGetListenerfv
alGetListenerfv.restype = None
alGetListenerfv.argtypes = [ALenum, POINTER(ALfloat)]
alGetListeneri = _lib.alGetListeneri
alGetListeneri.restype = None
alGetListeneri.argtypes = [ALenum, POINTER(ALint)]
alGetListener3i = _lib.alGetListener3i
alGetListener3i.restype = None
alGetListener3i.argtypes = [ALenum, POINTER(ALint), POINTER(ALint), POINTER(ALint)]
alGetListeneriv = _lib.alGetListeneriv
alGetListeneriv.restype = None
alGetListeneriv.argtypes = [ALenum, POINTER(ALint)]
alGenSources = _lib.alGenSources
alGenSources.restype = None
alGenSources.argtypes = [ALsizei, POINTER(ALuint)]
alDeleteSources = _lib.alDeleteSources
alDeleteSources.restype = None
alDeleteSources.argtypes = [ALsizei, POINTER(ALuint)]
alIsSource = _lib.alIsSource
alIsSource.restype = ALboolean
alIsSource.argtypes = [ALuint]
alSourcef = _lib.alSourcef
alSourcef.restype = None
alSourcef.argtypes = [ALuint, ALenum, ALfloat]
alSource3f = _lib.alSource3f
alSource3f.restype = None
alSource3f.argtypes = [ALuint, ALenum, ALfloat, ALfloat, ALfloat]
alSourcefv = _lib.alSourcefv
alSourcefv.restype = None
alSourcefv.argtypes = [ALuint, ALenum, POINTER(ALfloat)]
alSourcei = _lib.alSourcei
alSourcei.restype = None
alSourcei.argtypes = [ALuint, ALenum, ALint]
alGetSourcef = _lib.alGetSourcef
alGetSourcef.restype = None
alGetSourcef.argtypes = [ALuint, ALenum, POINTER(ALfloat)]
alGetSource3f = _lib.alGetSource3f
alGetSource3f.restype = None
alGetSource3f.argtypes = [ALuint, ALenum, POINTER(ALfloat), POINTER(ALfloat), POINTER(ALfloat)]
alGetSourcefv = _lib.alGetSourcefv
alGetSourcefv.restype = None
alGetSourcefv.argtypes = [ALuint, ALenum, POINTER(ALfloat)]
alGetSourcei = _lib.alGetSourcei
alGetSourcei.restype = None
alGetSourcei.argtypes = [ALuint, ALenum, POINTER(ALint)]
alGetSourceiv = _lib.alGetSourceiv
alGetSourceiv.restype = None
alGetSourceiv.argtypes = [ALuint, ALenum, POINTER(ALint)]
alSourcePlayv = _lib.alSourcePlayv
alSourcePlayv.restype = None
alSourcePlayv.argtypes = [ALsizei, POINTER(ALuint)]
alSourceStopv = _lib.alSourceStopv
alSourceStopv.restype = None
alSourceStopv.argtypes = [ALsizei, POINTER(ALuint)]
alSourceRewindv = _lib.alSourceRewindv
alSourceRewindv.restype = None
alSourceRewindv.argtypes = [ALsizei, POINTER(ALuint)]
alSourcePausev = _lib.alSourcePausev
alSourcePausev.restype = None
alSourcePausev.argtypes = [ALsizei, POINTER(ALuint)]
alSourcePlay = _lib.alSourcePlay
alSourcePlay.restype = None
alSourcePlay.argtypes = [ALuint]
alSourceStop = _lib.alSourceStop
alSourceStop.restype = None
alSourceStop.argtypes = [ALuint]
alSourceRewind = _lib.alSourceRewind
alSourceRewind.restype = None
alSourceRewind.argtypes = [ALuint]
alSourcePause = _lib.alSourcePause
alSourcePause.restype = None
alSourcePause.argtypes = [ALuint]
alSourceQueueBuffers = _lib.alSourceQueueBuffers
alSourceQueueBuffers.restype = None
alSourceQueueBuffers.argtypes = [ALuint, ALsizei, POINTER(ALuint)]
alSourceUnqueueBuffers = _lib.alSourceUnqueueBuffers
alSourceUnqueueBuffers.restype = None
alSourceUnqueueBuffers.argtypes = [ALuint, ALsizei, POINTER(ALuint)]
alGenBuffers = _lib.alGenBuffers
alGenBuffers.restype = None
alGenBuffers.argtypes = [ALsizei, POINTER(ALuint)]
alDeleteBuffers = _lib.alDeleteBuffers
alDeleteBuffers.restype = None
alDeleteBuffers.argtypes = [ALsizei, POINTER(ALuint)]
alIsBuffer = _lib.alIsBuffer
alIsBuffer.restype = ALboolean
alIsBuffer.argtypes = [ALuint]
alBufferData = _lib.alBufferData
alBufferData.restype = None
alBufferData.argtypes = [ALuint, ALenum, POINTER(ALvoid), ALsizei, ALsizei]
alBufferf = _lib.alBufferf
alBufferf.restype = None
alBufferf.argtypes = [ALuint, ALenum, ALfloat]
alBuffer3f = _lib.alBuffer3f
alBuffer3f.restype = None
alBuffer3f.argtypes = [ALuint, ALenum, ALfloat, ALfloat, ALfloat]
alBufferfv = _lib.alBufferfv
alBufferfv.restype = None
alBufferfv.argtypes = [ALuint, ALenum, POINTER(ALfloat)]
alBufferi = _lib.alBufferi
alBufferi.restype = None
alBufferi.argtypes = [ALuint, ALenum, ALint]
alBuffer3i = _lib.alBuffer3i
alBuffer3i.restype = None
alBuffer3i.argtypes = [ALuint, ALenum, ALint, ALint, ALint]
alBufferiv = _lib.alBufferiv
alBufferiv.restype = None
alBufferiv.argtypes = [ALuint, ALenum, POINTER(ALint)]
alGetBufferf = _lib.alGetBufferf
alGetBufferf.restype = None
alGetBufferf.argtypes = [ALuint, ALenum, POINTER(ALfloat)]
alGetBuffer3f = _lib.alGetBuffer3f
alGetBuffer3f.restype = None
alGetBuffer3f.argtypes = [ALuint, ALenum, POINTER(ALfloat), POINTER(ALfloat), POINTER(ALfloat)]
alGetBufferfv = _lib.alGetBufferfv
alGetBufferfv.restype = None
alGetBufferfv.argtypes = [ALuint, ALenum, POINTER(ALfloat)]
alGetBufferi = _lib.alGetBufferi
alGetBufferi.restype = None
alGetBufferi.argtypes = [ALuint, ALenum, POINTER(ALint)]
alGetBuffer3i = _lib.alGetBuffer3i
alGetBuffer3i.restype = None
alGetBuffer3i.argtypes = [ALuint, ALenum, POINTER(ALint), POINTER(ALint), POINTER(ALint)]
alGetBufferiv = _lib.alGetBufferiv
alGetBufferiv.restype = None
alGetBufferiv.argtypes = [ALuint, ALenum, POINTER(ALint)]
alDopplerFactor = _lib.alDopplerFactor
alDopplerFactor.restype = None
alDopplerFactor.argtypes = [ALfloat]
alDopplerVelocity = _lib.alDopplerVelocity
alDopplerVelocity.restype = None
alDopplerVelocity.argtypes = [ALfloat]
alSpeedOfSound = _lib.alSpeedOfSound
alSpeedOfSound.restype = None
alSpeedOfSound.argtypes = [ALfloat]
alDistanceModel = _lib.alDistanceModel
alDistanceModel.restype = None
alDistanceModel.argtypes = [ALenum]
LPALENABLE = CFUNCTYPE(None, ALenum)
LPALDISABLE = CFUNCTYPE(None, ALenum)
LPALISENABLED = CFUNCTYPE(ALboolean, ALenum)
LPALGETSTRING = CFUNCTYPE(POINTER(ALchar), ALenum)
LPALGETBOOLEANV = CFUNCTYPE(None, ALenum, POINTER(ALboolean))
LPALGETINTEGERV = CFUNCTYPE(None, ALenum, POINTER(ALint))
LPALGETFLOATV = CFUNCTYPE(None, ALenum, POINTER(ALfloat))
LPALGETDOUBLEV = CFUNCTYPE(None, ALenum, POINTER(ALdouble))
LPALGETBOOLEAN = CFUNCTYPE(ALboolean, ALenum)
LPALGETINTEGER = CFUNCTYPE(ALint, ALenum)
LPALGETFLOAT = CFUNCTYPE(ALfloat, ALenum)
LPALGETDOUBLE = CFUNCTYPE(ALdouble, ALenum)
LPALGETERROR = CFUNCTYPE(ALenum)
LPALISEXTENSIONPRESENT = CFUNCTYPE(ALboolean, POINTER(ALchar))
LPALGETPROCADDRESS = CFUNCTYPE(POINTER(c_void), POINTER(ALchar))
LPALGETENUMVALUE = CFUNCTYPE(ALenum, POINTER(ALchar))
LPALLISTENERF = CFUNCTYPE(None, ALenum, ALfloat)
LPALLISTENER3F = CFUNCTYPE(None, ALenum, ALfloat, ALfloat, ALfloat)
LPALLISTENERFV = CFUNCTYPE(None, ALenum, POINTER(ALfloat))
LPALLISTENERI = CFUNCTYPE(None, ALenum, ALint)
LPALLISTENER3I = CFUNCTYPE(None, ALenum, ALint, ALint, ALint)
LPALLISTENERIV = CFUNCTYPE(None, ALenum, POINTER(ALint))
LPALGETLISTENERF = CFUNCTYPE(None, ALenum, POINTER(ALfloat))
LPALGETLISTENER3F = CFUNCTYPE(None, ALenum, POINTER(ALfloat), POINTER(ALfloat), POINTER(ALfloat))
LPALGETLISTENERFV = CFUNCTYPE(None, ALenum, POINTER(ALfloat))
LPALGETLISTENERI = CFUNCTYPE(None, ALenum, POINTER(ALint))
LPALGETLISTENER3I = CFUNCTYPE(None, ALenum, POINTER(ALint), POINTER(ALint), POINTER(ALint))
LPALGETLISTENERIV = CFUNCTYPE(None, ALenum, POINTER(ALint))
LPALGENSOURCES = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALDELETESOURCES = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALISSOURCE = CFUNCTYPE(ALboolean, ALuint)
LPALSOURCEF = CFUNCTYPE(None, ALuint, ALenum, ALfloat)
LPALSOURCE3F = CFUNCTYPE(None, ALuint, ALenum, ALfloat, ALfloat, ALfloat)
LPALSOURCEFV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat))
LPALSOURCEI = CFUNCTYPE(None, ALuint, ALenum, ALint)
LPALSOURCE3I = CFUNCTYPE(None, ALuint, ALenum, ALint, ALint, ALint)
LPALSOURCEIV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint))
LPALGETSOURCEF = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat))
LPALGETSOURCE3F = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat), POINTER(ALfloat), POINTER(ALfloat))
LPALGETSOURCEFV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat))
LPALGETSOURCEI = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint))
LPALGETSOURCE3I = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint), POINTER(ALint), POINTER(ALint))
LPALGETSOURCEIV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint))
LPALSOURCEPLAYV = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALSOURCESTOPV = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALSOURCEREWINDV = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALSOURCEPAUSEV = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALSOURCEPLAY = CFUNCTYPE(None, ALuint)
LPALSOURCESTOP = CFUNCTYPE(None, ALuint)
LPALSOURCEREWIND = CFUNCTYPE(None, ALuint)
LPALSOURCEPAUSE = CFUNCTYPE(None, ALuint)
LPALSOURCEQUEUEBUFFERS = CFUNCTYPE(None, ALuint, ALsizei, POINTER(ALuint))
LPALSOURCEUNQUEUEBUFFERS = CFUNCTYPE(None, ALuint, ALsizei, POINTER(ALuint))
LPALGENBUFFERS = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALDELETEBUFFERS = CFUNCTYPE(None, ALsizei, POINTER(ALuint))
LPALISBUFFER = CFUNCTYPE(ALboolean, ALuint)
LPALBUFFERDATA = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALvoid), ALsizei, ALsizei)
LPALBUFFERF = CFUNCTYPE(None, ALuint, ALenum, ALfloat)
LPALBUFFER3F = CFUNCTYPE(None, ALuint, ALenum, ALfloat, ALfloat, ALfloat)
LPALBUFFERFV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat))
LPALBUFFERI = CFUNCTYPE(None, ALuint, ALenum, ALint)
LPALBUFFER3I = CFUNCTYPE(None, ALuint, ALenum, ALint, ALint, ALint)
LPALBUFFERIV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint))
LPALGETBUFFERF = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat))
LPALGETBUFFER3F = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat), POINTER(ALfloat), POINTER(ALfloat))
LPALGETBUFFERFV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALfloat))
LPALGETBUFFERI = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint))
LPALGETBUFFER3I = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint), POINTER(ALint), POINTER(ALint))
LPALGETBUFFERIV = CFUNCTYPE(None, ALuint, ALenum, POINTER(ALint))
LPALDOPPLERFACTOR = CFUNCTYPE(None, ALfloat)
LPALDOPPLERVELOCITY = CFUNCTYPE(None, ALfloat)
LPALSPEEDOFSOUND = CFUNCTYPE(None, ALfloat)
LPALDISTANCEMODEL = CFUNCTYPE(None, ALenum)
__all__ = [
 'AL_API', 'ALAPI', 'AL_INVALID', 'AL_ILLEGAL_ENUM', 
 'AL_ILLEGAL_COMMAND', 
 'ALboolean', 'ALchar', 'ALbyte', 'ALubyte', 'ALshort', 
 'ALushort', 'ALint', 
 'ALuint', 'ALsizei', 'ALenum', 'ALfloat', 'ALdouble', 
 'ALvoid', 'AL_NONE', 
 'AL_FALSE', 'AL_TRUE', 'AL_SOURCE_RELATIVE', 
 'AL_CONE_INNER_ANGLE', 'AL_CONE_OUTER_ANGLE', 
 'AL_PITCH', 'AL_POSITION', 
 'AL_DIRECTION', 'AL_VELOCITY', 'AL_LOOPING', 
 'AL_BUFFER', 'AL_GAIN', 
 'AL_MIN_GAIN', 'AL_MAX_GAIN', 'AL_ORIENTATION', 
 'AL_SOURCE_STATE', 
 'AL_INITIAL', 'AL_PLAYING', 'AL_PAUSED', 'AL_STOPPED', 
 'AL_BUFFERS_QUEUED', 
 'AL_BUFFERS_PROCESSED', 'AL_SEC_OFFSET', 'AL_SAMPLE_OFFSET', 
 'AL_BYTE_OFFSET', 
 'AL_SOURCE_TYPE', 'AL_STATIC', 'AL_STREAMING', 'AL_UNDETERMINED', 
 'AL_FORMAT_MONO8', 
 'AL_FORMAT_MONO16', 'AL_FORMAT_STEREO8', 
 'AL_FORMAT_STEREO16', 'AL_REFERENCE_DISTANCE', 
 'AL_ROLLOFF_FACTOR', 
 'AL_CONE_OUTER_GAIN', 'AL_MAX_DISTANCE', 'AL_FREQUENCY', 
 'AL_BITS', 
 'AL_CHANNELS', 'AL_SIZE', 'AL_UNUSED', 'AL_PENDING', 'AL_PROCESSED', 
 'AL_NO_ERROR', 
 'AL_INVALID_NAME', 'AL_INVALID_ENUM', 'AL_INVALID_VALUE', 
 'AL_INVALID_OPERATION', 
 'AL_OUT_OF_MEMORY', 'AL_VENDOR', 'AL_VERSION', 
 'AL_RENDERER', 'AL_EXTENSIONS', 
 'AL_DOPPLER_FACTOR', 'AL_DOPPLER_VELOCITY', 
 'AL_SPEED_OF_SOUND', 'AL_DISTANCE_MODEL', 
 'AL_INVERSE_DISTANCE', 
 'AL_INVERSE_DISTANCE_CLAMPED', 'AL_LINEAR_DISTANCE', 
 'AL_LINEAR_DISTANCE_CLAMPED', 
 'AL_EXPONENT_DISTANCE', 
 'AL_EXPONENT_DISTANCE_CLAMPED', 'alEnable', 'alDisable', 
 'alIsEnabled', 
 'alGetString', 'alGetBooleanv', 'alGetIntegerv', 'alGetFloatv', 
 'alGetDoublev', 
 'alGetBoolean', 'alGetInteger', 'alGetFloat', 'alGetDouble', 
 'alGetError', 
 'alIsExtensionPresent', 'alGetProcAddress', 'alGetEnumValue', 
 'alListenerf', 
 'alListener3f', 'alListenerfv', 'alListeneri', 'alListener3i', 
 'alListeneriv', 
 'alGetListenerf', 'alGetListener3f', 'alGetListenerfv', 
 'alGetListeneri', 
 'alGetListener3i', 'alGetListeneriv', 'alGenSources', 
 'alDeleteSources', 
 'alIsSource', 'alSourcef', 'alSource3f', 'alSourcefv', 
 'alSourcei', 'alSource3i', 
 'alSourceiv', 'alGetSourcef', 'alGetSource3f', 
 'alGetSourcefv', 'alGetSourcei', 
 'alGetSource3i', 'alGetSourceiv', 
 'alSourcePlayv', 'alSourceStopv', 'alSourceRewindv', 
 'alSourcePausev', 
 'alSourcePlay', 'alSourceStop', 'alSourceRewind', 'alSourcePause', 
 'alSourceQueueBuffers', 
 'alSourceUnqueueBuffers', 'alGenBuffers', 
 'alDeleteBuffers', 'alIsBuffer', 
 'alBufferData', 'alBufferf', 'alBuffer3f', 
 'alBufferfv', 'alBufferi', 
 'alBuffer3i', 'alBufferiv', 'alGetBufferf', 
 'alGetBuffer3f', 'alGetBufferfv', 
 'alGetBufferi', 'alGetBuffer3i', 
 'alGetBufferiv', 'alDopplerFactor', 'alDopplerVelocity', 
 'alSpeedOfSound', 
 'alDistanceModel', 'LPALENABLE', 'LPALDISABLE', 'LPALISENABLED', 
 'LPALGETSTRING', 
 'LPALGETBOOLEANV', 'LPALGETINTEGERV', 'LPALGETFLOATV', 
 'LPALGETDOUBLEV', 
 'LPALGETBOOLEAN', 'LPALGETINTEGER', 'LPALGETFLOAT', 
 'LPALGETDOUBLE', 'LPALGETERROR', 
 'LPALISEXTENSIONPRESENT', 
 'LPALGETPROCADDRESS', 'LPALGETENUMVALUE', 'LPALLISTENERF', 
 'LPALLISTENER3F', 
 'LPALLISTENERFV', 'LPALLISTENERI', 'LPALLISTENER3I', 
 'LPALLISTENERIV', 
 'LPALGETLISTENERF', 'LPALGETLISTENER3F', 'LPALGETLISTENERFV', 
 'LPALGETLISTENERI', 
 'LPALGETLISTENER3I', 'LPALGETLISTENERIV', 
 'LPALGENSOURCES', 'LPALDELETESOURCES', 
 'LPALISSOURCE', 'LPALSOURCEF', 
 'LPALSOURCE3F', 'LPALSOURCEFV', 'LPALSOURCEI', 
 'LPALSOURCE3I', 'LPALSOURCEIV', 
 'LPALGETSOURCEF', 'LPALGETSOURCE3F', 'LPALGETSOURCEFV', 
 'LPALGETSOURCEI', 
 'LPALGETSOURCE3I', 'LPALGETSOURCEIV', 'LPALSOURCEPLAYV', 
 'LPALSOURCESTOPV', 
 'LPALSOURCEREWINDV', 'LPALSOURCEPAUSEV', 'LPALSOURCEPLAY', 
 'LPALSOURCESTOP', 
 'LPALSOURCEREWIND', 'LPALSOURCEPAUSE', 'LPALSOURCEQUEUEBUFFERS', 
 'LPALSOURCEUNQUEUEBUFFERS', 
 'LPALGENBUFFERS', 'LPALDELETEBUFFERS', 
 'LPALISBUFFER', 'LPALBUFFERDATA', 
 'LPALBUFFERF', 'LPALBUFFER3F', 
 'LPALBUFFERFV', 'LPALBUFFERI', 'LPALBUFFER3I', 
 'LPALBUFFERIV', 
 'LPALGETBUFFERF', 'LPALGETBUFFER3F', 'LPALGETBUFFERFV', 
 'LPALGETBUFFERI', 
 'LPALGETBUFFER3I', 'LPALGETBUFFERIV', 'LPALDOPPLERFACTOR', 
 'LPALDOPPLERVELOCITY', 
 'LPALSPEEDOFSOUND', 'LPALDISTANCEMODEL']
# okay decompiling out\pyglet.media.drivers.openal.lib_openal.pyc
