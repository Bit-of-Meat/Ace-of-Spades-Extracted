# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.mapListItem
from aoslib.scenes.main.listPanelItemBase import ListPanelItemBase
from aoslib.text import draw_text_with_size_validation, medium_aldo_ui_font, big_aldo_ui_font
from pyglet import gl
from aoslib import strings
from shared.constants import A1054

class MapListItem(ListPanelItemBase):

    def initialize(self, name, available_map=True):
        super(MapListItem, self).initialize()
        self.name = name
        self.available_map = available_map

    def update_position(self, x, y, width, height, highlight_width):
        super(MapListItem, self).update_position(x, y, width, height, highlight_width)

    def set_selected(self, selected, media):
        if self.available_map:
            super(MapListItem, self).set_selected(selected, media)

    def set_hovered(self, hovered):
        if self.available_map:
            super(MapListItem, self).set_hovered(hovered)

    def draw_name(self):
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        y = self.get_text_y_position()
        pad_x = 20
        pad_y = 10
        height = self.height - pad_y
        right_text_width = 25
        right_text_x = self.x1 + self.width - pad_x / 2 - right_text_width
        pad_x = 15
        name_width = self.width / 3 * 2
        name_x = self.x1 + pad_x
        if self.available_map:
            colour = A1054
        else:
            colour = (
             self.background_colour[0] + 20, self.background_colour[1] + 20, self.background_colour[2] + 20, self.background_colour[3])
            draw_text_with_size_validation(strings.NOT_OWNED, name_x + name_width + pad_x, y, self.width / 3 - pad_x * 3, height, colour, medium_aldo_ui_font, False)
        draw_text_with_size_validation(self.name, name_x, y, name_width, height, colour, self.font, False)
# okay decompiling out\aoslib.scenes.main.mapListItem.pyc
