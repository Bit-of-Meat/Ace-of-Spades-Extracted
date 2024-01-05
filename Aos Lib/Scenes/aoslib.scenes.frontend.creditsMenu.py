# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.creditsMenu
import time
from aoslib.scenes import MenuScene
from aoslib.text import welcome_font, get_fitting_lines, load_font, draw_text_lines, draw_text_with_size_validation, big_button_aldo_font, credits_text_font
from aoslib.gui import TextButton, NavigationBar, Label, NAVBAR_LEFT
from aoslib.images import global_images
from pyglet import gl
from aoslib import strings
from shared.steam import SteamShowAchievements, SteamActivateGameOverlayToStore
from aoslib.media import HUD_AUDIO_ZONE
from shared.constants import *
from joiningGameMenu import JoiningGameMenu
from shared.hud_constants import *
from aoslib.gui import VerticalScrollBar
from aoslib.text import map_info_font

class CreditsMenu(MenuScene):

    def initialize(self):
        self.elements = []
        from aoslib.gamemanager import GameManager
        if GameManager.invalid_data_error:
            self.manager.set_big_text_message(A952, False, 600.0)
        self.navigation_bar = NavigationBar(x=CREDITS_MENU_BACK_BUTTON_POSITION_X, y=CREDITS_MENU_BACK_BUTTON_POSITION_Y, width=CREDITS_MENU_BACK_BUTTON_WIDTH, height=CREDITS_MENU_BACK_BUTTON_HEIGHT, middle_button=False, right_button=False, left_button=False)
        self.navigation_bar.add_left_button(strings.BACK)
        self.navigation_bar.add_handler(self.navigation_button_pressed)
        self.elements.append(self.navigation_bar)
        credits_text = ''
        width = 967
        self.text_x = CREDITS_MENU_CREDITS_FRAME_POSITION_X - width * 0.5 + CREDITS_MENU_CREDITS_FRAME_SPACING_TO_TEXT + LIST_PANEL_SPACING
        self.text_width = width - CREDITS_MENU_CREDITS_FRAME_SPACING_TO_TEXT * 2 - LIST_PANEL_SPACING * 3 - CREDITS_MENU_SCROLLBAR_WIDTH
        self.text_y = CREDITS_MENU_CREDITS_TEXT_Y
        self.text_height = CREDITS_MENU_CREDITS_TEXT_HEIGHT
        self.lines, self.fitting_lines = get_fitting_lines(credits_text, self.text_width, self.text_height, credits_text_font, CREDITS_MENU_CREDITS_TEXT_LINE_SPACING)
        self.noof_visible_lines = len(self.fitting_lines)
        self.scrollbar = VerticalScrollBar(x=self.text_x + self.text_width + LIST_PANEL_SPACING * 2, y=self.text_y - self.text_height, width=CREDITS_MENU_SCROLLBAR_WIDTH, height=self.text_height, max_lines=len(self.lines), noof_visible_lines=self.noof_visible_lines)
        self.scrollbar.add_on_scrolled_handler(self.on_scroll)
        self.on_scroll(0, silent=True)
        self.scrollbar.set_scroll(0)
        self.elements.append(self.scrollbar)

    def on_scroll(self, value, silent=False):
        self.fitting_lines = self.lines[int(value):min(int(value) + self.noof_visible_lines, len(self.lines))]

    def on_start(self):
        if not self.media.is_playing_music('mainmenu'):
            self.media.play_music('mainmenu', self.config.music_volume)
        self.on_scroll(0, silent=True)
        self.scrollbar.set_scroll(0)

    def navigation_button_pressed(self, navigation_button):
        if navigation_button == NAVBAR_LEFT:
            from selectMenu import SelectMenu
            self.parent.set_menu(SelectMenu, back=True)

    def update(self, dt):
        super(CreditsMenu, self).update(dt)

    def draw(self):
        draw_text_with_size_validation(strings.CREDITS_BUTTON, 275, 480, 250, 50, A1054, font=big_button_aldo_font)
        draw_text_lines(lines=self.fitting_lines, x=self.text_x, y=self.text_y - LIST_PANEL_SPACING * 2, width=self.text_width, height=self.text_height, font_to_use=credits_text_font, line_spacing=CREDITS_MENU_CREDITS_TEXT_LINE_SPACING, color=CREDITS_MENU_CREDITS_TEXT_COLOR, horizontal_alignment=CREDITS_MENU_CREDITS_TEXT_ALIGNMENT)
        for element in self.elements:
            element.draw()
# okay decompiling out\aoslib.scenes.frontend.creditsMenu.pyc
