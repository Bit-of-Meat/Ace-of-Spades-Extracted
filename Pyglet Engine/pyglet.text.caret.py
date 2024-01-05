# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.caret
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import re, time
from pyglet import clock
from pyglet import event
from pyglet.window import key

class Caret(object):
    _next_word_re = re.compile('(?<=\\W)\\w')
    _previous_word_re = re.compile('(?<=\\W)\\w+\\W*$')
    _next_para_re = re.compile('\\n', flags=re.DOTALL)
    _previous_para_re = re.compile('\\n', flags=re.DOTALL)
    _position = 0
    _active = True
    _visible = True
    _blink_visible = True
    _click_count = 0
    _click_time = 0
    PERIOD = 0.5
    SCROLL_INCREMENT = 16

    def __init__(self, layout, batch=None, color=(0, 0, 0)):
        from pyglet import gl
        self._layout = layout
        if batch is None:
            batch = layout.batch
        r, g, b = color
        colors = (r, g, b, 255, r, g, b, 255)
        self._list = batch.add(2, gl.GL_LINES, layout.background_group, 'v2f', ('c4B', colors))
        self._ideal_x = None
        self._ideal_line = None
        self._next_attributes = {}
        self.visible = True
        layout.push_handlers(self)
        return

    def delete(self):
        self._list.delete()
        self._layout.remove_handlers(self)

    def _blink(self, dt):
        if self.PERIOD:
            self._blink_visible = not self._blink_visible
        if self._visible and self._active and self._blink_visible:
            alpha = 255
        else:
            alpha = 0
        self._list.colors[3] = alpha
        self._list.colors[7] = alpha

    def _nudge(self):
        self.visible = True

    def _set_visible(self, visible):
        self._visible = visible
        clock.unschedule(self._blink)
        if visible and self._active and self.PERIOD:
            clock.schedule_interval(self._blink, self.PERIOD)
            self._blink_visible = False
        self._blink(0)

    def _get_visible(self):
        return self._visible

    visible = property(_get_visible, _set_visible, doc='Caret visibility.\n    \n    The caret may be hidden despite this property due to the periodic blinking\n    or by `on_deactivate` if the event handler is attached to a window.\n\n    :type: bool\n    ')

    def _set_color(self, color):
        self._list.colors[:3] = color
        self._list.colors[4:7] = color

    def _get_color(self):
        return self._list.colors[:3]

    color = property(_get_color, _set_color, doc='Caret color.\n\n    The default caret color is ``[0, 0, 0]`` (black).  Each RGB color\n    component is in the range 0 to 255.\n\n    :type: (int, int, int)\n    ')

    def _set_position(self, index):
        self._position = index
        self._next_attributes.clear()
        self._update()

    def _get_position(self):
        return self._position

    position = property(_get_position, _set_position, doc='Position of caret within document.\n\n    :type: int\n    ')
    _mark = None

    def _set_mark(self, mark):
        self._mark = mark
        self._update(line=self._ideal_line)
        if mark is None:
            self._layout.set_selection(0, 0)
        return

    def _get_mark(self):
        return self._mark

    mark = property(_get_mark, _set_mark, doc="Position of immovable end of text selection within\n    document.\n\n    An interactive text selection is determined by its immovable end (the\n    caret's position when a mouse drag begins) and the caret's position, which\n    moves interactively by mouse and keyboard input.\n\n    This property is ``None`` when there is no selection.\n\n    :type: int\n    ")

    def _set_line(self, line):
        if self._ideal_x is None:
            self._ideal_x, _ = self._layout.get_point_from_position(self._position)
        self._position = self._layout.get_position_on_line(line, self._ideal_x)
        self._update(line=line, update_ideal_x=False)
        return

    def _get_line(self):
        if self._ideal_line is not None:
            return self._ideal_line
        else:
            return self._layout.get_line_from_position(self._position)
            return

    line = property(_get_line, _set_line, doc="Index of line containing the caret's position.\n\n    When set, `position` is modified to place the caret on requested line\n    while maintaining the closest possible X offset.\n                    \n    :type: int\n    ")

    def get_style(self, attribute):
        if self._mark is None or self._mark == self._position:
            try:
                return self._next_attributes[attribute]
            except KeyError:
                return self._layout.document.get_style(attribute, self._position)

        start = min(self._position, self._mark)
        end = max(self._position, self._mark)
        return self._layout.document.get_style_range(attribute, start, end)

    def set_style(self, attributes):
        if self._mark is None or self._mark == self._position:
            self._next_attributes.update(attributes)
            return
        else:
            start = min(self._position, self._mark)
            end = max(self._position, self._mark)
            self._layout.document.set_style(start, end, attributes)
            return

    def _delete_selection(self):
        start = min(self._mark, self._position)
        end = max(self._mark, self._position)
        self._position = start
        self._mark = None
        self._layout.document.delete_text(start, end)
        self._layout.set_selection(0, 0)
        return

    def move_to_point(self, x, y):
        line = self._layout.get_line_from_point(x, y)
        self._mark = None
        self._layout.set_selection(0, 0)
        self._position = self._layout.get_position_on_line(line, x)
        self._update(line=line)
        self._next_attributes.clear()
        return

    def select_to_point(self, x, y):
        line = self._layout.get_line_from_point(x, y)
        self._position = self._layout.get_position_on_line(line, x)
        self._update(line=line)
        self._next_attributes.clear()

    def select_word(self, x, y):
        line = self._layout.get_line_from_point(x, y)
        p = self._layout.get_position_on_line(line, x)
        m1 = self._previous_word_re.search(self._layout.document.text, 0, p + 1)
        if not m1:
            m1 = 0
        else:
            m1 = m1.start()
        self.mark = m1
        m2 = self._next_word_re.search(self._layout.document.text, p)
        if not m2:
            m2 = len(self._layout.document.text)
        else:
            m2 = m2.start()
        self._position = m2
        self._update(line=line)
        self._next_attributes.clear()

    def select_paragraph(self, x, y):
        line = self._layout.get_line_from_point(x, y)
        p = self._layout.get_position_on_line(line, x)
        self.mark = self._layout.document.get_paragraph_start(p)
        self._position = self._layout.document.get_paragraph_end(p)
        self._update(line=line)
        self._next_attributes.clear()

    def _update(self, line=None, update_ideal_x=True):
        if line is None:
            line = self._layout.get_line_from_position(self._position)
            self._ideal_line = None
        else:
            self._ideal_line = line
        x, y = self._layout.get_point_from_position(self._position, line)
        if update_ideal_x:
            self._ideal_x = x
        x -= self._layout.top_group.translate_x
        y -= self._layout.top_group.translate_y
        font = self._layout.document.get_font(max(0, self._position - 1))
        self._list.vertices[:] = [x, y + font.descent, x, y + font.ascent]
        if self._mark is not None:
            self._layout.set_selection(min(self._position, self._mark), max(self._position, self._mark))
        self._layout.ensure_line_visible(line)
        self._layout.ensure_x_visible(x)
        return

    def on_layout_update(self):
        if self.position > len(self._layout.document.text):
            self.position = len(self._layout.document.text)
        self._update()

    def on_text(self, text):
        if self._mark is not None:
            self._delete_selection()
        text = text.replace('\r', '\n')
        pos = self._position
        self._position += len(text)
        self._layout.document.insert_text(pos, text, self._next_attributes)
        self._nudge()
        return event.EVENT_HANDLED

    def on_text_motion(self, motion, select=False):
        if motion == key.MOTION_BACKSPACE:
            if self.mark is not None:
                self._delete_selection()
            elif self._position > 0:
                self._position -= 1
                self._layout.document.delete_text(self._position, self._position + 1)
        elif motion == key.MOTION_DELETE:
            if self.mark is not None:
                self._delete_selection()
            elif self._position < len(self._layout.document.text):
                self._layout.document.delete_text(self._position, self._position + 1)
        elif self._mark is not None and not select:
            self._mark = None
            self._layout.set_selection(0, 0)
        if motion == key.MOTION_LEFT:
            self.position = max(0, self.position - 1)
        elif motion == key.MOTION_RIGHT:
            self.position = min(len(self._layout.document.text), self.position + 1)
        elif motion == key.MOTION_UP:
            self.line = max(0, self.line - 1)
        elif motion == key.MOTION_DOWN:
            line = self.line
            if line < self._layout.get_line_count() - 1:
                self.line = line + 1
        elif motion == key.MOTION_BEGINNING_OF_LINE:
            self.position = self._layout.get_position_from_line(self.line)
        elif motion == key.MOTION_END_OF_LINE:
            line = self.line
            if line < self._layout.get_line_count() - 1:
                self._position = self._layout.get_position_from_line(line + 1) - 1
                self._update(line)
            else:
                self.position = len(self._layout.document.text)
        elif motion == key.MOTION_BEGINNING_OF_FILE:
            self.position = 0
        elif motion == key.MOTION_END_OF_FILE:
            self.position = len(self._layout.document.text)
        elif motion == key.MOTION_NEXT_WORD:
            pos = self._position + 1
            m = self._next_word_re.search(self._layout.document.text, pos)
            if not m:
                self.position = len(self._layout.document.text)
            else:
                self.position = m.start()
        elif motion == key.MOTION_PREVIOUS_WORD:
            pos = self._position
            m = self._previous_word_re.search(self._layout.document.text, 0, pos)
            if not m:
                self.position = 0
            else:
                self.position = m.start()
        self._next_attributes.clear()
        self._nudge()
        return event.EVENT_HANDLED

    def on_text_motion_select(self, motion):
        if self.mark is None:
            self.mark = self.position
        self.on_text_motion(motion, True)
        return event.EVENT_HANDLED

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self._layout.view_x -= scroll_x * self.SCROLL_INCREMENT
        self._layout.view_y += scroll_y * self.SCROLL_INCREMENT
        return event.EVENT_HANDLED

    def on_mouse_press(self, x, y, button, modifiers):
        t = time.time()
        if t - self._click_time < 0.25:
            self._click_count += 1
        else:
            self._click_count = 1
        self._click_time = time.time()
        if self._click_count == 1:
            self.move_to_point(x, y)
        elif self._click_count == 2:
            self.select_word(x, y)
        elif self._click_count == 3:
            self.select_paragraph(x, y)
            self._click_count = 0
        self._nudge()
        return event.EVENT_HANDLED

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.mark is None:
            self.mark = self.position
        self.select_to_point(x, y)
        self._nudge()
        return event.EVENT_HANDLED

    def on_activate(self):
        self._active = True
        self.visible = self._active
        return event.EVENT_HANDLED

    def on_deactivate(self):
        self._active = False
        self.visible = self._active
        return event.EVENT_HANDLED
# okay decompiling out\pyglet.text.caret.pyc
