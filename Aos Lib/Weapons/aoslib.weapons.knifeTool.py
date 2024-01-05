# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.knifeTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.animations.animUseKnife import *
from aoslib import strings

class KnifeTool(DiggingTool):
    name = strings.KNIFE
    model = [KNIFE_MODEL]
    view_model = [KNIFE_VIEW_MODEL]
    model_size = 0.03
    view_model_size = 0.025
    image = TOOL_IMAGES[A297]
    shoot_interval = A1109
    damage = A1110
    damage_type = A375
    hit_player_sound = A2833
    hit_block_sound = A2831
    pitch_increase = 50

    def __init__(self, character):
        super(KnifeTool, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(-0.05, 0.03, -0.05)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.05, -0.03, 0.05)
        self.animations['use_knife'] = AnimUseKnife(self.shoot_interval)

    def use_primary(self):
        super(KnifeTool, self).use_primary()
        self.animations['use_knife'].start()
        return self.use_spade(False)
# okay decompiling out\aoslib.weapons.knifeTool.pyc
