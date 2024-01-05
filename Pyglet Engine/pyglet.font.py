# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.font
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import sys, os, math, weakref, pyglet
from ..pyglet.gl import *
from pyglet import gl
from pyglet import image
from pyglet import window

class GlyphString(object):

    def __init__(self, text, glyphs, x=0, y=0):
        lst = []
        texture = None
        self.text = text
        self.states = []
        self.cumulative_advance = []
        state_from = 0
        state_length = 0
        for i, glyph in enumerate(glyphs):
            if glyph.owner != texture:
                if state_length:
                    self.states.append((state_from, state_length, texture))
                texture = glyph.owner
                state_from = i
                state_length = 0
            state_length += 1
            t = glyph.tex_coords
            lst += [t[0], t[1], t[2], 1.0,
             x + glyph.vertices[0], y + glyph.vertices[1], 0.0, 1.0,
             t[3], t[4], t[5], 1.0,
             x + glyph.vertices[2], y + glyph.vertices[1], 0.0, 1.0,
             t[6], t[7], t[8], 1.0,
             x + glyph.vertices[2], y + glyph.vertices[3], 0.0, 1.0,
             t[9], t[10], t[11], 1.0,
             x + glyph.vertices[0], y + glyph.vertices[3], 0.0, 1.0]
            x += glyph.advance
            self.cumulative_advance.append(x)

        self.states.append((state_from, state_length, texture))
        self.array = (c_float * len(lst))(*lst)
        self.width = x
        return

    def get_break_index(self, from_index, width):
        to_index = from_index
        if from_index >= len(self.text):
            return from_index
        if from_index:
            width += self.cumulative_advance[from_index - 1]
        for i, (c, w) in enumerate(zip(self.text[from_index:], self.cumulative_advance[from_index:])):
            if c in ' \u200b':
                to_index = i + from_index + 1
            if c == '\n':
                return i + from_index + 1
            if w > width:
                return to_index

        return to_index

    def get_subwidth(self, from_index, to_index):
        if to_index <= from_index:
            return 0
        width = self.cumulative_advance[to_index - 1]
        if from_index:
            width -= self.cumulative_advance[from_index - 1]
        return width

    def draw(self, from_index=0, to_index=None):
        if from_index >= len(self.text) or from_index == to_index or not self.text:
            return
        self.states[0][2].apply_blend_state()
        if from_index:
            glPushMatrix()
            glTranslatef(-self.cumulative_advance[from_index - 1], 0, 0)
        if to_index is None:
            to_index = len(self.text)
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glInterleavedArrays(GL_T4F_V4F, 0, self.array)
        for state_from, state_length, texture in self.states:
            if state_from + state_length < from_index:
                continue
            state_from = max(state_from, from_index)
            state_length = min(state_length, to_index - state_from)
            if state_length <= 0:
                break
            glBindTexture(GL_TEXTURE_2D, texture.id)
            glDrawArrays(GL_QUADS, state_from * 4, state_length * 4)

        glPopClientAttrib()
        if from_index:
            glPopMatrix()
        return


class _TextZGroup(pyglet.graphics.Group):
    z = 0

    def set_state(self):
        glTranslatef(0, 0, self.z)

    def unset_state(self):
        glTranslatef(0, 0, -self.z)


class Text(object):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'
    BOTTOM = 'bottom'
    BASELINE = 'baseline'
    TOP = 'top'
    _wrap = None
    _width = None

    def __init__(self, font, text='', x=0, y=0, z=0, color=(1, 1, 1, 1), width=None, halign=LEFT, valign=BASELINE):
        multiline = False
        if width is not None:
            self._width = width
            self._wrap = 'width'
            multiline = True
        elif '\n' in text:
            self._wrap = 'multiline'
            multiline = True
        self._group = _TextZGroup()
        self._document = pyglet.text.decode_text(text)
        self._layout = pyglet.text.layout.TextLayout(self._document, width=width, multiline=multiline, dpi=font.dpi, group=self._group)
        self._layout.begin_update()
        if self._wrap == 'multiline':
            self._document.set_style(0, len(text), dict(wrap=False))
        self.font = font
        self.color = color
        self._x = x
        self.y = y
        self.z = z
        self.width = width
        self.halign = halign
        self.valign = valign
        self._update_layout_halign()
        self._layout.end_update()
        return

    def _get_font(self):
        return self._font

    def _set_font(self, font):
        self._font = font
        self._layout.begin_update()
        self._document.set_style(0, len(self._document.text), {'font_name': font.name, 
           'font_size': font.size, 
           'bold': font.bold, 
           'italic': font.italic})
        self._layout._dpi = font.dpi
        self._layout.end_update()

    font = property(_get_font, _set_font)

    def _get_color(self):
        color = self._document.get_style('color')
        if color is None:
            return (1.0, 1.0, 1.0, 1.0)
        else:
            return tuple([ c / 255.0 for c in color ])

    def _set_color(self, color):
        color = [ int(c * 255) for c in color ]
        self._document.set_style(0, len(self._document.text), {'color': color})

    color = property(_get_color, _set_color)

    def _update_layout_halign(self):
        if self._layout.multiline:
            if self._layout.anchor_x == 'left':
                self._layout.x = self.x
            else:
                if self._layout.anchor_x == 'center':
                    self._layout.x = self.x + self._layout.width - self._layout.content_width // 2
                elif self._layout.anchor_x == 'right':
                    self._layout.x = self.x + 2 * self._layout.width - self._layout.content_width
        else:
            self._layout.x = self.x

    def _get_x(self):
        return self._x

    def _set_x(self, x):
        self._x = x
        self._update_layout_halign()

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._layout.y

    def _set_y(self, y):
        self._layout.y = y

    y = property(_get_y, _set_y)

    def _get_z(self):
        return self._group.z

    def _set_z(self, z):
        self._group.z = z

    z = property(_get_z, _set_z)

    def _update_wrap(self):
        if self._width is not None:
            self._wrap = 'width'
        elif '\n' in self.text:
            self._wrap = 'multiline'
        self._layout.begin_update()
        if self._wrap == None:
            self._layout.multiline = False
        elif self._wrap == 'width':
            self._layout.multiline = True
            self._layout.width = self._width
            self._document.set_style(0, len(self.text), dict(wrap=True))
        elif self._wrap == 'multiline':
            self._layout.multiline = True
            self._document.set_style(0, len(self.text), dict(wrap=False))
        self._update_layout_halign()
        self._layout.end_update()
        return

    def _get_width(self):
        if self._wrap == 'width':
            return self._layout.width
        else:
            return self._layout.content_width

    def _set_width(self, width):
        self._width = width
        self._update_wrap()

    width = property(_get_width, _set_width, doc='Width of the text.\n\n        When set, this enables word-wrapping to the specified width.\n        Otherwise, the width of the text as it will be rendered can be\n        determined.\n        \n        :type: float\n        ')

    def _get_height(self):
        return self._layout.content_height

    height = property(_get_height, doc='Height of the text.\n        \n        This property is the ascent minus the descent of the font, unless\n        there is more than one line of word-wrapped text, in which case\n        the height takes into account the line leading.  Read-only.\n\n        :type: float\n        ')

    def _get_text(self):
        return self._document.text

    def _set_text(self, text):
        self._document.text = text
        self._update_wrap()

    text = property(_get_text, _set_text, doc='Text to render.\n\n        The glyph vertices are only recalculated as needed, so multiple\n        changes to the text can be performed with no performance penalty.\n        \n        :type: str\n        ')

    def _get_halign(self):
        return self._layout.anchor_x

    def _set_halign(self, halign):
        self._layout.anchor_x = halign
        self._update_layout_halign()

    halign = property(_get_halign, _set_halign, doc='Horizontal alignment of the text.\n\n        The text is positioned relative to `x` and `width` according to this\n        property, which must be one of the alignment constants `LEFT`,\n        `CENTER` or `RIGHT`.\n\n        :type: str\n        ')

    def _get_valign(self):
        return self._layout.anchor_y

    def _set_valign(self, valign):
        self._layout.anchor_y = valign

    valign = property(_get_valign, _set_valign, doc='Vertical alignment of the text.\n\n        The text is positioned relative to `y` according to this property,\n        which must be one of the alignment constants `BOTTOM`, `BASELINE`,\n        `CENTER` or `TOP`.\n\n        :type: str\n        ')

    def _get_leading(self):
        return self._document.get_style('leading') or 0

    def _set_leading(self, leading):
        self._document.set_style(0, len(self._document.text), {'leading': leading})

    leading = property(_get_leading, _set_leading, doc='Vertical space between adjacent lines, in pixels.\n\n        :type: int\n        ')

    def _get_line_height(self):
        return self._font.ascent - self._font.descent + self.leading

    def _set_line_height(self, line_height):
        self.leading = line_height - (self._font.ascent - self._font.descent)

    line_height = property(_get_line_height, _set_line_height, doc='Vertical distance between adjacent baselines, in pixels.\n\n        :type: int\n        ')

    def draw(self):
        self._layout.draw()


if not getattr(sys, 'is_epydoc', False):
    if sys.platform == 'darwin':
        if pyglet.options['darwin_cocoa']:
            from pyglet.font.quartz import QuartzFont
            _font_class = QuartzFont
        else:
            from pyglet.font.carbon import CarbonFont
            _font_class = CarbonFont
    elif sys.platform in ('win32', 'cygwin'):
        if pyglet.options['font'][0] == 'win32':
            from pyglet.font.win32 import Win32Font
            _font_class = Win32Font
        elif pyglet.options['font'][0] == 'gdiplus':
            from pyglet.font.win32 import GDIPlusFont
            _font_class = GDIPlusFont
    else:
        from pyglet.font.freetype import FreeTypeFont
        _font_class = FreeTypeFont

def load(name=None, size=None, bold=False, italic=False, dpi=None):
    if size is None:
        size = 12
    if dpi is None:
        dpi = 96
    if type(name) in (tuple, list):
        for n in name:
            if _font_class.have_font(n):
                name = n
                break
        else:
            name = None

    shared_object_space = gl.current_context.object_space
    if not hasattr(shared_object_space, 'pyglet_font_font_cache'):
        shared_object_space.pyglet_font_font_cache = weakref.WeakValueDictionary()
        shared_object_space.pyglet_font_font_hold = []
    font_cache = shared_object_space.pyglet_font_font_cache
    font_hold = shared_object_space.pyglet_font_font_hold
    descriptor = (
     name, size, bold, italic, dpi)
    if descriptor in font_cache:
        return font_cache[descriptor]
    else:
        font = _font_class(name, size, bold=bold, italic=italic, dpi=dpi)
        font.name = name
        font.size = size
        font.bold = bold
        font.italic = italic
        font.dpi = dpi
        font_cache[descriptor] = font
        del font_hold[3:]
        font_hold.insert(0, font)
        return font


def add_file(font):
    if type(font) in (str, unicode):
        font = open(font, 'rb')
    if hasattr(font, 'read'):
        font = font.read()
    _font_class.add_font_data(font)


def add_directory(dir):
    for file in os.listdir(dir):
        if file[-4:].lower() == '.ttf':
            add_file(os.path.join(dir, file))
# okay decompiling out\pyglet.font.pyc
