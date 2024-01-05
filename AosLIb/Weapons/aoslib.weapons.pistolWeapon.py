# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.pistolWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.draw import DisplayList
from aoslib import strings
from shared.glm import Vector3

class PistolWeapon(Weapon):
    name = strings.PISTOL
    damage = (A1124, A1125, A1126, A1127, A1127)
    block_damage = A1129
    range = A1118
    shoot_sound = A2818
    reload_sound = 'pistolreload'
    shoot_interval = A1120
    reload_time = A1119
    accuracy = A1121
    recoil_up = A1122
    recoil_side = A1123
    ammo = (A1133, A1133, A1130, A1131, A1132)
    clip_reload = False
    short_ranged_distance = None
    model = [PISTOL_MODEL]
    view_model = [PISTOL_VIEW_MODEL]
    sight = PISTOL_SIGHT
    casing = PISTOL_CASING
    tracer = PISTOL_TRACER
    image = TOOL_IMAGES[A313]
    sight_pos = (0, -0.1, -1)
    muzzle_flash_display = DisplayList(MUZZLE_FLASH_PISTOL)
    muzzle_flash_view_display = DisplayList(MUZZLE_FLASH_PISTOL_VIEW)
    muzzle_flash_offset = Vector3(-13.0, 53.0, -6.0)
    muzzle_flash_view_offset = Vector3(-0.05, 0.12, 0.35)
    muzzle_flash_zoomed_view_offset = Vector3(0.0, -0.1, 1.5)
    show_crosshair = A293
# okay decompiling out\aoslib.weapons.pistolWeapon.pyc
