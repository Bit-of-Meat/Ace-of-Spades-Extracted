# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.ugcSuperSpadeTool
from superSpadeTool import SuperSpadeTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib import strings

class UGCSuperSpadeTool(SuperSpadeTool):
    name = strings.UGC_SUPERSPADE
    model = [UGC_SUPERSPADE_MODEL]
    view_model = [UGC_SUPERSPADE_VIEW_MODEL]
    shoot_interval = A1099
    secondary_shoot_interval = A1099
    delay_secondary = False
    image = TOOL_IMAGES[A341]
    damage = A1100
    secondary_damage = A1101
    damage_type = A403
    hit_block_sound = A2799
    has_secondary = True

    def use_secondary(self):
        super(UGCSuperSpadeTool, self).use_secondary()
        self.animations['use_spade'].start()
        return self.use_spade(True)

    hit_block_sound = A2799
# okay decompiling out\aoslib.weapons.ugcSuperSpadeTool.pyc
