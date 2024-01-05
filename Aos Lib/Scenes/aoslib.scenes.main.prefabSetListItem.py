# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.prefabSetListItem
from aoslib.scenes.main.listPanelItemBase import ListPanelItemBase
from aoslib.common import collides
from aoslib.images import global_images
from aoslib.text import draw_text_with_size_validation, get_resized_font_and_formatted_text_to_fit_boundaries, big_standard_ui_font, medium_standard_ui_font, small_standard_ui_font
from aoslib.draw import draw_quad
from pyglet import gl
from shared.constants import A1054
from shared.hud_constants import MINIMUM_HEIGHT_FOR_BIG_FONT, MINIMUM_HEIGHT_FOR_MEDIUM_FONT, TEXT_BACKGROUND_SPACING

class PrefabSetListItem(ListPanelItemBase):

    def initialize(self, name, id):
        super(PrefabSetListItem, self).initialize(name)
        self.id = id
# okay decompiling out\aoslib.scenes.main.prefabSetListItem.pyc
