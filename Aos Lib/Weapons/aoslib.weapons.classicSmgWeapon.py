# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.classicSmgWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from aoslib.draw import DisplayList
from aoslib import strings
from shared.glm import Vector3
from aoslib import media

class ClassicSmgWeapon(Weapon):
    name = strings.CLASSIC_SUB_MACHINE_GUN
    damage = (A1185, A1186, A1187, A1188, A1188)
    block_damage = A1190
    range = A1173
    shoot_sound = A2788
    reload_sound = 'smgreload'
    shoot_interval = A1176
    reload_time = A1174
    accuracy_min = A1177
    accuracy = accuracy_min
    accuracy_max = accuracy_min + A1178
    recoil_up = A1183
    recoil_side = A1184
    ammo = (A1194, A1194, A1191, A1192, A1193)
    clip_reload = False
    short_ranged_distance = None
    model = [CLASSIC_SMG_MODEL]
    view_model = [CLASSIC_SMG_VIEW_MODEL]
    casing = CLASSIC_SMG_CASING
    tracer = CLASSIC_SMG_TRACER
    sight = CLASSIC_SMG_SIGHT
    ring = CLASSIC_SMG_RING
    image = TOOL_IMAGES[A334]
    sight_pos = (0.0, -0.2, 0.0)
    accuracy_spread_min = A1179
    accuracy_spread = accuracy_spread_min
    accuracy_spread_max = accuracy_spread_min + A1180
    accuracy_spread_increase_per_shot = A1181
    accuracy_spread_reduction_speed = A1182
    can_zoom = True
    show_crosshair = A293
    variable_accuracy = True
    muzzle_flash_display = DisplayList(MUZZLE_FLASH_SMG)
    muzzle_flash_duration = 0.01
    muzzle_flash_view_display = DisplayList(MUZZLE_FLASH_SMG_VIEW)
    muzzle_flash_offset = Vector3(-12.0, 59.0, -5.0)
    muzzle_flash_view_offset = Vector3(-0.0, 0.12, 0.5)
    muzzle_flash_zoomed_view_offset = Vector3(0.0, -0.1, 3.0)
    shooting = False

    def __init__(self, character):
        super(ClassicSmgWeapon, self).__init__(character)
        self.looping_fire_sound = None
        self.play_shoot_sound = False
        self.time_firing = 0.0
        return

    def on_unset(self):
        if self.looping_fire_sound:
            self.looping_fire_sound.close()
            self.looping_fire_sound = None
        self.time_firing = 0.0
        super(ClassicSmgWeapon, self).on_unset()
        return

    def update(self, dt):
        if self.character.can_shoot_primary() and self.can_fire():
            if not self.looping_fire_sound:
                self.looping_fire_sound = self.play_sound('classic_smg_fire_loop', position=self.get_audio_pos(), loops=0, zone=media.IN_WORLD_AUDIO_ZONE)
            self.shooting = True
        if self.shooting:
            self.time_firing += dt
        if self.time_firing >= A1176:
            self.play_shoot_sound = False
            self.time_firing -= A1176
            if not self.character.can_shoot_primary() or not self.can_fire():
                self.shooting = False
            if not self.shooting:
                if self.looping_fire_sound:
                    self.looping_fire_sound.close()
                    self.looping_fire_sound = None
                self.play_sound('classic_smg_fire_tail', position=self.get_audio_pos(), zone=media.IN_WORLD_AUDIO_ZONE)
                self.time_firing = 0.0
        if self.looping_fire_sound:
            pos = self.get_audio_pos()
            if pos:
                self.looping_fire_sound.set_position(*pos)
        return super(ClassicSmgWeapon, self).update(dt)
# okay decompiling out\aoslib.weapons.classicSmgWeapon.pyc
