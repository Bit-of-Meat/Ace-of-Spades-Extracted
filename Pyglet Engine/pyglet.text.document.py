# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.document
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import re, sys
from pyglet import event
from pyglet.text import runlist
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc
STYLE_INDETERMINATE = 'indeterminate'

class InlineElement(object):

    def __init__(self, ascent, descent, advance):
        self.ascent = ascent
        self.descent = descent
        self.advance = advance
        self._position = None
        return

    position = property((lambda self: self._position), doc='Position of the element within the\n        document.  Read-only.\n\n        :type: int\n        ')

    def place(self, layout, x, y):
        raise NotImplementedError('abstract')

    def remove(self, layout):
        raise NotImplementedError('abstract')


class AbstractDocument(event.EventDispatcher):
    _previous_paragraph_re = re.compile('\n[^\n\u2029]*$')
    _next_paragraph_re = re.compile('[\n\u2029]')

    def __init__(self, text=''):
        super(AbstractDocument, self).__init__()
        self._text = ''
        self._elements = []
        if text:
            self.insert_text(0, text)

    def _get_text(self):
        return self._text

    def _set_text(self, text):
        if text == self._text:
            return
        self.delete_text(0, len(self._text))
        self.insert_text(0, text)

    text = property(_get_text, _set_text, doc='Document text.\n                   \n        For efficient incremental updates, use the `insert_text` and\n        `delete_text` methods instead of replacing this property.\n        \n        :type: str\n        ')

    def get_paragraph_start(self, pos):
        if self._text[:pos + 1].endswith('\n') or self._text[:pos + 1].endswith('\u2029'):
            return pos
        m = self._previous_paragraph_re.search(self._text, 0, pos + 1)
        if not m:
            return 0
        return m.start() + 1

    def get_paragraph_end(self, pos):
        m = self._next_paragraph_re.search(self._text, pos)
        if not m:
            return len(self._text)
        return m.start() + 1

    def get_style_runs(self, attribute):
        raise NotImplementedError('abstract')

    def get_style(self, attribute, position=0):
        raise NotImplementedError('abstract')

    def get_style_range(self, attribute, start, end):
        iter = self.get_style_runs(attribute)
        _, value_end, value = iter.ranges(start, end).next()
        if value_end < end:
            return STYLE_INDETERMINATE
        else:
            return value

    def get_font_runs(self, dpi=None):
        raise NotImplementedError('abstract')

    def get_font(self, position, dpi=None):
        raise NotImplementedError('abstract')

    def insert_text(self, start, text, attributes=None):
        self._insert_text(start, text, attributes)
        self.dispatch_event('on_insert_text', start, text)

    def _insert_text(self, start, text, attributes):
        self._text = ('').join((self._text[:start], text, self._text[start:]))
        len_text = len(text)
        for element in self._elements:
            if element._position >= start:
                element._position += len_text

    def delete_text(self, start, end):
        self._delete_text(start, end)
        self.dispatch_event('on_delete_text', start, end)

    def _delete_text(self, start, end):
        for element in list(self._elements):
            if start <= element.position < end:
                self._elements.remove(element)

        self._text = self._text[:start] + self._text[end:]

    def insert_element(self, position, element, attributes=None):
        self.insert_text(position, '\x00', attributes)
        element._position = position
        self._elements.append(element)
        self._elements.sort(key=(lambda d: d.position))

    def get_element(self, position):
        for element in self._elements:
            if element._position == position:
                return element

        raise RuntimeError('No element at position %d' % position)

    def set_style(self, start, end, attributes):
        self._set_style(start, end, attributes)
        self.dispatch_event('on_style_text', start, end, attributes)

    def _set_style(self, start, end, attributes):
        raise NotImplementedError('abstract')

    def set_paragraph_style(self, start, end, attributes):
        start = self.get_paragraph_start(start)
        end = self.get_paragraph_end(end)
        self._set_style(start, end, attributes)
        self.dispatch_event('on_style_text', start, end, attributes)

    if _is_epydoc:

        def on_insert_text(self, start, text):
            pass

        def on_delete_text(self, start, end):
            pass

        def on_style_text(self, start, end, attributes):
            pass


AbstractDocument.register_event_type('on_insert_text')
AbstractDocument.register_event_type('on_delete_text')
AbstractDocument.register_event_type('on_style_text')

class UnformattedDocument(AbstractDocument):

    def __init__(self, text=''):
        super(UnformattedDocument, self).__init__(text)
        self.styles = {}

    def get_style_runs(self, attribute):
        value = self.styles.get(attribute)
        return runlist.ConstRunIterator(len(self.text), value)

    def get_style(self, attribute, position=None):
        return self.styles.get(attribute)

    def set_style(self, start, end, attributes):
        return super(UnformattedDocument, self).set_style(0, len(self.text), attributes)

    def _set_style(self, start, end, attributes):
        self.styles.update(attributes)

    def set_paragraph_style(self, start, end, attributes):
        return super(UnformattedDocument, self).set_paragraph_style(0, len(self.text), attributes)

    def get_font_runs(self, dpi=None):
        ft = self.get_font(dpi=dpi)
        return runlist.ConstRunIterator(len(self.text), ft)

    def get_font(self, position=None, dpi=None):
        from pyglet import font
        font_name = self.styles.get('font_name')
        font_size = self.styles.get('font_size')
        bold = self.styles.get('bold', False)
        italic = self.styles.get('italic', False)
        return font.load(font_name, font_size, bold=bool(bold), italic=bool(italic), dpi=dpi)

    def get_element_runs(self):
        return runlist.ConstRunIterator(len(self._text), None)


class FormattedDocument(AbstractDocument):

    def __init__(self, text=''):
        self._style_runs = {}
        super(FormattedDocument, self).__init__(text)

    def get_style_runs(self, attribute):
        try:
            return self._style_runs[attribute].get_run_iterator()
        except KeyError:
            return _no_style_range_iterator

    def get_style(self, attribute, position=0):
        try:
            return self._style_runs[attribute][position]
        except KeyError:
            return

        return

    def _set_style(self, start, end, attributes):
        for attribute, value in attributes.items():
            try:
                runs = self._style_runs[attribute]
            except KeyError:
                runs = self._style_runs[attribute] = runlist.RunList(0, None)
                runs.insert(0, len(self._text))

            runs.set_run(start, end, value)

        return

    def get_font_runs(self, dpi=None):
        return _FontStyleRunsRangeIterator(self.get_style_runs('font_name'), self.get_style_runs('font_size'), self.get_style_runs('bold'), self.get_style_runs('italic'), dpi)

    def get_font(self, position, dpi=None):
        iter = self.get_font_runs(dpi)
        return iter[position]

    def get_element_runs(self):
        return _ElementIterator(self._elements, len(self._text))

    def _insert_text(self, start, text, attributes):
        super(FormattedDocument, self)._insert_text(start, text, attributes)
        len_text = len(text)
        for runs in self._style_runs.values():
            runs.insert(start, len_text)

        if attributes is not None:
            for attribute, value in attributes.items():
                try:
                    runs = self._style_runs[attribute]
                except KeyError:
                    runs = self._style_runs[attribute] = runlist.RunList(0, None)
                    runs.insert(0, len(self.text))

                runs.set_run(start, start + len_text, value)

        return

    def _delete_text(self, start, end):
        super(FormattedDocument, self)._delete_text(start, end)
        for runs in self._style_runs.values():
            runs.delete(start, end)


def _iter_elements(elements, length):
    last = 0
    for element in elements:
        p = element.position
        yield (last, p, None)
        yield (p, p + 1, element)
        last = p + 1

    yield (
     last, length, None)
    return


class _ElementIterator(runlist.RunIterator):

    def __init__(self, elements, length):
        self._run_list_iter = _iter_elements(elements, length)
        self.start, self.end, self.value = self.next()


class _FontStyleRunsRangeIterator(object):

    def __init__(self, font_names, font_sizes, bolds, italics, dpi):
        self.zip_iter = runlist.ZipRunIterator((
         font_names, font_sizes, bolds, italics))
        self.dpi = dpi

    def ranges(self, start, end):
        from pyglet import font
        for start, end, styles in self.zip_iter.ranges(start, end):
            font_name, font_size, bold, italic = styles
            ft = font.load(font_name, font_size, bold=bool(bold), italic=bool(italic), dpi=self.dpi)
            yield (start, end, ft)

    def __getitem__(self, index):
        from pyglet import font
        font_name, font_size, bold, italic = self.zip_iter[index]
        return font.load(font_name, font_size, bold=bool(bold), italic=bool(italic), dpi=self.dpi)


class _NoStyleRangeIterator(object):

    def ranges(self, start, end):
        yield (
         start, end, None)
        return

    def __getitem__(self, index):
        return


_no_style_range_iterator = _NoStyleRangeIterator()
# okay decompiling out\pyglet.text.document.pyc
