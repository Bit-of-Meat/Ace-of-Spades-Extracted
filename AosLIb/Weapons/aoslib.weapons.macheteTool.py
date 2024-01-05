# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.macheteTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.animations.animUseMachete import *
from aoslib import strings

class MacheteTool(DiggingTool):
    name = strings.MACHETE
    model = [MACHETE_MODEL]
    view_model = [MACHETE_VIEW_MODEL]
    model_size = 0.03
    view_model_size = 0.025
    image = TOOL_IMAGES[A346]
    shoot_interval = A1857
    damage = A1858
    damage_type = A409
    hit_player_sound = A2855
    hit_block_sound = A2853
    miss_sound = A2956
    pitch_increase = 50

    def __init__(self, character):
        super(MacheteTool, self).__init__(character)
        self.arms_position_offset = Vector3(0.0, 0.03, -0.05)
        self.animations['use_machete'] = AnimUseMachete(self.shoot_interval)

    def use_primary(self):
        super(MacheteTool, self).use_primary()
        self.animations['use_machete'].start()
        return self.use_spade(False)
# okay decompiling out\aoslib.weapons.macheteTool.pyc
