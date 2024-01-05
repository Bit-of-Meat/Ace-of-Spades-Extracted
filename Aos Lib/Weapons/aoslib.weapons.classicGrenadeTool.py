# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.classicGrenadeTool
from grenadeTool import GrenadeTool
from aoslib.models import *
from shared.constants import *
from . import TOOL_IMAGES
from aoslib import media, strings
from aoslib.animations.animThrowGrenade import *

class ClassicGrenadeTool(GrenadeTool):
    name = strings.CLASSIC_GRENADE
    shoot_interval = A2061
    fuse = A2063
    default_count = A2058
    initial_count = A2059
    restock_amount = A2060
    image = TOOL_IMAGES[A327]
    show_crosshair = A294
    show_crosshair_centre = True
    accuracy_spread_min = A2070
    accuracy_spread = accuracy_spread_min
    accuracy_spread_max = accuracy_spread_min + A2071
    accuracy_spread_increase_per_shot = A2072
    accuracy_spread_reduction_speed = A2073
    max_fuse = A2063

    def __init__(self, character):
        super(ClassicGrenadeTool, self).__init__(character)
        self.set_equipped_tool_tip_text(strings.EQUIPPED_TOOL_TIP_GRENADE)

    def throw(self, fuse):
        if self.character and self.character.main:
            self.character.throw_grenade(fuse, classic=True)
# okay decompiling out\aoslib.weapons.classicGrenadeTool.pyc
