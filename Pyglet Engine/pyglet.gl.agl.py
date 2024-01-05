# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.agl
__docformat__ = 'restructuredtext'
__version__ = '$Id: gengl.py 601 2007-02-04 05:36:59Z Alex.Holkner $'
from ..ctypes import *
from pyglet.gl.lib import link_AGL as _link_function
if not _link_function:
    raise ImportError('AGL framework is not available.')
AGL_VERSION_2_0 = 1

class struct_GDevice(Structure):
    __slots__ = []


struct_GDevice._fields_ = [
 (
  '_opaque_struct', c_int)]
GDevice = struct_GDevice
GDPtr = POINTER(GDevice)
GDHandle = POINTER(GDPtr)
AGLDevice = GDHandle

class struct_OpaqueGrafPtr(Structure):
    __slots__ = []


struct_OpaqueGrafPtr._fields_ = [
 (
  '_opaque_struct', c_int)]
GrafPtr = POINTER(struct_OpaqueGrafPtr)
CGrafPtr = GrafPtr
AGLDrawable = CGrafPtr

class struct___AGLRendererInfoRec(Structure):
    __slots__ = []


struct___AGLRendererInfoRec._fields_ = [
 (
  '_opaque_struct', c_int)]
AGLRendererInfo = POINTER(struct___AGLRendererInfoRec)

class struct___AGLPixelFormatRec(Structure):
    __slots__ = []


struct___AGLPixelFormatRec._fields_ = [
 (
  '_opaque_struct', c_int)]
AGLPixelFormat = POINTER(struct___AGLPixelFormatRec)

class struct___AGLContextRec(Structure):
    __slots__ = []


struct___AGLContextRec._fields_ = [
 (
  '_opaque_struct', c_int)]
AGLContext = POINTER(struct___AGLContextRec)

class struct___AGLPBufferRec(Structure):
    __slots__ = []


struct___AGLPBufferRec._fields_ = [
 (
  '_opaque_struct', c_int)]
AGLPbuffer = POINTER(struct___AGLPBufferRec)
AGL_NONE = 0
AGL_ALL_RENDERERS = 1
AGL_BUFFER_SIZE = 2
AGL_LEVEL = 3
AGL_RGBA = 4
AGL_DOUBLEBUFFER = 5
AGL_STEREO = 6
AGL_AUX_BUFFERS = 7
AGL_RED_SIZE = 8
AGL_GREEN_SIZE = 9
AGL_BLUE_SIZE = 10
AGL_ALPHA_SIZE = 11
AGL_DEPTH_SIZE = 12
AGL_STENCIL_SIZE = 13
AGL_ACCUM_RED_SIZE = 14
AGL_ACCUM_GREEN_SIZE = 15
AGL_ACCUM_BLUE_SIZE = 16
AGL_ACCUM_ALPHA_SIZE = 17
AGL_PIXEL_SIZE = 50
AGL_MINIMUM_POLICY = 51
AGL_MAXIMUM_POLICY = 52
AGL_OFFSCREEN = 53
AGL_FULLSCREEN = 54
AGL_SAMPLE_BUFFERS_ARB = 55
AGL_SAMPLES_ARB = 56
AGL_AUX_DEPTH_STENCIL = 57
AGL_COLOR_FLOAT = 58
AGL_MULTISAMPLE = 59
AGL_SUPERSAMPLE = 60
AGL_SAMPLE_ALPHA = 61
AGL_RENDERER_ID = 70
AGL_SINGLE_RENDERER = 71
AGL_NO_RECOVERY = 72
AGL_ACCELERATED = 73
AGL_CLOSEST_POLICY = 74
AGL_ROBUST = 75
AGL_BACKING_STORE = 76
AGL_MP_SAFE = 78
AGL_WINDOW = 80
AGL_MULTISCREEN = 81
AGL_VIRTUAL_SCREEN = 82
AGL_COMPLIANT = 83
AGL_PBUFFER = 90
AGL_BUFFER_MODES = 100
AGL_MIN_LEVEL = 101
AGL_MAX_LEVEL = 102
AGL_COLOR_MODES = 103
AGL_ACCUM_MODES = 104
AGL_DEPTH_MODES = 105
AGL_STENCIL_MODES = 106
AGL_MAX_AUX_BUFFERS = 107
AGL_VIDEO_MEMORY = 120
AGL_TEXTURE_MEMORY = 121
AGL_RENDERER_COUNT = 128
AGL_SWAP_RECT = 200
AGL_BUFFER_RECT = 202
AGL_SWAP_LIMIT = 203
AGL_COLORMAP_TRACKING = 210
AGL_COLORMAP_ENTRY = 212
AGL_RASTERIZATION = 220
AGL_SWAP_INTERVAL = 222
AGL_STATE_VALIDATION = 230
AGL_BUFFER_NAME = 231
AGL_ORDER_CONTEXT_TO_FRONT = 232
AGL_CONTEXT_SURFACE_ID = 233
AGL_CONTEXT_DISPLAY_ID = 234
AGL_SURFACE_ORDER = 235
AGL_SURFACE_OPACITY = 236
AGL_CLIP_REGION = 254
AGL_FS_CAPTURE_SINGLE = 255
AGL_SURFACE_BACKING_SIZE = 304
AGL_ENABLE_SURFACE_BACKING_SIZE = 305
AGL_SURFACE_VOLATILE = 306
AGL_FORMAT_CACHE_SIZE = 501
AGL_CLEAR_FORMAT_CACHE = 502
AGL_RETAIN_RENDERERS = 503
AGL_MONOSCOPIC_BIT = 1
AGL_STEREOSCOPIC_BIT = 2
AGL_SINGLEBUFFER_BIT = 4
AGL_DOUBLEBUFFER_BIT = 8
AGL_0_BIT = 1
AGL_1_BIT = 2
AGL_2_BIT = 4
AGL_3_BIT = 8
AGL_4_BIT = 16
AGL_5_BIT = 32
AGL_6_BIT = 64
AGL_8_BIT = 128
AGL_10_BIT = 256
AGL_12_BIT = 512
AGL_16_BIT = 1024
AGL_24_BIT = 2048
AGL_32_BIT = 4096
AGL_48_BIT = 8192
AGL_64_BIT = 16384
AGL_96_BIT = 32768
AGL_128_BIT = 65536
AGL_RGB8_BIT = 1
AGL_RGB8_A8_BIT = 2
AGL_BGR233_BIT = 4
AGL_BGR233_A8_BIT = 8
AGL_RGB332_BIT = 16
AGL_RGB332_A8_BIT = 32
AGL_RGB444_BIT = 64
AGL_ARGB4444_BIT = 128
AGL_RGB444_A8_BIT = 256
AGL_RGB555_BIT = 512
AGL_ARGB1555_BIT = 1024
AGL_RGB555_A8_BIT = 2048
AGL_RGB565_BIT = 4096
AGL_RGB565_A8_BIT = 8192
AGL_RGB888_BIT = 16384
AGL_ARGB8888_BIT = 32768
AGL_RGB888_A8_BIT = 65536
AGL_RGB101010_BIT = 131072
AGL_ARGB2101010_BIT = 262144
AGL_RGB101010_A8_BIT = 524288
AGL_RGB121212_BIT = 1048576
AGL_ARGB12121212_BIT = 2097152
AGL_RGB161616_BIT = 4194304
AGL_ARGB16161616_BIT = 8388608
AGL_INDEX8_BIT = 536870912
AGL_INDEX16_BIT = 1073741824
AGL_RGBFLOAT64_BIT = 16777216
AGL_RGBAFLOAT64_BIT = 33554432
AGL_RGBFLOAT128_BIT = 67108864
AGL_RGBAFLOAT128_BIT = 134217728
AGL_RGBFLOAT256_BIT = 268435456
AGL_RGBAFLOAT256_BIT = 536870912
AGL_NO_ERROR = 0
AGL_BAD_ATTRIBUTE = 10000
AGL_BAD_PROPERTY = 10001
AGL_BAD_PIXELFMT = 10002
AGL_BAD_RENDINFO = 10003
AGL_BAD_CONTEXT = 10004
AGL_BAD_DRAWABLE = 10005
AGL_BAD_GDEV = 10006
AGL_BAD_STATE = 10007
AGL_BAD_VALUE = 10008
AGL_BAD_MATCH = 10009
AGL_BAD_ENUM = 10010
AGL_BAD_OFFSCREEN = 10011
AGL_BAD_FULLSCREEN = 10012
AGL_BAD_WINDOW = 10013
AGL_BAD_POINTER = 10014
AGL_BAD_MODULE = 10015
AGL_BAD_ALLOC = 10016
AGL_BAD_CONNECTION = 10017
GLint = c_long
aglChoosePixelFormat = _link_function('aglChoosePixelFormat', AGLPixelFormat, [POINTER(AGLDevice), GLint, POINTER(GLint)], None)
aglDestroyPixelFormat = _link_function('aglDestroyPixelFormat', None, [AGLPixelFormat], None)
aglNextPixelFormat = _link_function('aglNextPixelFormat', AGLPixelFormat, [AGLPixelFormat], None)
GLboolean = c_ubyte
aglDescribePixelFormat = _link_function('aglDescribePixelFormat', GLboolean, [AGLPixelFormat, GLint, POINTER(GLint)], None)
aglDevicesOfPixelFormat = _link_function('aglDevicesOfPixelFormat', POINTER(AGLDevice), [AGLPixelFormat, POINTER(GLint)], None)
aglQueryRendererInfo = _link_function('aglQueryRendererInfo', AGLRendererInfo, [POINTER(AGLDevice), GLint], None)
aglDestroyRendererInfo = _link_function('aglDestroyRendererInfo', None, [AGLRendererInfo], None)
aglNextRendererInfo = _link_function('aglNextRendererInfo', AGLRendererInfo, [AGLRendererInfo], None)
aglDescribeRenderer = _link_function('aglDescribeRenderer', GLboolean, [AGLRendererInfo, GLint, POINTER(GLint)], None)
aglCreateContext = _link_function('aglCreateContext', AGLContext, [AGLPixelFormat, AGLContext], None)
aglDestroyContext = _link_function('aglDestroyContext', GLboolean, [AGLContext], None)
GLuint = c_ulong
aglCopyContext = _link_function('aglCopyContext', GLboolean, [AGLContext, AGLContext, GLuint], None)
aglUpdateContext = _link_function('aglUpdateContext', GLboolean, [AGLContext], None)
aglSetCurrentContext = _link_function('aglSetCurrentContext', GLboolean, [AGLContext], None)
aglGetCurrentContext = _link_function('aglGetCurrentContext', AGLContext, [], None)
aglSetDrawable = _link_function('aglSetDrawable', GLboolean, [AGLContext, AGLDrawable], None)
GLsizei = c_long
GLvoid = None
aglSetOffScreen = _link_function('aglSetOffScreen', GLboolean, [AGLContext, GLsizei, GLsizei, GLsizei, POINTER(GLvoid)], None)
aglSetFullScreen = _link_function('aglSetFullScreen', GLboolean, [AGLContext, GLsizei, GLsizei, GLsizei, GLint], None)
aglGetDrawable = _link_function('aglGetDrawable', AGLDrawable, [AGLContext], None)
aglSetVirtualScreen = _link_function('aglSetVirtualScreen', GLboolean, [AGLContext, GLint], None)
aglGetVirtualScreen = _link_function('aglGetVirtualScreen', GLint, [AGLContext], None)
aglGetVersion = _link_function('aglGetVersion', None, [POINTER(GLint), POINTER(GLint)], None)
GLenum = c_ulong
aglConfigure = _link_function('aglConfigure', GLboolean, [GLenum, GLuint], None)
aglSwapBuffers = _link_function('aglSwapBuffers', None, [AGLContext], None)
aglEnable = _link_function('aglEnable', GLboolean, [AGLContext, GLenum], None)
aglDisable = _link_function('aglDisable', GLboolean, [AGLContext, GLenum], None)
aglIsEnabled = _link_function('aglIsEnabled', GLboolean, [AGLContext, GLenum], None)
aglSetInteger = _link_function('aglSetInteger', GLboolean, [AGLContext, GLenum, POINTER(GLint)], None)
aglGetInteger = _link_function('aglGetInteger', GLboolean, [AGLContext, GLenum, POINTER(GLint)], None)
Style = c_ubyte
aglUseFont = _link_function('aglUseFont', GLboolean, [AGLContext, GLint, Style, GLint, GLint, GLint, GLint], None)
aglGetError = _link_function('aglGetError', GLenum, [], None)
GLubyte = c_ubyte
aglErrorString = _link_function('aglErrorString', POINTER(GLubyte), [GLenum], None)
aglResetLibrary = _link_function('aglResetLibrary', None, [], None)
aglSurfaceTexture = _link_function('aglSurfaceTexture', None, [AGLContext, GLenum, GLenum, AGLContext], None)
aglCreatePBuffer = _link_function('aglCreatePBuffer', GLboolean, [GLint, GLint, GLenum, GLenum, c_long, POINTER(AGLPbuffer)], None)
aglDestroyPBuffer = _link_function('aglDestroyPBuffer', GLboolean, [AGLPbuffer], None)
aglDescribePBuffer = _link_function('aglDescribePBuffer', GLboolean, [AGLPbuffer, POINTER(GLint), POINTER(GLint), POINTER(GLenum), POINTER(GLenum), POINTER(GLint)], None)
aglTexImagePBuffer = _link_function('aglTexImagePBuffer', GLboolean, [AGLContext, AGLPbuffer, GLint], None)
aglSetPBuffer = _link_function('aglSetPBuffer', GLboolean, [AGLContext, AGLPbuffer, GLint, GLint, GLint], None)
aglGetPBuffer = _link_function('aglGetPBuffer', GLboolean, [AGLContext, POINTER(AGLPbuffer), POINTER(GLint), POINTER(GLint), POINTER(GLint)], None)
aglGetCGLContext = _link_function('aglGetCGLContext', GLboolean, [AGLContext, POINTER(POINTER(None))], None)
aglGetCGLPixelFormat = _link_function('aglGetCGLPixelFormat', GLboolean, [AGLPixelFormat, POINTER(POINTER(None))], None)
__all__ = [
 'AGL_VERSION_2_0', 'AGLDevice', 'AGLDrawable', 'AGLRendererInfo', 
 'AGLPixelFormat', 
 'AGLContext', 'AGLPbuffer', 'AGL_NONE', 'AGL_ALL_RENDERERS', 
 'AGL_BUFFER_SIZE', 
 'AGL_LEVEL', 'AGL_RGBA', 'AGL_DOUBLEBUFFER', 'AGL_STEREO', 
 'AGL_AUX_BUFFERS', 
 'AGL_RED_SIZE', 'AGL_GREEN_SIZE', 'AGL_BLUE_SIZE', 
 'AGL_ALPHA_SIZE', 'AGL_DEPTH_SIZE', 
 'AGL_STENCIL_SIZE', 'AGL_ACCUM_RED_SIZE', 
 'AGL_ACCUM_GREEN_SIZE', 'AGL_ACCUM_BLUE_SIZE', 
 'AGL_ACCUM_ALPHA_SIZE', 
 'AGL_PIXEL_SIZE', 'AGL_MINIMUM_POLICY', 'AGL_MAXIMUM_POLICY', 
 'AGL_OFFSCREEN', 
 'AGL_FULLSCREEN', 'AGL_SAMPLE_BUFFERS_ARB', 'AGL_SAMPLES_ARB', 
 'AGL_AUX_DEPTH_STENCIL', 
 'AGL_COLOR_FLOAT', 'AGL_MULTISAMPLE', 
 'AGL_SUPERSAMPLE', 'AGL_SAMPLE_ALPHA', 
 'AGL_RENDERER_ID', 
 'AGL_SINGLE_RENDERER', 'AGL_NO_RECOVERY', 'AGL_ACCELERATED', 
 'AGL_CLOSEST_POLICY', 
 'AGL_ROBUST', 'AGL_BACKING_STORE', 'AGL_MP_SAFE', 
 'AGL_WINDOW', 'AGL_MULTISCREEN', 
 'AGL_VIRTUAL_SCREEN', 'AGL_COMPLIANT', 
 'AGL_PBUFFER', 'AGL_BUFFER_MODES', 
 'AGL_MIN_LEVEL', 'AGL_MAX_LEVEL', 
 'AGL_COLOR_MODES', 'AGL_ACCUM_MODES', 
 'AGL_DEPTH_MODES', 'AGL_STENCIL_MODES', 
 'AGL_MAX_AUX_BUFFERS', 'AGL_VIDEO_MEMORY', 
 'AGL_TEXTURE_MEMORY', 
 'AGL_RENDERER_COUNT', 'AGL_SWAP_RECT', 'AGL_BUFFER_RECT', 
 'AGL_SWAP_LIMIT', 
 'AGL_COLORMAP_TRACKING', 'AGL_COLORMAP_ENTRY', 'AGL_RASTERIZATION', 
 'AGL_SWAP_INTERVAL', 
 'AGL_STATE_VALIDATION', 'AGL_BUFFER_NAME', 
 'AGL_ORDER_CONTEXT_TO_FRONT', 
 'AGL_CONTEXT_SURFACE_ID', 
 'AGL_CONTEXT_DISPLAY_ID', 'AGL_SURFACE_ORDER', 
 'AGL_SURFACE_OPACITY', 
 'AGL_CLIP_REGION', 'AGL_FS_CAPTURE_SINGLE', 'AGL_SURFACE_BACKING_SIZE', 
 'AGL_ENABLE_SURFACE_BACKING_SIZE', 
 'AGL_SURFACE_VOLATILE', 
 'AGL_FORMAT_CACHE_SIZE', 'AGL_CLEAR_FORMAT_CACHE', 
 'AGL_RETAIN_RENDERERS', 
 'AGL_MONOSCOPIC_BIT', 'AGL_STEREOSCOPIC_BIT', 'AGL_SINGLEBUFFER_BIT', 
 'AGL_DOUBLEBUFFER_BIT', 
 'AGL_0_BIT', 'AGL_1_BIT', 'AGL_2_BIT', 'AGL_3_BIT', 
 'AGL_4_BIT', 'AGL_5_BIT', 
 'AGL_6_BIT', 'AGL_8_BIT', 'AGL_10_BIT', 
 'AGL_12_BIT', 'AGL_16_BIT', 'AGL_24_BIT', 
 'AGL_32_BIT', 'AGL_48_BIT', 
 'AGL_64_BIT', 'AGL_96_BIT', 'AGL_128_BIT', 
 'AGL_RGB8_BIT', 'AGL_RGB8_A8_BIT', 
 'AGL_BGR233_BIT', 'AGL_BGR233_A8_BIT', 
 'AGL_RGB332_BIT', 'AGL_RGB332_A8_BIT', 
 'AGL_RGB444_BIT', 'AGL_ARGB4444_BIT', 
 'AGL_RGB444_A8_BIT', 'AGL_RGB555_BIT', 
 'AGL_ARGB1555_BIT', 'AGL_RGB555_A8_BIT', 
 'AGL_RGB565_BIT', 
 'AGL_RGB565_A8_BIT', 'AGL_RGB888_BIT', 'AGL_ARGB8888_BIT', 
 'AGL_RGB888_A8_BIT', 
 'AGL_RGB101010_BIT', 'AGL_ARGB2101010_BIT', 
 'AGL_RGB101010_A8_BIT', 'AGL_RGB121212_BIT', 
 'AGL_ARGB12121212_BIT', 
 'AGL_RGB161616_BIT', 'AGL_ARGB16161616_BIT', 'AGL_INDEX8_BIT', 
 'AGL_INDEX16_BIT', 
 'AGL_RGBFLOAT64_BIT', 'AGL_RGBAFLOAT64_BIT', 
 'AGL_RGBFLOAT128_BIT', 'AGL_RGBAFLOAT128_BIT', 
 'AGL_RGBFLOAT256_BIT', 
 'AGL_RGBAFLOAT256_BIT', 'AGL_NO_ERROR', 'AGL_BAD_ATTRIBUTE', 
 'AGL_BAD_PROPERTY', 
 'AGL_BAD_PIXELFMT', 'AGL_BAD_RENDINFO', 'AGL_BAD_CONTEXT', 
 'AGL_BAD_DRAWABLE', 
 'AGL_BAD_GDEV', 'AGL_BAD_STATE', 'AGL_BAD_VALUE', 
 'AGL_BAD_MATCH', 'AGL_BAD_ENUM', 
 'AGL_BAD_OFFSCREEN', 'AGL_BAD_FULLSCREEN', 
 'AGL_BAD_WINDOW', 'AGL_BAD_POINTER', 
 'AGL_BAD_MODULE', 'AGL_BAD_ALLOC', 
 'AGL_BAD_CONNECTION', 'aglChoosePixelFormat', 
 'aglDestroyPixelFormat', 
 'aglNextPixelFormat', 'aglDescribePixelFormat', 
 'aglDevicesOfPixelFormat', 
 'aglQueryRendererInfo', 'aglDestroyRendererInfo', 
 'aglNextRendererInfo', 
 'aglDescribeRenderer', 'aglCreateContext', 'aglDestroyContext', 
 'aglCopyContext', 
 'aglUpdateContext', 'aglSetCurrentContext', 
 'aglGetCurrentContext', 'aglSetDrawable', 
 'aglSetOffScreen', 
 'aglSetFullScreen', 'aglGetDrawable', 'aglSetVirtualScreen', 
 'aglGetVirtualScreen', 
 'aglGetVersion', 'aglConfigure', 'aglSwapBuffers', 
 'aglEnable', 'aglDisable', 
 'aglIsEnabled', 'aglSetInteger', 'aglGetInteger', 
 'aglUseFont', 'aglGetError', 
 'aglErrorString', 'aglResetLibrary', 
 'aglSurfaceTexture', 'aglCreatePBuffer', 
 'aglDestroyPBuffer', 
 'aglDescribePBuffer', 'aglTexImagePBuffer', 'aglSetPBuffer', 
 'aglGetPBuffer', 
 'aglGetCGLContext', 'aglGetCGLPixelFormat']
# okay decompiling out\pyglet.gl.agl.pyc
