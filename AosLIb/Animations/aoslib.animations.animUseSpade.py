# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.animations.animUseSpade
from aoslib.animations.animation import Animation
from shared.glm import Vector3

class AnimUseSpade(Animation):
    default_length = 0.2

    def __init__(self, length=default_length, speed=None):
        super(AnimUseSpade, self).__init__(length, speed)

    def start(self, length=None):
        super(AnimUseSpade, self).start(length)
        f = self.length
        if f >= 0.6:
            f2 = 0
            f = 1 - f
        elif f >= 0.3:
            f2 = 0.6 - f
            f = 0.4
        elif f >= 0.1:
            f2 = 0.3
            f = 0.4
        else:
            f2 = f * 3
            f *= 4
        self.position = Vector3(-(f2 / 16.0 * 3.0), f / 1.3, -f2 / 0.6)
        self.orientation = Vector3(f / -0.32 * 60.0, 0.0, f * 30.0)

    def update(self, dt):
        dt = min(self.timer, dt * self.speed)
        if super(AnimUseSpade, self).update(dt):
            f = self.timer
            if f >= 0.6:
                f2 = 0
                f = 1 - f
            elif f >= 0.3:
                f2 = 0.6 - f
                f = 0.4
            elif f >= 0.1:
                f2 = 0.3
                f = 0.4
            else:
                f2 = f * 3
                f *= 4
            self.position.x = f2 / 16.0 * 3.0
            self.position.y = -(f / 1.3)
            self.position.z = f2 / 0.6
            self.orientation.x = -f / -0.32 * 60.0
            self.orientation.z = -f * 30.0
            return True
        else:
            return False
# okay decompiling out\aoslib.animations.animUseSpade.pyc
