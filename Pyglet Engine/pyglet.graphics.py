# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.graphics
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes, pyglet
from ..pyglet.gl import *
from pyglet import gl
from pyglet.graphics import vertexbuffer, vertexattribute, vertexdomain
_debug_graphics_batch = pyglet.options['debug_graphics_batch']

def draw(size, mode, *data):
    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    buffers = []
    for format, array in data:
        attribute = vertexattribute.create_attribute(format)
        buffer = vertexbuffer.create_mappable_buffer(size * attribute.stride, vbo=False)
        attribute.set_region(buffer, 0, size, array)
        attribute.enable()
        attribute.set_pointer(buffer.ptr)
        buffers.append(buffer)

    glDrawArrays(mode, 0, size)
    glFlush()
    glPopClientAttrib()


def draw_indexed(size, mode, indices, *data):
    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    buffers = []
    for format, array in data:
        attribute = vertexattribute.create_attribute(format)
        buffer = vertexbuffer.create_mappable_buffer(size * attribute.stride, vbo=False)
        attribute.set_region(buffer, 0, size, array)
        attribute.enable()
        attribute.set_pointer(buffer.ptr)
        buffers.append(buffer)

    if size <= 255:
        index_type = GL_UNSIGNED_BYTE
        index_c_type = ctypes.c_ubyte
    elif size <= 65535:
        index_type = GL_UNSIGNED_SHORT
        index_c_type = ctypes.c_ushort
    else:
        index_type = GL_UNSIGNED_INT
        index_c_type = ctypes.c_uint
    index_array = (index_c_type * len(indices))(*indices)
    glDrawElements(mode, len(indices), index_type, index_array)
    glFlush()
    glPopClientAttrib()


def _parse_data(data):
    formats = []
    initial_arrays = []
    for i, format in enumerate(data):
        if isinstance(format, tuple):
            format, array = format
            initial_arrays.append((i, array))
        formats.append(format)

    formats = tuple(formats)
    return (formats, initial_arrays)


def _get_default_batch():
    shared_object_space = gl.current_context.object_space
    try:
        return shared_object_space.pyglet_graphics_default_batch
    except AttributeError:
        shared_object_space.pyglet_graphics_default_batch = Batch()
        return shared_object_space.pyglet_graphics_default_batch


def vertex_list(count, *data):
    return _get_default_batch().add(count, 0, None, *data)


def vertex_list_indexed(count, indices, *data):
    return _get_default_batch().add_indexed(count, 0, None, indices, *data)


class Batch(object):

    def __init__(self):
        self.group_map = {}
        self.group_children = {}
        self.top_groups = []
        self._draw_list = []
        self._draw_list_dirty = False

    def add(self, count, mode, group, *data):
        formats, initial_arrays = _parse_data(data)
        domain = self._get_domain(False, mode, group, formats)
        vlist = domain.create(count)
        for i, array in initial_arrays:
            vlist._set_attribute_data(i, array)

        return vlist

    def add_indexed(self, count, mode, group, indices, *data):
        formats, initial_arrays = _parse_data(data)
        domain = self._get_domain(True, mode, group, formats)
        vlist = domain.create(count, len(indices))
        start = vlist.start
        vlist._set_index_data(map((lambda i: i + start), indices))
        for i, array in initial_arrays:
            vlist._set_attribute_data(i, array)

        return vlist

    def migrate(self, vertex_list, mode, group, batch):
        formats = vertex_list.domain.__formats
        domain = batch._get_domain(False, mode, group, formats)
        vertex_list.migrate(domain)

    def _get_domain(self, indexed, mode, group, formats):
        if group is None:
            group = null_group
        if group not in self.group_map:
            self._add_group(group)
        domain_map = self.group_map[group]
        key = (
         formats, mode, indexed)
        try:
            domain = domain_map[key]
        except KeyError:
            if indexed:
                domain = vertexdomain.create_indexed_domain(*formats)
            else:
                domain = vertexdomain.create_domain(*formats)
            domain.__formats = formats
            domain_map[key] = domain
            self._draw_list_dirty = True

        return domain

    def _add_group(self, group):
        self.group_map[group] = {}
        if group.parent is None:
            self.top_groups.append(group)
        else:
            if group.parent not in self.group_map:
                self._add_group(group.parent)
            if group.parent not in self.group_children:
                self.group_children[group.parent] = []
            self.group_children[group.parent].append(group)
        self._draw_list_dirty = True
        return

    def _update_draw_list(self):

        def visit(group):
            draw_list = []
            domain_map = self.group_map[group]
            for (formats, mode, indexed), domain in list(domain_map.items()):
                if domain._is_empty():
                    del domain_map[(formats, mode, indexed)]
                    continue
                draw_list.append((lambda d, m: (lambda : d.draw(m)))(domain, mode))

            children = self.group_children.get(group)
            if children:
                children.sort()
                for child in list(children):
                    draw_list.extend(visit(child))

            if children or domain_map:
                return [group.set_state] + draw_list + [group.unset_state]
            else:
                del self.group_map[group]
                if group.parent:
                    self.group_children[group.parent].remove(group)
                try:
                    del self.group_children[group]
                except KeyError:
                    pass

                try:
                    self.top_groups.remove(group)
                except ValueError:
                    pass

                return []

        self._draw_list = []
        self.top_groups.sort()
        for group in list(self.top_groups):
            self._draw_list.extend(visit(group))

        self._draw_list_dirty = False
        if _debug_graphics_batch:
            self._dump_draw_list()

    def _dump_draw_list(self):

        def dump(group, indent=''):
            print indent, 'Begin group', group
            domain_map = self.group_map[group]
            for _, domain in domain_map.items():
                print indent, '  ', domain
                for start, size in zip(*domain.allocator.get_allocated_regions()):
                    print indent, '    ', 'Region %d size %d:' % (start, size)
                    for key, attribute in domain.attribute_names.items():
                        print indent, '      ',
                        try:
                            region = attribute.get_region(attribute.buffer, start, size)
                            print key, region.array[:]
                        except:
                            print key, '(unmappable)'

            for child in self.group_children.get(group, ()):
                dump(child, indent + '  ')

            print indent, 'End group', group

        print 'Draw list for %r:' % self
        for group in self.top_groups:
            dump(group)

    def draw(self):
        if self._draw_list_dirty:
            self._update_draw_list()
        for func in self._draw_list:
            func()

    def draw_subset(self, vertex_lists):

        def visit(group):
            group.set_state()
            domain_map = self.group_map[group]
            for (_, mode, _), domain in domain_map.items():
                for list in vertex_lists:
                    if list.domain is domain:
                        list.draw(mode)

            children = self.group_children.get(group)
            if children:
                children.sort()
                for child in children:
                    visit(child)

            group.unset_state()

        self.top_groups.sort()
        for group in self.top_groups:
            visit(group)


class Group(object):

    def __init__(self, parent=None):
        self.parent = parent

    def __lt__(self, other):
        return hash(self) < hash(other)

    def set_state(self):
        pass

    def unset_state(self):
        pass

    def set_state_recursive(self):
        if self.parent:
            self.parent.set_state_recursive()
        self.set_state()

    def unset_state_recursive(self):
        self.unset_state()
        if self.parent:
            self.parent.unset_state_recursive()


class NullGroup(Group):
    pass


null_group = NullGroup()

class TextureGroup(Group):

    def __init__(self, texture, parent=None):
        super(TextureGroup, self).__init__(parent)
        self.texture = texture

    def set_state(self):
        glEnable(self.texture.target)
        glBindTexture(self.texture.target, self.texture.id)

    def unset_state(self):
        glDisable(self.texture.target)

    def __hash__(self):
        return hash((self.texture.target, self.texture.id, self.parent))

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.texture.target == other.texture.target and self.texture.id == other.texture.id and self.parent == other.parent

    def __repr__(self):
        return '%s(id=%d)' % (self.__class__.__name__, self.texture.id)


class OrderedGroup(Group):

    def __init__(self, order, parent=None):
        super(OrderedGroup, self).__init__(parent)
        self.order = order

    def __lt__(self, other):
        if isinstance(other, OrderedGroup):
            return self.order < other.order
        return super(OrderedGroup, self).__lt__(other)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.order == other.order and self.parent == other.parent

    def __hash__(self):
        return hash((self.order, self.parent))

    def __repr__(self):
        return '%s(%d)' % (self.__class__.__name__, self.order)
# okay decompiling out\pyglet.graphics.pyc
