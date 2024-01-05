# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.input.base
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import sys
from pyglet.event import EventDispatcher
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

class DeviceException(Exception):
    pass


class DeviceOpenException(DeviceException):
    pass


class DeviceExclusiveException(DeviceException):
    pass


class Device(object):

    def __init__(self, display, name):
        self.display = display
        self.name = name
        self.manufacturer = None
        self.is_open = False
        return

    def open(self, window=None, exclusive=False):
        if self.is_open:
            raise DeviceOpenException('Device is already open.')
        self.is_open = True

    def close(self):
        self.is_open = False

    def get_controls(self):
        raise NotImplementedError('abstract')

    def __repr__(self):
        return '%s(name=%s)' % (self.__class__.__name__, self.name)


class Control(EventDispatcher):
    _value = None

    def __init__(self, name, raw_name=None):
        self.name = name
        self.raw_name = raw_name
        self.inverted = False

    def _get_value(self):
        return self._value

    def _set_value(self, value):
        if value == self._value:
            return
        self._value = value
        self.dispatch_event('on_change', value)

    value = property(_get_value, doc='Current value of the control.\n    \n    The range of the value is device-dependent; for absolute controls\n    the range is given by ``min`` and ``max`` (however the value may exceed\n    this range); for relative controls the range is undefined.\n    \n    :type: float')

    def __repr__(self):
        if self.name:
            return '%s(name=%s, raw_name=%s)' % (
             self.__class__.__name__, self.name, self.raw_name)
        else:
            return '%s(raw_name=%s)' % (self.__class__.__name__, self.raw_name)

    if _is_epydoc:

        def on_change(self, value):
            pass


Control.register_event_type('on_change')

class RelativeAxis(Control):
    X = 'x'
    Y = 'y'
    Z = 'z'
    RX = 'rx'
    RY = 'ry'
    RZ = 'rz'
    WHEEL = 'wheel'

    def _get_value(self):
        return self._value

    def _set_value(self, value):
        self._value = value
        self.dispatch_event('on_change', value)

    value = property(_get_value)


class AbsoluteAxis(Control):
    X = 'x'
    Y = 'y'
    Z = 'z'
    RX = 'rx'
    RY = 'ry'
    RZ = 'rz'
    HAT = 'hat'
    HAT_X = 'hat_x'
    HAT_Y = 'hat_y'

    def __init__(self, name, min, max, raw_name=None):
        super(AbsoluteAxis, self).__init__(name, raw_name)
        self.min = min
        self.max = max


class Button(Control):

    def _get_value(self):
        return bool(self._value)

    def _set_value(self, value):
        if value == self._value:
            return
        self._value = value
        self.dispatch_event('on_change', bool(value))
        if value:
            self.dispatch_event('on_press')
        else:
            self.dispatch_event('on_release')

    value = property(_get_value)
    if _is_epydoc:

        def on_press(self):
            pass

        def on_release(self):
            pass


Button.register_event_type('on_press')
Button.register_event_type('on_release')

class Joystick(object):

    def __init__(self, device):
        self.device = device
        self.x = 0
        self.y = 0
        self.z = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.hat_x = 0
        self.hat_y = 0
        self.buttons = []
        self.x_control = None
        self.y_control = None
        self.z_control = None
        self.rx_control = None
        self.ry_control = None
        self.rz_control = None
        self.hat_x_control = None
        self.hat_y_control = None
        self.button_controls = []

        def add_axis(control):
            name = control.name
            scale = 2.0 / (control.max - control.min)
            bias = -1.0 - control.min * scale
            if control.inverted:
                scale = -scale
                bias = -bias
            setattr(self, name + '_control', control)

            @control.event
            def on_change(value):
                setattr(self, name, value * scale + bias)

        def add_button(control):
            i = len(self.buttons)
            self.buttons.append(False)
            self.button_controls.append(control)

            @control.event
            def on_change(value):
                self.buttons[i] = value

        def add_hat(control):
            self.hat_x_control = control
            self.hat_y_control = control

            @control.event
            def on_change(value):
                if value & 65535 == 65535:
                    self.hat_x = self.hat_y = 0
                else:
                    if control.max > 8:
                        value //= 4095
                    if 0 <= value < 8:
                        self.hat_x, self.hat_y = ((0, 1),
                         (1, 1),
                         (1, 0),
                         (1, -1),
                         (0, -1),
                         (-1, -1),
                         (-1, 0),
                         (-1, 1))[value]
                    else:
                        self.hat_x = self.hat_y = 0

        for control in device.get_controls():
            if isinstance(control, AbsoluteAxis):
                if control.name in ('x', 'y', 'z', 'rx', 'ry', 'rz', 'hat_x', 'hat_y'):
                    add_axis(control)
                elif control.name == 'hat':
                    add_hat(control)
            elif isinstance(control, Button):
                add_button(control)

        return

    def open(self, window=None, exclusive=False):
        self.device.open(window, exclusive)

    def close(self):
        self.device.close()


class AppleRemote(EventDispatcher):

    def __init__(self, device):

        def add_button(control):
            setattr(self, control.name + '_control', control)

            @control.event
            def on_press():
                self.dispatch_event('on_button_press', control.name)

            @control.event
            def on_release():
                self.dispatch_event('on_button_release', control.name)

        self.device = device
        for control in device.get_controls():
            if control.name in ('left', 'left_hold', 'right', 'right_hold', 'up', 'down',
                                'menu', 'select', 'menu_hold', 'select_hold'):
                add_button(control)

    def open(self, window=None, exclusive=False):
        self.device.open(window, exclusive)

    def close(self):
        self.device.close()

    def on_button_press(self, button):
        pass

    def on_button_release(self, button):
        pass


AppleRemote.register_event_type('on_button_press')
AppleRemote.register_event_type('on_button_release')

class Tablet(object):

    def open(self, window):
        raise NotImplementedError('abstract')


class TabletCanvas(EventDispatcher):

    def __init__(self, window):
        self.window = window

    def close(self):
        raise NotImplementedError('abstract')

    if _is_epydoc:

        def on_enter(self, cursor):
            pass

        def on_leave(self, cursor):
            pass

        def on_motion(self, cursor, x, y, pressure):
            pass


TabletCanvas.register_event_type('on_enter')
TabletCanvas.register_event_type('on_leave')
TabletCanvas.register_event_type('on_motion')

class TabletCursor(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)
# okay decompiling out\pyglet.input.base.pyc
