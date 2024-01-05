# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.grenadeLauncherWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from shared.glm import Vector3
from aoslib import strings
from aoslib import media
from aoslib.scenes.main.glGrenade import *

class GrenadeLauncherWeapon(Weapon):
    name = strings.GRENADE_LAUNCHER_WEAPON
    damage = None
    sight = None
    shoot_sound = A2911
    reload_sound = A2912
    accuracy = A1697
    recoil_up = A1698
    recoil_side = A1699
    reload_time = A1695
    clip_reload = False
    shoot_interval = A1700
    model = [GRENADE_LAUNCHER_MODEL]
    view_model = [GRENADE_LAUNCHER_VIEW_MODEL]
    model_size = 0.028
    view_model_size = 0.065
    tracer = None
    ammo = (A1704, A1704, A1701, A1702, A1703)
    image = TOOL_IMAGES[A351]
    grenade_fuse = A1717
    grenade_speed = A1705

    def __init__(self, character):
        super(GrenadeLauncherWeapon, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(-0.15, 0.12, 0.1)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.1, -0.18, -0.0)

    def shoot(self, fp3, seed):
        if self.play_shoot_sound:
            self.play_sound(self.shoot_sound, zone=media.IN_WORLD_AUDIO_ZONE)
        character = self.character
        if not character.main:
            return
        scene = character.scene
        player = character.world_object
        x, y, z = player.position.get()
        scene.send_gl_grenade(player.position, fp3 * self.grenade_speed, self.grenade_fuse)
        return True
# okay decompiling out\aoslib.weapons.grenadeLauncherWeapon.pyc
