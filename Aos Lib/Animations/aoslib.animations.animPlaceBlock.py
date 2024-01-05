# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.animations.animPlaceBlock
from aoslib.animations.animation import Animation
from shared.glm import Vector3

class AnimPlaceBlock(Animation):
    default_length = 0.5

    def start(self, length=None):
        super(AnimPlaceBlock, self).start(length)
        self.position = Vector3(-self.length, -self.length, 0.0)
        self.orientation = Vector3(0.0, 0.0, 0.0)

    def update(self, dt):
        dt = min(self.timer, dt * self.speed)
        if super(AnimPlaceBlock, self).update(dt):
            self.position.x += dt
            self.position.y += dt
            return True
        else:
            return False
# okay decompiling out\aoslib.animations.animPlaceBlock.pyc
