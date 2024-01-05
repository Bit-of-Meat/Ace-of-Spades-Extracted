# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.gfx.particleEffectManager
from shared.glm import Vector3
import sys, aoslib.images as aosimages
from aoslib.draw import create_billboards, update_billboards, create_particles, use_particles_for_effect, update_particles, set_particle_gravity, use_lut_particles_for_effect, set_new_map_for_particles, reload_particle_textures
from shared.constants import A2324
import math, random
MAX_ROTATION = 360

class ParticleEffectManager:

    def __init__(self, scene, max_particles_proportion):
        self.scene = scene
        create_billboards()
        create_particles(max_particles_proportion)

    def recreate_particle_pool(self, max_particles_proportion):
        create_particles(max_particles_proportion)

    def recreate_billboard_pool(self):
        create_billboards()

    def reload_particle_textures(self):
        reload_particle_textures()

    def set_map(self, map):
        set_new_map_for_particles(map)

    def set_particles_gravity(self, gravity):
        set_particle_gravity(gravity)

    def create_particle_effect(self, image, position, velocity, color, numparticles, explode_velocity=0, size=2.0, initial_rotation=180, rotation_speed=0, needs_collision=True, decay_rate=1.0, lifetime=2.0, start_frame=0, num_frames_x=8, num_frames_y=8, forward_animate=random.randint(0, 1), loop=1, framerate=30, needs_gravity=True, alpha_blend_mode=A2324, spawn_idx=-1):
        if self.scene.manager.showing_loading_screen:
            return
        else:
            if image == None:
                image = aosimages.particle_tumbling_cube
            if len(color) == 3:
                color = color + (int(255),)
            use_particles_for_effect(numparticles, position, velocity, color, explode_velocity, size, initial_rotation, rotation_speed, decay_rate, lifetime, needs_collision, needs_gravity, image, start_frame, num_frames_x, num_frames_y, forward_animate, loop, framerate, alpha_blend_mode, spawn_idx)
            return

    def create_particle_effect_with_lut(self, image, lut_image, position, velocity, color, numparticles, explode_velocity=0, size=2.0, initial_rotation=180, rotation_speed=0, needs_collision=True, decay_rate=1.0, lifetime=2.0, start_frame=0, num_frames_x=8, num_frames_y=8, forward_animate=random.randint(0, 1), loop=1, framerate=30, needs_gravity=True, alpha_blend_mode=A2324, spawn_idx=-1):
        if self.scene.manager.showing_loading_screen:
            return
        else:
            if image == None:
                image = aosimages.particle_tumbling_cube
            if lut_image == None:
                lut_image = aosimages.particle_lut_image
            if len(color) == 3:
                color = color + (int(255),)
            use_lut_particles_for_effect(numparticles, position, velocity, color, explode_velocity, size, initial_rotation, rotation_speed, decay_rate, lifetime, needs_collision, needs_gravity, image, lut_image, start_frame, num_frames_x, num_frames_y, forward_animate, loop, framerate, alpha_blend_mode, spawn_idx)
            return

    def update(self, dt):
        update_particles(dt)
        update_billboards(dt)
# okay decompiling out\aoslib.gfx.particleEffectManager.pyc
