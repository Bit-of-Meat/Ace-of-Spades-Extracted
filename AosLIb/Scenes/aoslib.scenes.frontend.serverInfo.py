# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.serverInfo
from aoslib.tools import make_server_identifier
from aoslib import strings
from shared.constants_gamemode import A2441, A2450, A2448
from shared.constants import A2362, A2361
from shared.steam import game_version

class ServerInfo(object):

    def __init__(self, name, ip, port, queryPort, ping, map, mode, num_players, max_players, tags, time_last_played):
        self.count = num_players
        self.max = max_players
        self.name = name
        self.ping = ping / 1000.0
        self.map = map
        self.mode_tla = mode
        self.time_last_played = time_last_played
        try:
            self.mode_id = A2450[self.mode_tla]
        except KeyError:
            self.mode_tla = 'tdm'
            self.mode_id = A2441

        self.identifier = make_server_identifier(ip, port)
        self.texture_skin = None
        for tag in tags:
            if tag[:5] == 'skin=':
                self.texture_skin = tag[5:]
                break

        self.region = ''
        for tag in tags:
            if tag[:7] == 'region=':
                self.region = tag[7:]
                break

        if 'classic' in tags:
            mode = 'c' + mode
        try:
            game_mode_title = A2448[mode]
        except:
            game_mode_title = 'TDM_TITLE'

        self.game_mode = strings.get_by_id(game_mode_title)
        self.identifier = make_server_identifier(ip, port)
        splitted = self.identifier.split(':')
        self.ip = splitted[0]
        self.ipn = ip
        self.port = port
        self.queryPort = queryPort
        self.tags = tags
        self.beta = True if 'beta' in tags else False
        self.monitor = True if 'monitor' in tags else False
        self.classic = A2362 if 'classic' in tags else A2361
        client_version = 'v%d' % game_version()
        self.is_matching_version = True if tags[0] == client_version else False
        if tags[1].startswith('playlist='):
            id, num = tags[1].split('=')
            self.playlist_id = num
        else:
            self.playlist_id = 0
        return
# okay decompiling out\aoslib.scenes.frontend.serverInfo.pyc
