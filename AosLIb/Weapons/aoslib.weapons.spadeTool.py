# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.spadeTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.animations.animUseSpade import *
from aoslib import strings

class SpadeTool(DiggingTool):
    name = strings.SPADE
    model = [SPADE_MODEL]
    view_model = [SPADE_VIEW_MODEL]
    shoot_interval = A1093
    secondary_shoot_interval = 1.0
    delay_secondary = True
    image = TOOL_IMAGES[A298]
    damage = A1094
    damage_type = A376
    pitch_increase = 40

    def __init__(self, character):
        super(SpadeTool, self).__init__(character)
        self.animations['use_spade'] = AnimUseSpade(self.shoot_interval)
        self.set_equipped_tool_tip_text(strings.EQUIPPED_TOOL_TIP_MELEE)

    def use_primary(self):
        super(SpadeTool, self).use_primary()
        self.animations['use_spade'].start()
        return self.use_spade(False)
# okay decompiling out\aoslib.weapons.spadeTool.pyc
