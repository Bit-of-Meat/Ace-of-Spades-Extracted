# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.graphics.vertexbuffer
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import ctypes, sys, pyglet
from ..pyglet.gl import *
_enable_vbo = pyglet.options['graphics_vbo']
_workaround_vbo_finish = False

def create_buffer(size, target=GL_ARRAY_BUFFER, usage=GL_DYNAMIC_DRAW, vbo=True):
    from pyglet import gl
    if vbo and gl_info.have_version(1, 5) and _enable_vbo and not gl.current_context._workaround_vbo:
        return VertexBufferObject(size, target, usage)
    else:
        return VertexArray(size)


def create_mappable_buffer(size, target=GL_ARRAY_BUFFER, usage=GL_DYNAMIC_DRAW, vbo=True):
    from pyglet import gl
    if vbo and gl_info.have_version(1, 5) and _enable_vbo and not gl.current_context._workaround_vbo:
        return MappableVertexBufferObject(size, target, usage)
    else:
        return VertexArray(size)


class AbstractBuffer(object):
    ptr = 0
    size = 0

    def bind(self):
        raise NotImplementedError('abstract')

    def unbind(self):
        raise NotImplementedError('abstract')

    def set_data(self, data):
        raise NotImplementedError('abstract')

    def set_data_region(self, data, start, length):
        raise NotImplementedError('abstract')

    def map(self, invalidate=False):
        raise NotImplementedError('abstract')

    def unmap(self):
        raise NotImplementedError('abstract')

    def resize(self, size):
        pass

    def delete(self):
        raise NotImplementedError('abstract')


class AbstractMappable(object):

    def get_region(self, start, size, ptr_type):
        raise NotImplementedError('abstract')


class VertexArray(AbstractBuffer, AbstractMappable):

    def __init__(self, size):
        self.size = size
        self.array = (ctypes.c_byte * size)()
        self.ptr = ctypes.cast(self.array, ctypes.c_void_p).value

    def bind(self):
        pass

    def unbind(self):
        pass

    def set_data(self, data):
        ctypes.memmove(self.ptr, data, self.size)

    def set_data_region(self, data, start, length):
        ctypes.memmove(self.ptr + start, data, length)

    def map(self, invalidate=False):
        return self.array

    def unmap(self):
        pass

    def get_region(self, start, size, ptr_type):
        array = ctypes.cast(self.ptr + start, ptr_type).contents
        return VertexArrayRegion(array)

    def delete(self):
        pass

    def resize(self, size):
        array = (ctypes.c_byte * size)()
        ctypes.memmove(array, self.array, min(size, self.size))
        self.size = size
        self.array = array
        self.ptr = ctypes.cast(self.array, ctypes.c_void_p).value


class VertexBufferObject(AbstractBuffer):

    def __init__(self, size, target, usage):
        global _workaround_vbo_finish
        self.size = size
        self.target = target
        self.usage = usage
        self._context = pyglet.gl.current_context
        id = GLuint()
        glGenBuffers(1, id)
        self.id = id.value
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glBindBuffer(target, self.id)
        glBufferData(target, self.size, None, self.usage)
        glPopClientAttrib()
        if pyglet.gl.current_context._workaround_vbo_finish:
            _workaround_vbo_finish = True
        return

    def bind(self):
        glBindBuffer(self.target, self.id)

    def unbind(self):
        glBindBuffer(self.target, 0)

    def set_data(self, data):
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glBindBuffer(self.target, self.id)
        glBufferData(self.target, self.size, data, self.usage)
        glPopClientAttrib()

    def set_data_region(self, data, start, length):
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glBindBuffer(self.target, self.id)
        glBufferSubData(self.target, start, length, data)
        glPopClientAttrib()

    def map(self, invalidate=False):
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glBindBuffer(self.target, self.id)
        if invalidate:
            glBufferData(self.target, self.size, None, self.usage)
        ptr = ctypes.cast(glMapBuffer(self.target, GL_WRITE_ONLY), ctypes.POINTER(ctypes.c_byte * self.size)).contents
        glPopClientAttrib()
        return ptr

    def unmap(self):
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glUnmapBuffer(self.target)
        glPopClientAttrib()

    def __del__(self):
        try:
            if self.id is not None:
                self._context.delete_buffer(self.id)
        except:
            pass

        return

    def delete(self):
        id = GLuint(self.id)
        glDeleteBuffers(1, id)
        self.id = None
        return

    def resize(self, size):
        temp = (ctypes.c_byte * size)()
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glBindBuffer(self.target, self.id)
        data = glMapBuffer(self.target, GL_READ_ONLY)
        ctypes.memmove(temp, data, min(size, self.size))
        glUnmapBuffer(self.target)
        self.size = size
        glBufferData(self.target, self.size, temp, self.usage)
        glPopClientAttrib()


class MappableVertexBufferObject(VertexBufferObject, AbstractMappable):

    def __init__(self, size, target, usage):
        super(MappableVertexBufferObject, self).__init__(size, target, usage)
        self.data = (ctypes.c_byte * size)()
        self.data_ptr = ctypes.cast(self.data, ctypes.c_void_p).value
        self._dirty_min = sys.maxint
        self._dirty_max = 0

    def bind(self):
        super(MappableVertexBufferObject, self).bind()
        size = self._dirty_max - self._dirty_min
        if size > 0:
            if size == self.size:
                glBufferData(self.target, self.size, self.data, self.usage)
            else:
                glBufferSubData(self.target, self._dirty_min, size, self.data_ptr + self._dirty_min)
            self._dirty_min = sys.maxint
            self._dirty_max = 0

    def set_data(self, data):
        super(MappableVertexBufferObject, self).set_data(data)
        ctypes.memmove(self.data, data, self.size)
        self._dirty_min = 0
        self._dirty_max = self.size

    def set_data_region(self, data, start, length):
        ctypes.memmove(self.data_ptr + start, data, length)
        self._dirty_min = min(start, self._dirty_min)
        self._dirty_max = max(start + length, self._dirty_max)

    def map(self, invalidate=False):
        self._dirty_min = 0
        self._dirty_max = self.size
        return self.data

    def unmap(self):
        pass

    def get_region(self, start, size, ptr_type):
        array = ctypes.cast(self.data_ptr + start, ptr_type).contents
        return VertexBufferObjectRegion(self, start, start + size, array)

    def resize(self, size):
        data = (ctypes.c_byte * size)()
        ctypes.memmove(data, self.data, min(size, self.size))
        self.data = data
        self.data_ptr = ctypes.cast(self.data, ctypes.c_void_p).value
        self.size = size
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glBindBuffer(self.target, self.id)
        glBufferData(self.target, self.size, self.data, self.usage)
        glPopClientAttrib()
        self._dirty_min = sys.maxint
        self._dirty_max = 0


class AbstractBufferRegion(object):

    def invalidate(self):
        pass


class VertexBufferObjectRegion(AbstractBufferRegion):

    def __init__(self, buffer, start, end, array):
        self.buffer = buffer
        self.start = start
        self.end = end
        self.array = array

    def invalidate(self):
        buffer = self.buffer
        buffer._dirty_min = min(buffer._dirty_min, self.start)
        buffer._dirty_max = max(buffer._dirty_max, self.end)


class VertexArrayRegion(AbstractBufferRegion):

    def __init__(self, array):
        self.array = array


class IndirectArrayRegion(AbstractBufferRegion):

    def __init__(self, region, size, component_count, component_stride):
        self.region = region
        self.size = size
        self.count = component_count
        self.stride = component_stride
        self.array = self

    def __repr__(self):
        return 'IndirectArrayRegion(size=%d, count=%d, stride=%d)' % (
         self.size, self.count, self.stride)

    def __getitem__(self, index):
        count = self.count
        if not isinstance(index, slice):
            elem = index // count
            j = index % count
            return self.region.array[elem * self.stride + j]
        else:
            start = index.start or 0
            stop = index.stop
            step = index.step or 1
            if start < 0:
                start = self.size + start
            if stop is None:
                stop = self.size
            elif stop < 0:
                stop = self.size + stop
            data_start = start // count * self.stride + start % count
            data_stop = stop // count * self.stride + stop % count
            data_step = step * self.stride
            value_step = step * count
            data = self.region.array[:]
            value = [0] * ((stop - start) // step)
            stride = self.stride
            for i in range(count):
                value[i::value_step] = data[data_start + i:data_stop + i:data_step]

            return value

    def __setitem__(self, index, value):
        count = self.count
        if not isinstance(index, slice):
            elem = index // count
            j = index % count
            self.region.array[elem * self.stride + j] = value
            return
        else:
            start = index.start or 0
            stop = index.stop
            step = index.step or 1
            if start < 0:
                start = self.size + start
            if stop is None:
                stop = self.size
            elif stop < 0:
                stop = self.size + stop
            data_start = start // count * self.stride + start % count
            data_stop = stop // count * self.stride + stop % count
            data = self.region.array[:]
            if step == 1:
                data_step = self.stride
                value_step = count
                for i in range(count):
                    data[data_start + i:data_stop + i:data_step] = value[i::value_step]

            else:
                data_step = step // count * self.stride
                data[data_start:data_stop:data_step] = value
            self.region.array[:] = data
            return

    def invalidate(self):
        self.region.invalidate()
# okay decompiling out\pyglet.graphics.vertexbuffer.pyc
