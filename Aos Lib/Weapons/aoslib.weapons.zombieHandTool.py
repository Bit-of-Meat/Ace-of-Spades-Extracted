# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.zombieHandTool
from diggingTool import DiggingTool
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from shared.glm import Vector3
from aoslib.animations.animZombieHand import *
from aoslib import strings

class ZombieHandTool(DiggingTool):
    name = strings.ZOMBIE_HANDS
    model = [ZOMBIE_HAND_MODEL, ZOMBIE_HAND_LEFT_MODEL]
    model_scale = 0.5
    view_model = [ZOMBIE_HAND_VIEW_MODEL, ZOMBIE_HAND_VIEW_LEFT_MODEL]
    image = TOOL_IMAGES[A320]
    shoot_interval = A1115
    damage = A1116
    damage_type = A391
    use_team_color = True
    flash_with_spawn_protection = True
    hit_player_sound = A2802
    hit_block_sound = A2801
    miss_sound = A2800
    last_used_hand = 1
    draw_ammo = False
    pitch_increase = 200

    def __init__(self, character):
        super(ZombieHandTool, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.0, 0.0, -0.25)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, 0.0, 0.25)
        self.animations['zombie_hand'] = AnimZombieHand(self.shoot_interval)
        self.set_equipped_tool_tip_text(strings.EQUIPPED_TOOL_TIP_MELEE)

    def use_primary(self):
        super(ZombieHandTool, self).use_primary()
        self.last_used_hand += 1
        if self.last_used_hand >= len(self.model):
            self.last_used_hand = 0
        self.use_spade(False)
        self.animations['zombie_hand'].start()

    def apply_transform(self, model_index, apply_animation_position=True, apply_animation_orientation=True):
        if model_index == self.last_used_hand:
            super(ZombieHandTool, self).apply_transform(model_index, apply_animation_position=self.character is not None and self.character.main, apply_animation_orientation=True)
        else:
            super(ZombieHandTool, self).apply_transform(model_index, apply_animation_position=False, apply_animation_orientation=False)
        return

    def needs_player_arms_drawing(self):
        return False

    def use_spade(self, secondary_damage, damage_amount=None):
        temp_pitch = self.pitch
        super(ZombieHandTool, self).use_spade(secondary_damage, damage_amount)
        self.pitch = temp_pitch

    def update(self, dt):
        temp_pitch = self.pitch
        super(DiggingTool, self).update(dt)
        self.pitch = temp_pitch

    def get_arm_pitch_range(self):
        return super(DiggingTool, self).get_arm_pitch_range()
# okay decompiling out\aoslib.weapons.zombieHandTool.pyc
