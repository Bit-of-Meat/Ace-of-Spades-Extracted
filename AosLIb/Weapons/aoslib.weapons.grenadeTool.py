# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.grenadeTool
from tool import Tool
from aoslib.models import *
from shared.constants import *
from . import TOOL_IMAGES
from aoslib import media, strings
from aoslib.animations.animThrowGrenade import *

class GrenadeTool(Tool):
    name = strings.A307
    model = [GRENADE_MODEL]
    view_model = [GRENADE_VIEW_MODEL]
    shoot_interval = A1814
    fuse = A1817
    pitch_initial = -4.0
    stoppable = True
    delay = True
    has_secondary = False
    default_count = A1811
    initial_count = A1812
    restock_amount = A1813
    image = TOOL_IMAGES[A307]
    empty_fire_sound_ready = True
    show_crosshair = A294
    show_crosshair_centre = True
    accuracy_spread_min = A1828
    accuracy_spread = accuracy_spread_min
    accuracy_spread_max = accuracy_spread_min + A1829
    accuracy_spread_increase_per_shot = A1830
    accuracy_spread_reduction_speed = A1831
    max_fuse = A1817

    def __init__(self, character):
        super(GrenadeTool, self).__init__(character)
        self.animations['throw_grenade'] = AnimThrowGrenade(self.fuse)
        self.fuse_timer = 0
        self.set_equipped_tool_tip_text(strings.EQUIPPED_TOOL_TIP_GRENADE)

    def can_shoot_primary(self):
        if self.is_active():
            return False
        else:
            return super(GrenadeTool, self).can_shoot_primary()

    def can_shoot_secondary(self):
        if self.is_active():
            return False
        else:
            return super(GrenadeTool, self).can_shoot_secondary()

    def update(self, dt):
        if self.active_primary:
            if self.fuse_timer > 0:
                self.fuse_timer = max(self.fuse_timer - dt, 0)
            if self.fuse_timer == 0:
                self.use_primary()
                self.on_stop_primary()
        if self.is_active():
            self.pitch = self.pitch_initial + (self.max_fuse - self.fuse_timer) / self.max_fuse * -90
        else:
            self.pitch = self.pitch_initial
        if not self.character.can_shoot_primary():
            self.empty_fire_sound_ready = True
        return super(GrenadeTool, self).update(dt)

    def use_primary(self, fuse=0.0):
        if self.get_has_enough_ammo():
            super(GrenadeTool, self).use_primary()
            character = self.character
            character.shoot_primary = False
            if character.main:
                self.count -= 1
                self.update_ammo()
            self.play_sound(A2804, zone=media.IN_WORLD_AUDIO_ZONE)
            self.throw(fuse)
            self.fuse_timer = 0

    def throw(self, fuse):
        if self.character and self.character.main:
            self.character.throw_grenade(fuse)

    def on_stop_primary(self):
        super(GrenadeTool, self).on_stop_primary()
        self.use_primary(self.fuse_timer)
        self.animations['throw_grenade'].stop()
        return True

    def on_start_primary(self):
        if not self.get_has_enough_ammo() or not self.empty_fire_sound_ready:
            if not self.get_has_enough_ammo() and self.character is not None and self.character.main:
                self.character.auto_switch_tool(self)
            if self.empty_fire_sound_ready:
                self.empty_fire_sound_ready = False
        else:
            super(GrenadeTool, self).on_start_primary()
            self.fuse_timer = self.fuse
            self.play_sound(A2803, zone=media.IN_WORLD_AUDIO_ZONE)
            self.animations['throw_grenade'].start()
        return

    def is_available(self):
        return self.count > 0

    def get_has_enough_ammo(self):
        return self.is_available()

    def on_unset(self):
        super(GrenadeTool, self).on_unset()
        self.fuse_timer = 0
        if self.animations['throw_grenade']:
            self.animations['throw_grenade'].stop()
        self.active_primary = False
        self.active_secondary = False
# okay decompiling out\aoslib.weapons.grenadeTool.pyc
