# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.drawItem


class DrawItem(object):
    draw_on_minimap_when_out_of_range = False
    deleted = False
    requires_update = True
    requires_draw = True
    needs_shadow = False

    def __init__(self, scene, *arg, **kw):
        self.scene = scene
        scene.objects.append(self)
        if self.__class__ not in scene.objects_by_type.keys():
            scene.objects_by_type[self.__class__] = []
        scene.objects_by_type[self.__class__].append(self)
        self.initialize(*arg, **kw)

    def initialize(self, *arg, **kw):
        pass

    def update(self, dt):
        pass

    def delete(self):
        if self.deleted:
            return
        self.deleted = True
        self.scene.objects.remove(self)
        self.scene.objects_by_type[self.__class__].remove(self)
        self.on_delete()

    def on_delete(self):
        pass
# okay decompiling out\aoslib.scenes.main.drawItem.pyc
