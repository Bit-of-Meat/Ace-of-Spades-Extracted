# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.intelTool
from tool import Tool
from aoslib.models import *
from . import TOOL_IMAGES
from shared.constants import *
from shared.glm import Vector3
from aoslib import image, strings

class IntelTool(Tool):
    intel_icon = image.load('minimap_intel', center=True)
    name = strings.A326
    model = [INTEL_MODEL]
    view_model = [INTEL_VIEW_MODEL]
    shoot_interval = 0.0
    pitch = 1.0
    image = TOOL_IMAGES[A326]
    show_crosshair = A290
    carried = False
    draw_ammo = False
    use_other_team_color = True
    can_shoot_primary_while_sprinting = True

    def __init__(self, character):
        super(IntelTool, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.0, 0.18, 0.0)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, -0.18, 0.0)

    def use_primary(self):
        self.character.parent.drop_pickup(self.character.world_object.position, self.character.world_object.orientation * A2100, send_packet=self.character.main)
        self.carried = False

    def is_available(self):
        return self.carried

    def can_swap(self):
        return not self.carried

    def get_map_icon(self, viewer):
        return self.intel_icon
# okay decompiling out\aoslib.weapons.intelTool.pyc
