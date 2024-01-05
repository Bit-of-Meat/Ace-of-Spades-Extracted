# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.LeaderboardMenu
from aoslib.scenes import Scene, ElementScene, MenuScene
from aoslib.common import wave, collides
from shared.constants import *
from shared.common import clamp
from aoslib.text import title_font, settings_font, settings_changed_font, Label, draw_text_with_alignment_and_size_validation, ammo_font, reserve_font, network_font, medium_aldo_ui_font
from aoslib.gui import TextButton, VerticalScrollBar, SquareButton, NavigationBar, NAVBAR_LEFT
from aoslib.scenes.gui.dropBoxControl import DropBoxControl
from aoslib.images import global_images
from pyglet import gl
from aoslib import strings
from aoslib.media import MUSIC_AUDIO_ZONE, HUD_AUDIO_ZONE
from shared.steam import SteamGetPersonaName, SteamGetFriendList, GetUserSteamID, SteamGetFriendPersonaName, SteamIsLoggedOn
from aoslib.weapons.list import WEAPONS
from aoslib.draw import draw_quad
from aoslib.scoremanager import ScoreManager
from shared.hud_constants import *
from aoslib.scenes.frontend.listPanelBase import ListPanelBase
from aoslib.scenes.frontend.panelBase import BACKGROUND_NONE
from aoslib.scenes.main.listPanelItemBase import ListPanelItemBase
from aoslib.scenes.frontend.leaderboardListItem import *
from aoslib.scenes.frontend.leaderboardListPanel import *
import math
from aoslib.text import big_aldo_ui_font
LEADERBOARD_GLOBAL, LEADERBOARD_LOCAL, LEADERBOARD_FRIENDS = xrange(3)
LEADERBOARD_MENU_GRID_COLUMN_NAMES = {A855: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_KILLS, strings.LEADERBOARD_DEATHS, strings.LEADERBOARD_KDR, strings.LEADERBOARD_WINS, strings.LEADERBOARD_LOSSES], 
   A856: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_HEADSHOT, strings.LEADERBOARD_MELEE, strings.LEADERBOARD_KILLS, strings.LEADERBOARD_ASSIST, strings.LEADERBOARD_RETRIBUTION, strings.LEADERBOARD_DEFENCE], 
   A857: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_SURVIVAL, strings.LEADERBOARD_ASSAULT, strings.LEADERBOARD_DEFEND, strings.LEADERBOARD_ESCORT], 
   A858: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_OCCUPY, strings.LEADERBOARD_CLAIM, strings.LEADERBOARD_CONTROL, strings.LEADERBOARD_DEFEND, strings.LEADERBOARD_CONTEST], 
   A859: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_OCCUPY, strings.LEADERBOARD_BOMB, strings.LEADERBOARD_CARRY, strings.LEADERBOARD_ASSIST, strings.LEADERBOARD_DEFEND, strings.LEADERBOARD_SURVIVAL], 
   A860: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_CAPTURE, strings.LEADERBOARD_UNCOVER, strings.LEADERBOARD_CARRY, strings.LEADERBOARD_ASSIST, strings.LEADERBOARD_ASSAULT, strings.LEADERBOARD_STEAL], 
   A861: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_CAPTURE, strings.LEADERBOARD_CARRY, strings.LEADERBOARD_CLAIM, strings.LEADERBOARD_ASSIST, strings.LEADERBOARD_DEFEND, strings.LEADERBOARD_ASSAULT], 
   A862: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_SURVIVAL, strings.LEADERBOARD_LASTMANSTANDING, strings.LEADERBOARD_KILLSURVIVOR, strings.LEADERBOARD_KILLSASLASTMAN], 
   A863: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_DESTROY, strings.LEADERBOARD_REPAIR, strings.LEADERBOARD_DEFEND, strings.LEADERBOARD_ASSAULT], 
   A864: [
        strings.LEADERBOARD_RANK, strings.LEADERBOARD_NAME, strings.LEADERBOARD_TOTAL, strings.LEADERBOARD_OCCUPY, strings.LEADERBOARD_FIRST, strings.LEADERBOARD_CONTROL, strings.LEADERBOARD_DEFEND, strings.LEADERBOARD_ASSAULT, strings.LEADERBOARD_CONTEST]}

class LeaderboardMenu(MenuScene):

    def on_start(self, menu=None, tab=-1, **kw):
        self.show_wait_msg = True
        self.profile_data = None
        self.leaderboard_data = []
        self.elements = []
        self.visible_items = LEADERBOARD_MENU_NOOF_VISIBLE_ITEMS
        self.leaderboard_index = A855
        self.scope_index = LEADERBOARD_GLOBAL
        self.focused_dropbox = None
        self.columns = []
        self.friend_list = SteamGetFriendList()
        self.friend_list.append(GetUserSteamID())
        self.grid = LeaderboardListPanel(self.manager)
        self.grid.initialise_ui(title='leaderboard', x=LEADERBOARD_MENU_GRID_POSITION_X, y=LEADERBOARD_MENU_GRID_POSITION_Y, width=LEADERBOARD_MENU_GRID_WIDTH, height=LEADERBOARD_MENU_GRID_HEIGHT, row_height=LEADERBOARD_MENU_GRID_ROW_HEIGHT, has_header=False, list_items_background_colors=None, spacing=LEADERBOARD_MENU_GRID_SPACING)
        self.grid.set_columns(self.columns)
        self.elements.append(self.grid)
        self.navigation_bar = NavigationBar(x=LEADERBOARD_MENU_BACK_BUTTON_POSITION_X, y=LEADERBOARD_MENU_BACK_BUTTON_POSITION_Y, width=LEADERBOARD_MENU_BACK_BUTTON_WIDTH, height=LEADERBOARD_MENU_BACK_BUTTON_HEIGHT, middle_button=False, right_button=False, left_button=False)
        self.navigation_bar.add_left_button(strings.BACK)
        self.navigation_bar.add_handler(self.navigation_button_pressed)
        self.elements.append(self.navigation_bar)
        leaderboard_types = []
        for leaderboard_type in A871.itervalues():
            leaderboard_types.append(strings.get_by_id(leaderboard_type[A866]))

        self.type_drop_box = DropBoxControl(manager=self.manager, rows=leaderboard_types, selected_index=self.leaderboard_index, x=LEADERBOARD_MENU_TYPE_DROPBOX_POSITION_X, y=LEADERBOARD_MENU_TYPE_DROPBOX_POSITION_Y, width=LEADERBOARD_MENU_TYPE_DROPBOX_WIDTH, height=LEADERBOARD_MENU_TYPE_DROPBOX_HEIGHT, noof_visible_rows=LEADERBOARD_MENU_TYPE_DROPBOX_NOOF_VISIBLE_ROWS, row_height=LEADERBOARD_MENU_TYPE_DROPBOX_ROW_HEIGHT)
        self.type_drop_box.add_handler(self.on_type_changed)
        self.type_drop_box.add_focus_gained_handler(self.on_focus_lost)
        self.type_drop_box.add_focus_lost_handler(self.on_focus_gained)
        self.elements.append(self.type_drop_box)
        scope_types = []
        for scope_type in LEADERBOARD_MENU_SCOPE_OPTIONS:
            scope_types.append(strings.get_by_id(scope_type))

        self.scope_drop_down = DropBoxControl(manager=self.manager, rows=scope_types, selected_index=self.scope_index, x=LEADERBOARD_MENU_SCOPE_DROPBOX_POSITION_X, y=LEADERBOARD_MENU_SCOPE_DROPBOX_POSITION_Y, width=LEADERBOARD_MENU_SCOPE_DROPBOX_WIDTH, height=LEADERBOARD_MENU_SCOPE_DROPBOX_HEIGHT, noof_visible_rows=LEADERBOARD_MENU_SCOPE_DROPBOX_NOOF_VISIBLE_ROWS, row_height=LEADERBOARD_MENU_SCOPE_DROPBOX_ROW_HEIGHT)
        self.scope_drop_down.add_handler(self.on_scope_changed)
        self.scope_drop_down.add_focus_gained_handler(self.on_focus_lost)
        self.scope_drop_down.add_focus_lost_handler(self.on_focus_gained)
        self.elements.append(self.scope_drop_down)
        self.leaderboard_data = None
        self.leaderboard_dataCach = []
        for _ in A871:
            self.leaderboard_dataCach.append([None, None, None])

        self.manager.score_manager.set_request_leaderboard_callback(self.score_manager_leaderboard_callback)
        self.getCurrentLeaderBoard()
        return

    def update(self, dt):
        super(LeaderboardMenu, self).update(dt)
        if not SteamIsLoggedOn():
            from aoslib.scenes.frontend.selectMenu import SelectMenu
            self.manager.set_menu(SelectMenu, back=True)

    def on_focus_lost(self, dropBoxControl):
        if self.focused_dropbox and self.focused_dropbox != dropBoxControl:
            self.focused_dropbox.close_drop_down(True)
        self.focused_dropbox = dropBoxControl
        self.grid.enabled = False

    def on_focus_gained(self, dropBoxControl):
        self.focused_dropbox = None
        self.grid.enabled = True
        return

    def on_type_changed(self, index):
        if not self.show_wait_msg:
            self.leaderboard_index = index
            self.getCurrentLeaderBoard()

    def on_scope_changed(self, index):
        if not self.show_wait_msg:
            self.scope_index = index
            self.getCurrentLeaderBoard()

    def getCurrentLeaderBoard(self):
        self.leaderboard_data = self.leaderboard_dataCach[self.leaderboard_index][self.scope_index]
        if self.leaderboard_data == None:
            self.show_wait_msg = True
            self.leaderboard_data = []
            self.refresh()
            self.type_drop_box.set_enabled(False)
            self.scope_drop_down.set_enabled(False)
            if self.scope_index == LEADERBOARD_GLOBAL:
                self.manager.score_manager.request_global_leaderboard(A871[self.leaderboard_index][A870], A871[self.leaderboard_index][A869])
            else:
                if self.scope_index == LEADERBOARD_LOCAL:
                    self.manager.score_manager.request_local_leaderboard(A871[self.leaderboard_index][A870], A871[self.leaderboard_index][A869], GetUserSteamID())
                elif self.scope_index == LEADERBOARD_FRIENDS:
                    self.manager.score_manager.request_friend_leaderboard(A871[self.leaderboard_index][A870], A871[self.leaderboard_index][A869], self.friend_list)
        else:
            self.refresh()
        return

    def on_stop(self):
        self.manager.score_manager.clear_request_profile_callback()

    def on_scroll(self, value, silent=False):
        if self.media is not None and not silent:
            self.media.play('menu_scrollA', zone=HUD_AUDIO_ZONE)
        return

    def score_manager_leaderboard_callback(self, leaderboard):
        self.type_drop_box.set_enabled(True)
        self.scope_drop_down.set_enabled(True)
        self.show_wait_msg = False
        if leaderboard is None or 'leaderboard' not in leaderboard:
            return
        current_player_steam_id = GetUserSteamID()
        for leaderboard_entry in leaderboard['leaderboard']:
            if leaderboard_entry[0] == current_player_steam_id:
                leaderboard_entry[1] = SteamGetPersonaName()
            elif leaderboard_entry[0] in self.friend_list:
                leaderboard_entry[1] = SteamGetFriendPersonaName(leaderboard_entry[0])

        self.leaderboard_data = self.leaderboard_dataCach[self.leaderboard_index][self.scope_index] = leaderboard['leaderboard']
        self.refresh()
        return

    def refresh(self):
        self.columns = []
        noof_columns = len(LEADERBOARD_MENU_GRID_COLUMN_NAMES[self.leaderboard_index])
        widest_name_column_index = None
        widest_name_width = 0
        kdr_special_case_column_index = None
        for column_index, column_name in enumerate(LEADERBOARD_MENU_GRID_COLUMN_NAMES[self.leaderboard_index]):
            if column_name == strings.LEADERBOARD_KDR:
                kdr_special_case_column_index = column_index
            column_name_width = self.grid.header_font.get_content_width(column_name)
            if column_name_width > widest_name_width:
                widest_name_width = column_name_width
                widest_name_column_index = column_index
            self.columns.append([column_name, 0, A13, False])

        column_width = widest_name_width + LEADERBOARD_MENU_GRID_COLUMN_TEXT_PADDING
        self.columns[0][1] = LEADERBOARD_MENU_GRID_COLUMN_RANK_WIDTH
        rank_column_header_width = self.grid.header_font.get_content_width(self.columns[0][0]) + LEADERBOARD_MENU_GRID_COLUMN_TEXT_PADDING
        if self.columns[0][1] < rank_column_header_width:
            self.columns[0][1] = rank_column_header_width
        self.columns[1][1] = LEADERBOARD_MENU_GRID_COLUMN_NAME_WIDTH
        self.grid.set_columns(self.columns)
        rows = []
        for leaderboard_row_index in xrange(0, len(self.leaderboard_data)):
            line = [
             str(self.leaderboard_data[leaderboard_row_index][4]),
             self.leaderboard_data[leaderboard_row_index][1],
             str(self.leaderboard_data[leaderboard_row_index][2][1])]
            deaths = None
            kills = None
            for scoreReason in A871[self.leaderboard_index][A870]:
                stat = str(self.leaderboard_data[leaderboard_row_index][3].get(str(scoreReason), [0, 0])[1])
                if stat:
                    line.append(stat)
                    if scoreReason == A816:
                        deaths = stat
                    elif scoreReason == A597:
                        kills = stat
                else:
                    line.append('-')

            if kdr_special_case_column_index != None and kills != None and deaths != None:
                if deaths == 0:
                    deaths = 1
                line[kdr_special_case_column_index] = ('{0:.3f}').format(round(float(kills) / float(deaths), 3))
            grid_row = LeaderboardListItem(leaderboard_row_index)
            grid_row.set_columns(line)
            rows.append(grid_row)

        self.grid.populate(rows)
        self.grid.on_scroll(0, silent=True)
        return

    def navigation_button_pressed(self, navigation_button):
        if navigation_button == NAVBAR_LEFT:
            self.go_back()

    def go_back(self):
        from selectMenu import SelectMenu
        if self.media:
            self.media.play('menu_backA', zone=HUD_AUDIO_ZONE)
        self.parent.set_menu(SelectMenu, back=True)

    def draw(self):
        noof_items_for_scrollbar = 0
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        global_images.leaderboard_frame.blit(LEADERBOARD_MENU_SCREEN_CENTER_X, LEADERBOARD_MENU_SCREEN_CENTER_Y)
        draw_text_with_alignment_and_size_validation(strings.LEADERBOARD, LEADERBOARD_MENU_TITLE_POSITION_X, LEADERBOARD_MENU_TITLE_POSITION_Y, LEADERBOARD_MENU_TITLE_WIDTH, LEADERBOARD_MENU_TITLE_HEIGHT, A1054, font=title_font, alignment_y='center')
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        self.navigation_bar.draw()
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        for element in self.elements:
            if element != self.navigation_bar:
                element.draw()

        if self.show_wait_msg:
            settings_font.draw(strings.CONNECTING_PLEASE_WAIT, LEADERBOARD_MENU_SCREEN_CENTER_X, LEADERBOARD_MENU_SCREEN_CENTER_Y, A1054, center=True)
# okay decompiling out\aoslib.scenes.frontend.LeaderboardMenu.pyc
