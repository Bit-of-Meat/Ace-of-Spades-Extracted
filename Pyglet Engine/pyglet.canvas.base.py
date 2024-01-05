# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.canvas.base
from pyglet import app
from pyglet import gl
from pyglet import window

class Display(object):
    name = None
    x_screen = None

    def __init__(self, name=None, x_screen=None):
        app.displays.add(self)

    def get_screens(self):
        raise NotImplementedError('abstract')

    def get_default_screen(self):
        mainScreen = None
        for screen in self.get_screens():
            if mainScreen is None:
                mainScreen = screen
            if screen.x == 0 and screen.y == 0:
                mainScreen = screen

        return mainScreen

    def get_windows(self):
        return [ window for window in app.windows if window.display is self ]


class Screen(object):

    def __init__(self, display, x, y, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return '%s(x=%d, y=%d, width=%d, height=%d)' % (
         self.__class__.__name__, self.x, self.y, self.width, self.height)

    def get_best_config(self, template=None):
        if template is None:
            template = gl.Config()
        configs = self.get_matching_configs(template)
        if not configs:
            raise window.NoSuchConfigException()
        return configs[0]

    def get_matching_configs(self, template):
        raise NotImplementedError('abstract')

    def get_modes(self):
        raise NotImplementedError('abstract')

    def get_mode(self):
        raise NotImplementedError('abstract')

    def get_closest_mode(self, width, height):
        current = self.get_mode()
        best = None
        for mode in self.get_modes():
            if mode.width < width or mode.height < height:
                continue
            if best is None:
                best = mode
            if mode.width <= best.width and mode.height <= best.height and (mode.width < best.width or mode.height < best.height):
                best = mode
            if mode.width == best.width and mode.height == best.height:
                points = 0
                if mode.rate == current.rate:
                    points += 2
                if best.rate == current.rate:
                    points -= 2
                if mode.depth == current.depth:
                    points += 1
                if best.depth == current.depth:
                    points -= 1
                if points > 0:
                    best = mode

        return best

    def set_mode(self, mode):
        raise NotImplementedError('abstract')

    def restore_mode(self):
        raise NotImplementedError('abstract')


class ScreenMode(object):
    width = None
    height = None
    depth = None
    rate = None

    def __init__(self, screen):
        self.screen = screen

    def __repr__(self):
        return '%s(width=%r, height=%r, depth=%r, rate=%r)' % (
         self.__class__.__name__,
         self.width, self.height, self.depth, self.rate)


class Canvas(object):

    def __init__(self, display):
        self.display = display
# okay decompiling out\pyglet.canvas.base.pyc
