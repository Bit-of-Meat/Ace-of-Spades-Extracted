# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.snubPistolWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.draw import DisplayList
from aoslib import strings
from shared.glm import Vector3

class SnubPistolWeapon(Weapon):
    name = strings.A332
    damage = (A1141, A1142, A1143, A1144, A1144)
    block_damage = A1146
    range = A1134
    shoot_sound = A2838
    reload_sound = 'snub_reload'
    reload_done_sound = 'snub_cock'
    shoot_interval = A1137
    reload_time = A1135
    accuracy = A1138
    recoil_up = A1139
    recoil_side = A1140
    ammo = (A1150, A1150, A1147, A1148, A1149)
    clip_reload = True
    short_ranged_distance = None
    model = [WEAPON_SNUBNOSEPISTOL_MODEL]
    model_size = 1.3 * A274 * 0.666
    view_model = [WEAPON_SNUBNOSEPISTOL_VIEW_MODEL]
    sight = WEAPON_SNUBNOSEPISTOL_SIGHT
    casing = WEAPON_SNUBNOSEPISTOL_CASING
    tracer = WEAPON_SNUBNOSEPISTOL_TRACER
    image = TOOL_IMAGES[A332]
    sight_pos = (0, -0.1, -1)
    muzzle_flash_display = DisplayList(MUZZLE_FLASH_SNUB_PISTOL)
    muzzle_flash_view_display = DisplayList(MUZZLE_FLASH_SNUB_PISTOL_VIEW)
    muzzle_flash_offset = Vector3(-19.0, 59.0, -13.0)
    muzzle_flash_view_offset = Vector3(0.0, 0.34, 0.5)
    muzzle_flash_zoomed_view_offset = Vector3(0.0, -0.2, 2.5)
    show_crosshair = A293

    def __init__(self, character):
        super(SnubPistolWeapon, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.0, 0.12, 0.0)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, -0.12, 0.0)
# okay decompiling out\aoslib.weapons.snubPistolWeapon.pyc
