# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.zombiePrefabTool
from prefabTool import PrefabTool
from aoslib.models import *
from shared.constants import *
from shared.glm import Vector3
from aoslib import strings

class ZombiePrefabTool(PrefabTool):
    name = strings.A319
    model = [ZOMBIE_HAND_MODEL, BLOCK_MODEL, ZOMBIE_HAND_LEFT_MODEL]
    view_model = [ZOMBIE_HAND_VIEW_MODEL, BLOCK_VIEW_MODEL]

    def __init__(self, character):
        super(ZombiePrefabTool, self).__init__(character)
        if self.character.main:
            self.initial_orientation[0] = Vector3(0.0, 0.0, 180.0)
            self.reset_orientation(0)
            self.initial_orientation[1] = Vector3(0.0, 45.0, 30.0)
            self.reset_orientation(1)
            self.initial_position[0] = Vector3(0.0, 0.0, 0.0)
            self.reset_position(0)
            self.initial_position[1] = Vector3(0.0, 0.2, 0.8)
            self.reset_position(1)

    def needs_player_arms_drawing(self):
        return False
# okay decompiling out\aoslib.weapons.zombiePrefabTool.pyc
