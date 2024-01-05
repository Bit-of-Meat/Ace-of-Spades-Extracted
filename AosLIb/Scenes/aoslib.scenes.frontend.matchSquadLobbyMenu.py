# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.matchSquadLobbyMenu
from aoslib.scenes.frontend.baseSquadLobbyMenu import *
from shared.steam import SteamGetLobbyMembers, SteamGetCurrentLobby, SteamGetFriendPersonaName, SteamGetPersonaName, SteamShowInviteFriendOverlay, SteamLeaveLobby, SteamGetLobbyOwner, SteamAmITheLobbyOwner, SteamSetLobbyData, SteamSetLobbyMemberData, SteamGetLobbyData, SteamGetLobbyMemberData, SteamSendChatMessage, SteamSetLobbyGameServer, SteamGetLobbyGameServer, SteamClearLobbyGameServer, GetUserSteamID

class MatchSquadLobbyMenu(BaseSquadLobbyMenu):
    title = strings.MATCH_LOBBY
    settings_title = strings.MATCH_SETTINGS

    def initialize(self, ugc=False):
        super(MatchSquadLobbyMenu, self).initialize(ugc)

    def on_start(self, *arg, **kw):
        super(MatchSquadLobbyMenu, self).on_start(arg, kw)
        self.match_settings_panel.enable_privacy_type = True
        self.match_settings_panel.enable_match_length = True
        self.match_settings_panel.enable_game_rules = True
        self.match_settings_panel.enable_map_rotation = True
        self.match_settings_panel.enable_max_players = True
        self.match_settings_panel.enable_playlist = True
        self.match_settings_panel.enable_ugc_mode = False
        self.match_settings_panel.populate_match_settings_list()
        self.original_lobby_owner = SteamAmITheLobbyOwner()

    def open_parent_menu(self):
        if SteamAmITheLobbyOwner():
            self.on_cancel_game()
        SteamLeaveLobby()
        self.lobby_id = None
        if not self.original_lobby_owner:
            from aoslib.scenes.frontend.matchSquadsMenu import MatchSquadsMenu
            self.parent.set_menu(MatchSquadsMenu, back=True)
        else:
            from selectMenu import SelectMenu
            self.parent.set_menu(SelectMenu, back=True)
        return
# okay decompiling out\aoslib.scenes.frontend.matchSquadLobbyMenu.pyc
