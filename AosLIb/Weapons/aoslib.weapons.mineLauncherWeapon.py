# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.mineLauncherWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from shared.glm import Vector3
from aoslib import strings
from aoslib import media

class MineLauncherWeapon(Weapon):
    name = strings.MINE_LAUNCHER
    damage = None
    sight = None
    shoot_sound = A2941
    reload_sound = A2946
    accuracy = A1720
    recoil_up = A1721
    recoil_side = A1722
    reload_time = A1718
    clip_reload = False
    shoot_interval = A1723
    model = [MINE_LAUNCHER_MODEL]
    view_model = [MINE_LAUNCHER_VIEW_MODEL]
    model_size = 0.04
    view_model_size = 0.08
    sight_pos = (0.0, 0.325, -1.85)
    tracer = None
    ammo = (A1727, A1727, A1724,
     A1725, A1726)
    image = TOOL_IMAGES[A354]

    def __init__(self, character):
        super(MineLauncherWeapon, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(-0.15, 0.15, 0.0)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, -0.1, 0.0)

    def shoot(self, fp3, seed):
        if self.play_shoot_sound:
            self.play_sound(self.shoot_sound, zone=media.IN_WORLD_AUDIO_ZONE)
        character = self.character
        if not character.main:
            return
        scene = character.scene
        player = character.world_object
        x, y, z = player.position.get()
        scene.send_mine_projectile(player.position, fp3 * A1728)
        return True
# okay decompiling out\aoslib.weapons.mineLauncherWeapon.pyc
