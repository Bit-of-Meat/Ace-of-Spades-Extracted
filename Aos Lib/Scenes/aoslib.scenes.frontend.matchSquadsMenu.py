# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.matchSquadsMenu
from aoslib.scenes.frontend.baseSquadsMenu import *
from shared.steam import SteamEnumerateFriendLobbies, SteamEnumeratePublicLobbies, SteamGetLobbyMembers, SteamCreateLobby, SteamJoinLobby, SteamSetLobbyData, SteamGetPersonaName, SteamLeaveLobby, SteamRefreshLobbyData, SteamGetLobbyData, SteamActivateGameOverlayToStore, SteamAmITheLobbyOwner
from shared.constants_matchmaking import A2664
from aoslib.scenes.main.matchSettings import DEFAULT_MATCH_SETTINGS
import time
from shared.steam import game_version

class MatchSquadsMenu(BaseSquadsMenu):
    lobbyType = A2664
    title = strings.SQUAD_LIST
    create_button_text = strings.CREATE_SQUAD
    join_button_text = strings.JOIN_SQUAD
    available_lobbies_text = strings.AVAILABLE_SQUADS
    move_to_lobby = False

    def on_lobby_join_success(self, lobby_id):
        from aoslib.scenes.frontend.matchSquadLobbyMenu import MatchSquadLobbyMenu
        self.parent.set_menu(MatchSquadLobbyMenu)

    def lobby_created_callback(self, lobby_id):
        if not SteamAmITheLobbyOwner():
            return
        else:
            SteamSetLobbyData('Name', SteamGetPersonaName())
            SteamSetLobbyData('Version', str(game_version()))
            SteamSetLobbyData('LobbyType', str(self.lobbyType))
            SteamSetLobbyData('LobbyCreator', str(SteamGetLobbyOwner()))
            default_playlist = get_default_playlist()
            if default_playlist is not None:
                game_rules = ''
                SteamSetLobbyData('PlaylistID', str(default_playlist.id))
                SteamSetLobbyData('PLAYLIST', str(default_playlist.modes[0]))
                SteamSetLobbyData('UGC_MODES', str([]))
                map_rotation_name = sorted(default_playlist.map_names)[0]
                SteamSetLobbyData('MAP_ROTATION_FILENAME', map_rotation_name)
                SteamSetLobbyData('MAP_ROTATION_ORIGINAL_TITLE', map_rotation_name)
                SteamSetLobbyData('MAP_ROTATION_NEW_TITLE', map_rotation_name)
                SteamSetLobbyData('Custom_UGC_Map', 'False')
                teams = ['TEAM1', 'TEAM2']
                for team in teams:
                    SteamSetLobbyData(team, '0')

                SteamSetLobbyData('TEAM_NEUTRAL', '1')
                reset_all_game_rules()
            default_match_length = get_default_match_length_for_playlist_in_minutes(default_playlist.id)
            SteamSetLobbyData('MATCH_LENGTH', str(default_match_length))
            SteamSetLobbyData('MAX_PLAYERS', DEFAULT_MATCH_SETTINGS['MAX_PLAYERS'])
            self.manager.hosted_ugc_map_filename = ''
            time.sleep(0.1)
            self.move_to_lobby = True
            return

    def update(self, dt):
        super(MatchSquadsMenu, self).update(dt)
        if self.move_to_lobby:
            self.move_to_lobby = False
            from aoslib.scenes.frontend.matchSquadLobbyMenu import MatchSquadLobbyMenu
            self.parent.set_menu(MatchSquadLobbyMenu)

    def open_parent_menu(self):
        from joinMatchMenu import JoinMatchMenu
        self.parent.set_menu(JoinMatchMenu, back=True)
# okay decompiling out\aoslib.scenes.frontend.matchSquadsMenu.pyc
