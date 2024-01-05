# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.font.win32
from ctypes import *
import ctypes, math
from sys import byteorder
import pyglet
from pyglet.font import base
import pyglet.image
from pyglet.libs.win32.constants import *
from pyglet.libs.win32.types import *
from pyglet.libs.win32 import _gdi32 as gdi32, _user32 as user32
from pyglet.libs.win32 import _kernel32 as kernel32
from pyglet.compat import asbytes
_debug_font = pyglet.options['debug_font']
HFONT = HANDLE
HBITMAP = HANDLE
HDC = HANDLE
HGDIOBJ = HANDLE
gdi32.CreateFontIndirectA.restype = HFONT
gdi32.CreateCompatibleBitmap.restype = HBITMAP
gdi32.CreateCompatibleDC.restype = HDC
user32.GetDC.restype = HDC
gdi32.GetStockObject.restype = HGDIOBJ
gdi32.CreateDIBSection.restype = HBITMAP

class LOGFONT(Structure):
    _fields_ = [
     (
      'lfHeight', c_long),
     (
      'lfWidth', c_long),
     (
      'lfEscapement', c_long),
     (
      'lfOrientation', c_long),
     (
      'lfWeight', c_long),
     (
      'lfItalic', c_byte),
     (
      'lfUnderline', c_byte),
     (
      'lfStrikeOut', c_byte),
     (
      'lfCharSet', c_byte),
     (
      'lfOutPrecision', c_byte),
     (
      'lfClipPrecision', c_byte),
     (
      'lfQuality', c_byte),
     (
      'lfPitchAndFamily', c_byte),
     (
      'lfFaceName', c_char * LF_FACESIZE)]
    __slots__ = [ f[0] for f in _fields_ ]


class TEXTMETRIC(Structure):
    _fields_ = [
     (
      'tmHeight', c_long),
     (
      'tmAscent', c_long),
     (
      'tmDescent', c_long),
     (
      'tmInternalLeading', c_long),
     (
      'tmExternalLeading', c_long),
     (
      'tmAveCharWidth', c_long),
     (
      'tmMaxCharWidth', c_long),
     (
      'tmWeight', c_long),
     (
      'tmOverhang', c_long),
     (
      'tmDigitizedAspectX', c_long),
     (
      'tmDigitizedAspectY', c_long),
     (
      'tmFirstChar', c_char),
     (
      'tmLastChar', c_char),
     (
      'tmDefaultChar', c_char),
     (
      'tmBreakChar', c_char),
     (
      'tmItalic', c_byte),
     (
      'tmUnderlined', c_byte),
     (
      'tmStruckOut', c_byte),
     (
      'tmPitchAndFamily', c_byte),
     (
      'tmCharSet', c_byte)]
    __slots__ = [ f[0] for f in _fields_ ]


class ABC(Structure):
    _fields_ = [
     (
      'abcA', c_int),
     (
      'abcB', c_uint),
     (
      'abcC', c_int)]
    __slots__ = [ f[0] for f in _fields_ ]


class BITMAPINFOHEADER(Structure):
    _fields_ = [
     (
      'biSize', c_uint32),
     (
      'biWidth', c_int),
     (
      'biHeight', c_int),
     (
      'biPlanes', c_short),
     (
      'biBitCount', c_short),
     (
      'biCompression', c_uint32),
     (
      'biSizeImage', c_uint32),
     (
      'biXPelsPerMeter', c_long),
     (
      'biYPelsPerMeter', c_long),
     (
      'biClrUsed', c_uint32),
     (
      'biClrImportant', c_uint32)]
    __slots__ = [ f[0] for f in _fields_ ]


class RGBQUAD(Structure):
    _fields_ = [
     (
      'rgbBlue', c_byte),
     (
      'rgbGreen', c_byte),
     (
      'rgbRed', c_byte),
     (
      'rgbReserved', c_byte)]

    def __init__(self, r, g, b):
        self.rgbRed = r
        self.rgbGreen = g
        self.rgbBlue = b


class BITMAPINFO(Structure):
    _fields_ = [
     (
      'bmiHeader', BITMAPINFOHEADER),
     (
      'bmiColors', c_ulong * 3)]


def str_ucs2(text):
    if byteorder == 'big':
        text = text.encode('utf_16_be')
    else:
        text = text.encode('utf_16_le')
    return create_string_buffer(text + '\x00')


_debug_dir = 'debug_font'

def _debug_filename(base, extension):
    import os
    if not os.path.exists(_debug_dir):
        os.makedirs(_debug_dir)
    name = '%s-%%d.%%s' % os.path.join(_debug_dir, base)
    num = 1
    while os.path.exists(name % (num, extension)):
        num += 1

    return name % (num, extension)


def _debug_image(image, name):
    filename = _debug_filename(name, 'png')
    image.save(filename)
    _debug('Saved image %r to %s' % (image, filename))


_debug_logfile = None

def _debug(msg):
    global _debug_logfile
    if not _debug_logfile:
        _debug_logfile = open(_debug_filename('log', 'txt'), 'wt')
    _debug_logfile.write(msg + '\n')


class Win32GlyphRenderer(base.GlyphRenderer):
    _bitmap = None
    _dc = None
    _bitmap_rect = None

    def __init__(self, font):
        super(Win32GlyphRenderer, self).__init__(font)
        self.font = font
        width = font.max_glyph_width
        height = font.ascent - font.descent
        width = (width | 3) + 1
        height = (height | 3) + 1
        self._create_bitmap(width, height)
        gdi32.SelectObject(self._dc, self.font.hfont)

    def _create_bitmap(self, width, height):
        pass

    def render(self, text):
        raise NotImplementedError('abstract')


class GDIGlyphRenderer(Win32GlyphRenderer):

    def __del__(self):
        try:
            if self._dc:
                gdi32.DeleteDC(self._dc)
            if self._bitmap:
                gdi32.DeleteObject(self._bitmap)
        except:
            pass

    def render(self, text):
        abc = ABC()
        if gdi32.GetCharABCWidthsW(self._dc, ord(text), ord(text), byref(abc)):
            width = abc.abcB
            lsb = abc.abcA
            advance = abc.abcA + abc.abcB + abc.abcC
        else:
            width_buf = c_int()
            gdi32.GetCharWidth32W(self._dc, ord(text), ord(text), byref(width_buf))
            width = width_buf.value
            lsb = 0
            advance = width
        height = self._bitmap_height
        image = self._get_image(text, width, height, lsb)
        glyph = self.font.create_glyph(image)
        glyph.set_bearings(-self.font.descent, lsb, advance)
        if _debug_font:
            _debug('%r.render(%s)' % (self, text))
            _debug('abc.abcA = %r' % abc.abcA)
            _debug('abc.abcB = %r' % abc.abcB)
            _debug('abc.abcC = %r' % abc.abcC)
            _debug('width = %r' % width)
            _debug('height = %r' % height)
            _debug('lsb = %r' % lsb)
            _debug('advance = %r' % advance)
            _debug_image(image, 'glyph_%s' % text)
            _debug_image(self.font.textures[0], 'tex_%s' % text)
        return glyph

    def _get_image(self, text, width, height, lsb):
        gdi32.SelectObject(self._dc, self._bitmap)
        gdi32.SelectObject(self._dc, self.font.hfont)
        gdi32.SetBkColor(self._dc, 0)
        gdi32.SetTextColor(self._dc, 16777215)
        gdi32.SetBkMode(self._dc, OPAQUE)
        user32.FillRect(self._dc, byref(self._bitmap_rect), self._black)
        gdi32.ExtTextOutA(self._dc, -lsb, 0, 0, c_void_p(), text, len(text), c_void_p())
        gdi32.GdiFlush()
        image = pyglet.image.ImageData(width, height, 'AXXX', self._bitmap_data, self._bitmap_rect.right * 4)
        return image

    def _create_bitmap(self, width, height):
        self._black = gdi32.GetStockObject(BLACK_BRUSH)
        self._white = gdi32.GetStockObject(WHITE_BRUSH)
        if self._dc:
            gdi32.ReleaseDC(self._dc)
        if self._bitmap:
            gdi32.DeleteObject(self._bitmap)
        pitch = width * 4
        data = POINTER(c_byte * (height * pitch))()
        info = BITMAPINFO()
        info.bmiHeader.biSize = sizeof(info.bmiHeader)
        info.bmiHeader.biWidth = width
        info.bmiHeader.biHeight = height
        info.bmiHeader.biPlanes = 1
        info.bmiHeader.biBitCount = 32
        info.bmiHeader.biCompression = BI_RGB
        self._dc = gdi32.CreateCompatibleDC(c_void_p())
        self._bitmap = gdi32.CreateDIBSection(c_void_p(), byref(info), DIB_RGB_COLORS, byref(data), c_void_p(), 0)
        kernel32.SetLastError(0)
        self._bitmap_data = data.contents
        self._bitmap_rect = RECT()
        self._bitmap_rect.left = 0
        self._bitmap_rect.right = width
        self._bitmap_rect.top = 0
        self._bitmap_rect.bottom = height
        self._bitmap_height = height
        if _debug_font:
            _debug('%r._create_dc(%d, %d)' % (self, width, height))
            _debug('_dc = %r' % self._dc)
            _debug('_bitmap = %r' % self._bitmap)
            _debug('pitch = %r' % pitch)
            _debug('info.bmiHeader.biSize = %r' % info.bmiHeader.biSize)


class Win32Font(base.Font):
    glyph_renderer_class = GDIGlyphRenderer

    def __init__(self, name, size, bold=False, italic=False, dpi=None):
        super(Win32Font, self).__init__()
        self.logfont = self.get_logfont(name, size, bold, italic, dpi)
        self.hfont = gdi32.CreateFontIndirectA(byref(self.logfont))
        dc = user32.GetDC(0)
        metrics = TEXTMETRIC()
        gdi32.SelectObject(dc, self.hfont)
        gdi32.GetTextMetricsA(dc, byref(metrics))
        self.ascent = metrics.tmAscent
        self.descent = -metrics.tmDescent
        self.max_glyph_width = metrics.tmMaxCharWidth

    @staticmethod
    def get_logfont(name, size, bold, italic, dpi):
        dc = user32.GetDC(0)
        if dpi is None:
            dpi = 96
        logpixelsy = dpi
        logfont = LOGFONT()
        logfont.lfHeight = int(-size * logpixelsy // 72)
        if bold:
            logfont.lfWeight = FW_BOLD
        else:
            logfont.lfWeight = FW_NORMAL
        logfont.lfItalic = italic
        logfont.lfFaceName = asbytes(name)
        logfont.lfQuality = ANTIALIASED_QUALITY
        return logfont

    @classmethod
    def have_font(cls, name):
        return True

    @classmethod
    def add_font_data(cls, data):
        numfonts = c_uint32()
        gdi32.AddFontMemResourceEx(data, len(data), 0, byref(numfonts))


from pyglet.image.codecs.gdiplus import PixelFormat32bppARGB, gdiplus, Rect
from pyglet.image.codecs.gdiplus import ImageLockModeRead, BitmapData
DriverStringOptionsCmapLookup = 1
DriverStringOptionsRealizedAdvance = 4
TextRenderingHintAntiAlias = 4
TextRenderingHintAntiAliasGridFit = 3
StringFormatFlagsDirectionRightToLeft = 1
StringFormatFlagsDirectionVertical = 2
StringFormatFlagsNoFitBlackBox = 4
StringFormatFlagsDisplayFormatControl = 32
StringFormatFlagsNoFontFallback = 1024
StringFormatFlagsMeasureTrailingSpaces = 2048
StringFormatFlagsNoWrap = 4096
StringFormatFlagsLineLimit = 8192
StringFormatFlagsNoClip = 16384

class Rectf(ctypes.Structure):
    _fields_ = [
     (
      'x', ctypes.c_float),
     (
      'y', ctypes.c_float),
     (
      'width', ctypes.c_float),
     (
      'height', ctypes.c_float)]


class GDIPlusGlyphRenderer(Win32GlyphRenderer):

    def _create_bitmap(self, width, height):
        self._data = (ctypes.c_byte * (4 * width * height))()
        self._bitmap = ctypes.c_void_p()
        self._format = PixelFormat32bppARGB
        gdiplus.GdipCreateBitmapFromScan0(width, height, width * 4, self._format, self._data, ctypes.byref(self._bitmap))
        self._graphics = ctypes.c_void_p()
        gdiplus.GdipGetImageGraphicsContext(self._bitmap, ctypes.byref(self._graphics))
        gdiplus.GdipSetPageUnit(self._graphics, UnitPixel)
        self._dc = user32.GetDC(0)
        gdi32.SelectObject(self._dc, self.font.hfont)
        gdiplus.GdipSetTextRenderingHint(self._graphics, TextRenderingHintAntiAliasGridFit)
        self._brush = ctypes.c_void_p()
        gdiplus.GdipCreateSolidFill(4294967295, ctypes.byref(self._brush))
        self._matrix = ctypes.c_void_p()
        gdiplus.GdipCreateMatrix(ctypes.byref(self._matrix))
        self._flags = DriverStringOptionsCmapLookup | DriverStringOptionsRealizedAdvance
        self._rect = Rect(0, 0, width, height)
        self._bitmap_height = height

    def render(self, text):
        ch = ctypes.create_unicode_buffer(text)
        len_ch = len(text)
        width = 10000
        height = self._bitmap_height
        rect = Rectf(0, self._bitmap_height - self.font.ascent + self.font.descent, width, height)
        generic = ctypes.c_void_p()
        gdiplus.GdipStringFormatGetGenericTypographic(ctypes.byref(generic))
        format = ctypes.c_void_p()
        gdiplus.GdipCloneStringFormat(generic, ctypes.byref(format))
        bbox = Rectf()
        flags = StringFormatFlagsMeasureTrailingSpaces | StringFormatFlagsNoClip | StringFormatFlagsNoFitBlackBox
        gdiplus.GdipSetStringFormatFlags(format, flags)
        gdiplus.GdipMeasureString(self._graphics, ch, len_ch, self.font._gdipfont, ctypes.byref(rect), format, ctypes.byref(bbox), 0, 0)
        lsb = 0
        advance = int(math.ceil(bbox.width))
        width = advance
        if self.font.italic:
            width += width // 2
        gdiplus.GdipGraphicsClear(self._graphics, 0)
        gdiplus.GdipDrawString(self._graphics, ch, len_ch, self.font._gdipfont, ctypes.byref(rect), format, self._brush)
        gdiplus.GdipFlush(self._graphics, 1)
        bitmap_data = BitmapData()
        gdiplus.GdipBitmapLockBits(self._bitmap, byref(self._rect), ImageLockModeRead, self._format, byref(bitmap_data))
        buffer = create_string_buffer(bitmap_data.Stride * bitmap_data.Height)
        memmove(buffer, bitmap_data.Scan0, len(buffer))
        gdiplus.GdipBitmapUnlockBits(self._bitmap, byref(bitmap_data))
        image = pyglet.image.ImageData(width, height, 'BGRA', buffer, -bitmap_data.Stride)
        glyph = self.font.create_glyph(image)
        glyph.set_bearings(-self.font.descent, lsb, advance)
        return glyph


FontStyleBold = 1
FontStyleItalic = 2
UnitPixel = 2
UnitPoint = 3

class GDIPlusFont(Win32Font):
    glyph_renderer_class = GDIPlusGlyphRenderer
    _private_fonts = None
    _default_name = 'Arial'

    def __init__(self, name, size, bold=False, italic=False, dpi=None):
        if not name:
            name = self._default_name
        super(GDIPlusFont, self).__init__(name, size, bold, italic, dpi)
        family = ctypes.c_void_p()
        name = ctypes.c_wchar_p(name)
        if self._private_fonts:
            gdiplus.GdipCreateFontFamilyFromName(name, self._private_fonts, ctypes.byref(family))
        if not family:
            gdiplus.GdipCreateFontFamilyFromName(name, None, ctypes.byref(family))
        if not family:
            name = self._default_name
            gdiplus.GdipCreateFontFamilyFromName(ctypes.c_wchar_p(name), None, ctypes.byref(family))
        if dpi is None:
            unit = UnitPoint
            self.dpi = 96
        else:
            unit = UnitPixel
            size = size * dpi // 72
            self.dpi = dpi
        style = 0
        if bold:
            style |= FontStyleBold
        if italic:
            style |= FontStyleItalic
        self.italic = italic
        self._gdipfont = ctypes.c_void_p()
        gdiplus.GdipCreateFont(family, ctypes.c_float(size), style, unit, ctypes.byref(self._gdipfont))
        return

    @classmethod
    def add_font_data(cls, data):
        super(GDIPlusFont, cls).add_font_data(data)
        if not cls._private_fonts:
            cls._private_fonts = ctypes.c_void_p()
            gdiplus.GdipNewPrivateFontCollection(ctypes.byref(cls._private_fonts))
        gdiplus.GdipPrivateAddMemoryFont(cls._private_fonts, data, len(data))
# okay decompiling out\pyglet.font.win32.pyc
