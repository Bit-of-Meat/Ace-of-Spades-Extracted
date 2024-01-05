# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.drillgunWeapon
from weapon import Weapon
from . import TOOL_IMAGES
from aoslib.models import *
from shared.constants import *
from shared.glm import Vector3
from aoslib import strings
from aoslib import media

class DrillgunWeapon(Weapon):
    name = strings.DRILL_TOOL
    damage = None
    sight = None
    shoot_sound = A2786
    reload_sound = 'drillreload'
    reload_done_sound = 'cock'
    accuracy = A1485
    recoil_up = A1486
    recoil_side = A1487
    reload_time = A1483
    clip_reload = False
    shoot_interval = A1488
    model = [DRILLGUN_MODEL]
    view_model = [DRILLGUN_VIEW_MODEL]
    sight = DRILLGUN_SIGHT
    sight_pos = (0.0, 0.325, -1.85)
    tracer = None
    ammo = (A1492, A1492, A1489, A1490, A1491)
    image = TOOL_IMAGES[A310]

    def __init__(self, character):
        super(DrillgunWeapon, self).__init__(character)
        if character.main:
            for model_index in range(len(self.view_model)):
                self.initial_position[model_index] = Vector3(0.0, 0.1, 0.0)
                self.reset_position(model_index)

        self.arms_position_offset = Vector3(0.0, -0.1, 0.0)

    def shoot(self, orientation, seed):
        if self.play_shoot_sound:
            self.play_sound(self.shoot_sound, zone=media.IN_WORLD_AUDIO_ZONE)
        character = self.character
        if not character.main:
            return
        scene = character.scene
        player = character.world_object
        from aoslib.scenes.main.drill import Drill
        x, y, z = player.position.get()
        scene.send_drill(player.position, orientation * A1493)
        return True
# okay decompiling out\aoslib.weapons.drillgunWeapon.pyc
