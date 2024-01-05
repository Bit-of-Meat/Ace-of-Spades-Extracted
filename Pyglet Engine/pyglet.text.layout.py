# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.layout
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import re, sys
from ..pyglet.gl import *
from pyglet import event
from pyglet import graphics
from pyglet.text import runlist
from pyglet.font.base import _grapheme_break
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc
_distance_re = re.compile('([-0-9.]+)([a-zA-Z]+)')

def _parse_distance(distance, dpi):
    if isinstance(distance, int):
        return distance
    if isinstance(distance, float):
        return int(distance)
    match = _distance_re.match(distance)
    if not match:
        return 0
    value, unit = match.groups()
    value = float(value)
    if unit == 'px':
        return int(value)
    if unit == 'pt':
        return int(value * dpi / 72.0)
    if unit == 'pc':
        return int(value * dpi / 6.0)
    if unit == 'in':
        return int(value * dpi)
    if unit == 'mm':
        return int(value * dpi * 0.0393700787)
    if unit == 'cm':
        return int(value * dpi * 0.393700787)


class _Line(object):
    align = 'left'
    margin_left = 0
    margin_right = 0
    length = 0
    ascent = 0
    descent = 0
    width = 0
    paragraph_begin = False
    paragraph_end = False
    x = None
    y = None

    def __init__(self, start):
        self.vertex_lists = []
        self.start = start
        self.boxes = []

    def __repr__(self):
        return '_Line(%r)' % self.boxes

    def add_box(self, box):
        self.boxes.append(box)
        self.length += box.length
        self.ascent = max(self.ascent, box.ascent)
        self.descent = min(self.descent, box.descent)
        self.width += box.advance

    def delete(self, layout):
        for vertex_list in self.vertex_lists:
            vertex_list.delete()

        self.vertex_lists = []
        for box in self.boxes:
            box.delete(layout)


class _LayoutContext(object):

    def __init__(self, layout, document, colors_iter, background_iter):
        self.colors_iter = colors_iter
        underline_iter = document.get_style_runs('underline')
        self.decoration_iter = runlist.ZipRunIterator((
         background_iter,
         underline_iter))
        self.baseline_iter = runlist.FilteredRunIterator(document.get_style_runs('baseline'), (lambda value: value is not None), 0)


class _StaticLayoutContext(_LayoutContext):

    def __init__(self, layout, document, colors_iter, background_iter):
        super(_StaticLayoutContext, self).__init__(layout, document, colors_iter, background_iter)
        self.vertex_lists = layout._vertex_lists
        self.boxes = layout._boxes

    def add_list(self, vertex_list):
        self.vertex_lists.append(vertex_list)

    def add_box(self, box):
        self.boxes.append(box)


class _IncrementalLayoutContext(_LayoutContext):
    line = None

    def add_list(self, vertex_list):
        self.line.vertex_lists.append(vertex_list)

    def add_box(self, box):
        pass


class _AbstractBox(object):
    owner = None

    def __init__(self, ascent, descent, advance, length):
        self.ascent = ascent
        self.descent = descent
        self.advance = advance
        self.length = length

    def place(self, layout, i, x, y):
        raise NotImplementedError('abstract')

    def delete(self, layout):
        raise NotImplementedError('abstract')

    def get_position_in_box(self, x):
        raise NotImplementedError('abstract')

    def get_point_in_box(self, position):
        raise NotImplementedError('abstract')


class _GlyphBox(_AbstractBox):

    def __init__(self, owner, font, glyphs, advance):
        super(_GlyphBox, self).__init__(font.ascent, font.descent, advance, len(glyphs))
        self.owner = owner
        self.font = font
        self.glyphs = glyphs
        self.advance = advance

    def place(self, layout, i, x, y, context):
        try:
            group = layout.groups[self.owner]
        except KeyError:
            group = layout.groups[self.owner] = TextLayoutTextureGroup(self.owner, layout.foreground_group)

        n_glyphs = self.length
        vertices = []
        tex_coords = []
        x1 = x
        for start, end, baseline in context.baseline_iter.ranges(i, i + n_glyphs):
            baseline = layout._parse_distance(baseline)
            for kern, glyph in self.glyphs[start - i:end - i]:
                x1 += kern
                v0, v1, v2, v3 = glyph.vertices
                v0 += x1
                v2 += x1
                v1 += y + baseline
                v3 += y + baseline
                vertices.extend(map(int, [v0, v1, v2, v1, v2, v3, v0, v3]))
                t = glyph.tex_coords
                tex_coords.extend(t)
                x1 += glyph.advance

        colors = []
        for start, end, color in context.colors_iter.ranges(i, i + n_glyphs):
            if color is None:
                color = (0, 0, 0, 255)
            colors.extend(color * ((end - start) * 4))

        vertex_list = layout.batch.add(n_glyphs * 4, GL_QUADS, group, (
         'v2f/dynamic', vertices), (
         't3f/dynamic', tex_coords), (
         'c4B/dynamic', colors))
        context.add_list(vertex_list)
        background_vertices = []
        background_colors = []
        underline_vertices = []
        underline_colors = []
        y1 = y + self.descent + baseline
        y2 = y + self.ascent + baseline
        x1 = x
        for start, end, decoration in context.decoration_iter.ranges(i, i + n_glyphs):
            bg, underline = decoration
            x2 = x1
            for kern, glyph in self.glyphs[start - i:end - i]:
                x2 += glyph.advance + kern

            if bg is not None:
                background_vertices.extend([
                 x1, y1, x2, y1, x2, y2, x1, 
                 y2])
                background_colors.extend(bg * 4)
            if underline is not None:
                underline_vertices.extend([
                 x1, y + baseline - 2, x2, y + baseline - 2])
                underline_colors.extend(underline * 2)
            x1 = x2

        if background_vertices:
            background_list = layout.batch.add(len(background_vertices) // 2, GL_QUADS, layout.background_group, (
             'v2f/dynamic', background_vertices), (
             'c4B/dynamic', background_colors))
            context.add_list(background_list)
        if underline_vertices:
            underline_list = layout.batch.add(len(underline_vertices) // 2, GL_LINES, layout.foreground_decoration_group, (
             'v2f/dynamic', underline_vertices), (
             'c4B/dynamic', underline_colors))
            context.add_list(underline_list)
        return

    def delete(self, layout):
        pass

    def get_point_in_box(self, position):
        x = 0
        for kern, glyph in self.glyphs:
            if position == 0:
                break
            position -= 1
            x += glyph.advance + kern

        return x

    def get_position_in_box(self, x):
        position = 0
        last_glyph_x = 0
        for kern, glyph in self.glyphs:
            last_glyph_x += kern
            if last_glyph_x + glyph.advance / 2 > x:
                return position
            position += 1
            last_glyph_x += glyph.advance

        return position

    def __repr__(self):
        return '_GlyphBox(%r)' % self.glyphs


class _InlineElementBox(_AbstractBox):

    def __init__(self, element):
        super(_InlineElementBox, self).__init__(element.ascent, element.descent, element.advance, 1)
        self.element = element
        self.placed = False

    def place(self, layout, i, x, y, context):
        self.element.place(layout, x, y)
        self.placed = True
        context.add_box(self)

    def delete(self, layout):
        if self.placed:
            self.element.remove(layout)
            self.placed = False

    def get_point_in_box(self, position):
        if position == 0:
            return 0
        else:
            return self.advance

    def get_position_in_box(self, x):
        if x < self.advance / 2:
            return 0
        else:
            return 1

    def __repr__(self):
        return '_InlineElementBox(%r)' % self.element


class _InvalidRange(object):

    def __init__(self):
        self.start = sys.maxint
        self.end = 0

    def insert(self, start, length):
        if self.start >= start:
            self.start += length
        if self.end >= start:
            self.end += length
        self.invalidate(start, start + length)

    def delete(self, start, end):
        if self.start > end:
            self.start -= end - start
        elif self.start > start:
            self.start = start
        if self.end > end:
            self.end -= end - start
        elif self.end > start:
            self.end = start

    def invalidate(self, start, end):
        if end <= start:
            return
        self.start = min(self.start, start)
        self.end = max(self.end, end)

    def validate(self):
        start, end = self.start, self.end
        self.start = sys.maxint
        self.end = 0
        return (start, end)

    def is_invalid(self):
        return self.end > self.start


class TextLayoutGroup(graphics.Group):

    def set_state(self):
        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def unset_state(self):
        glPopAttrib()


class ScrollableTextLayoutGroup(graphics.Group):
    _clip_x = 0
    _clip_y = 0
    _clip_width = 0
    _clip_height = 0
    _view_x = 0
    _view_y = 0
    translate_x = 0
    translate_y = 0

    def set_state(self):
        glPushAttrib(GL_ENABLE_BIT | GL_TRANSFORM_BIT | GL_CURRENT_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_CLIP_PLANE0)
        glEnable(GL_CLIP_PLANE1)
        glEnable(GL_CLIP_PLANE2)
        glEnable(GL_CLIP_PLANE3)
        glClipPlane(GL_CLIP_PLANE0, (GLdouble * 4)(1, 0, 0, -(self._clip_x - 1)))
        glClipPlane(GL_CLIP_PLANE1, (GLdouble * 4)(0, -1, 0, self._clip_y))
        glClipPlane(GL_CLIP_PLANE2, (GLdouble * 4)(-1, 0, 0, self._clip_x + self._clip_width + 1))
        glClipPlane(GL_CLIP_PLANE3, (GLdouble * 4)(0, 1, 0, -(self._clip_y - self._clip_height)))
        glTranslatef(self.translate_x, self.translate_y, 0)

    def unset_state(self):
        glTranslatef(-self.translate_x, -self.translate_y, 0)
        glPopAttrib()

    def _set_top(self, top):
        self._clip_y = top
        self.translate_y = self._clip_y - self._view_y

    top = property((lambda self: self._clip_y), _set_top, doc='Top edge of the text layout (measured from the\n    bottom of the graphics viewport).\n\n    :type: int\n    ')

    def _set_left(self, left):
        self._clip_x = left
        self.translate_x = self._clip_x - self._view_x

    left = property((lambda self: self._clip_x), _set_left, doc='Left edge of the text layout.\n\n    :type: int\n    ')

    def _set_width(self, width):
        self._clip_width = width

    width = property((lambda self: self._clip_width), _set_width, doc='Width of the text layout.\n\n    :type: int\n    ')

    def _set_height(self, height):
        self._clip_height = height

    height = property((lambda self: self._height), _set_height, doc='Height of the text layout.\n\n    :type: int\n    ')

    def _set_view_x(self, view_x):
        self._view_x = view_x
        self.translate_x = self._clip_x - self._view_x

    view_x = property((lambda self: self._view_x), _set_view_x, doc='Horizontal scroll offset.\n\n    :type: int\n    ')

    def _set_view_y(self, view_y):
        self._view_y = view_y
        self.translate_y = self._clip_y - self._view_y

    view_y = property((lambda self: self._view_y), _set_view_y, doc='Vertical scroll offset.\n\n    :type: int\n    ')

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return id(self)


class TextLayoutForegroundGroup(graphics.OrderedGroup):

    def set_state(self):
        glEnable(GL_TEXTURE_2D)


class TextLayoutForegroundDecorationGroup(graphics.OrderedGroup):

    def set_state(self):
        glDisable(GL_TEXTURE_2D)


class TextLayoutTextureGroup(graphics.Group):

    def __init__(self, texture, parent):
        super(TextLayoutTextureGroup, self).__init__(parent)
        self.texture = texture

    def set_state(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)

    def __hash__(self):
        return hash((self.texture.id, self.parent))

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.texture.id == other.texture.id and self.parent is other.parent

    def __repr__(self):
        return '%s(%d, %r)' % (self.__class__.__name__,
         self.texture.id,
         self.parent)


class TextLayout(object):
    _document = None
    _vertex_lists = ()
    _boxes = ()
    top_group = TextLayoutGroup()
    background_group = graphics.OrderedGroup(0, top_group)
    foreground_group = TextLayoutForegroundGroup(1, top_group)
    foreground_decoration_group = TextLayoutForegroundDecorationGroup(2, top_group)
    _update_enabled = True
    _own_batch = False
    _origin_layout = False

    def __init__(self, document, width=None, height=None, multiline=False, dpi=None, batch=None, group=None):
        self.content_width = 0
        self.content_height = 0
        self.groups = {}
        self._init_groups(group)
        if batch is None:
            batch = graphics.Batch()
            self._own_batch = True
        self.batch = batch
        if width is not None:
            self._width = width
        if height is not None:
            self._height = height
        if multiline:
            self._multiline = multiline
        if dpi is None:
            dpi = 96
        self._dpi = dpi
        self.document = document
        return

    def _parse_distance(self, distance):
        if distance is None:
            return
        else:
            return _parse_distance(distance, self._dpi)

    def begin_update(self):
        self._update_enabled = False

    def end_update(self):
        self._update_enabled = True
        self._update()

    dpi = property((lambda self: self._dpi), doc='Get DPI used by this layout.\n\n    Read-only.\n\n    :type: float\n    ')

    def delete(self):
        for vertex_list in self._vertex_lists:
            vertex_list.delete()

        self._vertex_lists = []
        for box in self._boxes:
            box.delete(self)

    def draw(self):
        if self._own_batch:
            self.batch.draw()
        else:
            self.batch.draw_subset(self._vertex_lists)

    def _init_groups(self, group):
        if group:
            self.top_group = TextLayoutGroup(group)
            self.background_group = graphics.OrderedGroup(0, self.top_group)
            self.foreground_group = TextLayoutForegroundGroup(1, self.top_group)
            self.foreground_decoration_group = TextLayoutForegroundDecorationGroup(2, self.top_group)

    def _get_document(self):
        return self._document

    def _set_document(self, document):
        if self._document:
            self._document.remove_handlers(self)
            self._uninit_document()
        document.push_handlers(self)
        self._document = document
        self._init_document()

    document = property(_get_document, _set_document, 'Document to display.\n\n    For `IncrementalTextLayout` it is far more efficient to modify a document\n    in-place than to replace the document instance on the layout.\n\n    :type: `AbstractDocument`\n    ')

    def _get_lines(self):
        len_text = len(self._document.text)
        glyphs = self._get_glyphs()
        owner_runs = runlist.RunList(len_text, None)
        self._get_owner_runs(owner_runs, glyphs, 0, len_text)
        lines = [ line for line in self._flow_glyphs(glyphs, owner_runs, 0, len_text)
                ]
        self.content_width = 0
        self._flow_lines(lines, 0, len(lines))
        return lines

    def _update(self):
        if not self._update_enabled:
            return
        for _vertex_list in self._vertex_lists:
            _vertex_list.delete()

        for box in self._boxes:
            box.delete(self)

        self._vertex_lists = []
        self._boxes = []
        self.groups.clear()
        if not self._document or not self._document.text:
            return
        lines = self._get_lines()
        colors_iter = self._document.get_style_runs('color')
        background_iter = self._document.get_style_runs('background_color')
        if self._origin_layout:
            left = top = 0
        else:
            left = self._get_left()
            top = self._get_top(lines)
        context = _StaticLayoutContext(self, self._document, colors_iter, background_iter)
        for line in lines:
            self._create_vertex_lists(left + line.x, top + line.y, line.start, line.boxes, context)

    def _get_left(self):
        if self._multiline:
            width = self._width
        else:
            width = self.content_width
        if self._anchor_x == 'left':
            return self._x
        if self._anchor_x == 'center':
            return self._x - width // 2
        if self._anchor_x == 'right':
            return self._x - width

    def _get_top(self, lines):
        if self._height is None:
            height = self.content_height
            offset = 0
        else:
            height = self._height
            if self._content_valign == 'top':
                offset = 0
            elif self._content_valign == 'bottom':
                offset = max(0, self._height - self.content_height)
            elif self._content_valign == 'center':
                offset = max(0, self._height - self.content_height) // 2
        if self._anchor_y == 'top':
            return self._y - offset
        else:
            if self._anchor_y == 'baseline':
                return self._y + lines[0].ascent - offset
            if self._anchor_y == 'bottom':
                return self._y + height - offset
            if self._anchor_y == 'center':
                if len(lines) == 1 and self._height is None:
                    line = lines[0]
                    return self._y + line.ascent // 2 - line.descent // 4
                else:
                    return self._y + height // 2 - offset

            return

    def _init_document(self):
        self._update()

    def _uninit_document(self):
        pass

    def on_insert_text(self, start, text):
        self._init_document()

    def on_delete_text(self, start, end):
        self._init_document()

    def on_style_text(self, start, end, attributes):
        self._init_document()

    def _get_glyphs(self):
        glyphs = []
        runs = runlist.ZipRunIterator((
         self._document.get_font_runs(dpi=self._dpi),
         self._document.get_element_runs()))
        text = self._document.text
        for start, end, (font, element) in runs.ranges(0, len(text)):
            if element:
                glyphs.append(_InlineElementBox(element))
            else:
                glyphs.extend(font.get_glyphs(text[start:end]))

        return glyphs

    def _get_owner_runs(self, owner_runs, glyphs, start, end):
        owner = glyphs[start].owner
        run_start = start
        for i, glyph in enumerate(glyphs[start:end]):
            if owner != glyph.owner:
                owner_runs.set_run(run_start, i + start, owner)
                owner = glyph.owner
                run_start = i + start

        owner_runs.set_run(run_start, end, owner)

    def _flow_glyphs(self, glyphs, owner_runs, start, end):
        if not self._multiline:
            for line in self._flow_glyphs_single_line(glyphs, owner_runs, start, end):
                yield line

        else:
            for line in self._flow_glyphs_wrap(glyphs, owner_runs, start, end):
                yield line

    def _flow_glyphs_wrap(self, glyphs, owner_runs, start, end):
        owner_iterator = owner_runs.get_run_iterator().ranges(start, end)
        font_iterator = self._document.get_font_runs(dpi=self._dpi)
        align_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('align'), (lambda value: value in ('left', 'right', 'center')), 'left')
        if self._width is None:
            wrap_iterator = runlist.ConstRunIterator(len(self.document.text), False)
        else:
            wrap_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('wrap'), (lambda value: value in (True, False, 'char', 'word')), True)
        margin_left_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('margin_left'), (lambda value: value is not None), 0)
        margin_right_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('margin_right'), (lambda value: value is not None), 0)
        indent_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('indent'), (lambda value: value is not None), 0)
        kerning_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('kerning'), (lambda value: value is not None), 0)
        tab_stops_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('tab_stops'), (lambda value: value is not None), [])
        line = _Line(start)
        line.align = align_iterator[start]
        line.margin_left = self._parse_distance(margin_left_iterator[start])
        line.margin_right = self._parse_distance(margin_right_iterator[start])
        if start == 0 or self.document.text[start - 1] in '\n\u2029':
            line.paragraph_begin = True
            line.margin_left += self._parse_distance(indent_iterator[start])
        wrap = wrap_iterator[start]
        if self._width is None:
            width = None
        else:
            width = self._width - line.margin_left - line.margin_right
        x = 0
        run_accum = []
        run_accum_width = 0
        eol_ws = 0
        font = None
        for start, end, owner in owner_iterator:
            font = font_iterator[start]
            owner_accum = []
            owner_accum_width = 0
            owner_accum_commit = []
            owner_accum_commit_width = 0
            nokern = True
            index = start
            for text, glyph in zip(self.document.text[start:end], glyphs[start:end]):
                if nokern:
                    kern = 0
                    nokern = False
                else:
                    kern = self._parse_distance(kerning_iterator[index])
                if wrap != 'char' and text in ' \u200b\t':
                    for run in run_accum:
                        line.add_box(run)

                    run_accum = []
                    run_accum_width = 0
                    if text == '\t':
                        for tab_stop in tab_stops_iterator[index]:
                            tab_stop = self._parse_distance(tab_stop)
                            if tab_stop > x + line.margin_left:
                                break
                        else:
                            tab = 50.0
                            tab_stop = ((x + line.margin_left) // tab + 1) * tab

                        kern = int(tab_stop - x - line.margin_left - glyph.advance)
                    owner_accum.append((kern, glyph))
                    owner_accum_commit.extend(owner_accum)
                    owner_accum_commit_width += owner_accum_width + glyph.advance + kern
                    eol_ws += glyph.advance + kern
                    owner_accum = []
                    owner_accum_width = 0
                    x += glyph.advance + kern
                    index += 1
                    next_start = index
                else:
                    new_paragraph = text in '\n\u2029'
                    new_line = text == '\u2028' or new_paragraph
                    if wrap and x + kern + glyph.advance >= width or new_line:
                        if new_line or wrap == 'char':
                            for run in run_accum:
                                line.add_box(run)

                            run_accum = []
                            run_accum_width = 0
                            owner_accum_commit.extend(owner_accum)
                            owner_accum_commit_width += owner_accum_width
                            owner_accum = []
                            owner_accum_width = 0
                            line.length += 1
                            next_start = index
                            if new_line:
                                next_start += 1
                        if owner_accum_commit:
                            line.add_box(_GlyphBox(owner, font, owner_accum_commit, owner_accum_commit_width))
                            owner_accum_commit = []
                            owner_accum_commit_width = 0
                        if new_line and not line.boxes:
                            line.ascent = font.ascent
                            line.descent = font.descent
                        if line.boxes or new_line:
                            line.width -= eol_ws
                            if new_paragraph:
                                line.paragraph_end = True
                            yield line
                            line = _Line(next_start)
                            line.align = align_iterator[next_start]
                            line.margin_left = self._parse_distance(margin_left_iterator[next_start])
                            line.margin_right = self._parse_distance(margin_right_iterator[next_start])
                            if new_paragraph:
                                line.paragraph_begin = True
                            if run_accum:
                                k, g = run_accum[0].glyphs[0]
                                run_accum[0].glyphs[0] = (0, g)
                                run_accum_width -= k
                            elif owner_accum:
                                k, g = owner_accum[0]
                                owner_accum[0] = (0, g)
                                owner_accum_width -= k
                            else:
                                nokern = True
                            x = run_accum_width + owner_accum_width
                            width = self._width - line.margin_left - line.margin_right
                    if isinstance(glyph, _AbstractBox):
                        run_accum.append(glyph)
                        run_accum_width += glyph.advance
                        x += glyph.advance
                    elif new_paragraph:
                        wrap = wrap_iterator[next_start]
                        line.margin_left += self._parse_distance(indent_iterator[next_start])
                        if width is not None:
                            width = self._width - line.margin_left - line.margin_right
                    elif not new_line:
                        owner_accum.append((kern, glyph))
                        owner_accum_width += glyph.advance + kern
                        x += glyph.advance + kern
                    index += 1
                    eol_ws = 0

            if owner_accum_commit:
                line.add_box(_GlyphBox(owner, font, owner_accum_commit, owner_accum_commit_width))
            if owner_accum:
                run_accum.append(_GlyphBox(owner, font, owner_accum, owner_accum_width))
                run_accum_width += owner_accum_width

        for run in run_accum:
            line.add_box(run)

        if not line.boxes:
            if font is None:
                font = self._document.get_font(0, dpi=self._dpi)
            line.ascent = font.ascent
            line.descent = font.descent
        yield line
        return

    def _flow_glyphs_single_line(self, glyphs, owner_runs, start, end):
        owner_iterator = owner_runs.get_run_iterator().ranges(start, end)
        font_iterator = self.document.get_font_runs(dpi=self._dpi)
        kern_iterator = runlist.FilteredRunIterator(self.document.get_style_runs('kerning'), (lambda value: value is not None), 0)
        line = _Line(start)
        font = font_iterator[0]
        for start, end, owner in owner_iterator:
            font = font_iterator[start]
            width = 0
            owner_glyphs = []
            for kern_start, kern_end, kern in kern_iterator.ranges(start, end):
                gs = glyphs[kern_start:kern_end]
                width += sum([ g.advance for g in gs ])
                width += kern * (kern_end - kern_start)
                owner_glyphs.extend(zip([kern] * (kern_end - kern_start), gs))

            if owner is None:
                for kern, glyph in owner_glyphs:
                    line.add_box(glyph)

            else:
                line.add_box(_GlyphBox(owner, font, owner_glyphs, width))

        if not line.boxes:
            line.ascent = font.ascent
            line.descent = font.descent
        line.paragraph_begin = line.paragraph_end = True
        yield line
        return

    def _flow_lines(self, lines, start, end):
        margin_top_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('margin_top'), (lambda value: value is not None), 0)
        margin_bottom_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('margin_bottom'), (lambda value: value is not None), 0)
        line_spacing_iterator = self._document.get_style_runs('line_spacing')
        leading_iterator = runlist.FilteredRunIterator(self._document.get_style_runs('leading'), (lambda value: value is not None), 0)
        if start == 0:
            y = 0
        else:
            line = lines[start - 1]
            line_spacing = self._parse_distance(line_spacing_iterator[line.start])
            leading = self._parse_distance(leading_iterator[line.start])
            y = line.y
            if line_spacing is None:
                y += line.descent
            if line.paragraph_end:
                y -= self._parse_distance(margin_bottom_iterator[line.start])
            line_index = start
            for line in lines[start:]:
                if line.paragraph_begin:
                    y -= self._parse_distance(margin_top_iterator[line.start])
                    line_spacing = self._parse_distance(line_spacing_iterator[line.start])
                    leading = self._parse_distance(leading_iterator[line.start])
                else:
                    y -= leading
                if line_spacing is None:
                    y -= line.ascent
                else:
                    y -= line_spacing
                if line.align == 'left' or line.width > self.width:
                    line.x = line.margin_left
                elif line.align == 'center':
                    line.x = (self.width - line.margin_left - line.margin_right - line.width) // 2 + line.margin_left
                elif line.align == 'right':
                    line.x = self.width - line.margin_right - line.width
                self.content_width = max(self.content_width, line.width + line.margin_left)
                if line.y == y and line_index >= end:
                    break
                line.y = y
                if line_spacing is None:
                    y += line.descent
                if line.paragraph_end:
                    y -= self._parse_distance(margin_bottom_iterator[line.start])
                line_index += 1

            self.content_height = -y
        return line_index

    def _create_vertex_lists(self, x, y, i, boxes, context):
        for box in boxes:
            box.place(self, i, x, y, context)
            x += box.advance
            i += box.length

    _x = 0

    def _set_x(self, x):
        if self._boxes:
            self._x = x
            self._update()
        else:
            dx = x - self._x
            l_dx = lambda x: int(x + dx)
            for vertex_list in self._vertex_lists:
                vertices = vertex_list.vertices[:]
                vertices[::2] = map(l_dx, vertices[::2])
                vertex_list.vertices[:] = vertices

            self._x = x

    def _get_x(self):
        return self._x

    x = property(_get_x, _set_x, doc='X coordinate of the layout.\n\n    See also `anchor_x`.\n\n    :type: int\n    ')
    _y = 0

    def _set_y(self, y):
        if self._boxes:
            self._y = y
            self._update()
        else:
            dy = y - self._y
            l_dy = lambda y: int(y + dy)
            for vertex_list in self._vertex_lists:
                vertices = vertex_list.vertices[:]
                vertices[1::2] = map(l_dy, vertices[1::2])
                vertex_list.vertices[:] = vertices

            self._y = y

    def _get_y(self):
        return self._y

    y = property(_get_y, _set_y, doc='Y coordinate of the layout.\n\n    See also `anchor_y`.\n\n    :type: int\n    ')
    _width = None

    def _set_width(self, width):
        self._width = width
        self._update()

    def _get_width(self):
        return self._width

    width = property(_get_width, _set_width, doc='Width of the layout.\n                     \n    This property has no effect if `multiline` is False.\n\n    :type: int\n    ')
    _height = None

    def _set_height(self, height):
        self._height = height
        self._update()

    def _get_height(self):
        return self._height

    height = property(_get_height, _set_height, doc='Height of the layout.\n                      \n    :type: int\n    ')
    _multiline = False

    def _set_multiline(self, multiline):
        self._multiline = multiline
        self._update()

    def _get_multiline(self):
        return self._multiline

    multiline = property(_get_multiline, _set_multiline, doc='Set if multiline layout is enabled.\n\n    If multiline is False, newline and paragraph characters are ignored and\n    text is not word-wrapped.\n                         \n    :type: bool\n    ')
    _anchor_x = 'left'

    def _set_anchor_x(self, anchor_x):
        self._anchor_x = anchor_x
        self._update()

    def _get_anchor_x(self):
        return self._anchor_x

    anchor_x = property(_get_anchor_x, _set_anchor_x, doc='Horizontal anchor alignment.\n                      \n    This property determines the meaning of the `x` coordinate.  It is one of\n    the enumerants:\n\n    ``"left"`` (default)\n        The X coordinate gives the position of the left edge of the layout.\n    ``"center"``\n        The X coordinate gives the position of the center of the layout.\n    ``"right"``\n        The X coordinate gives the position of the right edge of the layout.\n\n    For the purposes of calculating the position resulting from this\n    alignment, the width of the layout is taken to be `width` if `multiline`\n    is True, otherwise `content_width`.\n\n    :type: str\n    ')
    _anchor_y = 'bottom'

    def _set_anchor_y(self, anchor_y):
        self._anchor_y = anchor_y
        self._update()

    def _get_anchor_y(self):
        return self._anchor_y

    anchor_y = property(_get_anchor_y, _set_anchor_y, doc='Vertical anchor alignment.\n                      \n    This property determines the meaning of the `y` coordinate.  It is one of\n    the enumerants:\n\n    ``"top"``\n        The Y coordinate gives the position of the top edge of the layout.\n    ``"center"``\n        The Y coordinate gives the position of the center of the layout.\n    ``"baseline"``\n        The Y coordinate gives the position of the baseline of the first\n        line of text in the layout.\n    ``"bottom"`` (default)\n        The Y coordinate gives the position of the bottom edge of the layout.\n\n    For the purposes of calculating the position resulting from this\n    alignment, the height of the layout is taken to be the smaller of\n    `height` and `content_height`.\n\n    See also `content_valign`.\n\n    :type: str\n    ')
    _content_valign = 'top'

    def _set_content_valign(self, content_valign):
        self._content_valign = content_valign
        self._update()

    def _get_content_valign(self):
        return self._content_valign

    content_valign = property(_get_content_valign, _set_content_valign, doc='Vertical alignment of content within\n    larger layout box.\n\n    This property determines how content is positioned within the layout\n    box when ``content_height`` is less than ``height``.  It is one\n    of the enumerants:\n\n    ``top`` (default)\n        Content is aligned to the top of the layout box.\n    ``center``\n        Content is centered vertically within the layout box.\n    ``bottom``\n        Content is aligned to the bottom of the layout box.\n\n    This property has no effect when ``content_height`` is greater\n    than ``height`` (in which case the content is aligned to the top) or when\n    ``height`` is ``None`` (in which case there is no vertical layout box\n    dimension).\n\n    :type: str\n    ')


class ScrollableTextLayout(TextLayout):
    _origin_layout = True

    def __init__(self, document, width, height, multiline=False, dpi=None, batch=None, group=None):
        super(ScrollableTextLayout, self).__init__(document, width, height, multiline, dpi, batch, group)
        self.top_group.width = self._width
        self.top_group.height = self._height

    def _init_groups(self, group):
        self.top_group = ScrollableTextLayoutGroup(group)
        self.background_group = graphics.OrderedGroup(0, self.top_group)
        self.foreground_group = TextLayoutForegroundGroup(1, self.top_group)
        self.foreground_decoration_group = TextLayoutForegroundDecorationGroup(2, self.top_group)

    def _set_x(self, x):
        self._x = x
        self.top_group.left = self._get_left()

    def _get_x(self):
        return self._x

    x = property(_get_x, _set_x)

    def _set_y(self, y):
        self._y = y
        self.top_group.top = self._get_top(self._get_lines())

    def _get_y(self):
        return self._y

    y = property(_get_y, _set_y)

    def _set_width(self, width):
        super(ScrollableTextLayout, self)._set_width(width)
        self.top_group.left = self._get_left()
        self.top_group.width = self._width

    def _get_width(self):
        return self._width

    width = property(_get_width, _set_width)

    def _set_height(self, height):
        super(ScrollableTextLayout, self)._set_height(height)
        self.top_group.top = self._get_top(self._get_lines())
        self.top_group.height = self._height

    def _get_height(self):
        return self._height

    height = property(_get_height, _set_height)

    def _set_anchor_x(self, anchor_x):
        self._anchor_x = anchor_x
        self.top_group.left = self._get_left()

    def _get_anchor_x(self):
        return self._anchor_x

    anchor_x = property(_get_anchor_x, _set_anchor_x)

    def _set_anchor_y(self, anchor_y):
        self._anchor_y = anchor_y
        self.top_group.top = self._get_top(self._get_lines())

    def _get_anchor_y(self):
        return self._anchor_y

    anchor_y = property(_get_anchor_y, _set_anchor_y)

    def _set_view_x(self, view_x):
        view_x = max(0, min(self.content_width - self.width, view_x))
        self.top_group.view_x = view_x

    def _get_view_x(self):
        return self.top_group.view_x

    view_x = property(_get_view_x, _set_view_x, doc='Horizontal scroll offset.\n\n    The initial value is 0, and the left edge of the text will touch the left\n    side of the layout bounds.  A positive value causes the text to "scroll"\n    to the right.  Values are automatically clipped into the range\n    ``[0, content_width - width]``\n                      \n    :type: int\n    ')

    def _set_view_y(self, view_y):
        view_y = min(0, max(self.height - self.content_height, view_y))
        self.top_group.view_y = view_y

    def _get_view_y(self):
        return self.top_group.view_y

    view_y = property(_get_view_y, _set_view_y, doc='Vertical scroll offset.\n\n    The initial value is 0, and the top of the text will touch the top of the\n    layout bounds (unless the content height is less than the layout height,\n    in which case `content_valign` is used).  \n    \n    A negative value causes the text to "scroll" upwards.  Values outside of\n    the range ``[height - content_height, 0]`` are automatically clipped in\n    range.\n\n    :type: int\n    ')


class IncrementalTextLayout(ScrollableTextLayout, event.EventDispatcher):
    _selection_start = 0
    _selection_end = 0
    _selection_color = [255, 255, 255, 255]
    _selection_background_color = [46, 106, 197, 255]

    def __init__(self, document, width, height, multiline=False, dpi=None, batch=None, group=None):
        event.EventDispatcher.__init__(self)
        self.glyphs = []
        self.lines = []
        self.invalid_glyphs = _InvalidRange()
        self.invalid_flow = _InvalidRange()
        self.invalid_lines = _InvalidRange()
        self.invalid_style = _InvalidRange()
        self.invalid_vertex_lines = _InvalidRange()
        self.visible_lines = _InvalidRange()
        self.owner_runs = runlist.RunList(0, None)
        ScrollableTextLayout.__init__(self, document, width, height, multiline, dpi, batch, group)
        self.top_group.width = width
        self.top_group.left = self._get_left()
        self.top_group.height = height
        self.top_group.top = self._get_top(self._get_lines())
        return

    def _init_document(self):
        self.on_insert_text(0, self._document.text)

    def _uninit_document(self):
        self.on_delete_text(0, len(self._document.text))

    def _get_lines(self):
        return self.lines

    def delete(self):
        for line in self.lines:
            line.delete(self)

        self.batch = None
        if self._document:
            self._document.remove_handlers(self)
        self._document = None
        return

    def on_insert_text(self, start, text):
        len_text = len(text)
        self.glyphs[start:start] = [None] * len_text
        self.invalid_glyphs.insert(start, len_text)
        self.invalid_flow.insert(start, len_text)
        self.invalid_style.insert(start, len_text)
        self.owner_runs.insert(start, len_text)
        for line in self.lines:
            if line.start >= start:
                line.start += len_text

        self._update()
        return

    def on_delete_text(self, start, end):
        self.glyphs[start:end] = []
        self.invalid_glyphs.delete(start, end)
        self.invalid_flow.delete(start, end)
        self.invalid_style.delete(start, end)
        self.owner_runs.delete(start, end)
        size = end - start
        for line in self.lines:
            if line.start > start:
                line.start = max(line.start - size, start)

        if start == 0:
            self.invalid_flow.invalidate(0, 1)
        else:
            self.invalid_flow.invalidate(start - 1, start)
        self._update()

    def on_style_text(self, start, end, attributes):
        if 'font_name' in attributes or 'font_size' in attributes or 'bold' in attributes or 'italic' in attributes:
            self.invalid_glyphs.invalidate(start, end)
        elif False:
            self.invalid_flow.invalidate(start, end)
        elif 'color' in attributes or 'background_color' in attributes:
            self.invalid_style.invalidate(start, end)
        self._update()

    def _update(self):
        if not self._update_enabled:
            return
        trigger_update_event = self.invalid_glyphs.is_invalid() or self.invalid_flow.is_invalid() or self.invalid_lines.is_invalid()
        if not self.glyphs:
            for line in self.lines:
                line.delete(self)

            del self.lines[:]
            self.lines.append(_Line(0))
            font = self.document.get_font(0, dpi=self._dpi)
            self.lines[0].ascent = font.ascent
            self.lines[0].descent = font.descent
            self.lines[0].paragraph_begin = self.lines[0].paragraph_end = True
            self.invalid_lines.invalidate(0, 1)
        self._update_glyphs()
        self._update_flow_glyphs()
        self._update_flow_lines()
        self._update_visible_lines()
        self._update_vertex_lists()
        self.top_group.top = self._get_top(self.lines)
        self.view_y = self.view_y
        self.top_group.top = self._get_top(self._get_lines())
        if trigger_update_event:
            self.dispatch_event('on_layout_update')

    def _update_glyphs(self):
        invalid_start, invalid_end = self.invalid_glyphs.validate()
        if invalid_end - invalid_start <= 0:
            return
        text = self.document.text
        while invalid_start > 0:
            if _grapheme_break(text[invalid_start - 1], text[invalid_start]):
                break
            invalid_start -= 1

        len_text = len(text)
        while invalid_end < len_text:
            if _grapheme_break(text[invalid_end - 1], text[invalid_end]):
                break
            invalid_end += 1

        runs = runlist.ZipRunIterator((
         self._document.get_font_runs(dpi=self._dpi),
         self._document.get_element_runs()))
        for start, end, (font, element) in runs.ranges(invalid_start, invalid_end):
            if element:
                self.glyphs[start] = _InlineElementBox(element)
            else:
                text = self.document.text[start:end]
                self.glyphs[start:end] = font.get_glyphs(text)

        self._get_owner_runs(self.owner_runs, self.glyphs, invalid_start, invalid_end)
        self.invalid_flow.invalidate(invalid_start, invalid_end)

    def _update_flow_glyphs(self):
        invalid_start, invalid_end = self.invalid_flow.validate()
        if invalid_end - invalid_start <= 0:
            return
        line_index = 0
        for i, line in enumerate(self.lines):
            if line.start >= invalid_start:
                break
            line_index = i

        line_index = max(0, line_index - 1)
        try:
            line = self.lines[line_index]
            invalid_start = min(invalid_start, line.start)
            line.delete(self)
            line = self.lines[line_index] = _Line(invalid_start)
            self.invalid_lines.invalidate(line_index, line_index + 1)
        except IndexError:
            line_index = 0
            invalid_start = 0
            line = _Line(0)
            self.lines.append(line)
            self.invalid_lines.insert(0, 1)

        content_width_invalid = False
        next_start = invalid_start
        for line in self._flow_glyphs(self.glyphs, self.owner_runs, invalid_start, len(self._document.text)):
            try:
                old_line = self.lines[line_index]
                old_line.delete(self)
                old_line_width = old_line.width + old_line.margin_left
                new_line_width = line.width + line.margin_left
                if old_line_width == self.content_width and new_line_width < old_line_width:
                    content_width_invalid = True
                self.lines[line_index] = line
                self.invalid_lines.invalidate(line_index, line_index + 1)
            except IndexError:
                self.lines.append(line)
                self.invalid_lines.insert(line_index, 1)

            next_start = line.start + line.length
            line_index += 1
            try:
                next_line = self.lines[line_index]
                if next_start == next_line.start and next_start > invalid_end:
                    break
            except IndexError:
                pass

        else:
            if next_start == len(self._document.text) and line_index > 0:
                for line in self.lines[line_index:]:
                    old_line_width = old_line.width + old_line.margin_left
                    if old_line_width == self.content_width:
                        content_width_invalid = True
                    line.delete(self)

                del self.lines[line_index:]
            if content_width_invalid:
                content_width = 0
                for line in self.lines:
                    content_width = max(line.width + line.margin_left, content_width)

                self.content_width = content_width

    def _update_flow_lines(self):
        invalid_start, invalid_end = self.invalid_lines.validate()
        if invalid_end - invalid_start <= 0:
            return
        invalid_end = self._flow_lines(self.lines, invalid_start, invalid_end)
        self.invalid_vertex_lines.invalidate(invalid_start, invalid_end)

    def _update_visible_lines(self):
        start = sys.maxint
        end = 0
        for i, line in enumerate(self.lines):
            if line.y + line.descent < self.view_y:
                start = min(start, i)
            if line.y + line.ascent > self.view_y - self.height:
                end = max(end, i) + 1

        for i in range(self.visible_lines.start, min(start, len(self.lines))):
            self.lines[i].delete(self)

        for i in range(end, min(self.visible_lines.end, len(self.lines))):
            self.lines[i].delete(self)

        self.invalid_vertex_lines.invalidate(start, self.visible_lines.start)
        self.invalid_vertex_lines.invalidate(self.visible_lines.end, end)
        self.visible_lines.start = start
        self.visible_lines.end = end

    def _update_vertex_lists(self):
        style_invalid_start, style_invalid_end = self.invalid_style.validate()
        self.invalid_vertex_lines.invalidate(self.get_line_from_position(style_invalid_start), self.get_line_from_position(style_invalid_end) + 1)
        invalid_start, invalid_end = self.invalid_vertex_lines.validate()
        if invalid_end - invalid_start <= 0:
            return
        colors_iter = self.document.get_style_runs('color')
        background_iter = self.document.get_style_runs('background_color')
        if self._selection_end - self._selection_start > 0:
            colors_iter = runlist.OverriddenRunIterator(colors_iter, self._selection_start, self._selection_end, self._selection_color)
            background_iter = runlist.OverriddenRunIterator(background_iter, self._selection_start, self._selection_end, self._selection_background_color)
        context = _IncrementalLayoutContext(self, self._document, colors_iter, background_iter)
        for line in self.lines[invalid_start:invalid_end]:
            line.delete(self)
            context.line = line
            y = line.y
            if y + line.descent > self.view_y:
                continue
            elif y + line.ascent < self.view_y - self.height:
                break
            self._create_vertex_lists(line.x, y, line.start, line.boxes, context)

    def _set_width(self, width):
        if width == self._width:
            return
        self.invalid_flow.invalidate(0, len(self.document.text))
        super(IncrementalTextLayout, self)._set_width(width)

    def _get_width(self):
        return self._width

    width = property(_get_width, _set_width)

    def _set_height(self, height):
        if height == self._height:
            return
        super(IncrementalTextLayout, self)._set_height(height)
        if self._update_enabled:
            self._update_visible_lines()
            self._update_vertex_lists()

    def _get_height(self):
        return self._height

    height = property(_get_height, _set_height)

    def _set_multiline(self, multiline):
        self.invalid_flow.invalidate(0, len(self.document.text))
        super(IncrementalTextLayout, self)._set_multiline(multiline)

    def _get_multiline(self):
        return self._multiline

    multiline = property(_get_multiline, _set_multiline)

    def _set_view_y(self, view_y):
        super(IncrementalTextLayout, self)._set_view_y(view_y)
        self._update_visible_lines()
        self._update_vertex_lists()

    def _get_view_y(self):
        return self.top_group.view_y

    view_y = property(_get_view_y, _set_view_y)

    def set_selection(self, start, end):
        start = max(0, start)
        end = min(end, len(self.document.text))
        if start == self._selection_start and end == self._selection_end:
            return
        if end > self._selection_start and start < self._selection_end:
            self.invalid_style.invalidate(min(start, self._selection_start), max(start, self._selection_start))
            self.invalid_style.invalidate(min(end, self._selection_end), max(end, self._selection_end))
        else:
            self.invalid_style.invalidate(self._selection_start, self._selection_end)
            self.invalid_style.invalidate(start, end)
        self._selection_start = start
        self._selection_end = end
        self._update()

    selection_start = property((lambda self: self._selection_start), (lambda self, v: self.set_selection(v, self._selection_end)), doc='Starting position of the active selection.\n\n    :see: `set_selection`\n\n    :type: int\n    ')
    selection_end = property((lambda self: self._selection_end), (lambda self, v: self.set_selection(self._selection_start, v)), doc='End position of the active selection (exclusive).\n\n    :see: `set_selection`\n\n    :type: int\n    ')

    def _get_selection_color(self):
        return self._selection_color

    def _set_selection_color(self, color):
        self._selection_color = color
        self.invalid_style.invalidate(self._selection_start, self._selection_end)

    selection_color = property(_get_selection_color, _set_selection_color, doc='Text color of active selection.\n\n    The color is an RGBA tuple with components in range [0, 255].\n\n    :type: (int, int, int, int)\n    ')

    def _get_selection_background_color(self):
        return self._selection_background_color

    def _set_selection_background_color(self, background_color):
        self._selection_background_color = background_color
        self.invalid_style.invalidate(self._selection_start, self._selection_end)

    selection_background_color = property(_get_selection_background_color, _set_selection_background_color, doc='Background color of active\n    selection.\n\n    The color is an RGBA tuple with components in range [0, 255].\n\n    :type: (int, int, int, int)\n    ')

    def get_position_from_point(self, x, y):
        line = self.get_line_from_point(x, y)
        return self.get_position_on_line(line, x)

    def get_point_from_position(self, position, line=None):
        if line is None:
            line = self.lines[0]
            for next_line in self.lines:
                if next_line.start > position:
                    break
                line = next_line

        else:
            line = self.lines[line]
        x = line.x
        baseline = self._document.get_style('baseline', max(0, position - 1))
        if baseline is None:
            baseline = 0
        else:
            baseline = self._parse_distance(baseline)
        position -= line.start
        for box in line.boxes:
            if position - box.length <= 0:
                x += box.get_point_in_box(position)
                break
            position -= box.length
            x += box.advance

        return (x + self.top_group.translate_x,
         line.y + self.top_group.translate_y + baseline)

    def get_line_from_point(self, x, y):
        x -= self.top_group.translate_x
        y -= self.top_group.translate_y
        line_index = 0
        for line in self.lines:
            if y > line.y + line.descent:
                break
            line_index += 1

        if line_index >= len(self.lines):
            line_index = len(self.lines) - 1
        return line_index

    def get_point_from_line(self, line):
        line = self.lines[line]
        return (line.x + self.top_group.translate_x,
         line.y + self.top_group.translate_y)

    def get_line_from_position(self, position):
        line = -1
        for next_line in self.lines:
            if next_line.start > position:
                break
            line += 1

        return line

    def get_position_from_line(self, line):
        return self.lines[line].start

    def get_position_on_line(self, line, x):
        line = self.lines[line]
        x -= self.top_group.translate_x
        position = line.start
        last_glyph_x = line.x
        for box in line.boxes:
            if 0 <= x - last_glyph_x < box.advance:
                position += box.get_position_in_box(x - last_glyph_x)
                break
            last_glyph_x += box.advance
            position += box.length

        return position

    def get_line_count(self):
        return len(self.lines)

    def ensure_line_visible(self, line):
        line = self.lines[line]
        y1 = line.y + line.ascent
        y2 = line.y + line.descent
        if y1 > self.view_y:
            self.view_y = y1
        elif y2 < self.view_y - self.height:
            self.view_y = y2 + self.height

    def ensure_x_visible(self, x):
        if x <= self.view_x + 10:
            self.view_x = x - 10
        elif x >= self.view_x + self.width:
            self.view_x = x - self.width + 10
        elif x >= self.view_x + self.width - 10 and self.content_width > self.width:
            self.view_x = x - self.width + 10

    if _is_epydoc:

        def on_layout_update(self):
            pass


IncrementalTextLayout.register_event_type('on_layout_update')
# okay decompiling out\pyglet.text.layout.pyc
