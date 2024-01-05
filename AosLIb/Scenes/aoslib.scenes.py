# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes
from aoslib.gui import ControlBase
from pyglet import gl

class Scene(ControlBase):

    def __init__(self, manager, in_game_menu=False):
        self.manager = manager
        self.config = manager.config
        self.window = manager.window
        self.media = manager.media
        self.keyboard = manager.keyboard
        self.mouse = manager.mouse
        self.in_game_menu = in_game_menu
        self.initialize()

    def initialize(self):
        pass

    def on_start(self, *arg, **kw):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

    def close(self):
        pass

    def on_stop(self):
        pass

    def set_scene(self, *arg, **kw):
        self.manager.set_scene(*arg, **kw)

    def play_select(self):
        pass

    def transform_mouse(self, x, y):
        return (
         x, y)

    def is_current(self):
        return self is self.manager.scene

    def set_resizing_perspective(self, width, height):
        window = self.window
        gl.glViewport(0, 0, window.width, window.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, width, 0, height, -1, 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

    def set_normal_perspective(self):
        window = self.window
        self.set_resizing_perspective(window.width, window.height)


class ElementScene(Scene):
    enabled = True
    visible = True
    elements = ()

    def get_elements(self):
        return self.elements

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_mouse_press(x, y, button, modifiers)

    def on_double_click(self, x, y, button, modifiers):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_double_click(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_mouse_drag(x, y, dx, dy, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_mouse_motion(x, y, dx, dy)

    def on_key_press(self, *arg, **kw):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_key_press(*arg, **kw)

    def on_key_release(self, *arg, **kw):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_key_release(*arg, **kw)

    def on_mouse_scroll(self, *arg, **kw):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_mouse_scroll(*arg, **kw)

    def on_text(self, value):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_text(value)

    def on_text_motion(self, value):
        if not self.enabled:
            return
        for element in self.get_elements():
            element.on_text_motion(value)

    def draw_hud(self):
        pass

    def on_connect(self):
        pass

    def on_disconnect(self, reason=0):
        pass

    def packet_received(self, packet, sent_time):
        pass

    def on_map_transfer(self):
        pass

    def on_pack_transfer(self):
        pass


class MenuScene(ElementScene):
    clears_scene_lock = True
    control = True


class HUDScene(MenuScene):
    control = False
# okay decompiling out\aoslib.scenes.pyc
