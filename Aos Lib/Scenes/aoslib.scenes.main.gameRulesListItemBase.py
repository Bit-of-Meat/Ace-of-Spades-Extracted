# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.gameRulesListItemBase
from aoslib.scenes.main.listPanelItemBase import ListPanelItemBase
from shared.constants import A1054, A1055
from aoslib.text import draw_text_with_size_validation, medium_aldo_ui_font
from aoslib import strings
from pyglet import gl
from shared.constants_matchmaking import *
from shared.steam import SteamGetLobbyData, SteamSetLobbyData
from playlists import get_default_rule_value_for_lobby

class GameRulesListItemBase(ListPanelItemBase):

    def initialize(self, rule_id, lobby_id, on_value_changed_callback, media, rule_type='GENERAL'):
        super(GameRulesListItemBase, self).initialize()
        self.elements = []
        self.lobby_id = lobby_id
        self.name = strings.get_by_id(rule_id)
        self.name_width = 0
        self.pad_x = 0
        self.pad_y = 0
        self.rule_id = rule_id
        self.current_value = SteamGetLobbyData(self.lobby_id, self.rule_id)
        self.media = media
        self.rule_type = rule_type
        self.disabled = False
        if self.current_value == '':
            self.set_default_value()
        self.on_value_changed_callback = on_value_changed_callback

    def set_disabled(self, do_disable=True):
        self.disabled = do_disable

    def set_default_value(self):
        self.current_value = self.get_default_value()
        if self.disabled:
            self.set_disabled(False)

    def get_default_value(self):
        return get_default_rule_value_for_lobby(self.rule_id, self.lobby_id)

    def draw_selection_highlight(self):
        pass

    def draw_hovered_highlight(self):
        pass

    def reset(self):
        self.set_default_value()

    def update_position(self, x, y, width, height, highlight_width):
        super(GameRulesListItemBase, self).update_position(x, y, width, height, highlight_width)
        self.pad_x = self.width * 0.03
        self.pad_y = self.height * 0.015
        spacing_x = self.pad_x
        self.name_width = self.width - self.pad_x * 2

    def draw_name(self):
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        name_width = self.width - TEXT_BACKGROUND_SPACING * 2
        if self.disabled:
            colour = A1055
        else:
            colour = A1054
        draw_text_with_size_validation(self.name, self.x1 + TEXT_BACKGROUND_SPACING, self.get_text_y_position(), name_width, self.height, colour, medium_aldo_ui_font, False)
# okay decompiling out\aoslib.scenes.main.gameRulesListItemBase.pyc
