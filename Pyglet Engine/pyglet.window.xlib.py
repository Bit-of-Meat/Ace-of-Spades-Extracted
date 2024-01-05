# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.window.xlib
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
import unicodedata, warnings, pyglet
from pyglet.window import WindowException, NoSuchDisplayException, MouseCursorException, MouseCursor, DefaultMouseCursor, ImageMouseCursor, BaseWindow, _PlatformEventHandler, _ViewEventHandler
from pyglet.window import key
from pyglet.window import mouse
from pyglet.event import EventDispatcher
from pyglet.canvas.xlib import XlibCanvas
from pyglet.libs.x11 import xlib
from pyglet.libs.x11 import cursorfont
from pyglet.compat import asbytes
try:
    from pyglet.libs.x11 import xsync
    _have_xsync = True
except:
    _have_xsync = False

class mwmhints_t(Structure):
    _fields_ = [
     (
      'flags', c_uint32),
     (
      'functions', c_uint32),
     (
      'decorations', c_uint32),
     (
      'input_mode', c_int32),
     (
      'status', c_uint32)]


XA_CARDINAL = 6
_have_utf8 = hasattr(xlib._lib, 'Xutf8TextListToTextProperty')
_motion_map = {(key.UP, False): key.MOTION_UP, 
   (key.RIGHT, False): key.MOTION_RIGHT, 
   (key.DOWN, False): key.MOTION_DOWN, 
   (key.LEFT, False): key.MOTION_LEFT, 
   (key.RIGHT, True): key.MOTION_NEXT_WORD, 
   (key.LEFT, True): key.MOTION_PREVIOUS_WORD, 
   (key.HOME, False): key.MOTION_BEGINNING_OF_LINE, 
   (key.END, False): key.MOTION_END_OF_LINE, 
   (key.PAGEUP, False): key.MOTION_PREVIOUS_PAGE, 
   (key.PAGEDOWN, False): key.MOTION_NEXT_PAGE, 
   (key.HOME, True): key.MOTION_BEGINNING_OF_FILE, 
   (key.END, True): key.MOTION_END_OF_FILE, 
   (key.BACKSPACE, False): key.MOTION_BACKSPACE, 
   (key.DELETE, False): key.MOTION_DELETE}

class XlibException(WindowException):
    pass


class XlibMouseCursor(MouseCursor):
    drawable = False

    def __init__(self, cursor):
        self.cursor = cursor


XlibEventHandler = _PlatformEventHandler
ViewEventHandler = _ViewEventHandler

class XlibWindow(BaseWindow):
    _x_display = None
    _x_screen_id = None
    _x_ic = None
    _window = None
    _minimum_size = None
    _maximum_size = None
    _override_redirect = False
    _x = 0
    _y = 0
    _width = 0
    _height = 0
    _mouse_exclusive_client = None
    _mouse_buttons = [False] * 6
    _keyboard_exclusive = False
    _active = True
    _applied_mouse_exclusive = False
    _applied_keyboard_exclusive = False
    _mapped = False
    _lost_context = False
    _lost_context_state = False
    _enable_xsync = False
    _current_sync_value = None
    _current_sync_valid = False
    _needs_resize = False
    _default_event_mask = 33554431 & ~xlib.PointerMotionHintMask & ~xlib.ResizeRedirectMask & ~xlib.SubstructureNotifyMask

    def __init__(self, *args, **kwargs):
        self._event_handlers = {}
        self._view_event_handlers = {}
        for name in self._platform_event_names:
            if not hasattr(self, name):
                continue
            func = getattr(self, name)
            for message in func._platform_event_data:
                if hasattr(func, '_view'):
                    self._view_event_handlers[message] = func
                else:
                    self._event_handlers[message] = func

        super(XlibWindow, self).__init__(*args, **kwargs)

    def _recreate(self, changes):
        if 'fullscreen' in changes or 'resizable' in changes:
            self.context.detach()
            xlib.XDestroyWindow(self._x_display, self._window)
            del self.display._window_map[self._window]
            del self.display._window_map[self._view]
            self._window = None
            self._mapped = False
        if 'context' in changes:
            self._lost_context = True
            self._lost_context_state = True
        self._create()
        return

    def _create(self):
        if self._window and self._mapped:
            self._unmap()
        self._x_display = self.display._display
        self._x_screen_id = self.display.x_screen
        if not self._window:
            root = xlib.XRootWindow(self._x_display, self._x_screen_id)
            visual_info = self.config.get_visual_info()
            visual = visual_info.visual
            visual_id = xlib.XVisualIDFromVisual(visual)
            default_visual = xlib.XDefaultVisual(self._x_display, self._x_screen_id)
            default_visual_id = xlib.XVisualIDFromVisual(default_visual)
            window_attributes = xlib.XSetWindowAttributes()
            if visual_id != default_visual_id:
                window_attributes.colormap = xlib.XCreateColormap(self._x_display, root, visual, xlib.AllocNone)
            else:
                window_attributes.colormap = xlib.XDefaultColormap(self._x_display, self._x_screen_id)
            window_attributes.bit_gravity = xlib.StaticGravity
            mask = xlib.CWColormap | xlib.CWBitGravity | xlib.CWBackPixel
            if self._fullscreen:
                width, height = self.screen.width, self.screen.height
                self._view_x = (width - self._width) // 2
                self._view_y = (height - self._height) // 2
            else:
                width, height = self._width, self._height
                self._view_x = self._view_y = 0
            self._window = xlib.XCreateWindow(self._x_display, root, 0, 0, width, height, 0, visual_info.depth, xlib.InputOutput, visual, mask, byref(window_attributes))
            self._view = xlib.XCreateWindow(self._x_display, self._window, self._view_x, self._view_y, self._width, self._height, 0, visual_info.depth, xlib.InputOutput, visual, mask, byref(window_attributes))
            xlib.XMapWindow(self._x_display, self._view)
            xlib.XSelectInput(self._x_display, self._view, self._default_event_mask)
            self.display._window_map[self._window] = self.dispatch_platform_event
            self.display._window_map[self._view] = self.dispatch_platform_event_view
            self.canvas = XlibCanvas(self.display, self._view)
            self.context.attach(self.canvas)
            self.context.set_vsync(self._vsync)
            self._enable_xsync = pyglet.options['xsync'] and self.display._enable_xsync and self.config.double_buffer
            protocols = []
            protocols.append(xlib.XInternAtom(self._x_display, asbytes('WM_DELETE_WINDOW'), False))
            if self._enable_xsync:
                protocols.append(xlib.XInternAtom(self._x_display, asbytes('_NET_WM_SYNC_REQUEST'), False))
            protocols = (c_ulong * len(protocols))(*protocols)
            xlib.XSetWMProtocols(self._x_display, self._window, protocols, len(protocols))
            if self._enable_xsync:
                value = xsync.XSyncValue()
                self._sync_counter = xlib.XID(xsync.XSyncCreateCounter(self._x_display, value))
                atom = xlib.XInternAtom(self._x_display, asbytes('_NET_WM_SYNC_REQUEST_COUNTER'), False)
                ptr = pointer(self._sync_counter)
                xlib.XChangeProperty(self._x_display, self._window, atom, XA_CARDINAL, 32, xlib.PropModeReplace, cast(ptr, POINTER(c_ubyte)), 1)
        attributes = xlib.XSetWindowAttributes()
        attributes_mask = 0
        self._override_redirect = False
        if self._fullscreen:
            if pyglet.options['xlib_fullscreen_override_redirect']:
                attributes.override_redirect = self._fullscreen
                attributes_mask |= xlib.CWOverrideRedirect
                self._override_redirect = True
            else:
                self._set_wm_state('_NET_WM_STATE_FULLSCREEN')
        if self._fullscreen:
            xlib.XMoveResizeWindow(self._x_display, self._window, self.screen.x, self.screen.y, self.screen.width, self.screen.height)
        else:
            xlib.XResizeWindow(self._x_display, self._window, self._width, self._height)
        xlib.XChangeWindowAttributes(self._x_display, self._window, attributes_mask, byref(attributes))
        styles = {self.WINDOW_STYLE_DEFAULT: '_NET_WM_WINDOW_TYPE_NORMAL', 
           self.WINDOW_STYLE_DIALOG: '_NET_WM_WINDOW_TYPE_DIALOG', 
           self.WINDOW_STYLE_TOOL: '_NET_WM_WINDOW_TYPE_UTILITY'}
        if self._style in styles:
            self._set_atoms_property('_NET_WM_WINDOW_TYPE', (
             styles[self._style],))
        elif self._style == self.WINDOW_STYLE_BORDERLESS:
            MWM_HINTS_DECORATIONS = 2
            PROP_MWM_HINTS_ELEMENTS = 5
            mwmhints = mwmhints_t()
            mwmhints.flags = MWM_HINTS_DECORATIONS
            mwmhints.decorations = 0
            name = xlib.XInternAtom(self._x_display, '_MOTIF_WM_HINTS', False)
            xlib.XChangeProperty(self._x_display, self._window, name, name, 32, xlib.PropModeReplace, cast(pointer(mwmhints), POINTER(c_ubyte)), PROP_MWM_HINTS_ELEMENTS)
        if not self._resizable and not self._fullscreen:
            self.set_minimum_size(self._width, self._height)
            self.set_maximum_size(self._width, self._height)
        self.set_caption(self._caption)
        if _have_utf8 and not self._x_ic:
            if not self.display._x_im:
                xlib.XSetLocaleModifiers(asbytes('@im=none'))
                self.display._x_im = xlib.XOpenIM(self._x_display, None, None, None)
            xlib.XFlush(self._x_display)
            xlib.XCreateIC.argtypes = [
             xlib.XIM,
             c_char_p, c_int,
             c_char_p, xlib.Window,
             c_char_p, xlib.Window,
             c_void_p]
            self._x_ic = xlib.XCreateIC(self.display._x_im, asbytes('inputStyle'), xlib.XIMPreeditNothing | xlib.XIMStatusNothing, asbytes('clientWindow'), self._window, asbytes('focusWindow'), self._window, None)
            filter_events = c_ulong()
            xlib.XGetICValues(self._x_ic, 'filterEvents', byref(filter_events), None)
            self._default_event_mask |= filter_events.value
            xlib.XSetICFocus(self._x_ic)
        self.switch_to()
        if self._visible:
            self.set_visible(True)
        self.set_mouse_platform_visible()
        self._applied_mouse_exclusive = None
        self._update_exclusivity()
        return

    def _map(self):
        if self._mapped:
            return
        xlib.XSelectInput(self._x_display, self._window, xlib.StructureNotifyMask)
        xlib.XMapRaised(self._x_display, self._window)
        e = xlib.XEvent()
        while True:
            xlib.XNextEvent(self._x_display, e)
            if e.type == xlib.MapNotify:
                break

        xlib.XSelectInput(self._x_display, self._window, self._default_event_mask)
        self._mapped = True
        if self._override_redirect:
            self.activate()
        self.dispatch_event('on_resize', self._width, self._height)
        self.dispatch_event('on_show')
        self.dispatch_event('on_expose')

    def _unmap(self):
        if not self._mapped:
            return
        xlib.XSelectInput(self._x_display, self._window, xlib.StructureNotifyMask)
        xlib.XUnmapWindow(self._x_display, self._window)
        e = xlib.XEvent()
        while True:
            xlib.XNextEvent(self._x_display, e)
            if e.type == xlib.UnmapNotify:
                break

        xlib.XSelectInput(self._x_display, self._window, self._default_event_mask)
        self._mapped = False

    def _get_root(self):
        attributes = xlib.XWindowAttributes()
        xlib.XGetWindowAttributes(self._x_display, self._window, byref(attributes))
        return attributes.root

    def close(self):
        if not self._window:
            return
        else:
            self.context.destroy()
            self._unmap()
            if self._window:
                xlib.XDestroyWindow(self._x_display, self._window)
            del self.display._window_map[self._window]
            self._window = None
            if _have_utf8:
                xlib.XDestroyIC(self._x_ic)
                self._x_ic = None
            super(XlibWindow, self).close()
            return

    def switch_to(self):
        if self.context:
            self.context.set_current()

    def flip(self):
        self.draw_mouse_cursor()
        if self.context:
            self.context.flip()
        self._sync_resize()

    def set_vsync(self, vsync):
        if pyglet.options['vsync'] is not None:
            vsync = pyglet.options['vsync']
        self._vsync = vsync
        self.context.set_vsync(vsync)
        return

    def set_caption(self, caption):
        if caption is None:
            caption = ''
        self._caption = caption
        self._set_text_property('WM_NAME', caption, allow_utf8=False)
        self._set_text_property('WM_ICON_NAME', caption, allow_utf8=False)
        self._set_text_property('_NET_WM_NAME', caption)
        self._set_text_property('_NET_WM_ICON_NAME', caption)
        return

    def get_caption(self):
        return self._caption

    def set_size(self, width, height):
        if self._fullscreen:
            raise WindowException('Cannot set size of fullscreen window.')
        self._width = width
        self._height = height
        if not self._resizable:
            self.set_minimum_size(width, height)
            self.set_maximum_size(width, height)
        xlib.XResizeWindow(self._x_display, self._window, width, height)
        self._update_view_size()
        self.dispatch_event('on_resize', width, height)

    def _update_view_size(self):
        xlib.XResizeWindow(self._x_display, self._view, self._width, self._height)

    def get_size(self):
        return (
         self._width, self._height)

    def set_location(self, x, y):
        attributes = xlib.XWindowAttributes()
        xlib.XGetWindowAttributes(self._x_display, self._window, byref(attributes))
        x -= attributes.x
        y -= attributes.y
        xlib.XMoveWindow(self._x_display, self._window, x, y)

    def get_location(self):
        child = xlib.Window()
        x = c_int()
        y = c_int()
        xlib.XTranslateCoordinates(self._x_display, self._window, self._get_root(), 0, 0, byref(x), byref(y), byref(child))
        return (x.value, y.value)

    def activate(self):
        xlib.XSetInputFocus(self._x_display, self._window, xlib.RevertToParent, xlib.CurrentTime)

    def set_visible(self, visible=True):
        if visible:
            self._map()
        else:
            self._unmap()
        self._visible = visible

    def set_minimum_size(self, width, height):
        self._minimum_size = (
         width, height)
        self._set_wm_normal_hints()

    def set_maximum_size(self, width, height):
        self._maximum_size = (
         width, height)
        self._set_wm_normal_hints()

    def minimize(self):
        xlib.XIconifyWindow(self._x_display, self._window, self._x_screen_id)

    def maximize(self):
        self._set_wm_state('_NET_WM_STATE_MAXIMIZED_HORZ', '_NET_WM_STATE_MAXIMIZED_VERT')

    def set_mouse_platform_visible(self, platform_visible=None):
        if platform_visible is None:
            platform_visible = self._mouse_visible and not self._mouse_cursor.drawable
        if not platform_visible:
            black = xlib.XBlackPixel(self._x_display, self._x_screen_id)
            black = xlib.XColor()
            bmp = xlib.XCreateBitmapFromData(self._x_display, self._window, c_buffer(8), 8, 8)
            cursor = xlib.XCreatePixmapCursor(self._x_display, bmp, bmp, black, black, 0, 0)
            xlib.XDefineCursor(self._x_display, self._window, cursor)
            xlib.XFreeCursor(self._x_display, cursor)
            xlib.XFreePixmap(self._x_display, bmp)
        elif isinstance(self._mouse_cursor, XlibMouseCursor):
            xlib.XDefineCursor(self._x_display, self._window, self._mouse_cursor.cursor)
        else:
            xlib.XUndefineCursor(self._x_display, self._window)
        return

    def set_mouse_position(self, x, y):
        xlib.XWarpPointer(self._x_display, 0, self._window, 0, 0, 0, 0, x, self._height - y)

    def _update_exclusivity(self):
        mouse_exclusive = self._active and self._mouse_exclusive
        keyboard_exclusive = self._active and self._keyboard_exclusive
        if mouse_exclusive != self._applied_mouse_exclusive:
            if mouse_exclusive:
                self.set_mouse_platform_visible(False)
                xlib.XGrabPointer(self._x_display, self._window, True, 0, xlib.GrabModeAsync, xlib.GrabModeAsync, self._window, 0, xlib.CurrentTime)
                x = self._width / 2
                y = self._height / 2
                self._mouse_exclusive_client = (x, y)
                self.set_mouse_position(x, y)
            elif self._fullscreen and not self.screen._xinerama:
                self.set_mouse_position(0, 0)
                r = xlib.XGrabPointer(self._x_display, self._view, True, 0, xlib.GrabModeAsync, xlib.GrabModeAsync, self._view, 0, xlib.CurrentTime)
                if r:
                    self._applied_mouse_exclusive = None
                    return
                self.set_mouse_platform_visible()
            else:
                xlib.XUngrabPointer(self._x_display, xlib.CurrentTime)
                self.set_mouse_platform_visible()
            self._applied_mouse_exclusive = mouse_exclusive
        if keyboard_exclusive != self._applied_keyboard_exclusive:
            if keyboard_exclusive:
                xlib.XGrabKeyboard(self._x_display, self._window, False, xlib.GrabModeAsync, xlib.GrabModeAsync, xlib.CurrentTime)
            else:
                xlib.XUngrabKeyboard(self._x_display, xlib.CurrentTime)
            self._applied_keyboard_exclusive = keyboard_exclusive
        return

    def set_exclusive_mouse(self, exclusive=True):
        if exclusive == self._mouse_exclusive:
            return
        self._mouse_exclusive = exclusive
        self._update_exclusivity()

    def set_exclusive_keyboard(self, exclusive=True):
        if exclusive == self._keyboard_exclusive:
            return
        self._keyboard_exclusive = exclusive
        self._update_exclusivity()

    def get_system_mouse_cursor(self, name):
        if name == self.CURSOR_DEFAULT:
            return DefaultMouseCursor()
        cursor_shapes = {self.CURSOR_CROSSHAIR: cursorfont.XC_crosshair, 
           self.CURSOR_HAND: cursorfont.XC_hand2, 
           self.CURSOR_HELP: cursorfont.XC_question_arrow, 
           self.CURSOR_NO: cursorfont.XC_pirate, 
           self.CURSOR_SIZE: cursorfont.XC_fleur, 
           self.CURSOR_SIZE_UP: cursorfont.XC_top_side, 
           self.CURSOR_SIZE_UP_RIGHT: cursorfont.XC_top_right_corner, 
           self.CURSOR_SIZE_RIGHT: cursorfont.XC_right_side, 
           self.CURSOR_SIZE_DOWN_RIGHT: cursorfont.XC_bottom_right_corner, 
           self.CURSOR_SIZE_DOWN: cursorfont.XC_bottom_side, 
           self.CURSOR_SIZE_DOWN_LEFT: cursorfont.XC_bottom_left_corner, 
           self.CURSOR_SIZE_LEFT: cursorfont.XC_left_side, 
           self.CURSOR_SIZE_UP_LEFT: cursorfont.XC_top_left_corner, 
           self.CURSOR_SIZE_UP_DOWN: cursorfont.XC_sb_v_double_arrow, 
           self.CURSOR_SIZE_LEFT_RIGHT: cursorfont.XC_sb_h_double_arrow, 
           self.CURSOR_TEXT: cursorfont.XC_xterm, 
           self.CURSOR_WAIT: cursorfont.XC_watch, 
           self.CURSOR_WAIT_ARROW: cursorfont.XC_watch}
        if name not in cursor_shapes:
            raise MouseCursorException('Unknown cursor name "%s"' % name)
        cursor = xlib.XCreateFontCursor(self._x_display, cursor_shapes[name])
        return XlibMouseCursor(cursor)

    def set_icon(self, *images):
        import sys
        format = {('little', 4): 'BGRA', 
           ('little', 8): 'BGRAAAAA', 
           ('big', 4): 'ARGB', 
           ('big', 8): 'AAAAARGB'}[(
         sys.byteorder, sizeof(c_ulong))]
        data = ''
        for image in images:
            image = image.get_image_data()
            pitch = -(image.width * len(format))
            s = c_buffer(sizeof(c_ulong) * 2)
            memmove(s, cast((c_ulong * 2)(image.width, image.height), POINTER(c_ubyte)), len(s))
            data += s.raw + image.get_data(format, pitch)

        buffer = (c_ubyte * len(data))()
        memmove(buffer, data, len(data))
        atom = xlib.XInternAtom(self._x_display, '_NET_WM_ICON', False)
        xlib.XChangeProperty(self._x_display, self._window, atom, XA_CARDINAL, 32, xlib.PropModeReplace, buffer, len(data) / sizeof(c_ulong))

    def _set_wm_normal_hints(self):
        hints = xlib.XAllocSizeHints().contents
        if self._minimum_size:
            hints.flags |= xlib.PMinSize
            hints.min_width, hints.min_height = self._minimum_size
        if self._maximum_size:
            hints.flags |= xlib.PMaxSize
            hints.max_width, hints.max_height = self._maximum_size
        xlib.XSetWMNormalHints(self._x_display, self._window, byref(hints))

    def _set_text_property(self, name, value, allow_utf8=True):
        atom = xlib.XInternAtom(self._x_display, asbytes(name), False)
        if not atom:
            raise XlibException('Undefined atom "%s"' % name)
        property = xlib.XTextProperty()
        if _have_utf8 and allow_utf8:
            buf = create_string_buffer(value.encode('utf8'))
            result = xlib.Xutf8TextListToTextProperty(self._x_display, cast(pointer(buf), c_char_p), 1, xlib.XUTF8StringStyle, byref(property))
            if result < 0:
                raise XlibException('Could not create UTF8 text property')
        else:
            buf = create_string_buffer(value.encode('ascii', 'ignore'))
            result = xlib.XStringListToTextProperty(cast(pointer(buf), c_char_p), 1, byref(property))
            if result < 0:
                raise XlibException('Could not create text property')
        xlib.XSetTextProperty(self._x_display, self._window, byref(property), atom)

    def _set_atoms_property(self, name, values, mode=xlib.PropModeReplace):
        name_atom = xlib.XInternAtom(self._x_display, asbytes(name), False)
        atoms = []
        for value in values:
            atoms.append(xlib.XInternAtom(self._x_display, asbytes(value), False))

        atom_type = xlib.XInternAtom(self._x_display, asbytes('ATOM'), False)
        if len(atoms):
            atoms_ar = (xlib.Atom * len(atoms))(*atoms)
            xlib.XChangeProperty(self._x_display, self._window, name_atom, atom_type, 32, mode, cast(pointer(atoms_ar), POINTER(c_ubyte)), len(atoms))
        else:
            xlib.XDeleteProperty(self._x_display, self._window, net_wm_state)

    def _set_wm_state(self, *states):
        net_wm_state = xlib.XInternAtom(self._x_display, '_NET_WM_STATE', False)
        atoms = []
        for state in states:
            atoms.append(xlib.XInternAtom(self._x_display, state, False))

        atom_type = xlib.XInternAtom(self._x_display, 'ATOM', False)
        if len(atoms):
            atoms_ar = (xlib.Atom * len(atoms))(*atoms)
            xlib.XChangeProperty(self._x_display, self._window, net_wm_state, atom_type, 32, xlib.PropModePrepend, cast(pointer(atoms_ar), POINTER(c_ubyte)), len(atoms))
        else:
            xlib.XDeleteProperty(self._x_display, self._window, net_wm_state)
        e = xlib.XEvent()
        e.xclient.type = xlib.ClientMessage
        e.xclient.message_type = net_wm_state
        e.xclient.display = cast(self._x_display, POINTER(xlib.Display))
        e.xclient.window = self._window
        e.xclient.format = 32
        e.xclient.data.l[0] = xlib.PropModePrepend
        for i, atom in enumerate(atoms):
            e.xclient.data.l[i + 1] = atom

        xlib.XSendEvent(self._x_display, self._get_root(), False, xlib.SubstructureRedirectMask, byref(e))

    def dispatch_events(self):
        self.dispatch_pending_events()
        self._allow_dispatch_event = True
        e = xlib.XEvent()
        _x_display = self._x_display
        _window = self._window
        _view = self._view
        while xlib.XCheckWindowEvent(_x_display, _window, 33554431, byref(e)):
            if e.xany.type not in (xlib.KeyPress, xlib.KeyRelease):
                if xlib.XFilterEvent(e, 0):
                    continue
            self.dispatch_platform_event(e)

        while xlib.XCheckWindowEvent(_x_display, _view, 33554431, byref(e)):
            if e.xany.type not in (xlib.KeyPress, xlib.KeyRelease):
                if xlib.XFilterEvent(e, 0):
                    continue
            self.dispatch_platform_event_view(e)

        while xlib.XCheckTypedWindowEvent(_x_display, _window, xlib.ClientMessage, byref(e)):
            self.dispatch_platform_event(e)

        if self._needs_resize:
            self.dispatch_event('on_resize', self._width, self._height)
            self.dispatch_event('on_expose')
            self._needs_resize = False
        self._allow_dispatch_event = False

    def dispatch_pending_events(self):
        while self._event_queue:
            EventDispatcher.dispatch_event(self, *self._event_queue.pop(0))

        if self._lost_context:
            self._lost_context = False
            EventDispatcher.dispatch_event(self, 'on_context_lost')
        if self._lost_context_state:
            self._lost_context_state = False
            EventDispatcher.dispatch_event(self, 'on_context_state_lost')

    def dispatch_platform_event(self, e):
        if self._applied_mouse_exclusive is None:
            self._update_exclusivity()
        event_handler = self._event_handlers.get(e.type)
        if event_handler:
            event_handler(e)
        return

    def dispatch_platform_event_view(self, e):
        event_handler = self._view_event_handlers.get(e.type)
        if event_handler:
            event_handler(e)

    @staticmethod
    def _translate_modifiers(state):
        modifiers = 0
        if state & xlib.ShiftMask:
            modifiers |= key.MOD_SHIFT
        if state & xlib.ControlMask:
            modifiers |= key.MOD_CTRL
        if state & xlib.LockMask:
            modifiers |= key.MOD_CAPSLOCK
        if state & xlib.Mod1Mask:
            modifiers |= key.MOD_ALT
        if state & xlib.Mod2Mask:
            modifiers |= key.MOD_NUMLOCK
        if state & xlib.Mod4Mask:
            modifiers |= key.MOD_WINDOWS
        if state & xlib.Mod5Mask:
            modifiers |= key.MOD_SCROLLLOCK
        return modifiers

    def _event_text_symbol(self, ev):
        text = None
        symbol = xlib.KeySym()
        buffer = create_string_buffer(128)
        count = xlib.XLookupString(ev.xkey, buffer, len(buffer) - 1, byref(symbol), None)
        filtered = xlib.XFilterEvent(ev, ev.xany.window)
        if ev.type == xlib.KeyPress and not filtered:
            status = c_int()
            if _have_utf8:
                encoding = 'utf8'
                count = xlib.Xutf8LookupString(self._x_ic, ev.xkey, buffer, len(buffer) - 1, byref(symbol), byref(status))
                if status.value == xlib.XBufferOverflow:
                    raise NotImplementedError('TODO: XIM buffer resize')
            else:
                encoding = 'ascii'
                count = xlib.XLookupString(ev.xkey, buffer, len(buffer) - 1, byref(symbol), None)
                if count:
                    status.value = xlib.XLookupBoth
            if status.value & (xlib.XLookupChars | xlib.XLookupBoth):
                text = buffer.value[:count].decode(encoding)
            if text and unicodedata.category(text) == 'Cc' and text != '\r':
                text = None
        symbol = symbol.value
        if ev.xkey.keycode == 0 and not filtered:
            symbol = None
        if symbol and symbol not in key._key_names and ev.xkey.keycode:
            symbol = ord(unichr(symbol).lower())
            if symbol not in key._key_names:
                symbol = key.user_key(ev.xkey.keycode)
        if symbol in (key.LSHIFT_REAL, key.RSHIFT_REAL):
            symbol = key.LSHIFT
        elif symbol in (key.LCTRL_REAL, key.RCTRL_REAL):
            symbol = key.LCTRL
        if filtered:
            return (
             None, symbol)
        else:
            return (
             text, symbol)

    def _event_text_motion(self, symbol, modifiers):
        if modifiers & key.MOD_ALT:
            return
        else:
            ctrl = modifiers & key.MOD_CTRL != 0
            return _motion_map.get((symbol, ctrl), None)

    @ViewEventHandler
    @XlibEventHandler(xlib.KeyPress)
    @XlibEventHandler(xlib.KeyRelease)
    def _event_key_view(self, ev):
        if ev.type == xlib.KeyRelease:
            saved = []
            while True:
                auto_event = xlib.XEvent()
                result = xlib.XCheckWindowEvent(self._x_display, self._window, xlib.KeyPress | xlib.KeyRelease, byref(auto_event))
                if not result:
                    break
                saved.append(auto_event)
                if auto_event.type == xlib.KeyRelease:
                    continue
                if ev.xkey.keycode == auto_event.xkey.keycode:
                    text, symbol = self._event_text_symbol(auto_event)
                    modifiers = self._translate_modifiers(ev.xkey.state)
                    modifiers_ctrl = modifiers & (key.MOD_CTRL | key.MOD_ALT)
                    motion = self._event_text_motion(symbol, modifiers)
                    if motion:
                        if modifiers & key.MOD_SHIFT:
                            self.dispatch_event('on_text_motion_select', motion)
                        else:
                            self.dispatch_event('on_text_motion', motion)
                    elif text and not modifiers_ctrl:
                        self.dispatch_event('on_text', text)
                    ditched = saved.pop()
                    for auto_event in reversed(saved):
                        xlib.XPutBackEvent(self._x_display, byref(auto_event))

                    return
                break

            for auto_event in reversed(saved):
                xlib.XPutBackEvent(self._x_display, byref(auto_event))

        text, symbol = self._event_text_symbol(ev)
        modifiers = self._translate_modifiers(ev.xkey.state)
        modifiers_ctrl = modifiers & (key.MOD_CTRL | key.MOD_ALT)
        motion = self._event_text_motion(symbol, modifiers)
        if ev.type == xlib.KeyPress:
            if symbol:
                self.dispatch_event('on_key_press', symbol, modifiers)
            if motion:
                if modifiers & key.MOD_SHIFT:
                    self.dispatch_event('on_text_motion_select', motion)
                else:
                    self.dispatch_event('on_text_motion', motion)
            elif text and not modifiers_ctrl:
                self.dispatch_event('on_text', text)
        elif ev.type == xlib.KeyRelease:
            if symbol:
                self.dispatch_event('on_key_release', symbol, modifiers)

    @XlibEventHandler(xlib.KeyPress)
    @XlibEventHandler(xlib.KeyRelease)
    def _event_key(self, ev):
        return self._event_key_view(ev)

    @ViewEventHandler
    @XlibEventHandler(xlib.MotionNotify)
    def _event_motionnotify_view(self, ev):
        x = ev.xmotion.x
        y = self.height - ev.xmotion.y
        if self._mouse_in_window:
            dx = x - self._mouse_x
            dy = y - self._mouse_y
        else:
            dx = dy = 0
        if self._applied_mouse_exclusive and (
         ev.xmotion.x, ev.xmotion.y) == self._mouse_exclusive_client:
            self._mouse_x = x
            self._mouse_y = y
            return
        if self._applied_mouse_exclusive:
            ex, ey = self._mouse_exclusive_client
            xlib.XWarpPointer(self._x_display, 0, self._window, 0, 0, 0, 0, ex, ey)
        self._mouse_x = x
        self._mouse_y = y
        self._mouse_in_window = True
        buttons = 0
        if ev.xmotion.state & xlib.Button1MotionMask:
            buttons |= mouse.LEFT
        if ev.xmotion.state & xlib.Button2MotionMask:
            buttons |= mouse.MIDDLE
        if ev.xmotion.state & xlib.Button3MotionMask:
            buttons |= mouse.RIGHT
        if buttons:
            modifiers = self._translate_modifiers(ev.xmotion.state)
            self.dispatch_event('on_mouse_drag', x, y, dx, dy, buttons, modifiers)
        else:
            self.dispatch_event('on_mouse_motion', x, y, dx, dy)

    @XlibEventHandler(xlib.MotionNotify)
    def _event_motionnotify(self, ev):
        buttons = 0
        if ev.xmotion.state & xlib.Button1MotionMask:
            buttons |= mouse.LEFT
        if ev.xmotion.state & xlib.Button2MotionMask:
            buttons |= mouse.MIDDLE
        if ev.xmotion.state & xlib.Button3MotionMask:
            buttons |= mouse.RIGHT
        if buttons:
            x = ev.xmotion.x - self._view_x
            y = self._height - (ev.xmotion.y - self._view_y)
            if self._mouse_in_window:
                dx = x - self._mouse_x
                dy = y - self._mouse_y
            else:
                dx = dy = 0
            self._mouse_x = x
            self._mouse_y = y
            modifiers = self._translate_modifiers(ev.xmotion.state)
            self.dispatch_event('on_mouse_drag', x, y, dx, dy, buttons, modifiers)

    @XlibEventHandler(xlib.ClientMessage)
    def _event_clientmessage(self, ev):
        atom = ev.xclient.data.l[0]
        if atom == xlib.XInternAtom(ev.xclient.display, asbytes('WM_DELETE_WINDOW'), False):
            self.dispatch_event('on_close')
        elif self._enable_xsync and atom == xlib.XInternAtom(ev.xclient.display, asbytes('_NET_WM_SYNC_REQUEST'), False):
            lo = ev.xclient.data.l[2]
            hi = ev.xclient.data.l[3]
            self._current_sync_value = xsync.XSyncValue(hi, lo)

    def _sync_resize(self):
        if self._enable_xsync and self._current_sync_valid:
            if xsync.XSyncValueIsZero(self._current_sync_value):
                self._current_sync_valid = False
                return
            xsync.XSyncSetCounter(self._x_display, self._sync_counter, self._current_sync_value)
            self._current_sync_value = None
            self._current_sync_valid = False
        return

    @ViewEventHandler
    @XlibEventHandler(xlib.ButtonPress)
    @XlibEventHandler(xlib.ButtonRelease)
    def _event_button(self, ev):
        x = ev.xbutton.x
        y = self.height - ev.xbutton.y
        button = 1 << ev.xbutton.button - 1
        modifiers = self._translate_modifiers(ev.xbutton.state)
        if ev.type == xlib.ButtonPress:
            if self._override_redirect and not self._active:
                self.activate()
            if ev.xbutton.button == 4:
                self.dispatch_event('on_mouse_scroll', x, y, 0, 1)
            else:
                if ev.xbutton.button == 5:
                    self.dispatch_event('on_mouse_scroll', x, y, 0, -1)
                elif ev.xbutton.button < len(self._mouse_buttons):
                    self._mouse_buttons[ev.xbutton.button] = True
                    self.dispatch_event('on_mouse_press', x, y, button, modifiers)
        elif ev.xbutton.button < 4:
            self._mouse_buttons[ev.xbutton.button] = False
            self.dispatch_event('on_mouse_release', x, y, button, modifiers)

    @ViewEventHandler
    @XlibEventHandler(xlib.Expose)
    def _event_expose(self, ev):
        if ev.xexpose.count > 0:
            return
        self.dispatch_event('on_expose')

    @ViewEventHandler
    @XlibEventHandler(xlib.EnterNotify)
    def _event_enternotify(self, ev):
        state = ev.xcrossing.state
        self._mouse_buttons[1] = state & xlib.Button1Mask
        self._mouse_buttons[2] = state & xlib.Button2Mask
        self._mouse_buttons[3] = state & xlib.Button3Mask
        self._mouse_buttons[4] = state & xlib.Button4Mask
        self._mouse_buttons[5] = state & xlib.Button5Mask
        x = self._mouse_x = ev.xcrossing.x
        y = self._mouse_y = self.height - ev.xcrossing.y
        self._mouse_in_window = True
        self.dispatch_event('on_mouse_enter', x, y)

    @ViewEventHandler
    @XlibEventHandler(xlib.LeaveNotify)
    def _event_leavenotify(self, ev):
        x = self._mouse_x = ev.xcrossing.x
        y = self._mouse_y = self.height - ev.xcrossing.y
        self._mouse_in_window = False
        self.dispatch_event('on_mouse_leave', x, y)

    @XlibEventHandler(xlib.ConfigureNotify)
    def _event_configurenotify(self, ev):
        if self._enable_xsync and self._current_sync_value:
            self._current_sync_valid = True
        if self._fullscreen:
            return
        self.switch_to()
        w, h = ev.xconfigure.width, ev.xconfigure.height
        x, y = ev.xconfigure.x, ev.xconfigure.y
        if self._width != w or self._height != h:
            self._width = w
            self._height = h
            self._needs_resize = True
            self._update_view_size()
        if self._x != x or self._y != y:
            self.dispatch_event('on_move', x, y)
            self._x = x
            self._y = y

    @XlibEventHandler(xlib.FocusIn)
    def _event_focusin(self, ev):
        self._active = True
        self._update_exclusivity()
        self.dispatch_event('on_activate')
        xlib.XSetICFocus(self._x_ic)

    @XlibEventHandler(xlib.FocusOut)
    def _event_focusout(self, ev):
        self._active = False
        self._update_exclusivity()
        self.dispatch_event('on_deactivate')
        xlib.XUnsetICFocus(self._x_ic)

    @XlibEventHandler(xlib.MapNotify)
    def _event_mapnotify(self, ev):
        self._mapped = True
        self.dispatch_event('on_show')
        self._update_exclusivity()

    @XlibEventHandler(xlib.UnmapNotify)
    def _event_unmapnotify(self, ev):
        self._mapped = False
        self.dispatch_event('on_hide')
# okay decompiling out\pyglet.window.xlib.pyc
