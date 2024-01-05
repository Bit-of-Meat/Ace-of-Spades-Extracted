# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.formats.structured
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import re, pyglet

class ImageElement(pyglet.text.document.InlineElement):

    def __init__(self, image, width=None, height=None):
        self.image = image.get_texture()
        self.width = width is None and image.width or width
        self.height = height is None and image.height or height
        self.vertex_lists = {}
        anchor_y = self.height // image.height * image.anchor_y
        ascent = max(0, self.height - anchor_y)
        descent = min(0, -anchor_y)
        super(ImageElement, self).__init__(ascent, descent, self.width)
        return

    def place(self, layout, x, y):
        group = pyglet.graphics.TextureGroup(self.image.texture, layout.top_group)
        x1 = x
        y1 = y + self.descent
        x2 = x + self.width
        y2 = y + self.height + self.descent
        vertex_list = layout.batch.add(4, pyglet.gl.GL_QUADS, group, (
         'v2i', (x1, y1, x2, y1, x2, y2, x1, y2)), (
         'c3B', (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255)), (
         't3f', self.image.tex_coords))
        self.vertex_lists[layout] = vertex_list

    def remove(self, layout):
        self.vertex_lists[layout].delete()
        del self.vertex_lists[layout]


def _int_to_roman(input):
    if not 0 < input < 4000:
        raise ValueError, 'Argument must be between 1 and 3999'
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ''
    for i in range(len(ints)):
        count = int(input / ints[i])
        result += nums[i] * count
        input -= ints[i] * count

    return result


class ListBuilder(object):

    def begin(self, decoder, style):
        left_margin = decoder.current_style.get('margin_left') or 0
        tab_stops = decoder.current_style.get('tab_stops')
        if tab_stops:
            tab_stops = list(tab_stops)
        else:
            tab_stops = []
        tab_stops.append(left_margin + 50)
        style['margin_left'] = left_margin + 50
        style['indent'] = -30
        style['tab_stops'] = tab_stops

    def item(self, decoder, style, value=None):
        mark = self.get_mark(value)
        if mark:
            decoder.add_text(mark)
        decoder.add_text('\t')

    def get_mark(self, value=None):
        return ''


class UnorderedListBuilder(ListBuilder):

    def __init__(self, mark):
        self.mark = mark

    def get_mark(self, value):
        return self.mark


class OrderedListBuilder(ListBuilder):
    format_re = re.compile('(.*?)([1aAiI])(.*)')

    def __init__(self, start, format):
        self.next_value = start
        self.prefix, self.numbering, self.suffix = self.format_re.match(format).groups()

    def get_mark(self, value):
        if value is None:
            value = self.next_value
        self.next_value = value + 1
        if self.numbering in 'aA':
            try:
                mark = 'abcdefghijklmnopqrstuvwxyz'[value - 1]
            except ValueError:
                mark = '?'

            if self.numbering == 'A':
                mark = mark.upper()
            return '%s%s%s' % (self.prefix, mark, self.suffix)
        else:
            if self.numbering in 'iI':
                try:
                    mark = _int_to_roman(value)
                except ValueError:
                    mark = '?'

                if self.numbering == 'i':
                    mark = mark.lower()
                return '%s%s%s' % (self.prefix, mark, self.suffix)
            else:
                return '%s%d%s' % (self.prefix, value, self.suffix)

            return


class StructuredTextDecoder(pyglet.text.DocumentDecoder):

    def decode(self, text, location=None):
        self.len_text = 0
        self.current_style = {}
        self.next_style = {}
        self.stack = []
        self.list_stack = []
        self.document = pyglet.text.document.FormattedDocument()
        if location is None:
            location = pyglet.resource.FileLocation('')
        self.decode_structured(text, location)
        return self.document

    def decode_structured(self, text, location):
        raise NotImplementedError('abstract')

    def push_style(self, key, styles):
        old_styles = {}
        for name in styles.keys():
            old_styles[name] = self.current_style.get(name)

        self.stack.append((key, old_styles))
        self.current_style.update(styles)
        self.next_style.update(styles)

    def pop_style(self, key):
        for match, _ in self.stack:
            if key == match:
                break
        else:
            return

        while True:
            match, old_styles = self.stack.pop()
            self.next_style.update(old_styles)
            self.current_style.update(old_styles)
            if match == key:
                break

    def add_text(self, text):
        self.document.insert_text(self.len_text, text, self.next_style)
        self.next_style.clear()
        self.len_text += len(text)

    def add_element(self, element):
        self.document.insert_element(self.len_text, element, self.next_style)
        self.next_style.clear()
        self.len_text += 1
# okay decompiling out\pyglet.text.formats.structured.pyc
