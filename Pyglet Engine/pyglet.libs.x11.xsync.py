# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.x11.xsync
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
import pyglet.lib
_lib = pyglet.lib.load_library('Xext')
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


import xlib
SYNC_MAJOR_VERSION = 3
SYNC_MINOR_VERSION = 0
X_SyncInitialize = 0
X_SyncListSystemCounters = 1
X_SyncCreateCounter = 2
X_SyncSetCounter = 3
X_SyncChangeCounter = 4
X_SyncQueryCounter = 5
X_SyncDestroyCounter = 6
X_SyncAwait = 7
X_SyncCreateAlarm = 8
X_SyncChangeAlarm = 9
X_SyncQueryAlarm = 10
X_SyncDestroyAlarm = 11
X_SyncSetPriority = 12
X_SyncGetPriority = 13
XSyncCounterNotify = 0
XSyncAlarmNotify = 1
XSyncAlarmNotifyMask = 2
XSyncNumberEvents = 2
XSyncBadCounter = 0
XSyncBadAlarm = 1
XSyncNumberErrors = 2
XSyncCACounter = 1
XSyncCAValueType = 2
XSyncCAValue = 4
XSyncCATestType = 8
XSyncCADelta = 16
XSyncCAEvents = 32
enum_anon_93 = c_int
XSyncAbsolute = 0
XSyncRelative = 1
XSyncValueType = enum_anon_93
enum_anon_94 = c_int
XSyncPositiveTransition = 0
XSyncNegativeTransition = 1
XSyncPositiveComparison = 2
XSyncNegativeComparison = 3
XSyncTestType = enum_anon_94
enum_anon_95 = c_int
XSyncAlarmActive = 0
XSyncAlarmInactive = 1
XSyncAlarmDestroyed = 2
XSyncAlarmState = enum_anon_95
XID = xlib.XID
XSyncCounter = XID
XSyncAlarm = XID

class struct__XSyncValue(Structure):
    __slots__ = [
     'hi',
     'lo']


struct__XSyncValue._fields_ = [
 (
  'hi', c_int),
 (
  'lo', c_uint)]
XSyncValue = struct__XSyncValue
XSyncIntToValue = _lib.XSyncIntToValue
XSyncIntToValue.restype = None
XSyncIntToValue.argtypes = [POINTER(XSyncValue), c_int]
XSyncIntsToValue = _lib.XSyncIntsToValue
XSyncIntsToValue.restype = None
XSyncIntsToValue.argtypes = [POINTER(XSyncValue), c_uint, c_int]
Bool = xlib.Bool
XSyncValueGreaterThan = _lib.XSyncValueGreaterThan
XSyncValueGreaterThan.restype = Bool
XSyncValueGreaterThan.argtypes = [XSyncValue, XSyncValue]
XSyncValueLessThan = _lib.XSyncValueLessThan
XSyncValueLessThan.restype = Bool
XSyncValueLessThan.argtypes = [XSyncValue, XSyncValue]
XSyncValueGreaterOrEqual = _lib.XSyncValueGreaterOrEqual
XSyncValueGreaterOrEqual.restype = Bool
XSyncValueGreaterOrEqual.argtypes = [XSyncValue, XSyncValue]
XSyncValueLessOrEqual = _lib.XSyncValueLessOrEqual
XSyncValueLessOrEqual.restype = Bool
XSyncValueLessOrEqual.argtypes = [XSyncValue, XSyncValue]
XSyncValueEqual = _lib.XSyncValueEqual
XSyncValueEqual.restype = Bool
XSyncValueEqual.argtypes = [XSyncValue, XSyncValue]
XSyncValueIsNegative = _lib.XSyncValueIsNegative
XSyncValueIsNegative.restype = Bool
XSyncValueIsNegative.argtypes = [XSyncValue]
XSyncValueIsZero = _lib.XSyncValueIsZero
XSyncValueIsZero.restype = Bool
XSyncValueIsZero.argtypes = [XSyncValue]
XSyncValueIsPositive = _lib.XSyncValueIsPositive
XSyncValueIsPositive.restype = Bool
XSyncValueIsPositive.argtypes = [XSyncValue]
XSyncValueLow32 = _lib.XSyncValueLow32
XSyncValueLow32.restype = c_uint
XSyncValueLow32.argtypes = [XSyncValue]
XSyncValueHigh32 = _lib.XSyncValueHigh32
XSyncValueHigh32.restype = c_int
XSyncValueHigh32.argtypes = [XSyncValue]
XSyncValueAdd = _lib.XSyncValueAdd
XSyncValueAdd.restype = None
XSyncValueAdd.argtypes = [POINTER(XSyncValue), XSyncValue, XSyncValue, POINTER(c_int)]
XSyncValueSubtract = _lib.XSyncValueSubtract
XSyncValueSubtract.restype = None
XSyncValueSubtract.argtypes = [POINTER(XSyncValue), XSyncValue, XSyncValue, POINTER(c_int)]
XSyncMaxValue = _lib.XSyncMaxValue
XSyncMaxValue.restype = None
XSyncMaxValue.argtypes = [POINTER(XSyncValue)]
XSyncMinValue = _lib.XSyncMinValue
XSyncMinValue.restype = None
XSyncMinValue.argtypes = [POINTER(XSyncValue)]

class struct__XSyncSystemCounter(Structure):
    __slots__ = [
     'name',
     'counter',
     'resolution']


struct__XSyncSystemCounter._fields_ = [
 (
  'name', c_char_p),
 (
  'counter', XSyncCounter),
 (
  'resolution', XSyncValue)]
XSyncSystemCounter = struct__XSyncSystemCounter

class struct_anon_96(Structure):
    __slots__ = [
     'counter',
     'value_type',
     'wait_value',
     'test_type']


struct_anon_96._fields_ = [
 (
  'counter', XSyncCounter),
 (
  'value_type', XSyncValueType),
 (
  'wait_value', XSyncValue),
 (
  'test_type', XSyncTestType)]
XSyncTrigger = struct_anon_96

class struct_anon_97(Structure):
    __slots__ = [
     'trigger',
     'event_threshold']


struct_anon_97._fields_ = [
 (
  'trigger', XSyncTrigger),
 (
  'event_threshold', XSyncValue)]
XSyncWaitCondition = struct_anon_97

class struct_anon_98(Structure):
    __slots__ = [
     'trigger',
     'delta',
     'events',
     'state']


struct_anon_98._fields_ = [
 (
  'trigger', XSyncTrigger),
 (
  'delta', XSyncValue),
 (
  'events', Bool),
 (
  'state', XSyncAlarmState)]
XSyncAlarmAttributes = struct_anon_98

class struct_anon_99(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'counter', 
     'wait_value', 
     'counter_value', 
     'time', 
     'count', 
     'destroyed']


Display = xlib.Display
Time = xlib.Time
struct_anon_99._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', Bool),
 (
  'display', POINTER(Display)),
 (
  'counter', XSyncCounter),
 (
  'wait_value', XSyncValue),
 (
  'counter_value', XSyncValue),
 (
  'time', Time),
 (
  'count', c_int),
 (
  'destroyed', Bool)]
XSyncCounterNotifyEvent = struct_anon_99

class struct_anon_100(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'alarm', 
     'counter_value', 
     'alarm_value', 
     'time', 
     'state']


struct_anon_100._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', Bool),
 (
  'display', POINTER(Display)),
 (
  'alarm', XSyncAlarm),
 (
  'counter_value', XSyncValue),
 (
  'alarm_value', XSyncValue),
 (
  'time', Time),
 (
  'state', XSyncAlarmState)]
XSyncAlarmNotifyEvent = struct_anon_100

class struct_anon_101(Structure):
    __slots__ = [
     'type', 
     'display', 
     'alarm', 
     'serial', 
     'error_code', 
     'request_code', 
     'minor_code']


struct_anon_101._fields_ = [
 (
  'type', c_int),
 (
  'display', POINTER(Display)),
 (
  'alarm', XSyncAlarm),
 (
  'serial', c_ulong),
 (
  'error_code', c_ubyte),
 (
  'request_code', c_ubyte),
 (
  'minor_code', c_ubyte)]
XSyncAlarmError = struct_anon_101

class struct_anon_102(Structure):
    __slots__ = [
     'type', 
     'display', 
     'counter', 
     'serial', 
     'error_code', 
     'request_code', 
     'minor_code']


struct_anon_102._fields_ = [
 (
  'type', c_int),
 (
  'display', POINTER(Display)),
 (
  'counter', XSyncCounter),
 (
  'serial', c_ulong),
 (
  'error_code', c_ubyte),
 (
  'request_code', c_ubyte),
 (
  'minor_code', c_ubyte)]
XSyncCounterError = struct_anon_102
XSyncQueryExtension = _lib.XSyncQueryExtension
XSyncQueryExtension.restype = c_int
XSyncQueryExtension.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XSyncInitialize = _lib.XSyncInitialize
XSyncInitialize.restype = c_int
XSyncInitialize.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XSyncListSystemCounters = _lib.XSyncListSystemCounters
XSyncListSystemCounters.restype = POINTER(XSyncSystemCounter)
XSyncListSystemCounters.argtypes = [POINTER(Display), POINTER(c_int)]
XSyncFreeSystemCounterList = _lib.XSyncFreeSystemCounterList
XSyncFreeSystemCounterList.restype = None
XSyncFreeSystemCounterList.argtypes = [POINTER(XSyncSystemCounter)]
XSyncCreateCounter = _lib.XSyncCreateCounter
XSyncCreateCounter.restype = XSyncCounter
XSyncCreateCounter.argtypes = [POINTER(Display), XSyncValue]
XSyncSetCounter = _lib.XSyncSetCounter
XSyncSetCounter.restype = c_int
XSyncSetCounter.argtypes = [POINTER(Display), XSyncCounter, XSyncValue]
XSyncChangeCounter = _lib.XSyncChangeCounter
XSyncChangeCounter.restype = c_int
XSyncChangeCounter.argtypes = [POINTER(Display), XSyncCounter, XSyncValue]
XSyncDestroyCounter = _lib.XSyncDestroyCounter
XSyncDestroyCounter.restype = c_int
XSyncDestroyCounter.argtypes = [POINTER(Display), XSyncCounter]
XSyncQueryCounter = _lib.XSyncQueryCounter
XSyncQueryCounter.restype = c_int
XSyncQueryCounter.argtypes = [POINTER(Display), XSyncCounter, POINTER(XSyncValue)]
XSyncAwait = _lib.XSyncAwait
XSyncAwait.restype = c_int
XSyncAwait.argtypes = [POINTER(Display), POINTER(XSyncWaitCondition), c_int]
XSyncCreateAlarm = _lib.XSyncCreateAlarm
XSyncCreateAlarm.restype = XSyncAlarm
XSyncCreateAlarm.argtypes = [POINTER(Display), c_ulong, POINTER(XSyncAlarmAttributes)]
XSyncDestroyAlarm = _lib.XSyncDestroyAlarm
XSyncDestroyAlarm.restype = c_int
XSyncDestroyAlarm.argtypes = [POINTER(Display), XSyncAlarm]
XSyncQueryAlarm = _lib.XSyncQueryAlarm
XSyncQueryAlarm.restype = c_int
XSyncQueryAlarm.argtypes = [POINTER(Display), XSyncAlarm, POINTER(XSyncAlarmAttributes)]
XSyncChangeAlarm = _lib.XSyncChangeAlarm
XSyncChangeAlarm.restype = c_int
XSyncChangeAlarm.argtypes = [POINTER(Display), XSyncAlarm, c_ulong, POINTER(XSyncAlarmAttributes)]
XSyncSetPriority = _lib.XSyncSetPriority
XSyncSetPriority.restype = c_int
XSyncSetPriority.argtypes = [POINTER(Display), XID, c_int]
XSyncGetPriority = _lib.XSyncGetPriority
XSyncGetPriority.restype = c_int
XSyncGetPriority.argtypes = [POINTER(Display), XID, POINTER(c_int)]
__all__ = [
 'SYNC_MAJOR_VERSION', 'SYNC_MINOR_VERSION', 'X_SyncInitialize', 
 'X_SyncListSystemCounters', 
 'X_SyncCreateCounter', 'X_SyncSetCounter', 
 'X_SyncChangeCounter', 'X_SyncQueryCounter', 
 'X_SyncDestroyCounter', 
 'X_SyncAwait', 'X_SyncCreateAlarm', 'X_SyncChangeAlarm', 
 'X_SyncQueryAlarm', 
 'X_SyncDestroyAlarm', 'X_SyncSetPriority', 'X_SyncGetPriority', 
 'XSyncCounterNotify', 
 'XSyncAlarmNotify', 'XSyncAlarmNotifyMask', 
 'XSyncNumberEvents', 'XSyncBadCounter', 
 'XSyncBadAlarm', 'XSyncNumberErrors', 
 'XSyncCACounter', 'XSyncCAValueType', 
 'XSyncCAValue', 'XSyncCATestType', 
 'XSyncCADelta', 'XSyncCAEvents', 'XSyncValueType', 
 'XSyncAbsolute', 
 'XSyncRelative', 'XSyncTestType', 'XSyncPositiveTransition', 
 'XSyncNegativeTransition', 
 'XSyncPositiveComparison', 
 'XSyncNegativeComparison', 'XSyncAlarmState', 
 'XSyncAlarmActive', 
 'XSyncAlarmInactive', 'XSyncAlarmDestroyed', 'XSyncCounter', 
 'XSyncAlarm', 
 'XSyncValue', 'XSyncIntToValue', 'XSyncIntsToValue', 'XSyncValueGreaterThan', 
 'XSyncValueLessThan', 
 'XSyncValueGreaterOrEqual', 'XSyncValueLessOrEqual', 
 'XSyncValueEqual', 
 'XSyncValueIsNegative', 'XSyncValueIsZero', 
 'XSyncValueIsPositive', 'XSyncValueLow32', 
 'XSyncValueHigh32', 
 'XSyncValueAdd', 'XSyncValueSubtract', 'XSyncMaxValue', 
 'XSyncMinValue', 
 'XSyncSystemCounter', 'XSyncTrigger', 'XSyncWaitCondition', 
 'XSyncAlarmAttributes', 
 'XSyncCounterNotifyEvent', 'XSyncAlarmNotifyEvent', 
 'XSyncAlarmError', 'XSyncCounterError', 
 'XSyncQueryExtension', 
 'XSyncInitialize', 'XSyncListSystemCounters', 'XSyncFreeSystemCounterList', 
 'XSyncCreateCounter', 
 'XSyncSetCounter', 'XSyncChangeCounter', 
 'XSyncDestroyCounter', 'XSyncQueryCounter', 
 'XSyncAwait', 'XSyncCreateAlarm', 
 'XSyncDestroyAlarm', 'XSyncQueryAlarm', 
 'XSyncChangeAlarm', 
 'XSyncSetPriority', 'XSyncGetPriority']
# okay decompiling out\pyglet.libs.x11.xsync.pyc
