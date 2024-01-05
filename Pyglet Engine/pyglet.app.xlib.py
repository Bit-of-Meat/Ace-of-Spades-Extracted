# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.app.xlib
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import os, select, threading
from ..ctypes import *
from pyglet import app
from pyglet.app.base import PlatformEventLoop
from pyglet.compat import asbytes

class XlibSelectDevice(object):

    def fileno(self):
        raise NotImplementedError('abstract')

    def select(self):
        raise NotImplementedError('abstract')

    def poll(self):
        return False


class NotificationDevice(XlibSelectDevice):

    def __init__(self):
        self._sync_file_read, self._sync_file_write = os.pipe()
        self._event = threading.Event()

    def fileno(self):
        return self._sync_file_read

    def set(self):
        self._event.set()
        os.write(self._sync_file_write, asbytes('1'))

    def select(self):
        self._event.clear()
        app.platform_event_loop.dispatch_posted_events()

    def poll(self):
        return self._event.isSet()


class XlibEventLoop(PlatformEventLoop):

    def __init__(self):
        super(XlibEventLoop, self).__init__()
        self._notification_device = NotificationDevice()
        self._select_devices = set()
        self._select_devices.add(self._notification_device)

    def notify(self):
        self._notification_device.set()

    def step(self, timeout=None):
        pending_devices = []
        for device in self._select_devices:
            if device.poll():
                pending_devices.append(device)

        if not pending_devices and (timeout is None or not timeout):
            iwtd = self._select_devices
            pending_devices, _, _ = select.select(iwtd, (), (), timeout)
        if not pending_devices:
            return False
        else:
            for device in pending_devices:
                device.select()

            for window in app.windows:
                if window._needs_resize:
                    window.switch_to()
                    window.dispatch_event('on_resize', window._width, window._height)
                    window.dispatch_event('on_expose')
                    window._needs_resize = False

            return True
# okay decompiling out\pyglet.app.xlib.pyc
