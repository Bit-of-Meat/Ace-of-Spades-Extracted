# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import sys, re, warnings, weakref
from ..ctypes import *
from math import ceil
from StringIO import StringIO
from pyglet import gl
from ..pyglet.gl import *
from pyglet.gl import gl_info
from pyglet import graphics
from ..pyglet.window import *
from pyglet.image import atlas
from pyglet.compat import asbytes

class ImageException(Exception):
    pass


def load(filename, file=None, decoder=None):
    if not file:
        file = open(filename, 'rb')
    if not hasattr(file, 'seek'):
        file = StringIO(file.read())
    if decoder:
        return decoder.decode(file, filename)
    else:
        first_exception = None
        for decoder in codecs.get_decoders(filename):
            try:
                image = decoder.decode(file, filename)
                return image
            except codecs.ImageDecodeException as e:
                if not first_exception or first_exception.exception_priority < e.exception_priority:
                    first_exception = e
                file.seek(0)

        if not first_exception:
            raise codecs.ImageDecodeException('No image decoders are available')
        raise first_exception
        return


def create(width, height, pattern=None):
    if not pattern:
        pattern = SolidColorImagePattern()
    return pattern.create_image(width, height)


class ImagePattern(object):

    def create_image(self, width, height):
        raise NotImplementedError('abstract')


class SolidColorImagePattern(ImagePattern):

    def __init__(self, color=(0, 0, 0, 0)):
        self.color = '%c%c%c%c' % color

    def create_image(self, width, height):
        data = self.color * width * height
        return ImageData(width, height, 'RGBA', data)


class CheckerImagePattern(ImagePattern):

    def __init__(self, color1=(150, 150, 150, 255), color2=(200, 200, 200, 255)):
        self.color1 = '%c%c%c%c' % color1
        self.color2 = '%c%c%c%c' % color2

    def create_image(self, width, height):
        hw = width // 2
        hh = height // 2
        row1 = self.color1 * hw + self.color2 * hw
        row2 = self.color2 * hw + self.color1 * hw
        data = row1 * hh + row2 * hh
        return ImageData(width, height, 'RGBA', data)


class AbstractImage(object):
    anchor_x = 0
    anchor_y = 0
    _is_rectangle = False

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return '<%s %dx%d>' % (self.__class__.__name__, self.width, self.height)

    def get_image_data(self):
        raise ImageException('Cannot retrieve image data for %r' % self)

    image_data = property((lambda self: self.get_image_data()), doc='An `ImageData` view of this image.  \n        \n        Changes to the returned instance may or may not be reflected in this\n        image.  Read-only.\n\n        :deprecated: Use `get_image_data`.\n\n        :type: `ImageData`\n        ')

    def get_texture(self, rectangle=False, force_rectangle=False):
        raise ImageException('Cannot retrieve texture for %r' % self)

    texture = property((lambda self: self.get_texture()), doc='Get a `Texture` view of this image.  \n        \n        Changes to the returned instance may or may not be reflected in this\n        image.\n\n        :deprecated: Use `get_texture`.\n\n        :type: `Texture`\n        ')

    def get_mipmapped_texture(self):
        raise ImageException('Cannot retrieve mipmapped texture for %r' % self)

    mipmapped_texture = property((lambda self: self.get_mipmapped_texture()), doc='A Texture view of this image.  \n        \n        The returned Texture will have mipmaps filled in for all levels.\n        Requires that image dimensions be powers of 2.  Read-only.\n\n        :deprecated: Use `get_mipmapped_texture`.\n\n        :type: `Texture`\n        ')

    def get_region(self, x, y, width, height):
        raise ImageException('Cannot get region for %r' % self)

    def save(self, filename=None, file=None, encoder=None):
        if not file:
            file = open(filename, 'wb')
        if encoder:
            encoder.encode(self, file, filename)
        else:
            first_exception = None
            for encoder in codecs.get_encoders(filename):
                try:
                    encoder.encode(self, file, filename)
                    return
                except codecs.ImageDecodeException as e:
                    first_exception = first_exception or e
                    file.seek(0)

            if not first_exception:
                raise codecs.ImageEncodeException('No image encoders are available')
            raise first_exception
        return

    def blit(self, x, y, z=0):
        raise ImageException('Cannot blit %r.' % self)

    def blit_into(self, source, x, y, z):
        raise ImageException('Cannot blit images onto %r.' % self)

    def blit_to_texture(self, target, level, x, y, z=0):
        raise ImageException('Cannot blit %r to a texture.' % self)


class AbstractImageSequence(object):

    def get_texture_sequence(self):
        raise NotImplementedError('abstract')

    texture_sequence = property((lambda self: self.get_texture_sequence()), doc='Access this image sequence as a texture sequence.\n        \n        :deprecated: Use `get_texture_sequence`\n\n        :type: `TextureSequence`\n        ')

    def get_animation(self, period, loop=True):
        return Animation.from_image_sequence(self, period, loop)

    def __getitem__(self, slice):
        raise NotImplementedError('abstract')

    def __setitem__(self, slice, image):
        raise NotImplementedError('abstract')

    def __len__(self):
        raise NotImplementedError('abstract')

    def __iter__(self):
        raise NotImplementedError('abstract')


class TextureSequence(AbstractImageSequence):

    def get_texture_sequence(self):
        return self


class UniformTextureSequence(TextureSequence):

    def _get_item_width(self):
        raise NotImplementedError('abstract')

    item_width = property(_get_item_width)

    def _get_item_height(self):
        raise NotImplementedError('abstract')

    item_height = property(_get_item_height)


class ImageData(AbstractImage):
    _swap1_pattern = re.compile('(.)', re.DOTALL)
    _swap2_pattern = re.compile('(.)(.)', re.DOTALL)
    _swap3_pattern = re.compile('(.)(.)(.)', re.DOTALL)
    _swap4_pattern = re.compile('(.)(.)(.)(.)', re.DOTALL)
    _current_texture = None
    _current_mipmap_texture = None

    def __init__(self, width, height, format, data, pitch=None):
        super(ImageData, self).__init__(width, height)
        self._current_format = self._desired_format = format.upper()
        self._current_data = data
        if not pitch:
            pitch = width * len(format)
        self._current_pitch = self.pitch = pitch
        self.mipmap_images = []

    def __getstate__(self):
        return {'width': self.width, 
           'height': self.height, 
           '_current_data': self.get_data(self._current_format, self._current_pitch), 
           '_current_format': self._current_format, 
           '_desired_format': self._desired_format, 
           '_current_pitch': self._current_pitch, 
           'pitch': self.pitch, 
           'mipmap_images': self.mipmap_images}

    def get_image_data(self):
        return self

    def _set_format(self, format):
        self._desired_format = format.upper()
        self._current_texture = None
        return

    format = property((lambda self: self._desired_format), _set_format, doc='Format string of the data.  Read-write.\n        \n        :type: str\n        ')

    def _get_data(self):
        if self._current_pitch != self.pitch or self._current_format != self.format:
            self._current_data = self._convert(self.format, self.pitch)
            self._current_format = self.format
            self._current_pitch = self.pitch
        self._ensure_string_data()
        return self._current_data

    def _set_data(self, data):
        self._current_data = data
        self._current_format = self.format
        self._current_pitch = self.pitch
        self._current_texture = None
        self._current_mipmapped_texture = None
        return

    data = property(_get_data, _set_data, doc='The byte data of the image.  Read-write.\n\n        :deprecated: Use `get_data` and `set_data`.\n        \n        :type: sequence of bytes, or str\n        ')

    def get_data(self, format, pitch):
        if format == self._current_format and pitch == self._current_pitch:
            return self._current_data
        return self._convert(format, pitch)

    def set_data(self, format, pitch, data):
        self._current_format = format
        self._current_pitch = pitch
        self._current_data = data
        self._current_texture = None
        self._current_mipmapped_texture = None
        return

    def set_mipmap_image(self, level, image):
        if level == 0:
            raise ImageException('Cannot set mipmap image at level 0 (it is this image)')
        if not _is_pow2(self.width) or not _is_pow2(self.height):
            raise ImageException('Image dimensions must be powers of 2 to use mipmaps.')
        width, height = self.width, self.height
        for i in range(level):
            width >>= 1
            height >>= 1

        if width != image.width or height != image.height:
            raise ImageException('Mipmap image has wrong dimensions for level %d' % level)
        self.mipmap_images += [None] * (level - len(self.mipmap_images))
        self.mipmap_images[level - 1] = image
        return

    def create_texture(self, cls, rectangle=False, force_rectangle=False):
        internalformat = self._get_internalformat(self.format)
        texture = cls.create(self.width, self.height, internalformat, rectangle, force_rectangle)
        if self.anchor_x or self.anchor_y:
            texture.anchor_x = self.anchor_x
            texture.anchor_y = self.anchor_y
        self.blit_to_texture(texture.target, texture.level, self.anchor_x, self.anchor_y, 0, None)
        return texture

    def get_texture(self, rectangle=False, force_rectangle=False):
        if not self._current_texture or not self._current_texture._is_rectangle and force_rectangle:
            self._current_texture = self.create_texture(Texture, rectangle, force_rectangle)
        return self._current_texture

    def get_mipmapped_texture(self):
        if self._current_mipmap_texture:
            return self._current_mipmap_texture
        if not _is_pow2(self.width) or not _is_pow2(self.height):
            raise ImageException('Image dimensions must be powers of 2 to use mipmaps.')
        texture = Texture.create_for_size(GL_TEXTURE_2D, self.width, self.height)
        if self.anchor_x or self.anchor_y:
            texture.anchor_x = self.anchor_x
            texture.anchor_y = self.anchor_y
        internalformat = self._get_internalformat(self.format)
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        if self.mipmap_images:
            self.blit_to_texture(texture.target, texture.level, self.anchor_x, self.anchor_y, 0, internalformat)
            level = 0
            for image in self.mipmap_images:
                level += 1
                if image:
                    image.blit_to_texture(texture.target, level, self.anchor_x, self.anchor_y, 0, internalformat)

        elif gl_info.have_version(1, 4):
            glTexParameteri(texture.target, GL_GENERATE_MIPMAP, GL_TRUE)
            self.blit_to_texture(texture.target, texture.level, self.anchor_x, self.anchor_y, 0, internalformat)
        else:
            raise NotImplementedError('TODO: gluBuild2DMipmaps')
        self._current_mipmap_texture = texture
        return texture

    def get_region(self, x, y, width, height):
        return ImageDataRegion(x, y, width, height, self)

    def blit(self, x, y, z=0, width=None, height=None):
        self.get_texture().blit(x, y, z, width, height)

    def blit_to_texture(self, target, level, x, y, z, internalformat=None):
        x -= self.anchor_x
        y -= self.anchor_y
        data_format = self.format
        data_pitch = abs(self._current_pitch)
        matrix = None
        format, type = self._get_gl_format_and_type(data_format)
        if format is None:
            if len(data_format) in (3, 4) and gl_info.have_extension('GL_ARB_imaging'):

                def component_column(component):
                    try:
                        pos = ('RGBA').index(component)
                        return [0] * pos + [1] + [0] * (3 - pos)
                    except ValueError:
                        return [
                         0, 0, 0, 0]

                lookup_format = data_format + 'XXX'
                matrix = component_column(lookup_format[0]) + component_column(lookup_format[1]) + component_column(lookup_format[2]) + component_column(lookup_format[3])
                format = {3: GL_RGB, 
                   4: GL_RGBA}.get(len(data_format))
                type = GL_UNSIGNED_BYTE
                glMatrixMode(GL_COLOR)
                glPushMatrix()
                glLoadMatrixf((GLfloat * 16)(*matrix))
            else:
                data_format = {1: 'L', 2: 'LA', 
                   3: 'RGB', 
                   4: 'RGBA'}.get(len(data_format))
                format, type = self._get_gl_format_and_type(data_format)
        if gl.current_context and gl.current_context._workaround_unpack_row_length:
            data_pitch = self.width * len(data_format)
        data = self._convert(data_format, data_pitch)
        if data_pitch & 1:
            alignment = 1
        elif data_pitch & 2:
            alignment = 2
        else:
            alignment = 4
        row_length = data_pitch // len(data_format)
        glPushClientAttrib(GL_CLIENT_PIXEL_STORE_BIT)
        glPixelStorei(GL_UNPACK_ALIGNMENT, alignment)
        glPixelStorei(GL_UNPACK_ROW_LENGTH, row_length)
        self._apply_region_unpack()
        if target == GL_TEXTURE_3D:
            glTexSubImage3D(target, level, x, y, z, self.width, self.height, 1, format, type, data)
        elif internalformat:
            glTexImage2D(target, level, internalformat, self.width, self.height, 0, format, type, data)
        else:
            glTexSubImage2D(target, level, x, y, self.width, self.height, format, type, data)
        glPopClientAttrib()
        if matrix:
            glPopMatrix()
            glMatrixMode(GL_MODELVIEW)
        glFlush()
        return

    def _apply_region_unpack(self):
        pass

    def _convert(self, format, pitch):
        if format == self._current_format and pitch == self._current_pitch:
            return self._current_data
        self._ensure_string_data()
        data = self._current_data
        current_pitch = self._current_pitch
        current_format = self._current_format
        sign_pitch = current_pitch // abs(current_pitch)
        if format != self._current_format:
            repl = ''
            for c in format:
                try:
                    idx = current_format.index(c) + 1
                except ValueError:
                    idx = 1

                repl += '\\%d' % idx

            if len(current_format) == 1:
                swap_pattern = self._swap1_pattern
            elif len(current_format) == 2:
                swap_pattern = self._swap2_pattern
            elif len(current_format) == 3:
                swap_pattern = self._swap3_pattern
            elif len(current_format) == 4:
                swap_pattern = self._swap4_pattern
            else:
                raise ImageException('Current image format is wider than 32 bits.')
            packed_pitch = self.width * len(current_format)
            if abs(self._current_pitch) != packed_pitch:
                rows = re.findall('.' * abs(self._current_pitch), data, re.DOTALL)
                rows = [ swap_pattern.sub(repl, r[:packed_pitch]) for r in rows ]
                data = ('').join(rows)
            else:
                data = swap_pattern.sub(repl, data)
            current_pitch = sign_pitch * (len(format) * self.width)
        if pitch != current_pitch:
            diff = abs(current_pitch) - abs(pitch)
            if diff > 0:
                pattern = re.compile('(%s)%s' % ('.' * abs(pitch), '.' * diff), re.DOTALL)
                data = pattern.sub('\\1', data)
            elif diff < 0:
                pattern = re.compile('(%s)' % ('.' * abs(current_pitch)), re.DOTALL)
                pad = '.' * -diff
                data = pattern.sub('\\1%s' % pad, data)
            if current_pitch * pitch < 0:
                rows = re.findall(asbytes('.') * abs(pitch), data, re.DOTALL)
                rows.reverse()
                data = asbytes('').join(rows)
        return data

    def _ensure_string_data(self):
        if type(self._current_data) is not str:
            buf = create_string_buffer(len(self._current_data))
            memmove(buf, self._current_data, len(self._current_data))
            self._current_data = buf.raw

    def _get_gl_format_and_type(self, format):
        if format == 'I':
            return (GL_LUMINANCE, GL_UNSIGNED_BYTE)
        else:
            if format == 'L':
                return (GL_LUMINANCE, GL_UNSIGNED_BYTE)
            if format == 'LA':
                return (GL_LUMINANCE_ALPHA, GL_UNSIGNED_BYTE)
            if format == 'R':
                return (GL_RED, GL_UNSIGNED_BYTE)
            if format == 'G':
                return (GL_GREEN, GL_UNSIGNED_BYTE)
            if format == 'B':
                return (GL_BLUE, GL_UNSIGNED_BYTE)
            if format == 'A':
                return (GL_ALPHA, GL_UNSIGNED_BYTE)
            if format == 'RGB':
                return (GL_RGB, GL_UNSIGNED_BYTE)
            if format == 'RGBA':
                return (GL_RGBA, GL_UNSIGNED_BYTE)
            if format == 'ARGB' and gl_info.have_extension('GL_EXT_bgra') and gl_info.have_extension('GL_APPLE_packed_pixels'):
                return (GL_BGRA, GL_UNSIGNED_INT_8_8_8_8_REV)
            if format == 'ABGR' and gl_info.have_extension('GL_EXT_abgr'):
                return (GL_ABGR_EXT, GL_UNSIGNED_BYTE)
            if format == 'BGR' and gl_info.have_extension('GL_EXT_bgra'):
                return (GL_BGR, GL_UNSIGNED_BYTE)
            if format == 'BGRA' and gl_info.have_extension('GL_EXT_bgra'):
                return (GL_BGRA, GL_UNSIGNED_BYTE)
            return (None, None)

    def _get_internalformat(self, format):
        if len(format) == 4:
            return GL_RGBA
        if len(format) == 3:
            return GL_RGB
        if len(format) == 2:
            return GL_LUMINANCE_ALPHA
        if format == 'A':
            return GL_ALPHA
        if format == 'L':
            return GL_LUMINANCE
        if format == 'I':
            return GL_INTENSITY
        return GL_RGBA


class ImageDataRegion(ImageData):

    def __init__(self, x, y, width, height, image_data):
        super(ImageDataRegion, self).__init__(width, height, image_data._current_format, image_data._current_data, image_data._current_pitch)
        self.x = x
        self.y = y

    def __getstate__(self):
        return {'width': self.width, 
           'height': self.height, 
           '_current_data': self.get_data(self._current_format, self._current_pitch), 
           '_current_format': self._current_format, 
           '_desired_format': self._desired_format, 
           '_current_pitch': self._current_pitch, 
           'pitch': self.pitch, 
           'mipmap_images': self.mipmap_images, 
           'x': self.x, 
           'y': self.y}

    def _get_data(self):
        x1 = len(self._current_format) * self.x
        x2 = len(self._current_format) * (self.x + self.width)
        self._ensure_string_data()
        data = self._convert(self._current_format, abs(self._current_pitch))
        rows = re.findall('.' * abs(self._current_pitch), data, re.DOTALL)
        rows = [ row[x1:x2] for row in rows[self.y:self.y + self.height] ]
        self._current_data = ('').join(rows)
        self._current_pitch = self.width * len(self._current_format)
        self._current_texture = None
        self.x = 0
        self.y = 0
        return super(ImageDataRegion, self)._get_data()

    def _set_data(self, data):
        self.x = 0
        self.y = 0
        super(ImageDataRegion, self)._set_data(data)

    data = property(_get_data, _set_data)

    def get_data(self, format, pitch):
        x1 = len(self._current_format) * self.x
        x2 = len(self._current_format) * (self.x + self.width)
        self._ensure_string_data()
        data = self._convert(self._current_format, abs(self._current_pitch))
        rows = re.findall(asbytes('.') * abs(self._current_pitch), data, re.DOTALL)
        rows = [ row[x1:x2] for row in rows[self.y:self.y + self.height] ]
        self._current_data = asbytes('').join(rows)
        self._current_pitch = self.width * len(self._current_format)
        self._current_texture = None
        self.x = 0
        self.y = 0
        return super(ImageDataRegion, self).get_data(format, pitch)

    def _apply_region_unpack(self):
        glPixelStorei(GL_UNPACK_SKIP_PIXELS, self.x)
        glPixelStorei(GL_UNPACK_SKIP_ROWS, self.y)

    def _ensure_string_data(self):
        super(ImageDataRegion, self)._ensure_string_data()

    def get_region(self, x, y, width, height):
        x += self.x
        y += self.y
        return super(ImageDataRegion, self).get_region(x, y, width, height)


class CompressedImageData(AbstractImage):
    _current_texture = None
    _current_mipmapped_texture = None

    def __init__(self, width, height, gl_format, data, extension=None, decoder=None):
        if not _is_pow2(width) or not _is_pow2(height):
            raise ImageException('Dimensions of %r must be powers of 2' % self)
        super(CompressedImageData, self).__init__(width, height)
        self.data = data
        self.gl_format = gl_format
        self.extension = extension
        self.decoder = decoder
        self.mipmap_data = []

    def set_mipmap_data(self, level, data):
        self.mipmap_data += [None] * (level - len(self.mipmap_data))
        self.mipmap_data[level - 1] = data
        return

    def _have_extension(self):
        return self.extension is None or gl_info.have_extension(self.extension)

    def _verify_driver_supported(self):
        if not self._have_extension():
            raise ImageException('%s is required to decode %r' % (
             self.extension, self))

    def get_texture(self, rectangle=False, force_rectangle=False):
        if force_rectangle:
            raise ImageException('Compressed texture rectangles not supported')
        if self._current_texture:
            return self._current_texture
        texture = Texture.create_for_size(GL_TEXTURE_2D, self.width, self.height)
        if self.anchor_x or self.anchor_y:
            texture.anchor_x = self.anchor_x
            texture.anchor_y = self.anchor_y
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target, GL_TEXTURE_MIN_FILTER, texture.min_filter)
        glTexParameteri(texture.target, GL_TEXTURE_MAG_FILTER, texture.mag_filter)
        if self._have_extension():
            glCompressedTexImage2DARB(texture.target, texture.level, self.gl_format, self.width, self.height, 0, len(self.data), self.data)
        else:
            image = self.decoder(self.data, self.width, self.height)
            texture = image.get_texture()
        glFlush()
        self._current_texture = texture
        return texture

    def get_mipmapped_texture(self):
        if self._current_mipmap_texture:
            return self._current_mipmap_texture
        if not self._have_extension():
            return self.get_texture()
        texture = Texture.create_for_size(GL_TEXTURE_2D, self.width, self.height)
        if self.anchor_x or self.anchor_y:
            texture.anchor_x = self.anchor_x
            texture.anchor_y = self.anchor_y
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        if not self.mipmap_data:
            if not gl_info.have_version(1, 4):
                raise ImageException('Require GL 1.4 to generate mipmaps for compressed textures')
            glTexParameteri(texture.target, GL_GENERATE_MIPMAP, GL_TRUE)
        glCompressedTexImage2DARB(texture.target, texture.level, self.gl_format, self.width, self.height, 0, len(self.data), self.data)
        width, height = self.width, self.height
        level = 0
        for data in self.mipmap_data:
            width >>= 1
            height >>= 1
            level += 1
            glCompressedTexImage2DARB(texture.target, level, self.gl_format, width, height, 0, len(data), data)

        glFlush()
        self._current_mipmap_texture = texture
        return texture

    def blit_to_texture(self, target, level, x, y, z):
        self._verify_driver_supported()
        if target == GL_TEXTURE_3D:
            glCompressedTexSubImage3DARB(target, level, x - self.anchor_x, y - self.anchor_y, z, self.width, self.height, 1, self.gl_format, len(self.data), self.data)
        else:
            glCompressedTexSubImage2DARB(target, level, x - self.anchor_x, y - self.anchor_y, self.width, self.height, self.gl_format, len(self.data), self.data)


def _nearest_pow2(v):
    v -= 1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    return v + 1


def _is_pow2(v):
    return v & v - 1 == 0


class Texture(AbstractImage):
    region_class = None
    tex_coords = (0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)
    tex_coords_order = (0, 1, 2, 3)
    level = 0
    images = 1
    x = y = z = 0

    def __init__(self, width, height, target, id):
        super(Texture, self).__init__(width, height)
        self.target = target
        self.id = id
        self._context = gl.current_context

    def delete(self):
        warnings.warn('Texture.delete() is deprecated; textures are released through GC now')
        self._context.delete_texture(self.id)
        self.id = 0

    def __del__(self):
        try:
            self._context.delete_texture(self.id)
        except:
            pass

    @classmethod
    def create(cls, width, height, internalformat=GL_RGBA, rectangle=False, force_rectangle=False, min_filter=GL_LINEAR, mag_filter=GL_LINEAR):
        target = GL_TEXTURE_2D
        if rectangle or force_rectangle:
            if not force_rectangle and _is_pow2(width) and _is_pow2(height):
                rectangle = False
            elif gl_info.have_extension('GL_ARB_texture_rectangle'):
                target = GL_TEXTURE_RECTANGLE_ARB
                rectangle = True
            else:
                if gl_info.have_extension('GL_NV_texture_rectangle'):
                    target = GL_TEXTURE_RECTANGLE_NV
                    rectangle = True
                else:
                    rectangle = False
        if force_rectangle and not rectangle:
            raise ImageException('Texture rectangle extensions not available')
        if rectangle:
            texture_width = width
            texture_height = height
        else:
            texture_width = _nearest_pow2(width)
            texture_height = _nearest_pow2(height)
        id = GLuint()
        glGenTextures(1, byref(id))
        glBindTexture(target, id.value)
        glTexParameteri(target, GL_TEXTURE_MIN_FILTER, min_filter)
        glTexParameteri(target, GL_TEXTURE_MAG_FILTER, mag_filter)
        blank = (GLubyte * (texture_width * texture_height * 4))()
        glTexImage2D(target, 0, internalformat, texture_width, texture_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, blank)
        texture = cls(texture_width, texture_height, target, id.value)
        texture.min_filter = min_filter
        texture.mag_filter = mag_filter
        if rectangle:
            texture._is_rectangle = True
            texture.tex_coords = (0.0, 0.0, 0.0,
             width, 0.0, 0.0,
             width, height, 0.0,
             0.0, height, 0.0)
        glFlush()
        if texture_width == width and texture_height == height:
            return texture
        return texture.get_region(0, 0, width, height)

    @classmethod
    def create_for_size(cls, target, min_width, min_height, internalformat=None, min_filter=GL_LINEAR, mag_filter=GL_LINEAR):
        if target not in (GL_TEXTURE_RECTANGLE_NV, GL_TEXTURE_RECTANGLE_ARB):
            width = _nearest_pow2(min_width)
            height = _nearest_pow2(min_height)
            tex_coords = cls.tex_coords
        else:
            width = min_width
            height = min_height
            tex_coords = (0.0, 0.0, 0.0,
             width, 0.0, 0.0,
             width, height, 0.0,
             0.0, height, 0.0)
        id = GLuint()
        glGenTextures(1, byref(id))
        glBindTexture(target, id.value)
        glTexParameteri(target, GL_TEXTURE_MIN_FILTER, min_filter)
        glTexParameteri(target, GL_TEXTURE_MAG_FILTER, mag_filter)
        if internalformat is not None:
            blank = (GLubyte * (width * height * 4))()
            glTexImage2D(target, 0, internalformat, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, blank)
            glFlush()
        texture = cls(width, height, target, id.value)
        texture.min_filter = min_filter
        texture.mag_filter = mag_filter
        texture.tex_coords = tex_coords
        return texture

    def get_image_data(self, z=0):
        glBindTexture(self.target, self.id)
        format = 'RGBA'
        gl_format = GL_RGBA
        glPushClientAttrib(GL_CLIENT_PIXEL_STORE_BIT)
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        buffer = (GLubyte * (self.width * self.height * self.images * len(format)))()
        glGetTexImage(self.target, self.level, gl_format, GL_UNSIGNED_BYTE, buffer)
        glPopClientAttrib()
        data = ImageData(self.width, self.height, format, buffer)
        if self.images > 1:
            data = data.get_region(0, z * self.height, self.width, self.height)
        return data

    image_data = property((lambda self: self.get_image_data()), doc='An ImageData view of this texture.  \n        \n        Changes to the returned instance will not be reflected in this\n        texture.  If the texture is a 3D texture, the first image will be \n        returned.  See also `get_image_data`.  Read-only.\n\n        :deprecated: Use `get_image_data`.\n        \n        :type: `ImageData`\n        ')

    def get_texture(self, rectangle=False, force_rectangle=False):
        if force_rectangle and not self._is_rectangle:
            raise ImageException('Texture is not a rectangle.')
        return self

    def blit(self, x, y, z=0, width=None, height=None):
        t = self.tex_coords
        x1 = x - self.anchor_x
        y1 = y - self.anchor_y
        x2 = x1 + (width is None and self.width or width)
        y2 = y1 + (height is None and self.height or height)
        vertex_array = (GLfloat * 16)(x1, y1, z, 1.0, x2, y1, z, 1.0, x2, y2, z, 1.0, x1, y2, z, 1.0)
        tex_array = (GLfloat * 16)(t[0], t[1], t[2], 1.0, t[3], t[4], t[5], 1.0, t[6], t[7], t[8], 1.0, t[9], t[10], t[11], 1.0)
        glPushAttrib(GL_ENABLE_BIT)
        glEnable(self.target)
        glBindTexture(self.target, self.id)
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(4, GL_FLOAT, 0, vertex_array)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glTexCoordPointer(4, GL_FLOAT, 0, tex_array)
        glDrawArrays(GL_QUADS, 0, 4)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glPopClientAttrib()
        glPopAttrib()
        return

    def blit_into(self, source, x, y, z):
        glBindTexture(self.target, self.id)
        source.blit_to_texture(self.target, self.level, x, y, z)

    def get_region(self, x, y, width, height):
        return self.region_class(x, y, 0, width, height, self)

    def get_transform(self, flip_x=False, flip_y=False, rotate=0):
        transform = self.get_region(0, 0, self.width, self.height)
        bl, br, tr, tl = (0, 1, 2, 3)
        transform.anchor_x = self.anchor_x
        transform.anchor_y = self.anchor_y
        if flip_x:
            bl, br, tl, tr = (
             br, bl, tr, tl)
            transform.anchor_x = self.width - self.anchor_x
        if flip_y:
            bl, br, tl, tr = (
             tl, tr, bl, br)
            transform.anchor_y = self.height - self.anchor_y
        rotate %= 360
        if rotate < 0:
            rotate += 360
        if rotate == 0:
            pass
        elif rotate == 90:
            bl, br, tr, tl = (
             br, tr, tl, bl)
            transform.anchor_x, transform.anchor_y = transform.anchor_y, transform.width - transform.anchor_x
        elif rotate == 180:
            bl, br, tr, tl = (
             tr, tl, bl, br)
            transform.anchor_x = transform.width - transform.anchor_x
            transform.anchor_y = transform.height - transform.anchor_y
        elif rotate == 270:
            bl, br, tr, tl = (
             tl, bl, br, tr)
            transform.anchor_x, transform.anchor_y = transform.height - transform.anchor_y, transform.anchor_x
        if rotate in (90, 270):
            transform.width, transform.height = transform.height, transform.width
        transform._set_tex_coords_order(bl, br, tr, tl)
        return transform

    def _set_tex_coords_order(self, bl, br, tr, tl):
        tex_coords = (
         self.tex_coords[:3],
         self.tex_coords[3:6],
         self.tex_coords[6:9],
         self.tex_coords[9:])
        self.tex_coords = tex_coords[bl] + tex_coords[br] + tex_coords[tr] + tex_coords[tl]
        order = self.tex_coords_order
        self.tex_coords_order = (
         order[bl], order[br], order[tr], order[tl])


class TextureRegion(Texture):

    def __init__(self, x, y, z, width, height, owner):
        super(TextureRegion, self).__init__(width, height, owner.target, owner.id)
        self.x = x
        self.y = y
        self.z = z
        self.owner = owner
        owner_u1 = owner.tex_coords[0]
        owner_v1 = owner.tex_coords[1]
        owner_u2 = owner.tex_coords[3]
        owner_v2 = owner.tex_coords[7]
        scale_u = owner_u2 - owner_u1
        scale_v = owner_v2 - owner_v1
        u1 = x / float(owner.width) * scale_u + owner_u1
        v1 = y / float(owner.height) * scale_v + owner_v1
        u2 = (x + width) / float(owner.width) * scale_u + owner_u1
        v2 = (y + height) / float(owner.height) * scale_v + owner_v1
        r = z / float(owner.images) + owner.tex_coords[2]
        self.tex_coords = (u1, v1, r, u2, v1, r, u2, v2, r, u1, v2, r)

    def get_image_data(self):
        image_data = self.owner.get_image_data(self.z)
        return image_data.get_region(self.x, self.y, self.width, self.height)

    def get_region(self, x, y, width, height):
        x += self.x
        y += self.y
        region = self.region_class(x, y, self.z, width, height, self.owner)
        region._set_tex_coords_order(*self.tex_coords_order)
        return region

    def blit_into(self, source, x, y, z):
        self.owner.blit_into(source, x + self.x, y + self.y, z + self.z)

    def __del__(self):
        pass


Texture.region_class = TextureRegion

class Texture3D(Texture, UniformTextureSequence):
    item_width = 0
    item_height = 0
    items = ()

    @classmethod
    def create_for_images(cls, images, internalformat=GL_RGBA):
        item_width = images[0].width
        item_height = images[0].height
        for image in images:
            if image.width != item_width or image.height != item_height:
                raise ImageException('Images do not have same dimensions.')

        depth = len(images)
        if not gl_info.have_version(2, 0):
            depth = _nearest_pow2(depth)
        texture = cls.create_for_size(GL_TEXTURE_3D, item_width, item_height)
        if images[0].anchor_x or images[0].anchor_y:
            texture.anchor_x = images[0].anchor_x
            texture.anchor_y = images[0].anchor_y
        texture.images = depth
        blank = (GLubyte * (texture.width * texture.height * texture.images))()
        glBindTexture(texture.target, texture.id)
        glTexImage3D(texture.target, texture.level, internalformat, texture.width, texture.height, texture.images, 0, GL_ALPHA, GL_UNSIGNED_BYTE, blank)
        items = []
        for i, image in enumerate(images):
            item = cls.region_class(0, 0, i, item_width, item_height, texture)
            items.append(item)
            image.blit_to_texture(texture.target, texture.level, image.anchor_x, image.anchor_y, i)

        glFlush()
        texture.items = items
        texture.item_width = item_width
        texture.item_height = item_height
        return texture

    @classmethod
    def create_for_image_grid(cls, grid, internalformat=GL_RGBA):
        return cls.create_for_images(grid[:], internalformat)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        if type(index) is slice:
            for item, image in zip(self[index], value):
                image.blit_to_texture(self.target, self.level, image.anchor_x, image.anchor_y, item.z)

        else:
            value.blit_to_texture(self.target, self.level, value.anchor_x, value.anchor_y, self[index].z)

    def __iter__(self):
        return iter(self.items)


class TileableTexture(Texture):

    def __init__(self, width, height, target, id):
        if not _is_pow2(width) or not _is_pow2(height):
            raise ImageException('TileableTexture requires dimensions that are powers of 2')
        super(TileableTexture, self).__init__(width, height, target, id)

    def get_region(self, x, y, width, height):
        raise ImageException('Cannot get region of %r' % self)

    def blit_tiled(self, x, y, z, width, height):
        u1 = self.anchor_x / float(self.width)
        v1 = self.anchor_y / float(self.height)
        u2 = u1 + width / float(self.width)
        v2 = v1 + height / float(self.height)
        w, h = width, height
        t = self.tex_coords
        vertex_array = (GLfloat * 16)(x, y, z, 1.0, x + w, y, z, 1.0, x + w, y + h, z, 1.0, x, y + h, z, 1.0)
        tex_array = (GLfloat * 16)(u1, v1, t[2], 1.0, u2, v1, t[5], 1.0, u2, v2, t[8], 1.0, u1, v2, t[11], 1.0)
        glPushAttrib(GL_ENABLE_BIT)
        glEnable(self.target)
        glBindTexture(self.target, self.id)
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(4, GL_FLOAT, 0, vertex_array)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glTexCoordPointer(4, GL_FLOAT, 0, tex_array)
        glDrawArrays(GL_QUADS, 0, 4)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glPopClientAttrib()
        glPopAttrib()

    @classmethod
    def create_for_image(cls, image):
        if not _is_pow2(image.width) or not _is_pow2(image.height):
            image = image.get_image_data()
            texture_width = _nearest_pow2(image.width)
            texture_height = _nearest_pow2(image.height)
            newdata = c_buffer(texture_width * texture_height * 4)
            gluScaleImage(GL_RGBA, image.width, image.height, GL_UNSIGNED_BYTE, image.get_data('RGBA', image.width * 4), texture_width, texture_height, GL_UNSIGNED_BYTE, newdata)
            image = ImageData(texture_width, texture_height, 'RGBA', newdata)
        image = image.get_image_data()
        return image.create_texture(cls)


class DepthTexture(Texture):

    def blit_into(self, source, x, y, z):
        glBindTexture(self.target, self.id)
        source.blit_to_texture(self.level, x, y, z)


class BufferManager(object):

    def __init__(self):
        self.color_buffer = None
        self.depth_buffer = None
        aux_buffers = GLint()
        glGetIntegerv(GL_AUX_BUFFERS, byref(aux_buffers))
        self.free_aux_buffers = [GL_AUX0,
         GL_AUX1,
         GL_AUX2,
         GL_AUX3][:aux_buffers.value]
        stencil_bits = GLint()
        glGetIntegerv(GL_STENCIL_BITS, byref(stencil_bits))
        self.free_stencil_bits = range(stencil_bits.value)
        self.refs = []
        return

    def get_viewport(self):
        viewport = (GLint * 4)()
        glGetIntegerv(GL_VIEWPORT, viewport)
        return viewport

    def get_color_buffer(self):
        viewport = self.get_viewport()
        viewport_width = viewport[2]
        viewport_height = viewport[3]
        if not self.color_buffer or viewport_width != self.color_buffer.width or viewport_height != self.color_buffer.height:
            self.color_buffer = ColorBufferImage(*viewport)
        return self.color_buffer

    def get_aux_buffer(self):
        if not self.free_aux_buffers:
            raise ImageException('No free aux buffer is available.')
        gl_buffer = self.free_aux_buffers.pop(0)
        viewport = self.get_viewport()
        buffer = ColorBufferImage(*viewport)
        buffer.gl_buffer = gl_buffer

        def release_buffer(ref, self=self):
            self.free_aux_buffers.insert(0, gl_buffer)

        self.refs.append(weakref.ref(buffer, release_buffer))
        return buffer

    def get_depth_buffer(self):
        viewport = self.get_viewport()
        viewport_width = viewport[2]
        viewport_height = viewport[3]
        if not self.depth_buffer or viewport_width != self.depth_buffer.width or viewport_height != self.depth_buffer.height:
            self.depth_buffer = DepthBufferImage(*viewport)
        return self.depth_buffer

    def get_buffer_mask(self):
        if not self.free_stencil_bits:
            raise ImageException('No free stencil bits are available.')
        stencil_bit = self.free_stencil_bits.pop(0)
        x, y, width, height = self.get_viewport()
        buffer = BufferImageMask(x, y, width, height)
        buffer.stencil_bit = stencil_bit

        def release_buffer(ref, self=self):
            self.free_stencil_bits.insert(0, stencil_bit)

        self.refs.append(weakref.ref(buffer, release_buffer))
        return buffer


def get_buffer_manager():
    context = gl.current_context
    if not hasattr(context, 'image_buffer_manager'):
        context.image_buffer_manager = BufferManager()
    return context.image_buffer_manager


class BufferImage(AbstractImage):
    gl_buffer = GL_BACK
    gl_format = 0
    format = ''
    owner = None

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_image_data(self):
        buffer = (GLubyte * (len(self.format) * self.width * self.height))()
        x = self.x
        y = self.y
        if self.owner:
            x += self.owner.x
            y += self.owner.y
        glReadBuffer(self.gl_buffer)
        glPushClientAttrib(GL_CLIENT_PIXEL_STORE_BIT)
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        glReadPixels(x, y, self.width, self.height, self.gl_format, GL_UNSIGNED_BYTE, buffer)
        glPopClientAttrib()
        return ImageData(self.width, self.height, self.format, buffer)

    def get_region(self, x, y, width, height):
        if self.owner:
            return self.owner.get_region(x + self.x, y + self.y, width, height)
        region = self.__class__(x + self.x, y + self.y, width, height)
        region.gl_buffer = self.gl_buffer
        region.owner = self
        return region


class ColorBufferImage(BufferImage):
    gl_format = GL_RGBA
    format = 'RGBA'

    def get_texture(self, rectangle=False, force_rectangle=False):
        texture = Texture.create(self.width, self.height, GL_RGBA, rectangle, force_rectangle)
        self.blit_to_texture(texture.target, texture.level, self.anchor_x, self.anchor_y, 0)
        return texture

    def blit_to_texture(self, target, level, x, y, z):
        glReadBuffer(self.gl_buffer)
        glCopyTexSubImage2D(target, level, x - self.anchor_x, y - self.anchor_y, self.x, self.y, self.width, self.height)


class DepthBufferImage(BufferImage):
    gl_format = GL_DEPTH_COMPONENT
    format = 'L'

    def get_texture(self, rectangle=False, force_rectangle=False):
        if not _is_pow2(self.width) or not _is_pow2(self.height):
            raise ImageException('Depth texture requires that buffer dimensions be powers of 2')
        texture = DepthTexture.create_for_size(GL_TEXTURE_2D, self.width, self.height)
        if self.anchor_x or self.anchor_y:
            texture.anchor_x = self.anchor_x
            texture.anchor_y = self.anchor_y
        glReadBuffer(self.gl_buffer)
        glCopyTexImage2D(texture.target, 0, GL_DEPTH_COMPONENT, self.x, self.y, self.width, self.height, 0)
        return texture

    def blit_to_texture(self, target, level, x, y, z):
        glReadBuffer(self.gl_buffer)
        glCopyTexSubImage2D(target, level, x - self.anchor_x, y - self.anchor_y, self.x, self.y, self.width, self.height)


class BufferImageMask(BufferImage):
    gl_format = GL_STENCIL_INDEX
    format = 'L'


class ImageGrid(AbstractImage, AbstractImageSequence):
    _items = ()
    _texture_grid = None

    def __init__(self, image, rows, columns, item_width=None, item_height=None, row_padding=0, column_padding=0):
        super(ImageGrid, self).__init__(image.width, image.height)
        if item_width is None:
            item_width = int((image.width - column_padding * (columns - 1)) / columns)
        if item_height is None:
            item_height = int((image.height - row_padding * (rows - 1)) / rows)
        self.image = image
        self.rows = rows
        self.columns = columns
        self.item_width = item_width
        self.item_height = item_height
        self.row_padding = row_padding
        self.column_padding = column_padding
        return

    def get_texture(self, rectangle=False, force_rectangle=False):
        return self.image.get_texture(rectangle, force_rectangle)

    def get_image_data(self):
        return self.image.get_image_data()

    def get_texture_sequence(self):
        if not self._texture_grid:
            self._texture_grid = TextureGrid(self)
        return self._texture_grid

    def __len__(self):
        return self.rows * self.columns

    def _update_items(self):
        if not self._items:
            self._items = []
            y = 0
            for row in range(self.rows):
                x = 0
                for col in range(self.columns):
                    self._items.append(self.image.get_region(x, y, self.item_width, self.item_height))
                    x += self.item_width + self.column_padding

                y += self.item_height + self.row_padding

    def __getitem__(self, index):
        self._update_items()
        return self._items[index]

    def __iter__(self):
        self._update_items()
        return iter(self._items)


class TextureGrid(TextureRegion, UniformTextureSequence):
    items = ()
    rows = 1
    columns = 1
    item_width = 0
    item_height = 0

    def __init__(self, grid):
        image = grid.get_texture()
        if isinstance(image, TextureRegion):
            owner = image.owner
        else:
            owner = image
        super(TextureGrid, self).__init__(image.x, image.y, image.z, image.width, image.height, owner)
        items = []
        y = 0
        for row in range(grid.rows):
            x = 0
            for col in range(grid.columns):
                items.append(self.get_region(x, y, grid.item_width, grid.item_height))
                x += grid.item_width + grid.column_padding

            y += grid.item_height + grid.row_padding

        self.items = items
        self.rows = grid.rows
        self.columns = grid.columns
        self.item_width = grid.item_width
        self.item_height = grid.item_height

    def get(self, row, column):
        return self[(row, column)]

    def __getitem__(self, index):
        if type(index) is slice:
            if type(index.start) is not tuple and type(index.stop) is not tuple:
                return self.items[index]
            else:
                row1 = 0
                col1 = 0
                row2 = self.rows
                col2 = self.columns
                if type(index.start) is tuple:
                    row1, col1 = index.start
                elif type(index.start) is int:
                    row1 = index.start / self.columns
                    col1 = index.start % self.columns
                if type(index.stop) is tuple:
                    row2, col2 = index.stop
                elif type(index.stop) is int:
                    row2 = index.stop / self.columns
                    col2 = index.stop % self.columns
                result = []
                i = row1 * self.columns
                for row in range(row1, row2):
                    result += self.items[i + col1:i + col2]
                    i += self.columns

                return result

        else:
            if type(index) is tuple:
                row, column = index
                return self.items[row * self.columns + column]
            if type(index) is int:
                return self.items[index]

    def __setitem__(self, index, value):
        if type(index) is slice:
            for region, image in zip(self[index], value):
                if image.width != self.item_width or image.height != self.item_height:
                    raise ImageException('Image has incorrect dimensions')
                image.blit_into(region, image.anchor_x, image.anchor_y, 0)

        else:
            image = value
            if image.width != self.item_width or image.height != self.item_height:
                raise ImageException('Image has incorrect dimensions')
            image.blit_into(self[index], image.anchor_x, image.anchor_y, 0)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)


def load_animation(filename, file=None, decoder=None):
    if not file:
        file = open(filename, 'rb')
    if not hasattr(file, 'seek'):
        file = StringIO(file.read())
    if decoder:
        return decoder.decode(file, filename)
    else:
        first_exception = None
        for decoder in codecs.get_animation_decoders(filename):
            try:
                image = decoder.decode_animation(file, filename)
                return image
            except codecs.ImageDecodeException as e:
                first_exception = first_exception or e
                file.seek(0)

        if not first_exception:
            raise codecs.ImageDecodeException('No image decoders are available')
        raise first_exception
        return


class Animation(object):

    def __init__(self, frames):
        self.frames = frames

    def add_to_texture_bin(self, bin):
        for frame in self.frames:
            frame.image = bin.add(frame.image)

    def get_transform(self, flip_x=False, flip_y=False, rotate=0):
        frames = [ AnimationFrame(frame.image.get_texture().get_transform(flip_x, flip_y, rotate), frame.duration) for frame in self.frames
                 ]
        return Animation(frames)

    def get_duration(self):
        return sum([ frame.duration for frame in self.frames if frame.duration is not None
                   ])

    def get_max_width(self):
        return max([ frame.image.width for frame in self.frames ])

    def get_max_height(self):
        return max([ frame.image.height for frame in self.frames ])

    @classmethod
    def from_image_sequence(cls, sequence, period, loop=True):
        frames = [ AnimationFrame(image, period) for image in sequence ]
        if not loop:
            frames[-1].duration = None
        return cls(frames)


class AnimationFrame(object):

    def __init__(self, image, duration):
        self.image = image
        self.duration = duration

    def __repr__(self):
        return 'AnimationFrame(%r, %r)' % (self.image, self.duration)


from pyglet.image import codecs as _codecs
_codecs.add_default_image_codecs()
# okay decompiling out\pyglet.image.pyc
