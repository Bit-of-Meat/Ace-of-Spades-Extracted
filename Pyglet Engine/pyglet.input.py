# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.input
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import sys
from base import Device, Control, RelativeAxis, AbsoluteAxis, Button, Joystick, AppleRemote, Tablet
from base import DeviceException, DeviceOpenException, DeviceExclusiveException
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

def get_apple_remote(display=None):
    return


if _is_epydoc:

    def get_devices(display=None):
        pass


    def get_joysticks(display=None):
        pass


    def get_tablets(display=None):
        pass


else:

    def get_tablets(display=None):
        return []


    if sys.platform == 'linux2':
        from x11_xinput import get_devices as xinput_get_devices
        from x11_xinput_tablet import get_tablets
        from evdev import get_devices as evdev_get_devices
        from evdev import get_joysticks

        def get_devices(display=None):
            return evdev_get_devices(display) + xinput_get_devices(display)


    elif sys.platform in ('cygwin', 'win32'):
        from directinput import get_devices, get_joysticks
        try:
            from wintab import get_tablets
        except:
            pass

    elif sys.platform == 'darwin':
        from pyglet import options as pyglet_options
        if pyglet_options['darwin_cocoa']:
            from darwin_hid import get_devices, get_joysticks, get_apple_remote
        else:
            from carbon_hid import get_devices, get_joysticks, get_apple_remote
            from carbon_tablet import get_tablets
# okay decompiling out\pyglet.input.pyc
