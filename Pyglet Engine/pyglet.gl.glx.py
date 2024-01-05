# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.glx
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from pyglet.gl.lib import link_GLX as _link_function
from pyglet.gl.lib import c_ptrdiff_t, c_void
if not _link_function:
    raise ImportError('libGL.so is not available.')
import pyglet.libs.x11.xlib
GLX_VERSION_1_1 = 1
GLX_VERSION_1_2 = 1
GLX_VERSION_1_3 = 1
GLX_VERSION_1_4 = 1
GLX_USE_GL = 1
GLX_BUFFER_SIZE = 2
GLX_LEVEL = 3
GLX_RGBA = 4
GLX_DOUBLEBUFFER = 5
GLX_STEREO = 6
GLX_AUX_BUFFERS = 7
GLX_RED_SIZE = 8
GLX_GREEN_SIZE = 9
GLX_BLUE_SIZE = 10
GLX_ALPHA_SIZE = 11
GLX_DEPTH_SIZE = 12
GLX_STENCIL_SIZE = 13
GLX_ACCUM_RED_SIZE = 14
GLX_ACCUM_GREEN_SIZE = 15
GLX_ACCUM_BLUE_SIZE = 16
GLX_ACCUM_ALPHA_SIZE = 17
GLX_BAD_SCREEN = 1
GLX_BAD_ATTRIBUTE = 2
GLX_NO_EXTENSION = 3
GLX_BAD_VISUAL = 4
GLX_BAD_CONTEXT = 5
GLX_BAD_VALUE = 6
GLX_BAD_ENUM = 7
GLX_VENDOR = 1
GLX_VERSION = 2
GLX_EXTENSIONS = 3
GLX_CONFIG_CAVEAT = 32
GLX_DONT_CARE = 4294967295
GLX_X_VISUAL_TYPE = 34
GLX_TRANSPARENT_TYPE = 35
GLX_TRANSPARENT_INDEX_VALUE = 36
GLX_TRANSPARENT_RED_VALUE = 37
GLX_TRANSPARENT_GREEN_VALUE = 38
GLX_TRANSPARENT_BLUE_VALUE = 39
GLX_TRANSPARENT_ALPHA_VALUE = 40
GLX_WINDOW_BIT = 1
GLX_PIXMAP_BIT = 2
GLX_PBUFFER_BIT = 4
GLX_AUX_BUFFERS_BIT = 16
GLX_FRONT_LEFT_BUFFER_BIT = 1
GLX_FRONT_RIGHT_BUFFER_BIT = 2
GLX_BACK_LEFT_BUFFER_BIT = 4
GLX_BACK_RIGHT_BUFFER_BIT = 8
GLX_DEPTH_BUFFER_BIT = 32
GLX_STENCIL_BUFFER_BIT = 64
GLX_ACCUM_BUFFER_BIT = 128
GLX_NONE = 32768
GLX_SLOW_CONFIG = 32769
GLX_TRUE_COLOR = 32770
GLX_DIRECT_COLOR = 32771
GLX_PSEUDO_COLOR = 32772
GLX_STATIC_COLOR = 32773
GLX_GRAY_SCALE = 32774
GLX_STATIC_GRAY = 32775
GLX_TRANSPARENT_RGB = 32776
GLX_TRANSPARENT_INDEX = 32777
GLX_VISUAL_ID = 32779
GLX_SCREEN = 32780
GLX_NON_CONFORMANT_CONFIG = 32781
GLX_DRAWABLE_TYPE = 32784
GLX_RENDER_TYPE = 32785
GLX_X_RENDERABLE = 32786
GLX_FBCONFIG_ID = 32787
GLX_RGBA_TYPE = 32788
GLX_COLOR_INDEX_TYPE = 32789
GLX_MAX_PBUFFER_WIDTH = 32790
GLX_MAX_PBUFFER_HEIGHT = 32791
GLX_MAX_PBUFFER_PIXELS = 32792
GLX_PRESERVED_CONTENTS = 32795
GLX_LARGEST_PBUFFER = 32796
GLX_WIDTH = 32797
GLX_HEIGHT = 32798
GLX_EVENT_MASK = 32799
GLX_DAMAGED = 32800
GLX_SAVED = 32801
GLX_WINDOW = 32802
GLX_PBUFFER = 32803
GLX_PBUFFER_HEIGHT = 32832
GLX_PBUFFER_WIDTH = 32833
GLX_RGBA_BIT = 1
GLX_COLOR_INDEX_BIT = 2
GLX_PBUFFER_CLOBBER_MASK = 134217728
GLX_SAMPLE_BUFFERS = 100000
GLX_SAMPLES = 100001

class struct___GLXcontextRec(Structure):
    __slots__ = []


struct___GLXcontextRec._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct___GLXcontextRec(Structure):
    __slots__ = []


struct___GLXcontextRec._fields_ = [
 (
  '_opaque_struct', c_int)]
GLXContext = POINTER(struct___GLXcontextRec)
XID = pyglet.libs.x11.xlib.XID
GLXPixmap = XID
GLXDrawable = XID

class struct___GLXFBConfigRec(Structure):
    __slots__ = []


struct___GLXFBConfigRec._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct___GLXFBConfigRec(Structure):
    __slots__ = []


struct___GLXFBConfigRec._fields_ = [
 (
  '_opaque_struct', c_int)]
GLXFBConfig = POINTER(struct___GLXFBConfigRec)
GLXFBConfigID = XID
GLXContextID = XID
GLXWindow = XID
GLXPbuffer = XID
XVisualInfo = pyglet.libs.x11.xlib.XVisualInfo
Display = pyglet.libs.x11.xlib.Display
glXChooseVisual = _link_function('glXChooseVisual', POINTER(XVisualInfo), [POINTER(Display), c_int, POINTER(c_int)], 'H')
glXCreateContext = _link_function('glXCreateContext', GLXContext, [POINTER(Display), POINTER(XVisualInfo), GLXContext, c_int], 'H')
glXDestroyContext = _link_function('glXDestroyContext', None, [POINTER(Display), GLXContext], 'H')
glXMakeCurrent = _link_function('glXMakeCurrent', c_int, [POINTER(Display), GLXDrawable, GLXContext], 'H')
glXCopyContext = _link_function('glXCopyContext', None, [POINTER(Display), GLXContext, GLXContext, c_ulong], 'H')
glXSwapBuffers = _link_function('glXSwapBuffers', None, [POINTER(Display), GLXDrawable], 'H')
Pixmap = pyglet.libs.x11.xlib.Pixmap
glXCreateGLXPixmap = _link_function('glXCreateGLXPixmap', GLXPixmap, [POINTER(Display), POINTER(XVisualInfo), Pixmap], 'H')
glXDestroyGLXPixmap = _link_function('glXDestroyGLXPixmap', None, [POINTER(Display), GLXPixmap], 'H')
glXQueryExtension = _link_function('glXQueryExtension', c_int, [POINTER(Display), POINTER(c_int), POINTER(c_int)], 'H')
glXQueryVersion = _link_function('glXQueryVersion', c_int, [POINTER(Display), POINTER(c_int), POINTER(c_int)], 'H')
glXIsDirect = _link_function('glXIsDirect', c_int, [POINTER(Display), GLXContext], 'H')
glXGetConfig = _link_function('glXGetConfig', c_int, [POINTER(Display), POINTER(XVisualInfo), c_int, POINTER(c_int)], 'H')
glXGetCurrentContext = _link_function('glXGetCurrentContext', GLXContext, [], 'H')
glXGetCurrentDrawable = _link_function('glXGetCurrentDrawable', GLXDrawable, [], 'H')
glXWaitGL = _link_function('glXWaitGL', None, [], 'H')
glXWaitX = _link_function('glXWaitX', None, [], 'H')
Font = pyglet.libs.x11.xlib.Font
glXUseXFont = _link_function('glXUseXFont', None, [Font, c_int, c_int, c_int], 'H')
glXQueryExtensionsString = _link_function('glXQueryExtensionsString', c_char_p, [POINTER(Display), c_int], 'H')
glXQueryServerString = _link_function('glXQueryServerString', c_char_p, [POINTER(Display), c_int, c_int], 'H')
glXGetClientString = _link_function('glXGetClientString', c_char_p, [POINTER(Display), c_int], 'H')
glXGetCurrentDisplay = _link_function('glXGetCurrentDisplay', POINTER(Display), [], 'H')
glXChooseFBConfig = _link_function('glXChooseFBConfig', POINTER(GLXFBConfig), [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)], 'H')
glXGetFBConfigAttrib = _link_function('glXGetFBConfigAttrib', c_int, [POINTER(Display), GLXFBConfig, c_int, POINTER(c_int)], 'H')
glXGetFBConfigs = _link_function('glXGetFBConfigs', POINTER(GLXFBConfig), [POINTER(Display), c_int, POINTER(c_int)], 'H')
glXGetVisualFromFBConfig = _link_function('glXGetVisualFromFBConfig', POINTER(XVisualInfo), [POINTER(Display), GLXFBConfig], 'H')
Window = pyglet.libs.x11.xlib.Window
glXCreateWindow = _link_function('glXCreateWindow', GLXWindow, [POINTER(Display), GLXFBConfig, Window, POINTER(c_int)], 'H')
glXDestroyWindow = _link_function('glXDestroyWindow', None, [POINTER(Display), GLXWindow], 'H')
glXCreatePixmap = _link_function('glXCreatePixmap', GLXPixmap, [POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int)], 'H')
glXDestroyPixmap = _link_function('glXDestroyPixmap', None, [POINTER(Display), GLXPixmap], 'H')
glXCreatePbuffer = _link_function('glXCreatePbuffer', GLXPbuffer, [POINTER(Display), GLXFBConfig, POINTER(c_int)], 'H')
glXDestroyPbuffer = _link_function('glXDestroyPbuffer', None, [POINTER(Display), GLXPbuffer], 'H')
glXQueryDrawable = _link_function('glXQueryDrawable', None, [POINTER(Display), GLXDrawable, c_int, POINTER(c_uint)], 'H')
glXCreateNewContext = _link_function('glXCreateNewContext', GLXContext, [POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int], 'H')
glXMakeContextCurrent = _link_function('glXMakeContextCurrent', c_int, [POINTER(Display), GLXDrawable, GLXDrawable, GLXContext], 'H')
glXGetCurrentReadDrawable = _link_function('glXGetCurrentReadDrawable', GLXDrawable, [], 'H')
glXQueryContext = _link_function('glXQueryContext', c_int, [POINTER(Display), GLXContext, c_int, POINTER(c_int)], 'H')
glXSelectEvent = _link_function('glXSelectEvent', None, [POINTER(Display), GLXDrawable, c_ulong], 'H')
glXGetSelectedEvent = _link_function('glXGetSelectedEvent', None, [POINTER(Display), GLXDrawable, POINTER(c_ulong)], 'H')
PFNGLXGETFBCONFIGSPROC = CFUNCTYPE(POINTER(GLXFBConfig), POINTER(Display), c_int, POINTER(c_int))
PFNGLXCHOOSEFBCONFIGPROC = CFUNCTYPE(POINTER(GLXFBConfig), POINTER(Display), c_int, POINTER(c_int), POINTER(c_int))
PFNGLXGETFBCONFIGATTRIBPROC = CFUNCTYPE(c_int, POINTER(Display), GLXFBConfig, c_int, POINTER(c_int))
PFNGLXGETVISUALFROMFBCONFIGPROC = CFUNCTYPE(POINTER(XVisualInfo), POINTER(Display), GLXFBConfig)
PFNGLXCREATEWINDOWPROC = CFUNCTYPE(GLXWindow, POINTER(Display), GLXFBConfig, Window, POINTER(c_int))
PFNGLXDESTROYWINDOWPROC = CFUNCTYPE(None, POINTER(Display), GLXWindow)
PFNGLXCREATEPIXMAPPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int))
PFNGLXDESTROYPIXMAPPROC = CFUNCTYPE(None, POINTER(Display), GLXPixmap)
PFNGLXCREATEPBUFFERPROC = CFUNCTYPE(GLXPbuffer, POINTER(Display), GLXFBConfig, POINTER(c_int))
PFNGLXDESTROYPBUFFERPROC = CFUNCTYPE(None, POINTER(Display), GLXPbuffer)
PFNGLXQUERYDRAWABLEPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int, POINTER(c_uint))
PFNGLXCREATENEWCONTEXTPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int)
PFNGLXMAKECONTEXTCURRENTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, GLXDrawable, GLXContext)
PFNGLXGETCURRENTREADDRAWABLEPROC = CFUNCTYPE(GLXDrawable)
PFNGLXGETCURRENTDISPLAYPROC = CFUNCTYPE(POINTER(Display))
PFNGLXQUERYCONTEXTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXContext, c_int, POINTER(c_int))
PFNGLXSELECTEVENTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_ulong)
PFNGLXGETSELECTEDEVENTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, POINTER(c_ulong))
GLX_ARB_get_proc_address = 1
__GLXextFuncPtr = CFUNCTYPE(None)
GLubyte = c_ubyte
glXGetProcAddressARB = _link_function('glXGetProcAddressARB', __GLXextFuncPtr, [POINTER(GLubyte)], 'ARB_get_proc_address')
glXGetProcAddress = _link_function('glXGetProcAddress', POINTER(CFUNCTYPE(None)), [POINTER(GLubyte)], 'ARB_get_proc_address')
PFNGLXGETPROCADDRESSPROC = CFUNCTYPE(__GLXextFuncPtr, POINTER(GLubyte))
GLsizei = c_int
GLfloat = c_float
glXAllocateMemoryNV = _link_function('glXAllocateMemoryNV', POINTER(c_void), [GLsizei, GLfloat, GLfloat, GLfloat], 'NV_vertex_array_range')
GLvoid = None
glXFreeMemoryNV = _link_function('glXFreeMemoryNV', None, [POINTER(GLvoid)], 'NV_vertex_array_range')
PFNGLXALLOCATEMEMORYNVPROC = CFUNCTYPE(POINTER(c_void), GLsizei, GLfloat, GLfloat, GLfloat)
PFNGLXFREEMEMORYNVPROC = CFUNCTYPE(None, POINTER(GLvoid))
GLX_MESA_allocate_memory = 1
glXAllocateMemoryMESA = _link_function('glXAllocateMemoryMESA', POINTER(c_void), [POINTER(Display), c_int, c_size_t, c_float, c_float, c_float], 'MESA_allocate_memory')
glXFreeMemoryMESA = _link_function('glXFreeMemoryMESA', None, [POINTER(Display), c_int, POINTER(None)], 'MESA_allocate_memory')
GLuint = c_uint
glXGetMemoryOffsetMESA = _link_function('glXGetMemoryOffsetMESA', GLuint, [POINTER(Display), c_int, POINTER(None)], 'MESA_allocate_memory')
PFNGLXALLOCATEMEMORYMESAPROC = CFUNCTYPE(POINTER(c_void), POINTER(Display), c_int, c_size_t, c_float, c_float, c_float)
PFNGLXFREEMEMORYMESAPROC = CFUNCTYPE(None, POINTER(Display), c_int, POINTER(None))
PFNGLXGETMEMORYOFFSETMESAPROC = CFUNCTYPE(GLuint, POINTER(Display), c_int, POINTER(None))
GLX_ARB_render_texture = 1
glXBindTexImageARB = _link_function('glXBindTexImageARB', c_int, [POINTER(Display), GLXPbuffer, c_int], 'ARB_render_texture')
glXReleaseTexImageARB = _link_function('glXReleaseTexImageARB', c_int, [POINTER(Display), GLXPbuffer, c_int], 'ARB_render_texture')
glXDrawableAttribARB = _link_function('glXDrawableAttribARB', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int)], 'ARB_render_texture')
GLX_MESA_swap_frame_usage = 1
glXGetFrameUsageMESA = _link_function('glXGetFrameUsageMESA', c_int, [POINTER(Display), GLXDrawable, POINTER(c_float)], 'MESA_swap_frame_usage')
glXBeginFrameTrackingMESA = _link_function('glXBeginFrameTrackingMESA', c_int, [POINTER(Display), GLXDrawable], 'MESA_swap_frame_usage')
glXEndFrameTrackingMESA = _link_function('glXEndFrameTrackingMESA', c_int, [POINTER(Display), GLXDrawable], 'MESA_swap_frame_usage')
glXQueryFrameTrackingMESA = _link_function('glXQueryFrameTrackingMESA', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_float)], 'MESA_swap_frame_usage')
PFNGLXGETFRAMEUSAGEMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_float))
PFNGLXBEGINFRAMETRACKINGMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable)
PFNGLXENDFRAMETRACKINGMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable)
PFNGLXQUERYFRAMETRACKINGMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_float))
GLX_MESA_swap_control = 1
glXSwapIntervalMESA = _link_function('glXSwapIntervalMESA', c_int, [c_uint], 'MESA_swap_control')
glXGetSwapIntervalMESA = _link_function('glXGetSwapIntervalMESA', c_int, [], 'MESA_swap_control')
PFNGLXSWAPINTERVALMESAPROC = CFUNCTYPE(c_int, c_uint)
PFNGLXGETSWAPINTERVALMESAPROC = CFUNCTYPE(c_int)

class struct_anon_111(Structure):
    __slots__ = [
     'event_type', 
     'draw_type', 
     'serial', 
     'send_event', 
     'display', 
     'drawable', 
     'buffer_mask', 
     'aux_buffer', 
     'x', 
     'y', 
     'width', 
     'height', 
     'count']


struct_anon_111._fields_ = [
 (
  'event_type', c_int),
 (
  'draw_type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'drawable', GLXDrawable),
 (
  'buffer_mask', c_uint),
 (
  'aux_buffer', c_uint),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'count', c_int)]
GLXPbufferClobberEvent = struct_anon_111

class struct___GLXEvent(Union):
    __slots__ = [
     'glxpbufferclobber',
     'pad']


struct___GLXEvent._fields_ = [
 (
  'glxpbufferclobber', GLXPbufferClobberEvent),
 (
  'pad', c_long * 24)]
GLXEvent = struct___GLXEvent
__all__ = [
 'GLX_VERSION_1_1', 'GLX_VERSION_1_2', 'GLX_VERSION_1_3', 
 'GLX_VERSION_1_4', 
 'GLX_USE_GL', 'GLX_BUFFER_SIZE', 'GLX_LEVEL', 'GLX_RGBA', 
 'GLX_DOUBLEBUFFER', 
 'GLX_STEREO', 'GLX_AUX_BUFFERS', 'GLX_RED_SIZE', 
 'GLX_GREEN_SIZE', 'GLX_BLUE_SIZE', 
 'GLX_ALPHA_SIZE', 'GLX_DEPTH_SIZE', 
 'GLX_STENCIL_SIZE', 'GLX_ACCUM_RED_SIZE', 
 'GLX_ACCUM_GREEN_SIZE', 
 'GLX_ACCUM_BLUE_SIZE', 'GLX_ACCUM_ALPHA_SIZE', 'GLX_BAD_SCREEN', 
 'GLX_BAD_ATTRIBUTE', 
 'GLX_NO_EXTENSION', 'GLX_BAD_VISUAL', 'GLX_BAD_CONTEXT', 
 'GLX_BAD_VALUE', 
 'GLX_BAD_ENUM', 'GLX_VENDOR', 'GLX_VERSION', 
 'GLX_EXTENSIONS', 'GLX_CONFIG_CAVEAT', 
 'GLX_DONT_CARE', 'GLX_X_VISUAL_TYPE', 
 'GLX_TRANSPARENT_TYPE', 'GLX_TRANSPARENT_INDEX_VALUE', 
 'GLX_TRANSPARENT_RED_VALUE', 
 'GLX_TRANSPARENT_GREEN_VALUE', 
 'GLX_TRANSPARENT_BLUE_VALUE', 'GLX_TRANSPARENT_ALPHA_VALUE', 
 'GLX_WINDOW_BIT', 
 'GLX_PIXMAP_BIT', 'GLX_PBUFFER_BIT', 'GLX_AUX_BUFFERS_BIT', 
 'GLX_FRONT_LEFT_BUFFER_BIT', 
 'GLX_FRONT_RIGHT_BUFFER_BIT', 
 'GLX_BACK_LEFT_BUFFER_BIT', 'GLX_BACK_RIGHT_BUFFER_BIT', 
 'GLX_DEPTH_BUFFER_BIT', 
 'GLX_STENCIL_BUFFER_BIT', 'GLX_ACCUM_BUFFER_BIT', 
 'GLX_NONE', 'GLX_SLOW_CONFIG', 
 'GLX_TRUE_COLOR', 'GLX_DIRECT_COLOR', 
 'GLX_PSEUDO_COLOR', 'GLX_STATIC_COLOR', 
 'GLX_GRAY_SCALE', 'GLX_STATIC_GRAY', 
 'GLX_TRANSPARENT_RGB', 'GLX_TRANSPARENT_INDEX', 
 'GLX_VISUAL_ID', 'GLX_SCREEN', 
 'GLX_NON_CONFORMANT_CONFIG', 'GLX_DRAWABLE_TYPE', 
 'GLX_RENDER_TYPE', 
 'GLX_X_RENDERABLE', 'GLX_FBCONFIG_ID', 'GLX_RGBA_TYPE', 
 'GLX_COLOR_INDEX_TYPE', 
 'GLX_MAX_PBUFFER_WIDTH', 'GLX_MAX_PBUFFER_HEIGHT', 
 'GLX_MAX_PBUFFER_PIXELS', 
 'GLX_PRESERVED_CONTENTS', 'GLX_LARGEST_PBUFFER', 
 'GLX_WIDTH', 'GLX_HEIGHT', 
 'GLX_EVENT_MASK', 'GLX_DAMAGED', 'GLX_SAVED', 
 'GLX_WINDOW', 'GLX_PBUFFER', 
 'GLX_PBUFFER_HEIGHT', 'GLX_PBUFFER_WIDTH', 
 'GLX_RGBA_BIT', 'GLX_COLOR_INDEX_BIT', 
 'GLX_PBUFFER_CLOBBER_MASK', 
 'GLX_SAMPLE_BUFFERS', 'GLX_SAMPLES', 'GLXContext', 
 'GLXPixmap', 'GLXDrawable', 
 'GLXFBConfig', 'GLXFBConfigID', 'GLXContextID', 
 'GLXWindow', 'GLXPbuffer', 
 'glXChooseVisual', 'glXCreateContext', 'glXDestroyContext', 
 'glXMakeCurrent', 
 'glXCopyContext', 'glXSwapBuffers', 'glXCreateGLXPixmap', 
 'glXDestroyGLXPixmap', 
 'glXQueryExtension', 'glXQueryVersion', 'glXIsDirect', 
 'glXGetConfig', 
 'glXGetCurrentContext', 'glXGetCurrentDrawable', 'glXWaitGL', 
 'glXWaitX', 
 'glXUseXFont', 'glXQueryExtensionsString', 'glXQueryServerString', 
 'glXGetClientString', 
 'glXGetCurrentDisplay', 'glXChooseFBConfig', 
 'glXGetFBConfigAttrib', 'glXGetFBConfigs', 
 'glXGetVisualFromFBConfig', 
 'glXCreateWindow', 'glXDestroyWindow', 'glXCreatePixmap', 
 'glXDestroyPixmap', 
 'glXCreatePbuffer', 'glXDestroyPbuffer', 'glXQueryDrawable', 
 'glXCreateNewContext', 
 'glXMakeContextCurrent', 'glXGetCurrentReadDrawable', 
 'glXQueryContext', 
 'glXSelectEvent', 'glXGetSelectedEvent', 
 'PFNGLXGETFBCONFIGSPROC', 'PFNGLXCHOOSEFBCONFIGPROC', 
 'PFNGLXGETFBCONFIGATTRIBPROC', 
 'PFNGLXGETVISUALFROMFBCONFIGPROC', 
 'PFNGLXCREATEWINDOWPROC', 'PFNGLXDESTROYWINDOWPROC', 
 'PFNGLXCREATEPIXMAPPROC', 
 'PFNGLXDESTROYPIXMAPPROC', 'PFNGLXCREATEPBUFFERPROC', 
 'PFNGLXDESTROYPBUFFERPROC', 
 'PFNGLXQUERYDRAWABLEPROC', 
 'PFNGLXCREATENEWCONTEXTPROC', 'PFNGLXMAKECONTEXTCURRENTPROC', 
 'PFNGLXGETCURRENTREADDRAWABLEPROC', 
 'PFNGLXGETCURRENTDISPLAYPROC', 
 'PFNGLXQUERYCONTEXTPROC', 'PFNGLXSELECTEVENTPROC', 
 'PFNGLXGETSELECTEDEVENTPROC', 
 'GLX_ARB_get_proc_address', '__GLXextFuncPtr', 
 'glXGetProcAddressARB', 'glXGetProcAddress', 
 'PFNGLXGETPROCADDRESSPROC', 
 'glXAllocateMemoryNV', 'glXFreeMemoryNV', 'PFNGLXALLOCATEMEMORYNVPROC', 
 'PFNGLXFREEMEMORYNVPROC', 
 'GLX_MESA_allocate_memory', 'glXAllocateMemoryMESA', 
 'glXFreeMemoryMESA', 
 'glXGetMemoryOffsetMESA', 'PFNGLXALLOCATEMEMORYMESAPROC', 
 'PFNGLXFREEMEMORYMESAPROC', 
 'PFNGLXGETMEMORYOFFSETMESAPROC', 
 'GLX_ARB_render_texture', 'glXBindTexImageARB', 
 'glXReleaseTexImageARB', 
 'glXDrawableAttribARB', 'GLX_MESA_swap_frame_usage', 
 'glXGetFrameUsageMESA', 
 'glXBeginFrameTrackingMESA', 'glXEndFrameTrackingMESA', 
 'glXQueryFrameTrackingMESA', 
 'PFNGLXGETFRAMEUSAGEMESAPROC', 
 'PFNGLXBEGINFRAMETRACKINGMESAPROC', 'PFNGLXENDFRAMETRACKINGMESAPROC', 
 'PFNGLXQUERYFRAMETRACKINGMESAPROC', 
 'GLX_MESA_swap_control', 
 'glXSwapIntervalMESA', 'glXGetSwapIntervalMESA', 
 'PFNGLXSWAPINTERVALMESAPROC', 
 'PFNGLXGETSWAPINTERVALMESAPROC', 'GLXPbufferClobberEvent', 
 'GLXEvent']
GLXBadContext = 0
GLXBadContextState = 1
GLXBadDrawable = 2
GLXBadPixmap = 3
GLXBadContextTag = 4
GLXBadCurrentWindow = 5
GLXBadRenderRequest = 6
GLXBadLargeRequest = 7
GLXUnsupportedPrivateRequest = 8
GLXBadFBConfig = 9
GLXBadPbuffer = 10
GLXBadCurrentDrawable = 11
GLXBadWindow = 12
__all__ += ['GLXBadContext', 'GLXBadContextState', 'GLXBadDrawable', 
 'GLXBadPixmap', 'GLXBadContextTag', 
 'GLXBadCurrentWindow', 
 'GLXBadRenderRequest', 'GLXBadLargeRequest', 'GLXUnsupportedPrivateRequest', 
 'GLXBadFBConfig', 
 'GLXBadPbuffer', 'GLXBadCurrentDrawable', 'GLXBadWindow']
# okay decompiling out\pyglet.gl.glx.pyc
