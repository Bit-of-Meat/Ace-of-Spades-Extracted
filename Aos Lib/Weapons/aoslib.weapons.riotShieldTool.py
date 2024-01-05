# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.riotShieldTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.animations.animUseRiotShield import *
from aoslib import strings

class RiotShieldTool(DiggingTool):
    name = strings.RIOTSHIELD
    model = [RIOTSHIELD_MODEL]
    view_model = [RIOTSHIELD_VIEW_MODEL]
    model_size = 0.073
    view_model_size = 0.18
    image = TOOL_IMAGES[A348]
    shoot_interval = A1881
    damage = A1882
    damage_type = A410
    hit_player_sound = A2858
    hit_block_sound = A2856
    miss_sound = A2951
    pitch_increase = 10

    def __init__(self, character):
        super(RiotShieldTool, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.45, -0.6, -0.2)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.05, -0.03, 0.05)
        self.animations['use_riotshield'] = AnimUseRiotShield(self.shoot_interval)

    def use_primary(self):
        super(RiotShieldTool, self).use_primary()
        self.animations['use_riotshield'].start()
        return self.use_spade(False)

    def get_arm_pitch_range(self):
        return (
         A1886, A1887)
# okay decompiling out\aoslib.weapons.riotShieldTool.pyc
