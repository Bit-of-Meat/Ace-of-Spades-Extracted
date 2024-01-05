# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.glxext_arb
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
from pyglet.gl.lib import link_GLX as _link_function
from pyglet.gl.lib import c_ptrdiff_t
if not hasattr(ctypes, 'c_int64'):
    c_int64 = c_long
    c_uint64 = c_ulong
import pyglet.libs.x11.xlib, pyglet.gl.glx
GLX_GLXEXT_VERSION = 32
GLX_SAMPLE_BUFFERS_ARB = 100000
GLX_SAMPLES_ARB = 100001
GLX_CONTEXT_ALLOW_BUFFER_BYTE_ORDER_MISMATCH_ARB = 8341
GLX_RGBA_FLOAT_TYPE_ARB = 8377
GLX_RGBA_FLOAT_BIT_ARB = 4
GLX_FRAMEBUFFER_SRGB_CAPABLE_ARB = 8370
GLX_CONTEXT_DEBUG_BIT_ARB = 1
GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB = 2
GLX_CONTEXT_MAJOR_VERSION_ARB = 8337
GLX_CONTEXT_MINOR_VERSION_ARB = 8338
GLX_CONTEXT_FLAGS_ARB = 8340
GLX_CONTEXT_CORE_PROFILE_BIT_ARB = 1
GLX_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB = 2
GLX_CONTEXT_PROFILE_MASK_ARB = 37158
GLX_CONTEXT_ROBUST_ACCESS_BIT_ARB = 4
GLX_LOSE_CONTEXT_ON_RESET_ARB = 33362
GLX_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB = 33366
GLX_NO_RESET_NOTIFICATION_ARB = 33377
GLX_SAMPLE_BUFFERS_SGIS = 100000
GLX_SAMPLES_SGIS = 100001
GLX_X_VISUAL_TYPE_EXT = 34
GLX_TRANSPARENT_TYPE_EXT = 35
GLX_TRANSPARENT_INDEX_VALUE_EXT = 36
GLX_TRANSPARENT_RED_VALUE_EXT = 37
GLX_TRANSPARENT_GREEN_VALUE_EXT = 38
GLX_TRANSPARENT_BLUE_VALUE_EXT = 39
GLX_TRANSPARENT_ALPHA_VALUE_EXT = 40
GLX_NONE_EXT = 32768
GLX_TRUE_COLOR_EXT = 32770
GLX_DIRECT_COLOR_EXT = 32771
GLX_PSEUDO_COLOR_EXT = 32772
GLX_STATIC_COLOR_EXT = 32773
GLX_GRAY_SCALE_EXT = 32774
GLX_STATIC_GRAY_EXT = 32775
GLX_TRANSPARENT_RGB_EXT = 32776
GLX_TRANSPARENT_INDEX_EXT = 32777
GLX_VISUAL_CAVEAT_EXT = 32
GLX_SLOW_VISUAL_EXT = 32769
GLX_NON_CONFORMANT_VISUAL_EXT = 32781
GLX_SHARE_CONTEXT_EXT = 32778
GLX_VISUAL_ID_EXT = 32779
GLX_SCREEN_EXT = 32780
GLX_WINDOW_BIT_SGIX = 1
GLX_PIXMAP_BIT_SGIX = 2
GLX_RGBA_BIT_SGIX = 1
GLX_COLOR_INDEX_BIT_SGIX = 2
GLX_DRAWABLE_TYPE_SGIX = 32784
GLX_RENDER_TYPE_SGIX = 32785
GLX_X_RENDERABLE_SGIX = 32786
GLX_FBCONFIG_ID_SGIX = 32787
GLX_RGBA_TYPE_SGIX = 32788
GLX_COLOR_INDEX_TYPE_SGIX = 32789
GLX_PBUFFER_BIT_SGIX = 4
GLX_BUFFER_CLOBBER_MASK_SGIX = 134217728
GLX_FRONT_LEFT_BUFFER_BIT_SGIX = 1
GLX_FRONT_RIGHT_BUFFER_BIT_SGIX = 2
GLX_BACK_LEFT_BUFFER_BIT_SGIX = 4
GLX_BACK_RIGHT_BUFFER_BIT_SGIX = 8
GLX_AUX_BUFFERS_BIT_SGIX = 16
GLX_DEPTH_BUFFER_BIT_SGIX = 32
GLX_STENCIL_BUFFER_BIT_SGIX = 64
GLX_ACCUM_BUFFER_BIT_SGIX = 128
GLX_SAMPLE_BUFFERS_BIT_SGIX = 256
GLX_MAX_PBUFFER_WIDTH_SGIX = 32790
GLX_MAX_PBUFFER_HEIGHT_SGIX = 32791
GLX_MAX_PBUFFER_PIXELS_SGIX = 32792
GLX_OPTIMAL_PBUFFER_WIDTH_SGIX = 32793
GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX = 32794
GLX_PRESERVED_CONTENTS_SGIX = 32795
GLX_LARGEST_PBUFFER_SGIX = 32796
GLX_WIDTH_SGIX = 32797
GLX_HEIGHT_SGIX = 32798
GLX_EVENT_MASK_SGIX = 32799
GLX_DAMAGED_SGIX = 32800
GLX_SAVED_SGIX = 32801
GLX_WINDOW_SGIX = 32802
GLX_PBUFFER_SGIX = 32803
GLX_SYNC_FRAME_SGIX = 0
GLX_SYNC_SWAP_SGIX = 1
GLX_DIGITAL_MEDIA_PBUFFER_SGIX = 32804
GLX_BLENDED_RGBA_SGIS = 32805
GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS = 32806
GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS = 32807
GLX_SAMPLE_BUFFERS_3DFX = 32848
GLX_SAMPLES_3DFX = 32849
GLX_3DFX_WINDOW_MODE_MESA = 1
GLX_3DFX_FULLSCREEN_MODE_MESA = 2
GLX_VISUAL_SELECT_GROUP_SGIX = 32808
GLX_SWAP_METHOD_OML = 32864
GLX_SWAP_EXCHANGE_OML = 32865
GLX_SWAP_COPY_OML = 32866
GLX_SWAP_UNDEFINED_OML = 32867
GLX_FLOAT_COMPONENTS_NV = 8368
GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX = 80
GLX_BAD_HYPERPIPE_CONFIG_SGIX = 91
GLX_BAD_HYPERPIPE_SGIX = 92
GLX_HYPERPIPE_DISPLAY_PIPE_SGIX = 1
GLX_HYPERPIPE_RENDER_PIPE_SGIX = 2
GLX_PIPE_RECT_SGIX = 1
GLX_PIPE_RECT_LIMITS_SGIX = 2
GLX_HYPERPIPE_STEREO_SGIX = 3
GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX = 4
GLX_HYPERPIPE_ID_SGIX = 32816
GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT = 8369
GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT = 8
GLX_FRAMEBUFFER_SRGB_CAPABLE_EXT = 8370
GLX_TEXTURE_1D_BIT_EXT = 1
GLX_TEXTURE_2D_BIT_EXT = 2
GLX_TEXTURE_RECTANGLE_BIT_EXT = 4
GLX_BIND_TO_TEXTURE_RGB_EXT = 8400
GLX_BIND_TO_TEXTURE_RGBA_EXT = 8401
GLX_BIND_TO_MIPMAP_TEXTURE_EXT = 8402
GLX_BIND_TO_TEXTURE_TARGETS_EXT = 8403
GLX_Y_INVERTED_EXT = 8404
GLX_TEXTURE_FORMAT_EXT = 8405
GLX_TEXTURE_TARGET_EXT = 8406
GLX_MIPMAP_TEXTURE_EXT = 8407
GLX_TEXTURE_FORMAT_NONE_EXT = 8408
GLX_TEXTURE_FORMAT_RGB_EXT = 8409
GLX_TEXTURE_FORMAT_RGBA_EXT = 8410
GLX_TEXTURE_1D_EXT = 8411
GLX_TEXTURE_2D_EXT = 8412
GLX_TEXTURE_RECTANGLE_EXT = 8413
GLX_FRONT_LEFT_EXT = 8414
GLX_FRONT_RIGHT_EXT = 8415
GLX_BACK_LEFT_EXT = 8416
GLX_BACK_RIGHT_EXT = 8417
GLX_FRONT_EXT = 8414
GLX_BACK_EXT = 8416
GLX_AUX0_EXT = 8418
GLX_AUX1_EXT = 8419
GLX_AUX2_EXT = 8420
GLX_AUX3_EXT = 8421
GLX_AUX4_EXT = 8422
GLX_AUX5_EXT = 8423
GLX_AUX6_EXT = 8424
GLX_AUX7_EXT = 8425
GLX_AUX8_EXT = 8426
GLX_AUX9_EXT = 8427
GLX_NUM_VIDEO_SLOTS_NV = 8432
GLX_VIDEO_OUT_COLOR_NV = 8387
GLX_VIDEO_OUT_ALPHA_NV = 8388
GLX_VIDEO_OUT_DEPTH_NV = 8389
GLX_VIDEO_OUT_COLOR_AND_ALPHA_NV = 8390
GLX_VIDEO_OUT_COLOR_AND_DEPTH_NV = 8391
GLX_VIDEO_OUT_FRAME_NV = 8392
GLX_VIDEO_OUT_FIELD_1_NV = 8393
GLX_VIDEO_OUT_FIELD_2_NV = 8394
GLX_VIDEO_OUT_STACKED_FIELDS_1_2_NV = 8395
GLX_VIDEO_OUT_STACKED_FIELDS_2_1_NV = 8396
GLX_DEVICE_ID_NV = 8397
GLX_UNIQUE_ID_NV = 8398
GLX_NUM_VIDEO_CAPTURE_SLOTS_NV = 8399
GLX_SWAP_INTERVAL_EXT = 8433
GLX_MAX_SWAP_INTERVAL_EXT = 8434
GLX_BUFFER_SWAP_COMPLETE_INTEL_MASK = 67108864
GLX_EXCHANGE_COMPLETE_INTEL = 33152
GLX_COPY_COMPLETE_INTEL = 33153
GLX_FLIP_COMPLETE_INTEL = 33154
GLX_COVERAGE_SAMPLES_NV = 100001
GLX_COLOR_SAMPLES_NV = 8371
GLX_GPU_VENDOR_AMD = 7936
GLX_GPU_RENDERER_STRING_AMD = 7937
GLX_GPU_OPENGL_VERSION_STRING_AMD = 7938
GLX_GPU_FASTEST_TARGET_GPUS_AMD = 8610
GLX_GPU_RAM_AMD = 8611
GLX_GPU_CLOCK_AMD = 8612
GLX_GPU_NUM_PIPES_AMD = 8613
GLX_GPU_NUM_SIMD_AMD = 8614
GLX_GPU_NUM_RB_AMD = 8615
GLX_GPU_NUM_SPI_AMD = 8616
GLX_CONTEXT_ES2_PROFILE_BIT_EXT = 4
XID = pyglet.libs.x11.xlib.XID
GLXVideoSourceSGIX = XID
GLXFBConfigIDSGIX = XID

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
GLXFBConfigSGIX = POINTER(struct___GLXFBConfigRec)
GLXPbufferSGIX = XID

class struct_anon_106(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'drawable', 
     'event_type', 
     'draw_type', 
     'mask', 
     'x', 
     'y', 
     'width', 
     'height', 
     'count']


Display = pyglet.libs.x11.xlib.Display
GLXDrawable = pyglet.gl.glx.GLXDrawable
struct_anon_106._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'drawable', GLXDrawable),
 (
  'event_type', c_int),
 (
  'draw_type', c_int),
 (
  'mask', c_uint),
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
GLXBufferClobberEventSGIX = struct_anon_106
GLXVideoDeviceNV = c_uint
GLXVideoCaptureDeviceNV = XID
GLX_ARB_multisample = 1
GLX_ARB_fbconfig_float = 1
GLX_ARB_framebuffer_sRGB = 1
GLX_ARB_create_context = 1
GLXContext = pyglet.gl.glx.GLXContext
GLXFBConfig = pyglet.gl.glx.GLXFBConfig
glXCreateContextAttribsARB = _link_function('glXCreateContextAttribsARB', GLXContext, [POINTER(Display), GLXFBConfig, GLXContext, c_int, POINTER(c_int)], 'ARB_create_context')
PFNGLXCREATECONTEXTATTRIBSARBPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXFBConfig, GLXContext, c_int, POINTER(c_int))
GLX_ARB_create_context_profile = 1
GLX_ARB_create_context_robustness = 1
GLX_SGIS_multisample = 1
GLX_EXT_visual_info = 1
GLX_SGI_swap_control = 1
glXSwapIntervalSGI = _link_function('glXSwapIntervalSGI', c_int, [c_int], 'SGI_swap_control')
PFNGLXSWAPINTERVALSGIPROC = CFUNCTYPE(c_int, c_int)
GLX_SGI_video_sync = 1
glXGetVideoSyncSGI = _link_function('glXGetVideoSyncSGI', c_int, [POINTER(c_uint)], 'SGI_video_sync')
glXWaitVideoSyncSGI = _link_function('glXWaitVideoSyncSGI', c_int, [c_int, c_int, POINTER(c_uint)], 'SGI_video_sync')
PFNGLXGETVIDEOSYNCSGIPROC = CFUNCTYPE(c_int, POINTER(c_uint))
PFNGLXWAITVIDEOSYNCSGIPROC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_uint))
GLX_SGI_make_current_read = 1
glXMakeCurrentReadSGI = _link_function('glXMakeCurrentReadSGI', c_int, [POINTER(Display), GLXDrawable, GLXDrawable, GLXContext], 'SGI_make_current_read')
glXGetCurrentReadDrawableSGI = _link_function('glXGetCurrentReadDrawableSGI', GLXDrawable, [], 'SGI_make_current_read')
PFNGLXMAKECURRENTREADSGIPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, GLXDrawable, GLXContext)
PFNGLXGETCURRENTREADDRAWABLESGIPROC = CFUNCTYPE(GLXDrawable)
GLX_SGIX_video_source = 1
GLX_EXT_visual_rating = 1
GLX_EXT_import_context = 1
glXGetCurrentDisplayEXT = _link_function('glXGetCurrentDisplayEXT', POINTER(Display), [], 'EXT_import_context')
glXQueryContextInfoEXT = _link_function('glXQueryContextInfoEXT', c_int, [POINTER(Display), GLXContext, c_int, POINTER(c_int)], 'EXT_import_context')
GLXContextID = pyglet.gl.glx.GLXContextID
glXGetContextIDEXT = _link_function('glXGetContextIDEXT', GLXContextID, [GLXContext], 'EXT_import_context')
glXImportContextEXT = _link_function('glXImportContextEXT', GLXContext, [POINTER(Display), GLXContextID], 'EXT_import_context')
glXFreeContextEXT = _link_function('glXFreeContextEXT', None, [POINTER(Display), GLXContext], 'EXT_import_context')
PFNGLXGETCURRENTDISPLAYEXTPROC = CFUNCTYPE(POINTER(Display))
PFNGLXQUERYCONTEXTINFOEXTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXContext, c_int, POINTER(c_int))
PFNGLXGETCONTEXTIDEXTPROC = CFUNCTYPE(GLXContextID, GLXContext)
PFNGLXIMPORTCONTEXTEXTPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXContextID)
PFNGLXFREECONTEXTEXTPROC = CFUNCTYPE(None, POINTER(Display), GLXContext)
GLX_SGIX_fbconfig = 1
glXGetFBConfigAttribSGIX = _link_function('glXGetFBConfigAttribSGIX', c_int, [POINTER(Display), GLXFBConfigSGIX, c_int, POINTER(c_int)], 'SGIX_fbconfig')
glXChooseFBConfigSGIX = _link_function('glXChooseFBConfigSGIX', POINTER(GLXFBConfigSGIX), [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)], 'SGIX_fbconfig')
GLXPixmap = pyglet.gl.glx.GLXPixmap
Pixmap = pyglet.libs.x11.xlib.Pixmap
glXCreateGLXPixmapWithConfigSGIX = _link_function('glXCreateGLXPixmapWithConfigSGIX', GLXPixmap, [POINTER(Display), GLXFBConfigSGIX, Pixmap], 'SGIX_fbconfig')
glXCreateContextWithConfigSGIX = _link_function('glXCreateContextWithConfigSGIX', GLXContext, [POINTER(Display), GLXFBConfigSGIX, c_int, GLXContext, c_int], 'SGIX_fbconfig')
XVisualInfo = pyglet.libs.x11.xlib.XVisualInfo
glXGetVisualFromFBConfigSGIX = _link_function('glXGetVisualFromFBConfigSGIX', POINTER(XVisualInfo), [POINTER(Display), GLXFBConfigSGIX], 'SGIX_fbconfig')
glXGetFBConfigFromVisualSGIX = _link_function('glXGetFBConfigFromVisualSGIX', GLXFBConfigSGIX, [POINTER(Display), POINTER(XVisualInfo)], 'SGIX_fbconfig')
PFNGLXGETFBCONFIGATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), GLXFBConfigSGIX, c_int, POINTER(c_int))
PFNGLXCHOOSEFBCONFIGSGIXPROC = CFUNCTYPE(POINTER(GLXFBConfigSGIX), POINTER(Display), c_int, POINTER(c_int), POINTER(c_int))
PFNGLXCREATEGLXPIXMAPWITHCONFIGSGIXPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), GLXFBConfigSGIX, Pixmap)
PFNGLXCREATECONTEXTWITHCONFIGSGIXPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXFBConfigSGIX, c_int, GLXContext, c_int)
PFNGLXGETVISUALFROMFBCONFIGSGIXPROC = CFUNCTYPE(POINTER(XVisualInfo), POINTER(Display), GLXFBConfigSGIX)
PFNGLXGETFBCONFIGFROMVISUALSGIXPROC = CFUNCTYPE(GLXFBConfigSGIX, POINTER(Display), POINTER(XVisualInfo))
GLX_SGIX_pbuffer = 1
glXCreateGLXPbufferSGIX = _link_function('glXCreateGLXPbufferSGIX', GLXPbufferSGIX, [POINTER(Display), GLXFBConfigSGIX, c_uint, c_uint, POINTER(c_int)], 'SGIX_pbuffer')
glXDestroyGLXPbufferSGIX = _link_function('glXDestroyGLXPbufferSGIX', None, [POINTER(Display), GLXPbufferSGIX], 'SGIX_pbuffer')
glXQueryGLXPbufferSGIX = _link_function('glXQueryGLXPbufferSGIX', c_int, [POINTER(Display), GLXPbufferSGIX, c_int, POINTER(c_uint)], 'SGIX_pbuffer')
glXSelectEventSGIX = _link_function('glXSelectEventSGIX', None, [POINTER(Display), GLXDrawable, c_ulong], 'SGIX_pbuffer')
glXGetSelectedEventSGIX = _link_function('glXGetSelectedEventSGIX', None, [POINTER(Display), GLXDrawable, POINTER(c_ulong)], 'SGIX_pbuffer')
PFNGLXCREATEGLXPBUFFERSGIXPROC = CFUNCTYPE(GLXPbufferSGIX, POINTER(Display), GLXFBConfigSGIX, c_uint, c_uint, POINTER(c_int))
PFNGLXDESTROYGLXPBUFFERSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXPbufferSGIX)
PFNGLXQUERYGLXPBUFFERSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), GLXPbufferSGIX, c_int, POINTER(c_uint))
PFNGLXSELECTEVENTSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_ulong)
PFNGLXGETSELECTEDEVENTSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, POINTER(c_ulong))
GLX_SGI_cushion = 1
Window = pyglet.libs.x11.xlib.Window
glXCushionSGI = _link_function('glXCushionSGI', None, [POINTER(Display), Window, c_float], 'SGI_cushion')
PFNGLXCUSHIONSGIPROC = CFUNCTYPE(None, POINTER(Display), Window, c_float)
GLX_SGIX_video_resize = 1
glXBindChannelToWindowSGIX = _link_function('glXBindChannelToWindowSGIX', c_int, [POINTER(Display), c_int, c_int, Window], 'SGIX_video_resize')
glXChannelRectSGIX = _link_function('glXChannelRectSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, c_int, c_int, c_int], 'SGIX_video_resize')
glXQueryChannelRectSGIX = _link_function('glXQueryChannelRectSGIX', c_int, [POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)], 'SGIX_video_resize')
glXQueryChannelDeltasSGIX = _link_function('glXQueryChannelDeltasSGIX', c_int, [POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)], 'SGIX_video_resize')
GLenum = c_uint
glXChannelRectSyncSGIX = _link_function('glXChannelRectSyncSGIX', c_int, [POINTER(Display), c_int, c_int, GLenum], 'SGIX_video_resize')
PFNGLXBINDCHANNELTOWINDOWSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, Window)
PFNGLXCHANNELRECTSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, c_int, c_int, c_int)
PFNGLXQUERYCHANNELRECTSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
PFNGLXQUERYCHANNELDELTASSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
PFNGLXCHANNELRECTSYNCSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, GLenum)
GLX_SGIX_dmbuffer = 1
GLX_SGIX_swap_group = 1
glXJoinSwapGroupSGIX = _link_function('glXJoinSwapGroupSGIX', None, [POINTER(Display), GLXDrawable, GLXDrawable], 'SGIX_swap_group')
PFNGLXJOINSWAPGROUPSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, GLXDrawable)
GLX_SGIX_swap_barrier = 1
glXBindSwapBarrierSGIX = _link_function('glXBindSwapBarrierSGIX', None, [POINTER(Display), GLXDrawable, c_int], 'SGIX_swap_barrier')
glXQueryMaxSwapBarriersSGIX = _link_function('glXQueryMaxSwapBarriersSGIX', c_int, [POINTER(Display), c_int, POINTER(c_int)], 'SGIX_swap_barrier')
PFNGLXBINDSWAPBARRIERSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int)
PFNGLXQUERYMAXSWAPBARRIERSSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, POINTER(c_int))
GLX_SUN_get_transparent_index = 1
glXGetTransparentIndexSUN = _link_function('glXGetTransparentIndexSUN', c_int, [POINTER(Display), Window, Window, POINTER(c_long)], 'SUN_get_transparent_index')
PFNGLXGETTRANSPARENTINDEXSUNPROC = CFUNCTYPE(c_int, POINTER(Display), Window, Window, POINTER(c_long))
GLX_MESA_copy_sub_buffer = 1
glXCopySubBufferMESA = _link_function('glXCopySubBufferMESA', None, [POINTER(Display), GLXDrawable, c_int, c_int, c_int, c_int], 'MESA_copy_sub_buffer')
PFNGLXCOPYSUBBUFFERMESAPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int, c_int, c_int, c_int)
GLX_MESA_pixmap_colormap = 1
Colormap = pyglet.libs.x11.xlib.Colormap
glXCreateGLXPixmapMESA = _link_function('glXCreateGLXPixmapMESA', GLXPixmap, [POINTER(Display), POINTER(XVisualInfo), Pixmap, Colormap], 'MESA_pixmap_colormap')
PFNGLXCREATEGLXPIXMAPMESAPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), POINTER(XVisualInfo), Pixmap, Colormap)
GLX_MESA_release_buffers = 1
glXReleaseBuffersMESA = _link_function('glXReleaseBuffersMESA', c_int, [POINTER(Display), GLXDrawable], 'MESA_release_buffers')
PFNGLXRELEASEBUFFERSMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable)
GLX_MESA_set_3dfx_mode = 1
glXSet3DfxModeMESA = _link_function('glXSet3DfxModeMESA', c_int, [c_int], 'MESA_set_3dfx_mode')
PFNGLXSET3DFXMODEMESAPROC = CFUNCTYPE(c_int, c_int)
GLX_SGIX_visual_select_group = 1
GLX_OML_swap_method = 1
GLX_OML_sync_control = 1
glXGetSyncValuesOML = _link_function('glXGetSyncValuesOML', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)], 'OML_sync_control')
glXGetMscRateOML = _link_function('glXGetMscRateOML', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int32), POINTER(c_int32)], 'OML_sync_control')
glXSwapBuffersMscOML = _link_function('glXSwapBuffersMscOML', c_int64, [POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64], 'OML_sync_control')
glXWaitForMscOML = _link_function('glXWaitForMscOML', c_int, [POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)], 'OML_sync_control')
glXWaitForSbcOML = _link_function('glXWaitForSbcOML', c_int, [POINTER(Display), GLXDrawable, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)], 'OML_sync_control')
PFNGLXGETSYNCVALUESOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64))
PFNGLXGETMSCRATEOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_int32), POINTER(c_int32))
PFNGLXSWAPBUFFERSMSCOMLPROC = CFUNCTYPE(c_int64, POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64)
PFNGLXWAITFORMSCOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64))
PFNGLXWAITFORSBCOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64))
GLX_NV_float_buffer = 1
GLX_SGIX_hyperpipe = 1

class struct_anon_107(Structure):
    __slots__ = [
     'pipeName',
     'networkId']


struct_anon_107._fields_ = [
 (
  'pipeName', c_char * 80),
 (
  'networkId', c_int)]
GLXHyperpipeNetworkSGIX = struct_anon_107

class struct_anon_108(Structure):
    __slots__ = [
     'pipeName',
     'channel',
     'participationType',
     'timeSlice']


struct_anon_108._fields_ = [
 (
  'pipeName', c_char * 80),
 (
  'channel', c_int),
 (
  'participationType', c_uint),
 (
  'timeSlice', c_int)]
GLXHyperpipeConfigSGIX = struct_anon_108

class struct_anon_109(Structure):
    __slots__ = [
     'pipeName', 
     'srcXOrigin', 
     'srcYOrigin', 
     'srcWidth', 
     'srcHeight', 
     'destXOrigin', 
     'destYOrigin', 
     'destWidth', 
     'destHeight']


struct_anon_109._fields_ = [
 (
  'pipeName', c_char * 80),
 (
  'srcXOrigin', c_int),
 (
  'srcYOrigin', c_int),
 (
  'srcWidth', c_int),
 (
  'srcHeight', c_int),
 (
  'destXOrigin', c_int),
 (
  'destYOrigin', c_int),
 (
  'destWidth', c_int),
 (
  'destHeight', c_int)]
GLXPipeRect = struct_anon_109

class struct_anon_110(Structure):
    __slots__ = [
     'pipeName', 
     'XOrigin', 
     'YOrigin', 
     'maxHeight', 
     'maxWidth']


struct_anon_110._fields_ = [
 (
  'pipeName', c_char * 80),
 (
  'XOrigin', c_int),
 (
  'YOrigin', c_int),
 (
  'maxHeight', c_int),
 (
  'maxWidth', c_int)]
GLXPipeRectLimits = struct_anon_110
glXQueryHyperpipeNetworkSGIX = _link_function('glXQueryHyperpipeNetworkSGIX', POINTER(GLXHyperpipeNetworkSGIX), [POINTER(Display), POINTER(c_int)], 'SGIX_hyperpipe')
glXHyperpipeConfigSGIX = _link_function('glXHyperpipeConfigSGIX', c_int, [POINTER(Display), c_int, c_int, POINTER(GLXHyperpipeConfigSGIX), POINTER(c_int)], 'SGIX_hyperpipe')
glXQueryHyperpipeConfigSGIX = _link_function('glXQueryHyperpipeConfigSGIX', POINTER(GLXHyperpipeConfigSGIX), [POINTER(Display), c_int, POINTER(c_int)], 'SGIX_hyperpipe')
glXDestroyHyperpipeConfigSGIX = _link_function('glXDestroyHyperpipeConfigSGIX', c_int, [POINTER(Display), c_int], 'SGIX_hyperpipe')
glXBindHyperpipeSGIX = _link_function('glXBindHyperpipeSGIX', c_int, [POINTER(Display), c_int], 'SGIX_hyperpipe')
glXQueryHyperpipeBestAttribSGIX = _link_function('glXQueryHyperpipeBestAttribSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, POINTER(None), POINTER(None)], 'SGIX_hyperpipe')
glXHyperpipeAttribSGIX = _link_function('glXHyperpipeAttribSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, POINTER(None)], 'SGIX_hyperpipe')
glXQueryHyperpipeAttribSGIX = _link_function('glXQueryHyperpipeAttribSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, POINTER(None)], 'SGIX_hyperpipe')
PFNGLXQUERYHYPERPIPENETWORKSGIXPROC = CFUNCTYPE(POINTER(GLXHyperpipeNetworkSGIX), POINTER(Display), POINTER(c_int))
PFNGLXHYPERPIPECONFIGSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(GLXHyperpipeConfigSGIX), POINTER(c_int))
PFNGLXQUERYHYPERPIPECONFIGSGIXPROC = CFUNCTYPE(POINTER(GLXHyperpipeConfigSGIX), POINTER(Display), c_int, POINTER(c_int))
PFNGLXDESTROYHYPERPIPECONFIGSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int)
PFNGLXBINDHYPERPIPESGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int)
PFNGLXQUERYHYPERPIPEBESTATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, POINTER(None), POINTER(None))
PFNGLXHYPERPIPEATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, POINTER(None))
PFNGLXQUERYHYPERPIPEATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, POINTER(None))
GLX_MESA_agp_offset = 1
glXGetAGPOffsetMESA = _link_function('glXGetAGPOffsetMESA', c_uint, [POINTER(None)], 'MESA_agp_offset')
PFNGLXGETAGPOFFSETMESAPROC = CFUNCTYPE(c_uint, POINTER(None))
GLX_EXT_fbconfig_packed_float = 1
GLX_EXT_framebuffer_sRGB = 1
GLX_EXT_texture_from_pixmap = 1
glXBindTexImageEXT = _link_function('glXBindTexImageEXT', None, [POINTER(Display), GLXDrawable, c_int, POINTER(c_int)], 'EXT_texture_from_pixmap')
glXReleaseTexImageEXT = _link_function('glXReleaseTexImageEXT', None, [POINTER(Display), GLXDrawable, c_int], 'EXT_texture_from_pixmap')
PFNGLXBINDTEXIMAGEEXTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int, POINTER(c_int))
PFNGLXRELEASETEXIMAGEEXTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int)
GLX_NV_present_video = 1
glXEnumerateVideoDevicesNV = _link_function('glXEnumerateVideoDevicesNV', POINTER(c_uint), [POINTER(Display), c_int, POINTER(c_int)], 'NV_present_video')
glXBindVideoDeviceNV = _link_function('glXBindVideoDeviceNV', c_int, [POINTER(Display), c_uint, c_uint, POINTER(c_int)], 'NV_present_video')
PFNGLXENUMERATEVIDEODEVICESNVPROC = CFUNCTYPE(POINTER(c_uint), POINTER(Display), c_int, POINTER(c_int))
PFNGLXBINDVIDEODEVICENVPROC = CFUNCTYPE(c_int, POINTER(Display), c_uint, c_uint, POINTER(c_int))
GLX_NV_video_output = 1
glXGetVideoDeviceNV = _link_function('glXGetVideoDeviceNV', c_int, [POINTER(Display), c_int, c_int, POINTER(GLXVideoDeviceNV)], 'NV_video_output')
glXReleaseVideoDeviceNV = _link_function('glXReleaseVideoDeviceNV', c_int, [POINTER(Display), c_int, GLXVideoDeviceNV], 'NV_video_output')
GLXPbuffer = pyglet.gl.glx.GLXPbuffer
glXBindVideoImageNV = _link_function('glXBindVideoImageNV', c_int, [POINTER(Display), GLXVideoDeviceNV, GLXPbuffer, c_int], 'NV_video_output')
glXReleaseVideoImageNV = _link_function('glXReleaseVideoImageNV', c_int, [POINTER(Display), GLXPbuffer], 'NV_video_output')
GLboolean = c_ubyte
glXSendPbufferToVideoNV = _link_function('glXSendPbufferToVideoNV', c_int, [POINTER(Display), GLXPbuffer, c_int, POINTER(c_ulong), GLboolean], 'NV_video_output')
glXGetVideoInfoNV = _link_function('glXGetVideoInfoNV', c_int, [POINTER(Display), c_int, GLXVideoDeviceNV, POINTER(c_ulong), POINTER(c_ulong)], 'NV_video_output')
PFNGLXGETVIDEODEVICENVPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(GLXVideoDeviceNV))
PFNGLXRELEASEVIDEODEVICENVPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, GLXVideoDeviceNV)
PFNGLXBINDVIDEOIMAGENVPROC = CFUNCTYPE(c_int, POINTER(Display), GLXVideoDeviceNV, GLXPbuffer, c_int)
PFNGLXRELEASEVIDEOIMAGENVPROC = CFUNCTYPE(c_int, POINTER(Display), GLXPbuffer)
PFNGLXSENDPBUFFERTOVIDEONVPROC = CFUNCTYPE(c_int, POINTER(Display), GLXPbuffer, c_int, POINTER(c_ulong), GLboolean)
PFNGLXGETVIDEOINFONVPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, GLXVideoDeviceNV, POINTER(c_ulong), POINTER(c_ulong))
GLX_NV_swap_group = 1
GLuint = c_uint
glXJoinSwapGroupNV = _link_function('glXJoinSwapGroupNV', c_int, [POINTER(Display), GLXDrawable, GLuint], 'NV_swap_group')
glXBindSwapBarrierNV = _link_function('glXBindSwapBarrierNV', c_int, [POINTER(Display), GLuint, GLuint], 'NV_swap_group')
glXQuerySwapGroupNV = _link_function('glXQuerySwapGroupNV', c_int, [POINTER(Display), GLXDrawable, POINTER(GLuint), POINTER(GLuint)], 'NV_swap_group')
glXQueryMaxSwapGroupsNV = _link_function('glXQueryMaxSwapGroupsNV', c_int, [POINTER(Display), c_int, POINTER(GLuint), POINTER(GLuint)], 'NV_swap_group')
glXQueryFrameCountNV = _link_function('glXQueryFrameCountNV', c_int, [POINTER(Display), c_int, POINTER(GLuint)], 'NV_swap_group')
glXResetFrameCountNV = _link_function('glXResetFrameCountNV', c_int, [POINTER(Display), c_int], 'NV_swap_group')
PFNGLXJOINSWAPGROUPNVPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, GLuint)
PFNGLXBINDSWAPBARRIERNVPROC = CFUNCTYPE(c_int, POINTER(Display), GLuint, GLuint)
PFNGLXQUERYSWAPGROUPNVPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(GLuint), POINTER(GLuint))
PFNGLXQUERYMAXSWAPGROUPSNVPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, POINTER(GLuint), POINTER(GLuint))
PFNGLXQUERYFRAMECOUNTNVPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, POINTER(GLuint))
PFNGLXRESETFRAMECOUNTNVPROC = CFUNCTYPE(c_int, POINTER(Display), c_int)
GLX_NV_video_capture = 1
glXBindVideoCaptureDeviceNV = _link_function('glXBindVideoCaptureDeviceNV', c_int, [POINTER(Display), c_uint, GLXVideoCaptureDeviceNV], 'NV_video_capture')
glXEnumerateVideoCaptureDevicesNV = _link_function('glXEnumerateVideoCaptureDevicesNV', POINTER(GLXVideoCaptureDeviceNV), [POINTER(Display), c_int, POINTER(c_int)], 'NV_video_capture')
glXLockVideoCaptureDeviceNV = _link_function('glXLockVideoCaptureDeviceNV', None, [POINTER(Display), GLXVideoCaptureDeviceNV], 'NV_video_capture')
glXQueryVideoCaptureDeviceNV = _link_function('glXQueryVideoCaptureDeviceNV', c_int, [POINTER(Display), GLXVideoCaptureDeviceNV, c_int, POINTER(c_int)], 'NV_video_capture')
glXReleaseVideoCaptureDeviceNV = _link_function('glXReleaseVideoCaptureDeviceNV', None, [POINTER(Display), GLXVideoCaptureDeviceNV], 'NV_video_capture')
PFNGLXBINDVIDEOCAPTUREDEVICENVPROC = CFUNCTYPE(c_int, POINTER(Display), c_uint, GLXVideoCaptureDeviceNV)
PFNGLXENUMERATEVIDEOCAPTUREDEVICESNVPROC = CFUNCTYPE(POINTER(GLXVideoCaptureDeviceNV), POINTER(Display), c_int, POINTER(c_int))
PFNGLXLOCKVIDEOCAPTUREDEVICENVPROC = CFUNCTYPE(None, POINTER(Display), GLXVideoCaptureDeviceNV)
PFNGLXQUERYVIDEOCAPTUREDEVICENVPROC = CFUNCTYPE(c_int, POINTER(Display), GLXVideoCaptureDeviceNV, c_int, POINTER(c_int))
PFNGLXRELEASEVIDEOCAPTUREDEVICENVPROC = CFUNCTYPE(None, POINTER(Display), GLXVideoCaptureDeviceNV)
GLX_EXT_swap_control = 1
glXSwapIntervalEXT = _link_function('glXSwapIntervalEXT', c_int, [POINTER(Display), GLXDrawable, c_int], 'EXT_swap_control')
PFNGLXSWAPINTERVALEXTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, c_int)
GLX_NV_copy_image = 1
GLint = c_int
GLsizei = c_int
glXCopyImageSubDataNV = _link_function('glXCopyImageSubDataNV', None, [POINTER(Display), GLXContext, GLuint, GLenum, GLint, GLint, GLint, GLint, GLXContext, GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei], 'NV_copy_image')
PFNGLXCOPYIMAGESUBDATANVPROC = CFUNCTYPE(None, POINTER(Display), GLXContext, GLuint, GLenum, GLint, GLint, GLint, GLint, GLXContext, GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei)
GLX_INTEL_swap_event = 1
GLX_NV_multisample_coverage = 1
__all__ = [
 'GLX_GLXEXT_VERSION', 'GLX_SAMPLE_BUFFERS_ARB', 'GLX_SAMPLES_ARB', 
 'GLX_CONTEXT_ALLOW_BUFFER_BYTE_ORDER_MISMATCH_ARB', 
 'GLX_RGBA_FLOAT_TYPE_ARB', 
 'GLX_RGBA_FLOAT_BIT_ARB', 'GLX_FRAMEBUFFER_SRGB_CAPABLE_ARB', 
 'GLX_CONTEXT_DEBUG_BIT_ARB', 
 'GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB', 
 'GLX_CONTEXT_MAJOR_VERSION_ARB', 
 'GLX_CONTEXT_MINOR_VERSION_ARB', 
 'GLX_CONTEXT_FLAGS_ARB', 'GLX_CONTEXT_CORE_PROFILE_BIT_ARB', 
 'GLX_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB', 
 'GLX_CONTEXT_PROFILE_MASK_ARB', 
 'GLX_CONTEXT_ROBUST_ACCESS_BIT_ARB', 'GLX_LOSE_CONTEXT_ON_RESET_ARB', 
 'GLX_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB', 
 'GLX_NO_RESET_NOTIFICATION_ARB', 
 'GLX_SAMPLE_BUFFERS_SGIS', 
 'GLX_SAMPLES_SGIS', 'GLX_X_VISUAL_TYPE_EXT', 
 'GLX_TRANSPARENT_TYPE_EXT', 
 'GLX_TRANSPARENT_INDEX_VALUE_EXT', 'GLX_TRANSPARENT_RED_VALUE_EXT', 
 'GLX_TRANSPARENT_GREEN_VALUE_EXT', 
 'GLX_TRANSPARENT_BLUE_VALUE_EXT', 
 'GLX_TRANSPARENT_ALPHA_VALUE_EXT', 'GLX_NONE_EXT', 
 'GLX_TRUE_COLOR_EXT', 
 'GLX_DIRECT_COLOR_EXT', 'GLX_PSEUDO_COLOR_EXT', 'GLX_STATIC_COLOR_EXT', 
 'GLX_GRAY_SCALE_EXT', 
 'GLX_STATIC_GRAY_EXT', 'GLX_TRANSPARENT_RGB_EXT', 
 'GLX_TRANSPARENT_INDEX_EXT', 
 'GLX_VISUAL_CAVEAT_EXT', 'GLX_SLOW_VISUAL_EXT', 
 'GLX_NON_CONFORMANT_VISUAL_EXT', 
 'GLX_SHARE_CONTEXT_EXT', 'GLX_VISUAL_ID_EXT', 
 'GLX_SCREEN_EXT', 'GLX_WINDOW_BIT_SGIX', 
 'GLX_PIXMAP_BIT_SGIX', 
 'GLX_RGBA_BIT_SGIX', 'GLX_COLOR_INDEX_BIT_SGIX', 
 'GLX_DRAWABLE_TYPE_SGIX', 
 'GLX_RENDER_TYPE_SGIX', 'GLX_X_RENDERABLE_SGIX', 
 'GLX_FBCONFIG_ID_SGIX', 
 'GLX_RGBA_TYPE_SGIX', 'GLX_COLOR_INDEX_TYPE_SGIX', 
 'GLX_PBUFFER_BIT_SGIX', 
 'GLX_BUFFER_CLOBBER_MASK_SGIX', 'GLX_FRONT_LEFT_BUFFER_BIT_SGIX', 
 'GLX_FRONT_RIGHT_BUFFER_BIT_SGIX', 
 'GLX_BACK_LEFT_BUFFER_BIT_SGIX', 
 'GLX_BACK_RIGHT_BUFFER_BIT_SGIX', 'GLX_AUX_BUFFERS_BIT_SGIX', 
 'GLX_DEPTH_BUFFER_BIT_SGIX', 
 'GLX_STENCIL_BUFFER_BIT_SGIX', 
 'GLX_ACCUM_BUFFER_BIT_SGIX', 'GLX_SAMPLE_BUFFERS_BIT_SGIX', 
 'GLX_MAX_PBUFFER_WIDTH_SGIX', 
 'GLX_MAX_PBUFFER_HEIGHT_SGIX', 
 'GLX_MAX_PBUFFER_PIXELS_SGIX', 'GLX_OPTIMAL_PBUFFER_WIDTH_SGIX', 
 'GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX', 
 'GLX_PRESERVED_CONTENTS_SGIX', 
 'GLX_LARGEST_PBUFFER_SGIX', 'GLX_WIDTH_SGIX', 
 'GLX_HEIGHT_SGIX', 
 'GLX_EVENT_MASK_SGIX', 'GLX_DAMAGED_SGIX', 'GLX_SAVED_SGIX', 
 'GLX_WINDOW_SGIX', 
 'GLX_PBUFFER_SGIX', 'GLX_SYNC_FRAME_SGIX', 
 'GLX_SYNC_SWAP_SGIX', 'GLX_DIGITAL_MEDIA_PBUFFER_SGIX', 
 'GLX_BLENDED_RGBA_SGIS', 
 'GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS', 
 'GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS', 
 'GLX_SAMPLE_BUFFERS_3DFX', 
 'GLX_SAMPLES_3DFX', 'GLX_3DFX_WINDOW_MODE_MESA', 
 'GLX_3DFX_FULLSCREEN_MODE_MESA', 
 'GLX_VISUAL_SELECT_GROUP_SGIX', 
 'GLX_SWAP_METHOD_OML', 'GLX_SWAP_EXCHANGE_OML', 
 'GLX_SWAP_COPY_OML', 
 'GLX_SWAP_UNDEFINED_OML', 'GLX_FLOAT_COMPONENTS_NV', 
 'GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX', 
 'GLX_BAD_HYPERPIPE_CONFIG_SGIX', 
 'GLX_BAD_HYPERPIPE_SGIX', 'GLX_HYPERPIPE_DISPLAY_PIPE_SGIX', 
 'GLX_HYPERPIPE_RENDER_PIPE_SGIX', 
 'GLX_PIPE_RECT_SGIX', 
 'GLX_PIPE_RECT_LIMITS_SGIX', 'GLX_HYPERPIPE_STEREO_SGIX', 
 'GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX', 
 'GLX_HYPERPIPE_ID_SGIX', 
 'GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT', 'GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT', 
 'GLX_FRAMEBUFFER_SRGB_CAPABLE_EXT', 
 'GLX_TEXTURE_1D_BIT_EXT', 
 'GLX_TEXTURE_2D_BIT_EXT', 'GLX_TEXTURE_RECTANGLE_BIT_EXT', 
 'GLX_BIND_TO_TEXTURE_RGB_EXT', 
 'GLX_BIND_TO_TEXTURE_RGBA_EXT', 
 'GLX_BIND_TO_MIPMAP_TEXTURE_EXT', 'GLX_BIND_TO_TEXTURE_TARGETS_EXT', 
 'GLX_Y_INVERTED_EXT', 
 'GLX_TEXTURE_FORMAT_EXT', 'GLX_TEXTURE_TARGET_EXT', 
 'GLX_MIPMAP_TEXTURE_EXT', 
 'GLX_TEXTURE_FORMAT_NONE_EXT', 
 'GLX_TEXTURE_FORMAT_RGB_EXT', 'GLX_TEXTURE_FORMAT_RGBA_EXT', 
 'GLX_TEXTURE_1D_EXT', 
 'GLX_TEXTURE_2D_EXT', 'GLX_TEXTURE_RECTANGLE_EXT', 
 'GLX_FRONT_LEFT_EXT', 
 'GLX_FRONT_RIGHT_EXT', 'GLX_BACK_LEFT_EXT', 
 'GLX_BACK_RIGHT_EXT', 'GLX_FRONT_EXT', 
 'GLX_BACK_EXT', 'GLX_AUX0_EXT', 
 'GLX_AUX1_EXT', 'GLX_AUX2_EXT', 'GLX_AUX3_EXT', 
 'GLX_AUX4_EXT', 
 'GLX_AUX5_EXT', 'GLX_AUX6_EXT', 'GLX_AUX7_EXT', 'GLX_AUX8_EXT', 
 'GLX_AUX9_EXT', 
 'GLX_NUM_VIDEO_SLOTS_NV', 'GLX_VIDEO_OUT_COLOR_NV', 
 'GLX_VIDEO_OUT_ALPHA_NV', 
 'GLX_VIDEO_OUT_DEPTH_NV', 
 'GLX_VIDEO_OUT_COLOR_AND_ALPHA_NV', 'GLX_VIDEO_OUT_COLOR_AND_DEPTH_NV', 
 'GLX_VIDEO_OUT_FRAME_NV', 
 'GLX_VIDEO_OUT_FIELD_1_NV', 
 'GLX_VIDEO_OUT_FIELD_2_NV', 'GLX_VIDEO_OUT_STACKED_FIELDS_1_2_NV', 
 'GLX_VIDEO_OUT_STACKED_FIELDS_2_1_NV', 
 'GLX_DEVICE_ID_NV', 'GLX_UNIQUE_ID_NV', 
 'GLX_NUM_VIDEO_CAPTURE_SLOTS_NV', 
 'GLX_SWAP_INTERVAL_EXT', 
 'GLX_MAX_SWAP_INTERVAL_EXT', 'GLX_BUFFER_SWAP_COMPLETE_INTEL_MASK', 
 'GLX_EXCHANGE_COMPLETE_INTEL', 
 'GLX_COPY_COMPLETE_INTEL', 
 'GLX_FLIP_COMPLETE_INTEL', 'GLX_COVERAGE_SAMPLES_NV', 
 'GLX_COLOR_SAMPLES_NV', 
 'GLX_GPU_VENDOR_AMD', 'GLX_GPU_RENDERER_STRING_AMD', 
 'GLX_GPU_OPENGL_VERSION_STRING_AMD', 
 'GLX_GPU_FASTEST_TARGET_GPUS_AMD', 
 'GLX_GPU_RAM_AMD', 'GLX_GPU_CLOCK_AMD', 
 'GLX_GPU_NUM_PIPES_AMD', 
 'GLX_GPU_NUM_SIMD_AMD', 'GLX_GPU_NUM_RB_AMD', 'GLX_GPU_NUM_SPI_AMD', 
 'GLX_CONTEXT_ES2_PROFILE_BIT_EXT', 
 'GLXVideoSourceSGIX', 'GLXFBConfigIDSGIX', 
 'GLXFBConfigSGIX', 'GLXPbufferSGIX', 
 'GLXBufferClobberEventSGIX', 
 'GLXVideoDeviceNV', 'GLXVideoCaptureDeviceNV', 
 'GLX_ARB_multisample', 
 'GLX_ARB_fbconfig_float', 'GLX_ARB_framebuffer_sRGB', 
 'GLX_ARB_create_context', 
 'glXCreateContextAttribsARB', 
 'PFNGLXCREATECONTEXTATTRIBSARBPROC', 'GLX_ARB_create_context_profile', 
 'GLX_ARB_create_context_robustness', 
 'GLX_SGIS_multisample', 
 'GLX_EXT_visual_info', 'GLX_SGI_swap_control', 'glXSwapIntervalSGI', 
 'PFNGLXSWAPINTERVALSGIPROC', 
 'GLX_SGI_video_sync', 'glXGetVideoSyncSGI', 
 'glXWaitVideoSyncSGI', 'PFNGLXGETVIDEOSYNCSGIPROC', 
 'PFNGLXWAITVIDEOSYNCSGIPROC', 
 'GLX_SGI_make_current_read', 
 'glXMakeCurrentReadSGI', 'glXGetCurrentReadDrawableSGI', 
 'PFNGLXMAKECURRENTREADSGIPROC', 
 'PFNGLXGETCURRENTREADDRAWABLESGIPROC', 
 'GLX_SGIX_video_source', 'GLX_EXT_visual_rating', 
 'GLX_EXT_import_context', 
 'glXGetCurrentDisplayEXT', 'glXQueryContextInfoEXT', 
 'glXGetContextIDEXT', 
 'glXImportContextEXT', 'glXFreeContextEXT', 'PFNGLXGETCURRENTDISPLAYEXTPROC', 
 'PFNGLXQUERYCONTEXTINFOEXTPROC', 
 'PFNGLXGETCONTEXTIDEXTPROC', 
 'PFNGLXIMPORTCONTEXTEXTPROC', 'PFNGLXFREECONTEXTEXTPROC', 
 'GLX_SGIX_fbconfig', 
 'glXGetFBConfigAttribSGIX', 'glXChooseFBConfigSGIX', 
 'glXCreateGLXPixmapWithConfigSGIX', 
 'glXCreateContextWithConfigSGIX', 
 'glXGetVisualFromFBConfigSGIX', 'glXGetFBConfigFromVisualSGIX', 
 'PFNGLXGETFBCONFIGATTRIBSGIXPROC', 
 'PFNGLXCHOOSEFBCONFIGSGIXPROC', 
 'PFNGLXCREATEGLXPIXMAPWITHCONFIGSGIXPROC', 
 'PFNGLXCREATECONTEXTWITHCONFIGSGIXPROC', 
 'PFNGLXGETVISUALFROMFBCONFIGSGIXPROC', 
 'PFNGLXGETFBCONFIGFROMVISUALSGIXPROC', 
 'GLX_SGIX_pbuffer', 'glXCreateGLXPbufferSGIX', 
 'glXDestroyGLXPbufferSGIX', 
 'glXQueryGLXPbufferSGIX', 'glXSelectEventSGIX', 
 'glXGetSelectedEventSGIX', 
 'PFNGLXCREATEGLXPBUFFERSGIXPROC', 'PFNGLXDESTROYGLXPBUFFERSGIXPROC', 
 'PFNGLXQUERYGLXPBUFFERSGIXPROC', 
 'PFNGLXSELECTEVENTSGIXPROC', 
 'PFNGLXGETSELECTEDEVENTSGIXPROC', 'GLX_SGI_cushion', 
 'glXCushionSGI', 
 'PFNGLXCUSHIONSGIPROC', 'GLX_SGIX_video_resize', 'glXBindChannelToWindowSGIX', 
 'glXChannelRectSGIX', 
 'glXQueryChannelRectSGIX', 'glXQueryChannelDeltasSGIX', 
 'glXChannelRectSyncSGIX', 
 'PFNGLXBINDCHANNELTOWINDOWSGIXPROC', 
 'PFNGLXCHANNELRECTSGIXPROC', 'PFNGLXQUERYCHANNELRECTSGIXPROC', 
 'PFNGLXQUERYCHANNELDELTASSGIXPROC', 
 'PFNGLXCHANNELRECTSYNCSGIXPROC', 
 'GLX_SGIX_dmbuffer', 'GLX_SGIX_swap_group', 
 'glXJoinSwapGroupSGIX', 
 'PFNGLXJOINSWAPGROUPSGIXPROC', 'GLX_SGIX_swap_barrier', 
 'glXBindSwapBarrierSGIX', 
 'glXQueryMaxSwapBarriersSGIX', 
 'PFNGLXBINDSWAPBARRIERSGIXPROC', 'PFNGLXQUERYMAXSWAPBARRIERSSGIXPROC', 
 'GLX_SUN_get_transparent_index', 
 'glXGetTransparentIndexSUN', 
 'PFNGLXGETTRANSPARENTINDEXSUNPROC', 'GLX_MESA_copy_sub_buffer', 
 'glXCopySubBufferMESA', 
 'PFNGLXCOPYSUBBUFFERMESAPROC', 
 'GLX_MESA_pixmap_colormap', 'glXCreateGLXPixmapMESA', 
 'PFNGLXCREATEGLXPIXMAPMESAPROC', 
 'GLX_MESA_release_buffers', 
 'glXReleaseBuffersMESA', 'PFNGLXRELEASEBUFFERSMESAPROC', 
 'GLX_MESA_set_3dfx_mode', 
 'glXSet3DfxModeMESA', 'PFNGLXSET3DFXMODEMESAPROC', 
 'GLX_SGIX_visual_select_group', 
 'GLX_OML_swap_method', 'GLX_OML_sync_control', 
 'glXGetSyncValuesOML', 'glXGetMscRateOML', 
 'glXSwapBuffersMscOML', 
 'glXWaitForMscOML', 'glXWaitForSbcOML', 'PFNGLXGETSYNCVALUESOMLPROC', 
 'PFNGLXGETMSCRATEOMLPROC', 
 'PFNGLXSWAPBUFFERSMSCOMLPROC', 
 'PFNGLXWAITFORMSCOMLPROC', 'PFNGLXWAITFORSBCOMLPROC', 
 'GLX_NV_float_buffer', 
 'GLX_SGIX_hyperpipe', 'GLXHyperpipeNetworkSGIX', 
 'GLXHyperpipeConfigSGIX', 
 'GLXPipeRect', 'GLXPipeRectLimits', 'glXQueryHyperpipeNetworkSGIX', 
 'glXHyperpipeConfigSGIX', 
 'glXQueryHyperpipeConfigSGIX', 
 'glXDestroyHyperpipeConfigSGIX', 'glXBindHyperpipeSGIX', 
 'glXQueryHyperpipeBestAttribSGIX', 
 'glXHyperpipeAttribSGIX', 
 'glXQueryHyperpipeAttribSGIX', 'PFNGLXQUERYHYPERPIPENETWORKSGIXPROC', 
 'PFNGLXHYPERPIPECONFIGSGIXPROC', 
 'PFNGLXQUERYHYPERPIPECONFIGSGIXPROC', 
 'PFNGLXDESTROYHYPERPIPECONFIGSGIXPROC', 
 'PFNGLXBINDHYPERPIPESGIXPROC', 
 'PFNGLXQUERYHYPERPIPEBESTATTRIBSGIXPROC', 
 'PFNGLXHYPERPIPEATTRIBSGIXPROC', 
 'PFNGLXQUERYHYPERPIPEATTRIBSGIXPROC', 'GLX_MESA_agp_offset', 
 'glXGetAGPOffsetMESA', 
 'PFNGLXGETAGPOFFSETMESAPROC', 
 'GLX_EXT_fbconfig_packed_float', 'GLX_EXT_framebuffer_sRGB', 
 'GLX_EXT_texture_from_pixmap', 
 'glXBindTexImageEXT', 'glXReleaseTexImageEXT', 
 'PFNGLXBINDTEXIMAGEEXTPROC', 
 'PFNGLXRELEASETEXIMAGEEXTPROC', 
 'GLX_NV_present_video', 'glXEnumerateVideoDevicesNV', 
 'glXBindVideoDeviceNV', 
 'PFNGLXENUMERATEVIDEODEVICESNVPROC', 'PFNGLXBINDVIDEODEVICENVPROC', 
 'GLX_NV_video_output', 
 'glXGetVideoDeviceNV', 'glXReleaseVideoDeviceNV', 
 'glXBindVideoImageNV', 
 'glXReleaseVideoImageNV', 'glXSendPbufferToVideoNV', 
 'glXGetVideoInfoNV', 
 'PFNGLXGETVIDEODEVICENVPROC', 
 'PFNGLXRELEASEVIDEODEVICENVPROC', 'PFNGLXBINDVIDEOIMAGENVPROC', 
 'PFNGLXRELEASEVIDEOIMAGENVPROC', 
 'PFNGLXSENDPBUFFERTOVIDEONVPROC', 
 'PFNGLXGETVIDEOINFONVPROC', 'GLX_NV_swap_group', 
 'glXJoinSwapGroupNV', 
 'glXBindSwapBarrierNV', 'glXQuerySwapGroupNV', 'glXQueryMaxSwapGroupsNV', 
 'glXQueryFrameCountNV', 
 'glXResetFrameCountNV', 'PFNGLXJOINSWAPGROUPNVPROC', 
 'PFNGLXBINDSWAPBARRIERNVPROC', 
 'PFNGLXQUERYSWAPGROUPNVPROC', 
 'PFNGLXQUERYMAXSWAPGROUPSNVPROC', 'PFNGLXQUERYFRAMECOUNTNVPROC', 
 'PFNGLXRESETFRAMECOUNTNVPROC', 
 'GLX_NV_video_capture', 
 'glXBindVideoCaptureDeviceNV', 'glXEnumerateVideoCaptureDevicesNV', 
 'glXLockVideoCaptureDeviceNV', 
 'glXQueryVideoCaptureDeviceNV', 
 'glXReleaseVideoCaptureDeviceNV', 'PFNGLXBINDVIDEOCAPTUREDEVICENVPROC', 
 'PFNGLXENUMERATEVIDEOCAPTUREDEVICESNVPROC', 
 'PFNGLXLOCKVIDEOCAPTUREDEVICENVPROC', 
 'PFNGLXQUERYVIDEOCAPTUREDEVICENVPROC', 
 'PFNGLXRELEASEVIDEOCAPTUREDEVICENVPROC', 
 'GLX_EXT_swap_control', 
 'glXSwapIntervalEXT', 'PFNGLXSWAPINTERVALEXTPROC', 
 'GLX_NV_copy_image', 
 'glXCopyImageSubDataNV', 'PFNGLXCOPYIMAGESUBDATANVPROC', 
 'GLX_INTEL_swap_event', 
 'GLX_NV_multisample_coverage']
# okay decompiling out\pyglet.gl.glxext_arb.pyc
