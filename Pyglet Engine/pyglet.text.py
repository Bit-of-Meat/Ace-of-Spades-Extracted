# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import os.path, pyglet
from pyglet.text import layout, document, caret

class DocumentDecodeException(Exception):
    pass


class DocumentDecoder(object):

    def decode(self, text, location=None):
        raise NotImplementedError('abstract')


def get_decoder(filename, mimetype=None):
    if mimetype is None:
        _, ext = os.path.splitext(filename)
        if ext.lower() in ('.htm', '.html', '.xhtml'):
            mimetype = 'text/html'
        else:
            mimetype = 'text/plain'
    if mimetype == 'text/plain':
        from pyglet.text.formats import plaintext
        return plaintext.PlainTextDecoder()
    else:
        if mimetype == 'text/html':
            from pyglet.text.formats import html
            return html.HTMLDecoder()
        if mimetype == 'text/vnd.pyglet-attributed':
            from pyglet.text.formats import attributed
            return attributed.AttributedTextDecoder()
        raise DocumentDecodeException('Unknown format "%s"' % mimetype)
        return


def load(filename, file=None, mimetype=None):
    decoder = get_decoder(filename, mimetype)
    if file is None:
        file = open(filename)
    location = pyglet.resource.FileLocation(os.path.dirname(filename))
    return decoder.decode(file.read(), location)


def decode_html(text, location=None):
    decoder = get_decoder(None, 'text/html')
    return decoder.decode(text, location)


def decode_attributed(text):
    decoder = get_decoder(None, 'text/vnd.pyglet-attributed')
    return decoder.decode(text)


def decode_text(text):
    decoder = get_decoder(None, 'text/plain')
    return decoder.decode(text)


class DocumentLabel(layout.TextLayout):

    def __init__(self, document=None, x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='baseline', multiline=False, dpi=None, batch=None, group=None):
        super(DocumentLabel, self).__init__(document, width=width, height=height, multiline=multiline, dpi=dpi, batch=batch, group=group)
        self._x = x
        self._y = y
        self._anchor_x = anchor_x
        self._anchor_y = anchor_y
        self._update()

    def _get_text(self):
        return self.document.text

    def _set_text(self, text):
        self.document.text = text

    text = property(_get_text, _set_text, doc='The text of the label.\n                    \n    :type: str\n    ')

    def _get_color(self):
        return self.document.get_style('color')

    def _set_color(self, color):
        self.document.set_style(0, len(self.document.text), {'color': color})

    color = property(_get_color, _set_color, doc='Text color.\n\n    Color is a 4-tuple of RGBA components, each in range [0, 255].\n\n    :type: (int, int, int, int)\n    ')

    def _get_font_name(self):
        return self.document.get_style('font_name')

    def _set_font_name(self, font_name):
        self.document.set_style(0, len(self.document.text), {'font_name': font_name})

    font_name = property(_get_font_name, _set_font_name, doc='Font family name.\n\n    The font name, as passed to `pyglet.font.load`.  A list of names can\n    optionally be given: the first matching font will be used.\n\n    :type: str or list\n    ')

    def _get_font_size(self):
        return self.document.get_style('font_size')

    def _set_font_size(self, font_size):
        self.document.set_style(0, len(self.document.text), {'font_size': font_size})

    font_size = property(_get_font_size, _set_font_size, doc='Font size, in points.\n\n    :type: float\n    ')

    def _get_bold(self):
        return self.document.get_style('bold')

    def _set_bold(self, bold):
        self.document.set_style(0, len(self.document.text), {'bold': bold})

    bold = property(_get_bold, _set_bold, doc='Bold font style.\n\n    :type: bool\n    ')

    def _get_italic(self):
        return self.document.get_style('italic')

    def _set_italic(self, italic):
        self.document.set_style(0, len(self.document.text), {'italic': italic})

    italic = property(_get_italic, _set_italic, doc='Italic font style.\n                      \n    :type: bool\n    ')

    def get_style(self, name):
        return self.document.get_style_range(name, 0, len(self.document.text))

    def set_style(self, name, value):
        self.document.set_style(0, len(self.document.text), {name: value})


class Label(DocumentLabel):

    def __init__(self, text='', font_name=None, font_size=None, bold=False, italic=False, color=(255, 255, 255, 255), x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='baseline', align='left', multiline=False, dpi=None, batch=None, group=None):
        document = decode_text(text)
        super(Label, self).__init__(document, x, y, width, height, anchor_x, anchor_y, multiline, dpi, batch, group)
        self.document.set_style(0, len(self.document.text), {'font_name': font_name, 
           'font_size': font_size, 
           'bold': bold, 
           'italic': italic, 
           'color': color, 
           'align': align})


class HTMLLabel(DocumentLabel):

    def __init__(self, text='', location=None, x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='baseline', multiline=False, dpi=None, batch=None, group=None):
        self._text = text
        self._location = location
        document = decode_html(text, location)
        super(HTMLLabel, self).__init__(document, x, y, width, height, anchor_x, anchor_y, multiline, dpi, batch, group)

    def _set_text(self, text):
        self._text = text
        self.document = decode_html(text, self._location)

    def _get_text(self):
        return self._text

    text = property(_get_text, _set_text, doc='HTML formatted text of the label.\n\n    :type: str\n    ')
# okay decompiling out\pyglet.text.pyc
