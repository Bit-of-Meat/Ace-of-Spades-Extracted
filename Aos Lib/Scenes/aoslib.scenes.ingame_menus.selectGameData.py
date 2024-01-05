# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.ingame_menus.selectGameData
from aoslib import strings
from aoslib.scenes.ingame_menus.selectUGC import SelectUGC
from aoslib.images import global_images
from collections import namedtuple

class SelectGameData(SelectUGC):
    title = strings.UGC_GAME_DATA
    image_offset = [0.0, -13.0]
    selected_image_offset = [0.0, 4.0]

    def create_tabs(self):
        Tab = namedtuple('Tab', 'text table_index unselected_image selected_image')
        for index, category in enumerate(self.ugc_items_by_tag.keys()):
            self.tabs.append(Tab(strings.get_by_id(category), index + len(self.prefabs_by_tag.keys()), global_images.gdata_unselected_tab, global_images.gdata_selected_tab))

        super(SelectGameData, self).create_tabs(len(self.prefabs_by_tag.keys()))

    def draw_panel(self):
        global_images.gdata_template_bg.blit(235, 325)

    def on_key_press(self, symbol, modifiers):
        super(SelectGameData, self).on_key_press(symbol, modifiers, exit_menu_key=self.config.change_team)
# okay decompiling out\aoslib.scenes.ingame_menus.selectGameData.pyc
