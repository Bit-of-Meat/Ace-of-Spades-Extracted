# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.s3tc
import ctypes, re
from pyglet.gl import *
from pyglet.gl import gl_info
from pyglet.image import AbstractImage, Texture
split_8byte = re.compile('........', flags=re.DOTALL)
split_16byte = re.compile('................', flags=re.DOTALL)

class PackedImageData(AbstractImage):
    _current_texture = None

    def __init__(self, width, height, format, packed_format, data):
        super(PackedImageData, self).__init__(width, height)
        self.format = format
        self.packed_format = packed_format
        self.data = data

    def unpack(self):
        if self.packed_format == GL_UNSIGNED_SHORT_5_6_5:
            i = 0
            out = (c_ubyte * (self.width * self.height * 3))()
            for c in self.data:
                out[i + 2] = (c & 31) << 3
                out[i + 1] = (c & 2016) >> 3
                out[i] = (c & 63488) >> 8
                i += 3

            self.data = out
            self.packed_format = GL_UNSIGNED_BYTE

    def _get_texture(self):
        if self._current_texture:
            return self._current_texture
        texture = Texture.create_for_size(GL_TEXTURE_2D, self.width, self.height)
        glBindTexture(texture.target, texture.id)
        glTexParameteri(texture.target, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        if not gl_info.have_version(1, 2) or True:
            self.unpack()
        glTexImage2D(texture.target, texture.level, self.format, self.width, self.height, 0, self.format, self.packed_format, self.data)
        self._current_texture = texture
        return texture

    texture = property(_get_texture)


def decode_dxt1_rgb(data, width, height):
    out = (ctypes.c_uint16 * (width * height))()
    image_offset = 0
    for c0_lo, c0_hi, c1_lo, c1_hi, b0, b1, b2, b3 in split_8byte.findall(data):
        color0 = ord(c0_lo) | ord(c0_hi) << 8
        color1 = ord(c1_lo) | ord(c1_hi) << 8
        bits = ord(b0) | ord(b1) << 8 | ord(b2) << 16 | ord(b3) << 24
        r0 = color0 & 31
        g0 = (color0 & 2016) >> 5
        b0 = (color0 & 63488) >> 11
        r1 = color1 & 31
        g1 = (color1 & 2016) >> 5
        b1 = (color1 & 63488) >> 11
        i = image_offset
        for y in range(4):
            for x in range(4):
                code = bits & 3
                if code == 0:
                    out[i] = color0
                elif code == 1:
                    out[i] = color1
                elif code == 3 and color0 <= color1:
                    out[i] = 0
                else:
                    if code == 2 and color0 > color1:
                        r = (2 * r0 + r1) / 3
                        g = (2 * g0 + g1) / 3
                        b = (2 * b0 + b1) / 3
                    elif code == 3 and color0 > color1:
                        r = (r0 + 2 * r1) / 3
                        g = (g0 + 2 * g1) / 3
                        b = (b0 + 2 * b1) / 3
                    else:
                        r = (r0 + r1) / 2
                        g = (g0 + g1) / 2
                        b = (b0 + b1) / 2
                    out[i] = r | g << 5 | b << 11
                bits >>= 2
                i += 1

            i += width - 4

        advance_row = (image_offset + 4) % width == 0
        image_offset += width * 3 * advance_row + 4

    return PackedImageData(width, height, GL_RGB, GL_UNSIGNED_SHORT_5_6_5, out)


def decode_dxt1_rgba(data, width, height):
    out = (ctypes.c_ubyte * (width * height * 4))()
    pitch = width << 2
    image_offset = 0
    for c0_lo, c0_hi, c1_lo, c1_hi, b0, b1, b2, b3 in split_8byte.findall(data):
        color0 = ord(c0_lo) | ord(c0_hi) << 8
        color1 = ord(c1_lo) | ord(c1_hi) << 8
        bits = ord(b0) | ord(b1) << 8 | ord(b2) << 16 | ord(b3) << 24
        r0 = color0 & 31
        g0 = (color0 & 2016) >> 5
        b0 = (color0 & 63488) >> 11
        r1 = color1 & 31
        g1 = (color1 & 2016) >> 5
        b1 = (color1 & 63488) >> 11
        i = image_offset
        for y in range(4):
            for x in range(4):
                code = bits & 3
                a = 255
                if code == 0:
                    r, g, b = r0, g0, b0
                elif code == 1:
                    r, g, b = r1, g1, b1
                elif code == 3 and color0 <= color1:
                    r = g = b = a = 0
                elif code == 2 and color0 > color1:
                    r = (2 * r0 + r1) / 3
                    g = (2 * g0 + g1) / 3
                    b = (2 * b0 + b1) / 3
                elif code == 3 and color0 > color1:
                    r = (r0 + 2 * r1) / 3
                    g = (g0 + 2 * g1) / 3
                    b = (b0 + 2 * b1) / 3
                else:
                    r = (r0 + r1) / 2
                    g = (g0 + g1) / 2
                    b = (b0 + b1) / 2
                out[i] = b << 3
                out[i + 1] = g << 2
                out[i + 2] = r << 3
                out[i + 3] = a << 4
                bits >>= 2
                i += 4

            i += pitch - 16

        advance_row = (image_offset + 16) % pitch == 0
        image_offset += pitch * 3 * advance_row + 16

    return PackedImageData(width, height, GL_RGBA, GL_UNSIGNED_BYTE, out)


def decode_dxt3(data, width, height):
    out = (ctypes.c_ubyte * (width * height * 4))()
    pitch = width << 2
    image_offset = 0
    for a0, a1, a2, a3, a4, a5, a6, a7, c0_lo, c0_hi, c1_lo, c1_hi, b0, b1, b2, b3 in split_16byte.findall(data):
        color0 = ord(c0_lo) | ord(c0_hi) << 8
        color1 = ord(c1_lo) | ord(c1_hi) << 8
        bits = ord(b0) | ord(b1) << 8 | ord(b2) << 16 | ord(b3) << 24
        alpha = ord(a0) | ord(a1) << 8 | ord(a2) << 16 | ord(a3) << 24 | ord(a4) << 32 | ord(a5) << 40 | ord(a6) << 48 | ord(a7) << 56
        r0 = color0 & 31
        g0 = (color0 & 2016) >> 5
        b0 = (color0 & 63488) >> 11
        r1 = color1 & 31
        g1 = (color1 & 2016) >> 5
        b1 = (color1 & 63488) >> 11
        i = image_offset
        for y in range(4):
            for x in range(4):
                code = bits & 3
                a = alpha & 15
                if code == 0:
                    r, g, b = r0, g0, b0
                elif code == 1:
                    r, g, b = r1, g1, b1
                elif code == 3 and color0 <= color1:
                    r = g = b = 0
                elif code == 2 and color0 > color1:
                    r = (2 * r0 + r1) / 3
                    g = (2 * g0 + g1) / 3
                    b = (2 * b0 + b1) / 3
                elif code == 3 and color0 > color1:
                    r = (r0 + 2 * r1) / 3
                    g = (g0 + 2 * g1) / 3
                    b = (b0 + 2 * b1) / 3
                else:
                    r = (r0 + r1) / 2
                    g = (g0 + g1) / 2
                    b = (b0 + b1) / 2
                out[i] = b << 3
                out[i + 1] = g << 2
                out[i + 2] = r << 3
                out[i + 3] = a << 4
                bits >>= 2
                alpha >>= 4
                i += 4

            i += pitch - 16

        advance_row = (image_offset + 16) % pitch == 0
        image_offset += pitch * 3 * advance_row + 16

    return PackedImageData(width, height, GL_RGBA, GL_UNSIGNED_BYTE, out)


def decode_dxt5(data, width, height):
    out = (ctypes.c_ubyte * (width * height * 4))()
    pitch = width << 2
    image_offset = 0
    for alpha0, alpha1, ab0, ab1, ab2, ab3, ab4, ab5, c0_lo, c0_hi, c1_lo, c1_hi, b0, b1, b2, b3 in split_16byte.findall(data):
        color0 = ord(c0_lo) | ord(c0_hi) << 8
        color1 = ord(c1_lo) | ord(c1_hi) << 8
        alpha0 = ord(alpha0)
        alpha1 = ord(alpha1)
        bits = ord(b0) | ord(b1) << 8 | ord(b2) << 16 | ord(b3) << 24
        abits = ord(ab0) | ord(ab1) << 8 | ord(ab2) << 16 | ord(ab3) << 24 | ord(ab4) << 32 | ord(ab5) << 40
        r0 = color0 & 31
        g0 = (color0 & 2016) >> 5
        b0 = (color0 & 63488) >> 11
        r1 = color1 & 31
        g1 = (color1 & 2016) >> 5
        b1 = (color1 & 63488) >> 11
        i = image_offset
        for y in range(4):
            for x in range(4):
                code = bits & 3
                acode = abits & 7
                if code == 0:
                    r, g, b = r0, g0, b0
                elif code == 1:
                    r, g, b = r1, g1, b1
                elif code == 3 and color0 <= color1:
                    r = g = b = 0
                elif code == 2 and color0 > color1:
                    r = (2 * r0 + r1) / 3
                    g = (2 * g0 + g1) / 3
                    b = (2 * b0 + b1) / 3
                elif code == 3 and color0 > color1:
                    r = (r0 + 2 * r1) / 3
                    g = (g0 + 2 * g1) / 3
                    b = (b0 + 2 * b1) / 3
                else:
                    r = (r0 + r1) / 2
                    g = (g0 + g1) / 2
                    b = (b0 + b1) / 2
                if acode == 0:
                    a = alpha0
                elif acode == 1:
                    a = alpha1
                elif alpha0 > alpha1:
                    if acode == 2:
                        a = (6 * alpha0 + 1 * alpha1) / 7
                    elif acode == 3:
                        a = (5 * alpha0 + 2 * alpha1) / 7
                    elif acode == 4:
                        a = (4 * alpha0 + 3 * alpha1) / 7
                    elif acode == 5:
                        a = (3 * alpha0 + 4 * alpha1) / 7
                    else:
                        if acode == 6:
                            a = (2 * alpha0 + 5 * alpha1) / 7
                        else:
                            a = (1 * alpha0 + 6 * alpha1) / 7
                elif acode == 2:
                    a = (4 * alpha0 + 1 * alpha1) / 5
                elif acode == 3:
                    a = (3 * alpha0 + 2 * alpha1) / 5
                elif acode == 4:
                    a = (2 * alpha0 + 3 * alpha1) / 5
                elif acode == 5:
                    a = (1 * alpha0 + 4 * alpha1) / 5
                elif acode == 6:
                    a = 0
                else:
                    a = 255
                out[i] = b << 3
                out[i + 1] = g << 2
                out[i + 2] = r << 3
                out[i + 3] = a
                bits >>= 2
                abits >>= 3
                i += 4

            i += pitch - 16

        advance_row = (image_offset + 16) % pitch == 0
        image_offset += pitch * 3 * advance_row + 16

    return PackedImageData(width, height, GL_RGBA, GL_UNSIGNED_BYTE, out)
# okay decompiling out\pyglet.image.codecs.s3tc.pyc
