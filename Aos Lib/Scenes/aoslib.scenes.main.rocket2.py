# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.rocket2
from drawItem import DrawItem
from entity import Entity
from aoslib.world import GenericMovement
from aoslib.draw import DisplayList, create_particle_spawn_point
from shared.glm import Vector3
from aoslib.shaders import *
from aoslib.models import *
from aoslib.common import to_pitch_yaw
from aoslib import media
import aoslib.images as aosimages
from aoslib.common import to_pitch_yaw
from shared.constants import *
import random

class Rocket2(Entity):
    name = 'Rocket2'
    icon = None
    size = 0.02
    model = [ROCKET2_MODEL]
    model_position_offsets = []
    shoot_sound_played = True

    def __init__(self, scene, *arg, **kw):
        super(Rocket2, self).__init__(scene, *arg, **kw)
        self.world_object = self.scene.world.create_object(GenericMovement, Vector3(0, 0, 0), Vector3(0, 0, 0) * A1420)
        self.world_object.set_gravity_multiplier(A1421)
        self.world_object.set_bouncing(False)
        self.world_object.set_stop_on_collision(False)
        self.pitch, self.yaw = to_pitch_yaw(*Vector3(0, 0, 0).get())
        self.sound = self.scene.media.play('rocket_trip_projectile', pos=(0, 0, 0), loops=0, zone=media.IN_WORLD_AUDIO_ZONE)
        self.flame_dt = self.smoke_dt = 0.0

    def update(self, dt):
        scene = self.scene
        self.world_object.update(dt, None)
        pos = self.world_object.position
        if self.sound:
            self.sound.set_position(*pos.get())
        self.pitch, self.yaw = to_pitch_yaw(*self.world_object.velocity.norm().get())
        self.display[0].set_rotation(0.0, self.yaw + 180, 0.0)
        self.display[0].add_rotation(-self.pitch, 0.0, 0.0)
        v_x, v_y, v_z = self.world_object.velocity.x, self.world_object.velocity.y, self.world_object.velocity.z
        smoke_velocity = Vector3(v_x, v_y, v_z).norm() * (dt * A1420) * 0.005
        smoke_velocity.x *= A2179 + random.uniform(A2180, A2181)
        smoke_velocity.y *= A2179 + random.uniform(A2180, A2181)
        smoke_velocity.z *= A2179 + random.uniform(A2180, A2181)
        smoke_pos = Vector3(pos.x, pos.y, pos.z)
        smoke_pos.z += 0.5
        smoke_decay = random.randint(0, A2188) - A2187
        if smoke_decay == 0:
            smoke_decay = A2189
        self.scene.particle_effect_manager.create_particle_effect(aosimages.particle_smoke_trail, smoke_pos, smoke_velocity, (255,
                                                                                                                              255,
                                                                                                                              255), 1, 0.0, random.uniform(A2182, A2183), random.randint(A2184, A2185), 0, False, smoke_decay, A2186, 1, 8, 8, 1, 0, 60, False)
        self.display[0].x = self.world_object.position.x - 0.5
        self.display[0].y = self.world_object.position.y - 0.5
        self.display[0].z = self.world_object.position.z - 0.5
        return

    def set_position(self, x, y, z):
        if self.world_object:
            self.world_object.set_position(Vector3(x, y, z))

    def set_velocity(self, v_x, v_y, v_z):
        if self.world_object:
            self.world_object.set_velocity(Vector3(v_x, v_y, v_z))

    def delete(self):
        pos = self.world_object.position
        self.scene.glow_block_particles.create(8, pos)
        solid, color = self.scene.map.get_point(pos.x, pos.y, pos.z)
        r, g, b, a = color
        self.scene.particle_effect_manager.create_particle_effect(None, pos, None, (r, g, b), 10, 1.0, 10.0, 180, 0, True, 1.0, 1.0, 0, 8, 8, random.randint(0, 1), 1, 30, True)
        if pos.z >= A2214 - 1:
            self.scene.media.play_pitched(A2765, pos=(pos.x, pos.y, pos.z), zone=media.IN_WORLD_AUDIO_ZONE)
        else:
            self.scene.media.play_pitched(A2764, pos=(pos.x, pos.y, pos.z), zone=media.IN_WORLD_AUDIO_ZONE)
        if self.sound:
            self.sound.close()
        super(Rocket2, self).delete()
        return
# okay decompiling out\aoslib.scenes.main.rocket2.pyc
