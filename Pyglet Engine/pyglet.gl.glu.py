# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.glu
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from pyglet.gl.lib import link_GLU as _link_function
from pyglet.gl.lib import c_ptrdiff_t
GLU_EXT_object_space_tess = 1
GLU_EXT_nurbs_tessellator = 1
GLU_FALSE = 0
GLU_TRUE = 1
GLU_VERSION_1_1 = 1
GLU_VERSION_1_2 = 1
GLU_VERSION_1_3 = 1
GLU_VERSION = 100800
GLU_EXTENSIONS = 100801
GLU_INVALID_ENUM = 100900
GLU_INVALID_VALUE = 100901
GLU_OUT_OF_MEMORY = 100902
GLU_INCOMPATIBLE_GL_VERSION = 100903
GLU_INVALID_OPERATION = 100904
GLU_OUTLINE_POLYGON = 100240
GLU_OUTLINE_PATCH = 100241
GLU_NURBS_ERROR = 100103
GLU_ERROR = 100103
GLU_NURBS_BEGIN = 100164
GLU_NURBS_BEGIN_EXT = 100164
GLU_NURBS_VERTEX = 100165
GLU_NURBS_VERTEX_EXT = 100165
GLU_NURBS_NORMAL = 100166
GLU_NURBS_NORMAL_EXT = 100166
GLU_NURBS_COLOR = 100167
GLU_NURBS_COLOR_EXT = 100167
GLU_NURBS_TEXTURE_COORD = 100168
GLU_NURBS_TEX_COORD_EXT = 100168
GLU_NURBS_END = 100169
GLU_NURBS_END_EXT = 100169
GLU_NURBS_BEGIN_DATA = 100170
GLU_NURBS_BEGIN_DATA_EXT = 100170
GLU_NURBS_VERTEX_DATA = 100171
GLU_NURBS_VERTEX_DATA_EXT = 100171
GLU_NURBS_NORMAL_DATA = 100172
GLU_NURBS_NORMAL_DATA_EXT = 100172
GLU_NURBS_COLOR_DATA = 100173
GLU_NURBS_COLOR_DATA_EXT = 100173
GLU_NURBS_TEXTURE_COORD_DATA = 100174
GLU_NURBS_TEX_COORD_DATA_EXT = 100174
GLU_NURBS_END_DATA = 100175
GLU_NURBS_END_DATA_EXT = 100175
GLU_NURBS_ERROR1 = 100251
GLU_NURBS_ERROR2 = 100252
GLU_NURBS_ERROR3 = 100253
GLU_NURBS_ERROR4 = 100254
GLU_NURBS_ERROR5 = 100255
GLU_NURBS_ERROR6 = 100256
GLU_NURBS_ERROR7 = 100257
GLU_NURBS_ERROR8 = 100258
GLU_NURBS_ERROR9 = 100259
GLU_NURBS_ERROR10 = 100260
GLU_NURBS_ERROR11 = 100261
GLU_NURBS_ERROR12 = 100262
GLU_NURBS_ERROR13 = 100263
GLU_NURBS_ERROR14 = 100264
GLU_NURBS_ERROR15 = 100265
GLU_NURBS_ERROR16 = 100266
GLU_NURBS_ERROR17 = 100267
GLU_NURBS_ERROR18 = 100268
GLU_NURBS_ERROR19 = 100269
GLU_NURBS_ERROR20 = 100270
GLU_NURBS_ERROR21 = 100271
GLU_NURBS_ERROR22 = 100272
GLU_NURBS_ERROR23 = 100273
GLU_NURBS_ERROR24 = 100274
GLU_NURBS_ERROR25 = 100275
GLU_NURBS_ERROR26 = 100276
GLU_NURBS_ERROR27 = 100277
GLU_NURBS_ERROR28 = 100278
GLU_NURBS_ERROR29 = 100279
GLU_NURBS_ERROR30 = 100280
GLU_NURBS_ERROR31 = 100281
GLU_NURBS_ERROR32 = 100282
GLU_NURBS_ERROR33 = 100283
GLU_NURBS_ERROR34 = 100284
GLU_NURBS_ERROR35 = 100285
GLU_NURBS_ERROR36 = 100286
GLU_NURBS_ERROR37 = 100287
GLU_AUTO_LOAD_MATRIX = 100200
GLU_CULLING = 100201
GLU_SAMPLING_TOLERANCE = 100203
GLU_DISPLAY_MODE = 100204
GLU_PARAMETRIC_TOLERANCE = 100202
GLU_SAMPLING_METHOD = 100205
GLU_U_STEP = 100206
GLU_V_STEP = 100207
GLU_NURBS_MODE = 100160
GLU_NURBS_MODE_EXT = 100160
GLU_NURBS_TESSELLATOR = 100161
GLU_NURBS_TESSELLATOR_EXT = 100161
GLU_NURBS_RENDERER = 100162
GLU_NURBS_RENDERER_EXT = 100162
GLU_OBJECT_PARAMETRIC_ERROR = 100208
GLU_OBJECT_PARAMETRIC_ERROR_EXT = 100208
GLU_OBJECT_PATH_LENGTH = 100209
GLU_OBJECT_PATH_LENGTH_EXT = 100209
GLU_PATH_LENGTH = 100215
GLU_PARAMETRIC_ERROR = 100216
GLU_DOMAIN_DISTANCE = 100217
GLU_MAP1_TRIM_2 = 100210
GLU_MAP1_TRIM_3 = 100211
GLU_POINT = 100010
GLU_LINE = 100011
GLU_FILL = 100012
GLU_SILHOUETTE = 100013
GLU_SMOOTH = 100000
GLU_FLAT = 100001
GLU_NONE = 100002
GLU_OUTSIDE = 100020
GLU_INSIDE = 100021
GLU_TESS_BEGIN = 100100
GLU_BEGIN = 100100
GLU_TESS_VERTEX = 100101
GLU_VERTEX = 100101
GLU_TESS_END = 100102
GLU_END = 100102
GLU_TESS_ERROR = 100103
GLU_TESS_EDGE_FLAG = 100104
GLU_EDGE_FLAG = 100104
GLU_TESS_COMBINE = 100105
GLU_TESS_BEGIN_DATA = 100106
GLU_TESS_VERTEX_DATA = 100107
GLU_TESS_END_DATA = 100108
GLU_TESS_ERROR_DATA = 100109
GLU_TESS_EDGE_FLAG_DATA = 100110
GLU_TESS_COMBINE_DATA = 100111
GLU_CW = 100120
GLU_CCW = 100121
GLU_INTERIOR = 100122
GLU_EXTERIOR = 100123
GLU_UNKNOWN = 100124
GLU_TESS_WINDING_RULE = 100140
GLU_TESS_BOUNDARY_ONLY = 100141
GLU_TESS_TOLERANCE = 100142
GLU_TESS_ERROR1 = 100151
GLU_TESS_ERROR2 = 100152
GLU_TESS_ERROR3 = 100153
GLU_TESS_ERROR4 = 100154
GLU_TESS_ERROR5 = 100155
GLU_TESS_ERROR6 = 100156
GLU_TESS_ERROR7 = 100157
GLU_TESS_ERROR8 = 100158
GLU_TESS_MISSING_BEGIN_POLYGON = 100151
GLU_TESS_MISSING_BEGIN_CONTOUR = 100152
GLU_TESS_MISSING_END_POLYGON = 100153
GLU_TESS_MISSING_END_CONTOUR = 100154
GLU_TESS_COORD_TOO_LARGE = 100155
GLU_TESS_NEED_COMBINE_CALLBACK = 100156
GLU_TESS_WINDING_ODD = 100130
GLU_TESS_WINDING_NONZERO = 100131
GLU_TESS_WINDING_POSITIVE = 100132
GLU_TESS_WINDING_NEGATIVE = 100133
GLU_TESS_WINDING_ABS_GEQ_TWO = 100134

class struct_GLUnurbs(Structure):
    __slots__ = []


struct_GLUnurbs._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct_GLUnurbs(Structure):
    __slots__ = []


struct_GLUnurbs._fields_ = [
 (
  '_opaque_struct', c_int)]
GLUnurbs = struct_GLUnurbs

class struct_GLUquadric(Structure):
    __slots__ = []


struct_GLUquadric._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct_GLUquadric(Structure):
    __slots__ = []


struct_GLUquadric._fields_ = [
 (
  '_opaque_struct', c_int)]
GLUquadric = struct_GLUquadric

class struct_GLUtesselator(Structure):
    __slots__ = []


struct_GLUtesselator._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct_GLUtesselator(Structure):
    __slots__ = []


struct_GLUtesselator._fields_ = [
 (
  '_opaque_struct', c_int)]
GLUtesselator = struct_GLUtesselator
GLUnurbsObj = GLUnurbs
GLUquadricObj = GLUquadric
GLUtesselatorObj = GLUtesselator
GLUtriangulatorObj = GLUtesselator
GLU_TESS_MAX_COORD = 1e+150
_GLUfuncptr = CFUNCTYPE(None)
gluBeginCurve = _link_function('gluBeginCurve', None, [POINTER(GLUnurbs)], None)
gluBeginPolygon = _link_function('gluBeginPolygon', None, [POINTER(GLUtesselator)], None)
gluBeginSurface = _link_function('gluBeginSurface', None, [POINTER(GLUnurbs)], None)
gluBeginTrim = _link_function('gluBeginTrim', None, [POINTER(GLUnurbs)], None)
GLint = c_int
GLenum = c_uint
GLsizei = c_int
gluBuild1DMipmapLevels = _link_function('gluBuild1DMipmapLevels', GLint, [GLenum, GLint, GLsizei, GLenum, GLenum, GLint, GLint, GLint, POINTER(None)], None)
gluBuild1DMipmaps = _link_function('gluBuild1DMipmaps', GLint, [GLenum, GLint, GLsizei, GLenum, GLenum, POINTER(None)], None)
gluBuild2DMipmapLevels = _link_function('gluBuild2DMipmapLevels', GLint, [GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, GLint, GLint, GLint, POINTER(None)], None)
gluBuild2DMipmaps = _link_function('gluBuild2DMipmaps', GLint, [GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(None)], None)
gluBuild3DMipmapLevels = _link_function('gluBuild3DMipmapLevels', GLint, [GLenum, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, GLint, GLint, GLint, POINTER(None)], None)
gluBuild3DMipmaps = _link_function('gluBuild3DMipmaps', GLint, [GLenum, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(None)], None)
GLboolean = c_ubyte
GLubyte = c_ubyte
gluCheckExtension = _link_function('gluCheckExtension', GLboolean, [POINTER(GLubyte), POINTER(GLubyte)], None)
GLdouble = c_double
gluCylinder = _link_function('gluCylinder', None, [POINTER(GLUquadric), GLdouble, GLdouble, GLdouble, GLint, GLint], None)
gluDeleteNurbsRenderer = _link_function('gluDeleteNurbsRenderer', None, [POINTER(GLUnurbs)], None)
gluDeleteQuadric = _link_function('gluDeleteQuadric', None, [POINTER(GLUquadric)], None)
gluDeleteTess = _link_function('gluDeleteTess', None, [POINTER(GLUtesselator)], None)
gluDisk = _link_function('gluDisk', None, [POINTER(GLUquadric), GLdouble, GLdouble, GLint, GLint], None)
gluEndCurve = _link_function('gluEndCurve', None, [POINTER(GLUnurbs)], None)
gluEndPolygon = _link_function('gluEndPolygon', None, [POINTER(GLUtesselator)], None)
gluEndSurface = _link_function('gluEndSurface', None, [POINTER(GLUnurbs)], None)
gluEndTrim = _link_function('gluEndTrim', None, [POINTER(GLUnurbs)], None)
gluErrorString = _link_function('gluErrorString', POINTER(GLubyte), [GLenum], None)
GLfloat = c_float
gluGetNurbsProperty = _link_function('gluGetNurbsProperty', None, [POINTER(GLUnurbs), GLenum, POINTER(GLfloat)], None)
gluGetString = _link_function('gluGetString', POINTER(GLubyte), [GLenum], None)
gluGetTessProperty = _link_function('gluGetTessProperty', None, [POINTER(GLUtesselator), GLenum, POINTER(GLdouble)], None)
gluLoadSamplingMatrices = _link_function('gluLoadSamplingMatrices', None, [POINTER(GLUnurbs), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLint)], None)
gluLookAt = _link_function('gluLookAt', None, [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, 
 GLdouble], None)
gluNewNurbsRenderer = _link_function('gluNewNurbsRenderer', POINTER(GLUnurbs), [], None)
gluNewQuadric = _link_function('gluNewQuadric', POINTER(GLUquadric), [], None)
gluNewTess = _link_function('gluNewTess', POINTER(GLUtesselator), [], None)
gluNextContour = _link_function('gluNextContour', None, [POINTER(GLUtesselator), GLenum], None)
gluNurbsCallback = _link_function('gluNurbsCallback', None, [POINTER(GLUnurbs), GLenum, _GLUfuncptr], None)
GLvoid = None
gluNurbsCallbackData = _link_function('gluNurbsCallbackData', None, [POINTER(GLUnurbs), POINTER(GLvoid)], None)
gluNurbsCallbackDataEXT = _link_function('gluNurbsCallbackDataEXT', None, [POINTER(GLUnurbs), POINTER(GLvoid)], None)
gluNurbsCurve = _link_function('gluNurbsCurve', None, [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLenum], None)
gluNurbsProperty = _link_function('gluNurbsProperty', None, [POINTER(GLUnurbs), GLenum, GLfloat], None)
gluNurbsSurface = _link_function('gluNurbsSurface', None, [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLint, POINTER(GLfloat), GLint, GLint, GLenum], None)
gluOrtho2D = _link_function('gluOrtho2D', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
gluPartialDisk = _link_function('gluPartialDisk', None, [POINTER(GLUquadric), GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble], None)
gluPerspective = _link_function('gluPerspective', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
gluPickMatrix = _link_function('gluPickMatrix', None, [GLdouble, GLdouble, GLdouble, GLdouble, POINTER(GLint)], None)
gluProject = _link_function('gluProject', GLint, [GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)], None)
gluPwlCurve = _link_function('gluPwlCurve', None, [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, GLenum], None)
gluQuadricCallback = _link_function('gluQuadricCallback', None, [POINTER(GLUquadric), GLenum, _GLUfuncptr], None)
gluQuadricDrawStyle = _link_function('gluQuadricDrawStyle', None, [POINTER(GLUquadric), GLenum], None)
gluQuadricNormals = _link_function('gluQuadricNormals', None, [POINTER(GLUquadric), GLenum], None)
gluQuadricOrientation = _link_function('gluQuadricOrientation', None, [POINTER(GLUquadric), GLenum], None)
gluQuadricTexture = _link_function('gluQuadricTexture', None, [POINTER(GLUquadric), GLboolean], None)
gluScaleImage = _link_function('gluScaleImage', GLint, [GLenum, GLsizei, GLsizei, GLenum, POINTER(None), GLsizei, GLsizei, GLenum, POINTER(GLvoid)], None)
gluSphere = _link_function('gluSphere', None, [POINTER(GLUquadric), GLdouble, GLint, GLint], None)
gluTessBeginContour = _link_function('gluTessBeginContour', None, [POINTER(GLUtesselator)], None)
gluTessBeginPolygon = _link_function('gluTessBeginPolygon', None, [POINTER(GLUtesselator), POINTER(GLvoid)], None)
gluTessCallback = _link_function('gluTessCallback', None, [POINTER(GLUtesselator), GLenum, _GLUfuncptr], None)
gluTessEndContour = _link_function('gluTessEndContour', None, [POINTER(GLUtesselator)], None)
gluTessEndPolygon = _link_function('gluTessEndPolygon', None, [POINTER(GLUtesselator)], None)
gluTessNormal = _link_function('gluTessNormal', None, [POINTER(GLUtesselator), GLdouble, GLdouble, GLdouble], None)
gluTessProperty = _link_function('gluTessProperty', None, [POINTER(GLUtesselator), GLenum, GLdouble], None)
gluTessVertex = _link_function('gluTessVertex', None, [POINTER(GLUtesselator), POINTER(GLdouble), POINTER(GLvoid)], None)
gluUnProject = _link_function('gluUnProject', GLint, [GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)], None)
gluUnProject4 = _link_function('gluUnProject4', GLint, [GLdouble, GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)], None)
__all__ = [
 'GLU_EXT_object_space_tess', 'GLU_EXT_nurbs_tessellator', 
 'GLU_FALSE', 'GLU_TRUE', 
 'GLU_VERSION_1_1', 'GLU_VERSION_1_2', 
 'GLU_VERSION_1_3', 'GLU_VERSION', 
 'GLU_EXTENSIONS', 'GLU_INVALID_ENUM', 
 'GLU_INVALID_VALUE', 'GLU_OUT_OF_MEMORY', 
 'GLU_INCOMPATIBLE_GL_VERSION', 
 'GLU_INVALID_OPERATION', 'GLU_OUTLINE_POLYGON', 
 'GLU_OUTLINE_PATCH', 
 'GLU_NURBS_ERROR', 'GLU_ERROR', 'GLU_NURBS_BEGIN', 
 'GLU_NURBS_BEGIN_EXT', 
 'GLU_NURBS_VERTEX', 'GLU_NURBS_VERTEX_EXT', 'GLU_NURBS_NORMAL', 
 'GLU_NURBS_NORMAL_EXT', 
 'GLU_NURBS_COLOR', 'GLU_NURBS_COLOR_EXT', 
 'GLU_NURBS_TEXTURE_COORD', 'GLU_NURBS_TEX_COORD_EXT', 
 'GLU_NURBS_END', 
 'GLU_NURBS_END_EXT', 'GLU_NURBS_BEGIN_DATA', 'GLU_NURBS_BEGIN_DATA_EXT', 
 'GLU_NURBS_VERTEX_DATA', 
 'GLU_NURBS_VERTEX_DATA_EXT', 'GLU_NURBS_NORMAL_DATA', 
 'GLU_NURBS_NORMAL_DATA_EXT', 
 'GLU_NURBS_COLOR_DATA', 
 'GLU_NURBS_COLOR_DATA_EXT', 'GLU_NURBS_TEXTURE_COORD_DATA', 
 'GLU_NURBS_TEX_COORD_DATA_EXT', 
 'GLU_NURBS_END_DATA', 
 'GLU_NURBS_END_DATA_EXT', 'GLU_NURBS_ERROR1', 'GLU_NURBS_ERROR2', 
 'GLU_NURBS_ERROR3', 
 'GLU_NURBS_ERROR4', 'GLU_NURBS_ERROR5', 
 'GLU_NURBS_ERROR6', 'GLU_NURBS_ERROR7', 
 'GLU_NURBS_ERROR8', 
 'GLU_NURBS_ERROR9', 'GLU_NURBS_ERROR10', 'GLU_NURBS_ERROR11', 
 'GLU_NURBS_ERROR12', 
 'GLU_NURBS_ERROR13', 'GLU_NURBS_ERROR14', 
 'GLU_NURBS_ERROR15', 'GLU_NURBS_ERROR16', 
 'GLU_NURBS_ERROR17', 
 'GLU_NURBS_ERROR18', 'GLU_NURBS_ERROR19', 'GLU_NURBS_ERROR20', 
 'GLU_NURBS_ERROR21', 
 'GLU_NURBS_ERROR22', 'GLU_NURBS_ERROR23', 
 'GLU_NURBS_ERROR24', 'GLU_NURBS_ERROR25', 
 'GLU_NURBS_ERROR26', 
 'GLU_NURBS_ERROR27', 'GLU_NURBS_ERROR28', 'GLU_NURBS_ERROR29', 
 'GLU_NURBS_ERROR30', 
 'GLU_NURBS_ERROR31', 'GLU_NURBS_ERROR32', 
 'GLU_NURBS_ERROR33', 'GLU_NURBS_ERROR34', 
 'GLU_NURBS_ERROR35', 
 'GLU_NURBS_ERROR36', 'GLU_NURBS_ERROR37', 'GLU_AUTO_LOAD_MATRIX', 
 'GLU_CULLING', 
 'GLU_SAMPLING_TOLERANCE', 'GLU_DISPLAY_MODE', 
 'GLU_PARAMETRIC_TOLERANCE', 
 'GLU_SAMPLING_METHOD', 'GLU_U_STEP', 'GLU_V_STEP', 
 'GLU_NURBS_MODE', 'GLU_NURBS_MODE_EXT', 
 'GLU_NURBS_TESSELLATOR', 
 'GLU_NURBS_TESSELLATOR_EXT', 'GLU_NURBS_RENDERER', 
 'GLU_NURBS_RENDERER_EXT', 
 'GLU_OBJECT_PARAMETRIC_ERROR', 'GLU_OBJECT_PARAMETRIC_ERROR_EXT', 
 'GLU_OBJECT_PATH_LENGTH', 
 'GLU_OBJECT_PATH_LENGTH_EXT', 'GLU_PATH_LENGTH', 
 'GLU_PARAMETRIC_ERROR', 
 'GLU_DOMAIN_DISTANCE', 'GLU_MAP1_TRIM_2', 
 'GLU_MAP1_TRIM_3', 'GLU_POINT', 
 'GLU_LINE', 'GLU_FILL', 'GLU_SILHOUETTE', 
 'GLU_SMOOTH', 'GLU_FLAT', 'GLU_NONE', 
 'GLU_OUTSIDE', 'GLU_INSIDE', 
 'GLU_TESS_BEGIN', 'GLU_BEGIN', 'GLU_TESS_VERTEX', 
 'GLU_VERTEX', 
 'GLU_TESS_END', 'GLU_END', 'GLU_TESS_ERROR', 'GLU_TESS_EDGE_FLAG', 
 'GLU_EDGE_FLAG', 
 'GLU_TESS_COMBINE', 'GLU_TESS_BEGIN_DATA', 
 'GLU_TESS_VERTEX_DATA', 'GLU_TESS_END_DATA', 
 'GLU_TESS_ERROR_DATA', 
 'GLU_TESS_EDGE_FLAG_DATA', 'GLU_TESS_COMBINE_DATA', 
 'GLU_CW', 'GLU_CCW', 
 'GLU_INTERIOR', 'GLU_EXTERIOR', 'GLU_UNKNOWN', 'GLU_TESS_WINDING_RULE', 
 'GLU_TESS_BOUNDARY_ONLY', 
 'GLU_TESS_TOLERANCE', 'GLU_TESS_ERROR1', 
 'GLU_TESS_ERROR2', 'GLU_TESS_ERROR3', 
 'GLU_TESS_ERROR4', 'GLU_TESS_ERROR5', 
 'GLU_TESS_ERROR6', 'GLU_TESS_ERROR7', 
 'GLU_TESS_ERROR8', 
 'GLU_TESS_MISSING_BEGIN_POLYGON', 'GLU_TESS_MISSING_BEGIN_CONTOUR', 
 'GLU_TESS_MISSING_END_POLYGON', 
 'GLU_TESS_MISSING_END_CONTOUR', 
 'GLU_TESS_COORD_TOO_LARGE', 'GLU_TESS_NEED_COMBINE_CALLBACK', 
 'GLU_TESS_WINDING_ODD', 
 'GLU_TESS_WINDING_NONZERO', 
 'GLU_TESS_WINDING_POSITIVE', 'GLU_TESS_WINDING_NEGATIVE', 
 'GLU_TESS_WINDING_ABS_GEQ_TWO', 
 'GLUnurbs', 'GLUquadric', 'GLUtesselator', 
 'GLUnurbsObj', 'GLUquadricObj', 
 'GLUtesselatorObj', 'GLUtriangulatorObj', 
 'GLU_TESS_MAX_COORD', '_GLUfuncptr', 
 'gluBeginCurve', 'gluBeginPolygon', 
 'gluBeginSurface', 'gluBeginTrim', 
 'gluBuild1DMipmapLevels', 
 'gluBuild1DMipmaps', 'gluBuild2DMipmapLevels', 
 'gluBuild2DMipmaps', 
 'gluBuild3DMipmapLevels', 'gluBuild3DMipmaps', 'gluCheckExtension', 
 'gluCylinder', 
 'gluDeleteNurbsRenderer', 'gluDeleteQuadric', 'gluDeleteTess', 
 'gluDisk', 
 'gluEndCurve', 'gluEndPolygon', 'gluEndSurface', 'gluEndTrim', 
 'gluErrorString', 
 'gluGetNurbsProperty', 'gluGetString', 'gluGetTessProperty', 
 'gluLoadSamplingMatrices', 
 'gluLookAt', 'gluNewNurbsRenderer', 
 'gluNewQuadric', 'gluNewTess', 'gluNextContour', 
 'gluNurbsCallback', 
 'gluNurbsCallbackData', 'gluNurbsCallbackDataEXT', 'gluNurbsCurve', 
 'gluNurbsProperty', 
 'gluNurbsSurface', 'gluOrtho2D', 'gluPartialDisk', 
 'gluPerspective', 'gluPickMatrix', 
 'gluProject', 'gluPwlCurve', 
 'gluQuadricCallback', 'gluQuadricDrawStyle', 
 'gluQuadricNormals', 
 'gluQuadricOrientation', 'gluQuadricTexture', 'gluScaleImage', 
 'gluSphere', 
 'gluTessBeginContour', 'gluTessBeginPolygon', 'gluTessCallback', 
 'gluTessEndContour', 
 'gluTessEndPolygon', 'gluTessNormal', 'gluTessProperty', 
 'gluTessVertex', 
 'gluUnProject', 'gluUnProject4']
# okay decompiling out\pyglet.gl.glu.pyc
