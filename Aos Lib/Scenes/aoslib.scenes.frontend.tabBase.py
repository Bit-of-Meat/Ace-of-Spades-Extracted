# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.tabBase
from aoslib.scenes import Scene, ElementScene, MenuScene

class TabBase(MenuScene):
    enabled = False

    def set_in_game_tab(self, in_game_tab):
        self.in_game_tab = in_game_tab
        self.update_display()

    def on_menu_opened(self):
        pass

    def on_set(self):
        pass

    def update_display(self):
        pass

    def set_enabled_controls(self, enabled):
        pass
# okay decompiling out\aoslib.scenes.frontend.tabBase.pyc
