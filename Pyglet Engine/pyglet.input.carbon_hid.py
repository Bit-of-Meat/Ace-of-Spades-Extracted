# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.input.carbon_hid
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes, pyglet
from pyglet.libs.darwin import carbon, _oscheck, create_cfstring
from ..pyglet.libs.darwin.constants import *
from base import Device, Control, AbsoluteAxis, RelativeAxis, Button
from base import Joystick, AppleRemote
from base import DeviceExclusiveException
void_p = ctypes.POINTER(ctypes.c_int)

class CFUUIDBytes(ctypes.Structure):
    _fields_ = [ ('byte%d' % i, ctypes.c_uint8) for i in range(16) ]


mach_port_t = void_p
io_iterator_t = void_p
kern_return_t = ctypes.c_int
IOReturn = ctypes.c_uint
CFDictionaryRef = void_p
CFMutableDictionaryRef = void_p
CFArrayRef = void_p
CFStringRef = void_p
CFUUIDRef = ctypes.POINTER(CFUUIDBytes)
AbsoluteTime = ctypes.c_double
HRESULT = ctypes.c_int
REFIID = CFUUIDBytes
IOHIDElementType = ctypes.c_int
kIOHIDElementTypeInput_Misc = 1
kIOHIDElementTypeInput_Button = 2
kIOHIDElementTypeInput_Axis = 3
kIOHIDElementTypeInput_ScanCodes = 4
kIOHIDElementTypeOutput = 129
kIOHIDElementTypeFeature = 257
kIOHIDElementTypeCollection = 513
IOHIDElementCookie = ctypes.c_void_p
kHIDPage_GenericDesktop = 1
kHIDUsage_GD_Joystick = 4
kHIDUsage_GD_GamePad = 5
kHIDUsage_GD_Keyboard = 6
kHIDUsage_GD_Keypad = 7
kHIDUsage_GD_MultiAxisController = 8
kHIDUsage_GD_SystemAppMenu = 134
kHIDUsage_GD_SystemMenu = 137
kHIDUsage_GD_SystemMenuRight = 138
kHIDUsage_GD_SystemMenuLeft = 139
kHIDUsage_GD_SystemMenuUp = 140
kHIDUsage_GD_SystemMenuDown = 141
kHIDPage_Consumer = 12
kHIDUsage_Csmr_Menu = 64
kHIDUsage_Csmr_FastForward = 179
kHIDUsage_Csmr_Rewind = 180
MACH_PORT_NULL = 0
kIOHIDDeviceKey = 'IOHIDDevice'
kIOServicePlane = 'IOService'
kIOHIDProductIDKey = 'ProductID'
kCFNumberIntType = 9
kIOHIDOptionsTypeSeizeDevice = 1
kIOReturnExclusiveAccess = 3758097093
carbon.CFUUIDGetConstantUUIDWithBytes.restype = CFUUIDRef
kIOHIDDeviceUserClientTypeID = carbon.CFUUIDGetConstantUUIDWithBytes(None, 250, 18, 250, 56, 111, 26, 17, 212, 186, 12, 0, 5, 2, 143, 24, 213)
kIOCFPlugInInterfaceID = carbon.CFUUIDGetConstantUUIDWithBytes(None, 194, 68, 232, 88, 16, 156, 17, 212, 145, 212, 0, 80, 228, 198, 66, 111)
kIOHIDDeviceInterfaceID = carbon.CFUUIDGetConstantUUIDWithBytes(None, 120, 189, 66, 12, 111, 20, 17, 212, 148, 116, 0, 5, 2, 143, 24, 213)
IOHIDCallbackFunction = ctypes.CFUNCTYPE(None, void_p, IOReturn, ctypes.c_void_p, ctypes.c_void_p)
CFRunLoopSourceRef = ctypes.c_void_p

class IOHIDEventStruct(ctypes.Structure):
    _fields_ = (
     (
      'type', IOHIDElementType),
     (
      'elementCookie', IOHIDElementCookie),
     (
      'value', ctypes.c_int32),
     (
      'timestamp', AbsoluteTime),
     (
      'longValueSize', ctypes.c_uint32),
     (
      'longValue', ctypes.c_void_p))


Self = ctypes.c_void_p

class IUnknown(ctypes.Structure):
    _fields_ = (
     (
      '_reserved', ctypes.c_void_p),
     (
      'QueryInterface',
      ctypes.CFUNCTYPE(HRESULT, Self, REFIID, ctypes.c_void_p)),
     (
      'AddRef',
      ctypes.CFUNCTYPE(ctypes.c_ulong, Self)),
     (
      'Release',
      ctypes.CFUNCTYPE(ctypes.c_ulong, Self)))


class IOHIDQueueInterface(ctypes.Structure):
    _fields_ = IUnknown._fields_ + (
     (
      'createAsyncEventSource',
      ctypes.CFUNCTYPE(IOReturn, Self, ctypes.POINTER(CFRunLoopSourceRef))),
     (
      'getAsyncEventSource', ctypes.c_void_p),
     (
      'createAsyncPort', ctypes.c_void_p),
     (
      'getAsyncPort', ctypes.c_void_p),
     (
      'create',
      ctypes.CFUNCTYPE(IOReturn, Self, ctypes.c_uint32, ctypes.c_uint32)),
     (
      'dispose',
      ctypes.CFUNCTYPE(IOReturn, Self)),
     (
      'addElement',
      ctypes.CFUNCTYPE(IOReturn, Self, IOHIDElementCookie)),
     (
      'removeElement', ctypes.c_void_p),
     (
      'hasElement', ctypes.c_void_p),
     (
      'start',
      ctypes.CFUNCTYPE(IOReturn, Self)),
     (
      'stop',
      ctypes.CFUNCTYPE(IOReturn, Self)),
     (
      'getNextEvent',
      ctypes.CFUNCTYPE(IOReturn, Self, ctypes.POINTER(IOHIDEventStruct), AbsoluteTime, ctypes.c_uint32)),
     (
      'setEventCallout',
      ctypes.CFUNCTYPE(IOReturn, Self, IOHIDCallbackFunction, ctypes.c_void_p, ctypes.c_void_p)),
     (
      'getEventCallout', ctypes.c_void_p))


class IOHIDDeviceInterface(ctypes.Structure):
    _fields_ = IUnknown._fields_ + (
     (
      'createAsyncEventSource', ctypes.c_void_p),
     (
      'getAsyncEventSource', ctypes.c_void_p),
     (
      'createAsyncPort', ctypes.c_void_p),
     (
      'getAsyncPort', ctypes.c_void_p),
     (
      'open',
      ctypes.CFUNCTYPE(IOReturn, Self, ctypes.c_uint32)),
     (
      'close',
      ctypes.CFUNCTYPE(IOReturn, Self)),
     (
      'setRemovalCallback', ctypes.c_void_p),
     (
      'getElementValue',
      ctypes.CFUNCTYPE(IOReturn, Self, IOHIDElementCookie, ctypes.POINTER(IOHIDEventStruct))),
     (
      'setElementValue', ctypes.c_void_p),
     (
      'queryElementValue', ctypes.c_void_p),
     (
      'startAllQueues', ctypes.c_void_p),
     (
      'stopAllQueues', ctypes.c_void_p),
     (
      'allocQueue',
      ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.POINTER(IOHIDQueueInterface)), Self)),
     (
      'allocOutputTransaction', ctypes.c_void_p),
     (
      'setReport', ctypes.c_void_p),
     (
      'getReport', ctypes.c_void_p),
     (
      'copyMatchingElements',
      ctypes.CFUNCTYPE(IOReturn, Self, CFDictionaryRef, ctypes.POINTER(CFArrayRef))),
     (
      'setInterruptReportHandlerCallback', ctypes.c_void_p))


def get_master_port():
    master_port = mach_port_t()
    _oscheck(carbon.IOMasterPort(MACH_PORT_NULL, ctypes.byref(master_port)))
    return master_port


def get_matching_dictionary():
    carbon.IOServiceMatching.restype = CFMutableDictionaryRef
    matching_dictionary = carbon.IOServiceMatching(kIOHIDDeviceKey)
    return matching_dictionary


def get_matching_services(master_port, matching_dictionary):
    iterator = io_iterator_t()
    _oscheck(carbon.IOServiceGetMatchingServices(master_port, matching_dictionary, ctypes.byref(iterator)))
    services = []
    while carbon.IOIteratorIsValid(iterator):
        service = carbon.IOIteratorNext(iterator)
        if not service:
            break
        services.append(service)

    carbon.IOObjectRelease(iterator)
    return services


def cfstring_to_string(value_string):
    value_length = carbon.CFStringGetLength(value_string)
    buffer_length = carbon.CFStringGetMaximumSizeForEncoding(value_length, kCFStringEncodingUTF8)
    buffer = ctypes.c_buffer(buffer_length + 1)
    result = carbon.CFStringGetCString(value_string, buffer, len(buffer), kCFStringEncodingUTF8)
    if not result:
        return
    return buffer.value


def cfnumber_to_int(value):
    result = ctypes.c_int()
    carbon.CFNumberGetValue(value, kCFNumberIntType, ctypes.byref(result))
    return result.value


def cfboolean_to_bool(value):
    return bool(carbon.CFBooleanGetValue(value))


def cfvalue_to_value(value):
    if not value:
        return
    else:
        value_type = carbon.CFGetTypeID(value)
        if value_type == carbon.CFStringGetTypeID():
            return cfstring_to_string(value)
        if value_type == carbon.CFNumberGetTypeID():
            return cfnumber_to_int(value)
        if value_type == carbon.CFBooleanGetTypeID():
            return cfboolean_to_bool(value)
        return
        return


def get_property_value(properties, key):
    key_string = create_cfstring(key)
    value = ctypes.c_void_p()
    present = carbon.CFDictionaryGetValueIfPresent(properties, key_string, ctypes.byref(value))
    carbon.CFRelease(key_string)
    if not present:
        return None
    else:
        return value


def get_property(properties, key):
    return cfvalue_to_value(get_property_value(properties, key))


def dump_properties(properties):

    def func(key, value, context):
        print '%s = %s' % (cfstring_to_string(key), cfvalue_to_value(value))

    CFDictionaryApplierFunction = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
    carbon.CFDictionaryApplyFunction(properties, CFDictionaryApplierFunction(func), None)
    return


class DarwinHIDDevice(Device):

    def __init__(self, display, generic_device):
        super(DarwinHIDDevice, self).__init__(display, name=None)
        self._device = self._get_device_interface(generic_device)
        properties = CFMutableDictionaryRef()
        _oscheck(carbon.IORegistryEntryCreateCFProperties(generic_device, ctypes.byref(properties), None, 0))
        self.name = get_property(properties, 'Product')
        self.manufacturer = get_property(properties, 'Manufacturer')
        self.usage_page = get_property(properties, 'PrimaryUsagePage')
        self.usage = get_property(properties, 'PrimaryUsage')
        carbon.CFRelease(properties)
        self._controls = self._init_controls()
        self._open = False
        self._queue = None
        self._queue_depth = 8
        return

    def _get_device_interface(self, generic_device):
        plug_in_interface = ctypes.POINTER(ctypes.POINTER(IUnknown))()
        score = ctypes.c_int32()
        _oscheck(carbon.IOCreatePlugInInterfaceForService(generic_device, kIOHIDDeviceUserClientTypeID, kIOCFPlugInInterfaceID, ctypes.byref(plug_in_interface), ctypes.byref(score)))
        carbon.CFUUIDGetUUIDBytes.restype = CFUUIDBytes
        hid_device_interface = ctypes.POINTER(ctypes.POINTER(IOHIDDeviceInterface))()
        _oscheck(plug_in_interface.contents.contents.QueryInterface(plug_in_interface, carbon.CFUUIDGetUUIDBytes(kIOHIDDeviceInterfaceID), ctypes.byref(hid_device_interface)))
        plug_in_interface.contents.contents.Release(plug_in_interface)
        return hid_device_interface

    def _init_controls(self):
        elements_array = CFArrayRef()
        _oscheck(self._device.contents.contents.copyMatchingElements(self._device, None, ctypes.byref(elements_array)))
        self._control_cookies = {}
        controls = []
        n_elements = carbon.CFArrayGetCount(elements_array)
        for i in range(n_elements):
            properties = carbon.CFArrayGetValueAtIndex(elements_array, i)
            control = _create_control(properties)
            if control:
                controls.append(control)
                self._control_cookies[control._cookie] = control

        carbon.CFRelease(elements_array)
        return controls

    def open(self, window=None, exclusive=False):
        super(DarwinHIDDevice, self).open(window, exclusive)
        flags = 0
        if exclusive:
            flags |= kIOHIDOptionsTypeSeizeDevice
        result = self._device.contents.contents.open(self._device, flags)
        if result == 0:
            self._open = True
        else:
            if result == kIOReturnExclusiveAccess:
                raise DeviceExclusiveException()
            self._queue = self._device.contents.contents.allocQueue(self._device)
            _oscheck(self._queue.contents.contents.create(self._queue, 0, self._queue_depth))
            for control in self._controls:
                r = self._queue.contents.contents.addElement(self._queue, control._cookie, 0)
                if r != 0:
                    print 'error adding %r' % control

        self._event_source = CFRunLoopSourceRef()
        self._queue_callback_func = IOHIDCallbackFunction(self._queue_callback)
        _oscheck(self._queue.contents.contents.createAsyncEventSource(self._queue, ctypes.byref(self._event_source)))
        _oscheck(self._queue.contents.contents.setEventCallout(self._queue, self._queue_callback_func, None, None))
        event_loop = pyglet.app.platform_event_loop._event_loop
        carbon.GetCFRunLoopFromEventLoop.restype = void_p
        run_loop = carbon.GetCFRunLoopFromEventLoop(event_loop)
        kCFRunLoopDefaultMode = CFStringRef.in_dll(carbon, 'kCFRunLoopDefaultMode')
        carbon.CFRunLoopAddSource(run_loop, self._event_source, kCFRunLoopDefaultMode)
        _oscheck(self._queue.contents.contents.start(self._queue))
        return

    def close(self):
        super(DarwinHIDDevice, self).close()
        if not self._open:
            return
        else:
            _oscheck(self._queue.contents.contents.stop(self._queue))
            _oscheck(self._queue.contents.contents.dispose(self._queue))
            self._queue.contents.contents.Release(self._queue)
            self._queue = None
            _oscheck(self._device.contents.contents.close(self._device))
            self._open = False
            return

    def get_controls(self):
        return self._controls

    def _queue_callback(self, target, result, refcon, sender):
        if not self._open:
            return
        event = IOHIDEventStruct()
        r = self._queue.contents.contents.getNextEvent(self._queue, ctypes.byref(event), 0, 0)
        while r == 0:
            try:
                control = self._control_cookies[event.elementCookie]
                control._set_value(event.value)
            except KeyError:
                pass

            r = self._queue.contents.contents.getNextEvent(self._queue, ctypes.byref(event), 0, 0)


_axis_names = {(1, 48): 'x', 
   (1, 49): 'y', 
   (1, 50): 'z', 
   (1, 51): 'rx', 
   (1, 52): 'ry', 
   (1, 53): 'rz', 
   (1, 56): 'wheel', 
   (1, 57): 'hat'}
_button_names = {(kHIDPage_GenericDesktop, kHIDUsage_GD_SystemAppMenu): 'menu', 
   (kHIDPage_GenericDesktop, kHIDUsage_GD_SystemMenu): 'select', 
   (kHIDPage_GenericDesktop, kHIDUsage_GD_SystemMenuRight): 'right', 
   (kHIDPage_GenericDesktop, kHIDUsage_GD_SystemMenuLeft): 'left', 
   (kHIDPage_GenericDesktop, kHIDUsage_GD_SystemMenuUp): 'up', 
   (kHIDPage_GenericDesktop, kHIDUsage_GD_SystemMenuDown): 'down', 
   (kHIDPage_Consumer, kHIDUsage_Csmr_FastForward): 'right_hold', 
   (kHIDPage_Consumer, kHIDUsage_Csmr_Rewind): 'left_hold', 
   (kHIDPage_Consumer, kHIDUsage_Csmr_Menu): 'menu_hold', 
   (65281, 35): 'select_hold'}

def _create_control(properties):
    type = get_property(properties, 'Type')
    if type not in (kIOHIDElementTypeInput_Misc,
     kIOHIDElementTypeInput_Axis,
     kIOHIDElementTypeInput_Button):
        return
    cookie = get_property(properties, 'ElementCookie')
    usage_page = get_property(properties, 'UsagePage')
    usage = get_property(properties, 'Usage')
    raw_name = get_property(properties, 'Name')
    if not raw_name:
        raw_name = '%d:%d' % (usage_page, usage)
    if type in (kIOHIDElementTypeInput_Misc, kIOHIDElementTypeInput_Axis):
        name = _axis_names.get((usage_page, usage))
        relative = get_property(properties, 'IsRelative')
        if relative:
            control = RelativeAxis(name, raw_name)
        else:
            min = get_property(properties, 'Min')
            max = get_property(properties, 'Max')
            control = AbsoluteAxis(name, min, max, raw_name)
    elif type == kIOHIDElementTypeInput_Button:
        name = _button_names.get((usage_page, usage))
        control = Button(name, raw_name)
    else:
        return
    control._cookie = cookie
    return control


def _create_joystick(device):
    if device.usage_page == kHIDPage_GenericDesktop and device.usage not in (kHIDUsage_GD_Joystick,
     kHIDUsage_GD_GamePad,
     kHIDUsage_GD_MultiAxisController):
        return
    return Joystick(device)


def get_devices(display=None):
    services = get_matching_services(get_master_port(), get_matching_dictionary())
    return [ DarwinHIDDevice(display, service) for service in services ]


def get_joysticks(display=None):
    return filter(None, [ _create_joystick(device) for device in get_devices(display) ])


def get_apple_remote(display=None):
    for device in get_devices(display):
        if device.name == 'Apple IR':
            return AppleRemote(device)
# okay decompiling out\pyglet.input.carbon_hid.pyc
