# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.canvas.carbon
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from pyglet import app
from base import Display, Screen, ScreenMode, Canvas
from ..pyglet.libs.darwin import *
from pyglet.libs.darwin import _oscheck

class CarbonDisplay(Display):

    def __init__(self):
        super(CarbonDisplay, self).__init__()
        import MacOS
        if not MacOS.WMAvailable():
            raise app.AppException('Window manager is not available.  Ensure you run "pythonw", not "python"')
        self._install_application_event_handlers()

    def get_screens(self):
        count = CGDisplayCount()
        carbon.CGGetActiveDisplayList(0, None, byref(count))
        displays = (CGDirectDisplayID * count.value)()
        carbon.CGGetActiveDisplayList(count.value, displays, byref(count))
        return [ CarbonScreen(self, id) for id in displays ]

    def _install_application_event_handlers(self):
        self._carbon_event_handlers = []
        self._carbon_event_handler_refs = []
        target = carbon.GetApplicationEventTarget()
        handlers = [
         (
          self._on_mouse_down, kEventClassMouse, kEventMouseDown),
         (
          self._on_apple_event, kEventClassAppleEvent, kEventAppleEvent),
         (
          self._on_command, kEventClassCommand, kEventProcessCommand)]
        ae_handlers = [
         (
          self._on_ae_quit, kCoreEventClass, kAEQuitApplication)]
        for method, cls, event in handlers:
            proc = EventHandlerProcPtr(method)
            self._carbon_event_handlers.append(proc)
            upp = carbon.NewEventHandlerUPP(proc)
            types = EventTypeSpec()
            types.eventClass = cls
            types.eventKind = event
            handler_ref = EventHandlerRef()
            carbon.InstallEventHandler(target, upp, 1, byref(types), c_void_p(), byref(handler_ref))
            self._carbon_event_handler_refs.append(handler_ref)

        for method, cls, event in ae_handlers:
            proc = EventHandlerProcPtr(method)
            self._carbon_event_handlers.append(proc)
            upp = carbon.NewAEEventHandlerUPP(proc)
            carbon.AEInstallEventHandler(cls, event, upp, 0, False)

    def _on_command(self, next_handler, ev, data):
        command = HICommand()
        carbon.GetEventParameter(ev, kEventParamDirectObject, typeHICommand, c_void_p(), sizeof(command), c_void_p(), byref(command))
        if command.commandID == kHICommandQuit:
            self._on_quit()
        return noErr

    def _on_mouse_down(self, next_handler, ev, data):
        position = Point()
        carbon.GetEventParameter(ev, kEventParamMouseLocation, typeQDPoint, c_void_p(), sizeof(position), c_void_p(), byref(position))
        if carbon.FindWindow(position, None) == inMenuBar:
            app.event_loop.enter_blocking()
            carbon.MenuSelect(position)
            app.event_loop.exit_blocking()
            carbon.HiliteMenu(0)
        carbon.CallNextEventHandler(next_handler, ev)
        return noErr

    def _on_apple_event(self, next_handler, ev, data):
        release = False
        if carbon.IsEventInQueue(carbon.GetMainEventQueue(), ev):
            carbon.RetainEvent(ev)
            release = True
            carbon.RemoveEventFromQueue(carbon.GetMainEventQueue(), ev)
        ev_record = EventRecord()
        carbon.ConvertEventRefToEventRecord(ev, byref(ev_record))
        carbon.AEProcessAppleEvent(byref(ev_record))
        if release:
            carbon.ReleaseEvent(ev)
        return noErr

    def _on_ae_quit(self, ae, reply, refcon):
        self._on_quit()
        return noErr

    def _on_quit(self):
        app.event_loop.exit()


class CarbonScreen(Screen):
    _initial_mode = None
    _captured = False

    def __init__(self, display, id):
        self.display = display
        rect = carbon.CGDisplayBounds(id)
        super(CarbonScreen, self).__init__(display, int(rect.origin.x), int(rect.origin.y), int(rect.size.width), int(rect.size.height))
        self.id = id
        mode = carbon.CGDisplayCurrentMode(id)
        kCGDisplayRefreshRate = create_cfstring('RefreshRate')
        number = carbon.CFDictionaryGetValue(mode, kCGDisplayRefreshRate)
        refresh = c_long()
        kCFNumberLongType = 10
        carbon.CFNumberGetValue(number, kCFNumberLongType, byref(refresh))
        self._refresh_rate = refresh.value

    def get_gdevice(self):
        gdevice = POINTER(None)()
        _oscheck(carbon.DMGetGDeviceByDisplayID(self.id, byref(gdevice), False))
        return gdevice

    def get_matching_configs(self, template):
        canvas = CarbonCanvas(self.display, self, None)
        configs = template.match(canvas)
        for config in configs:
            config.screen = self

        return configs

    def get_modes(self):
        modes_array = carbon.CGDisplayAvailableModes(self.id)
        n_modes_array = carbon.CFArrayGetCount(modes_array)
        modes = []
        for i in range(n_modes_array):
            mode = carbon.CFArrayGetValueAtIndex(modes_array, i)
            modes.append(CarbonScreenMode(self, mode))

        return modes

    def get_mode(self):
        mode = carbon.CGDisplayCurrentMode(self.id)
        return CarbonScreenMode(self, mode)

    def set_mode(self, mode):
        if mode is not None:
            if not self._initial_mode:
                self._initial_mode = self.get_mode()
        if not self._captured:
            _oscheck(carbon.CGDisplayCapture(self.id))
            self._captured = True
        if mode is not None:
            _oscheck(carbon.CGDisplaySwitchToMode(self.id, mode.mode))
            self.width = mode.width
            self.height = mode.height
        return

    def restore_mode(self):
        if self._initial_mode:
            _oscheck(carbon.CGDisplaySwitchToMode(self.id, self._initial_mode.mode))
            self._initial_mode = None
        if self._captured:
            _oscheck(carbon.CGDisplayRelease(self.id))
            self._captured = False
        return


class CarbonScreenMode(ScreenMode):

    def __init__(self, screen, mode):
        super(CarbonScreenMode, self).__init__(screen)
        self.mode = mode
        self.width = self._get_long('Width')
        self.height = self._get_long('Height')
        self.depth = self._get_long('BitsPerPixel')
        self.rate = self._get_long('RefreshRate')

    def _get_long(self, key):
        kCFNumberLongType = 10
        cfkey = create_cfstring(key)
        number = carbon.CFDictionaryGetValue(self.mode, cfkey)
        if not number:
            return None
        else:
            value = c_long()
            carbon.CFNumberGetValue(number, kCFNumberLongType, byref(value))
            return value.value


class CarbonCanvas(Canvas):
    bounds = None

    def __init__(self, display, screen, drawable):
        super(CarbonCanvas, self).__init__(display)
        self.screen = screen
        self.drawable = drawable


class CarbonFullScreenCanvas(Canvas):

    def __init__(self, display, screen, width, height):
        super(CarbonFullScreenCanvas, self).__init__(display)
        self.screen = screen
        self.width = width
        self.height = height
# okay decompiling out\pyglet.canvas.carbon.pyc
