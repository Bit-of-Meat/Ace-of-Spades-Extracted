# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.font.base
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import unicodedata
from ..pyglet.gl import *
from pyglet import image
_other_grapheme_extend = map(unichr, [2494, 2519, 3043, 2903, 3006, 3031, 3266, 
 3285, 3286, 3390, 3415, 3535, 
 3551, 8204, 
 8205, 65438, 65439])
_logical_order_exception = map(unichr, range(3648, 3653) + range(3776, 3780))
_grapheme_extend = lambda c, cc: cc in ('Me', 'Mn') or c in _other_grapheme_extend
_CR = '\r'
_LF = '\n'
_control = lambda c, cc: cc in ('ZI', 'Zp', 'Cc', 'Cf') and c not in map(unichr, [13, 10, 8204, 8205])
_extend = lambda c, cc: _grapheme_extend(c, cc) or c in map(unichr, [3632, 3634, 3635, 3653, 3760, 3762, 3763])
_prepend = lambda c, cc: c in _logical_order_exception
_spacing_mark = lambda c, cc: cc == 'Mc' and c not in _other_grapheme_extend

def _grapheme_break(left, right):
    if left is None:
        return True
    else:
        if left == _CR and right == _LF:
            return False
        left_cc = unicodedata.category(left)
        if _control(left, left_cc):
            return True
        right_cc = unicodedata.category(right)
        if _control(right, right_cc):
            return True
        if _extend(right, right_cc):
            return False
        if _spacing_mark(right, right_cc):
            return False
        if _prepend(left, left_cc):
            return False
        return True


def get_grapheme_clusters(text):
    clusters = []
    cluster = ''
    left = None
    for right in text:
        if cluster and _grapheme_break(left, right):
            clusters.append(cluster)
            cluster = ''
        elif cluster:
            clusters.append('\u200b')
        cluster += right
        left = right

    if cluster:
        clusters.append(cluster)
    return clusters


class Glyph(image.TextureRegion):
    advance = 0
    vertices = (0, 0, 0, 0)

    def set_bearings(self, baseline, left_side_bearing, advance):
        self.advance = advance
        self.vertices = (
         left_side_bearing,
         -baseline,
         left_side_bearing + self.width,
         -baseline + self.height)

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.owner.id)
        glBegin(GL_QUADS)
        self.draw_quad_vertices()
        glEnd()

    def draw_quad_vertices(self):
        glTexCoord3f(*self.tex_coords[:3])
        glVertex2f(self.vertices[0], self.vertices[1])
        glTexCoord3f(*self.tex_coords[3:6])
        glVertex2f(self.vertices[2], self.vertices[1])
        glTexCoord3f(*self.tex_coords[6:9])
        glVertex2f(self.vertices[2], self.vertices[3])
        glTexCoord3f(*self.tex_coords[9:12])
        glVertex2f(self.vertices[0], self.vertices[3])

    def get_kerning_pair(self, right_glyph):
        return 0


class GlyphTextureAtlas(image.Texture):
    region_class = Glyph
    x = 0
    y = 0
    line_height = 0

    def apply_blend_state(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)

    def fit(self, image):
        if self.x + image.width > self.width:
            self.x = 0
            self.y += self.line_height + 1
            self.line_height = 0
        if self.y + image.height > self.height:
            return None
        else:
            self.line_height = max(self.line_height, image.height)
            region = self.get_region(self.x, self.y, image.width, image.height)
            if image.width > 0:
                region.blit_into(image, 0, 0, 0)
                self.x += image.width + 1
            return region


class GlyphRenderer(object):

    def __init__(self, font):
        pass

    def render(self, text):
        raise NotImplementedError('Subclass must override')


class FontException(Exception):
    pass


class Font(object):
    texture_width = 256
    texture_height = 256
    texture_internalformat = GL_ALPHA
    ascent = 0
    descent = 0
    glyph_renderer_class = GlyphRenderer
    texture_class = GlyphTextureAtlas

    def __init__(self):
        self.textures = []
        self.glyphs = {}

    @classmethod
    def add_font_data(cls, data):
        pass

    @classmethod
    def have_font(cls, name):
        return True

    def create_glyph(self, image):
        glyph = None
        for texture in self.textures:
            glyph = texture.fit(image)
            if glyph:
                break

        if not glyph:
            if image.width > self.texture_width or image.height > self.texture_height:
                texture = self.texture_class.create_for_size(GL_TEXTURE_2D, image.width * 2, image.height * 2, self.texture_internalformat)
                self.texture_width = texture.width
                self.texture_height = texture.height
            else:
                texture = self.texture_class.create_for_size(GL_TEXTURE_2D, self.texture_width, self.texture_height, self.texture_internalformat)
            self.textures.insert(0, texture)
            glyph = texture.fit(image)
        return glyph

    def get_glyphs(self, text):
        glyph_renderer = None
        glyphs = []
        for c in get_grapheme_clusters(unicode(text)):
            if c == '\t':
                c = ' '
            if c not in self.glyphs:
                if not glyph_renderer:
                    glyph_renderer = self.glyph_renderer_class(self)
                self.glyphs[c] = glyph_renderer.render(c)
            glyphs.append(self.glyphs[c])

        return glyphs

    def get_glyphs_for_width(self, text, width):
        glyph_renderer = None
        glyph_buffer = []
        glyphs = []
        for c in text:
            if c == '\n':
                glyphs += glyph_buffer
                break
            if c not in self.glyphs:
                if not glyph_renderer:
                    glyph_renderer = self.glyph_renderer_class(self)
                self.glyphs[c] = glyph_renderer.render(c)
            glyph = self.glyphs[c]
            glyph_buffer.append(glyph)
            width -= glyph.advance
            if width <= 0 and len(glyphs) > 0:
                break
            if c in ' \u200b':
                glyphs += glyph_buffer
                glyph_buffer = []

        if len(glyphs) == 0:
            glyphs = glyph_buffer
        return glyphs
# okay decompiling out\pyglet.font.base.pyc
