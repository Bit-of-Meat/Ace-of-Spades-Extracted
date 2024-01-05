# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.mainTab
from aoslib.scenes.frontend.tabBase import TabBase
from aoslib.scenes.frontend.panelBase import BACKGROUND_NONE
from aoslib.scenes.frontend.listPanelBase import ListPanelBase
from aoslib.scenes.main.settingsSliderListItem import SettingsSliderListItem
from aoslib.scenes.main.settingsToggleListItem import SettingsToggleListItem
from aoslib.scenes.main.settingsOptionCheckboxListItem import SettingsOptionCheckboxListItem
from aoslib.scenes.main.settingsRangeBarListItem import SettingsRangeBarListItem
from aoslib.images import global_images
from aoslib import strings
from aoslib.media import HUD_AUDIO_ZONE
from aoslib.tools import make_game_manager_favourite_key
from shared.hud_constants import SETTINGS_ROW_HEIGHT, SETTINGS_ROW_SPACING
import string
from shared.steam import SteamAddFavouriteServer, SteamRemoveFavouriteServer
from shared.constants import A2390

class MainTab(TabBase):
    content_frame = global_images.main_settings_frame
    favorite = False
    initial_favorite = False

    def initialize(self):
        self.x = 152
        self.y = 467
        self.width = 494
        self.height = 293
        self.elements = []
        self.controls_enabled = True
        self.in_game_tab = False
        self.list_panel = ListPanelBase(self.manager)
        self.list_panel.initialise_ui('', self.x, self.y, self.width, self.height, row_height=SETTINGS_ROW_HEIGHT)
        self.list_panel.set_background(BACKGROUND_NONE)
        self.list_panel.line_spacing = SETTINGS_ROW_SPACING
        self.elements.append(self.list_panel)
        self.populate_list()

    def populate_list(self):
        cfg = self.config
        self.list_panel.rows = []
        row = SettingsRangeBarListItem(strings.MASTER_VOLUME, 'master_volume', cfg.master_volume, self.set_volume)
        self.list_panel.rows.append(row)
        row = SettingsRangeBarListItem(strings.MUSIC_VOLUME, 'music_volume', cfg.music_volume, self.set_music_volume)
        self.list_panel.rows.append(row)
        row = SettingsToggleListItem(strings.FULLSCREEN, 'fullscreen', cfg.fullscreen, self.set_config)
        self.list_panel.rows.append(row)
        options = [
         strings.FALSE, strings.TRUE]
        row = SettingsSliderListItem(strings.INVERT_MOUSE, 'invert_mouse', options, cfg.invert_mouse, self.set_slider_config, self.media)
        self.list_panel.rows.append(row)
        row = SettingsOptionCheckboxListItem(strings.FAVORITE, 'favorite', self.in_game_tab, self.set_favorite)
        self.list_panel.rows.append(row)
        self.list_panel.on_scroll(0, silent=True)

    def get_row_with_id(self, id):
        for row in self.list_panel.rows:
            if row.id == id:
                return row

        return

    def on_menu_opened(self):
        fav_enabled = False
        if self.in_game_tab:
            server_mode = self.manager.client.server_mode
            if server_mode != A2390:
                fav_enabled = True
            host = self.manager.ip
            port = self.manager.port
            manager_key = make_game_manager_favourite_key(host, port)
            self.favorite = True if manager_key in self.manager.favourite_servers else False
            text = self.manager.server_name
        else:
            self.favorite = False
            text = strings.OPTION_ONLY_IN_PLAY
        row = self.get_row_with_id('favorite')
        if row is not None:
            row.set_enabled(fav_enabled)
            row.set_value(self.favorite)
            row.enable_on_scroll = False
            row.set_text(text)
        self.initial_favorite = self.favorite
        return

    def draw(self):
        for element in self.elements:
            element.draw()

    def update_display(self):
        pass

    def on_defaults_pressed(self):
        self.populate_list()
        self.on_menu_opened()

    def back_pressed(self):
        self.populate_list()

    def save_pressed(self):
        if self.in_game_tab and self.initial_favorite != self.favorite:
            host = self.manager.ip
            port = self.manager.port
            query_port = self.manager.query_port
            manager_key = make_game_manager_favourite_key(host, port)
            favourite_servers = self.manager.favourite_servers
            if self.favorite:
                SteamAddFavouriteServer(host, port, query_port, False)
                favourite_servers.add(manager_key)
            else:
                SteamRemoveFavouriteServer(host, port, query_port, False)
                if manager_key in favourite_servers:
                    favourite_servers.discard(manager_key)

    def set_slider_config(self, value, value_name, name):
        self.media.play('menu_scrollA', zone=HUD_AUDIO_ZONE)
        self.config.set(name, value)

    def set_config(self, value, name):
        self.media.play('menu_scrollA', zone=HUD_AUDIO_ZONE)
        self.config.set(name, value)

    def set_volume(self, set_on_click, current_value):
        if set_on_click:
            self.media.play('menu_scrollA', zone=HUD_AUDIO_ZONE)
        self.config.set('master_volume', current_value)

    def set_music_volume(self, set_on_click, current_value):
        if set_on_click:
            self.media.play('menu_scrollA', zone=HUD_AUDIO_ZONE)
        self.config.set('music_volume', current_value)

    def set_favorite(self, value, name):
        self.media.play('menu_scrollA', zone=HUD_AUDIO_ZONE)
        self.favorite = value
# okay decompiling out\aoslib.scenes.frontend.mainTab.pyc
