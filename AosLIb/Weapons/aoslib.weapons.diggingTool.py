# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.diggingTool
from tool import Tool
from aoslib.models import *
from aoslib.common import distance_3d, Vector3
from shared.common import distance_vector_3d
from aoslib.world import is_centered
from shared.constants import *
from aoslib import media
from aoslib.weapons import TOOL_IMAGES

class DiggingTool(Tool):
    name = 'nodiggity'
    pitch_initial = -4.0
    rotate_arm_ratio = 0.25
    show_crosshair = A293
    hit_player_sound = A2797
    hit_block_sound = A2795
    hit_wet_block_sound = A2796
    miss_sound = A2798
    animation_timer = 0

    def __init__(self, character):
        super(DiggingTool, self).__init__(character)
        self.ammo_image = TOOL_IMAGES[A301]
        self.animation_timer = self.shoot_interval
        self.pitch_from = self.pitch_to = self.pitch_initial

    def check_player_hit(self):
        character = self.character
        scene = character.scene
        world_object = character.world_object
        x, y, z = world_object.position.get()
        o_x, o_y, o_z = world_object.orientation.get()
        for player in scene.players.values():
            other = player.character
            if other is character or not other or not other.visible or other.dead:
                continue
            x2, y2, z2 = other.world_object.position.get()
            if not is_centered(x, y, z, o_x, o_y, o_z, x2, y2, z2 + 1, A993):
                continue
            if distance_3d(x, y, z, x2, y2, z2) > A1084:
                continue
            other.play_sound(self.hit_player_sound, zone=media.IN_WORLD_AUDIO_ZONE)
            other_pos = Vector3(x2, y2, z2)
            return True

        return False

    def use_spade(self, secondary_damage, damage_amount=None):
        character = self.character
        scene = character.scene
        world_object = character.world_object
        pitch_offset = max((self.character.pitch + self.pitch_increase - self.get_arm_pitch_range()[1], 0))
        self.pitch_from = self.pitch_initial + self.pitch_increase - pitch_offset
        self.pitch_to = self.pitch_initial - pitch_offset
        self.pitch = self.pitch_from
        self.animation_timer = 0
        self.play_sound(self.miss_sound, zone=media.IN_WORLD_AUDIO_ZONE)
        if character.main:
            damage = damage_amount if damage_amount is not None else self.damage
            scene.send_shoot_packet(self.character.parent, world_object.position, world_object.orientation, damage, 0, False, 0, secondary_damage)
        if self.check_player_hit():
            return True
        else:
            return

    def restock(self, type=None):
        self.update_ammo()

    def get_ammo(self):
        return (
         self.character.block_count, None)

    def get_arm_pitch_range(self):
        pitch_lower_limit, pitch_upper_limit = super(DiggingTool, self).get_arm_pitch_range()
        upper_limit_offset = 0 if self.animation_timer >= 0 and self.animation_timer < self.shoot_interval else -self.pitch_increase
        return (pitch_lower_limit, pitch_upper_limit + upper_limit_offset)

    def update(self, dt):
        temp_pitch = self.pitch
        super(DiggingTool, self).update(dt)
        self.pitch = temp_pitch
        if self.animation_timer >= 0 and self.animation_timer < self.shoot_interval:
            self.animation_timer = min((self.animation_timer + dt, self.shoot_interval))
            t = self.animation_timer / self.shoot_interval
            self.pitch = self.pitch_from + (self.pitch_to - self.pitch_from) * t
        else:
            self.pitch_from = self.pitch_initial
            self.pitch_to = self.pitch_initial
            self.pitch = self.pitch_initial
# okay decompiling out\aoslib.weapons.diggingTool.pyc
