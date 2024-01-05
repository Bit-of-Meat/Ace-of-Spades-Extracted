# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.shotgunWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.draw import DisplayList
from aoslib import strings
from shared.glm import Vector3

class ShotgunWeapon(Weapon):
    name = strings.SHOTGUN
    damage = (A1280, A1281, A1282, A1283, A1283)
    block_damage = A1285
    range = A1268
    shoot_sound = A2815
    reload_sound = 'shotgunreload'
    reload_done_sound = 'cock'
    shoot_interval = A1271
    reload_time = A1269
    accuracy_min = A1272
    accuracy = accuracy_min
    accuracy_max = accuracy_min + A1273
    recoil_up = A1278
    recoil_side = A1279
    ammo = (A1289, A1289, A1286, A1287, A1288)
    clip_reload = True
    pellets = A1290
    short_ranged_distance = 25
    model = [SHOTGUN_MODEL]
    view_model = [SHOTGUN_VIEW_MODEL]
    casing = SHOTGUN_CASING
    tracer = SHOTGUN_TRACER
    sight = SHOTGUN_SIGHT
    image = TOOL_IMAGES[A305]
    accuracy_spread_min = A1274
    accuracy_spread = accuracy_spread_min
    accuracy_spread_max = accuracy_spread_min + A1275
    accuracy_spread_increase_per_shot = A1276
    accuracy_spread_reduction_speed = A1277
    can_zoom = True
    show_crosshair = A293
    variable_accuracy = True
    muzzle_flash_display = DisplayList(MUZZLE_FLASH_SHOTGUN)
    muzzle_flash_scale = 1.0
    muzzle_flash_view_display = DisplayList(MUZZLE_FLASH_SHOTGUN_VIEW)
    muzzle_flash_offset = Vector3(-6.0, 36.0, -3.0)
    muzzle_flash_view_offset = Vector3(-0.05, 0.12, 0.8)
    muzzle_flash_zoomed_view_offset = Vector3(0.0, -0.1, 3.0)
# okay decompiling out\aoslib.weapons.shotgunWeapon.pyc
