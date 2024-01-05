# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.bmp
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from pyglet.image import ImageData
from pyglet.image.codecs import ImageDecoder, ImageDecodeException
BYTE = ctypes.c_ubyte
WORD = ctypes.c_uint16
DWORD = ctypes.c_uint32
LONG = ctypes.c_int32
FXPT2DOT30 = ctypes.c_uint32
BI_RGB = 0
BI_RLE8 = 1
BI_RLE4 = 2
BI_BITFIELDS = 3

class BITMAPFILEHEADER(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
     (
      'bfType', WORD),
     (
      'bfSize', DWORD),
     (
      'bfReserved1', WORD),
     (
      'bfReserved2', WORD),
     (
      'bfOffBits', DWORD)]


class BITMAPINFOHEADER(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
     (
      'biSize', DWORD),
     (
      'biWidth', LONG),
     (
      'biHeight', LONG),
     (
      'biPlanes', WORD),
     (
      'biBitCount', WORD),
     (
      'biCompression', DWORD),
     (
      'biSizeImage', DWORD),
     (
      'biXPelsPerMeter', LONG),
     (
      'biYPelsPerMeter', LONG),
     (
      'biClrUsed', DWORD),
     (
      'biClrImportant', DWORD)]


CIEXYZTRIPLE = FXPT2DOT30 * 9

class BITMAPV4HEADER(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
     (
      'biSize', DWORD),
     (
      'biWidth', LONG),
     (
      'biHeight', LONG),
     (
      'biPlanes', WORD),
     (
      'biBitCount', WORD),
     (
      'biCompression', DWORD),
     (
      'biSizeImage', DWORD),
     (
      'biXPelsPerMeter', LONG),
     (
      'biYPelsPerMeter', LONG),
     (
      'biClrUsed', DWORD),
     (
      'biClrImportant', DWORD),
     (
      'bV4RedMask', DWORD),
     (
      'bV4GreenMask', DWORD),
     (
      'bV4BlueMask', DWORD),
     (
      'bV4AlphaMask', DWORD),
     (
      'bV4CSType', DWORD),
     (
      'bV4Endpoints', CIEXYZTRIPLE),
     (
      'bV4GammaRed', DWORD),
     (
      'bV4GammaGreen', DWORD),
     (
      'bV4GammaBlue', DWORD)]


class RGBFields(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
     (
      'red', DWORD),
     (
      'green', DWORD),
     (
      'blue', DWORD)]


class RGBQUAD(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
     (
      'rgbBlue', BYTE),
     (
      'rgbGreen', BYTE),
     (
      'rgbRed', BYTE),
     (
      'rgbReserved', BYTE)]

    def __repr__(self):
        return '<%d, %d, %d>' % (self.rgbRed, self.rgbGreen, self.rgbBlue)


def ptr_add(ptr, offset):
    address = ctypes.addressof(ptr.contents) + offset
    return ctypes.pointer(type(ptr.contents).from_address(address))


def to_ctypes(buffer, offset, type):
    if offset + ctypes.sizeof(type) > len(buffer):
        raise ImageDecodeException('BMP file is truncated')
    ptr = ptr_add(ctypes.pointer(buffer), offset)
    return ctypes.cast(ptr, ctypes.POINTER(type)).contents


class BMPImageDecoder(ImageDecoder):

    def get_file_extensions(self):
        return [
         '.bmp']

    def decode(self, file, filename):
        if not file:
            file = open(filename, 'rb')
        bytes = file.read()
        buffer = ctypes.c_buffer(bytes)
        if bytes[:2] != 'BM':
            raise ImageDecodeException('Not a Windows bitmap file: %r' % (filename or file))
        file_header = to_ctypes(buffer, 0, BITMAPFILEHEADER)
        bits_offset = file_header.bfOffBits
        info_header_offset = ctypes.sizeof(BITMAPFILEHEADER)
        info_header = to_ctypes(buffer, info_header_offset, BITMAPINFOHEADER)
        palette_offset = info_header_offset + info_header.biSize
        if info_header.biSize < ctypes.sizeof(BITMAPINFOHEADER):
            raise ImageDecodeException('Unsupported BMP type: %r' % (filename or file))
        width = info_header.biWidth
        height = info_header.biHeight
        if width <= 0 or info_header.biPlanes != 1:
            raise ImageDecodeException('BMP file has corrupt parameters: %r' % (filename or file))
        pitch_sign = height < 0 and -1 or 1
        height = abs(height)
        compression = info_header.biCompression
        if compression not in (BI_RGB, BI_BITFIELDS):
            raise ImageDecodeException('Unsupported compression: %r' % (filename or file))
        clr_used = 0
        bitcount = info_header.biBitCount
        if bitcount == 1:
            pitch = (width + 7) // 8
            bits_type = ctypes.c_ubyte
            decoder = decode_1bit
        elif bitcount == 4:
            pitch = (width + 1) // 2
            bits_type = ctypes.c_ubyte
            decoder = decode_4bit
        elif bitcount == 8:
            bits_type = ctypes.c_ubyte
            pitch = width
            decoder = decode_8bit
        elif bitcount == 16:
            pitch = width * 2
            bits_type = ctypes.c_uint16
            decoder = decode_bitfields
        elif bitcount == 24:
            pitch = width * 3
            bits_type = ctypes.c_ubyte
            decoder = decode_24bit
        elif bitcount == 32:
            pitch = width * 4
            if compression == BI_RGB:
                decoder = decode_32bit_rgb
                bits_type = ctypes.c_ubyte
            else:
                if compression == BI_BITFIELDS:
                    decoder = decode_bitfields
                    bits_type = ctypes.c_uint32
                else:
                    raise ImageDecodeException('Unsupported compression: %r' % (filename or file))
        else:
            raise ImageDecodeException('Unsupported bit count %d: %r' % (bitcount, filename or file))
        pitch = pitch + 3 & -4
        packed_width = pitch // ctypes.sizeof(bits_type)
        if bitcount < 16 and compression == BI_RGB:
            clr_used = info_header.biClrUsed or 1 << bitcount
            palette = to_ctypes(buffer, palette_offset, RGBQUAD * clr_used)
            bits = to_ctypes(buffer, bits_offset, bits_type * packed_width * height)
            return decoder(bits, palette, width, height, pitch, pitch_sign)
        else:
            if bitcount >= 16 and compression == BI_RGB:
                bits = to_ctypes(buffer, bits_offset, bits_type * (packed_width * height))
                return decoder(bits, None, width, height, pitch, pitch_sign)
            if compression == BI_BITFIELDS:
                if info_header.biSize >= ctypes.sizeof(BITMAPV4HEADER):
                    info_header = to_ctypes(buffer, info_header_offset, BITMAPV4HEADER)
                    r_mask = info_header.bV4RedMask
                    g_mask = info_header.bV4GreenMask
                    b_mask = info_header.bV4BlueMask
                else:
                    fields_offset = info_header_offset + ctypes.sizeof(BITMAPINFOHEADER)
                    fields = to_ctypes(buffer, fields_offset, RGBFields)
                    r_mask = fields.red
                    g_mask = fields.green
                    b_mask = fields.blue

                class _BitsArray(ctypes.LittleEndianStructure):
                    _pack_ = 1
                    _fields_ = [
                     (
                      'data', bits_type * packed_width * height)]

                bits = to_ctypes(buffer, bits_offset, _BitsArray).data
                return decoder(bits, r_mask, g_mask, b_mask, width, height, pitch, pitch_sign)
            return


def decode_1bit(bits, palette, width, height, pitch, pitch_sign):
    rgb_pitch = ((pitch << 3) + 7 & -8) * 3
    buffer = (ctypes.c_ubyte * (height * rgb_pitch))()
    i = 0
    for row in bits:
        for packed in row:
            for _ in range(8):
                rgb = palette[(packed & 128) >> 7]
                buffer[i] = rgb.rgbRed
                buffer[i + 1] = rgb.rgbGreen
                buffer[i + 2] = rgb.rgbBlue
                i += 3
                packed <<= 1

    return ImageData(width, height, 'RGB', buffer, pitch_sign * rgb_pitch)


def decode_4bit(bits, palette, width, height, pitch, pitch_sign):
    rgb_pitch = ((pitch << 1) + 1 & -2) * 3
    buffer = (ctypes.c_ubyte * (height * rgb_pitch))()
    i = 0
    for row in bits:
        for packed in row:
            for index in ((packed & 240) >> 4, packed & 15):
                rgb = palette[index]
                buffer[i] = rgb.rgbRed
                buffer[i + 1] = rgb.rgbGreen
                buffer[i + 2] = rgb.rgbBlue
                i += 3

    return ImageData(width, height, 'RGB', buffer, pitch_sign * rgb_pitch)


def decode_8bit(bits, palette, width, height, pitch, pitch_sign):
    rgb_pitch = pitch * 3
    buffer = (ctypes.c_ubyte * (height * rgb_pitch))()
    i = 0
    for row in bits:
        for index in row:
            rgb = palette[index]
            buffer[i] = rgb.rgbRed
            buffer[i + 1] = rgb.rgbGreen
            buffer[i + 2] = rgb.rgbBlue
            i += 3

    return ImageData(width, height, 'RGB', buffer, pitch_sign * rgb_pitch)


def decode_24bit(bits, palette, width, height, pitch, pitch_sign):
    buffer = (ctypes.c_ubyte * (height * pitch))()
    ctypes.memmove(buffer, bits, len(buffer))
    return ImageData(width, height, 'BGR', buffer, pitch_sign * pitch)


def decode_32bit_rgb(bits, palette, width, height, pitch, pitch_sign):
    buffer = (ctypes.c_ubyte * (height * pitch))()
    ctypes.memmove(buffer, bits, len(buffer))
    return ImageData(width, height, 'BGRA', buffer, pitch_sign * pitch)


def get_shift(mask):
    if not mask:
        return 0
    else:
        shift = 0
        while not 1 << shift & mask:
            shift += 1

        shift_up = 0
        while mask >> shift >> shift_up:
            shift_up += 1

        s = shift - (8 - shift_up)
        if s < 0:
            return (0, -s)
        return (s, 0)


def decode_bitfields(bits, r_mask, g_mask, b_mask, width, height, pitch, pitch_sign):
    r_shift1, r_shift2 = get_shift(r_mask)
    g_shift1, g_shift2 = get_shift(g_mask)
    b_shift1, b_shift2 = get_shift(b_mask)
    rgb_pitch = 3 * len(bits[0])
    buffer = (ctypes.c_ubyte * (height * rgb_pitch))()
    i = 0
    for row in bits:
        for packed in row:
            buffer[i] = (packed & r_mask) >> r_shift1 << r_shift2
            buffer[i + 1] = (packed & g_mask) >> g_shift1 << g_shift2
            buffer[i + 2] = (packed & b_mask) >> b_shift1 << b_shift2
            i += 3

    return ImageData(width, height, 'RGB', buffer, pitch_sign * rgb_pitch)


def get_decoders():
    return [
     BMPImageDecoder()]


def get_encoders():
    return []
# okay decompiling out\pyglet.image.codecs.bmp.pyc
