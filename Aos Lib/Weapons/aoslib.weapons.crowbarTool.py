# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.crowbarTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.animations.animUseCrowbar import *
from aoslib import strings

class CrowbarTool(DiggingTool):
    name = strings.A330
    model = [CROWBAR_MODEL]
    model_size = 1.3 * A274 * 0.666
    view_model = [CROWBAR_VIEW_MODEL]
    image = TOOL_IMAGES[A330]
    shoot_interval = A1112
    damage = A1113
    damage_type = A400
    hit_player_sound = A2839
    hit_block_sound = A2840
    pitch_increase = 30

    def __init__(self, character):
        super(CrowbarTool, self).__init__(character)
        self.animations['use_crowbar'] = AnimUseCrowbar(self.shoot_interval)

    def use_primary(self):
        super(CrowbarTool, self).use_primary()
        self.animations['use_crowbar'].start()
        return self.use_spade(False)
# okay decompiling out\aoslib.weapons.crowbarTool.pyc
