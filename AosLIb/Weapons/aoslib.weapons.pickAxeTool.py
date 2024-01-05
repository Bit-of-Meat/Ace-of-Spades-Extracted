# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.pickAxeTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.animations.animUsePickAxe import *
from aoslib import strings

class PickAxeTool(DiggingTool):
    name = strings.PICKAXE
    model = [PICKAXE_MODEL]
    view_model = [PICKAXE_VIEW_MODEL]
    image = TOOL_IMAGES[A296]
    shoot_interval = A1103
    damage = A1104
    damage_type = A374
    hit_player_sound = A2830
    hit_block_sound = A2829
    pitch_increase = 30

    def __init__(self, character):
        super(PickAxeTool, self).__init__(character)
        self.animations['use_pickaxe'] = AnimUsePickAxe(self.shoot_interval)
        self.set_equipped_tool_tip_text(strings.EQUIPPED_TOOL_TIP_MELEE)

    def use_primary(self):
        super(PickAxeTool, self).use_primary()
        self.animations['use_pickaxe'].start()
        return self.use_spade(False)
# okay decompiling out\aoslib.weapons.pickAxeTool.pyc
