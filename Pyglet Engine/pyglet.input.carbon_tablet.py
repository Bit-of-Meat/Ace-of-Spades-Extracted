# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.input.carbon_tablet
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes, pyglet
from pyglet.input.base import Tablet, TabletCanvas, TabletCursor
from pyglet.window.carbon import CarbonEventHandler
from ..pyglet.libs.darwin import *
from pyglet.libs.darwin import _oscheck

class CarbonTablet(Tablet):
    name = 'OS X System Tablet'

    def open(self, window):
        return CarbonTabletCanvas(window)


_carbon_tablet = CarbonTablet()

class CarbonTabletCanvas(TabletCanvas):

    def __init__(self, window):
        super(CarbonTabletCanvas, self).__init__(window)
        for funcname in dir(self):
            func = getattr(self, funcname)
            if hasattr(func, '_platform_event'):
                window._install_event_handler(func)

        self._cursors = {}
        self._cursor = None
        return

    def close(self):
        pass

    def _get_cursor(self, proximity_rec):
        key = (
         proximity_rec.vendorID,
         proximity_rec.tabletID,
         proximity_rec.pointerID,
         proximity_rec.deviceID,
         proximity_rec.systemTabletID,
         proximity_rec.vendorPointerType,
         proximity_rec.pointerSerialNumber,
         proximity_rec.uniqueID,
         proximity_rec.pointerType)
        if key in self._cursors:
            cursor = self._cursors[key]
        else:
            self._cursors[key] = cursor = CarbonTabletCursor(proximity_rec.pointerType)
        self._cursor = cursor
        return cursor

    @CarbonEventHandler(kEventClassTablet, kEventTabletProximity)
    @CarbonEventHandler(kEventClassTablet, kEventTabletPoint)
    @CarbonEventHandler(kEventClassMouse, kEventMouseDragged)
    @CarbonEventHandler(kEventClassMouse, kEventMouseDown)
    @CarbonEventHandler(kEventClassMouse, kEventMouseUp)
    @CarbonEventHandler(kEventClassMouse, kEventMouseMoved)
    def _tablet_event(self, next_handler, ev, data):
        event_type = ctypes.c_uint32()
        r = carbon.GetEventParameter(ev, kEventParamTabletEventType, typeUInt32, None, ctypes.sizeof(event_type), None, ctypes.byref(event_type))
        if r != noErr:
            return False
        else:
            if event_type.value == kEventTabletProximity:
                proximity_rec = TabletProximityRec()
                _oscheck(carbon.GetEventParameter(ev, kEventParamTabletProximityRec, typeTabletProximityRec, None, ctypes.sizeof(proximity_rec), None, ctypes.byref(proximity_rec)))
                cursor = self._get_cursor(proximity_rec)
                if proximity_rec.enterProximity:
                    self.dispatch_event('on_enter', cursor)
                else:
                    self.dispatch_event('on_leave', cursor)
            elif event_type.value == kEventTabletPoint:
                point_rec = TabletPointRec()
                _oscheck(carbon.GetEventParameter(ev, kEventParamTabletPointRec, typeTabletPointRec, None, ctypes.sizeof(point_rec), None, ctypes.byref(point_rec)))
                x, y = self.window._get_mouse_position(ev)
                pressure = point_rec.pressure / float(65535)
                self.dispatch_event('on_motion', self._cursor, x, y, pressure, 0.0, 0.0)
            carbon.CallNextEventHandler(next_handler, ev)
            return noErr


class CarbonTabletCursor(TabletCursor):

    def __init__(self, cursor_type):
        if cursor_type == 1:
            name = 'Stylus'
        elif cursor_type == 3:
            name = 'Eraser'
        super(CarbonTabletCursor, self).__init__(name)


def get_tablets(display=None):
    return [_carbon_tablet]
# okay decompiling out\pyglet.input.carbon_tablet.pyc
