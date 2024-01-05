# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.settingsColourPreviewListItem
from aoslib.scenes.main.settingsListItemBase import SettingsListItemBase
from aoslib.images import global_images
from pyglet import gl
from aoslib.draw import draw_quad
from shared.hud_constants import UI_CONTROL_SPACING, TEXT_BACKGROUND_SPACING

class SettingsColourPreviewListItem(SettingsListItemBase):

    def initialize(self, name, id, colour):
        super(SettingsColourPreviewListItem, self).initialize(name)
        self.id = id
        self.initial_value = colour
        self.colour = colour

    def set_value(self, colour):
        self.colour = colour

    def reset(self):
        self.colour = self.initial_value

    def draw_elements(self):
        for element in self.elements:
            element.draw()

        height = self.height - UI_CONTROL_SPACING * 2
        width = self.width - TEXT_BACKGROUND_SPACING * 3 - self.name_width
        x = self.x1 + TEXT_BACKGROUND_SPACING + self.name_width + TEXT_BACKGROUND_SPACING
        y = self.y1 + UI_CONTROL_SPACING
        black = (0, 0, 0, 255)
        draw_quad(x, y, width, height, black)
        padding = 3
        draw_quad(x + padding, y + padding, width - padding * 2, height - padding * 2, self.colour)
# okay decompiling out\aoslib.scenes.main.settingsColourPreviewListItem.pyc
