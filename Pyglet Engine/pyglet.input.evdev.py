# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.input.evdev
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes, errno, os, pyglet
from pyglet.app.xlib import XlibSelectDevice
from base import Device, Control, RelativeAxis, AbsoluteAxis, Button, Joystick
from base import DeviceOpenException
from ..evdev_constants import *
from evdev_constants import _rel_raw_names, _abs_raw_names, _key_raw_names
c = pyglet.lib.load_library('c')
_IOC_NRBITS = 8
_IOC_TYPEBITS = 8
_IOC_SIZEBITS = 14
_IOC_DIRBITS = 2
_IOC_NRMASK = (1 << _IOC_NRBITS) - 1
_IOC_TYPEMASK = (1 << _IOC_TYPEBITS) - 1
_IOC_SIZEMASK = (1 << _IOC_SIZEBITS) - 1
_IOC_DIRMASK = (1 << _IOC_DIRBITS) - 1
_IOC_NRSHIFT = 0
_IOC_TYPESHIFT = _IOC_NRSHIFT + _IOC_NRBITS
_IOC_SIZESHIFT = _IOC_TYPESHIFT + _IOC_TYPEBITS
_IOC_DIRSHIFT = _IOC_SIZESHIFT + _IOC_SIZEBITS
_IOC_NONE = 0
_IOC_WRITE = 1
_IOC_READ = 2

def _IOC(dir, type, nr, size):
    return dir << _IOC_DIRSHIFT | type << _IOC_TYPESHIFT | nr << _IOC_NRSHIFT | size << _IOC_SIZESHIFT


def _IOR(type, nr, struct):
    request = _IOC(_IOC_READ, ord(type), nr, ctypes.sizeof(struct))

    def f(fileno):
        buffer = struct()
        if c.ioctl(fileno, request, ctypes.byref(buffer)) < 0:
            err = ctypes.c_int.in_dll(c, 'errno').value
            raise OSError(err, errno.errorcode[err])
        return buffer

    return f


def _IOR_len(type, nr):

    def f(fileno, buffer):
        request = _IOC(_IOC_READ, ord(type), nr, ctypes.sizeof(buffer))
        if c.ioctl(fileno, request, ctypes.byref(buffer)) < 0:
            err = ctypes.c_int.in_dll(c, 'errno').value
            raise OSError(err, errno.errorcode[err])
        return buffer

    return f


def _IOR_str(type, nr):
    g = _IOR_len(type, nr)

    def f(fileno, len=256):
        return g(fileno, ctypes.create_string_buffer(len)).value

    return f


time_t = ctypes.c_long
suseconds_t = ctypes.c_long

class timeval(ctypes.Structure):
    _fields_ = (
     (
      'tv_sec', time_t),
     (
      'tv_usec', suseconds_t))


class input_event(ctypes.Structure):
    _fields_ = (
     (
      'time', timeval),
     (
      'type', ctypes.c_uint16),
     (
      'code', ctypes.c_uint16),
     (
      'value', ctypes.c_int32))


class input_id(ctypes.Structure):
    _fields_ = (
     (
      'bustype', ctypes.c_uint16),
     (
      'vendor', ctypes.c_uint16),
     (
      'product', ctypes.c_uint16),
     (
      'version', ctypes.c_uint16))


class input_absinfo(ctypes.Structure):
    _fields_ = (
     (
      'value', ctypes.c_int32),
     (
      'minimum', ctypes.c_int32),
     (
      'maximum', ctypes.c_int32),
     (
      'fuzz', ctypes.c_int32),
     (
      'flat', ctypes.c_int32))


EVIOCGVERSION = _IOR('E', 1, ctypes.c_int)
EVIOCGID = _IOR('E', 2, input_id)
EVIOCGNAME = _IOR_str('E', 6)
EVIOCGPHYS = _IOR_str('E', 7)
EVIOCGUNIQ = _IOR_str('E', 8)

def EVIOCGBIT(fileno, ev, buffer):
    return _IOR_len('E', 32 + ev)(fileno, buffer)


def EVIOCGABS(fileno, abs):
    buffer = input_absinfo()
    return _IOR_len('E', 64 + abs)(fileno, buffer)


def get_set_bits(bytes):
    bits = set()
    j = 0
    for byte in bytes:
        for i in range(8):
            if byte & 1:
                bits.add(j + i)
            byte >>= 1

        j += 8

    return bits


_abs_names = {ABS_X: AbsoluteAxis.X, 
   ABS_Y: AbsoluteAxis.Y, 
   ABS_Z: AbsoluteAxis.Z, 
   ABS_RX: AbsoluteAxis.RX, 
   ABS_RY: AbsoluteAxis.RY, 
   ABS_RZ: AbsoluteAxis.RZ, 
   ABS_HAT0X: AbsoluteAxis.HAT_X, 
   ABS_HAT0Y: AbsoluteAxis.HAT_Y}
_rel_names = {REL_X: RelativeAxis.X, 
   REL_Y: RelativeAxis.Y, 
   REL_Z: RelativeAxis.Z, 
   REL_RX: RelativeAxis.RX, 
   REL_RY: RelativeAxis.RY, 
   REL_RZ: RelativeAxis.RZ, 
   REL_WHEEL: RelativeAxis.WHEEL}

def _create_control(fileno, event_type, event_code):
    if event_type == EV_ABS:
        raw_name = _abs_raw_names.get(event_code, 'EV_ABS(%x)' % event_code)
        name = _abs_names.get(event_code)
        absinfo = EVIOCGABS(fileno, event_code)
        value = absinfo.value
        min = absinfo.minimum
        max = absinfo.maximum
        control = AbsoluteAxis(name, min, max, raw_name)
        control._set_value(value)
        if name == 'hat_y':
            control.inverted = True
    elif event_type == EV_REL:
        raw_name = _rel_raw_names.get(event_code, 'EV_REL(%x)' % event_code)
        name = _rel_names.get(event_code)
        control = RelativeAxis(name, raw_name)
    elif event_type == EV_KEY:
        raw_name = _key_raw_names.get(event_code, 'EV_KEY(%x)' % event_code)
        name = None
        control = Button(name, raw_name)
    else:
        value = min = max = 0
        return
    control._event_type = event_type
    control._event_code = event_code
    return control


def _create_joystick(device):
    have_x = False
    have_y = False
    have_button = False
    for control in device.controls:
        if control._event_type == EV_ABS and control._event_code == ABS_X:
            have_x = True
        elif control._event_type == EV_ABS and control._event_code == ABS_Y:
            have_y = True
        elif control._event_type == EV_KEY and control._event_code == BTN_JOYSTICK:
            have_button = True

    if not (have_x and have_y and have_button):
        return
    return Joystick(device)


event_types = {EV_KEY: KEY_MAX, 
   EV_REL: REL_MAX, 
   EV_ABS: ABS_MAX, 
   EV_MSC: MSC_MAX, 
   EV_LED: LED_MAX, 
   EV_SND: SND_MAX}

class EvdevDevice(XlibSelectDevice, Device):
    _fileno = None

    def __init__(self, display, filename):
        self._filename = filename
        fileno = os.open(filename, os.O_RDONLY)
        id = EVIOCGID(fileno)
        self.id_bustype = id.bustype
        self.id_vendor = hex(id.vendor)
        self.id_product = hex(id.product)
        self.id_version = id.version
        name = EVIOCGNAME(fileno)
        try:
            name = name.decode('utf-8')
        except UnicodeDecodeError:
            try:
                name = name.decode('latin-1')
            except UnicodeDecodeError:
                pass

        try:
            self.phys = EVIOCGPHYS(fileno)
        except OSError:
            self.phys = ''

        try:
            self.uniq = EVIOCGUNIQ(fileno)
        except OSError:
            self.uniq = ''

        self.controls = []
        self.control_map = {}
        event_types_bits = (ctypes.c_byte * 4)()
        EVIOCGBIT(fileno, 0, event_types_bits)
        for event_type in get_set_bits(event_types_bits):
            if event_type not in event_types:
                continue
            max_code = event_types[event_type]
            nbytes = max_code // 8 + 1
            event_codes_bits = (ctypes.c_byte * nbytes)()
            EVIOCGBIT(fileno, event_type, event_codes_bits)
            for event_code in get_set_bits(event_codes_bits):
                control = _create_control(fileno, event_type, event_code)
                if control:
                    self.control_map[(event_type, event_code)] = control
                    self.controls.append(control)

        os.close(fileno)
        super(EvdevDevice, self).__init__(display, name)

    def open(self, window=None, exclusive=False):
        super(EvdevDevice, self).open(window, exclusive)
        try:
            self._fileno = os.open(self._filename, os.O_RDONLY | os.O_NONBLOCK)
        except OSError as e:
            raise DeviceOpenException(e)

        pyglet.app.platform_event_loop._select_devices.add(self)

    def close(self):
        super(EvdevDevice, self).close()
        if not self._fileno:
            return
        else:
            pyglet.app.platform_event_loop._select_devices.remove(self)
            os.close(self._fileno)
            self._fileno = None
            return

    def get_controls(self):
        return self.controls

    def fileno(self):
        return self._fileno

    def poll(self):
        return False

    def select(self):
        if not self._fileno:
            return
        events = (input_event * 64)()
        bytes = c.read(self._fileno, events, ctypes.sizeof(events))
        if bytes < 0:
            return
        n_events = bytes // ctypes.sizeof(input_event)
        for event in events[:n_events]:
            try:
                control = self.control_map[(event.type, event.code)]
                control._set_value(event.value)
            except KeyError:
                pass


_devices = {}

def get_devices(display=None):
    base = '/dev/input'
    for filename in os.listdir(base):
        if filename.startswith('event'):
            path = os.path.join(base, filename)
            if path in _devices:
                continue
            try:
                _devices[path] = EvdevDevice(display, path)
            except OSError:
                pass

    return _devices.values()


def get_joysticks(display=None):
    return filter(None, [ _create_joystick(d) for d in get_devices(display) ])
# okay decompiling out\pyglet.input.evdev.pyc
