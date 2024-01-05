# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.flareBlockTool
from aoslib.models import *
from . import TOOL_IMAGES
from shared.constants import *
from aoslib import media, strings
from blockToolCommon import BlockToolCommon
from aoslib.animations.animPlaceBlock import *
import math

class FlareBlockTool(BlockToolCommon):
    name = strings.FLARE_BLOCK_TOOL
    model = [BLOCK_MODEL]
    view_model = [BLOCK_VIEW_MODEL]
    shoot_interval = 0.5
    pitch = 1.0
    image = TOOL_IMAGES[A318]
    show_crosshair = A293
    use_color = True

    def __init__(self, character):
        super(FlareBlockTool, self).__init__(character)
        self.ammo_image = TOOL_IMAGES[A301]
        self.block_cost = A2258
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(-0.04, 0.0, 0.3)
                self.initial_orientation[model_index] = Vector3(0.0, 45.0, 0.0)
                self.reset_position(model_index)
                self.reset_orientation(model_index)

        self.arms_position_offset = Vector3(0.04, 0.0, -0.3)
        self.animations['place_block'] = AnimPlaceBlock(self.shoot_interval)

    def use_primary(self):
        super(FlareBlockTool, self).use_primary()
        character = self.character
        if character.main:
            if not self.valid_placement or not self.hit_cube or not self.get_has_enough_ammo():
                self.play_sound(A2827)
                return False
            character.scene.send_place_flare_block(self.hit_cube.x, self.hit_cube.y, self.hit_cube.z)
            player = character.parent
            if player and player.team and not player.team.infinite_blocks:
                character.block_count -= A2258
            self.update_ammo()
        elif not self.valid_placement or not self.hit_cube:
            return False
        character.scene.media.play(A2828, pos=(self.hit_cube.x, self.hit_cube.y, self.hit_cube.z))
        if character.main:
            self.valid_placement = False
            self.hit_cube = None
        self.animations['place_block'].start()
        return

    def is_available(self):
        return True

    def on_set(self):
        if self.character.main:
            self.character.scene.hud.palette.active = self.character.scene.manager.enable_colour_palette
            self.update_ammo()

    def get_has_enough_ammo(self):
        player = self.character.parent
        return self.character.block_count >= A2258 or player and player.team and player.team.infinite_blocks

    def on_unset(self):
        if self.character.main:
            self.character.scene.hud.palette.active = False
            self.hit_cube = old_hit_cube = None
            self.valid_placement = False
        super(FlareBlockTool, self).on_unset()
        return

    def update_ammo(self):
        super(FlareBlockTool, self).update_ammo()
# okay decompiling out\aoslib.weapons.flareBlockTool.pyc
