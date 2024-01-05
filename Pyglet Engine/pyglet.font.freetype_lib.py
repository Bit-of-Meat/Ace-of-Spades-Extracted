# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.font.freetype_lib
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from base import FontException
import pyglet.lib
_libfreetype = pyglet.lib.load_library('freetype')
_font_data = {}

def _get_function(name, argtypes, rtype):
    try:
        func = getattr(_libfreetype, name)
        func.argtypes = argtypes
        func.restype = rtype
        return func
    except AttributeError as e:
        raise ImportError(e)


FT_Done_FreeType = _get_function('FT_Done_FreeType', [c_void_p], None)
FT_Done_Face = _get_function('FT_Done_Face', [c_void_p], None)

class FT_LibraryRec(Structure):
    _fields_ = [
     (
      'dummy', c_int)]

    def __del__(self):
        global _library
        try:
            FT_Done_FreeType(byref(self))
            _library = None
        except:
            pass

        return


FT_Library = POINTER(FT_LibraryRec)

class FT_Glyph_Metrics(Structure):
    _fields_ = [
     (
      'width', c_long),
     (
      'height', c_long),
     (
      'horiBearingX', c_long),
     (
      'horiBearingY', c_long),
     (
      'horiAdvance', c_long),
     (
      'vertBearingX', c_long),
     (
      'vertBearingY', c_long),
     (
      'vertAdvance', c_long)]

    def dump(self):
        for name, type in self._fields_:
            print 'FT_Glyph_Metrics', name, `(getattr(self, name))`


class FT_Generic(Structure):
    _fields_ = [
     (
      'data', c_void_p), ('finalizer', c_void_p)]


class FT_BBox(Structure):
    _fields_ = [
     (
      'xMin', c_long), ('yMin', c_long), ('xMax', c_long),
     (
      'yMax', c_long)]


class FT_Vector(Structure):
    _fields_ = [
     (
      'x', c_long), ('y', c_long)]


class FT_Bitmap(Structure):
    _fields_ = [
     (
      'rows', c_int),
     (
      'width', c_int),
     (
      'pitch', c_int),
     (
      'buffer', POINTER(c_ubyte)),
     (
      'num_grays', c_short),
     (
      'pixel_mode', c_ubyte),
     (
      'palette_mode', c_char),
     (
      'palette', c_void_p)]


class FT_Outline(Structure):
    _fields_ = [
     (
      'n_contours', c_short),
     (
      'n_points', c_short),
     (
      'points', POINTER(FT_Vector)),
     (
      'tags', c_char_p),
     (
      'contours', POINTER(c_short)),
     (
      'flags', c_int)]


class FT_GlyphSlotRec(Structure):
    _fields_ = [
     (
      'library', FT_Library),
     (
      'face', c_void_p),
     (
      'next', c_void_p),
     (
      'reserved', c_uint),
     (
      'generic', FT_Generic),
     (
      'metrics', FT_Glyph_Metrics),
     (
      'linearHoriAdvance', c_long),
     (
      'linearVertAdvance', c_long),
     (
      'advance', FT_Vector),
     (
      'format', c_int),
     (
      'bitmap', FT_Bitmap),
     (
      'bitmap_left', c_int),
     (
      'bitmap_top', c_int),
     (
      'outline', FT_Outline),
     (
      'num_subglyphs', c_uint),
     (
      'subglyphs', c_void_p),
     (
      'control_data', c_void_p),
     (
      'control_len', c_long),
     (
      'lsb_delta', c_long),
     (
      'rsb_delta', c_long),
     (
      'other', c_void_p),
     (
      'internal', c_void_p)]


FT_GlyphSlot = POINTER(FT_GlyphSlotRec)

class FT_Size_Metrics(Structure):
    _fields_ = [
     (
      'x_ppem', c_ushort),
     (
      'y_ppem', c_ushort),
     (
      'x_scale', c_long),
     (
      'y_scale', c_long),
     (
      'ascender', c_long),
     (
      'descender', c_long),
     (
      'height', c_long),
     (
      'max_advance', c_long)]


class FT_SizeRec(Structure):
    _fields_ = [
     (
      'face', c_void_p),
     (
      'generic', FT_Generic),
     (
      'metrics', FT_Size_Metrics),
     (
      'internal', c_void_p)]


FT_Size = POINTER(FT_SizeRec)

class FT_Bitmap_Size(Structure):
    _fields_ = [
     (
      'height', c_ushort),
     (
      'width', c_ushort),
     (
      'size', c_long),
     (
      'x_ppem', c_long),
     (
      'y_ppem', c_long)]


FT_FACE_FLAG_SCALABLE = 1
FT_FACE_FLAG_FIXED_SIZES = 2
FT_FACE_FLAG_FIXED_WIDTH = 4
FT_FACE_FLAG_SFNT = 8
FT_FACE_FLAG_HORIZONTAL = 16
FT_FACE_FLAG_VERTICAL = 32
FT_FACE_FLAG_KERNING = 64
FT_FACE_FLAG_FAST_GLYPHS = 128
FT_FACE_FLAG_MULTIPLE_MASTERS = 256
FT_FACE_FLAG_GLYPH_NAMES = 512
FT_FACE_FLAG_EXTERNAL_STREAM = 1024
FT_FACE_FLAG_HINTER = 2048

class FT_FaceRec(Structure):
    _fields_ = [
     (
      'num_faces', c_long),
     (
      'face_index', c_long),
     (
      'face_flags', c_long),
     (
      'style_flags', c_long),
     (
      'num_glyphs', c_long),
     (
      'family_name', c_char_p),
     (
      'style_name', c_char_p),
     (
      'num_fixed_sizes', c_int),
     (
      'available_sizes', POINTER(FT_Bitmap_Size)),
     (
      'num_charmaps', c_int),
     (
      'charmaps', c_void_p),
     (
      'generic', FT_Generic),
     (
      'bbox', FT_BBox),
     (
      'units_per_EM', c_ushort),
     (
      'ascender', c_short),
     (
      'descender', c_short),
     (
      'height', c_short),
     (
      'max_advance_width', c_short),
     (
      'max_advance_height', c_short),
     (
      'underline_position', c_short),
     (
      'underline_thickness', c_short),
     (
      'glyph', FT_GlyphSlot),
     (
      'size', FT_Size),
     (
      'charmap', c_void_p),
     (
      'driver', c_void_p),
     (
      'memory', c_void_p),
     (
      'stream', c_void_p),
     (
      'sizes_list_head', c_void_p),
     (
      'sizes_list_tail', c_void_p),
     (
      'autohint', FT_Generic),
     (
      'extensions', c_void_p),
     (
      'internal', c_void_p)]

    def dump(self):
        for name, type in self._fields_:
            print 'FT_FaceRec', name, `(getattr(self, name))`

    def has_kerning(self):
        return self.face_flags & FT_FACE_FLAG_KERNING


FT_Face = POINTER(FT_FaceRec)

class Error(Exception):

    def __init__(self, message, errcode):
        self.message = message
        self.errcode = errcode

    def __str__(self):
        return '%s: %s (%s)' % (self.__class__.__name__, self.message,
         self._ft_errors.get(self.errcode, 'unknown error'))

    _ft_errors = {0: 'no error', 
       1: 'cannot open resource', 
       2: 'unknown file format', 
       3: 'broken file', 
       4: 'invalid FreeType version', 
       5: 'module version is too low', 
       6: 'invalid argument', 
       7: 'unimplemented feature', 
       8: 'broken table', 
       9: 'broken offset within table', 
       16: 'invalid glyph index', 
       17: 'invalid character code', 
       18: 'unsupported glyph image format', 
       19: 'cannot render this glyph format', 
       20: 'invalid outline', 
       21: 'invalid composite glyph', 
       22: 'too many hints', 
       23: 'invalid pixel size', 
       32: 'invalid object handle', 
       33: 'invalid library handle', 
       34: 'invalid module handle', 
       35: 'invalid face handle', 
       36: 'invalid size handle', 
       37: 'invalid glyph slot handle', 
       38: 'invalid charmap handle', 
       39: 'invalid cache manager handle', 
       40: 'invalid stream handle', 
       48: 'too many modules', 
       49: 'too many extensions', 
       64: 'out of memory', 
       65: 'unlisted object', 
       81: 'cannot open stream', 
       82: 'invalid stream seek', 
       83: 'invalid stream skip', 
       84: 'invalid stream read', 
       85: 'invalid stream operation', 
       86: 'invalid frame operation', 
       87: 'nested frame access', 
       88: 'invalid frame read', 
       96: 'raster uninitialized', 
       97: 'raster corrupted', 
       98: 'raster overflow', 
       99: 'negative height while rastering', 
       112: 'too many registered caches', 
       128: 'invalid opcode', 
       129: 'too few arguments', 
       130: 'stack overflow', 
       131: 'code overflow', 
       132: 'bad argument', 
       133: 'division by zero', 
       134: 'invalid reference', 
       135: 'found debug opcode', 
       136: 'found ENDF opcode in execution stream', 
       137: 'nested DEFS', 
       138: 'invalid code range', 
       139: 'execution context too long', 
       140: 'too many function definitions', 
       141: 'too many instruction definitions', 
       142: 'SFNT font table missing', 
       143: 'horizontal header (hhea, table missing', 
       144: 'locations (loca, table missing', 
       145: 'name table missing', 
       146: 'character map (cmap, table missing', 
       147: 'horizontal metrics (hmtx, table missing', 
       148: 'PostScript (post, table missing', 
       149: 'invalid horizontal metrics', 
       150: 'invalid character map (cmap, format', 
       151: 'invalid ppem value', 
       152: 'invalid vertical metrics', 
       153: 'could not find context', 
       154: 'invalid PostScript (post, table format', 
       155: 'invalid PostScript (post, table', 
       160: 'opcode syntax error', 
       161: 'argument stack underflow', 
       162: 'ignore', 
       176: "`STARTFONT' field missing", 
       177: "`FONT' field missing", 
       178: "`SIZE' field missing", 
       179: "`CHARS' field missing", 
       180: "`STARTCHAR' field missing", 
       181: "`ENCODING' field missing", 
       182: "`BBX' field missing", 
       183: "`BBX' too big"}


FT_LOAD_RENDER = 4
FT_F26Dot6 = c_long
FT_Init_FreeType = _get_function('FT_Init_FreeType', [
 POINTER(FT_Library)], c_int)
FT_New_Memory_Face = _get_function('FT_New_Memory_Face', [
 FT_Library, POINTER(c_byte), c_long, c_long, POINTER(FT_Face)], c_int)
FT_New_Face = _get_function('FT_New_Face', [
 FT_Library, c_char_p, c_long, POINTER(FT_Face)], c_int)
FT_Set_Pixel_Sizes = _get_function('FT_Set_Pixel_Sizes', [
 FT_Face, c_uint, c_uint], c_int)
FT_Set_Char_Size = _get_function('FT_Set_Char_Size', [
 FT_Face, FT_F26Dot6, FT_F26Dot6, c_uint, c_uint], c_int)
FT_Load_Glyph = _get_function('FT_Load_Glyph', [
 FT_Face, c_uint, c_int32], c_int)
FT_Get_Char_Index = _get_function('FT_Get_Char_Index', [
 FT_Face, c_ulong], c_uint)
FT_Load_Char = _get_function('FT_Load_Char', [
 FT_Face, c_ulong, c_int], c_int)
FT_Get_Kerning = _get_function('FT_Get_Kerning', [
 FT_Face, c_uint, c_uint, c_uint, POINTER(FT_Vector)], c_int)

class FT_SfntName(Structure):
    _fields_ = [
     (
      'platform_id', c_ushort),
     (
      'encoding_id', c_ushort),
     (
      'language_id', c_ushort),
     (
      'name_id', c_ushort),
     (
      'string', POINTER(c_byte)),
     (
      'string_len', c_uint)]


FT_Get_Sfnt_Name_Count = _get_function('FT_Get_Sfnt_Name_Count', [
 FT_Face], c_uint)
FT_Get_Sfnt_Name = _get_function('FT_Get_Sfnt_Name', [
 FT_Face, c_uint, POINTER(FT_SfntName)], c_int)
TT_PLATFORM_MICROSOFT = 3
TT_MS_ID_UNICODE_CS = 1
TT_NAME_ID_COPYRIGHT = 0
TT_NAME_ID_FONT_FAMILY = 1
TT_NAME_ID_FONT_SUBFAMILY = 2
TT_NAME_ID_UNIQUE_ID = 3
TT_NAME_ID_FULL_NAME = 4
TT_NAME_ID_VERSION_STRING = 5
TT_NAME_ID_PS_NAME = 6
TT_NAME_ID_TRADEMARK = 7
TT_NAME_ID_MANUFACTURER = 8
TT_NAME_ID_DESIGNER = 9
TT_NAME_ID_DESCRIPTION = 10
TT_NAME_ID_VENDOR_URL = 11
TT_NAME_ID_DESIGNER_URL = 12
TT_NAME_ID_LICENSE = 13
TT_NAME_ID_LICENSE_URL = 14
TT_NAME_ID_PREFERRED_FAMILY = 16
TT_NAME_ID_PREFERRED_SUBFAMILY = 17
TT_NAME_ID_MAC_FULL_NAME = 18
TT_NAME_ID_CID_FINDFONT_NAME = 20
_library = None

def ft_get_library():
    global _library
    if not _library:
        _library = FT_Library()
        error = FT_Init_FreeType(byref(_library))
        if error:
            raise FontException('an error occurred during library initialization', error)
    return _library
# okay decompiling out\pyglet.font.freetype_lib.pyc
