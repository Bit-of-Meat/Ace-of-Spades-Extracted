# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.graphics.vertexattribute
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes, re
from ..pyglet.gl import *
from pyglet.graphics import vertexbuffer
_c_types = {GL_BYTE: ctypes.c_byte, 
   GL_UNSIGNED_BYTE: ctypes.c_ubyte, 
   GL_SHORT: ctypes.c_short, 
   GL_UNSIGNED_SHORT: ctypes.c_ushort, 
   GL_INT: ctypes.c_int, 
   GL_UNSIGNED_INT: ctypes.c_uint, 
   GL_FLOAT: ctypes.c_float, 
   GL_DOUBLE: ctypes.c_double}
_gl_types = {'b': GL_BYTE, 
   'B': GL_UNSIGNED_BYTE, 
   's': GL_SHORT, 
   'S': GL_UNSIGNED_SHORT, 
   'i': GL_INT, 
   'I': GL_UNSIGNED_INT, 
   'f': GL_FLOAT, 
   'd': GL_DOUBLE}
_attribute_format_re = re.compile('\n    (?P<name>\n       [cefnstv] | \n       (?P<generic_index>[0-9]+) g (?P<generic_normalized>n?) |\n       (?P<texcoord_texture>[0-9]+) t)\n    (?P<count>[1234])\n    (?P<type>[bBsSiIfd])\n', re.VERBOSE)
_attribute_cache = {}

def _align(v, align):
    return (v - 1 & ~(align - 1)) + align


def interleave_attributes(attributes):
    stride = 0
    max_size = 0
    for attribute in attributes:
        stride = _align(stride, attribute.align)
        attribute.offset = stride
        stride += attribute.size
        max_size = max(max_size, attribute.size)

    stride = _align(stride, max_size)
    for attribute in attributes:
        attribute.stride = stride


def serialize_attributes(count, attributes):
    offset = 0
    for attribute in attributes:
        offset = _align(offset, attribute.align)
        attribute.offset = offset
        offset += count * attribute.stride


def create_attribute(format):
    try:
        cls, args = _attribute_cache[format]
        return cls(*args)
    except KeyError:
        pass

    match = _attribute_format_re.match(format)
    count = int(match.group('count'))
    gl_type = _gl_types[match.group('type')]
    generic_index = match.group('generic_index')
    texcoord_texture = match.group('texcoord_texture')
    if generic_index:
        normalized = match.group('generic_normalized')
        attr_class = GenericAttribute
        args = (int(generic_index), normalized, count, gl_type)
    elif texcoord_texture:
        attr_class = MultiTexCoordAttribute
        args = (int(texcoord_texture), count, gl_type)
    else:
        name = match.group('name')
        attr_class = _attribute_classes[name]
        if attr_class._fixed_count:
            args = (
             gl_type,)
        else:
            args = (
             count, gl_type)
    _attribute_cache[format] = (
     attr_class, args)
    return attr_class(*args)


class AbstractAttribute(object):
    _fixed_count = None

    def __init__(self, count, gl_type):
        self.gl_type = gl_type
        self.c_type = _c_types[gl_type]
        self.count = count
        self.align = ctypes.sizeof(self.c_type)
        self.size = count * self.align
        self.stride = self.size
        self.offset = 0

    def enable(self):
        raise NotImplementedError('abstract')

    def set_pointer(self, offset):
        raise NotImplementedError('abstract')

    def get_region(self, buffer, start, count):
        byte_start = self.stride * start
        byte_size = self.stride * count
        array_count = self.count * count
        if self.stride == self.size or not array_count:
            ptr_type = ctypes.POINTER(self.c_type * array_count)
            return buffer.get_region(byte_start, byte_size, ptr_type)
        else:
            byte_start += self.offset
            byte_size -= self.offset
            elem_stride = self.stride // ctypes.sizeof(self.c_type)
            elem_offset = self.offset // ctypes.sizeof(self.c_type)
            ptr_type = ctypes.POINTER(self.c_type * (count * elem_stride - elem_offset))
            region = buffer.get_region(byte_start, byte_size, ptr_type)
            return vertexbuffer.IndirectArrayRegion(region, array_count, self.count, elem_stride)

    def set_region(self, buffer, start, count, data):
        if self.stride == self.size:
            byte_start = self.stride * start
            byte_size = self.stride * count
            array_count = self.count * count
            data = (self.c_type * array_count)(*data)
            buffer.set_data_region(data, byte_start, byte_size)
        else:
            region = self.get_region(buffer, start, count)
            region[:] = data


class ColorAttribute(AbstractAttribute):
    plural = 'colors'

    def __init__(self, count, gl_type):
        super(ColorAttribute, self).__init__(count, gl_type)

    def enable(self):
        glEnableClientState(GL_COLOR_ARRAY)

    def set_pointer(self, pointer):
        glColorPointer(self.count, self.gl_type, self.stride, self.offset + pointer)


class EdgeFlagAttribute(AbstractAttribute):
    plural = 'edge_flags'
    _fixed_count = 1

    def __init__(self, gl_type):
        super(EdgeFlagAttribute, self).__init__(1, gl_type)

    def enable(self):
        glEnableClientState(GL_EDGE_FLAG_ARRAY)

    def set_pointer(self, pointer):
        glEdgeFlagPointer(self.stride, self.offset + pointer)


class FogCoordAttribute(AbstractAttribute):
    plural = 'fog_coords'

    def __init__(self, count, gl_type):
        super(FogCoordAttribute, self).__init__(count, gl_type)

    def enable(self):
        glEnableClientState(GL_FOG_COORD_ARRAY)

    def set_pointer(self, pointer):
        glFogCoordPointer(self.count, self.gl_type, self.stride, self.offset + pointer)


class NormalAttribute(AbstractAttribute):
    plural = 'normals'
    _fixed_count = 3

    def __init__(self, gl_type):
        super(NormalAttribute, self).__init__(3, gl_type)

    def enable(self):
        glEnableClientState(GL_NORMAL_ARRAY)

    def set_pointer(self, pointer):
        glNormalPointer(self.gl_type, self.stride, self.offset + pointer)


class SecondaryColorAttribute(AbstractAttribute):
    plural = 'secondary_colors'
    _fixed_count = 3

    def __init__(self, gl_type):
        super(SecondaryColorAttribute, self).__init__(3, gl_type)

    def enable(self):
        glEnableClientState(GL_SECONDARY_COLOR_ARRAY)

    def set_pointer(self, pointer):
        glSecondaryColorPointer(3, self.gl_type, self.stride, self.offset + pointer)


class TexCoordAttribute(AbstractAttribute):
    plural = 'tex_coords'

    def __init__(self, count, gl_type):
        super(TexCoordAttribute, self).__init__(count, gl_type)

    def enable(self):
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)

    def set_pointer(self, pointer):
        glTexCoordPointer(self.count, self.gl_type, self.stride, self.offset + pointer)

    def convert_to_multi_tex_coord_attribute(self):
        self.__class__ = MultiTexCoordAttribute
        self.texture = 0


class MultiTexCoordAttribute(AbstractAttribute):

    def __init__(self, texture, count, gl_type):
        self.texture = texture
        super(MultiTexCoordAttribute, self).__init__(count, gl_type)

    def enable(self):
        glClientActiveTexture(GL_TEXTURE0 + self.texture)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)

    def set_pointer(self, pointer):
        glTexCoordPointer(self.count, self.gl_type, self.stride, self.offset + pointer)


class VertexAttribute(AbstractAttribute):
    plural = 'vertices'

    def __init__(self, count, gl_type):
        super(VertexAttribute, self).__init__(count, gl_type)

    def enable(self):
        glEnableClientState(GL_VERTEX_ARRAY)

    def set_pointer(self, pointer):
        glVertexPointer(self.count, self.gl_type, self.stride, self.offset + pointer)


class GenericAttribute(AbstractAttribute):

    def __init__(self, index, normalized, count, gl_type):
        self.normalized = bool(normalized)
        self.index = index
        super(GenericAttribute, self).__init__(count, gl_type)

    def enable(self):
        glEnableVertexAttribArray(self.index)

    def set_pointer(self, pointer):
        glVertexAttribPointer(self.index, self.count, self.gl_type, self.normalized, self.stride, self.offset + pointer)


_attribute_classes = {'c': ColorAttribute, 
   'e': EdgeFlagAttribute, 
   'f': FogCoordAttribute, 
   'n': NormalAttribute, 
   's': SecondaryColorAttribute, 
   't': TexCoordAttribute, 
   'v': VertexAttribute}
# okay decompiling out\pyglet.graphics.vertexattribute.pyc
