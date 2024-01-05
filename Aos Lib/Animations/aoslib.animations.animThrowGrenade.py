# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.animations.animThrowGrenade
from aoslib.animations.animation import Animation
from shared.glm import Vector3

class AnimThrowGrenade(Animation):
    default_length = 0.5

    def __init__(self, length=default_length, speed=None, stop_on_end=True):
        super(AnimThrowGrenade, self).__init__(length, speed, stop_on_end)

    def start(self, length=None):
        super(AnimThrowGrenade, self).start(length)
        self.position = Vector3(0.0, 0.0, 0.0)
        self.orientation = Vector3(0.0, 0.0, 0.0)

    def update(self, dt):
        dt = min(self.timer, dt * self.speed)
        if super(AnimThrowGrenade, self).update(dt):
            value = self.length - self.timer
            self.position.x = -value * 1.5
            self.position.y = value * 0.5
            self.orientation.x = value * -40
            return True
        else:
            return False
# okay decompiling out\aoslib.animations.animThrowGrenade.pyc
