# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.atlas
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import pyglet

class AllocatorException(Exception):
    pass


class _Strip(object):

    def __init__(self, y, max_height):
        self.x = 0
        self.y = y
        self.max_height = max_height
        self.y2 = y

    def add(self, width, height):
        x, y = self.x, self.y
        self.x += width
        self.y2 = max(self.y + height, self.y2)
        return (x, y)

    def compact(self):
        self.max_height = self.y2 - self.y


class Allocator(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.strips = [_Strip(0, height)]
        self.used_area = 0

    def alloc(self, width, height):
        for strip in self.strips:
            if self.width - strip.x >= width and strip.max_height >= height:
                self.used_area += width * height
                return strip.add(width, height)

        if self.width >= width and self.height - strip.y2 >= height:
            self.used_area += width * height
            strip.compact()
            newstrip = _Strip(strip.y2, self.height - strip.y2)
            self.strips.append(newstrip)
            return newstrip.add(width, height)
        raise AllocatorException('No more space in %r for box %dx%d' % (
         self, width, height))

    def get_usage(self):
        return self.used_area / float(self.width * self.height)

    def get_fragmentation(self):
        if not self.strips:
            return 0.0
        possible_area = self.strips[-1].y2 * self.width
        return 1.0 - self.used_area / float(possible_area)


class TextureAtlas(object):

    def __init__(self, width=256, height=256):
        self.texture = pyglet.image.Texture.create(width, height, pyglet.gl.GL_RGBA, rectangle=True)
        self.allocator = Allocator(width, height)

    def add(self, img):
        x, y = self.allocator.alloc(img.width, img.height)
        self.texture.blit_into(img, x, y, 0)
        region = self.texture.get_region(x, y, img.width, img.height)
        self.tex_border(region)
        return region

    def tex_border(self, tex):
        coord_width = tex.tex_coords[6] - tex.tex_coords[0]
        coord_height = tex.tex_coords[7] - tex.tex_coords[1]
        x_adjust = coord_width / tex.width / 2.0
        y_adjust = coord_height / tex.height / 2.0
        tex.tex_coords = (
         tex.tex_coords[0] + x_adjust,
         tex.tex_coords[1] + y_adjust,
         0,
         tex.tex_coords[3] - x_adjust,
         tex.tex_coords[4] + y_adjust,
         0,
         tex.tex_coords[6] - x_adjust,
         tex.tex_coords[7] - y_adjust,
         0,
         tex.tex_coords[9] + x_adjust,
         tex.tex_coords[10] - y_adjust,
         0)


class TextureBin(object):

    def __init__(self, texture_width=256, texture_height=256):
        self.atlases = []
        self.texture_width = texture_width
        self.texture_height = texture_height

    def add(self, img):
        for atlas in list(self.atlases):
            try:
                return atlas.add(img)
            except AllocatorException:
                if img.width < 64 and img.height < 64:
                    self.atlases.remove(atlas)

        atlas = TextureAtlas(self.texture_width, self.texture_height)
        self.atlases.append(atlas)
        return atlas.add(img)
# okay decompiling out\pyglet.image.atlas.pyc
