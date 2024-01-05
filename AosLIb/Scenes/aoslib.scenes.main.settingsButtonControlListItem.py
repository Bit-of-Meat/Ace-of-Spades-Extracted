# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.settingsButtonControlListItem
from aoslib.scenes.main.settingsListItemBase import SettingsListItemBase
from aoslib.images import global_images
from pyglet import gl
from aoslib.draw import draw_quad
from shared.hud_constants import UI_CONTROL_SPACING, TEXT_BACKGROUND_SPACING
from aoslib.gui import TextButton

class SettingsButtonControlListItem(SettingsListItemBase):

    def initialize(self, name, button_text, id, on_click_callback):
        super(SettingsButtonControlListItem, self).initialize(name)
        self.id = id
        self.button_text = button_text
        self.on_click_callback = on_click_callback
        self.control = None
        return

    def update_position(self, x, y, width, height, highlight_width):
        super(SettingsButtonControlListItem, self).update_position(x, y, width, height, highlight_width)
        if not self.control:
            height = self.height - UI_CONTROL_SPACING * 2
            width = self.width - TEXT_BACKGROUND_SPACING * 3 - self.name_width
            x = self.x1 + TEXT_BACKGROUND_SPACING + self.name_width + TEXT_BACKGROUND_SPACING
            y = self.y1 + UI_CONTROL_SPACING + height
            self.control = TextButton(self.button_text, x, y, width, height, 30)
            self.control.add_handler(self.on_click_callback)
            self.elements.append(self.control)
        else:
            height = self.height - UI_CONTROL_SPACING * 2
            width = self.width - TEXT_BACKGROUND_SPACING * 3 - self.name_width
            self.control.x = self.x1 + TEXT_BACKGROUND_SPACING + self.name_width + TEXT_BACKGROUND_SPACING
            self.control.y = self.y1 + UI_CONTROL_SPACING + height
            self.control.width = width
            self.control.height = height
# okay decompiling out\aoslib.scenes.main.settingsButtonControlListItem.pyc
