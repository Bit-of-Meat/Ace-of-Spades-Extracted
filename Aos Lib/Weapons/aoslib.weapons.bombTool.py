# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.bombTool
from tool import Tool
from aoslib.models import *
from . import TOOL_IMAGES
from shared.constants import *
from shared.glm import Vector3
from aoslib import image, strings
import random, aoslib.images as aosimages

class BombTool(Tool):
    bomb_icon = image.load('minimap_bomb', center=True)
    name = strings.A321
    model = [BOMB_MODEL]
    view_model = [BOMB_VIEW_MODEL]
    shoot_interval = 0.0
    pitch = 1.0
    image = TOOL_IMAGES[A321]
    show_crosshair = A290
    carried = False
    draw_ammo = False
    can_shoot_primary_while_sprinting = True
    smoke_timer = None

    def __init__(self, character):
        super(BombTool, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.0, 0.18, 0.0)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, -0.18, 0.0)
        self.bomb_icon.scale = 1.0

    def use_primary(self):
        self.character.parent.drop_pickup(self.character.world_object.position, self.character.world_object.orientation * A2098, send_packet=self.character.main)
        self.carried = False

    def is_available(self):
        return self.carried

    def can_swap(self):
        return not self.carried

    def get_map_icon(self, viewer):
        return self.bomb_icon

    def update(self, dt):
        super(BombTool, self).update(dt)
        smoke_spawn_interval = 1 / A2148 if A2148 != 0 else 0
        if smoke_spawn_interval > 0:
            self.smoke_timer += dt
            forward = self.character.world_object.orientation
            right = forward.cross(Vector3(0, 0, -1)).norm()
            up = right.cross(forward).norm()
            forward_magnitude = 0
            right_magnitude = 0
            up_magnitude = 0
            if self.character.main:
                forward_magnitude += A2155
                right_magnitude += A2156
                up_magnitude += A2157
                base_position = self.character.interpolated_position
            else:
                forward_magnitude += A2158
                right_magnitude += A2159
                up_magnitude += A2160
                base_position = self.character.world_object.position + Vector3(0, 0, A245)
            if self.fps_position_offset is not None:
                right_magnitude += -self.fps_position_offset[0]
                up_magnitude += self.fps_position_offset[1]
                forward_magnitude += self.fps_position_offset[2]
            offset_forward = forward * forward_magnitude
            offset_right = right * right_magnitude
            offset_up = up * up_magnitude
            offset_position = base_position + offset_forward + offset_right + offset_up
            while self.smoke_timer >= smoke_spawn_interval:
                self.create_fuse_fx(offset_position)
                self.smoke_timer -= smoke_spawn_interval

        return

    def on_set(self):
        super(BombTool, self).on_set()
        self.smoke_timer = 0

    def create_fuse_fx(self, spawn_position):
        smoke_size = random.uniform(A2151, A2152)
        smoke_rotation = random.randint(160, 200)
        smoke_speed = random.uniform(A2153, A2154)
        smoke_dir = Vector3(0, 0, 1)
        smoke_velocity = smoke_dir * smoke_speed
        self.character.scene.particle_effect_manager.create_particle_effect_with_lut(image=aosimages.particle_smoke_trail, lut_image=aosimages.particle_smoke_lut, position=spawn_position, velocity=smoke_velocity, color=(255,
                                                                                                                                                                                                                            255,
                                                                                                                                                                                                                            255), numparticles=1, size=smoke_size, initial_rotation=smoke_rotation, rotation_speed=0, needs_collision=False, decay_rate=A2149, lifetime=A2150, start_frame=1, num_frames_x=8, num_frames_y=8, forward_animate=1, loop=0, framerate=30, needs_gravity=False)
# okay decompiling out\aoslib.weapons.bombTool.pyc
