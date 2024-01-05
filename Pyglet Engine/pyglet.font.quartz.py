# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.font.quartz
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import math
from ..ctypes import *
from ctypes import util
from pyglet.font import base
import pyglet.image
cf = cdll.LoadLibrary(util.find_library('CoreFoundation'))
quartz = cdll.LoadLibrary(util.find_library('quartz'))
ct = cdll.LoadLibrary(util.find_library('CoreText'))
CFIndex = c_long
UniChar = c_ushort
CGGlyph = c_ushort
import sys
if sys.maxint > 4294967296:
    CGFloat = c_double
else:
    CGFloat = c_float

class CFRange(Structure):
    _fields_ = [
     (
      'location', CFIndex), ('length', CFIndex)]


class CGPoint(Structure):
    _fields_ = [
     (
      'x', CGFloat), ('y', CGFloat)]


class CGSize(Structure):
    _fields_ = [
     (
      'width', CGFloat), ('height', CGFloat)]


class CGRect(Structure):
    _fields_ = [
     (
      'origin', CGPoint), ('size', CGSize)]


cf.CFDictionaryCreateMutable.restype = c_void_p
cf.CFStringCreateWithCString.restype = c_void_p
cf.CFAttributedStringCreate.restype = c_void_p
cf.CFDataCreate.restype = c_void_p
cf.CFNumberCreate.restype = c_void_p
ct.CTLineCreateWithAttributedString.restype = c_void_p
ct.CTFontGetBoundingRectsForGlyphs.restype = CGRect
ct.CTFontGetAdvancesForGlyphs.restype = c_double
ct.CTFontGetAscent.restype = CGFloat
ct.CTFontGetDescent.restype = CGFloat
ct.CTFontCreateWithGraphicsFont.restype = c_void_p
ct.CTFontCreateWithGraphicsFont.argtypes = [c_void_p, CGFloat, c_void_p, c_void_p]
ct.CTFontCopyFamilyName.restype = c_void_p
ct.CTFontCopyFullName.restype = c_void_p
ct.CTFontDescriptorCreateWithAttributes.restype = c_void_p
ct.CTFontCreateWithFontDescriptor.restype = c_void_p
ct.CTFontCreateWithFontDescriptor.argtypes = [c_void_p, CGFloat, c_void_p]
quartz.CGColorSpaceCreateDeviceRGB.restype = c_void_p
quartz.CGBitmapContextCreate.restype = c_void_p
quartz.CGBitmapContextCreateImage.restype = c_void_p
quartz.CGImageGetDataProvider.restype = c_void_p
quartz.CGDataProviderCopyData.restype = c_void_p
quartz.CGDataProviderCreateWithCFData.restype = c_void_p
quartz.CGFontCreateWithDataProvider.restype = c_void_p
quartz.CGContextSetTextPosition.argtypes = [c_void_p, CGFloat, CGFloat]
quartz.CGFontCreateWithFontName.restype = c_void_p
kCFStringEncodingUTF8 = 134217984
kCFNumberSInt32Type = 3
kCTFontAttributeName = c_void_p.in_dll(ct, 'kCTFontAttributeName')
kCTFontFamilyNameAttribute = c_void_p.in_dll(ct, 'kCTFontFamilyNameAttribute')
kCTFontSymbolicTrait = c_void_p.in_dll(ct, 'kCTFontSymbolicTrait')
kCTFontWeightTrait = c_void_p.in_dll(ct, 'kCTFontWeightTrait')
kCTFontTraitsAttribute = c_void_p.in_dll(ct, 'kCTFontTraitsAttribute')
kCTFontItalicTrait = 1
kCTFontBoldTrait = 2
kCGImageAlphaPremultipliedLast = 1

def CFSTR(text):
    return c_void_p(cf.CFStringCreateWithCString(None, text.encode('utf8'), kCFStringEncodingUTF8))


def cfstring_to_string(cfstring):
    length = cf.CFStringGetLength(cfstring)
    size = cf.CFStringGetMaximumSizeForEncoding(length, kCFStringEncodingUTF8)
    buffer = c_buffer(size + 1)
    result = cf.CFStringGetCString(cfstring, buffer, len(buffer), kCFStringEncodingUTF8)
    if result:
        return buffer.value


class QuartzGlyphRenderer(base.GlyphRenderer):

    def __init__(self, font):
        super(QuartzGlyphRenderer, self).__init__(font)
        self.font = font

    def render(self, text):
        ctFont = self.font.ctFont
        attributes = c_void_p(cf.CFDictionaryCreateMutable(None, 1, cf.kCFTypeDictionaryKeyCallBacks, cf.kCFTypeDictionaryValueCallBacks))
        cf.CFDictionaryAddValue(attributes, kCTFontAttributeName, ctFont)
        string = c_void_p(cf.CFAttributedStringCreate(None, CFSTR(text), attributes))
        line = c_void_p(ct.CTLineCreateWithAttributedString(string))
        cf.CFRelease(string)
        cf.CFRelease(attributes)
        count = len(text)
        chars = (UniChar * count)(*map(ord, unicode(text)))
        glyphs = (CGGlyph * count)()
        ct.CTFontGetGlyphsForCharacters(ctFont, chars, glyphs, count)
        rect = ct.CTFontGetBoundingRectsForGlyphs(ctFont, 0, glyphs, None, count)
        advance = ct.CTFontGetAdvancesForGlyphs(ctFont, 0, glyphs, None, count)
        width = max(int(math.ceil(rect.size.width) + 2), 1)
        height = max(int(math.ceil(rect.size.height) + 2), 1)
        baseline = -int(math.floor(rect.origin.y)) + 1
        lsb = int(math.floor(rect.origin.x)) - 1
        advance = int(round(advance))
        bitsPerComponent = 8
        bytesPerRow = 4 * width
        colorSpace = c_void_p(quartz.CGColorSpaceCreateDeviceRGB())
        bitmap = c_void_p(quartz.CGBitmapContextCreate(None, width, height, bitsPerComponent, bytesPerRow, colorSpace, kCGImageAlphaPremultipliedLast))
        quartz.CGContextSetShouldAntialias(bitmap, True)
        quartz.CGContextSetTextPosition(bitmap, -lsb, baseline)
        ct.CTLineDraw(line, bitmap)
        cf.CFRelease(line)
        imageRef = c_void_p(quartz.CGBitmapContextCreateImage(bitmap))
        bytesPerRow = quartz.CGImageGetBytesPerRow(imageRef)
        dataProvider = c_void_p(quartz.CGImageGetDataProvider(imageRef))
        imageData = c_void_p(quartz.CGDataProviderCopyData(dataProvider))
        buffersize = cf.CFDataGetLength(imageData)
        buffer = (c_byte * buffersize)()
        byteRange = CFRange(0, buffersize)
        cf.CFDataGetBytes(imageData, byteRange, buffer)
        quartz.CGImageRelease(imageRef)
        quartz.CGDataProviderRelease(imageData)
        cf.CFRelease(bitmap)
        cf.CFRelease(colorSpace)
        glyph_image = pyglet.image.ImageData(width, height, 'RGBA', buffer, bytesPerRow)
        glyph = self.font.create_glyph(glyph_image)
        glyph.set_bearings(baseline, lsb, advance)
        t = list(glyph.tex_coords)
        glyph.tex_coords = t[9:12] + t[6:9] + t[3:6] + t[:3]
        return glyph


class QuartzFont(base.Font):
    glyph_renderer_class = QuartzGlyphRenderer
    _loaded_CGFont_table = {}

    def _lookup_font_with_family_and_traits(self, family, traits):
        if family not in self._loaded_CGFont_table:
            return None
        else:
            fonts = self._loaded_CGFont_table[family]
            if not fonts:
                return None
            if traits in fonts:
                return fonts[traits]
            for t, f in fonts.items():
                if traits & t:
                    return f

            if 0 in fonts:
                return fonts[0]
            return fonts.values()[0]

    def _create_font_descriptor(self, family_name, traits):
        attributes = c_void_p(cf.CFDictionaryCreateMutable(None, 0, cf.kCFTypeDictionaryKeyCallBacks, cf.kCFTypeDictionaryValueCallBacks))
        cfname = CFSTR(family_name)
        cf.CFDictionaryAddValue(attributes, kCTFontFamilyNameAttribute, cfname)
        cf.CFRelease(cfname)
        itraits = c_int32(traits)
        symTraits = c_void_p(cf.CFNumberCreate(None, kCFNumberSInt32Type, byref(itraits)))
        if symTraits:
            traitsDict = c_void_p(cf.CFDictionaryCreateMutable(None, 0, cf.kCFTypeDictionaryKeyCallBacks, cf.kCFTypeDictionaryValueCallBacks))
            if traitsDict:
                cf.CFDictionaryAddValue(traitsDict, kCTFontSymbolicTrait, symTraits)
                cf.CFDictionaryAddValue(attributes, kCTFontTraitsAttribute, traitsDict)
                cf.CFRelease(traitsDict)
            cf.CFRelease(symTraits)
        descriptor = c_void_p(ct.CTFontDescriptorCreateWithAttributes(attributes))
        cf.CFRelease(attributes)
        return descriptor

    def __init__(self, name, size, bold=False, italic=False, dpi=None):
        super(QuartzFont, self).__init__()
        if not name:
            name = 'Helvetica'
        if dpi is None:
            dpi = 96
        size = size * dpi / 72.0
        traits = 0
        if bold:
            traits |= kCTFontBoldTrait
        if italic:
            traits |= kCTFontItalicTrait
        name = unicode(name)
        cgFont = self._lookup_font_with_family_and_traits(name, traits)
        if cgFont:
            self.ctFont = c_void_p(ct.CTFontCreateWithGraphicsFont(cgFont, size, None, None))
        else:
            descriptor = self._create_font_descriptor(name, traits)
            self.ctFont = c_void_p(ct.CTFontCreateWithFontDescriptor(descriptor, size, None))
        self.ascent = int(math.ceil(ct.CTFontGetAscent(self.ctFont)))
        self.descent = -int(math.ceil(ct.CTFontGetDescent(self.ctFont)))
        return

    @classmethod
    def have_font(cls, name):
        name = unicode(name)
        if name in cls._loaded_CGFont_table:
            return True
        cfstring = CFSTR(name)
        cgfont = c_void_p(quartz.CGFontCreateWithFontName(cfstring))
        cf.CFRelease(cfstring)
        if cgfont:
            cf.CFRelease(cgfont)
            return True
        return False

    @classmethod
    def add_font_data(cls, data):
        dataRef = c_void_p(cf.CFDataCreate(None, data, len(data)))
        provider = c_void_p(quartz.CGDataProviderCreateWithCFData(dataRef))
        cgFont = c_void_p(quartz.CGFontCreateWithDataProvider(provider))
        cf.CFRelease(dataRef)
        quartz.CGDataProviderRelease(provider)
        ctFont = c_void_p(ct.CTFontCreateWithGraphicsFont(cgFont, 1, None, None))
        string = c_void_p(ct.CTFontCopyFamilyName(ctFont))
        familyName = unicode(cfstring_to_string(string))
        cf.CFRelease(string)
        string = c_void_p(ct.CTFontCopyFullName(ctFont))
        fullName = unicode(cfstring_to_string(string))
        cf.CFRelease(string)
        traits = ct.CTFontGetSymbolicTraits(ctFont)
        cf.CFRelease(ctFont)
        if familyName not in cls._loaded_CGFont_table:
            cls._loaded_CGFont_table[familyName] = {}
        cls._loaded_CGFont_table[familyName][traits] = cgFont
        if fullName not in cls._loaded_CGFont_table:
            cls._loaded_CGFont_table[fullName] = {}
        cls._loaded_CGFont_table[fullName][traits] = cgFont
        return
# okay decompiling out\pyglet.font.quartz.pyc
