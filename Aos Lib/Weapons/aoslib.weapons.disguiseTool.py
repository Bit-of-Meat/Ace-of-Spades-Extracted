# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.disguiseTool
from tool import Tool
from aoslib.models import *
from shared.constants import *
from . import TOOL_IMAGES
from shared.glm import Vector3
from aoslib import media, strings

class DisguiseTool(Tool):
    name = strings.DISGUISE
    model = [DISGUISE_MODEL]
    view_model = [DISGUISE_VIEW_MODEL]
    shoot_interval = A2004
    has_secondary = False
    default_count = A2001
    initial_count = A2002
    restock_amount = A2003
    image = TOOL_IMAGES[A360]
    show_crosshair = A293
    show_crosshair_centre = True
    use_color = True
    model_size = 0.022
    view_model_size = 0.02

    def __init__(self, character):
        super(DisguiseTool, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(-0.1, 0.0, 0.05)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, 0.01, 0.0)

    def use_primary(self):
        if self.get_has_enough_ammo() and not self.character.parent.disguise_active:
            super(DisguiseTool, self).use_primary()
            self.character.shoot_primary = False
            if self.character.main:
                self.count -= 1
                self.update_ammo()
                self.character.scene.send_activate_disguise()

    def is_available(self):
        return self.count > 0

    def get_has_enough_ammo(self):
        return self.is_available()

    def use_custom(self):
        character = self.character
        if not character.scene.manager.enable_colour_picker:
            return False
        else:
            character.fire_secondary = False
            player = character.world_object
            max_block_distance = A1017 if not character.scene.manager.classic else A1012
            hit_scenery = character.scene.world.hitscan_accurate(player.position, player.orientation, max_block_distance)
            if hit_scenery is None:
                return False
            position, hit_block, face = hit_scenery
            if hit_block.z > A2215:
                return False
            solid, color = character.scene.map.get_point(hit_block.x, hit_block.y, hit_block.z)
            r, g, b, a = color
            self.set_block_color((r, g, b))
            character.pullout = 0.5
            palette = character.scene.hud.palette
            if palette is not None:
                palette.hide_selection()
            return

    def set_block_color(self, color):
        self.character.set_block_color(color)
# okay decompiling out\aoslib.weapons.disguiseTool.pyc
