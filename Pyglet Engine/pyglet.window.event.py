# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.window.event
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import sys
from pyglet.window import key
from pyglet.window import mouse

class WindowExitHandler(object):
    has_exit = False

    def on_close(self):
        self.has_exit = True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.has_exit = True


class WindowEventLogger(object):

    def __init__(self, logfile=None):
        if logfile is None:
            logfile = sys.stdout
        self.file = logfile
        return

    def on_key_press(self, symbol, modifiers):
        print >> self.file, 'on_key_press(symbol=%s, modifiers=%s)' % (
         key.symbol_string(symbol), key.modifiers_string(modifiers))

    def on_key_release(self, symbol, modifiers):
        print >> self.file, 'on_key_release(symbol=%s, modifiers=%s)' % (
         key.symbol_string(symbol), key.modifiers_string(modifiers))

    def on_text(self, text):
        print >> self.file, 'on_text(text=%r)' % text

    def on_text_motion(self, motion):
        print >> self.file, 'on_text_motion(motion=%s)' % key.motion_string(motion)

    def on_text_motion_select(self, motion):
        print >> self.file, 'on_text_motion_select(motion=%s)' % key.motion_string(motion)

    def on_mouse_motion(self, x, y, dx, dy):
        print >> self.file, 'on_mouse_motion(x=%d, y=%d, dx=%d, dy=%d)' % (
         x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print >> self.file, 'on_mouse_drag(x=%d, y=%d, dx=%d, dy=%d, buttons=%s, modifiers=%s)' % (
         x, y, dx, dy,
         mouse.buttons_string(buttons), key.modifiers_string(modifiers))

    def on_mouse_press(self, x, y, button, modifiers):
        print >> self.file, 'on_mouse_press(x=%d, y=%d, button=%r, modifiers=%s)' % (
         x, y,
         mouse.buttons_string(button), key.modifiers_string(modifiers))

    def on_mouse_release(self, x, y, button, modifiers):
        print >> self.file, 'on_mouse_release(x=%d, y=%d, button=%r, modifiers=%s)' % (
         x, y,
         mouse.buttons_string(button), key.modifiers_string(modifiers))

    def on_mouse_scroll(self, x, y, dx, dy):
        print >> self.file, 'on_mouse_scroll(x=%f, y=%f, dx=%f, dy=%f)' % (
         x, y, dx, dy)

    def on_close(self):
        print >> self.file, 'on_close()'

    def on_mouse_enter(self, x, y):
        print >> self.file, 'on_mouse_enter(x=%d, y=%d)' % (x, y)

    def on_mouse_leave(self, x, y):
        print >> self.file, 'on_mouse_leave(x=%d, y=%d)' % (x, y)

    def on_expose(self):
        print >> self.file, 'on_expose()'

    def on_resize(self, width, height):
        print >> self.file, 'on_resize(width=%d, height=%d)' % (width, height)

    def on_move(self, x, y):
        print >> self.file, 'on_move(x=%d, y=%d)' % (x, y)

    def on_activate(self):
        print >> self.file, 'on_activate()'

    def on_deactivate(self):
        print >> self.file, 'on_deactivate()'

    def on_show(self):
        print >> self.file, 'on_show()'

    def on_hide(self):
        print >> self.file, 'on_hide()'

    def on_context_lost(self):
        print >> self.file, 'on_context_lost()'

    def on_context_state_lost(self):
        print >> self.file, 'on_context_state_lost()'

    def on_draw(self):
        print >> self.file, 'on_draw()'
# okay decompiling out\pyglet.window.event.pyc
