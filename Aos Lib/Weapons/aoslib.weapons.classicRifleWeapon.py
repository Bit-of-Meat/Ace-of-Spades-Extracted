# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.classicRifleWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.draw import DisplayList
from aoslib import strings

class ClassicRifleWeapon(Weapon):
    name = strings.RIFLE
    damage = (A2048, A2049, A2050, A2051, A2051)
    block_damage = A2053
    range = A2041
    shoot_sound = A2819
    reload_sound = 'classic_semi_reload'
    shoot_interval = A2044
    reload_time = A2042
    accuracy = A2045
    recoil_up = A2046
    recoil_side = A2047
    ammo = (A2057, A2057, A2054, A2055, A2056)
    clip_reload = False
    short_ranged_distance = None
    show_crosshair = A292
    model = [SEMI_MODEL]
    view_model = [SEMI_VIEW_MODEL]
    casing = SEMI_CASING
    tracer = SEMI_TRACER
    sight = SEMI_SIGHT
    pin = SEMI_PIN
    image = TOOL_IMAGES[A302]
    muzzle_flash_display = DisplayList(MUZZLE_FLASH_RIFLE)
# okay decompiling out\aoslib.weapons.classicRifleWeapon.pyc
