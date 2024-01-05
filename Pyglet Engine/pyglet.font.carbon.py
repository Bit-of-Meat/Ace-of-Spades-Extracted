# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.font.carbon
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from ..ctypes import *
import math
from sys import byteorder
from pyglet.font import base
import pyglet.image
from ..pyglet.libs.darwin import *
from pyglet.libs.darwin import _oscheck

class FixedPoint(Structure):
    _fields_ = [
     (
      'x', Fixed),
     (
      'y', Fixed)]


class ATSTrapezoid(Structure):
    _fields_ = [
     (
      'upperLeft', FixedPoint),
     (
      'upperRight', FixedPoint),
     (
      'lowerRight', FixedPoint),
     (
      'lowerLeft', FixedPoint)]


CGGlyph = c_ushort
ATSUFontID = c_uint32
RGBColor = c_short * 3
ATSURGBAlphaColor = c_float * 4
kCGImageAlphaNone = 0
kCGImageAlphaPremultipliedLast = 1
kCGTextFill = 0
kATSUInvalidFontErr = -8796
kATSFontContextUnspecified = 0
kATSFontContextGlobal = 1
kATSFontContextLocal = 2
kATSFontFilterSelectorUnspecified = 0
kATSFontFilterSelectorGeneration = 3
kATSFontFilterSelectorFontFamily = 7
kATSFontFilterSelectorFontFamilyApplierFunction = 8
kATSFontFilterSelectorFontApplierFunction = 9
kATSOptionFlagsDoNotNotify = 256
kATSOptionFlagsIterationScopeMask = 28672
kATSOptionFlagsDefaultScope = 0
kATSOptionFlagsUnRestrictedScope = 4096
kATSOptionFlagsRestrictedScope = 8192
kATSOptionFlagsProcessSubdirectories = 64
kATSUFromTextBeginning = c_ulong(4294967295)
kATSUToTextEnd = c_ulong(4294967295)
kATSULineAscentTag = 8
kATSULineDescentTag = 9
ATSUTextMeasurement = Fixed
kATSUQDBoldfaceTag = 256
kATSUQDItalicTag = 257
kATSUFontTag = 261
kATSUSizeTag = 262
kATSUCGContextTag = 32767
kATSUColorTag = 263
kATSURGBAlphaColorTag = 288
kATSULineWidthTag = 1
kFontFullName = 4
kFontNoPlatformCode = c_ulong(-1)
kFontNoScriptCode = c_ulong(-1)
kFontNoLanguageCode = c_ulong(-1)
kATSUseDeviceOrigins = 1
kATSFontFormatUnspecified = 0
kATSFontContextLocal = 2
carbon.CGColorSpaceCreateWithName.restype = c_void_p
carbon.CGBitmapContextCreate.restype = POINTER(c_void_p)
UniCharArrayOffset = c_uint32
UniCharCount = c_uint32
kATSULayoutOperationJustification = 1
kATSULayoutOperationPostLayoutAdjustment = 32
kATSULayoutOperationCallbackStatusHandled = 0
kATSULayoutOperationCallbackStatusContinue = c_long(1)
kATSULayoutOperationOverrideTag = 15
kATSUDirectDataAdvanceDeltaFixedArray = 0
kATSUDirectDataDeviceDeltaSInt16Array = 2
kATSUDirectDataLayoutRecordATSLayoutRecordVersion1 = 100
ATSUDirectLayoutOperationOverrideUPP = CFUNCTYPE(c_int, c_int, c_void_p, c_uint32, c_void_p, POINTER(c_int))

class ATSULayoutOperationOverrideSpecifier(Structure):
    _fields_ = [
     (
      'operationSelector', c_uint32),
     (
      'overrideUPP', ATSUDirectLayoutOperationOverrideUPP)]


class ATSLayoutRecord(Structure):
    _pack_ = 2
    _fields_ = [
     (
      'glyphID', c_uint16),
     (
      'flags', c_uint32),
     (
      'originalOffset', c_uint32),
     (
      'realPos', Fixed)]


def fixed(value):
    return c_int32(carbon.Long2Fix(c_long(int(value))))


carbon.Fix2X.restype = c_double

def fix2float(value):
    return carbon.Fix2X(value)


def create_atsu_style(attributes):
    tags, values = zip(*attributes.items())
    tags = (c_int * len(tags))(*tags)
    sizes = (c_uint * len(values))(*[ sizeof(v) for v in values ])
    values = (c_void_p * len(values))(*[ cast(pointer(v), c_void_p) for v in values
                                       ])
    style = c_void_p()
    carbon.ATSUCreateStyle(byref(style))
    carbon.ATSUSetAttributes(style, len(tags), tags, sizes, values)
    return style


def set_layout_attributes(layout, attributes):
    if attributes:
        tags, values = zip(*attributes.items())
        tags = (c_int * len(tags))(*tags)
        sizes = (c_uint * len(values))(*[ sizeof(v) for v in values ])
        values = (c_void_p * len(values))(*[ cast(pointer(v), c_void_p) for v in values
                                           ])
        r = carbon.ATSUSetLayoutControls(layout, len(tags), tags, sizes, values)
        _oscheck(r)


def str_ucs2(text):
    if byteorder == 'big':
        text = text.encode('utf_16_be')
    else:
        text = text.encode('utf_16_le')
    return create_string_buffer(text + '\x00')


class CarbonGlyphRenderer(base.GlyphRenderer):
    _bitmap = None
    _bitmap_context = None
    _bitmap_rect = None
    _glyph_advance = 0

    def __init__(self, font):
        super(CarbonGlyphRenderer, self).__init__(font)
        self._create_bitmap_context(256, 256)
        self.font = font

    def __del__(self):
        try:
            if self._bitmap_context:
                carbon.CGContextRelease(self._bitmap_context)
        except:
            pass

    def _layout_callback(self, operation, line, ref, extra, callback_status):
        if not line:
            return 0
        records = c_void_p()
        n_records = c_uint()
        r = carbon.ATSUDirectGetLayoutDataArrayPtrFromLineRef(line, kATSUDirectDataLayoutRecordATSLayoutRecordVersion1, 0, byref(records), byref(n_records))
        _oscheck(r)
        records = cast(records, POINTER(ATSLayoutRecord * n_records.value)).contents
        self._glyph_advance = fix2float(records[-1].realPos)
        callback_status.contents = kATSULayoutOperationCallbackStatusContinue
        return 0

    def render(self, text):
        text_len = len(text)
        text_ucs2 = str_ucs2(text)
        override_spec = ATSULayoutOperationOverrideSpecifier()
        override_spec.operationSelector = kATSULayoutOperationPostLayoutAdjustment
        override_spec.overrideUPP = ATSUDirectLayoutOperationOverrideUPP(self._layout_callback)
        layout = c_void_p()
        carbon.ATSUCreateTextLayout(byref(layout))
        set_layout_attributes(layout, {kATSUCGContextTag: self._bitmap_context, 
           kATSULayoutOperationOverrideTag: override_spec})
        carbon.ATSUSetTextPointerLocation(layout, text_ucs2, kATSUFromTextBeginning, kATSUToTextEnd, text_len)
        carbon.ATSUSetRunStyle(layout, self.font.atsu_style, kATSUFromTextBeginning, kATSUToTextEnd)
        carbon.ATSUSetTransientFontMatching(layout, True)
        rect = Rect()
        carbon.ATSUMeasureTextImage(layout, kATSUFromTextBeginning, kATSUToTextEnd, 0, 0, byref(rect))
        image_width = rect.right - rect.left + 2
        image_height = rect.bottom - rect.top + 2
        baseline = rect.bottom + 1
        lsb = rect.left
        if image_width > self._bitmap_rect.size.width or image_height > self._bitmap_rect.size.height:
            self._create_bitmap_context(int(max(image_width, self._bitmap_rect.size.width)), int(max(image_height, self._bitmap_rect.size.height)))
            set_layout_attributes(layout, {kATSUCGContextTag: self._bitmap_context})
        carbon.CGContextClearRect(self._bitmap_context, self._bitmap_rect)
        carbon.ATSUDrawText(layout, 0, kATSUToTextEnd, fixed(-lsb + 1), fixed(baseline))
        advance = self._glyph_advance
        advance = int(round(advance))
        if text == '\u200b':
            advance = 0
        pitch = int(4 * self._bitmap_rect.size.width)
        image = pyglet.image.ImageData(image_width, self._bitmap_rect.size.height, 'RGBA', self._bitmap, pitch)
        skip_rows = int(self._bitmap_rect.size.height - image_height)
        image = image.get_region(0, skip_rows, image.width, image_height)
        glyph = self.font.create_glyph(image)
        glyph.set_bearings(baseline, lsb - 1, int(advance))
        t = list(glyph.tex_coords)
        glyph.tex_coords = t[9:12] + t[6:9] + t[3:6] + t[:3]
        return glyph

    def _create_bitmap_context(self, width, height):
        if self._bitmap_context:
            carbon.CGContextRelease(self._bitmap_context)
        components = 4
        pitch = width * components
        self._bitmap = (c_ubyte * (pitch * height))()
        color_space = carbon.CGColorSpaceCreateDeviceRGB()
        context = carbon.CGBitmapContextCreate(self._bitmap, width, height, 8, pitch, color_space, kCGImageAlphaPremultipliedLast)
        carbon.CGColorSpaceRelease(color_space)
        carbon.CGContextSetShouldSmoothFonts(context, False)
        carbon.CGContextSetShouldAntialias(context, True)
        self._bitmap_context = context
        self._bitmap_rect = CGRect()
        self._bitmap_rect.origin.x = 0
        self._bitmap_rect.origin.y = 0
        self._bitmap_rect.size.width = width
        self._bitmap_rect.size.height = height


class CarbonFont(base.Font):
    glyph_renderer_class = CarbonGlyphRenderer

    def __init__(self, name, size, bold=False, italic=False, dpi=None):
        super(CarbonFont, self).__init__()
        if not name:
            name = 'Helvetica'
        if dpi is None:
            dpi = 96
        size = size * dpi / 72.0
        name = name.encode('ascii', 'ignore')
        font_id = ATSUFontID()
        carbon.ATSUFindFontFromName(name, len(name), kFontFullName, kFontNoPlatformCode, kFontNoScriptCode, kFontNoLanguageCode, byref(font_id))
        attributes = {kATSUSizeTag: fixed(size), 
           kATSUFontTag: font_id, 
           kATSURGBAlphaColorTag: ATSURGBAlphaColor(1, 1, 1, 1), 
           kATSUQDBoldfaceTag: c_byte(bold), 
           kATSUQDItalicTag: c_byte(italic)}
        self.atsu_style = create_atsu_style(attributes)
        self.calculate_metrics()
        return

    @classmethod
    def have_font(cls, name):
        font_id = ATSUFontID()
        name = name.encode('ascii', 'ignore')
        r = carbon.ATSUFindFontFromName(name, len(name), kFontFullName, kFontNoPlatformCode, kFontNoScriptCode, kFontNoLanguageCode, byref(font_id))
        return r != kATSUInvalidFontErr

    def calculate_metrics(self):
        text = '\x00a'
        layout = c_void_p()
        carbon.ATSUCreateTextLayout(byref(layout))
        carbon.ATSUSetTextPointerLocation(layout, text, kATSUFromTextBeginning, kATSUToTextEnd, 1)
        carbon.ATSUSetRunStyle(layout, self.atsu_style, kATSUFromTextBeginning, kATSUToTextEnd)
        carbon.ATSUSetTransientFontMatching(layout, False)
        value = ATSUTextMeasurement()
        carbon.ATSUGetLineControl(layout, 0, kATSULineAscentTag, sizeof(value), byref(value), None)
        self.ascent = int(math.ceil(fix2float(value)))
        carbon.ATSUGetLineControl(layout, 0, kATSULineDescentTag, sizeof(value), byref(value), None)
        self.descent = -int(math.ceil(fix2float(value)))
        return

    @classmethod
    def add_font_data(cls, data):
        container = c_void_p()
        r = carbon.ATSFontActivateFromMemory(data, len(data), kATSFontContextLocal, kATSFontFormatUnspecified, None, 0, byref(container))
        _oscheck(r)
        return
# okay decompiling out\pyglet.font.carbon.pyc
