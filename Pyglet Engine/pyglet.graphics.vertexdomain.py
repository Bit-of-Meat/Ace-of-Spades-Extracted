# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.graphics.vertexdomain
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes, re
from ..pyglet.gl import *
from pyglet.graphics import allocation, vertexattribute, vertexbuffer
_usage_format_re = re.compile('\n    (?P<attribute>[^/]*)\n    (/ (?P<usage> static|dynamic|stream|none))?\n', re.VERBOSE)
_gl_usages = {'static': GL_STATIC_DRAW, 
   'dynamic': GL_DYNAMIC_DRAW, 
   'stream': GL_STREAM_DRAW, 
   'none': GL_STREAM_DRAW_ARB}

def _nearest_pow2(v):
    v -= 1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    return v + 1


def create_attribute_usage(format):
    match = _usage_format_re.match(format)
    attribute_format = match.group('attribute')
    attribute = vertexattribute.create_attribute(attribute_format)
    usage = match.group('usage')
    if usage:
        vbo = not usage == 'none'
        usage = _gl_usages[usage]
    else:
        usage = GL_DYNAMIC_DRAW
        vbo = True
    return (attribute, usage, vbo)


def create_domain(*attribute_usage_formats):
    attribute_usages = [ create_attribute_usage(f) for f in attribute_usage_formats
                       ]
    return VertexDomain(attribute_usages)


def create_indexed_domain(*attribute_usage_formats):
    attribute_usages = [ create_attribute_usage(f) for f in attribute_usage_formats
                       ]
    return IndexedVertexDomain(attribute_usages)


class VertexDomain(object):
    _version = 0
    _initial_count = 16

    def __init__(self, attribute_usages):
        self.allocator = allocation.Allocator(self._initial_count)
        have_multi_texcoord = False
        for attribute, _, _ in attribute_usages:
            if isinstance(attribute, vertexattribute.MultiTexCoordAttribute):
                have_multi_texcoord = True
                break

        static_attributes = []
        attributes = []
        self.buffer_attributes = []
        for attribute, usage, vbo in attribute_usages:
            if have_multi_texcoord and isinstance(attribute, vertexattribute.TexCoordAttribute):
                attribute.convert_to_multi_tex_coord_attribute()
            if usage == GL_STATIC_DRAW:
                static_attributes.append(attribute)
                attributes.append(attribute)
            else:
                attributes.append(attribute)
                attribute.buffer = vertexbuffer.create_mappable_buffer(attribute.stride * self.allocator.capacity, usage=usage, vbo=vbo)
                attribute.buffer.element_size = attribute.stride
                attribute.buffer.attributes = (attribute,)
                self.buffer_attributes.append((
                 attribute.buffer, (attribute,)))

        if static_attributes:
            vertexattribute.interleave_attributes(static_attributes)
            stride = static_attributes[0].stride
            buffer = vertexbuffer.create_mappable_buffer(stride * self.allocator.capacity, usage=GL_STATIC_DRAW)
            buffer.element_size = stride
            self.buffer_attributes.append((
             buffer, static_attributes))
            attributes.extend(static_attributes)
            for attribute in static_attributes:
                attribute.buffer = buffer

        self.attributes = attributes
        self.attribute_names = {}
        for attribute in attributes:
            if isinstance(attribute, vertexattribute.GenericAttribute):
                index = attribute.index
                if 'generic' not in self.attribute_names:
                    self.attribute_names['generic'] = {}
                self.attribute_names['generic'][index] = attribute
            elif isinstance(attribute, vertexattribute.MultiTexCoordAttribute):
                texture = attribute.texture
                if 'multi_tex_coords' not in self.attribute_names:
                    self.attribute_names['multi_tex_coords'] = {}
                self.attribute_names['multi_tex_coords'][texture] = attribute
            else:
                name = attribute.plural
                self.attribute_names[name] = attribute

    def __del__(self):
        for attribute in self.attributes:
            try:
                del attribute.buffer
            except AttributeError:
                pass

    def _safe_alloc(self, count):
        try:
            return self.allocator.alloc(count)
        except allocation.AllocatorMemoryException as e:
            capacity = _nearest_pow2(e.requested_capacity)
            self._version += 1
            for buffer, _ in self.buffer_attributes:
                buffer.resize(capacity * buffer.element_size)

            self.allocator.set_capacity(capacity)
            return self.allocator.alloc(count)

    def _safe_realloc(self, start, count, new_count):
        try:
            return self.allocator.realloc(start, count, new_count)
        except allocation.AllocatorMemoryException as e:
            capacity = _nearest_pow2(e.requested_capacity)
            self._version += 1
            for buffer, _ in self.buffer_attributes:
                buffer.resize(capacity * buffer.element_size)

            self.allocator.set_capacity(capacity)
            return self.allocator.realloc(start, count, new_count)

    def create(self, count):
        start = self._safe_alloc(count)
        return VertexList(self, start, count)

    def draw(self, mode, vertex_list=None):
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        for buffer, attributes in self.buffer_attributes:
            buffer.bind()
            for attribute in attributes:
                attribute.enable()
                attribute.set_pointer(attribute.buffer.ptr)

        if vertexbuffer._workaround_vbo_finish:
            glFinish()
        if vertex_list is not None:
            glDrawArrays(mode, vertex_list.start, vertex_list.count)
        else:
            starts, sizes = self.allocator.get_allocated_regions()
            primcount = len(starts)
            if primcount == 0:
                pass
            else:
                if primcount == 1:
                    glDrawArrays(mode, starts[0], sizes[0])
                else:
                    if gl_info.have_version(1, 4):
                        starts = (GLint * primcount)(*starts)
                        sizes = (GLsizei * primcount)(*sizes)
                        glMultiDrawArrays(mode, starts, sizes, primcount)
                    else:
                        for start, size in zip(starts, sizes):
                            glDrawArrays(mode, start, size)

            for buffer, _ in self.buffer_attributes:
                buffer.unbind()

        glPopClientAttrib()
        return

    def _is_empty(self):
        return not self.allocator.starts

    def __repr__(self):
        return '<%s@%x %s>' % (self.__class__.__name__, id(self),
         self.allocator)


class VertexList(object):

    def __init__(self, domain, start, count):
        self.domain = domain
        self.start = start
        self.count = count

    def get_size(self):
        return self.count

    def get_domain(self):
        return self.domain

    def draw(self, mode):
        self.domain.draw(mode, self)

    def resize(self, count):
        new_start = self.domain._safe_realloc(self.start, self.count, count)
        if new_start != self.start:
            for attribute in self.domain.attributes:
                old = attribute.get_region(attribute.buffer, self.start, self.count)
                new = attribute.get_region(attribute.buffer, new_start, self.count)
                new.array[:] = old.array[:]
                new.invalidate()

        self.start = new_start
        self.count = count
        self._colors_cache_version = None
        self._fog_coords_cache_version = None
        self._edge_flags_cache_version = None
        self._normals_cache_version = None
        self._secondary_colors_cache_version = None
        self._tex_coords_cache_version = None
        self._vertices_cache_version = None
        return

    def delete(self):
        self.domain.allocator.dealloc(self.start, self.count)

    def migrate(self, domain):
        new_start = domain._safe_alloc(self.count)
        for key, old_attribute in self.domain.attribute_names.items():
            old = old_attribute.get_region(old_attribute.buffer, self.start, self.count)
            new_attribute = domain.attribute_names[key]
            new = new_attribute.get_region(new_attribute.buffer, new_start, self.count)
            new.array[:] = old.array[:]
            new.invalidate()

        self.domain.allocator.dealloc(self.start, self.count)
        self.domain = domain
        self.start = new_start
        self._colors_cache_version = None
        self._fog_coords_cache_version = None
        self._edge_flags_cache_version = None
        self._normals_cache_version = None
        self._secondary_colors_cache_version = None
        self._tex_coords_cache_version = None
        self._vertices_cache_version = None
        return

    def _set_attribute_data(self, i, data):
        attribute = self.domain.attributes[i]
        region = attribute.get_region(attribute.buffer, self.start, self.count)
        region.array[:] = data
        region.invalidate()

    def _get_colors(self):
        if self._colors_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['colors']
            self._colors_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._colors_cache_version = domain._version
        region = self._colors_cache
        region.invalidate()
        return region.array

    def _set_colors(self, data):
        self._get_colors()[:] = data

    _colors_cache = None
    _colors_cache_version = None
    colors = property(_get_colors, _set_colors, doc='Array of color data.')

    def _get_fog_coords(self):
        if self._fog_coords_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['fog_coords']
            self._fog_coords_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._fog_coords_cache_version = domain._version
        region = self._fog_coords_cache
        region.invalidate()
        return region.array

    def _set_fog_coords(self, data):
        self._get_fog_coords()[:] = data

    _fog_coords_cache = None
    _fog_coords_cache_version = None
    fog_coords = property(_get_fog_coords, _set_fog_coords, doc='Array of fog coordinate data.')

    def _get_edge_flags(self):
        if self._edge_flags_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['edge_flags']
            self._edge_flags_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._edge_flags_cache_version = domain._version
        region = self._edge_flags_cache
        region.invalidate()
        return region.array

    def _set_edge_flags(self, data):
        self._get_edge_flags()[:] = data

    _edge_flags_cache = None
    _edge_flags_cache_version = None
    edge_flags = property(_get_edge_flags, _set_edge_flags, doc='Array of edge flag data.')

    def _get_normals(self):
        if self._normals_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['normals']
            self._normals_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._normals_cache_version = domain._version
        region = self._normals_cache
        region.invalidate()
        return region.array

    def _set_normals(self, data):
        self._get_normals()[:] = data

    _normals_cache = None
    _normals_cache_version = None
    normals = property(_get_normals, _set_normals, doc='Array of normal vector data.')

    def _get_secondary_colors(self):
        if self._secondary_colors_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['secondary_colors']
            self._secondary_colors_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._secondary_colors_cache_version = domain._version
        region = self._secondary_colors_cache
        region.invalidate()
        return region.array

    def _set_secondary_colors(self, data):
        self._get_secondary_colors()[:] = data

    _secondary_colors_cache = None
    _secondary_colors_cache_version = None
    secondary_colors = property(_get_secondary_colors, _set_secondary_colors, doc='Array of secondary color data.')
    _tex_coords_cache = None
    _tex_coords_cache_version = None

    def _get_tex_coords(self):
        if self._tex_coords_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['tex_coords']
            self._tex_coords_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._tex_coords_cache_version = domain._version
        region = self._tex_coords_cache
        region.invalidate()
        return region.array

    def _set_tex_coords(self, data):
        self._get_tex_coords()[:] = data

    tex_coords = property(_get_tex_coords, _set_tex_coords, doc='Array of texture coordinate data.')
    _vertices_cache = None
    _vertices_cache_version = None

    def _get_vertices(self):
        if self._vertices_cache_version != self.domain._version:
            domain = self.domain
            attribute = domain.attribute_names['vertices']
            self._vertices_cache = attribute.get_region(attribute.buffer, self.start, self.count)
            self._vertices_cache_version = domain._version
        region = self._vertices_cache
        region.invalidate()
        return region.array

    def _set_vertices(self, data):
        self._get_vertices()[:] = data

    vertices = property(_get_vertices, _set_vertices, doc='Array of vertex coordinate data.')


class IndexedVertexDomain(VertexDomain):
    _initial_index_count = 16

    def __init__(self, attribute_usages, index_gl_type=GL_UNSIGNED_INT):
        super(IndexedVertexDomain, self).__init__(attribute_usages)
        self.index_allocator = allocation.Allocator(self._initial_index_count)
        self.index_gl_type = index_gl_type
        self.index_c_type = vertexattribute._c_types[index_gl_type]
        self.index_element_size = ctypes.sizeof(self.index_c_type)
        self.index_buffer = vertexbuffer.create_mappable_buffer(self.index_allocator.capacity * self.index_element_size, target=GL_ELEMENT_ARRAY_BUFFER)

    def _safe_index_alloc(self, count):
        try:
            return self.index_allocator.alloc(count)
        except allocation.AllocatorMemoryException as e:
            capacity = _nearest_pow2(e.requested_capacity)
            self._version += 1
            self.index_buffer.resize(capacity * self.index_element_size)
            self.index_allocator.set_capacity(capacity)
            return self.index_allocator.alloc(count)

    def _safe_index_realloc(self, start, count, new_count):
        try:
            return self.index_allocator.realloc(start, count, new_count)
        except allocation.AllocatorMemoryException as e:
            capacity = _nearest_pow2(e.requested_capacity)
            self._version += 1
            self.index_buffer.resize(capacity * self.index_element_size)
            self.index_allocator.set_capacity(capacity)
            return self.index_allocator.realloc(start, count, new_count)

    def create(self, count, index_count):
        start = self._safe_alloc(count)
        index_start = self._safe_index_alloc(index_count)
        return IndexedVertexList(self, start, count, index_start, index_count)

    def get_index_region(self, start, count):
        byte_start = self.index_element_size * start
        byte_count = self.index_element_size * count
        ptr_type = ctypes.POINTER(self.index_c_type * count)
        return self.index_buffer.get_region(byte_start, byte_count, ptr_type)

    def draw(self, mode, vertex_list=None):
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        for buffer, attributes in self.buffer_attributes:
            buffer.bind()
            for attribute in attributes:
                attribute.enable()
                attribute.set_pointer(attribute.buffer.ptr)

        self.index_buffer.bind()
        if vertexbuffer._workaround_vbo_finish:
            glFinish()
        if vertex_list is not None:
            glDrawElements(mode, vertex_list.index_count, self.index_gl_type, self.index_buffer.ptr + vertex_list.index_start * self.index_element_size)
        else:
            starts, sizes = self.index_allocator.get_allocated_regions()
            primcount = len(starts)
            if primcount == 0:
                pass
            else:
                if primcount == 1:
                    glDrawElements(mode, sizes[0], self.index_gl_type, self.index_buffer.ptr + starts[0])
                else:
                    if gl_info.have_version(1, 4):
                        starts = [ s * self.index_element_size + self.index_buffer.ptr for s in starts ]
                        starts = ctypes.cast((GLuint * primcount)(*starts), ctypes.POINTER(ctypes.c_void_p))
                        sizes = (GLsizei * primcount)(*sizes)
                        glMultiDrawElements(mode, sizes, GL_UNSIGNED_INT, starts, primcount)
                    else:
                        for start, size in zip(starts, sizes):
                            glDrawElements(mode, size, self.index_gl_type, self.index_buffer.ptr + start * self.index_element_size)

            self.index_buffer.unbind()
            for buffer, _ in self.buffer_attributes:
                buffer.unbind()

        glPopClientAttrib()
        return


class IndexedVertexList(VertexList):

    def __init__(self, domain, start, count, index_start, index_count):
        super(IndexedVertexList, self).__init__(domain, start, count)
        self.index_start = index_start
        self.index_count = index_count

    def draw(self, mode):
        self.domain.draw(mode, self)

    def resize(self, count, index_count):
        old_start = self.start
        super(IndexedVertexList, self).resize(count)
        if old_start != self.start:
            diff = self.start - old_start
            self.indices[:] = map((lambda i: i + diff), self.indices)
        new_start = self.domain._safe_index_realloc(self.index_start, self.index_count, index_count)
        if new_start != self.index_start:
            old = self.domain.get_index_region(self.index_start, self.index_count)
            new = self.domain.get_index_region(self.index_start, self.index_count)
            new.array[:] = old.array[:]
            new.invalidate()
        self.index_start = new_start
        self.index_count = index_count
        self._indices_cache_version = None
        return

    def delete(self):
        super(IndexedVertexList, self).delete()
        self.domain.index_allocator.dealloc(self.index_start, self.index_count)

    def _set_index_data(self, data):
        region = self.domain.get_index_region(self.index_start, self.index_count)
        region.array[:] = data
        region.invalidate()

    def _get_indices(self):
        if self._indices_cache_version != self.domain._version:
            domain = self.domain
            self._indices_cache = domain.get_index_region(self.index_start, self.index_count)
            self._indices_cache_version = domain._version
        region = self._indices_cache
        region.invalidate()
        return region.array

    def _set_indices(self, data):
        self._get_indices()[:] = data

    _indices_cache = None
    _indices_cache_version = None
    indices = property(_get_indices, _set_indices, doc='Array of index data.')
# okay decompiling out\pyglet.graphics.vertexdomain.pyc
