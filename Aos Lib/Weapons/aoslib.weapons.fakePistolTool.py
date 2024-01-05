# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.fakePistolTool
from tool import Tool
from aoslib.models import *
from . import TOOL_IMAGES
from shared.constants import *
from shared.glm import Vector3
from aoslib import image, strings

class FakePistolTool(Tool):
    name = ''
    model = [PISTOL_MODEL]
    view_model = [PISTOL_VIEW_MODEL]
    shoot_interval = 0.0
    pitch = 1.0
    image = None
    show_crosshair = A290
    draw_ammo = False

    def __init__(self, character):
        super(FakePistolTool, self).__init__(character)
        self.arms_position_offset = Vector3(0.0, 0.0, 0.0)
        self.equipped_tool_tip_text = None
        return
# okay decompiling out\aoslib.weapons.fakePistolTool.pyc
