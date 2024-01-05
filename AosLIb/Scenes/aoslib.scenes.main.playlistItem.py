# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.playlistItem
from aoslib.scenes.main.ownableItemBase import OwnableItemBase
from aoslib.text import draw_text_with_size_validation
from pyglet import gl

class PlaylistItem(OwnableItemBase):

    def initialize(self, id, name, game_info, map_rotation, server_type, modes, dlc_manager, selectable_when_unowned):
        super(PlaylistItem, self).initialize(name, dlc_manager, selectable_when_unowned, playlist_id=id)
        self.id = id
        self.game_info = game_info
        self.map_rotation = map_rotation
        self.server_type = server_type
        self.modes = modes
        self.ping = None
        self.players = None
        return

    def draw_name(self):
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        text_width = self.width - self.pad * 2
        if self.ping is not None or self.players is not None:
            text_width -= 133
        text_height = self.height - self.pad * 2
        x = self.get_text_x_position()
        y = self.get_text_y_position()
        draw_text_with_size_validation(self.name, x, y, text_width, text_height, self.text_colour, self.font, self.center_text)
        if self.ping is not None:
            draw_text_with_size_validation(str(self.ping), x + text_width, y, 20, text_height, self.text_colour, self.font, self.center_text)
        if self.players is not None:
            draw_text_with_size_validation(self.players, x + text_width + 60, y, 30, text_height, self.text_colour, self.font, self.center_text)
        return
# okay decompiling out\aoslib.scenes.main.playlistItem.pyc
