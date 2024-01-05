# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.hud.text3d
from aoslib.text import text3d_font
from pyglet.gl import *
from aoslib.common import distance_3d
from shared.constants import A2383

class Text3D(object):

    def __init__(self, text, position, scale=0.003, color=(255, 255, 255, 255), disable_depth_test=False, font=None):
        self.text = text
        self.position = position
        self.scale = scale
        self.color = color
        self.disable_depth_test = disable_depth_test
        if font == None:
            self.font = text3d_font
        else:
            self.font = font
        return

    def set_text(self, text):
        self.text = text

    def set_position(self, position):
        self.position = position

    def set_font(self, font):
        self.font = font

    def set_color(self, color):
        self.color = color


class Text3DRenderer(object):

    def __init__(self):
        self.texts = {}

    def add_text(self, key, value):
        self.texts[key] = value

    def remove_text(self, key):
        self.texts.pop(key)

    def render(self, or_x, or_y, scenepos):
        glDisable(GL_LIGHTING)
        for key, text in self.texts.iteritems():
            if text.text == '':
                continue
            glPushMatrix()
            if text.disable_depth_test:
                glDisable(GL_DEPTH_TEST)
            position = text.position
            glTranslatef(position.x, -position.z, position.y)
            glRotatef(or_y, 0.0, 1.0, 0.0)
            glRotatef(or_x, 1.0, 0.0, 0.0)
            d = distance_3d(scenepos.x, scenepos.y, scenepos.z, position.x, position.y, position.z)
            if d < A2383:
                scale = text.scale * d ** 0.7
                glScalef(scale, scale, scale)
                try:
                    text.font.draw_3d(text.text, 0.0, 0.0, 0.0, text.color, center=True)
                except:
                    text3d_font.draw_3d(text.text, 0.0, 0.0, 0.0, text.color, center=True)

            if text.disable_depth_test:
                glEnable(GL_DEPTH_TEST)
            glPopMatrix()

        glEnable(GL_LIGHTING)
# okay decompiling out\aoslib.hud.text3d.pyc
