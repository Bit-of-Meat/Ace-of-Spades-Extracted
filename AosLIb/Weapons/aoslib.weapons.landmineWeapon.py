# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.landmineWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from aoslib.shaders import *
from aoslib.draw import DisplayList
from pyglet.gl import *
from shared.constants import *
from aoslib import strings
from aoslib.animations.animPlaceBlock import *
ghost_landmine = DisplayList(LANDMINE_VIEW_MODEL)
ghost_landmine.size = 0.06

class LandmineWeapon(Weapon):
    name = strings.A316
    damage = None
    sight = None
    shoot_sound = None
    model = [LANDMINE_MODEL]
    view_model = [LANDMINE_VIEW_MODEL]
    tracer = None
    ammo = (A1792, A1793, None, None, A1794)
    shoot_interval = A1795
    ghost_position = None
    image = TOOL_IMAGES[A316]

    def __init__(self, character):
        super(LandmineWeapon, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.0, 0.18, 0.0)
                self.initial_orientation[model_index] = Vector3(0.0, 70.0, 0.0)
                self.reset_position(model_index)
                self.reset_orientation(model_index)

        self.arms_position_offset = Vector3(0.0, -0.18, 0.0)
        self.animations['place_block'] = AnimPlaceBlock(self.shoot_interval)

    def shoot(self, fp3, seed):
        if not self.character.main:
            return False
        if not self.ghost_position:
            self.play_sound(A2827)
            return False
        self.character.scene.send_place_landmine(self.ghost_position)
        self.animations['place_block'].start()
        return True

    def draw_ghosting(self):
        self.ghost_position = None
        can_place_landmine, ret = self.character.scene.can_place_object(self.character, A1806, player_min_radius=0, entity_min_radius=1, others_min_radius=0, can_place_vertical=False)
        if not can_place_landmine:
            return
        else:
            position, face = ret
            if not A1810 and position.z > A2215:
                return
            self.ghost_position = position.get()
            glPushMatrix()
            glTranslatef(position.x + 0.5, -position.z, position.y + 0.5)
            MODEL_SHADER.bind()
            MODEL_SHADER.uniformf_loc(MODEL_SHADER_BLEND_COLOR_LOC, 1.0, 1.0, 1.0, 0.3)
            ghost_landmine.draw(frustum_check=False)
            MODEL_SHADER.uniformf_loc(MODEL_SHADER_BLEND_COLOR_LOC, 1.0, 1.0, 1.0, 1.0)
            MODEL_SHADER.unbind()
            glPopMatrix()
            return

    def is_available(self):
        return self.get_ammo()[0] > 0
# okay decompiling out\aoslib.weapons.landmineWeapon.pyc
