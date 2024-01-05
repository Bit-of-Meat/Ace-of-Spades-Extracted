# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.animations.animSlowPullout
from aoslib.animations.animation import Animation
from shared.glm import Vector3

class AnimSlowPullout(Animation):
    default_length = 0.5

    def start(self, length=None):
        super(AnimSlowPullout, self).start(length)
        self.position = Vector3(0.0, 0.0, 0.0)
        self.orientation = Vector3(0.0, 0.0, 0.0)

    def update(self, dt):
        dt = min(self.timer, dt * self.speed)
        if super(AnimSlowPullout, self).update(dt):
            if (self.length - self.timer) / self.length > 0.9:
                self.position.y -= 10 * dt / self.length
                self.position.z -= 10 * dt / self.length
            return True
        return False
# okay decompiling out\aoslib.animations.animSlowPullout.pyc
