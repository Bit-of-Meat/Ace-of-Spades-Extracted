# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.glGrenade
from aoslib.scenes.main.drawItem import DrawItem
from aoslib.models import *
from aoslib.world import Grenade as WorldGrenade
from aoslib.draw import DisplayList
from aoslib.shaders import *
from shared.constants import *
from aoslib.scenes.main.explodeOnImpactEntity import *

class GLGrenade(ExplodeOnImpactEntity):
    name = 'GLGrenade'
    size = 0.02
    model_position_offsets = []
    model = [GRENADE_MODEL]
    explode_sound = A2913
    water_explode_sound = A2914

    def __init__(self, scene, *arg, **kw):
        super(GLGrenade, self).__init__(scene, *arg, **kw)
# okay decompiling out\aoslib.scenes.main.glGrenade.pyc
