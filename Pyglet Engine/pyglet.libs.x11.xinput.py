# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.x11.xinput
__docformat__ = 'restructuredtext'
__version__ = '$Id: wrap.py 1694 2008-01-30 23:12:00Z Alex.Holkner $'
import ctypes
from ..ctypes import *
import pyglet.lib
_lib = pyglet.lib.load_library('Xi')
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
sz_xGetExtensionVersionReq = 8
sz_xGetExtensionVersionReply = 32
sz_xListInputDevicesReq = 4
sz_xListInputDevicesReply = 32
sz_xOpenDeviceReq = 8
sz_xOpenDeviceReply = 32
sz_xCloseDeviceReq = 8
sz_xSetDeviceModeReq = 8
sz_xSetDeviceModeReply = 32
sz_xSelectExtensionEventReq = 12
sz_xGetSelectedExtensionEventsReq = 8
sz_xGetSelectedExtensionEventsReply = 32
sz_xChangeDeviceDontPropagateListReq = 12
sz_xGetDeviceDontPropagateListReq = 8
sz_xGetDeviceDontPropagateListReply = 32
sz_xGetDeviceMotionEventsReq = 16
sz_xGetDeviceMotionEventsReply = 32
sz_xChangeKeyboardDeviceReq = 8
sz_xChangeKeyboardDeviceReply = 32
sz_xChangePointerDeviceReq = 8
sz_xChangePointerDeviceReply = 32
sz_xGrabDeviceReq = 20
sz_xGrabDeviceReply = 32
sz_xUngrabDeviceReq = 12
sz_xGrabDeviceKeyReq = 20
sz_xGrabDeviceKeyReply = 32
sz_xUngrabDeviceKeyReq = 16
sz_xGrabDeviceButtonReq = 20
sz_xGrabDeviceButtonReply = 32
sz_xUngrabDeviceButtonReq = 16
sz_xAllowDeviceEventsReq = 12
sz_xGetDeviceFocusReq = 8
sz_xGetDeviceFocusReply = 32
sz_xSetDeviceFocusReq = 16
sz_xGetFeedbackControlReq = 8
sz_xGetFeedbackControlReply = 32
sz_xChangeFeedbackControlReq = 12
sz_xGetDeviceKeyMappingReq = 8
sz_xGetDeviceKeyMappingReply = 32
sz_xChangeDeviceKeyMappingReq = 8
sz_xGetDeviceModifierMappingReq = 8
sz_xSetDeviceModifierMappingReq = 8
sz_xSetDeviceModifierMappingReply = 32
sz_xGetDeviceButtonMappingReq = 8
sz_xGetDeviceButtonMappingReply = 32
sz_xSetDeviceButtonMappingReq = 8
sz_xSetDeviceButtonMappingReply = 32
sz_xQueryDeviceStateReq = 8
sz_xQueryDeviceStateReply = 32
sz_xSendExtensionEventReq = 16
sz_xDeviceBellReq = 8
sz_xSetDeviceValuatorsReq = 8
sz_xSetDeviceValuatorsReply = 32
sz_xGetDeviceControlReq = 8
sz_xGetDeviceControlReply = 32
sz_xChangeDeviceControlReq = 8
sz_xChangeDeviceControlReply = 32
Dont_Check = 0
XInput_Initial_Release = 1
XInput_Add_XDeviceBell = 2
XInput_Add_XSetDeviceValuators = 3
XInput_Add_XChangeDeviceControl = 4
XInput_Add_DevicePresenceNotify = 5
XI_Absent = 0
XI_Present = 1
XI_Initial_Release_Major = 1
XI_Initial_Release_Minor = 0
XI_Add_XDeviceBell_Major = 1
XI_Add_XDeviceBell_Minor = 1
XI_Add_XSetDeviceValuators_Major = 1
XI_Add_XSetDeviceValuators_Minor = 2
XI_Add_XChangeDeviceControl_Major = 1
XI_Add_XChangeDeviceControl_Minor = 3
XI_Add_DevicePresenceNotify_Major = 1
XI_Add_DevicePresenceNotify_Minor = 4
DEVICE_RESOLUTION = 1
DEVICE_ABS_CALIB = 2
DEVICE_CORE = 3
DEVICE_ENABLE = 4
DEVICE_ABS_AREA = 5
NoSuchExtension = 1
COUNT = 0
CREATE = 1
NewPointer = 0
NewKeyboard = 1
XPOINTER = 0
XKEYBOARD = 1
UseXKeyboard = 255
IsXPointer = 0
IsXKeyboard = 1
IsXExtensionDevice = 2
IsXExtensionKeyboard = 3
IsXExtensionPointer = 4
AsyncThisDevice = 0
SyncThisDevice = 1
ReplayThisDevice = 2
AsyncOtherDevices = 3
AsyncAll = 4
SyncAll = 5
FollowKeyboard = 3
RevertToFollowKeyboard = 3
DvAccelNum = 1
DvAccelDenom = 2
DvThreshold = 4
DvKeyClickPercent = 1
DvPercent = 2
DvPitch = 4
DvDuration = 8
DvLed = 16
DvLedMode = 32
DvKey = 64
DvAutoRepeatMode = 128
DvString = 1
DvInteger = 1
DeviceMode = 1
Relative = 0
Absolute = 1
ProximityState = 2
InProximity = 0
OutOfProximity = 2
AddToList = 0
DeleteFromList = 1
KeyClass = 0
ButtonClass = 1
ValuatorClass = 2
FeedbackClass = 3
ProximityClass = 4
FocusClass = 5
OtherClass = 6
KbdFeedbackClass = 0
PtrFeedbackClass = 1
StringFeedbackClass = 2
IntegerFeedbackClass = 3
LedFeedbackClass = 4
BellFeedbackClass = 5
_devicePointerMotionHint = 0
_deviceButton1Motion = 1
_deviceButton2Motion = 2
_deviceButton3Motion = 3
_deviceButton4Motion = 4
_deviceButton5Motion = 5
_deviceButtonMotion = 6
_deviceButtonGrab = 7
_deviceOwnerGrabButton = 8
_noExtensionEvent = 9
_devicePresence = 0
DeviceAdded = 0
DeviceRemoved = 1
DeviceEnabled = 2
DeviceDisabled = 3
DeviceUnrecoverable = 4
XI_BadDevice = 0
XI_BadEvent = 1
XI_BadMode = 2
XI_DeviceBusy = 3
XI_BadClass = 4
XEventClass = c_ulong

class struct_anon_93(Structure):
    __slots__ = [
     'present',
     'major_version',
     'minor_version']


struct_anon_93._fields_ = [
 (
  'present', c_int),
 (
  'major_version', c_short),
 (
  'minor_version', c_short)]
XExtensionVersion = struct_anon_93
_deviceKeyPress = 0
_deviceKeyRelease = 1
_deviceButtonPress = 0
_deviceButtonRelease = 1
_deviceMotionNotify = 0
_deviceFocusIn = 0
_deviceFocusOut = 1
_proximityIn = 0
_proximityOut = 1
_deviceStateNotify = 0
_deviceMappingNotify = 1
_changeDeviceNotify = 2

class struct_anon_94(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'keycode', 
     'same_screen', 
     'device_state', 
     'axes_count', 
     'first_axis', 
     'axis_data']


Display = pyglet.libs.x11.xlib.Display
Window = pyglet.libs.x11.xlib.Window
XID = pyglet.libs.x11.xlib.XID
Time = pyglet.libs.x11.xlib.Time
struct_anon_94._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'keycode', c_uint),
 (
  'same_screen', c_int),
 (
  'device_state', c_uint),
 (
  'axes_count', c_ubyte),
 (
  'first_axis', c_ubyte),
 (
  'axis_data', c_int * 6)]
XDeviceKeyEvent = struct_anon_94
XDeviceKeyPressedEvent = XDeviceKeyEvent
XDeviceKeyReleasedEvent = XDeviceKeyEvent

class struct_anon_95(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'button', 
     'same_screen', 
     'device_state', 
     'axes_count', 
     'first_axis', 
     'axis_data']


struct_anon_95._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'button', c_uint),
 (
  'same_screen', c_int),
 (
  'device_state', c_uint),
 (
  'axes_count', c_ubyte),
 (
  'first_axis', c_ubyte),
 (
  'axis_data', c_int * 6)]
XDeviceButtonEvent = struct_anon_95
XDeviceButtonPressedEvent = XDeviceButtonEvent
XDeviceButtonReleasedEvent = XDeviceButtonEvent

class struct_anon_96(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'is_hint', 
     'same_screen', 
     'device_state', 
     'axes_count', 
     'first_axis', 
     'axis_data']


struct_anon_96._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'is_hint', c_char),
 (
  'same_screen', c_int),
 (
  'device_state', c_uint),
 (
  'axes_count', c_ubyte),
 (
  'first_axis', c_ubyte),
 (
  'axis_data', c_int * 6)]
XDeviceMotionEvent = struct_anon_96

class struct_anon_97(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'mode', 
     'detail', 
     'time']


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
  'window', Window),
 (
  'deviceid', XID),
 (
  'mode', c_int),
 (
  'detail', c_int),
 (
  'time', Time)]
XDeviceFocusChangeEvent = struct_anon_97
XDeviceFocusInEvent = XDeviceFocusChangeEvent
XDeviceFocusOutEvent = XDeviceFocusChangeEvent

class struct_anon_98(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'same_screen', 
     'device_state', 
     'axes_count', 
     'first_axis', 
     'axis_data']


struct_anon_98._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'same_screen', c_int),
 (
  'device_state', c_uint),
 (
  'axes_count', c_ubyte),
 (
  'first_axis', c_ubyte),
 (
  'axis_data', c_int * 6)]
XProximityNotifyEvent = struct_anon_98
XProximityInEvent = XProximityNotifyEvent
XProximityOutEvent = XProximityNotifyEvent

class struct_anon_99(Structure):
    __slots__ = [
     'class',
     'length']


struct_anon_99._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte)]
XInputClass = struct_anon_99

class struct_anon_100(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'time', 
     'num_classes', 
     'data']


struct_anon_100._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'time', Time),
 (
  'num_classes', c_int),
 (
  'data', c_char * 64)]
XDeviceStateNotifyEvent = struct_anon_100

class struct_anon_101(Structure):
    __slots__ = [
     'class', 
     'length', 
     'num_valuators', 
     'mode', 
     'valuators']


struct_anon_101._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte),
 (
  'num_valuators', c_ubyte),
 (
  'mode', c_ubyte),
 (
  'valuators', c_int * 6)]
XValuatorStatus = struct_anon_101

class struct_anon_102(Structure):
    __slots__ = [
     'class',
     'length',
     'num_keys',
     'keys']


struct_anon_102._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte),
 (
  'num_keys', c_short),
 (
  'keys', c_char * 32)]
XKeyStatus = struct_anon_102

class struct_anon_103(Structure):
    __slots__ = [
     'class',
     'length',
     'num_buttons',
     'buttons']


struct_anon_103._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte),
 (
  'num_buttons', c_short),
 (
  'buttons', c_char * 32)]
XButtonStatus = struct_anon_103

class struct_anon_104(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'time', 
     'request', 
     'first_keycode', 
     'count']


struct_anon_104._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'time', Time),
 (
  'request', c_int),
 (
  'first_keycode', c_int),
 (
  'count', c_int)]
XDeviceMappingEvent = struct_anon_104

class struct_anon_105(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'deviceid', 
     'time', 
     'request']


struct_anon_105._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'deviceid', XID),
 (
  'time', Time),
 (
  'request', c_int)]
XChangeDeviceNotifyEvent = struct_anon_105

class struct_anon_106(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'time', 
     'devchange', 
     'deviceid', 
     'control']


struct_anon_106._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'time', Time),
 (
  'devchange', c_int),
 (
  'deviceid', XID),
 (
  'control', XID)]
XDevicePresenceNotifyEvent = struct_anon_106

class struct_anon_107(Structure):
    __slots__ = [
     'class',
     'length',
     'id']


struct_anon_107._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID)]
XFeedbackState = struct_anon_107

class struct_anon_108(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'click', 
     'percent', 
     'pitch', 
     'duration', 
     'led_mask', 
     'global_auto_repeat', 
     'auto_repeats']


struct_anon_108._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'click', c_int),
 (
  'percent', c_int),
 (
  'pitch', c_int),
 (
  'duration', c_int),
 (
  'led_mask', c_int),
 (
  'global_auto_repeat', c_int),
 (
  'auto_repeats', c_char * 32)]
XKbdFeedbackState = struct_anon_108

class struct_anon_109(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'accelNum', 
     'accelDenom', 
     'threshold']


struct_anon_109._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'accelNum', c_int),
 (
  'accelDenom', c_int),
 (
  'threshold', c_int)]
XPtrFeedbackState = struct_anon_109

class struct_anon_110(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'resolution', 
     'minVal', 
     'maxVal']


struct_anon_110._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'resolution', c_int),
 (
  'minVal', c_int),
 (
  'maxVal', c_int)]
XIntegerFeedbackState = struct_anon_110

class struct_anon_111(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'max_symbols', 
     'num_syms_supported', 
     'syms_supported']


KeySym = pyglet.libs.x11.xlib.KeySym
struct_anon_111._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'max_symbols', c_int),
 (
  'num_syms_supported', c_int),
 (
  'syms_supported', POINTER(KeySym))]
XStringFeedbackState = struct_anon_111

class struct_anon_112(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'percent', 
     'pitch', 
     'duration']


struct_anon_112._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'percent', c_int),
 (
  'pitch', c_int),
 (
  'duration', c_int)]
XBellFeedbackState = struct_anon_112

class struct_anon_113(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'led_values', 
     'led_mask']


struct_anon_113._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'led_values', c_int),
 (
  'led_mask', c_int)]
XLedFeedbackState = struct_anon_113

class struct_anon_114(Structure):
    __slots__ = [
     'class',
     'length',
     'id']


struct_anon_114._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID)]
XFeedbackControl = struct_anon_114

class struct_anon_115(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'accelNum', 
     'accelDenom', 
     'threshold']


struct_anon_115._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'accelNum', c_int),
 (
  'accelDenom', c_int),
 (
  'threshold', c_int)]
XPtrFeedbackControl = struct_anon_115

class struct_anon_116(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'click', 
     'percent', 
     'pitch', 
     'duration', 
     'led_mask', 
     'led_value', 
     'key', 
     'auto_repeat_mode']


struct_anon_116._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'click', c_int),
 (
  'percent', c_int),
 (
  'pitch', c_int),
 (
  'duration', c_int),
 (
  'led_mask', c_int),
 (
  'led_value', c_int),
 (
  'key', c_int),
 (
  'auto_repeat_mode', c_int)]
XKbdFeedbackControl = struct_anon_116

class struct_anon_117(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'num_keysyms', 
     'syms_to_display']


struct_anon_117._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'num_keysyms', c_int),
 (
  'syms_to_display', POINTER(KeySym))]
XStringFeedbackControl = struct_anon_117

class struct_anon_118(Structure):
    __slots__ = [
     'class',
     'length',
     'id',
     'int_to_display']


struct_anon_118._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'int_to_display', c_int)]
XIntegerFeedbackControl = struct_anon_118

class struct_anon_119(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'percent', 
     'pitch', 
     'duration']


struct_anon_119._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'percent', c_int),
 (
  'pitch', c_int),
 (
  'duration', c_int)]
XBellFeedbackControl = struct_anon_119

class struct_anon_120(Structure):
    __slots__ = [
     'class', 
     'length', 
     'id', 
     'led_mask', 
     'led_values']


struct_anon_120._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'id', XID),
 (
  'led_mask', c_int),
 (
  'led_values', c_int)]
XLedFeedbackControl = struct_anon_120

class struct_anon_121(Structure):
    __slots__ = [
     'control',
     'length']


struct_anon_121._fields_ = [
 (
  'control', XID),
 (
  'length', c_int)]
XDeviceControl = struct_anon_121

class struct_anon_122(Structure):
    __slots__ = [
     'control', 
     'length', 
     'first_valuator', 
     'num_valuators', 
     'resolutions']


struct_anon_122._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'first_valuator', c_int),
 (
  'num_valuators', c_int),
 (
  'resolutions', POINTER(c_int))]
XDeviceResolutionControl = struct_anon_122

class struct_anon_123(Structure):
    __slots__ = [
     'control', 
     'length', 
     'num_valuators', 
     'resolutions', 
     'min_resolutions', 
     'max_resolutions']


struct_anon_123._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'num_valuators', c_int),
 (
  'resolutions', POINTER(c_int)),
 (
  'min_resolutions', POINTER(c_int)),
 (
  'max_resolutions', POINTER(c_int))]
XDeviceResolutionState = struct_anon_123

class struct_anon_124(Structure):
    __slots__ = [
     'control', 
     'length', 
     'min_x', 
     'max_x', 
     'min_y', 
     'max_y', 
     'flip_x', 
     'flip_y', 
     'rotation', 
     'button_threshold']


struct_anon_124._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'min_x', c_int),
 (
  'max_x', c_int),
 (
  'min_y', c_int),
 (
  'max_y', c_int),
 (
  'flip_x', c_int),
 (
  'flip_y', c_int),
 (
  'rotation', c_int),
 (
  'button_threshold', c_int)]
XDeviceAbsCalibControl = struct_anon_124

class struct_anon_125(Structure):
    __slots__ = [
     'control', 
     'length', 
     'min_x', 
     'max_x', 
     'min_y', 
     'max_y', 
     'flip_x', 
     'flip_y', 
     'rotation', 
     'button_threshold']


struct_anon_125._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'min_x', c_int),
 (
  'max_x', c_int),
 (
  'min_y', c_int),
 (
  'max_y', c_int),
 (
  'flip_x', c_int),
 (
  'flip_y', c_int),
 (
  'rotation', c_int),
 (
  'button_threshold', c_int)]
XDeviceAbsCalibState = struct_anon_125

class struct_anon_126(Structure):
    __slots__ = [
     'control', 
     'length', 
     'offset_x', 
     'offset_y', 
     'width', 
     'height', 
     'screen', 
     'following']


struct_anon_126._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'offset_x', c_int),
 (
  'offset_y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'screen', c_int),
 (
  'following', XID)]
XDeviceAbsAreaControl = struct_anon_126

class struct_anon_127(Structure):
    __slots__ = [
     'control', 
     'length', 
     'offset_x', 
     'offset_y', 
     'width', 
     'height', 
     'screen', 
     'following']


struct_anon_127._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'offset_x', c_int),
 (
  'offset_y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'screen', c_int),
 (
  'following', XID)]
XDeviceAbsAreaState = struct_anon_127

class struct_anon_128(Structure):
    __slots__ = [
     'control',
     'length',
     'status']


struct_anon_128._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'status', c_int)]
XDeviceCoreControl = struct_anon_128

class struct_anon_129(Structure):
    __slots__ = [
     'control',
     'length',
     'status',
     'iscore']


struct_anon_129._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'status', c_int),
 (
  'iscore', c_int)]
XDeviceCoreState = struct_anon_129

class struct_anon_130(Structure):
    __slots__ = [
     'control',
     'length',
     'enable']


struct_anon_130._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'enable', c_int)]
XDeviceEnableControl = struct_anon_130

class struct_anon_131(Structure):
    __slots__ = [
     'control',
     'length',
     'enable']


struct_anon_131._fields_ = [
 (
  'control', XID),
 (
  'length', c_int),
 (
  'enable', c_int)]
XDeviceEnableState = struct_anon_131

class struct__XAnyClassinfo(Structure):
    __slots__ = []


struct__XAnyClassinfo._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XAnyClassinfo(Structure):
    __slots__ = []


struct__XAnyClassinfo._fields_ = [
 (
  '_opaque_struct', c_int)]
XAnyClassPtr = POINTER(struct__XAnyClassinfo)

class struct__XAnyClassinfo(Structure):
    __slots__ = [
     'class',
     'length']


struct__XAnyClassinfo._fields_ = [
 (
  'class', XID),
 (
  'length', c_int)]
XAnyClassInfo = struct__XAnyClassinfo

class struct__XDeviceInfo(Structure):
    __slots__ = []


struct__XDeviceInfo._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XDeviceInfo(Structure):
    __slots__ = []


struct__XDeviceInfo._fields_ = [
 (
  '_opaque_struct', c_int)]
XDeviceInfoPtr = POINTER(struct__XDeviceInfo)

class struct__XDeviceInfo(Structure):
    __slots__ = [
     'id', 
     'type', 
     'name', 
     'num_classes', 
     'use', 
     'inputclassinfo']


Atom = pyglet.libs.x11.xlib.Atom
struct__XDeviceInfo._fields_ = [
 (
  'id', XID),
 (
  'type', Atom),
 (
  'name', c_char_p),
 (
  'num_classes', c_int),
 (
  'use', c_int),
 (
  'inputclassinfo', XAnyClassPtr)]
XDeviceInfo = struct__XDeviceInfo

class struct__XKeyInfo(Structure):
    __slots__ = []


struct__XKeyInfo._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XKeyInfo(Structure):
    __slots__ = []


struct__XKeyInfo._fields_ = [
 (
  '_opaque_struct', c_int)]
XKeyInfoPtr = POINTER(struct__XKeyInfo)

class struct__XKeyInfo(Structure):
    __slots__ = [
     'class', 
     'length', 
     'min_keycode', 
     'max_keycode', 
     'num_keys']


struct__XKeyInfo._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'min_keycode', c_ushort),
 (
  'max_keycode', c_ushort),
 (
  'num_keys', c_ushort)]
XKeyInfo = struct__XKeyInfo

class struct__XButtonInfo(Structure):
    __slots__ = []


struct__XButtonInfo._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XButtonInfo(Structure):
    __slots__ = []


struct__XButtonInfo._fields_ = [
 (
  '_opaque_struct', c_int)]
XButtonInfoPtr = POINTER(struct__XButtonInfo)

class struct__XButtonInfo(Structure):
    __slots__ = [
     'class',
     'length',
     'num_buttons']


struct__XButtonInfo._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'num_buttons', c_short)]
XButtonInfo = struct__XButtonInfo

class struct__XAxisInfo(Structure):
    __slots__ = []


struct__XAxisInfo._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XAxisInfo(Structure):
    __slots__ = []


struct__XAxisInfo._fields_ = [
 (
  '_opaque_struct', c_int)]
XAxisInfoPtr = POINTER(struct__XAxisInfo)

class struct__XAxisInfo(Structure):
    __slots__ = [
     'resolution',
     'min_value',
     'max_value']


struct__XAxisInfo._fields_ = [
 (
  'resolution', c_int),
 (
  'min_value', c_int),
 (
  'max_value', c_int)]
XAxisInfo = struct__XAxisInfo

class struct__XValuatorInfo(Structure):
    __slots__ = []


struct__XValuatorInfo._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XValuatorInfo(Structure):
    __slots__ = []


struct__XValuatorInfo._fields_ = [
 (
  '_opaque_struct', c_int)]
XValuatorInfoPtr = POINTER(struct__XValuatorInfo)

class struct__XValuatorInfo(Structure):
    __slots__ = [
     'class', 
     'length', 
     'num_axes', 
     'mode', 
     'motion_buffer', 
     'axes']


struct__XValuatorInfo._fields_ = [
 (
  'class', XID),
 (
  'length', c_int),
 (
  'num_axes', c_ubyte),
 (
  'mode', c_ubyte),
 (
  'motion_buffer', c_ulong),
 (
  'axes', XAxisInfoPtr)]
XValuatorInfo = struct__XValuatorInfo

class struct_anon_132(Structure):
    __slots__ = [
     'input_class',
     'event_type_base']


struct_anon_132._fields_ = [
 (
  'input_class', c_ubyte),
 (
  'event_type_base', c_ubyte)]
XInputClassInfo = struct_anon_132

class struct_anon_133(Structure):
    __slots__ = [
     'device_id',
     'num_classes',
     'classes']


struct_anon_133._fields_ = [
 (
  'device_id', XID),
 (
  'num_classes', c_int),
 (
  'classes', POINTER(XInputClassInfo))]
XDevice = struct_anon_133

class struct_anon_134(Structure):
    __slots__ = [
     'event_type',
     'device']


struct_anon_134._fields_ = [
 (
  'event_type', XEventClass),
 (
  'device', XID)]
XEventList = struct_anon_134

class struct_anon_135(Structure):
    __slots__ = [
     'time',
     'data']


struct_anon_135._fields_ = [
 (
  'time', Time),
 (
  'data', POINTER(c_int))]
XDeviceTimeCoord = struct_anon_135

class struct_anon_136(Structure):
    __slots__ = [
     'device_id',
     'num_classes',
     'data']


struct_anon_136._fields_ = [
 (
  'device_id', XID),
 (
  'num_classes', c_int),
 (
  'data', POINTER(XInputClass))]
XDeviceState = struct_anon_136

class struct_anon_137(Structure):
    __slots__ = [
     'class', 
     'length', 
     'num_valuators', 
     'mode', 
     'valuators']


struct_anon_137._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte),
 (
  'num_valuators', c_ubyte),
 (
  'mode', c_ubyte),
 (
  'valuators', POINTER(c_int))]
XValuatorState = struct_anon_137

class struct_anon_138(Structure):
    __slots__ = [
     'class',
     'length',
     'num_keys',
     'keys']


struct_anon_138._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte),
 (
  'num_keys', c_short),
 (
  'keys', c_char * 32)]
XKeyState = struct_anon_138

class struct_anon_139(Structure):
    __slots__ = [
     'class',
     'length',
     'num_buttons',
     'buttons']


struct_anon_139._fields_ = [
 (
  'class', c_ubyte),
 (
  'length', c_ubyte),
 (
  'num_buttons', c_short),
 (
  'buttons', c_char * 32)]
XButtonState = struct_anon_139
XChangeKeyboardDevice = _lib.XChangeKeyboardDevice
XChangeKeyboardDevice.restype = c_int
XChangeKeyboardDevice.argtypes = [POINTER(Display), POINTER(XDevice)]
XChangePointerDevice = _lib.XChangePointerDevice
XChangePointerDevice.restype = c_int
XChangePointerDevice.argtypes = [POINTER(Display), POINTER(XDevice), c_int, c_int]
XGrabDevice = _lib.XGrabDevice
XGrabDevice.restype = c_int
XGrabDevice.argtypes = [POINTER(Display), POINTER(XDevice), Window, c_int, c_int, POINTER(XEventClass), c_int, c_int, Time]
XUngrabDevice = _lib.XUngrabDevice
XUngrabDevice.restype = c_int
XUngrabDevice.argtypes = [POINTER(Display), POINTER(XDevice), Time]
XGrabDeviceKey = _lib.XGrabDeviceKey
XGrabDeviceKey.restype = c_int
XGrabDeviceKey.argtypes = [POINTER(Display), POINTER(XDevice), c_uint, c_uint, POINTER(XDevice), Window, c_int, c_uint, POINTER(XEventClass), c_int, c_int]
XUngrabDeviceKey = _lib.XUngrabDeviceKey
XUngrabDeviceKey.restype = c_int
XUngrabDeviceKey.argtypes = [POINTER(Display), POINTER(XDevice), c_uint, c_uint, POINTER(XDevice), Window]
XGrabDeviceButton = _lib.XGrabDeviceButton
XGrabDeviceButton.restype = c_int
XGrabDeviceButton.argtypes = [POINTER(Display), POINTER(XDevice), c_uint, c_uint, POINTER(XDevice), Window, c_int, c_uint, POINTER(XEventClass), c_int, c_int]
XUngrabDeviceButton = _lib.XUngrabDeviceButton
XUngrabDeviceButton.restype = c_int
XUngrabDeviceButton.argtypes = [POINTER(Display), POINTER(XDevice), c_uint, c_uint, POINTER(XDevice), Window]
XAllowDeviceEvents = _lib.XAllowDeviceEvents
XAllowDeviceEvents.restype = c_int
XAllowDeviceEvents.argtypes = [POINTER(Display), POINTER(XDevice), c_int, Time]
XGetDeviceFocus = _lib.XGetDeviceFocus
XGetDeviceFocus.restype = c_int
XGetDeviceFocus.argtypes = [POINTER(Display), POINTER(XDevice), POINTER(Window), POINTER(c_int), POINTER(Time)]
XSetDeviceFocus = _lib.XSetDeviceFocus
XSetDeviceFocus.restype = c_int
XSetDeviceFocus.argtypes = [POINTER(Display), POINTER(XDevice), Window, c_int, Time]
XGetFeedbackControl = _lib.XGetFeedbackControl
XGetFeedbackControl.restype = POINTER(XFeedbackState)
XGetFeedbackControl.argtypes = [POINTER(Display), POINTER(XDevice), POINTER(c_int)]
XFreeFeedbackList = _lib.XFreeFeedbackList
XFreeFeedbackList.restype = None
XFreeFeedbackList.argtypes = [POINTER(XFeedbackState)]
XChangeFeedbackControl = _lib.XChangeFeedbackControl
XChangeFeedbackControl.restype = c_int
XChangeFeedbackControl.argtypes = [POINTER(Display), POINTER(XDevice), c_ulong, POINTER(XFeedbackControl)]
XDeviceBell = _lib.XDeviceBell
XDeviceBell.restype = c_int
XDeviceBell.argtypes = [POINTER(Display), POINTER(XDevice), XID, XID, c_int]
KeyCode = pyglet.libs.x11.xlib.KeyCode
XGetDeviceKeyMapping = _lib.XGetDeviceKeyMapping
XGetDeviceKeyMapping.restype = POINTER(KeySym)
XGetDeviceKeyMapping.argtypes = [POINTER(Display), POINTER(XDevice), KeyCode, c_int, POINTER(c_int)]
XChangeDeviceKeyMapping = _lib.XChangeDeviceKeyMapping
XChangeDeviceKeyMapping.restype = c_int
XChangeDeviceKeyMapping.argtypes = [POINTER(Display), POINTER(XDevice), c_int, c_int, POINTER(KeySym), c_int]
XModifierKeymap = pyglet.libs.x11.xlib.XModifierKeymap
XGetDeviceModifierMapping = _lib.XGetDeviceModifierMapping
XGetDeviceModifierMapping.restype = POINTER(XModifierKeymap)
XGetDeviceModifierMapping.argtypes = [POINTER(Display), POINTER(XDevice)]
XSetDeviceModifierMapping = _lib.XSetDeviceModifierMapping
XSetDeviceModifierMapping.restype = c_int
XSetDeviceModifierMapping.argtypes = [POINTER(Display), POINTER(XDevice), POINTER(XModifierKeymap)]
XSetDeviceButtonMapping = _lib.XSetDeviceButtonMapping
XSetDeviceButtonMapping.restype = c_int
XSetDeviceButtonMapping.argtypes = [POINTER(Display), POINTER(XDevice), POINTER(c_ubyte), c_int]
XGetDeviceButtonMapping = _lib.XGetDeviceButtonMapping
XGetDeviceButtonMapping.restype = c_int
XGetDeviceButtonMapping.argtypes = [POINTER(Display), POINTER(XDevice), POINTER(c_ubyte), c_uint]
XQueryDeviceState = _lib.XQueryDeviceState
XQueryDeviceState.restype = POINTER(XDeviceState)
XQueryDeviceState.argtypes = [POINTER(Display), POINTER(XDevice)]
XFreeDeviceState = _lib.XFreeDeviceState
XFreeDeviceState.restype = None
XFreeDeviceState.argtypes = [POINTER(XDeviceState)]
XGetExtensionVersion = _lib.XGetExtensionVersion
XGetExtensionVersion.restype = POINTER(XExtensionVersion)
XGetExtensionVersion.argtypes = [POINTER(Display), c_char_p]
XListInputDevices = _lib.XListInputDevices
XListInputDevices.restype = POINTER(XDeviceInfo)
XListInputDevices.argtypes = [POINTER(Display), POINTER(c_int)]
XFreeDeviceList = _lib.XFreeDeviceList
XFreeDeviceList.restype = None
XFreeDeviceList.argtypes = [POINTER(XDeviceInfo)]
XOpenDevice = _lib.XOpenDevice
XOpenDevice.restype = POINTER(XDevice)
XOpenDevice.argtypes = [POINTER(Display), XID]
XCloseDevice = _lib.XCloseDevice
XCloseDevice.restype = c_int
XCloseDevice.argtypes = [POINTER(Display), POINTER(XDevice)]
XSetDeviceMode = _lib.XSetDeviceMode
XSetDeviceMode.restype = c_int
XSetDeviceMode.argtypes = [POINTER(Display), POINTER(XDevice), c_int]
XSetDeviceValuators = _lib.XSetDeviceValuators
XSetDeviceValuators.restype = c_int
XSetDeviceValuators.argtypes = [POINTER(Display), POINTER(XDevice), POINTER(c_int), c_int, c_int]
XGetDeviceControl = _lib.XGetDeviceControl
XGetDeviceControl.restype = POINTER(XDeviceControl)
XGetDeviceControl.argtypes = [POINTER(Display), POINTER(XDevice), c_int]
XChangeDeviceControl = _lib.XChangeDeviceControl
XChangeDeviceControl.restype = c_int
XChangeDeviceControl.argtypes = [POINTER(Display), POINTER(XDevice), c_int, POINTER(XDeviceControl)]
XSelectExtensionEvent = _lib.XSelectExtensionEvent
XSelectExtensionEvent.restype = c_int
XSelectExtensionEvent.argtypes = [POINTER(Display), Window, POINTER(XEventClass), c_int]
XGetSelectedExtensionEvents = _lib.XGetSelectedExtensionEvents
XGetSelectedExtensionEvents.restype = c_int
XGetSelectedExtensionEvents.argtypes = [POINTER(Display), Window, POINTER(c_int), POINTER(POINTER(XEventClass)), POINTER(c_int), POINTER(POINTER(XEventClass))]
XChangeDeviceDontPropagateList = _lib.XChangeDeviceDontPropagateList
XChangeDeviceDontPropagateList.restype = c_int
XChangeDeviceDontPropagateList.argtypes = [POINTER(Display), Window, c_int, POINTER(XEventClass), c_int]
XGetDeviceDontPropagateList = _lib.XGetDeviceDontPropagateList
XGetDeviceDontPropagateList.restype = POINTER(XEventClass)
XGetDeviceDontPropagateList.argtypes = [POINTER(Display), Window, POINTER(c_int)]
XEvent = pyglet.libs.x11.xlib.XEvent
XSendExtensionEvent = _lib.XSendExtensionEvent
XSendExtensionEvent.restype = c_int
XSendExtensionEvent.argtypes = [POINTER(Display), POINTER(XDevice), Window, c_int, c_int, POINTER(XEventClass), POINTER(XEvent)]
XGetDeviceMotionEvents = _lib.XGetDeviceMotionEvents
XGetDeviceMotionEvents.restype = POINTER(XDeviceTimeCoord)
XGetDeviceMotionEvents.argtypes = [POINTER(Display), POINTER(XDevice), Time, Time, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
XFreeDeviceMotionEvents = _lib.XFreeDeviceMotionEvents
XFreeDeviceMotionEvents.restype = None
XFreeDeviceMotionEvents.argtypes = [POINTER(XDeviceTimeCoord)]
XFreeDeviceControl = _lib.XFreeDeviceControl
XFreeDeviceControl.restype = None
XFreeDeviceControl.argtypes = [POINTER(XDeviceControl)]
__all__ = [
 'sz_xGetExtensionVersionReq', 'sz_xGetExtensionVersionReply', 
 'sz_xListInputDevicesReq', 
 'sz_xListInputDevicesReply', 'sz_xOpenDeviceReq', 
 'sz_xOpenDeviceReply', 
 'sz_xCloseDeviceReq', 'sz_xSetDeviceModeReq', 
 'sz_xSetDeviceModeReply', 
 'sz_xSelectExtensionEventReq', 
 'sz_xGetSelectedExtensionEventsReq', 'sz_xGetSelectedExtensionEventsReply', 
 'sz_xChangeDeviceDontPropagateListReq', 
 'sz_xGetDeviceDontPropagateListReq', 
 'sz_xGetDeviceDontPropagateListReply', 
 'sz_xGetDeviceMotionEventsReq', 
 'sz_xGetDeviceMotionEventsReply', 'sz_xChangeKeyboardDeviceReq', 
 'sz_xChangeKeyboardDeviceReply', 
 'sz_xChangePointerDeviceReq', 
 'sz_xChangePointerDeviceReply', 'sz_xGrabDeviceReq', 
 'sz_xGrabDeviceReply', 
 'sz_xUngrabDeviceReq', 'sz_xGrabDeviceKeyReq', 'sz_xGrabDeviceKeyReply', 
 'sz_xUngrabDeviceKeyReq', 
 'sz_xGrabDeviceButtonReq', 
 'sz_xGrabDeviceButtonReply', 'sz_xUngrabDeviceButtonReq', 
 'sz_xAllowDeviceEventsReq', 
 'sz_xGetDeviceFocusReq', 
 'sz_xGetDeviceFocusReply', 'sz_xSetDeviceFocusReq', 
 'sz_xGetFeedbackControlReq', 
 'sz_xGetFeedbackControlReply', 
 'sz_xChangeFeedbackControlReq', 'sz_xGetDeviceKeyMappingReq', 
 'sz_xGetDeviceKeyMappingReply', 
 'sz_xChangeDeviceKeyMappingReq', 
 'sz_xGetDeviceModifierMappingReq', 'sz_xSetDeviceModifierMappingReq', 
 'sz_xSetDeviceModifierMappingReply', 
 'sz_xGetDeviceButtonMappingReq', 
 'sz_xGetDeviceButtonMappingReply', 'sz_xSetDeviceButtonMappingReq', 
 'sz_xSetDeviceButtonMappingReply', 
 'sz_xQueryDeviceStateReq', 
 'sz_xQueryDeviceStateReply', 'sz_xSendExtensionEventReq', 
 'sz_xDeviceBellReq', 
 'sz_xSetDeviceValuatorsReq', 'sz_xSetDeviceValuatorsReply', 
 'sz_xGetDeviceControlReq', 
 'sz_xGetDeviceControlReply', 
 'sz_xChangeDeviceControlReq', 'sz_xChangeDeviceControlReply', 
 'Dont_Check', 
 'XInput_Initial_Release', 'XInput_Add_XDeviceBell', 
 'XInput_Add_XSetDeviceValuators', 
 'XInput_Add_XChangeDeviceControl', 
 'XInput_Add_DevicePresenceNotify', 'XI_Absent', 
 'XI_Present', 
 'XI_Initial_Release_Major', 'XI_Initial_Release_Minor', 
 'XI_Add_XDeviceBell_Major', 
 'XI_Add_XDeviceBell_Minor', 
 'XI_Add_XSetDeviceValuators_Major', 'XI_Add_XSetDeviceValuators_Minor', 
 'XI_Add_XChangeDeviceControl_Major', 
 'XI_Add_XChangeDeviceControl_Minor', 
 'XI_Add_DevicePresenceNotify_Major', 
 'XI_Add_DevicePresenceNotify_Minor', 
 'DEVICE_RESOLUTION', 'DEVICE_ABS_CALIB', 
 'DEVICE_CORE', 'DEVICE_ENABLE', 
 'DEVICE_ABS_AREA', 'NoSuchExtension', 'COUNT', 
 'CREATE', 'NewPointer', 
 'NewKeyboard', 'XPOINTER', 'XKEYBOARD', 'UseXKeyboard', 
 'IsXPointer', 
 'IsXKeyboard', 'IsXExtensionDevice', 'IsXExtensionKeyboard', 
 'IsXExtensionPointer', 
 'AsyncThisDevice', 'SyncThisDevice', 
 'ReplayThisDevice', 'AsyncOtherDevices', 
 'AsyncAll', 'SyncAll', 
 'FollowKeyboard', 'RevertToFollowKeyboard', 'DvAccelNum', 
 'DvAccelDenom', 
 'DvThreshold', 'DvKeyClickPercent', 'DvPercent', 'DvPitch', 
 'DvDuration', 
 'DvLed', 'DvLedMode', 'DvKey', 'DvAutoRepeatMode', 'DvString', 
 'DvInteger', 
 'DeviceMode', 'Relative', 'Absolute', 'ProximityState', 'InProximity', 
 'OutOfProximity', 
 'AddToList', 'DeleteFromList', 'KeyClass', 'ButtonClass', 
 'ValuatorClass', 
 'FeedbackClass', 'ProximityClass', 'FocusClass', 
 'OtherClass', 'KbdFeedbackClass', 
 'PtrFeedbackClass', 'StringFeedbackClass', 
 'IntegerFeedbackClass', 'LedFeedbackClass', 
 'BellFeedbackClass', 
 '_devicePointerMotionHint', '_deviceButton1Motion', 
 '_deviceButton2Motion', 
 '_deviceButton3Motion', '_deviceButton4Motion', 
 '_deviceButton5Motion', 
 '_deviceButtonMotion', '_deviceButtonGrab', '_deviceOwnerGrabButton', 
 '_noExtensionEvent', 
 '_devicePresence', 'DeviceAdded', 'DeviceRemoved', 
 'DeviceEnabled', 'DeviceDisabled', 
 'DeviceUnrecoverable', 'XI_BadDevice', 
 'XI_BadEvent', 'XI_BadMode', 'XI_DeviceBusy', 
 'XI_BadClass', 'XEventClass', 
 'XExtensionVersion', '_deviceKeyPress', '_deviceKeyRelease', 
 '_deviceButtonPress', 
 '_deviceButtonRelease', '_deviceMotionNotify', 
 '_deviceFocusIn', '_deviceFocusOut', 
 '_proximityIn', '_proximityOut', 
 '_deviceStateNotify', '_deviceMappingNotify', 
 '_changeDeviceNotify', 
 'XDeviceKeyEvent', 'XDeviceKeyPressedEvent', 'XDeviceKeyReleasedEvent', 
 'XDeviceButtonEvent', 
 'XDeviceButtonPressedEvent', 
 'XDeviceButtonReleasedEvent', 'XDeviceMotionEvent', 
 'XDeviceFocusChangeEvent', 
 'XDeviceFocusInEvent', 'XDeviceFocusOutEvent', 
 'XProximityNotifyEvent', 
 'XProximityInEvent', 'XProximityOutEvent', 'XInputClass', 
 'XDeviceStateNotifyEvent', 
 'XValuatorStatus', 'XKeyStatus', 'XButtonStatus', 
 'XDeviceMappingEvent', 
 'XChangeDeviceNotifyEvent', 
 'XDevicePresenceNotifyEvent', 'XFeedbackState', 
 'XKbdFeedbackState', 
 'XPtrFeedbackState', 'XIntegerFeedbackState', 'XStringFeedbackState', 
 'XBellFeedbackState', 
 'XLedFeedbackState', 'XFeedbackControl', 
 'XPtrFeedbackControl', 'XKbdFeedbackControl', 
 'XStringFeedbackControl', 
 'XIntegerFeedbackControl', 'XBellFeedbackControl', 
 'XLedFeedbackControl', 
 'XDeviceControl', 'XDeviceResolutionControl', 'XDeviceResolutionState', 
 'XDeviceAbsCalibControl', 
 'XDeviceAbsCalibState', 'XDeviceAbsAreaControl', 
 'XDeviceAbsAreaState', 
 'XDeviceCoreControl', 'XDeviceCoreState', 
 'XDeviceEnableControl', 'XDeviceEnableState', 
 'XAnyClassPtr', 'XAnyClassInfo', 
 'XDeviceInfoPtr', 'XDeviceInfo', 'XKeyInfoPtr', 
 'XKeyInfo', 'XButtonInfoPtr', 
 'XButtonInfo', 'XAxisInfoPtr', 'XAxisInfo', 
 'XValuatorInfoPtr', 
 'XValuatorInfo', 'XInputClassInfo', 'XDevice', 'XEventList', 
 'XDeviceTimeCoord', 
 'XDeviceState', 'XValuatorState', 'XKeyState', 
 'XButtonState', 'XChangeKeyboardDevice', 
 'XChangePointerDevice', 
 'XGrabDevice', 'XUngrabDevice', 'XGrabDeviceKey', 
 'XUngrabDeviceKey', 
 'XGrabDeviceButton', 'XUngrabDeviceButton', 'XAllowDeviceEvents', 
 'XGetDeviceFocus', 
 'XSetDeviceFocus', 'XGetFeedbackControl', 
 'XFreeFeedbackList', 'XChangeFeedbackControl', 
 'XDeviceBell', 
 'XGetDeviceKeyMapping', 'XChangeDeviceKeyMapping', 
 'XGetDeviceModifierMapping', 
 'XSetDeviceModifierMapping', 
 'XSetDeviceButtonMapping', 'XGetDeviceButtonMapping', 
 'XQueryDeviceState', 
 'XFreeDeviceState', 'XGetExtensionVersion', 'XListInputDevices', 
 'XFreeDeviceList', 
 'XOpenDevice', 'XCloseDevice', 'XSetDeviceMode', 
 'XSetDeviceValuators', 
 'XGetDeviceControl', 'XChangeDeviceControl', 
 'XSelectExtensionEvent', 'XGetSelectedExtensionEvents', 
 'XChangeDeviceDontPropagateList', 
 'XGetDeviceDontPropagateList', 
 'XSendExtensionEvent', 'XGetDeviceMotionEvents', 
 'XFreeDeviceMotionEvents', 
 'XFreeDeviceControl']
# okay decompiling out\pyglet.libs.x11.xinput.pyc
