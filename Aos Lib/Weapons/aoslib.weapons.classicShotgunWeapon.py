# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.classicShotgunWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.draw import DisplayList
from aoslib import strings
from shared.glm import Vector3

class ClassicShotgunWeapon(Weapon):
    name = strings.CLASSIC_SHOTGUN
    damage = (A1303, A1304, A1305, A1306, A1306)
    block_damage = A1308
    range = A1291
    shoot_sound = A2842
    reload_sound = 'shotgunreload'
    reload_done_sound = 'cock'
    shoot_interval = A1294
    reload_time = A1292
    accuracy_min = A1295
    accuracy = accuracy_min
    accuracy_max = accuracy_min + A1296
    recoil_up = A1301
    recoil_side = A1302
    ammo = (A1312, A1312, A1309, A1310, A1311)
    clip_reload = True
    pellets = A1313
    short_ranged_distance = 25
    model = [CLASSIC_SHOTGUN_MODEL]
    view_model = [CLASSIC_SHOTGUN_VIEW_MODEL]
    casing = CLASSIC_SHOTGUN_CASING
    tracer = CLASSIC_SHOTGUN_TRACER
    sight = CLASSIC_SHOTGUN_SIGHT
    image = TOOL_IMAGES[A333]
    accuracy_spread_min = A1297
    accuracy_spread = accuracy_spread_min
    accuracy_spread_max = accuracy_spread_min + A1298
    accuracy_spread_increase_per_shot = A1299
    accuracy_spread_reduction_speed = A1300
    can_zoom = True
    show_crosshair = A293
    variable_accuracy = True
    muzzle_flash_display = DisplayList(MUZZLE_FLASH_SHOTGUN)
    muzzle_flash_scale = 1.0
    muzzle_flash_view_display = DisplayList(MUZZLE_FLASH_SHOTGUN_VIEW)
    muzzle_flash_offset = Vector3(-6.0, 36.0, -3.0)
    muzzle_flash_view_offset = Vector3(-0.05, 0.12, 0.8)
    muzzle_flash_zoomed_view_offset = Vector3(0.0, -0.1, 3.0)
# okay decompiling out\aoslib.weapons.classicShotgunWeapon.pyc
