# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.window
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import pprint, sys, pyglet
from pyglet import gl
from pyglet.gl import gl_info
from pyglet.event import EventDispatcher
import pyglet.window.key, pyglet.window.event
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

class WindowException(Exception):
    pass


class NoSuchDisplayException(WindowException):
    pass


class NoSuchConfigException(WindowException):
    pass


class NoSuchScreenModeException(WindowException):
    pass


class MouseCursorException(WindowException):
    pass


class MouseCursor(object):
    drawable = True

    def draw(self, x, y):
        raise NotImplementedError('abstract')


class DefaultMouseCursor(MouseCursor):
    drawable = False


class ImageMouseCursor(MouseCursor):
    drawable = True

    def __init__(self, image, hot_x=0, hot_y=0):
        self.texture = image.get_texture()
        self.hot_x = hot_x
        self.hot_y = hot_y

    def draw(self, x, y):
        gl.glPushAttrib(gl.GL_ENABLE_BIT | gl.GL_CURRENT_BIT)
        gl.glColor4f(1, 1, 1, 1)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        self.texture.blit(x - self.hot_x, y - self.hot_y, 0)
        gl.glPopAttrib()


def _PlatformEventHandler(data):

    def _event_wrapper(f):
        f._platform_event = True
        if not hasattr(f, '_platform_event_data'):
            f._platform_event_data = []
        f._platform_event_data.append(data)
        return f

    return _event_wrapper


def _ViewEventHandler(f):
    f._view = True
    return f


class _WindowMetaclass(type):

    def __init__(cls, name, bases, dict):
        cls._platform_event_names = set()
        for base in bases:
            if hasattr(base, '_platform_event_names'):
                cls._platform_event_names.update(base._platform_event_names)

        for name, func in dict.items():
            if hasattr(func, '_platform_event'):
                cls._platform_event_names.add(name)

        super(_WindowMetaclass, cls).__init__(name, bases, dict)


class BaseWindow(EventDispatcher):
    __metaclass__ = _WindowMetaclass
    _platform_event_names = set()
    WINDOW_STYLE_DEFAULT = None
    WINDOW_STYLE_DIALOG = 'dialog'
    WINDOW_STYLE_TOOL = 'tool'
    WINDOW_STYLE_BORDERLESS = 'borderless'
    CURSOR_DEFAULT = None
    CURSOR_CROSSHAIR = 'crosshair'
    CURSOR_HAND = 'hand'
    CURSOR_HELP = 'help'
    CURSOR_NO = 'no'
    CURSOR_SIZE = 'size'
    CURSOR_SIZE_UP = 'size_up'
    CURSOR_SIZE_UP_RIGHT = 'size_up_right'
    CURSOR_SIZE_RIGHT = 'size_right'
    CURSOR_SIZE_DOWN_RIGHT = 'size_down_right'
    CURSOR_SIZE_DOWN = 'size_down'
    CURSOR_SIZE_DOWN_LEFT = 'size_down_left'
    CURSOR_SIZE_LEFT = 'size_left'
    CURSOR_SIZE_UP_LEFT = 'size_up_left'
    CURSOR_SIZE_UP_DOWN = 'size_up_down'
    CURSOR_SIZE_LEFT_RIGHT = 'size_left_right'
    CURSOR_TEXT = 'text'
    CURSOR_WAIT = 'wait'
    CURSOR_WAIT_ARROW = 'wait_arrow'
    has_exit = False
    invalid = True
    _legacy_invalid = True
    _width = None
    _height = None
    _caption = None
    _resizable = False
    _style = WINDOW_STYLE_DEFAULT
    _fullscreen = False
    _visible = False
    _vsync = False
    _screen = None
    _config = None
    _context = None
    _windowed_size = None
    _windowed_location = None
    _mouse_cursor = DefaultMouseCursor()
    _mouse_x = 0
    _mouse_y = 0
    _mouse_visible = True
    _mouse_exclusive = False
    _mouse_in_window = False
    _event_queue = None
    _enable_event_queue = True
    _allow_dispatch_event = False
    _default_width = 640
    _default_height = 480

    def __init__(self, width=None, height=None, caption=None, resizable=False, style=WINDOW_STYLE_DEFAULT, fullscreen=False, visible=True, vsync=True, display=None, screen=None, config=None, context=None, mode=None):
        EventDispatcher.__init__(self)
        self._event_queue = []
        if not display:
            display = get_platform().get_default_display()
        if not screen:
            screen = display.get_default_screen()
        if not config:
            for template_config in [gl.Config(double_buffer=True, depth_size=24),
             gl.Config(double_buffer=True, depth_size=16),
             None]:
                try:
                    config = screen.get_best_config(template_config)
                    break
                except NoSuchConfigException:
                    pass

            if not config:
                raise NoSuchConfigException('No standard config is available.')
        if not config.is_complete():
            config = screen.get_best_config(config)
        if not context:
            context = config.create_context(gl.current_context)
        self._context = context
        self._config = self._context.config
        if hasattr(self._config, 'screen'):
            self._screen = self._config.screen
        else:
            display = self._config.canvas.display
            self._screen = display.get_default_screen()
        self._display = self._screen.display
        if fullscreen:
            if width is None and height is None:
                self._windowed_size = (
                 self._default_width, self._default_height)
            width, height = self._set_fullscreen_mode(mode, width, height)
            if not self._windowed_size:
                self._windowed_size = (
                 width, height)
        else:
            if width is None:
                width = self._default_width
            if height is None:
                height = self._default_height
        self._width = width
        self._height = height
        self._resizable = resizable
        self._fullscreen = fullscreen
        self._style = style
        if pyglet.options['vsync'] is not None:
            self._vsync = pyglet.options['vsync']
        else:
            self._vsync = vsync
        if caption is None:
            caption = sys.argv[0]
        self._caption = caption
        from pyglet import app
        app.windows.add(self)
        self._create()
        self.switch_to()
        if visible:
            self.set_visible(True)
            self.activate()
        return

    def _create(self):
        raise NotImplementedError('abstract')

    def _recreate(self, changes):
        raise NotImplementedError('abstract')

    def flip(self):
        raise NotImplementedError('abstract')

    def switch_to(self):
        raise NotImplementedError('abstract')

    def set_fullscreen(self, fullscreen=True, screen=None, mode=None, width=None, height=None):
        if fullscreen == self._fullscreen and (screen is None or screen is self._screen) and (width is None or width == self._width) and (height is None or height == self._height):
            return
        if not self._fullscreen:
            self._windowed_size = self.get_size()
            self._windowed_location = self.get_location()
        if fullscreen and screen is not None:
            self._screen = screen
        self._fullscreen = fullscreen
        if self._fullscreen:
            self._width, self._height = self._set_fullscreen_mode(mode, width, height)
        else:
            self.screen.restore_mode()
            self._width, self._height = self._windowed_size
            if width is not None:
                self._width = width
            if height is not None:
                self._height = height
        self._recreate(['fullscreen'])
        if not self._fullscreen and self._windowed_location:
            if sys.platform != 'darwin' or pyglet.options['darwin_cocoa']:
                self.set_location(*self._windowed_location)
        return

    def _set_fullscreen_mode(self, mode, width, height):
        if mode is not None:
            self.screen.set_mode(mode)
            if width is None:
                width = self.screen.width
            if height is None:
                height = self.screen.height
        elif width is not None or height is not None:
            if width is None:
                width = 0
            if height is None:
                height = 0
            mode = self.screen.get_closest_mode(width, height)
            if mode is not None:
                self.screen.set_mode(mode)
            elif self.screen.get_modes():
                raise NoSuchScreenModeException('No mode matching %dx%d' % (width, height))
        else:
            width = self.screen.width
            height = self.screen.height
            if sys.platform == 'darwin' and not pyglet.options['darwin_cocoa']:
                self.screen.set_mode(None)
        return (
         width, height)

    def on_resize(self, width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, width, 0, height, -1, 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def on_close(self):
        self.has_exit = True
        from pyglet import app
        if app.event_loop is not None:
            self.close()
        return

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE and not modifiers & ~(key.MOD_NUMLOCK | key.MOD_CAPSLOCK | key.MOD_SCROLLLOCK):
            self.dispatch_event('on_close')

    def close(self):
        from pyglet import app
        if not self._context:
            return
        else:
            app.windows.remove(self)
            self._context.destroy()
            self._config = None
            self._context = None
            if app.event_loop:
                app.event_loop.dispatch_event('on_window_close', self)
            return

    def draw_mouse_cursor(self):
        if self._mouse_cursor.drawable and self._mouse_visible and self._mouse_in_window:
            gl.glMatrixMode(gl.GL_PROJECTION)
            gl.glPushMatrix()
            gl.glLoadIdentity()
            gl.glOrtho(0, self.width, 0, self.height, -1, 1)
            gl.glMatrixMode(gl.GL_MODELVIEW)
            gl.glPushMatrix()
            gl.glLoadIdentity()
            self._mouse_cursor.draw(self._mouse_x, self._mouse_y)
            gl.glMatrixMode(gl.GL_PROJECTION)
            gl.glPopMatrix()
            gl.glMatrixMode(gl.GL_MODELVIEW)
            gl.glPopMatrix()

    caption = property((lambda self: self._caption), doc='The window caption (title).  Read-only.\n\n        :type: str\n        ')
    resizable = property((lambda self: self._resizable), doc='True if the window is resizable.  Read-only.\n\n        :type: bool\n        ')
    style = property((lambda self: self._style), doc='The window style; one of the ``WINDOW_STYLE_*`` constants.\n        Read-only.\n        \n        :type: int\n        ')
    fullscreen = property((lambda self: self._fullscreen), doc='True if the window is currently fullscreen.  Read-only.\n        \n        :type: bool\n        ')
    visible = property((lambda self: self._visible), doc='True if the window is currently visible.  Read-only.\n        \n        :type: bool\n        ')
    vsync = property((lambda self: self._vsync), doc="True if buffer flips are synchronised to the screen's vertical\n        retrace.  Read-only.\n        \n        :type: bool\n        ")
    display = property((lambda self: self._display), doc='The display this window belongs to.  Read-only.\n\n        :type: `Display`\n        ')
    screen = property((lambda self: self._screen), doc='The screen this window is fullscreen in.  Read-only.\n        \n        :type: `Screen`\n        ')
    config = property((lambda self: self._config), doc='A GL config describing the context of this window.  Read-only.\n        \n        :type: `pyglet.gl.Config`\n        ')
    context = property((lambda self: self._context), doc='The OpenGL context attached to this window.  Read-only.\n        \n        :type: `pyglet.gl.Context`\n        ')
    width = property((lambda self: self.get_size()[0]), (lambda self, width: self.set_size(width, self.height)), doc='The width of the window, in pixels.  Read-write.\n         \n         :type: int\n         ')
    height = property((lambda self: self.get_size()[1]), (lambda self, height: self.set_size(self.width, height)), doc='The height of the window, in pixels.  Read-write.\n         \n         :type: int\n         ')

    def set_caption(self, caption):
        raise NotImplementedError('abstract')

    def set_minimum_size(self, width, height):
        raise NotImplementedError('abstract')

    def set_maximum_size(self, width, height):
        raise NotImplementedError('abstract')

    def set_size(self, width, height):
        raise NotImplementedError('abstract')

    def get_size(self):
        raise NotImplementedError('abstract')

    def set_location(self, x, y):
        raise NotImplementedError('abstract')

    def get_location(self):
        raise NotImplementedError('abstract')

    def activate(self):
        raise NotImplementedError('abstract')

    def set_visible(self, visible=True):
        raise NotImplementedError('abstract')

    def minimize(self):
        raise NotImplementedError('abstract')

    def maximize(self):
        raise NotImplementedError('abstract')

    def set_vsync(self, vsync):
        raise NotImplementedError('abstract')

    def set_mouse_visible(self, visible=True):
        self._mouse_visible = visible
        self.set_mouse_platform_visible()

    def set_mouse_platform_visible(self, platform_visible=None):
        raise NotImplementedError()

    def set_mouse_cursor(self, cursor=None):
        if cursor is None:
            cursor = DefaultMouseCursor()
        self._mouse_cursor = cursor
        self.set_mouse_platform_visible()
        return

    def set_exclusive_mouse(self, exclusive=True):
        raise NotImplementedError('abstract')

    def set_exclusive_keyboard(self, exclusive=True):
        raise NotImplementedError('abstract')

    def get_system_mouse_cursor(self, name):
        raise NotImplementedError()

    def set_icon(self, *images):
        pass

    def clear(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    def dispatch_event(self, *args):
        if not self._enable_event_queue or self._allow_dispatch_event:
            if EventDispatcher.dispatch_event(self, *args) != False:
                self._legacy_invalid = True
        else:
            self._event_queue.append(args)

    def dispatch_events(self):
        raise NotImplementedError('abstract')

    if _is_epydoc:

        def on_key_press(symbol, modifiers):
            pass

        def on_key_release(symbol, modifiers):
            pass

        def on_text(text):
            pass

        def on_text_motion(motion):
            pass

        def on_text_motion_select(motion):
            pass

        def on_mouse_motion(x, y, dx, dy):
            pass

        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            pass

        def on_mouse_press(x, y, button, modifiers):
            pass

        def on_mouse_release(x, y, button, modifiers):
            pass

        def on_mouse_scroll(x, y, scroll_x, scroll_y):
            pass

        def on_close():
            pass

        def on_mouse_enter(x, y):
            pass

        def on_mouse_leave(x, y):
            pass

        def on_expose():
            pass

        def on_resize(width, height):
            pass

        def on_move(x, y):
            pass

        def on_activate():
            pass

        def on_deactivate():
            pass

        def on_show():
            pass

        def on_hide():
            pass

        def on_context_lost():
            pass

        def on_context_state_lost():
            pass

        def on_draw():
            pass


BaseWindow.register_event_type('on_key_press')
BaseWindow.register_event_type('on_key_release')
BaseWindow.register_event_type('on_text')
BaseWindow.register_event_type('on_text_motion')
BaseWindow.register_event_type('on_text_motion_select')
BaseWindow.register_event_type('on_mouse_motion')
BaseWindow.register_event_type('on_mouse_drag')
BaseWindow.register_event_type('on_mouse_press')
BaseWindow.register_event_type('on_mouse_release')
BaseWindow.register_event_type('on_mouse_scroll')
BaseWindow.register_event_type('on_mouse_enter')
BaseWindow.register_event_type('on_mouse_leave')
BaseWindow.register_event_type('on_close')
BaseWindow.register_event_type('on_expose')
BaseWindow.register_event_type('on_resize')
BaseWindow.register_event_type('on_move')
BaseWindow.register_event_type('on_activate')
BaseWindow.register_event_type('on_deactivate')
BaseWindow.register_event_type('on_show')
BaseWindow.register_event_type('on_hide')
BaseWindow.register_event_type('on_context_lost')
BaseWindow.register_event_type('on_context_state_lost')
BaseWindow.register_event_type('on_draw')

class FPSDisplay(object):
    update_period = 0.25

    def __init__(self, window):
        from time import time
        from pyglet.text import Label
        self.label = Label('', x=10, y=10, font_size=24, bold=True, color=(127, 127,
                                                                           127, 127))
        self.window = window
        self._window_flip = window.flip
        window.flip = self._hook_flip
        self.time = 0.0
        self.last_time = time()
        self.count = 0

    def update(self):
        from time import time
        t = time()
        self.count += 1
        self.time += t - self.last_time
        self.last_time = t
        if self.time >= self.update_period:
            self.set_fps(self.count / self.update_period)
            self.time %= self.update_period
            self.count = 0

    def set_fps(self, fps):
        self.label.text = '%.2f' % fps

    def draw(self):
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()
        gl.glLoadIdentity()
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glPushMatrix()
        gl.glLoadIdentity()
        gl.glOrtho(0, self.window.width, 0, self.window.height, -1, 1)
        self.label.draw()
        gl.glPopMatrix()
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPopMatrix()

    def _hook_flip(self):
        self.update()
        self._window_flip()


if _is_epydoc:
    Window = BaseWindow
    Window.__name__ = 'Window'
    del BaseWindow
elif sys.platform == 'darwin':
    if pyglet.options['darwin_cocoa']:
        from pyglet.window.cocoa import CocoaWindow as Window
    else:
        from pyglet.window.carbon import CarbonWindow as Window
elif sys.platform in ('win32', 'cygwin'):
    from pyglet.window.win32 import Win32Window as Window
else:
    from pyglet.window.xlib import XlibWindow as Window

def get_platform():
    return Platform()


class Platform(object):

    def get_display(self, name):
        for display in pyglet.app.displays:
            if display.name == name:
                return display

        return pyglet.canvas.Display(name)

    def get_default_display(self):
        return pyglet.canvas.get_display()


if _is_epydoc:

    class Display(object):

        def __init__(self):
            raise NotImplementedError('deprecated')

        def get_screens(self):
            raise NotImplementedError('deprecated')

        def get_default_screen(self):
            raise NotImplementedError('deprecated')

        def get_windows(self):
            raise NotImplementedError('deprecated')


else:
    Display = pyglet.canvas.Display
    Screen = pyglet.canvas.Screen
if not _is_epydoc:
    pyglet.window = sys.modules[__name__]
    gl._create_shadow_window()
# okay decompiling out\pyglet.window.pyc
