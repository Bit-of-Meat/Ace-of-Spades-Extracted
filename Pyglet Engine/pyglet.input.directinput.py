# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.input.directinput
import ctypes, pyglet
from pyglet.input import base
from pyglet.libs import win32
from pyglet.libs.win32 import dinput
from pyglet.libs.win32 import _kernel32
_abs_instance_names = {0: 'x', 
   1: 'y', 
   2: 'z', 
   3: 'rx', 
   4: 'ry', 
   5: 'rz'}
_rel_instance_names = {0: 'x', 
   1: 'y', 
   2: 'wheel'}
_btn_instance_names = {}

def _create_control(object_instance):
    raw_name = object_instance.tszName
    type = object_instance.dwType
    instance = dinput.DIDFT_GETINSTANCE(type)
    if type & dinput.DIDFT_ABSAXIS:
        name = _abs_instance_names.get(instance)
        control = base.AbsoluteAxis(name, 0, 65535, raw_name)
    elif type & dinput.DIDFT_RELAXIS:
        name = _rel_instance_names.get(instance)
        control = base.RelativeAxis(name, raw_name)
    elif type & dinput.DIDFT_BUTTON:
        name = _btn_instance_names.get(instance)
        control = base.Button(name, raw_name)
    elif type & dinput.DIDFT_POV:
        control = base.AbsoluteAxis(base.AbsoluteAxis.HAT, 0, 4294967295, raw_name)
    else:
        return
    control._type = object_instance.dwType
    return control


class DirectInputDevice(base.Device):

    def __init__(self, display, device, device_instance):
        name = device_instance.tszInstanceName
        super(DirectInputDevice, self).__init__(display, name)
        self._type = device_instance.dwDevType & 255
        self._subtype = device_instance.dwDevType & 65280
        self._device = device
        self._init_controls()
        self._set_format()

    def _init_controls(self):
        self.controls = []
        self._device.EnumObjects(dinput.LPDIENUMDEVICEOBJECTSCALLBACK(self._object_enum), None, dinput.DIDFT_ALL)
        return

    def _object_enum(self, object_instance, arg):
        control = _create_control(object_instance.contents)
        if control:
            self.controls.append(control)
        return dinput.DIENUM_CONTINUE

    def _set_format(self):
        if not self.controls:
            return
        object_formats = (dinput.DIOBJECTDATAFORMAT * len(self.controls))()
        offset = 0
        for object_format, control in zip(object_formats, self.controls):
            object_format.dwOfs = offset
            object_format.dwType = control._type
            offset += 4

        format = dinput.DIDATAFORMAT()
        format.dwSize = ctypes.sizeof(format)
        format.dwObjSize = ctypes.sizeof(dinput.DIOBJECTDATAFORMAT)
        format.dwFlags = 0
        format.dwDataSize = offset
        format.dwNumObjs = len(object_formats)
        format.rgodf = ctypes.cast(ctypes.pointer(object_formats), dinput.LPDIOBJECTDATAFORMAT)
        self._device.SetDataFormat(format)
        prop = dinput.DIPROPDWORD()
        prop.diph.dwSize = ctypes.sizeof(prop)
        prop.diph.dwHeaderSize = ctypes.sizeof(prop.diph)
        prop.diph.dwObj = 0
        prop.diph.dwHow = dinput.DIPH_DEVICE
        prop.dwData = 64 * ctypes.sizeof(dinput.DIDATAFORMAT)
        self._device.SetProperty(dinput.DIPROP_BUFFERSIZE, ctypes.byref(prop.diph))

    def open(self, window=None, exclusive=False):
        if not self.controls:
            return
        else:
            if window is None:
                window = pyglet.gl._shadow_window
                for window in pyglet.app.windows:
                    break

            flags = dinput.DISCL_BACKGROUND
            if exclusive:
                flags |= dinput.DISCL_EXCLUSIVE
            else:
                flags |= dinput.DISCL_NONEXCLUSIVE
            self._wait_object = _kernel32.CreateEventW(None, False, False, None)
            self._device.SetEventNotification(self._wait_object)
            pyglet.app.platform_event_loop.add_wait_object(self._wait_object, self._dispatch_events)
            self._device.SetCooperativeLevel(window._hwnd, flags)
            self._device.Acquire()
            return

    def close(self):
        if not self.controls:
            return
        else:
            pyglet.app.platform_event_loop.remove_wait_object(self._wait_object)
            self._device.Unacquire()
            self._device.SetEventNotification(None)
            _kernel32.CloseHandle(self._wait_object)
            return

    def get_controls(self):
        return self.controls

    def _dispatch_events(self):
        if not self.controls:
            return
        events = (dinput.DIDEVICEOBJECTDATA * 64)()
        n_events = win32.DWORD(len(events))
        self._device.GetDeviceData(ctypes.sizeof(dinput.DIDEVICEOBJECTDATA), ctypes.cast(ctypes.pointer(events), dinput.LPDIDEVICEOBJECTDATA), ctypes.byref(n_events), 0)
        for event in events[:n_events.value]:
            index = event.dwOfs // 4
            self.controls[index]._set_value(event.dwData)


_i_dinput = None

def _init_directinput():
    global _i_dinput
    if _i_dinput:
        return
    else:
        _i_dinput = dinput.IDirectInput8()
        module = _kernel32.GetModuleHandleW(None)
        dinput.DirectInput8Create(module, dinput.DIRECTINPUT_VERSION, dinput.IID_IDirectInput8W, ctypes.byref(_i_dinput), None)
        return


def get_devices(display=None):
    _init_directinput()
    _devices = []

    def _device_enum(device_instance, arg):
        device = dinput.IDirectInputDevice8()
        _i_dinput.CreateDevice(device_instance.contents.guidInstance, ctypes.byref(device), None)
        _devices.append(DirectInputDevice(display, device, device_instance.contents))
        return dinput.DIENUM_CONTINUE

    _i_dinput.EnumDevices(dinput.DI8DEVCLASS_ALL, dinput.LPDIENUMDEVICESCALLBACK(_device_enum), None, dinput.DIEDFL_ATTACHEDONLY)
    return _devices


def _create_joystick(device):
    if device._type in (dinput.DI8DEVTYPE_JOYSTICK,
     dinput.DI8DEVTYPE_GAMEPAD):
        return base.Joystick(device)


def get_joysticks(display=None):
    return filter(None, [ _create_joystick(d) for d in get_devices(display) ])
# okay decompiling out\pyglet.input.directinput.pyc
