# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.gl
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from pyglet.gl.lib import link_GL as _link_function
from pyglet.gl.lib import c_ptrdiff_t
GL_VERSION_1_1 = 1
GL_VERSION_1_2 = 1
GL_VERSION_1_3 = 1
GL_ARB_imaging = 1
GLenum = c_uint
GLboolean = c_ubyte
GLbitfield = c_uint
GLvoid = None
GLbyte = c_char
GLshort = c_short
GLint = c_int
GLubyte = c_ubyte
GLushort = c_ushort
GLuint = c_uint
GLsizei = c_int
GLfloat = c_float
GLclampf = c_float
GLdouble = c_double
GLclampd = c_double
GL_FALSE = 0
GL_TRUE = 1
GL_BYTE = 5120
GL_UNSIGNED_BYTE = 5121
GL_SHORT = 5122
GL_UNSIGNED_SHORT = 5123
GL_INT = 5124
GL_UNSIGNED_INT = 5125
GL_FLOAT = 5126
GL_2_BYTES = 5127
GL_3_BYTES = 5128
GL_4_BYTES = 5129
GL_DOUBLE = 5130
GL_POINTS = 0
GL_LINES = 1
GL_LINE_LOOP = 2
GL_LINE_STRIP = 3
GL_TRIANGLES = 4
GL_TRIANGLE_STRIP = 5
GL_TRIANGLE_FAN = 6
GL_QUADS = 7
GL_QUAD_STRIP = 8
GL_POLYGON = 9
GL_VERTEX_ARRAY = 32884
GL_NORMAL_ARRAY = 32885
GL_COLOR_ARRAY = 32886
GL_INDEX_ARRAY = 32887
GL_TEXTURE_COORD_ARRAY = 32888
GL_EDGE_FLAG_ARRAY = 32889
GL_VERTEX_ARRAY_SIZE = 32890
GL_VERTEX_ARRAY_TYPE = 32891
GL_VERTEX_ARRAY_STRIDE = 32892
GL_NORMAL_ARRAY_TYPE = 32894
GL_NORMAL_ARRAY_STRIDE = 32895
GL_COLOR_ARRAY_SIZE = 32897
GL_COLOR_ARRAY_TYPE = 32898
GL_COLOR_ARRAY_STRIDE = 32899
GL_INDEX_ARRAY_TYPE = 32901
GL_INDEX_ARRAY_STRIDE = 32902
GL_TEXTURE_COORD_ARRAY_SIZE = 32904
GL_TEXTURE_COORD_ARRAY_TYPE = 32905
GL_TEXTURE_COORD_ARRAY_STRIDE = 32906
GL_EDGE_FLAG_ARRAY_STRIDE = 32908
GL_VERTEX_ARRAY_POINTER = 32910
GL_NORMAL_ARRAY_POINTER = 32911
GL_COLOR_ARRAY_POINTER = 32912
GL_INDEX_ARRAY_POINTER = 32913
GL_TEXTURE_COORD_ARRAY_POINTER = 32914
GL_EDGE_FLAG_ARRAY_POINTER = 32915
GL_V2F = 10784
GL_V3F = 10785
GL_C4UB_V2F = 10786
GL_C4UB_V3F = 10787
GL_C3F_V3F = 10788
GL_N3F_V3F = 10789
GL_C4F_N3F_V3F = 10790
GL_T2F_V3F = 10791
GL_T4F_V4F = 10792
GL_T2F_C4UB_V3F = 10793
GL_T2F_C3F_V3F = 10794
GL_T2F_N3F_V3F = 10795
GL_T2F_C4F_N3F_V3F = 10796
GL_T4F_C4F_N3F_V4F = 10797
GL_MATRIX_MODE = 2976
GL_MODELVIEW = 5888
GL_PROJECTION = 5889
GL_TEXTURE = 5890
GL_POINT_SMOOTH = 2832
GL_POINT_SIZE = 2833
GL_POINT_SIZE_GRANULARITY = 2835
GL_POINT_SIZE_RANGE = 2834
GL_LINE_SMOOTH = 2848
GL_LINE_STIPPLE = 2852
GL_LINE_STIPPLE_PATTERN = 2853
GL_LINE_STIPPLE_REPEAT = 2854
GL_LINE_WIDTH = 2849
GL_LINE_WIDTH_GRANULARITY = 2851
GL_LINE_WIDTH_RANGE = 2850
GL_POINT = 6912
GL_LINE = 6913
GL_FILL = 6914
GL_CW = 2304
GL_CCW = 2305
GL_FRONT = 1028
GL_BACK = 1029
GL_POLYGON_MODE = 2880
GL_POLYGON_SMOOTH = 2881
GL_POLYGON_STIPPLE = 2882
GL_EDGE_FLAG = 2883
GL_CULL_FACE = 2884
GL_CULL_FACE_MODE = 2885
GL_FRONT_FACE = 2886
GL_POLYGON_OFFSET_FACTOR = 32824
GL_POLYGON_OFFSET_UNITS = 10752
GL_POLYGON_OFFSET_POINT = 10753
GL_POLYGON_OFFSET_LINE = 10754
GL_POLYGON_OFFSET_FILL = 32823
GL_COMPILE = 4864
GL_COMPILE_AND_EXECUTE = 4865
GL_LIST_BASE = 2866
GL_LIST_INDEX = 2867
GL_LIST_MODE = 2864
GL_NEVER = 512
GL_LESS = 513
GL_EQUAL = 514
GL_LEQUAL = 515
GL_GREATER = 516
GL_NOTEQUAL = 517
GL_GEQUAL = 518
GL_ALWAYS = 519
GL_DEPTH_TEST = 2929
GL_DEPTH_BITS = 3414
GL_DEPTH_CLEAR_VALUE = 2931
GL_DEPTH_FUNC = 2932
GL_DEPTH_RANGE = 2928
GL_DEPTH_WRITEMASK = 2930
GL_DEPTH_COMPONENT = 6402
GL_LIGHTING = 2896
GL_LIGHT0 = 16384
GL_LIGHT1 = 16385
GL_LIGHT2 = 16386
GL_LIGHT3 = 16387
GL_LIGHT4 = 16388
GL_LIGHT5 = 16389
GL_LIGHT6 = 16390
GL_LIGHT7 = 16391
GL_SPOT_EXPONENT = 4613
GL_SPOT_CUTOFF = 4614
GL_CONSTANT_ATTENUATION = 4615
GL_LINEAR_ATTENUATION = 4616
GL_QUADRATIC_ATTENUATION = 4617
GL_AMBIENT = 4608
GL_DIFFUSE = 4609
GL_SPECULAR = 4610
GL_SHININESS = 5633
GL_EMISSION = 5632
GL_POSITION = 4611
GL_SPOT_DIRECTION = 4612
GL_AMBIENT_AND_DIFFUSE = 5634
GL_COLOR_INDEXES = 5635
GL_LIGHT_MODEL_TWO_SIDE = 2898
GL_LIGHT_MODEL_LOCAL_VIEWER = 2897
GL_LIGHT_MODEL_AMBIENT = 2899
GL_FRONT_AND_BACK = 1032
GL_SHADE_MODEL = 2900
GL_FLAT = 7424
GL_SMOOTH = 7425
GL_COLOR_MATERIAL = 2903
GL_COLOR_MATERIAL_FACE = 2901
GL_COLOR_MATERIAL_PARAMETER = 2902
GL_NORMALIZE = 2977
GL_CLIP_PLANE0 = 12288
GL_CLIP_PLANE1 = 12289
GL_CLIP_PLANE2 = 12290
GL_CLIP_PLANE3 = 12291
GL_CLIP_PLANE4 = 12292
GL_CLIP_PLANE5 = 12293
GL_ACCUM_RED_BITS = 3416
GL_ACCUM_GREEN_BITS = 3417
GL_ACCUM_BLUE_BITS = 3418
GL_ACCUM_ALPHA_BITS = 3419
GL_ACCUM_CLEAR_VALUE = 2944
GL_ACCUM = 256
GL_ADD = 260
GL_LOAD = 257
GL_MULT = 259
GL_RETURN = 258
GL_ALPHA_TEST = 3008
GL_ALPHA_TEST_REF = 3010
GL_ALPHA_TEST_FUNC = 3009
GL_BLEND = 3042
GL_BLEND_SRC = 3041
GL_BLEND_DST = 3040
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 768
GL_ONE_MINUS_SRC_COLOR = 769
GL_SRC_ALPHA = 770
GL_ONE_MINUS_SRC_ALPHA = 771
GL_DST_ALPHA = 772
GL_ONE_MINUS_DST_ALPHA = 773
GL_DST_COLOR = 774
GL_ONE_MINUS_DST_COLOR = 775
GL_SRC_ALPHA_SATURATE = 776
GL_FEEDBACK = 7169
GL_RENDER = 7168
GL_SELECT = 7170
GL_2D = 1536
GL_3D = 1537
GL_3D_COLOR = 1538
GL_3D_COLOR_TEXTURE = 1539
GL_4D_COLOR_TEXTURE = 1540
GL_POINT_TOKEN = 1793
GL_LINE_TOKEN = 1794
GL_LINE_RESET_TOKEN = 1799
GL_POLYGON_TOKEN = 1795
GL_BITMAP_TOKEN = 1796
GL_DRAW_PIXEL_TOKEN = 1797
GL_COPY_PIXEL_TOKEN = 1798
GL_PASS_THROUGH_TOKEN = 1792
GL_FEEDBACK_BUFFER_POINTER = 3568
GL_FEEDBACK_BUFFER_SIZE = 3569
GL_FEEDBACK_BUFFER_TYPE = 3570
GL_SELECTION_BUFFER_POINTER = 3571
GL_SELECTION_BUFFER_SIZE = 3572
GL_FOG = 2912
GL_FOG_MODE = 2917
GL_FOG_DENSITY = 2914
GL_FOG_COLOR = 2918
GL_FOG_INDEX = 2913
GL_FOG_START = 2915
GL_FOG_END = 2916
GL_LINEAR = 9729
GL_EXP = 2048
GL_EXP2 = 2049
GL_LOGIC_OP = 3057
GL_INDEX_LOGIC_OP = 3057
GL_COLOR_LOGIC_OP = 3058
GL_LOGIC_OP_MODE = 3056
GL_CLEAR = 5376
GL_SET = 5391
GL_COPY = 5379
GL_COPY_INVERTED = 5388
GL_NOOP = 5381
GL_INVERT = 5386
GL_AND = 5377
GL_NAND = 5390
GL_OR = 5383
GL_NOR = 5384
GL_XOR = 5382
GL_EQUIV = 5385
GL_AND_REVERSE = 5378
GL_AND_INVERTED = 5380
GL_OR_REVERSE = 5387
GL_OR_INVERTED = 5389
GL_STENCIL_BITS = 3415
GL_STENCIL_TEST = 2960
GL_STENCIL_CLEAR_VALUE = 2961
GL_STENCIL_FUNC = 2962
GL_STENCIL_VALUE_MASK = 2963
GL_STENCIL_FAIL = 2964
GL_STENCIL_PASS_DEPTH_FAIL = 2965
GL_STENCIL_PASS_DEPTH_PASS = 2966
GL_STENCIL_REF = 2967
GL_STENCIL_WRITEMASK = 2968
GL_STENCIL_INDEX = 6401
GL_KEEP = 7680
GL_REPLACE = 7681
GL_INCR = 7682
GL_DECR = 7683
GL_NONE = 0
GL_LEFT = 1030
GL_RIGHT = 1031
GL_FRONT_LEFT = 1024
GL_FRONT_RIGHT = 1025
GL_BACK_LEFT = 1026
GL_BACK_RIGHT = 1027
GL_AUX0 = 1033
GL_AUX1 = 1034
GL_AUX2 = 1035
GL_AUX3 = 1036
GL_COLOR_INDEX = 6400
GL_RED = 6403
GL_GREEN = 6404
GL_BLUE = 6405
GL_ALPHA = 6406
GL_LUMINANCE = 6409
GL_LUMINANCE_ALPHA = 6410
GL_ALPHA_BITS = 3413
GL_RED_BITS = 3410
GL_GREEN_BITS = 3411
GL_BLUE_BITS = 3412
GL_INDEX_BITS = 3409
GL_SUBPIXEL_BITS = 3408
GL_AUX_BUFFERS = 3072
GL_READ_BUFFER = 3074
GL_DRAW_BUFFER = 3073
GL_DOUBLEBUFFER = 3122
GL_STEREO = 3123
GL_BITMAP = 6656
GL_COLOR = 6144
GL_DEPTH = 6145
GL_STENCIL = 6146
GL_DITHER = 3024
GL_RGB = 6407
GL_RGBA = 6408
GL_MAX_LIST_NESTING = 2865
GL_MAX_EVAL_ORDER = 3376
GL_MAX_LIGHTS = 3377
GL_MAX_CLIP_PLANES = 3378
GL_MAX_TEXTURE_SIZE = 3379
GL_MAX_PIXEL_MAP_TABLE = 3380
GL_MAX_ATTRIB_STACK_DEPTH = 3381
GL_MAX_MODELVIEW_STACK_DEPTH = 3382
GL_MAX_NAME_STACK_DEPTH = 3383
GL_MAX_PROJECTION_STACK_DEPTH = 3384
GL_MAX_TEXTURE_STACK_DEPTH = 3385
GL_MAX_VIEWPORT_DIMS = 3386
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 3387
GL_ATTRIB_STACK_DEPTH = 2992
GL_CLIENT_ATTRIB_STACK_DEPTH = 2993
GL_COLOR_CLEAR_VALUE = 3106
GL_COLOR_WRITEMASK = 3107
GL_CURRENT_INDEX = 2817
GL_CURRENT_COLOR = 2816
GL_CURRENT_NORMAL = 2818
GL_CURRENT_RASTER_COLOR = 2820
GL_CURRENT_RASTER_DISTANCE = 2825
GL_CURRENT_RASTER_INDEX = 2821
GL_CURRENT_RASTER_POSITION = 2823
GL_CURRENT_RASTER_TEXTURE_COORDS = 2822
GL_CURRENT_RASTER_POSITION_VALID = 2824
GL_CURRENT_TEXTURE_COORDS = 2819
GL_INDEX_CLEAR_VALUE = 3104
GL_INDEX_MODE = 3120
GL_INDEX_WRITEMASK = 3105
GL_MODELVIEW_MATRIX = 2982
GL_MODELVIEW_STACK_DEPTH = 2979
GL_NAME_STACK_DEPTH = 3440
GL_PROJECTION_MATRIX = 2983
GL_PROJECTION_STACK_DEPTH = 2980
GL_RENDER_MODE = 3136
GL_RGBA_MODE = 3121
GL_TEXTURE_MATRIX = 2984
GL_TEXTURE_STACK_DEPTH = 2981
GL_VIEWPORT = 2978
GL_AUTO_NORMAL = 3456
GL_MAP1_COLOR_4 = 3472
GL_MAP1_INDEX = 3473
GL_MAP1_NORMAL = 3474
GL_MAP1_TEXTURE_COORD_1 = 3475
GL_MAP1_TEXTURE_COORD_2 = 3476
GL_MAP1_TEXTURE_COORD_3 = 3477
GL_MAP1_TEXTURE_COORD_4 = 3478
GL_MAP1_VERTEX_3 = 3479
GL_MAP1_VERTEX_4 = 3480
GL_MAP2_COLOR_4 = 3504
GL_MAP2_INDEX = 3505
GL_MAP2_NORMAL = 3506
GL_MAP2_TEXTURE_COORD_1 = 3507
GL_MAP2_TEXTURE_COORD_2 = 3508
GL_MAP2_TEXTURE_COORD_3 = 3509
GL_MAP2_TEXTURE_COORD_4 = 3510
GL_MAP2_VERTEX_3 = 3511
GL_MAP2_VERTEX_4 = 3512
GL_MAP1_GRID_DOMAIN = 3536
GL_MAP1_GRID_SEGMENTS = 3537
GL_MAP2_GRID_DOMAIN = 3538
GL_MAP2_GRID_SEGMENTS = 3539
GL_COEFF = 2560
GL_ORDER = 2561
GL_DOMAIN = 2562
GL_PERSPECTIVE_CORRECTION_HINT = 3152
GL_POINT_SMOOTH_HINT = 3153
GL_LINE_SMOOTH_HINT = 3154
GL_POLYGON_SMOOTH_HINT = 3155
GL_FOG_HINT = 3156
GL_DONT_CARE = 4352
GL_FASTEST = 4353
GL_NICEST = 4354
GL_SCISSOR_BOX = 3088
GL_SCISSOR_TEST = 3089
GL_MAP_COLOR = 3344
GL_MAP_STENCIL = 3345
GL_INDEX_SHIFT = 3346
GL_INDEX_OFFSET = 3347
GL_RED_SCALE = 3348
GL_RED_BIAS = 3349
GL_GREEN_SCALE = 3352
GL_GREEN_BIAS = 3353
GL_BLUE_SCALE = 3354
GL_BLUE_BIAS = 3355
GL_ALPHA_SCALE = 3356
GL_ALPHA_BIAS = 3357
GL_DEPTH_SCALE = 3358
GL_DEPTH_BIAS = 3359
GL_PIXEL_MAP_S_TO_S_SIZE = 3249
GL_PIXEL_MAP_I_TO_I_SIZE = 3248
GL_PIXEL_MAP_I_TO_R_SIZE = 3250
GL_PIXEL_MAP_I_TO_G_SIZE = 3251
GL_PIXEL_MAP_I_TO_B_SIZE = 3252
GL_PIXEL_MAP_I_TO_A_SIZE = 3253
GL_PIXEL_MAP_R_TO_R_SIZE = 3254
GL_PIXEL_MAP_G_TO_G_SIZE = 3255
GL_PIXEL_MAP_B_TO_B_SIZE = 3256
GL_PIXEL_MAP_A_TO_A_SIZE = 3257
GL_PIXEL_MAP_S_TO_S = 3185
GL_PIXEL_MAP_I_TO_I = 3184
GL_PIXEL_MAP_I_TO_R = 3186
GL_PIXEL_MAP_I_TO_G = 3187
GL_PIXEL_MAP_I_TO_B = 3188
GL_PIXEL_MAP_I_TO_A = 3189
GL_PIXEL_MAP_R_TO_R = 3190
GL_PIXEL_MAP_G_TO_G = 3191
GL_PIXEL_MAP_B_TO_B = 3192
GL_PIXEL_MAP_A_TO_A = 3193
GL_PACK_ALIGNMENT = 3333
GL_PACK_LSB_FIRST = 3329
GL_PACK_ROW_LENGTH = 3330
GL_PACK_SKIP_PIXELS = 3332
GL_PACK_SKIP_ROWS = 3331
GL_PACK_SWAP_BYTES = 3328
GL_UNPACK_ALIGNMENT = 3317
GL_UNPACK_LSB_FIRST = 3313
GL_UNPACK_ROW_LENGTH = 3314
GL_UNPACK_SKIP_PIXELS = 3316
GL_UNPACK_SKIP_ROWS = 3315
GL_UNPACK_SWAP_BYTES = 3312
GL_ZOOM_X = 3350
GL_ZOOM_Y = 3351
GL_TEXTURE_ENV = 8960
GL_TEXTURE_ENV_MODE = 8704
GL_TEXTURE_1D = 3552
GL_TEXTURE_2D = 3553
GL_TEXTURE_WRAP_S = 10242
GL_TEXTURE_WRAP_T = 10243
GL_TEXTURE_MAG_FILTER = 10240
GL_TEXTURE_MIN_FILTER = 10241
GL_TEXTURE_ENV_COLOR = 8705
GL_TEXTURE_GEN_S = 3168
GL_TEXTURE_GEN_T = 3169
GL_TEXTURE_GEN_MODE = 9472
GL_TEXTURE_BORDER_COLOR = 4100
GL_TEXTURE_WIDTH = 4096
GL_TEXTURE_HEIGHT = 4097
GL_TEXTURE_BORDER = 4101
GL_TEXTURE_COMPONENTS = 4099
GL_TEXTURE_RED_SIZE = 32860
GL_TEXTURE_GREEN_SIZE = 32861
GL_TEXTURE_BLUE_SIZE = 32862
GL_TEXTURE_ALPHA_SIZE = 32863
GL_TEXTURE_LUMINANCE_SIZE = 32864
GL_TEXTURE_INTENSITY_SIZE = 32865
GL_NEAREST_MIPMAP_NEAREST = 9984
GL_NEAREST_MIPMAP_LINEAR = 9986
GL_LINEAR_MIPMAP_NEAREST = 9985
GL_LINEAR_MIPMAP_LINEAR = 9987
GL_OBJECT_LINEAR = 9217
GL_OBJECT_PLANE = 9473
GL_EYE_LINEAR = 9216
GL_EYE_PLANE = 9474
GL_SPHERE_MAP = 9218
GL_DECAL = 8449
GL_MODULATE = 8448
GL_NEAREST = 9728
GL_REPEAT = 10497
GL_CLAMP = 10496
GL_S = 8192
GL_T = 8193
GL_R = 8194
GL_Q = 8195
GL_TEXTURE_GEN_R = 3170
GL_TEXTURE_GEN_Q = 3171
GL_VENDOR = 7936
GL_RENDERER = 7937
GL_VERSION = 7938
GL_EXTENSIONS = 7939
GL_NO_ERROR = 0
GL_INVALID_ENUM = 1280
GL_INVALID_VALUE = 1281
GL_INVALID_OPERATION = 1282
GL_STACK_OVERFLOW = 1283
GL_STACK_UNDERFLOW = 1284
GL_OUT_OF_MEMORY = 1285
GL_CURRENT_BIT = 1
GL_POINT_BIT = 2
GL_LINE_BIT = 4
GL_POLYGON_BIT = 8
GL_POLYGON_STIPPLE_BIT = 16
GL_PIXEL_MODE_BIT = 32
GL_LIGHTING_BIT = 64
GL_FOG_BIT = 128
GL_DEPTH_BUFFER_BIT = 256
GL_ACCUM_BUFFER_BIT = 512
GL_STENCIL_BUFFER_BIT = 1024
GL_VIEWPORT_BIT = 2048
GL_TRANSFORM_BIT = 4096
GL_ENABLE_BIT = 8192
GL_COLOR_BUFFER_BIT = 16384
GL_HINT_BIT = 32768
GL_EVAL_BIT = 65536
GL_LIST_BIT = 131072
GL_TEXTURE_BIT = 262144
GL_SCISSOR_BIT = 524288
GL_ALL_ATTRIB_BITS = 1048575
GL_PROXY_TEXTURE_1D = 32867
GL_PROXY_TEXTURE_2D = 32868
GL_TEXTURE_PRIORITY = 32870
GL_TEXTURE_RESIDENT = 32871
GL_TEXTURE_BINDING_1D = 32872
GL_TEXTURE_BINDING_2D = 32873
GL_TEXTURE_INTERNAL_FORMAT = 4099
GL_ALPHA4 = 32827
GL_ALPHA8 = 32828
GL_ALPHA12 = 32829
GL_ALPHA16 = 32830
GL_LUMINANCE4 = 32831
GL_LUMINANCE8 = 32832
GL_LUMINANCE12 = 32833
GL_LUMINANCE16 = 32834
GL_LUMINANCE4_ALPHA4 = 32835
GL_LUMINANCE6_ALPHA2 = 32836
GL_LUMINANCE8_ALPHA8 = 32837
GL_LUMINANCE12_ALPHA4 = 32838
GL_LUMINANCE12_ALPHA12 = 32839
GL_LUMINANCE16_ALPHA16 = 32840
GL_INTENSITY = 32841
GL_INTENSITY4 = 32842
GL_INTENSITY8 = 32843
GL_INTENSITY12 = 32844
GL_INTENSITY16 = 32845
GL_R3_G3_B2 = 10768
GL_RGB4 = 32847
GL_RGB5 = 32848
GL_RGB8 = 32849
GL_RGB10 = 32850
GL_RGB12 = 32851
GL_RGB16 = 32852
GL_RGBA2 = 32853
GL_RGBA4 = 32854
GL_RGB5_A1 = 32855
GL_RGBA8 = 32856
GL_RGB10_A2 = 32857
GL_RGBA12 = 32858
GL_RGBA16 = 32859
GL_CLIENT_PIXEL_STORE_BIT = 1
GL_CLIENT_VERTEX_ARRAY_BIT = 2
GL_ALL_CLIENT_ATTRIB_BITS = 4294967295
GL_CLIENT_ALL_ATTRIB_BITS = 4294967295
glClearIndex = _link_function('glClearIndex', None, [GLfloat], None)
glClearColor = _link_function('glClearColor', None, [GLclampf, GLclampf, GLclampf, GLclampf], None)
glClear = _link_function('glClear', None, [GLbitfield], None)
glIndexMask = _link_function('glIndexMask', None, [GLuint], None)
glColorMask = _link_function('glColorMask', None, [GLboolean, GLboolean, GLboolean, GLboolean], None)
glAlphaFunc = _link_function('glAlphaFunc', None, [GLenum, GLclampf], None)
glBlendFunc = _link_function('glBlendFunc', None, [GLenum, GLenum], None)
glLogicOp = _link_function('glLogicOp', None, [GLenum], None)
glCullFace = _link_function('glCullFace', None, [GLenum], None)
glFrontFace = _link_function('glFrontFace', None, [GLenum], None)
glPointSize = _link_function('glPointSize', None, [GLfloat], None)
glLineWidth = _link_function('glLineWidth', None, [GLfloat], None)
glLineStipple = _link_function('glLineStipple', None, [GLint, GLushort], None)
glPolygonMode = _link_function('glPolygonMode', None, [GLenum, GLenum], None)
glPolygonOffset = _link_function('glPolygonOffset', None, [GLfloat, GLfloat], None)
glPolygonStipple = _link_function('glPolygonStipple', None, [POINTER(GLubyte)], None)
glGetPolygonStipple = _link_function('glGetPolygonStipple', None, [POINTER(GLubyte)], None)
glEdgeFlag = _link_function('glEdgeFlag', None, [GLboolean], None)
glEdgeFlagv = _link_function('glEdgeFlagv', None, [POINTER(GLboolean)], None)
glScissor = _link_function('glScissor', None, [GLint, GLint, GLsizei, GLsizei], None)
glClipPlane = _link_function('glClipPlane', None, [GLenum, POINTER(GLdouble)], None)
glGetClipPlane = _link_function('glGetClipPlane', None, [GLenum, POINTER(GLdouble)], None)
glDrawBuffer = _link_function('glDrawBuffer', None, [GLenum], None)
glReadBuffer = _link_function('glReadBuffer', None, [GLenum], None)
glEnable = _link_function('glEnable', None, [GLenum], None)
glDisable = _link_function('glDisable', None, [GLenum], None)
glIsEnabled = _link_function('glIsEnabled', GLboolean, [GLenum], None)
glEnableClientState = _link_function('glEnableClientState', None, [GLenum], None)
glDisableClientState = _link_function('glDisableClientState', None, [GLenum], None)
glGetBooleanv = _link_function('glGetBooleanv', None, [GLenum, POINTER(GLboolean)], None)
glGetDoublev = _link_function('glGetDoublev', None, [GLenum, POINTER(GLdouble)], None)
glGetFloatv = _link_function('glGetFloatv', None, [GLenum, POINTER(GLfloat)], None)
glGetIntegerv = _link_function('glGetIntegerv', None, [GLenum, POINTER(GLint)], None)
glPushAttrib = _link_function('glPushAttrib', None, [GLbitfield], None)
glPopAttrib = _link_function('glPopAttrib', None, [], None)
glPushClientAttrib = _link_function('glPushClientAttrib', None, [GLbitfield], None)
glPopClientAttrib = _link_function('glPopClientAttrib', None, [], None)
glRenderMode = _link_function('glRenderMode', GLint, [GLenum], None)
glGetError = _link_function('glGetError', GLenum, [], None)
glGetString = _link_function('glGetString', POINTER(GLubyte), [GLenum], None)
glFinish = _link_function('glFinish', None, [], None)
glFlush = _link_function('glFlush', None, [], None)
glHint = _link_function('glHint', None, [GLenum, GLenum], None)
glClearDepth = _link_function('glClearDepth', None, [GLclampd], None)
glDepthFunc = _link_function('glDepthFunc', None, [GLenum], None)
glDepthMask = _link_function('glDepthMask', None, [GLboolean], None)
glDepthRange = _link_function('glDepthRange', None, [GLclampd, GLclampd], None)
glClearAccum = _link_function('glClearAccum', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glAccum = _link_function('glAccum', None, [GLenum, GLfloat], None)
glMatrixMode = _link_function('glMatrixMode', None, [GLenum], None)
glOrtho = _link_function('glOrtho', None, [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble], None)
glFrustum = _link_function('glFrustum', None, [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble], None)
glViewport = _link_function('glViewport', None, [GLint, GLint, GLsizei, GLsizei], None)
glPushMatrix = _link_function('glPushMatrix', None, [], None)
glPopMatrix = _link_function('glPopMatrix', None, [], None)
glLoadIdentity = _link_function('glLoadIdentity', None, [], None)
glLoadMatrixd = _link_function('glLoadMatrixd', None, [POINTER(GLdouble)], None)
glLoadMatrixf = _link_function('glLoadMatrixf', None, [POINTER(GLfloat)], None)
glMultMatrixd = _link_function('glMultMatrixd', None, [POINTER(GLdouble)], None)
glMultMatrixf = _link_function('glMultMatrixf', None, [POINTER(GLfloat)], None)
glRotated = _link_function('glRotated', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
glRotatef = _link_function('glRotatef', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glScaled = _link_function('glScaled', None, [GLdouble, GLdouble, GLdouble], None)
glScalef = _link_function('glScalef', None, [GLfloat, GLfloat, GLfloat], None)
glTranslated = _link_function('glTranslated', None, [GLdouble, GLdouble, GLdouble], None)
glTranslatef = _link_function('glTranslatef', None, [GLfloat, GLfloat, GLfloat], None)
glIsList = _link_function('glIsList', GLboolean, [GLuint], None)
glDeleteLists = _link_function('glDeleteLists', None, [GLuint, GLsizei], None)
glGenLists = _link_function('glGenLists', GLuint, [GLsizei], None)
glNewList = _link_function('glNewList', None, [GLuint, GLenum], None)
glEndList = _link_function('glEndList', None, [], None)
glCallList = _link_function('glCallList', None, [GLuint], None)
glCallLists = _link_function('glCallLists', None, [GLsizei, GLenum, POINTER(GLvoid)], None)
glListBase = _link_function('glListBase', None, [GLuint], None)
glBegin = _link_function('glBegin', None, [GLenum], None)
glEnd = _link_function('glEnd', None, [], None)
glVertex2d = _link_function('glVertex2d', None, [GLdouble, GLdouble], None)
glVertex2f = _link_function('glVertex2f', None, [GLfloat, GLfloat], None)
glVertex2i = _link_function('glVertex2i', None, [GLint, GLint], None)
glVertex2s = _link_function('glVertex2s', None, [GLshort, GLshort], None)
glVertex3d = _link_function('glVertex3d', None, [GLdouble, GLdouble, GLdouble], None)
glVertex3f = _link_function('glVertex3f', None, [GLfloat, GLfloat, GLfloat], None)
glVertex3i = _link_function('glVertex3i', None, [GLint, GLint, GLint], None)
glVertex3s = _link_function('glVertex3s', None, [GLshort, GLshort, GLshort], None)
glVertex4d = _link_function('glVertex4d', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
glVertex4f = _link_function('glVertex4f', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glVertex4i = _link_function('glVertex4i', None, [GLint, GLint, GLint, GLint], None)
glVertex4s = _link_function('glVertex4s', None, [GLshort, GLshort, GLshort, GLshort], None)
glVertex2dv = _link_function('glVertex2dv', None, [POINTER(GLdouble)], None)
glVertex2fv = _link_function('glVertex2fv', None, [POINTER(GLfloat)], None)
glVertex2iv = _link_function('glVertex2iv', None, [POINTER(GLint)], None)
glVertex2sv = _link_function('glVertex2sv', None, [POINTER(GLshort)], None)
glVertex3dv = _link_function('glVertex3dv', None, [POINTER(GLdouble)], None)
glVertex3fv = _link_function('glVertex3fv', None, [POINTER(GLfloat)], None)
glVertex3iv = _link_function('glVertex3iv', None, [POINTER(GLint)], None)
glVertex3sv = _link_function('glVertex3sv', None, [POINTER(GLshort)], None)
glVertex4dv = _link_function('glVertex4dv', None, [POINTER(GLdouble)], None)
glVertex4fv = _link_function('glVertex4fv', None, [POINTER(GLfloat)], None)
glVertex4iv = _link_function('glVertex4iv', None, [POINTER(GLint)], None)
glVertex4sv = _link_function('glVertex4sv', None, [POINTER(GLshort)], None)
glNormal3b = _link_function('glNormal3b', None, [GLbyte, GLbyte, GLbyte], None)
glNormal3d = _link_function('glNormal3d', None, [GLdouble, GLdouble, GLdouble], None)
glNormal3f = _link_function('glNormal3f', None, [GLfloat, GLfloat, GLfloat], None)
glNormal3i = _link_function('glNormal3i', None, [GLint, GLint, GLint], None)
glNormal3s = _link_function('glNormal3s', None, [GLshort, GLshort, GLshort], None)
glNormal3bv = _link_function('glNormal3bv', None, [POINTER(GLbyte)], None)
glNormal3dv = _link_function('glNormal3dv', None, [POINTER(GLdouble)], None)
glNormal3fv = _link_function('glNormal3fv', None, [POINTER(GLfloat)], None)
glNormal3iv = _link_function('glNormal3iv', None, [POINTER(GLint)], None)
glNormal3sv = _link_function('glNormal3sv', None, [POINTER(GLshort)], None)
glIndexd = _link_function('glIndexd', None, [GLdouble], None)
glIndexf = _link_function('glIndexf', None, [GLfloat], None)
glIndexi = _link_function('glIndexi', None, [GLint], None)
glIndexs = _link_function('glIndexs', None, [GLshort], None)
glIndexub = _link_function('glIndexub', None, [GLubyte], None)
glIndexdv = _link_function('glIndexdv', None, [POINTER(GLdouble)], None)
glIndexfv = _link_function('glIndexfv', None, [POINTER(GLfloat)], None)
glIndexiv = _link_function('glIndexiv', None, [POINTER(GLint)], None)
glIndexsv = _link_function('glIndexsv', None, [POINTER(GLshort)], None)
glIndexubv = _link_function('glIndexubv', None, [POINTER(GLubyte)], None)
glColor3b = _link_function('glColor3b', None, [GLbyte, GLbyte, GLbyte], None)
glColor3d = _link_function('glColor3d', None, [GLdouble, GLdouble, GLdouble], None)
glColor3f = _link_function('glColor3f', None, [GLfloat, GLfloat, GLfloat], None)
glColor3i = _link_function('glColor3i', None, [GLint, GLint, GLint], None)
glColor3s = _link_function('glColor3s', None, [GLshort, GLshort, GLshort], None)
glColor3ub = _link_function('glColor3ub', None, [GLubyte, GLubyte, GLubyte], None)
glColor3ui = _link_function('glColor3ui', None, [GLuint, GLuint, GLuint], None)
glColor3us = _link_function('glColor3us', None, [GLushort, GLushort, GLushort], None)
glColor4b = _link_function('glColor4b', None, [GLbyte, GLbyte, GLbyte, GLbyte], None)
glColor4d = _link_function('glColor4d', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
glColor4f = _link_function('glColor4f', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glColor4i = _link_function('glColor4i', None, [GLint, GLint, GLint, GLint], None)
glColor4s = _link_function('glColor4s', None, [GLshort, GLshort, GLshort, GLshort], None)
glColor4ub = _link_function('glColor4ub', None, [GLubyte, GLubyte, GLubyte, GLubyte], None)
glColor4ui = _link_function('glColor4ui', None, [GLuint, GLuint, GLuint, GLuint], None)
glColor4us = _link_function('glColor4us', None, [GLushort, GLushort, GLushort, GLushort], None)
glColor3bv = _link_function('glColor3bv', None, [POINTER(GLbyte)], None)
glColor3dv = _link_function('glColor3dv', None, [POINTER(GLdouble)], None)
glColor3fv = _link_function('glColor3fv', None, [POINTER(GLfloat)], None)
glColor3iv = _link_function('glColor3iv', None, [POINTER(GLint)], None)
glColor3sv = _link_function('glColor3sv', None, [POINTER(GLshort)], None)
glColor3ubv = _link_function('glColor3ubv', None, [POINTER(GLubyte)], None)
glColor3uiv = _link_function('glColor3uiv', None, [POINTER(GLuint)], None)
glColor3usv = _link_function('glColor3usv', None, [POINTER(GLushort)], None)
glColor4bv = _link_function('glColor4bv', None, [POINTER(GLbyte)], None)
glColor4dv = _link_function('glColor4dv', None, [POINTER(GLdouble)], None)
glColor4fv = _link_function('glColor4fv', None, [POINTER(GLfloat)], None)
glColor4iv = _link_function('glColor4iv', None, [POINTER(GLint)], None)
glColor4sv = _link_function('glColor4sv', None, [POINTER(GLshort)], None)
glColor4ubv = _link_function('glColor4ubv', None, [POINTER(GLubyte)], None)
glColor4uiv = _link_function('glColor4uiv', None, [POINTER(GLuint)], None)
glColor4usv = _link_function('glColor4usv', None, [POINTER(GLushort)], None)
glTexCoord1d = _link_function('glTexCoord1d', None, [GLdouble], None)
glTexCoord1f = _link_function('glTexCoord1f', None, [GLfloat], None)
glTexCoord1i = _link_function('glTexCoord1i', None, [GLint], None)
glTexCoord1s = _link_function('glTexCoord1s', None, [GLshort], None)
glTexCoord2d = _link_function('glTexCoord2d', None, [GLdouble, GLdouble], None)
glTexCoord2f = _link_function('glTexCoord2f', None, [GLfloat, GLfloat], None)
glTexCoord2i = _link_function('glTexCoord2i', None, [GLint, GLint], None)
glTexCoord2s = _link_function('glTexCoord2s', None, [GLshort, GLshort], None)
glTexCoord3d = _link_function('glTexCoord3d', None, [GLdouble, GLdouble, GLdouble], None)
glTexCoord3f = _link_function('glTexCoord3f', None, [GLfloat, GLfloat, GLfloat], None)
glTexCoord3i = _link_function('glTexCoord3i', None, [GLint, GLint, GLint], None)
glTexCoord3s = _link_function('glTexCoord3s', None, [GLshort, GLshort, GLshort], None)
glTexCoord4d = _link_function('glTexCoord4d', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
glTexCoord4f = _link_function('glTexCoord4f', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glTexCoord4i = _link_function('glTexCoord4i', None, [GLint, GLint, GLint, GLint], None)
glTexCoord4s = _link_function('glTexCoord4s', None, [GLshort, GLshort, GLshort, GLshort], None)
glTexCoord1dv = _link_function('glTexCoord1dv', None, [POINTER(GLdouble)], None)
glTexCoord1fv = _link_function('glTexCoord1fv', None, [POINTER(GLfloat)], None)
glTexCoord1iv = _link_function('glTexCoord1iv', None, [POINTER(GLint)], None)
glTexCoord1sv = _link_function('glTexCoord1sv', None, [POINTER(GLshort)], None)
glTexCoord2dv = _link_function('glTexCoord2dv', None, [POINTER(GLdouble)], None)
glTexCoord2fv = _link_function('glTexCoord2fv', None, [POINTER(GLfloat)], None)
glTexCoord2iv = _link_function('glTexCoord2iv', None, [POINTER(GLint)], None)
glTexCoord2sv = _link_function('glTexCoord2sv', None, [POINTER(GLshort)], None)
glTexCoord3dv = _link_function('glTexCoord3dv', None, [POINTER(GLdouble)], None)
glTexCoord3fv = _link_function('glTexCoord3fv', None, [POINTER(GLfloat)], None)
glTexCoord3iv = _link_function('glTexCoord3iv', None, [POINTER(GLint)], None)
glTexCoord3sv = _link_function('glTexCoord3sv', None, [POINTER(GLshort)], None)
glTexCoord4dv = _link_function('glTexCoord4dv', None, [POINTER(GLdouble)], None)
glTexCoord4fv = _link_function('glTexCoord4fv', None, [POINTER(GLfloat)], None)
glTexCoord4iv = _link_function('glTexCoord4iv', None, [POINTER(GLint)], None)
glTexCoord4sv = _link_function('glTexCoord4sv', None, [POINTER(GLshort)], None)
glRasterPos2d = _link_function('glRasterPos2d', None, [GLdouble, GLdouble], None)
glRasterPos2f = _link_function('glRasterPos2f', None, [GLfloat, GLfloat], None)
glRasterPos2i = _link_function('glRasterPos2i', None, [GLint, GLint], None)
glRasterPos2s = _link_function('glRasterPos2s', None, [GLshort, GLshort], None)
glRasterPos3d = _link_function('glRasterPos3d', None, [GLdouble, GLdouble, GLdouble], None)
glRasterPos3f = _link_function('glRasterPos3f', None, [GLfloat, GLfloat, GLfloat], None)
glRasterPos3i = _link_function('glRasterPos3i', None, [GLint, GLint, GLint], None)
glRasterPos3s = _link_function('glRasterPos3s', None, [GLshort, GLshort, GLshort], None)
glRasterPos4d = _link_function('glRasterPos4d', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
glRasterPos4f = _link_function('glRasterPos4f', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glRasterPos4i = _link_function('glRasterPos4i', None, [GLint, GLint, GLint, GLint], None)
glRasterPos4s = _link_function('glRasterPos4s', None, [GLshort, GLshort, GLshort, GLshort], None)
glRasterPos2dv = _link_function('glRasterPos2dv', None, [POINTER(GLdouble)], None)
glRasterPos2fv = _link_function('glRasterPos2fv', None, [POINTER(GLfloat)], None)
glRasterPos2iv = _link_function('glRasterPos2iv', None, [POINTER(GLint)], None)
glRasterPos2sv = _link_function('glRasterPos2sv', None, [POINTER(GLshort)], None)
glRasterPos3dv = _link_function('glRasterPos3dv', None, [POINTER(GLdouble)], None)
glRasterPos3fv = _link_function('glRasterPos3fv', None, [POINTER(GLfloat)], None)
glRasterPos3iv = _link_function('glRasterPos3iv', None, [POINTER(GLint)], None)
glRasterPos3sv = _link_function('glRasterPos3sv', None, [POINTER(GLshort)], None)
glRasterPos4dv = _link_function('glRasterPos4dv', None, [POINTER(GLdouble)], None)
glRasterPos4fv = _link_function('glRasterPos4fv', None, [POINTER(GLfloat)], None)
glRasterPos4iv = _link_function('glRasterPos4iv', None, [POINTER(GLint)], None)
glRasterPos4sv = _link_function('glRasterPos4sv', None, [POINTER(GLshort)], None)
glRectd = _link_function('glRectd', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)
glRectf = _link_function('glRectf', None, [GLfloat, GLfloat, GLfloat, GLfloat], None)
glRecti = _link_function('glRecti', None, [GLint, GLint, GLint, GLint], None)
glRects = _link_function('glRects', None, [GLshort, GLshort, GLshort, GLshort], None)
glRectdv = _link_function('glRectdv', None, [POINTER(GLdouble), POINTER(GLdouble)], None)
glRectfv = _link_function('glRectfv', None, [POINTER(GLfloat), POINTER(GLfloat)], None)
glRectiv = _link_function('glRectiv', None, [POINTER(GLint), POINTER(GLint)], None)
glRectsv = _link_function('glRectsv', None, [POINTER(GLshort), POINTER(GLshort)], None)
glVertexPointer = _link_function('glVertexPointer', None, [GLint, GLenum, GLsizei, POINTER(GLvoid)], None)
glNormalPointer = _link_function('glNormalPointer', None, [GLenum, GLsizei, POINTER(GLvoid)], None)
glColorPointer = _link_function('glColorPointer', None, [GLint, GLenum, GLsizei, POINTER(GLvoid)], None)
glIndexPointer = _link_function('glIndexPointer', None, [GLenum, GLsizei, POINTER(GLvoid)], None)
glTexCoordPointer = _link_function('glTexCoordPointer', None, [GLint, GLenum, GLsizei, POINTER(GLvoid)], None)
glEdgeFlagPointer = _link_function('glEdgeFlagPointer', None, [GLsizei, POINTER(GLvoid)], None)
glGetPointerv = _link_function('glGetPointerv', None, [GLenum, POINTER(POINTER(GLvoid))], None)
glArrayElement = _link_function('glArrayElement', None, [GLint], None)
glDrawArrays = _link_function('glDrawArrays', None, [GLenum, GLint, GLsizei], None)
glDrawElements = _link_function('glDrawElements', None, [GLenum, GLsizei, GLenum, POINTER(GLvoid)], None)
glInterleavedArrays = _link_function('glInterleavedArrays', None, [GLenum, GLsizei, POINTER(GLvoid)], None)
glShadeModel = _link_function('glShadeModel', None, [GLenum], None)
glLightf = _link_function('glLightf', None, [GLenum, GLenum, GLfloat], None)
glLighti = _link_function('glLighti', None, [GLenum, GLenum, GLint], None)
glLightfv = _link_function('glLightfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glLightiv = _link_function('glLightiv', None, [GLenum, GLenum, POINTER(GLint)], None)
glGetLightfv = _link_function('glGetLightfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetLightiv = _link_function('glGetLightiv', None, [GLenum, GLenum, POINTER(GLint)], None)
glLightModelf = _link_function('glLightModelf', None, [GLenum, GLfloat], None)
glLightModeli = _link_function('glLightModeli', None, [GLenum, GLint], None)
glLightModelfv = _link_function('glLightModelfv', None, [GLenum, POINTER(GLfloat)], None)
glLightModeliv = _link_function('glLightModeliv', None, [GLenum, POINTER(GLint)], None)
glMaterialf = _link_function('glMaterialf', None, [GLenum, GLenum, GLfloat], None)
glMateriali = _link_function('glMateriali', None, [GLenum, GLenum, GLint], None)
glMaterialfv = _link_function('glMaterialfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glMaterialiv = _link_function('glMaterialiv', None, [GLenum, GLenum, POINTER(GLint)], None)
glGetMaterialfv = _link_function('glGetMaterialfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetMaterialiv = _link_function('glGetMaterialiv', None, [GLenum, GLenum, POINTER(GLint)], None)
glColorMaterial = _link_function('glColorMaterial', None, [GLenum, GLenum], None)
glPixelZoom = _link_function('glPixelZoom', None, [GLfloat, GLfloat], None)
glPixelStoref = _link_function('glPixelStoref', None, [GLenum, GLfloat], None)
glPixelStorei = _link_function('glPixelStorei', None, [GLenum, GLint], None)
glPixelTransferf = _link_function('glPixelTransferf', None, [GLenum, GLfloat], None)
glPixelTransferi = _link_function('glPixelTransferi', None, [GLenum, GLint], None)
glPixelMapfv = _link_function('glPixelMapfv', None, [GLenum, GLsizei, POINTER(GLfloat)], None)
glPixelMapuiv = _link_function('glPixelMapuiv', None, [GLenum, GLsizei, POINTER(GLuint)], None)
glPixelMapusv = _link_function('glPixelMapusv', None, [GLenum, GLsizei, POINTER(GLushort)], None)
glGetPixelMapfv = _link_function('glGetPixelMapfv', None, [GLenum, POINTER(GLfloat)], None)
glGetPixelMapuiv = _link_function('glGetPixelMapuiv', None, [GLenum, POINTER(GLuint)], None)
glGetPixelMapusv = _link_function('glGetPixelMapusv', None, [GLenum, POINTER(GLushort)], None)
glBitmap = _link_function('glBitmap', None, [GLsizei, GLsizei, GLfloat, GLfloat, GLfloat, GLfloat, POINTER(GLubyte)], None)
glReadPixels = _link_function('glReadPixels', None, [GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glDrawPixels = _link_function('glDrawPixels', None, [GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glCopyPixels = _link_function('glCopyPixels', None, [GLint, GLint, GLsizei, GLsizei, GLenum], None)
glStencilFunc = _link_function('glStencilFunc', None, [GLenum, GLint, GLuint], None)
glStencilMask = _link_function('glStencilMask', None, [GLuint], None)
glStencilOp = _link_function('glStencilOp', None, [GLenum, GLenum, GLenum], None)
glClearStencil = _link_function('glClearStencil', None, [GLint], None)
glTexGend = _link_function('glTexGend', None, [GLenum, GLenum, GLdouble], None)
glTexGenf = _link_function('glTexGenf', None, [GLenum, GLenum, GLfloat], None)
glTexGeni = _link_function('glTexGeni', None, [GLenum, GLenum, GLint], None)
glTexGendv = _link_function('glTexGendv', None, [GLenum, GLenum, POINTER(GLdouble)], None)
glTexGenfv = _link_function('glTexGenfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glTexGeniv = _link_function('glTexGeniv', None, [GLenum, GLenum, POINTER(GLint)], None)
glGetTexGendv = _link_function('glGetTexGendv', None, [GLenum, GLenum, POINTER(GLdouble)], None)
glGetTexGenfv = _link_function('glGetTexGenfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetTexGeniv = _link_function('glGetTexGeniv', None, [GLenum, GLenum, POINTER(GLint)], None)
glTexEnvf = _link_function('glTexEnvf', None, [GLenum, GLenum, GLfloat], None)
glTexEnvi = _link_function('glTexEnvi', None, [GLenum, GLenum, GLint], None)
glTexEnvfv = _link_function('glTexEnvfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glTexEnviv = _link_function('glTexEnviv', None, [GLenum, GLenum, POINTER(GLint)], None)
glGetTexEnvfv = _link_function('glGetTexEnvfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetTexEnviv = _link_function('glGetTexEnviv', None, [GLenum, GLenum, POINTER(GLint)], None)
glTexParameterf = _link_function('glTexParameterf', None, [GLenum, GLenum, GLfloat], None)
glTexParameteri = _link_function('glTexParameteri', None, [GLenum, GLenum, GLint], None)
glTexParameterfv = _link_function('glTexParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glTexParameteriv = _link_function('glTexParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glGetTexParameterfv = _link_function('glGetTexParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetTexParameteriv = _link_function('glGetTexParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glGetTexLevelParameterfv = _link_function('glGetTexLevelParameterfv', None, [GLenum, GLint, GLenum, POINTER(GLfloat)], None)
glGetTexLevelParameteriv = _link_function('glGetTexLevelParameteriv', None, [GLenum, GLint, GLenum, POINTER(GLint)], None)
glTexImage1D = _link_function('glTexImage1D', None, [GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)], None)
glTexImage2D = _link_function('glTexImage2D', None, [GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)], None)
glGetTexImage = _link_function('glGetTexImage', None, [GLenum, GLint, GLenum, GLenum, POINTER(GLvoid)], None)
glGenTextures = _link_function('glGenTextures', None, [GLsizei, POINTER(GLuint)], None)
glDeleteTextures = _link_function('glDeleteTextures', None, [GLsizei, POINTER(GLuint)], None)
glBindTexture = _link_function('glBindTexture', None, [GLenum, GLuint], None)
glPrioritizeTextures = _link_function('glPrioritizeTextures', None, [GLsizei, POINTER(GLuint), POINTER(GLclampf)], None)
glAreTexturesResident = _link_function('glAreTexturesResident', GLboolean, [GLsizei, POINTER(GLuint), POINTER(GLboolean)], None)
glIsTexture = _link_function('glIsTexture', GLboolean, [GLuint], None)
glTexSubImage1D = _link_function('glTexSubImage1D', None, [GLenum, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glTexSubImage2D = _link_function('glTexSubImage2D', None, [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glCopyTexImage1D = _link_function('glCopyTexImage1D', None, [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint], None)
glCopyTexImage2D = _link_function('glCopyTexImage2D', None, [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint], None)
glCopyTexSubImage1D = _link_function('glCopyTexSubImage1D', None, [GLenum, GLint, GLint, GLint, GLint, GLsizei], None)
glCopyTexSubImage2D = _link_function('glCopyTexSubImage2D', None, [GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei], None)
glMap1d = _link_function('glMap1d', None, [GLenum, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)], None)
glMap1f = _link_function('glMap1f', None, [GLenum, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)], None)
glMap2d = _link_function('glMap2d', None, [GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)], None)
glMap2f = _link_function('glMap2f', None, [GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)], None)
glGetMapdv = _link_function('glGetMapdv', None, [GLenum, GLenum, POINTER(GLdouble)], None)
glGetMapfv = _link_function('glGetMapfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetMapiv = _link_function('glGetMapiv', None, [GLenum, GLenum, POINTER(GLint)], None)
glEvalCoord1d = _link_function('glEvalCoord1d', None, [GLdouble], None)
glEvalCoord1f = _link_function('glEvalCoord1f', None, [GLfloat], None)
glEvalCoord1dv = _link_function('glEvalCoord1dv', None, [POINTER(GLdouble)], None)
glEvalCoord1fv = _link_function('glEvalCoord1fv', None, [POINTER(GLfloat)], None)
glEvalCoord2d = _link_function('glEvalCoord2d', None, [GLdouble, GLdouble], None)
glEvalCoord2f = _link_function('glEvalCoord2f', None, [GLfloat, GLfloat], None)
glEvalCoord2dv = _link_function('glEvalCoord2dv', None, [POINTER(GLdouble)], None)
glEvalCoord2fv = _link_function('glEvalCoord2fv', None, [POINTER(GLfloat)], None)
glMapGrid1d = _link_function('glMapGrid1d', None, [GLint, GLdouble, GLdouble], None)
glMapGrid1f = _link_function('glMapGrid1f', None, [GLint, GLfloat, GLfloat], None)
glMapGrid2d = _link_function('glMapGrid2d', None, [GLint, GLdouble, GLdouble, GLint, GLdouble, GLdouble], None)
glMapGrid2f = _link_function('glMapGrid2f', None, [GLint, GLfloat, GLfloat, GLint, GLfloat, GLfloat], None)
glEvalPoint1 = _link_function('glEvalPoint1', None, [GLint], None)
glEvalPoint2 = _link_function('glEvalPoint2', None, [GLint, GLint], None)
glEvalMesh1 = _link_function('glEvalMesh1', None, [GLenum, GLint, GLint], None)
glEvalMesh2 = _link_function('glEvalMesh2', None, [GLenum, GLint, GLint, GLint, GLint], None)
glFogf = _link_function('glFogf', None, [GLenum, GLfloat], None)
glFogi = _link_function('glFogi', None, [GLenum, GLint], None)
glFogfv = _link_function('glFogfv', None, [GLenum, POINTER(GLfloat)], None)
glFogiv = _link_function('glFogiv', None, [GLenum, POINTER(GLint)], None)
glFeedbackBuffer = _link_function('glFeedbackBuffer', None, [GLsizei, GLenum, POINTER(GLfloat)], None)
glPassThrough = _link_function('glPassThrough', None, [GLfloat], None)
glSelectBuffer = _link_function('glSelectBuffer', None, [GLsizei, POINTER(GLuint)], None)
glInitNames = _link_function('glInitNames', None, [], None)
glLoadName = _link_function('glLoadName', None, [GLuint], None)
glPushName = _link_function('glPushName', None, [GLuint], None)
glPopName = _link_function('glPopName', None, [], None)
GL_RESCALE_NORMAL = 32826
GL_CLAMP_TO_EDGE = 33071
GL_MAX_ELEMENTS_VERTICES = 33000
GL_MAX_ELEMENTS_INDICES = 33001
GL_BGR = 32992
GL_BGRA = 32993
GL_UNSIGNED_BYTE_3_3_2 = 32818
GL_UNSIGNED_BYTE_2_3_3_REV = 33634
GL_UNSIGNED_SHORT_5_6_5 = 33635
GL_UNSIGNED_SHORT_5_6_5_REV = 33636
GL_UNSIGNED_SHORT_4_4_4_4 = 32819
GL_UNSIGNED_SHORT_4_4_4_4_REV = 33637
GL_UNSIGNED_SHORT_5_5_5_1 = 32820
GL_UNSIGNED_SHORT_1_5_5_5_REV = 33638
GL_UNSIGNED_INT_8_8_8_8 = 32821
GL_UNSIGNED_INT_8_8_8_8_REV = 33639
GL_UNSIGNED_INT_10_10_10_2 = 32822
GL_UNSIGNED_INT_2_10_10_10_REV = 33640
GL_LIGHT_MODEL_COLOR_CONTROL = 33272
GL_SINGLE_COLOR = 33273
GL_SEPARATE_SPECULAR_COLOR = 33274
GL_TEXTURE_MIN_LOD = 33082
GL_TEXTURE_MAX_LOD = 33083
GL_TEXTURE_BASE_LEVEL = 33084
GL_TEXTURE_MAX_LEVEL = 33085
GL_SMOOTH_POINT_SIZE_RANGE = 2834
GL_SMOOTH_POINT_SIZE_GRANULARITY = 2835
GL_SMOOTH_LINE_WIDTH_RANGE = 2850
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 2851
GL_ALIASED_POINT_SIZE_RANGE = 33901
GL_ALIASED_LINE_WIDTH_RANGE = 33902
GL_PACK_SKIP_IMAGES = 32875
GL_PACK_IMAGE_HEIGHT = 32876
GL_UNPACK_SKIP_IMAGES = 32877
GL_UNPACK_IMAGE_HEIGHT = 32878
GL_TEXTURE_3D = 32879
GL_PROXY_TEXTURE_3D = 32880
GL_TEXTURE_DEPTH = 32881
GL_TEXTURE_WRAP_R = 32882
GL_MAX_3D_TEXTURE_SIZE = 32883
GL_TEXTURE_BINDING_3D = 32874
glDrawRangeElements = _link_function('glDrawRangeElements', None, [GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(GLvoid)], None)
glTexImage3D = _link_function('glTexImage3D', None, [GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)], None)
glTexSubImage3D = _link_function('glTexSubImage3D', None, [GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glCopyTexSubImage3D = _link_function('glCopyTexSubImage3D', None, [GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei], None)
PFNGLDRAWRANGEELEMENTSPROC = CFUNCTYPE(None, GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(GLvoid))
PFNGLTEXIMAGE3DPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid))
PFNGLTEXSUBIMAGE3DPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid))
PFNGLCOPYTEXSUBIMAGE3DPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei)
GL_CONSTANT_COLOR = 32769
GL_ONE_MINUS_CONSTANT_COLOR = 32770
GL_CONSTANT_ALPHA = 32771
GL_ONE_MINUS_CONSTANT_ALPHA = 32772
GL_COLOR_TABLE = 32976
GL_POST_CONVOLUTION_COLOR_TABLE = 32977
GL_POST_COLOR_MATRIX_COLOR_TABLE = 32978
GL_PROXY_COLOR_TABLE = 32979
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 32980
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 32981
GL_COLOR_TABLE_SCALE = 32982
GL_COLOR_TABLE_BIAS = 32983
GL_COLOR_TABLE_FORMAT = 32984
GL_COLOR_TABLE_WIDTH = 32985
GL_COLOR_TABLE_RED_SIZE = 32986
GL_COLOR_TABLE_GREEN_SIZE = 32987
GL_COLOR_TABLE_BLUE_SIZE = 32988
GL_COLOR_TABLE_ALPHA_SIZE = 32989
GL_COLOR_TABLE_LUMINANCE_SIZE = 32990
GL_COLOR_TABLE_INTENSITY_SIZE = 32991
GL_CONVOLUTION_1D = 32784
GL_CONVOLUTION_2D = 32785
GL_SEPARABLE_2D = 32786
GL_CONVOLUTION_BORDER_MODE = 32787
GL_CONVOLUTION_FILTER_SCALE = 32788
GL_CONVOLUTION_FILTER_BIAS = 32789
GL_REDUCE = 32790
GL_CONVOLUTION_FORMAT = 32791
GL_CONVOLUTION_WIDTH = 32792
GL_CONVOLUTION_HEIGHT = 32793
GL_MAX_CONVOLUTION_WIDTH = 32794
GL_MAX_CONVOLUTION_HEIGHT = 32795
GL_POST_CONVOLUTION_RED_SCALE = 32796
GL_POST_CONVOLUTION_GREEN_SCALE = 32797
GL_POST_CONVOLUTION_BLUE_SCALE = 32798
GL_POST_CONVOLUTION_ALPHA_SCALE = 32799
GL_POST_CONVOLUTION_RED_BIAS = 32800
GL_POST_CONVOLUTION_GREEN_BIAS = 32801
GL_POST_CONVOLUTION_BLUE_BIAS = 32802
GL_POST_CONVOLUTION_ALPHA_BIAS = 32803
GL_CONSTANT_BORDER = 33105
GL_REPLICATE_BORDER = 33107
GL_CONVOLUTION_BORDER_COLOR = 33108
GL_COLOR_MATRIX = 32945
GL_COLOR_MATRIX_STACK_DEPTH = 32946
GL_MAX_COLOR_MATRIX_STACK_DEPTH = 32947
GL_POST_COLOR_MATRIX_RED_SCALE = 32948
GL_POST_COLOR_MATRIX_GREEN_SCALE = 32949
GL_POST_COLOR_MATRIX_BLUE_SCALE = 32950
GL_POST_COLOR_MATRIX_ALPHA_SCALE = 32951
GL_POST_COLOR_MATRIX_RED_BIAS = 32952
GL_POST_COLOR_MATRIX_GREEN_BIAS = 32953
GL_POST_COLOR_MATRIX_BLUE_BIAS = 32954
GL_POST_COLOR_MATRIX_ALPHA_BIAS = 32955
GL_HISTOGRAM = 32804
GL_PROXY_HISTOGRAM = 32805
GL_HISTOGRAM_WIDTH = 32806
GL_HISTOGRAM_FORMAT = 32807
GL_HISTOGRAM_RED_SIZE = 32808
GL_HISTOGRAM_GREEN_SIZE = 32809
GL_HISTOGRAM_BLUE_SIZE = 32810
GL_HISTOGRAM_ALPHA_SIZE = 32811
GL_HISTOGRAM_LUMINANCE_SIZE = 32812
GL_HISTOGRAM_SINK = 32813
GL_MINMAX = 32814
GL_MINMAX_FORMAT = 32815
GL_MINMAX_SINK = 32816
GL_TABLE_TOO_LARGE = 32817
GL_BLEND_EQUATION = 32777
GL_MIN = 32775
GL_MAX = 32776
GL_FUNC_ADD = 32774
GL_FUNC_SUBTRACT = 32778
GL_FUNC_REVERSE_SUBTRACT = 32779
GL_BLEND_COLOR = 32773
glColorTable = _link_function('glColorTable', None, [GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glColorSubTable = _link_function('glColorSubTable', None, [GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glColorTableParameteriv = _link_function('glColorTableParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glColorTableParameterfv = _link_function('glColorTableParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glCopyColorSubTable = _link_function('glCopyColorSubTable', None, [GLenum, GLsizei, GLint, GLint, GLsizei], None)
glCopyColorTable = _link_function('glCopyColorTable', None, [GLenum, GLenum, GLint, GLint, GLsizei], None)
glGetColorTable = _link_function('glGetColorTable', None, [GLenum, GLenum, GLenum, POINTER(GLvoid)], None)
glGetColorTableParameterfv = _link_function('glGetColorTableParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetColorTableParameteriv = _link_function('glGetColorTableParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glBlendEquation = _link_function('glBlendEquation', None, [GLenum], None)
glBlendColor = _link_function('glBlendColor', None, [GLclampf, GLclampf, GLclampf, GLclampf], None)
glHistogram = _link_function('glHistogram', None, [GLenum, GLsizei, GLenum, GLboolean], None)
glResetHistogram = _link_function('glResetHistogram', None, [GLenum], None)
glGetHistogram = _link_function('glGetHistogram', None, [GLenum, GLboolean, GLenum, GLenum, POINTER(GLvoid)], None)
glGetHistogramParameterfv = _link_function('glGetHistogramParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetHistogramParameteriv = _link_function('glGetHistogramParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glMinmax = _link_function('glMinmax', None, [GLenum, GLenum, GLboolean], None)
glResetMinmax = _link_function('glResetMinmax', None, [GLenum], None)
glGetMinmax = _link_function('glGetMinmax', None, [GLenum, GLboolean, GLenum, GLenum, POINTER(GLvoid)], None)
glGetMinmaxParameterfv = _link_function('glGetMinmaxParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetMinmaxParameteriv = _link_function('glGetMinmaxParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glConvolutionFilter1D = _link_function('glConvolutionFilter1D', None, [GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glConvolutionFilter2D = _link_function('glConvolutionFilter2D', None, [GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)], None)
glConvolutionParameterf = _link_function('glConvolutionParameterf', None, [GLenum, GLenum, GLfloat], None)
glConvolutionParameterfv = _link_function('glConvolutionParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glConvolutionParameteri = _link_function('glConvolutionParameteri', None, [GLenum, GLenum, GLint], None)
glConvolutionParameteriv = _link_function('glConvolutionParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glCopyConvolutionFilter1D = _link_function('glCopyConvolutionFilter1D', None, [GLenum, GLenum, GLint, GLint, GLsizei], None)
glCopyConvolutionFilter2D = _link_function('glCopyConvolutionFilter2D', None, [GLenum, GLenum, GLint, GLint, GLsizei, GLsizei], None)
glGetConvolutionFilter = _link_function('glGetConvolutionFilter', None, [GLenum, GLenum, GLenum, POINTER(GLvoid)], None)
glGetConvolutionParameterfv = _link_function('glGetConvolutionParameterfv', None, [GLenum, GLenum, POINTER(GLfloat)], None)
glGetConvolutionParameteriv = _link_function('glGetConvolutionParameteriv', None, [GLenum, GLenum, POINTER(GLint)], None)
glSeparableFilter2D = _link_function('glSeparableFilter2D', None, [GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid), POINTER(GLvoid)], None)
glGetSeparableFilter = _link_function('glGetSeparableFilter', None, [GLenum, GLenum, GLenum, POINTER(GLvoid), POINTER(GLvoid), POINTER(GLvoid)], None)
PFNGLBLENDCOLORPROC = CFUNCTYPE(None, GLclampf, GLclampf, GLclampf, GLclampf)
PFNGLBLENDEQUATIONPROC = CFUNCTYPE(None, GLenum)
GL_TEXTURE0 = 33984
GL_TEXTURE1 = 33985
GL_TEXTURE2 = 33986
GL_TEXTURE3 = 33987
GL_TEXTURE4 = 33988
GL_TEXTURE5 = 33989
GL_TEXTURE6 = 33990
GL_TEXTURE7 = 33991
GL_TEXTURE8 = 33992
GL_TEXTURE9 = 33993
GL_TEXTURE10 = 33994
GL_TEXTURE11 = 33995
GL_TEXTURE12 = 33996
GL_TEXTURE13 = 33997
GL_TEXTURE14 = 33998
GL_TEXTURE15 = 33999
GL_TEXTURE16 = 34000
GL_TEXTURE17 = 34001
GL_TEXTURE18 = 34002
GL_TEXTURE19 = 34003
GL_TEXTURE20 = 34004
GL_TEXTURE21 = 34005
GL_TEXTURE22 = 34006
GL_TEXTURE23 = 34007
GL_TEXTURE24 = 34008
GL_TEXTURE25 = 34009
GL_TEXTURE26 = 34010
GL_TEXTURE27 = 34011
GL_TEXTURE28 = 34012
GL_TEXTURE29 = 34013
GL_TEXTURE30 = 34014
GL_TEXTURE31 = 34015
GL_ACTIVE_TEXTURE = 34016
GL_CLIENT_ACTIVE_TEXTURE = 34017
GL_MAX_TEXTURE_UNITS = 34018
GL_NORMAL_MAP = 34065
GL_REFLECTION_MAP = 34066
GL_TEXTURE_CUBE_MAP = 34067
GL_TEXTURE_BINDING_CUBE_MAP = 34068
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 34069
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 34070
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 34071
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 34073
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074
GL_PROXY_TEXTURE_CUBE_MAP = 34075
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 34076
GL_COMPRESSED_ALPHA = 34025
GL_COMPRESSED_LUMINANCE = 34026
GL_COMPRESSED_LUMINANCE_ALPHA = 34027
GL_COMPRESSED_INTENSITY = 34028
GL_COMPRESSED_RGB = 34029
GL_COMPRESSED_RGBA = 34030
GL_TEXTURE_COMPRESSION_HINT = 34031
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 34464
GL_TEXTURE_COMPRESSED = 34465
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 34466
GL_COMPRESSED_TEXTURE_FORMATS = 34467
GL_MULTISAMPLE = 32925
GL_SAMPLE_ALPHA_TO_COVERAGE = 32926
GL_SAMPLE_ALPHA_TO_ONE = 32927
GL_SAMPLE_COVERAGE = 32928
GL_SAMPLE_BUFFERS = 32936
GL_SAMPLES = 32937
GL_SAMPLE_COVERAGE_VALUE = 32938
GL_SAMPLE_COVERAGE_INVERT = 32939
GL_MULTISAMPLE_BIT = 536870912
GL_TRANSPOSE_MODELVIEW_MATRIX = 34019
GL_TRANSPOSE_PROJECTION_MATRIX = 34020
GL_TRANSPOSE_TEXTURE_MATRIX = 34021
GL_TRANSPOSE_COLOR_MATRIX = 34022
GL_COMBINE = 34160
GL_COMBINE_RGB = 34161
GL_COMBINE_ALPHA = 34162
GL_SOURCE0_RGB = 34176
GL_SOURCE1_RGB = 34177
GL_SOURCE2_RGB = 34178
GL_SOURCE0_ALPHA = 34184
GL_SOURCE1_ALPHA = 34185
GL_SOURCE2_ALPHA = 34186
GL_OPERAND0_RGB = 34192
GL_OPERAND1_RGB = 34193
GL_OPERAND2_RGB = 34194
GL_OPERAND0_ALPHA = 34200
GL_OPERAND1_ALPHA = 34201
GL_OPERAND2_ALPHA = 34202
GL_RGB_SCALE = 34163
GL_ADD_SIGNED = 34164
GL_INTERPOLATE = 34165
GL_SUBTRACT = 34023
GL_CONSTANT = 34166
GL_PRIMARY_COLOR = 34167
GL_PREVIOUS = 34168
GL_DOT3_RGB = 34478
GL_DOT3_RGBA = 34479
GL_CLAMP_TO_BORDER = 33069
glActiveTexture = _link_function('glActiveTexture', None, [GLenum], None)
glClientActiveTexture = _link_function('glClientActiveTexture', None, [GLenum], None)
glCompressedTexImage1D = _link_function('glCompressedTexImage1D', None, [GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, POINTER(GLvoid)], None)
glCompressedTexImage2D = _link_function('glCompressedTexImage2D', None, [GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid)], None)
glCompressedTexImage3D = _link_function('glCompressedTexImage3D', None, [GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid)], None)
glCompressedTexSubImage1D = _link_function('glCompressedTexSubImage1D', None, [GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, POINTER(GLvoid)], None)
glCompressedTexSubImage2D = _link_function('glCompressedTexSubImage2D', None, [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid)], None)
glCompressedTexSubImage3D = _link_function('glCompressedTexSubImage3D', None, [GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid)], None)
glGetCompressedTexImage = _link_function('glGetCompressedTexImage', None, [GLenum, GLint, POINTER(GLvoid)], None)
glMultiTexCoord1d = _link_function('glMultiTexCoord1d', None, [GLenum, GLdouble], None)
glMultiTexCoord1dv = _link_function('glMultiTexCoord1dv', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord1f = _link_function('glMultiTexCoord1f', None, [GLenum, GLfloat], None)
glMultiTexCoord1fv = _link_function('glMultiTexCoord1fv', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord1i = _link_function('glMultiTexCoord1i', None, [GLenum, GLint], None)
glMultiTexCoord1iv = _link_function('glMultiTexCoord1iv', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord1s = _link_function('glMultiTexCoord1s', None, [GLenum, GLshort], None)
glMultiTexCoord1sv = _link_function('glMultiTexCoord1sv', None, [GLenum, POINTER(GLshort)], None)
glMultiTexCoord2d = _link_function('glMultiTexCoord2d', None, [GLenum, GLdouble, GLdouble], None)
glMultiTexCoord2dv = _link_function('glMultiTexCoord2dv', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord2f = _link_function('glMultiTexCoord2f', None, [GLenum, GLfloat, GLfloat], None)
glMultiTexCoord2fv = _link_function('glMultiTexCoord2fv', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord2i = _link_function('glMultiTexCoord2i', None, [GLenum, GLint, GLint], None)
glMultiTexCoord2iv = _link_function('glMultiTexCoord2iv', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord2s = _link_function('glMultiTexCoord2s', None, [GLenum, GLshort, GLshort], None)
glMultiTexCoord2sv = _link_function('glMultiTexCoord2sv', None, [GLenum, POINTER(GLshort)], None)
glMultiTexCoord3d = _link_function('glMultiTexCoord3d', None, [GLenum, GLdouble, GLdouble, GLdouble], None)
glMultiTexCoord3dv = _link_function('glMultiTexCoord3dv', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord3f = _link_function('glMultiTexCoord3f', None, [GLenum, GLfloat, GLfloat, GLfloat], None)
glMultiTexCoord3fv = _link_function('glMultiTexCoord3fv', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord3i = _link_function('glMultiTexCoord3i', None, [GLenum, GLint, GLint, GLint], None)
glMultiTexCoord3iv = _link_function('glMultiTexCoord3iv', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord3s = _link_function('glMultiTexCoord3s', None, [GLenum, GLshort, GLshort, GLshort], None)
glMultiTexCoord3sv = _link_function('glMultiTexCoord3sv', None, [GLenum, POINTER(GLshort)], None)
glMultiTexCoord4d = _link_function('glMultiTexCoord4d', None, [GLenum, GLdouble, GLdouble, GLdouble, GLdouble], None)
glMultiTexCoord4dv = _link_function('glMultiTexCoord4dv', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord4f = _link_function('glMultiTexCoord4f', None, [GLenum, GLfloat, GLfloat, GLfloat, GLfloat], None)
glMultiTexCoord4fv = _link_function('glMultiTexCoord4fv', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord4i = _link_function('glMultiTexCoord4i', None, [GLenum, GLint, GLint, GLint, GLint], None)
glMultiTexCoord4iv = _link_function('glMultiTexCoord4iv', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord4s = _link_function('glMultiTexCoord4s', None, [GLenum, GLshort, GLshort, GLshort, GLshort], None)
glMultiTexCoord4sv = _link_function('glMultiTexCoord4sv', None, [GLenum, POINTER(GLshort)], None)
glLoadTransposeMatrixd = _link_function('glLoadTransposeMatrixd', None, [GLdouble * 16], None)
glLoadTransposeMatrixf = _link_function('glLoadTransposeMatrixf', None, [GLfloat * 16], None)
glMultTransposeMatrixd = _link_function('glMultTransposeMatrixd', None, [GLdouble * 16], None)
glMultTransposeMatrixf = _link_function('glMultTransposeMatrixf', None, [GLfloat * 16], None)
glSampleCoverage = _link_function('glSampleCoverage', None, [GLclampf, GLboolean], None)
PFNGLACTIVETEXTUREPROC = CFUNCTYPE(None, GLenum)
PFNGLSAMPLECOVERAGEPROC = CFUNCTYPE(None, GLclampf, GLboolean)
PFNGLCOMPRESSEDTEXIMAGE3DPROC = CFUNCTYPE(None, GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid))
PFNGLCOMPRESSEDTEXIMAGE2DPROC = CFUNCTYPE(None, GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid))
PFNGLCOMPRESSEDTEXIMAGE1DPROC = CFUNCTYPE(None, GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, POINTER(GLvoid))
PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid))
PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid))
PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, POINTER(GLvoid))
PFNGLGETCOMPRESSEDTEXIMAGEPROC = CFUNCTYPE(None, GLenum, GLint, POINTER(GLvoid))
GL_ARB_multitexture = 1
GL_TEXTURE0_ARB = 33984
GL_TEXTURE1_ARB = 33985
GL_TEXTURE2_ARB = 33986
GL_TEXTURE3_ARB = 33987
GL_TEXTURE4_ARB = 33988
GL_TEXTURE5_ARB = 33989
GL_TEXTURE6_ARB = 33990
GL_TEXTURE7_ARB = 33991
GL_TEXTURE8_ARB = 33992
GL_TEXTURE9_ARB = 33993
GL_TEXTURE10_ARB = 33994
GL_TEXTURE11_ARB = 33995
GL_TEXTURE12_ARB = 33996
GL_TEXTURE13_ARB = 33997
GL_TEXTURE14_ARB = 33998
GL_TEXTURE15_ARB = 33999
GL_TEXTURE16_ARB = 34000
GL_TEXTURE17_ARB = 34001
GL_TEXTURE18_ARB = 34002
GL_TEXTURE19_ARB = 34003
GL_TEXTURE20_ARB = 34004
GL_TEXTURE21_ARB = 34005
GL_TEXTURE22_ARB = 34006
GL_TEXTURE23_ARB = 34007
GL_TEXTURE24_ARB = 34008
GL_TEXTURE25_ARB = 34009
GL_TEXTURE26_ARB = 34010
GL_TEXTURE27_ARB = 34011
GL_TEXTURE28_ARB = 34012
GL_TEXTURE29_ARB = 34013
GL_TEXTURE30_ARB = 34014
GL_TEXTURE31_ARB = 34015
GL_ACTIVE_TEXTURE_ARB = 34016
GL_CLIENT_ACTIVE_TEXTURE_ARB = 34017
GL_MAX_TEXTURE_UNITS_ARB = 34018
glActiveTextureARB = _link_function('glActiveTextureARB', None, [GLenum], None)
glClientActiveTextureARB = _link_function('glClientActiveTextureARB', None, [GLenum], None)
glMultiTexCoord1dARB = _link_function('glMultiTexCoord1dARB', None, [GLenum, GLdouble], None)
glMultiTexCoord1dvARB = _link_function('glMultiTexCoord1dvARB', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord1fARB = _link_function('glMultiTexCoord1fARB', None, [GLenum, GLfloat], None)
glMultiTexCoord1fvARB = _link_function('glMultiTexCoord1fvARB', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord1iARB = _link_function('glMultiTexCoord1iARB', None, [GLenum, GLint], None)
glMultiTexCoord1ivARB = _link_function('glMultiTexCoord1ivARB', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord1sARB = _link_function('glMultiTexCoord1sARB', None, [GLenum, GLshort], None)
glMultiTexCoord1svARB = _link_function('glMultiTexCoord1svARB', None, [GLenum, POINTER(GLshort)], None)
glMultiTexCoord2dARB = _link_function('glMultiTexCoord2dARB', None, [GLenum, GLdouble, GLdouble], None)
glMultiTexCoord2dvARB = _link_function('glMultiTexCoord2dvARB', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord2fARB = _link_function('glMultiTexCoord2fARB', None, [GLenum, GLfloat, GLfloat], None)
glMultiTexCoord2fvARB = _link_function('glMultiTexCoord2fvARB', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord2iARB = _link_function('glMultiTexCoord2iARB', None, [GLenum, GLint, GLint], None)
glMultiTexCoord2ivARB = _link_function('glMultiTexCoord2ivARB', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord2sARB = _link_function('glMultiTexCoord2sARB', None, [GLenum, GLshort, GLshort], None)
glMultiTexCoord2svARB = _link_function('glMultiTexCoord2svARB', None, [GLenum, POINTER(GLshort)], None)
glMultiTexCoord3dARB = _link_function('glMultiTexCoord3dARB', None, [GLenum, GLdouble, GLdouble, GLdouble], None)
glMultiTexCoord3dvARB = _link_function('glMultiTexCoord3dvARB', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord3fARB = _link_function('glMultiTexCoord3fARB', None, [GLenum, GLfloat, GLfloat, GLfloat], None)
glMultiTexCoord3fvARB = _link_function('glMultiTexCoord3fvARB', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord3iARB = _link_function('glMultiTexCoord3iARB', None, [GLenum, GLint, GLint, GLint], None)
glMultiTexCoord3ivARB = _link_function('glMultiTexCoord3ivARB', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord3sARB = _link_function('glMultiTexCoord3sARB', None, [GLenum, GLshort, GLshort, GLshort], None)
glMultiTexCoord3svARB = _link_function('glMultiTexCoord3svARB', None, [GLenum, POINTER(GLshort)], None)
glMultiTexCoord4dARB = _link_function('glMultiTexCoord4dARB', None, [GLenum, GLdouble, GLdouble, GLdouble, GLdouble], None)
glMultiTexCoord4dvARB = _link_function('glMultiTexCoord4dvARB', None, [GLenum, POINTER(GLdouble)], None)
glMultiTexCoord4fARB = _link_function('glMultiTexCoord4fARB', None, [GLenum, GLfloat, GLfloat, GLfloat, GLfloat], None)
glMultiTexCoord4fvARB = _link_function('glMultiTexCoord4fvARB', None, [GLenum, POINTER(GLfloat)], None)
glMultiTexCoord4iARB = _link_function('glMultiTexCoord4iARB', None, [GLenum, GLint, GLint, GLint, GLint], None)
glMultiTexCoord4ivARB = _link_function('glMultiTexCoord4ivARB', None, [GLenum, POINTER(GLint)], None)
glMultiTexCoord4sARB = _link_function('glMultiTexCoord4sARB', None, [GLenum, GLshort, GLshort, GLshort, GLshort], None)
glMultiTexCoord4svARB = _link_function('glMultiTexCoord4svARB', None, [GLenum, POINTER(GLshort)], None)
PFNGLACTIVETEXTUREARBPROC = CFUNCTYPE(None, GLenum)
PFNGLCLIENTACTIVETEXTUREARBPROC = CFUNCTYPE(None, GLenum)
PFNGLMULTITEXCOORD1DARBPROC = CFUNCTYPE(None, GLenum, GLdouble)
PFNGLMULTITEXCOORD1DVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLdouble))
PFNGLMULTITEXCOORD1FARBPROC = CFUNCTYPE(None, GLenum, GLfloat)
PFNGLMULTITEXCOORD1FVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLfloat))
PFNGLMULTITEXCOORD1IARBPROC = CFUNCTYPE(None, GLenum, GLint)
PFNGLMULTITEXCOORD1IVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLint))
PFNGLMULTITEXCOORD1SARBPROC = CFUNCTYPE(None, GLenum, GLshort)
PFNGLMULTITEXCOORD1SVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLshort))
PFNGLMULTITEXCOORD2DARBPROC = CFUNCTYPE(None, GLenum, GLdouble, GLdouble)
PFNGLMULTITEXCOORD2DVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLdouble))
PFNGLMULTITEXCOORD2FARBPROC = CFUNCTYPE(None, GLenum, GLfloat, GLfloat)
PFNGLMULTITEXCOORD2FVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLfloat))
PFNGLMULTITEXCOORD2IARBPROC = CFUNCTYPE(None, GLenum, GLint, GLint)
PFNGLMULTITEXCOORD2IVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLint))
PFNGLMULTITEXCOORD2SARBPROC = CFUNCTYPE(None, GLenum, GLshort, GLshort)
PFNGLMULTITEXCOORD2SVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLshort))
PFNGLMULTITEXCOORD3DARBPROC = CFUNCTYPE(None, GLenum, GLdouble, GLdouble, GLdouble)
PFNGLMULTITEXCOORD3DVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLdouble))
PFNGLMULTITEXCOORD3FARBPROC = CFUNCTYPE(None, GLenum, GLfloat, GLfloat, GLfloat)
PFNGLMULTITEXCOORD3FVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLfloat))
PFNGLMULTITEXCOORD3IARBPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLint)
PFNGLMULTITEXCOORD3IVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLint))
PFNGLMULTITEXCOORD3SARBPROC = CFUNCTYPE(None, GLenum, GLshort, GLshort, GLshort)
PFNGLMULTITEXCOORD3SVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLshort))
PFNGLMULTITEXCOORD4DARBPROC = CFUNCTYPE(None, GLenum, GLdouble, GLdouble, GLdouble, GLdouble)
PFNGLMULTITEXCOORD4DVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLdouble))
PFNGLMULTITEXCOORD4FARBPROC = CFUNCTYPE(None, GLenum, GLfloat, GLfloat, GLfloat, GLfloat)
PFNGLMULTITEXCOORD4FVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLfloat))
PFNGLMULTITEXCOORD4IARBPROC = CFUNCTYPE(None, GLenum, GLint, GLint, GLint, GLint)
PFNGLMULTITEXCOORD4IVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLint))
PFNGLMULTITEXCOORD4SARBPROC = CFUNCTYPE(None, GLenum, GLshort, GLshort, GLshort, GLshort)
PFNGLMULTITEXCOORD4SVARBPROC = CFUNCTYPE(None, GLenum, POINTER(GLshort))
GL_MESA_shader_debug = 1
GL_DEBUG_OBJECT_MESA = 34649
GL_DEBUG_PRINT_MESA = 34650
GL_DEBUG_ASSERT_MESA = 34651
GLhandleARB = c_uint
glCreateDebugObjectMESA = _link_function('glCreateDebugObjectMESA', GLhandleARB, [], None)
glClearDebugLogMESA = _link_function('glClearDebugLogMESA', None, [GLhandleARB, GLenum, GLenum], None)
GLcharARB = c_char
glGetDebugLogMESA = _link_function('glGetDebugLogMESA', None, [GLhandleARB, GLenum, GLenum, GLsizei, POINTER(GLsizei), POINTER(GLcharARB)], None)
glGetDebugLogLengthMESA = _link_function('glGetDebugLogLengthMESA', GLsizei, [GLhandleARB, GLenum, GLenum], None)
GL_MESA_packed_depth_stencil = 1
GL_DEPTH_STENCIL_MESA = 34640
GL_UNSIGNED_INT_24_8_MESA = 34641
GL_UNSIGNED_INT_8_24_REV_MESA = 34642
GL_UNSIGNED_SHORT_15_1_MESA = 34643
GL_UNSIGNED_SHORT_1_15_REV_MESA = 34644
GL_MESA_program_debug = 1
GL_FRAGMENT_PROGRAM_POSITION_MESA = 35760
GL_FRAGMENT_PROGRAM_CALLBACK_MESA = 35761
GL_FRAGMENT_PROGRAM_CALLBACK_FUNC_MESA = 35762
GL_FRAGMENT_PROGRAM_CALLBACK_DATA_MESA = 35763
GL_VERTEX_PROGRAM_POSITION_MESA = 35764
GL_VERTEX_PROGRAM_CALLBACK_MESA = 35765
GL_VERTEX_PROGRAM_CALLBACK_FUNC_MESA = 35766
GL_VERTEX_PROGRAM_CALLBACK_DATA_MESA = 35767
GLprogramcallbackMESA = CFUNCTYPE(None, GLenum, POINTER(GLvoid))
glProgramCallbackMESA = _link_function('glProgramCallbackMESA', None, [GLenum, GLprogramcallbackMESA, POINTER(GLvoid)], None)
glGetProgramRegisterfvMESA = _link_function('glGetProgramRegisterfvMESA', None, [GLenum, GLsizei, POINTER(GLubyte), POINTER(GLfloat)], None)
GL_MESA_texture_array = 1
GL_ATI_blend_equation_separate = 1
GL_ALPHA_BLEND_EQUATION_ATI = 34877
glBlendEquationSeparateATI = _link_function('glBlendEquationSeparateATI', None, [GLenum, GLenum], None)
PFNGLBLENDEQUATIONSEPARATEATIPROC = CFUNCTYPE(None, GLenum, GLenum)
__all__ = [
 'GL_VERSION_1_1', 'GL_VERSION_1_2', 'GL_VERSION_1_3', 
 'GL_ARB_imaging', 
 'GLenum', 'GLboolean', 'GLbitfield', 'GLvoid', 'GLbyte', 
 'GLshort', 'GLint', 
 'GLubyte', 'GLushort', 'GLuint', 'GLsizei', 'GLfloat', 
 'GLclampf', 'GLdouble', 
 'GLclampd', 'GL_FALSE', 'GL_TRUE', 'GL_BYTE', 
 'GL_UNSIGNED_BYTE', 'GL_SHORT', 
 'GL_UNSIGNED_SHORT', 'GL_INT', 
 'GL_UNSIGNED_INT', 'GL_FLOAT', 'GL_2_BYTES', 
 'GL_3_BYTES', 'GL_4_BYTES', 
 'GL_DOUBLE', 'GL_POINTS', 'GL_LINES', 'GL_LINE_LOOP', 
 'GL_LINE_STRIP', 
 'GL_TRIANGLES', 'GL_TRIANGLE_STRIP', 'GL_TRIANGLE_FAN', 
 'GL_QUADS', 
 'GL_QUAD_STRIP', 'GL_POLYGON', 'GL_VERTEX_ARRAY', 'GL_NORMAL_ARRAY', 
 'GL_COLOR_ARRAY', 
 'GL_INDEX_ARRAY', 'GL_TEXTURE_COORD_ARRAY', 
 'GL_EDGE_FLAG_ARRAY', 'GL_VERTEX_ARRAY_SIZE', 
 'GL_VERTEX_ARRAY_TYPE', 
 'GL_VERTEX_ARRAY_STRIDE', 'GL_NORMAL_ARRAY_TYPE', 
 'GL_NORMAL_ARRAY_STRIDE', 
 'GL_COLOR_ARRAY_SIZE', 'GL_COLOR_ARRAY_TYPE', 
 'GL_COLOR_ARRAY_STRIDE', 
 'GL_INDEX_ARRAY_TYPE', 'GL_INDEX_ARRAY_STRIDE', 
 'GL_TEXTURE_COORD_ARRAY_SIZE', 
 'GL_TEXTURE_COORD_ARRAY_TYPE', 'GL_TEXTURE_COORD_ARRAY_STRIDE', 
 'GL_EDGE_FLAG_ARRAY_STRIDE', 
 'GL_VERTEX_ARRAY_POINTER', 
 'GL_NORMAL_ARRAY_POINTER', 'GL_COLOR_ARRAY_POINTER', 
 'GL_INDEX_ARRAY_POINTER', 
 'GL_TEXTURE_COORD_ARRAY_POINTER', 'GL_EDGE_FLAG_ARRAY_POINTER', 
 'GL_V2F', 
 'GL_V3F', 'GL_C4UB_V2F', 'GL_C4UB_V3F', 'GL_C3F_V3F', 'GL_N3F_V3F', 
 'GL_C4F_N3F_V3F', 
 'GL_T2F_V3F', 'GL_T4F_V4F', 'GL_T2F_C4UB_V3F', 
 'GL_T2F_C3F_V3F', 'GL_T2F_N3F_V3F', 
 'GL_T2F_C4F_N3F_V3F', 
 'GL_T4F_C4F_N3F_V4F', 'GL_MATRIX_MODE', 'GL_MODELVIEW', 
 'GL_PROJECTION', 
 'GL_TEXTURE', 'GL_POINT_SMOOTH', 'GL_POINT_SIZE', 'GL_POINT_SIZE_GRANULARITY', 
 'GL_POINT_SIZE_RANGE', 
 'GL_LINE_SMOOTH', 'GL_LINE_STIPPLE', 
 'GL_LINE_STIPPLE_PATTERN', 'GL_LINE_STIPPLE_REPEAT', 
 'GL_LINE_WIDTH', 
 'GL_LINE_WIDTH_GRANULARITY', 'GL_LINE_WIDTH_RANGE', 'GL_POINT', 
 'GL_LINE', 
 'GL_FILL', 'GL_CW', 'GL_CCW', 'GL_FRONT', 'GL_BACK', 'GL_POLYGON_MODE', 
 'GL_POLYGON_SMOOTH', 
 'GL_POLYGON_STIPPLE', 'GL_EDGE_FLAG', 'GL_CULL_FACE', 
 'GL_CULL_FACE_MODE', 
 'GL_FRONT_FACE', 'GL_POLYGON_OFFSET_FACTOR', 
 'GL_POLYGON_OFFSET_UNITS', 
 'GL_POLYGON_OFFSET_POINT', 
 'GL_POLYGON_OFFSET_LINE', 'GL_POLYGON_OFFSET_FILL', 
 'GL_COMPILE', 
 'GL_COMPILE_AND_EXECUTE', 'GL_LIST_BASE', 'GL_LIST_INDEX', 
 'GL_LIST_MODE', 
 'GL_NEVER', 'GL_LESS', 'GL_EQUAL', 'GL_LEQUAL', 'GL_GREATER', 
 'GL_NOTEQUAL', 
 'GL_GEQUAL', 'GL_ALWAYS', 'GL_DEPTH_TEST', 'GL_DEPTH_BITS', 
 'GL_DEPTH_CLEAR_VALUE', 
 'GL_DEPTH_FUNC', 'GL_DEPTH_RANGE', 
 'GL_DEPTH_WRITEMASK', 'GL_DEPTH_COMPONENT', 
 'GL_LIGHTING', 'GL_LIGHT0', 
 'GL_LIGHT1', 'GL_LIGHT2', 'GL_LIGHT3', 'GL_LIGHT4', 
 'GL_LIGHT5', 'GL_LIGHT6', 
 'GL_LIGHT7', 'GL_SPOT_EXPONENT', 'GL_SPOT_CUTOFF', 
 'GL_CONSTANT_ATTENUATION', 
 'GL_LINEAR_ATTENUATION', 'GL_QUADRATIC_ATTENUATION', 
 'GL_AMBIENT', 
 'GL_DIFFUSE', 'GL_SPECULAR', 'GL_SHININESS', 'GL_EMISSION', 
 'GL_POSITION', 
 'GL_SPOT_DIRECTION', 'GL_AMBIENT_AND_DIFFUSE', 'GL_COLOR_INDEXES', 
 'GL_LIGHT_MODEL_TWO_SIDE', 
 'GL_LIGHT_MODEL_LOCAL_VIEWER', 
 'GL_LIGHT_MODEL_AMBIENT', 'GL_FRONT_AND_BACK', 
 'GL_SHADE_MODEL', 'GL_FLAT', 
 'GL_SMOOTH', 'GL_COLOR_MATERIAL', 'GL_COLOR_MATERIAL_FACE', 
 'GL_COLOR_MATERIAL_PARAMETER', 
 'GL_NORMALIZE', 'GL_CLIP_PLANE0', 
 'GL_CLIP_PLANE1', 'GL_CLIP_PLANE2', 'GL_CLIP_PLANE3', 
 'GL_CLIP_PLANE4', 
 'GL_CLIP_PLANE5', 'GL_ACCUM_RED_BITS', 'GL_ACCUM_GREEN_BITS', 
 'GL_ACCUM_BLUE_BITS', 
 'GL_ACCUM_ALPHA_BITS', 'GL_ACCUM_CLEAR_VALUE', 
 'GL_ACCUM', 'GL_ADD', 'GL_LOAD', 
 'GL_MULT', 'GL_RETURN', 'GL_ALPHA_TEST', 
 'GL_ALPHA_TEST_REF', 'GL_ALPHA_TEST_FUNC', 
 'GL_BLEND', 'GL_BLEND_SRC', 
 'GL_BLEND_DST', 'GL_ZERO', 'GL_ONE', 'GL_SRC_COLOR', 
 'GL_ONE_MINUS_SRC_COLOR', 
 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA', 'GL_DST_ALPHA', 
 'GL_ONE_MINUS_DST_ALPHA', 
 'GL_DST_COLOR', 'GL_ONE_MINUS_DST_COLOR', 
 'GL_SRC_ALPHA_SATURATE', 'GL_FEEDBACK', 
 'GL_RENDER', 'GL_SELECT', 'GL_2D', 
 'GL_3D', 'GL_3D_COLOR', 'GL_3D_COLOR_TEXTURE', 
 'GL_4D_COLOR_TEXTURE', 
 'GL_POINT_TOKEN', 'GL_LINE_TOKEN', 'GL_LINE_RESET_TOKEN', 
 'GL_POLYGON_TOKEN', 
 'GL_BITMAP_TOKEN', 'GL_DRAW_PIXEL_TOKEN', 'GL_COPY_PIXEL_TOKEN', 
 'GL_PASS_THROUGH_TOKEN', 
 'GL_FEEDBACK_BUFFER_POINTER', 
 'GL_FEEDBACK_BUFFER_SIZE', 'GL_FEEDBACK_BUFFER_TYPE', 
 'GL_SELECTION_BUFFER_POINTER', 
 'GL_SELECTION_BUFFER_SIZE', 'GL_FOG', 
 'GL_FOG_MODE', 'GL_FOG_DENSITY', 
 'GL_FOG_COLOR', 'GL_FOG_INDEX', 
 'GL_FOG_START', 'GL_FOG_END', 'GL_LINEAR', 
 'GL_EXP', 'GL_EXP2', 'GL_LOGIC_OP', 
 'GL_INDEX_LOGIC_OP', 'GL_COLOR_LOGIC_OP', 
 'GL_LOGIC_OP_MODE', 'GL_CLEAR', 
 'GL_SET', 'GL_COPY', 'GL_COPY_INVERTED', 
 'GL_NOOP', 'GL_INVERT', 'GL_AND', 
 'GL_NAND', 'GL_OR', 'GL_NOR', 'GL_XOR', 
 'GL_EQUIV', 'GL_AND_REVERSE', 
 'GL_AND_INVERTED', 'GL_OR_REVERSE', 'GL_OR_INVERTED', 
 'GL_STENCIL_BITS', 
 'GL_STENCIL_TEST', 'GL_STENCIL_CLEAR_VALUE', 'GL_STENCIL_FUNC', 
 'GL_STENCIL_VALUE_MASK', 
 'GL_STENCIL_FAIL', 'GL_STENCIL_PASS_DEPTH_FAIL', 
 'GL_STENCIL_PASS_DEPTH_PASS', 
 'GL_STENCIL_REF', 'GL_STENCIL_WRITEMASK', 
 'GL_STENCIL_INDEX', 'GL_KEEP', 
 'GL_REPLACE', 'GL_INCR', 'GL_DECR', 'GL_NONE', 
 'GL_LEFT', 'GL_RIGHT', 
 'GL_FRONT_LEFT', 'GL_FRONT_RIGHT', 'GL_BACK_LEFT', 
 'GL_BACK_RIGHT', 'GL_AUX0', 
 'GL_AUX1', 'GL_AUX2', 'GL_AUX3', 'GL_COLOR_INDEX', 
 'GL_RED', 'GL_GREEN', 
 'GL_BLUE', 'GL_ALPHA', 'GL_LUMINANCE', 
 'GL_LUMINANCE_ALPHA', 'GL_ALPHA_BITS', 
 'GL_RED_BITS', 'GL_GREEN_BITS', 
 'GL_BLUE_BITS', 'GL_INDEX_BITS', 'GL_SUBPIXEL_BITS', 
 'GL_AUX_BUFFERS', 
 'GL_READ_BUFFER', 'GL_DRAW_BUFFER', 'GL_DOUBLEBUFFER', 
 'GL_STEREO', 
 'GL_BITMAP', 'GL_COLOR', 'GL_DEPTH', 'GL_STENCIL', 'GL_DITHER', 
 'GL_RGB', 
 'GL_RGBA', 'GL_MAX_LIST_NESTING', 'GL_MAX_EVAL_ORDER', 'GL_MAX_LIGHTS', 
 'GL_MAX_CLIP_PLANES', 
 'GL_MAX_TEXTURE_SIZE', 'GL_MAX_PIXEL_MAP_TABLE', 
 'GL_MAX_ATTRIB_STACK_DEPTH', 
 'GL_MAX_MODELVIEW_STACK_DEPTH', 
 'GL_MAX_NAME_STACK_DEPTH', 'GL_MAX_PROJECTION_STACK_DEPTH', 
 'GL_MAX_TEXTURE_STACK_DEPTH', 
 'GL_MAX_VIEWPORT_DIMS', 
 'GL_MAX_CLIENT_ATTRIB_STACK_DEPTH', 'GL_ATTRIB_STACK_DEPTH', 
 'GL_CLIENT_ATTRIB_STACK_DEPTH', 
 'GL_COLOR_CLEAR_VALUE', 'GL_COLOR_WRITEMASK', 
 'GL_CURRENT_INDEX', 'GL_CURRENT_COLOR', 
 'GL_CURRENT_NORMAL', 
 'GL_CURRENT_RASTER_COLOR', 'GL_CURRENT_RASTER_DISTANCE', 
 'GL_CURRENT_RASTER_INDEX', 
 'GL_CURRENT_RASTER_POSITION', 
 'GL_CURRENT_RASTER_TEXTURE_COORDS', 'GL_CURRENT_RASTER_POSITION_VALID', 
 'GL_CURRENT_TEXTURE_COORDS', 
 'GL_INDEX_CLEAR_VALUE', 'GL_INDEX_MODE', 
 'GL_INDEX_WRITEMASK', 'GL_MODELVIEW_MATRIX', 
 'GL_MODELVIEW_STACK_DEPTH', 
 'GL_NAME_STACK_DEPTH', 'GL_PROJECTION_MATRIX', 
 'GL_PROJECTION_STACK_DEPTH', 
 'GL_RENDER_MODE', 'GL_RGBA_MODE', 'GL_TEXTURE_MATRIX', 
 'GL_TEXTURE_STACK_DEPTH', 
 'GL_VIEWPORT', 'GL_AUTO_NORMAL', 'GL_MAP1_COLOR_4', 
 'GL_MAP1_INDEX', 'GL_MAP1_NORMAL', 
 'GL_MAP1_TEXTURE_COORD_1', 
 'GL_MAP1_TEXTURE_COORD_2', 'GL_MAP1_TEXTURE_COORD_3', 
 'GL_MAP1_TEXTURE_COORD_4', 
 'GL_MAP1_VERTEX_3', 'GL_MAP1_VERTEX_4', 
 'GL_MAP2_COLOR_4', 'GL_MAP2_INDEX', 
 'GL_MAP2_NORMAL', 
 'GL_MAP2_TEXTURE_COORD_1', 'GL_MAP2_TEXTURE_COORD_2', 
 'GL_MAP2_TEXTURE_COORD_3', 
 'GL_MAP2_TEXTURE_COORD_4', 'GL_MAP2_VERTEX_3', 
 'GL_MAP2_VERTEX_4', 'GL_MAP1_GRID_DOMAIN', 
 'GL_MAP1_GRID_SEGMENTS', 
 'GL_MAP2_GRID_DOMAIN', 'GL_MAP2_GRID_SEGMENTS', 
 'GL_COEFF', 'GL_ORDER', 
 'GL_DOMAIN', 'GL_PERSPECTIVE_CORRECTION_HINT', 
 'GL_POINT_SMOOTH_HINT', 
 'GL_LINE_SMOOTH_HINT', 'GL_POLYGON_SMOOTH_HINT', 
 'GL_FOG_HINT', 
 'GL_DONT_CARE', 'GL_FASTEST', 'GL_NICEST', 'GL_SCISSOR_BOX', 
 'GL_SCISSOR_TEST', 
 'GL_MAP_COLOR', 'GL_MAP_STENCIL', 'GL_INDEX_SHIFT', 
 'GL_INDEX_OFFSET', 
 'GL_RED_SCALE', 'GL_RED_BIAS', 'GL_GREEN_SCALE', 
 'GL_GREEN_BIAS', 'GL_BLUE_SCALE', 
 'GL_BLUE_BIAS', 'GL_ALPHA_SCALE', 
 'GL_ALPHA_BIAS', 'GL_DEPTH_SCALE', 'GL_DEPTH_BIAS', 
 'GL_PIXEL_MAP_S_TO_S_SIZE', 
 'GL_PIXEL_MAP_I_TO_I_SIZE', 
 'GL_PIXEL_MAP_I_TO_R_SIZE', 'GL_PIXEL_MAP_I_TO_G_SIZE', 
 'GL_PIXEL_MAP_I_TO_B_SIZE', 
 'GL_PIXEL_MAP_I_TO_A_SIZE', 
 'GL_PIXEL_MAP_R_TO_R_SIZE', 'GL_PIXEL_MAP_G_TO_G_SIZE', 
 'GL_PIXEL_MAP_B_TO_B_SIZE', 
 'GL_PIXEL_MAP_A_TO_A_SIZE', 'GL_PIXEL_MAP_S_TO_S', 
 'GL_PIXEL_MAP_I_TO_I', 
 'GL_PIXEL_MAP_I_TO_R', 'GL_PIXEL_MAP_I_TO_G', 
 'GL_PIXEL_MAP_I_TO_B', 'GL_PIXEL_MAP_I_TO_A', 
 'GL_PIXEL_MAP_R_TO_R', 
 'GL_PIXEL_MAP_G_TO_G', 'GL_PIXEL_MAP_B_TO_B', 'GL_PIXEL_MAP_A_TO_A', 
 'GL_PACK_ALIGNMENT', 
 'GL_PACK_LSB_FIRST', 'GL_PACK_ROW_LENGTH', 
 'GL_PACK_SKIP_PIXELS', 'GL_PACK_SKIP_ROWS', 
 'GL_PACK_SWAP_BYTES', 
 'GL_UNPACK_ALIGNMENT', 'GL_UNPACK_LSB_FIRST', 'GL_UNPACK_ROW_LENGTH', 
 'GL_UNPACK_SKIP_PIXELS', 
 'GL_UNPACK_SKIP_ROWS', 'GL_UNPACK_SWAP_BYTES', 
 'GL_ZOOM_X', 'GL_ZOOM_Y', 
 'GL_TEXTURE_ENV', 'GL_TEXTURE_ENV_MODE', 
 'GL_TEXTURE_1D', 'GL_TEXTURE_2D', 
 'GL_TEXTURE_WRAP_S', 'GL_TEXTURE_WRAP_T', 
 'GL_TEXTURE_MAG_FILTER', 'GL_TEXTURE_MIN_FILTER', 
 'GL_TEXTURE_ENV_COLOR', 
 'GL_TEXTURE_GEN_S', 'GL_TEXTURE_GEN_T', 'GL_TEXTURE_GEN_MODE', 
 'GL_TEXTURE_BORDER_COLOR', 
 'GL_TEXTURE_WIDTH', 'GL_TEXTURE_HEIGHT', 
 'GL_TEXTURE_BORDER', 'GL_TEXTURE_COMPONENTS', 
 'GL_TEXTURE_RED_SIZE', 
 'GL_TEXTURE_GREEN_SIZE', 'GL_TEXTURE_BLUE_SIZE', 
 'GL_TEXTURE_ALPHA_SIZE', 
 'GL_TEXTURE_LUMINANCE_SIZE', 'GL_TEXTURE_INTENSITY_SIZE', 
 'GL_NEAREST_MIPMAP_NEAREST', 
 'GL_NEAREST_MIPMAP_LINEAR', 
 'GL_LINEAR_MIPMAP_NEAREST', 'GL_LINEAR_MIPMAP_LINEAR', 
 'GL_OBJECT_LINEAR', 
 'GL_OBJECT_PLANE', 'GL_EYE_LINEAR', 'GL_EYE_PLANE', 
 'GL_SPHERE_MAP', 
 'GL_DECAL', 'GL_MODULATE', 'GL_NEAREST', 'GL_REPEAT', 
 'GL_CLAMP', 'GL_S', 
 'GL_T', 'GL_R', 'GL_Q', 'GL_TEXTURE_GEN_R', 'GL_TEXTURE_GEN_Q', 
 'GL_VENDOR', 
 'GL_RENDERER', 'GL_VERSION', 'GL_EXTENSIONS', 'GL_NO_ERROR', 
 'GL_INVALID_ENUM', 
 'GL_INVALID_VALUE', 'GL_INVALID_OPERATION', 
 'GL_STACK_OVERFLOW', 'GL_STACK_UNDERFLOW', 
 'GL_OUT_OF_MEMORY', 
 'GL_CURRENT_BIT', 'GL_POINT_BIT', 'GL_LINE_BIT', 'GL_POLYGON_BIT', 
 'GL_POLYGON_STIPPLE_BIT', 
 'GL_PIXEL_MODE_BIT', 'GL_LIGHTING_BIT', 
 'GL_FOG_BIT', 'GL_DEPTH_BUFFER_BIT', 
 'GL_ACCUM_BUFFER_BIT', 
 'GL_STENCIL_BUFFER_BIT', 'GL_VIEWPORT_BIT', 'GL_TRANSFORM_BIT', 
 'GL_ENABLE_BIT', 
 'GL_COLOR_BUFFER_BIT', 'GL_HINT_BIT', 'GL_EVAL_BIT', 
 'GL_LIST_BIT', 'GL_TEXTURE_BIT', 
 'GL_SCISSOR_BIT', 'GL_ALL_ATTRIB_BITS', 
 'GL_PROXY_TEXTURE_1D', 'GL_PROXY_TEXTURE_2D', 
 'GL_TEXTURE_PRIORITY', 
 'GL_TEXTURE_RESIDENT', 'GL_TEXTURE_BINDING_1D', 'GL_TEXTURE_BINDING_2D', 
 'GL_TEXTURE_INTERNAL_FORMAT', 
 'GL_ALPHA4', 'GL_ALPHA8', 'GL_ALPHA12', 
 'GL_ALPHA16', 'GL_LUMINANCE4', 
 'GL_LUMINANCE8', 'GL_LUMINANCE12', 
 'GL_LUMINANCE16', 'GL_LUMINANCE4_ALPHA4', 
 'GL_LUMINANCE6_ALPHA2', 
 'GL_LUMINANCE8_ALPHA8', 'GL_LUMINANCE12_ALPHA4', 
 'GL_LUMINANCE12_ALPHA12', 
 'GL_LUMINANCE16_ALPHA16', 'GL_INTENSITY', 'GL_INTENSITY4', 
 'GL_INTENSITY8', 
 'GL_INTENSITY12', 'GL_INTENSITY16', 'GL_R3_G3_B2', 'GL_RGB4', 
 'GL_RGB5', 
 'GL_RGB8', 'GL_RGB10', 'GL_RGB12', 'GL_RGB16', 'GL_RGBA2', 
 'GL_RGBA4', 
 'GL_RGB5_A1', 'GL_RGBA8', 'GL_RGB10_A2', 'GL_RGBA12', 'GL_RGBA16', 
 'GL_CLIENT_PIXEL_STORE_BIT', 
 'GL_CLIENT_VERTEX_ARRAY_BIT', 
 'GL_ALL_CLIENT_ATTRIB_BITS', 'GL_CLIENT_ALL_ATTRIB_BITS', 
 'glClearIndex', 
 'glClearColor', 'glClear', 'glIndexMask', 'glColorMask', 
 'glAlphaFunc', 
 'glBlendFunc', 'glLogicOp', 'glCullFace', 'glFrontFace', 
 'glPointSize', 
 'glLineWidth', 'glLineStipple', 'glPolygonMode', 'glPolygonOffset', 
 'glPolygonStipple', 
 'glGetPolygonStipple', 'glEdgeFlag', 'glEdgeFlagv', 
 'glScissor', 'glClipPlane', 
 'glGetClipPlane', 'glDrawBuffer', 'glReadBuffer', 
 'glEnable', 'glDisable', 
 'glIsEnabled', 'glEnableClientState', 
 'glDisableClientState', 'glGetBooleanv', 
 'glGetDoublev', 'glGetFloatv', 
 'glGetIntegerv', 'glPushAttrib', 'glPopAttrib', 
 'glPushClientAttrib', 
 'glPopClientAttrib', 'glRenderMode', 'glGetError', 
 'glGetString', 'glFinish', 
 'glFlush', 'glHint', 'glClearDepth', 'glDepthFunc', 
 'glDepthMask', 
 'glDepthRange', 'glClearAccum', 'glAccum', 'glMatrixMode', 
 'glOrtho', 
 'glFrustum', 'glViewport', 'glPushMatrix', 'glPopMatrix', 'glLoadIdentity', 
 'glLoadMatrixd', 
 'glLoadMatrixf', 'glMultMatrixd', 'glMultMatrixf', 
 'glRotated', 'glRotatef', 
 'glScaled', 'glScalef', 'glTranslated', 
 'glTranslatef', 'glIsList', 'glDeleteLists', 
 'glGenLists', 'glNewList', 
 'glEndList', 'glCallList', 'glCallLists', 'glListBase', 
 'glBegin', 'glEnd', 
 'glVertex2d', 'glVertex2f', 'glVertex2i', 'glVertex2s', 
 'glVertex3d', 
 'glVertex3f', 'glVertex3i', 'glVertex3s', 'glVertex4d', 
 'glVertex4f', 
 'glVertex4i', 'glVertex4s', 'glVertex2dv', 'glVertex2fv', 
 'glVertex2iv', 
 'glVertex2sv', 'glVertex3dv', 'glVertex3fv', 'glVertex3iv', 
 'glVertex3sv', 
 'glVertex4dv', 'glVertex4fv', 'glVertex4iv', 'glVertex4sv', 
 'glNormal3b', 
 'glNormal3d', 'glNormal3f', 'glNormal3i', 'glNormal3s', 
 'glNormal3bv', 
 'glNormal3dv', 'glNormal3fv', 'glNormal3iv', 'glNormal3sv', 
 'glIndexd', 
 'glIndexf', 'glIndexi', 'glIndexs', 'glIndexub', 'glIndexdv', 
 'glIndexfv', 
 'glIndexiv', 'glIndexsv', 'glIndexubv', 'glColor3b', 'glColor3d', 
 'glColor3f', 
 'glColor3i', 'glColor3s', 'glColor3ub', 'glColor3ui', 'glColor3us', 
 'glColor4b', 
 'glColor4d', 'glColor4f', 'glColor4i', 'glColor4s', 'glColor4ub', 
 'glColor4ui', 
 'glColor4us', 'glColor3bv', 'glColor3dv', 'glColor3fv', 
 'glColor3iv', 
 'glColor3sv', 'glColor3ubv', 'glColor3uiv', 'glColor3usv', 
 'glColor4bv', 
 'glColor4dv', 'glColor4fv', 'glColor4iv', 'glColor4sv', 
 'glColor4ubv', 
 'glColor4uiv', 'glColor4usv', 'glTexCoord1d', 'glTexCoord1f', 
 'glTexCoord1i', 
 'glTexCoord1s', 'glTexCoord2d', 'glTexCoord2f', 
 'glTexCoord2i', 'glTexCoord2s', 
 'glTexCoord3d', 'glTexCoord3f', 
 'glTexCoord3i', 'glTexCoord3s', 'glTexCoord4d', 
 'glTexCoord4f', 
 'glTexCoord4i', 'glTexCoord4s', 'glTexCoord1dv', 'glTexCoord1fv', 
 'glTexCoord1iv', 
 'glTexCoord1sv', 'glTexCoord2dv', 'glTexCoord2fv', 
 'glTexCoord2iv', 'glTexCoord2sv', 
 'glTexCoord3dv', 'glTexCoord3fv', 
 'glTexCoord3iv', 'glTexCoord3sv', 'glTexCoord4dv', 
 'glTexCoord4fv', 
 'glTexCoord4iv', 'glTexCoord4sv', 'glRasterPos2d', 'glRasterPos2f', 
 'glRasterPos2i', 
 'glRasterPos2s', 'glRasterPos3d', 'glRasterPos3f', 
 'glRasterPos3i', 'glRasterPos3s', 
 'glRasterPos4d', 'glRasterPos4f', 
 'glRasterPos4i', 'glRasterPos4s', 'glRasterPos2dv', 
 'glRasterPos2fv', 
 'glRasterPos2iv', 'glRasterPos2sv', 'glRasterPos3dv', 
 'glRasterPos3fv', 
 'glRasterPos3iv', 'glRasterPos3sv', 'glRasterPos4dv', 
 'glRasterPos4fv', 
 'glRasterPos4iv', 'glRasterPos4sv', 'glRectd', 'glRectf', 
 'glRecti', 
 'glRects', 'glRectdv', 'glRectfv', 'glRectiv', 'glRectsv', 
 'glVertexPointer', 
 'glNormalPointer', 'glColorPointer', 'glIndexPointer', 
 'glTexCoordPointer', 
 'glEdgeFlagPointer', 'glGetPointerv', 'glArrayElement', 
 'glDrawArrays', 
 'glDrawElements', 'glInterleavedArrays', 'glShadeModel', 
 'glLightf', 
 'glLighti', 'glLightfv', 'glLightiv', 'glGetLightfv', 'glGetLightiv', 
 'glLightModelf', 
 'glLightModeli', 'glLightModelfv', 'glLightModeliv', 
 'glMaterialf', 'glMateriali', 
 'glMaterialfv', 'glMaterialiv', 
 'glGetMaterialfv', 'glGetMaterialiv', 'glColorMaterial', 
 'glPixelZoom', 
 'glPixelStoref', 'glPixelStorei', 'glPixelTransferf', 'glPixelTransferi', 
 'glPixelMapfv', 
 'glPixelMapuiv', 'glPixelMapusv', 'glGetPixelMapfv', 
 'glGetPixelMapuiv', 
 'glGetPixelMapusv', 'glBitmap', 'glReadPixels', 
 'glDrawPixels', 'glCopyPixels', 
 'glStencilFunc', 'glStencilMask', 
 'glStencilOp', 'glClearStencil', 'glTexGend', 
 'glTexGenf', 'glTexGeni', 
 'glTexGendv', 'glTexGenfv', 'glTexGeniv', 'glGetTexGendv', 
 'glGetTexGenfv', 
 'glGetTexGeniv', 'glTexEnvf', 'glTexEnvi', 'glTexEnvfv', 
 'glTexEnviv', 
 'glGetTexEnvfv', 'glGetTexEnviv', 'glTexParameterf', 'glTexParameteri', 
 'glTexParameterfv', 
 'glTexParameteriv', 'glGetTexParameterfv', 
 'glGetTexParameteriv', 'glGetTexLevelParameterfv', 
 'glGetTexLevelParameteriv', 
 'glTexImage1D', 'glTexImage2D', 'glGetTexImage', 
 'glGenTextures', 
 'glDeleteTextures', 'glBindTexture', 'glPrioritizeTextures', 
 'glAreTexturesResident', 
 'glIsTexture', 'glTexSubImage1D', 'glTexSubImage2D', 
 'glCopyTexImage1D', 
 'glCopyTexImage2D', 'glCopyTexSubImage1D', 
 'glCopyTexSubImage2D', 'glMap1d', 
 'glMap1f', 'glMap2d', 'glMap2f', 
 'glGetMapdv', 'glGetMapfv', 'glGetMapiv', 
 'glEvalCoord1d', 'glEvalCoord1f', 
 'glEvalCoord1dv', 'glEvalCoord1fv', 'glEvalCoord2d', 
 'glEvalCoord2f', 
 'glEvalCoord2dv', 'glEvalCoord2fv', 'glMapGrid1d', 'glMapGrid1f', 
 'glMapGrid2d', 
 'glMapGrid2f', 'glEvalPoint1', 'glEvalPoint2', 'glEvalMesh1', 
 'glEvalMesh2', 
 'glFogf', 'glFogi', 'glFogfv', 'glFogiv', 'glFeedbackBuffer', 
 'glPassThrough', 
 'glSelectBuffer', 'glInitNames', 'glLoadName', 'glPushName', 
 'glPopName', 
 'GL_RESCALE_NORMAL', 'GL_CLAMP_TO_EDGE', 
 'GL_MAX_ELEMENTS_VERTICES', 'GL_MAX_ELEMENTS_INDICES', 
 'GL_BGR', 'GL_BGRA', 
 'GL_UNSIGNED_BYTE_3_3_2', 'GL_UNSIGNED_BYTE_2_3_3_REV', 
 'GL_UNSIGNED_SHORT_5_6_5', 
 'GL_UNSIGNED_SHORT_5_6_5_REV', 
 'GL_UNSIGNED_SHORT_4_4_4_4', 'GL_UNSIGNED_SHORT_4_4_4_4_REV', 
 'GL_UNSIGNED_SHORT_5_5_5_1', 
 'GL_UNSIGNED_SHORT_1_5_5_5_REV', 
 'GL_UNSIGNED_INT_8_8_8_8', 'GL_UNSIGNED_INT_8_8_8_8_REV', 
 'GL_UNSIGNED_INT_10_10_10_2', 
 'GL_UNSIGNED_INT_2_10_10_10_REV', 
 'GL_LIGHT_MODEL_COLOR_CONTROL', 'GL_SINGLE_COLOR', 
 'GL_SEPARATE_SPECULAR_COLOR', 
 'GL_TEXTURE_MIN_LOD', 'GL_TEXTURE_MAX_LOD', 
 'GL_TEXTURE_BASE_LEVEL', 'GL_TEXTURE_MAX_LEVEL', 
 'GL_SMOOTH_POINT_SIZE_RANGE', 
 'GL_SMOOTH_POINT_SIZE_GRANULARITY', 'GL_SMOOTH_LINE_WIDTH_RANGE', 
 'GL_SMOOTH_LINE_WIDTH_GRANULARITY', 
 'GL_ALIASED_POINT_SIZE_RANGE', 
 'GL_ALIASED_LINE_WIDTH_RANGE', 'GL_PACK_SKIP_IMAGES', 
 'GL_PACK_IMAGE_HEIGHT', 
 'GL_UNPACK_SKIP_IMAGES', 'GL_UNPACK_IMAGE_HEIGHT', 
 'GL_TEXTURE_3D', 
 'GL_PROXY_TEXTURE_3D', 'GL_TEXTURE_DEPTH', 'GL_TEXTURE_WRAP_R', 
 'GL_MAX_3D_TEXTURE_SIZE', 
 'GL_TEXTURE_BINDING_3D', 'glDrawRangeElements', 
 'glTexImage3D', 'glTexSubImage3D', 
 'glCopyTexSubImage3D', 
 'PFNGLDRAWRANGEELEMENTSPROC', 'PFNGLTEXIMAGE3DPROC', 
 'PFNGLTEXSUBIMAGE3DPROC', 
 'PFNGLCOPYTEXSUBIMAGE3DPROC', 'GL_CONSTANT_COLOR', 
 'GL_ONE_MINUS_CONSTANT_COLOR', 
 'GL_CONSTANT_ALPHA', 
 'GL_ONE_MINUS_CONSTANT_ALPHA', 'GL_COLOR_TABLE', 
 'GL_POST_CONVOLUTION_COLOR_TABLE', 
 'GL_POST_COLOR_MATRIX_COLOR_TABLE', 
 'GL_PROXY_COLOR_TABLE', 'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE', 
 'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE', 
 'GL_COLOR_TABLE_SCALE', 
 'GL_COLOR_TABLE_BIAS', 'GL_COLOR_TABLE_FORMAT', 
 'GL_COLOR_TABLE_WIDTH', 
 'GL_COLOR_TABLE_RED_SIZE', 'GL_COLOR_TABLE_GREEN_SIZE', 
 'GL_COLOR_TABLE_BLUE_SIZE', 
 'GL_COLOR_TABLE_ALPHA_SIZE', 
 'GL_COLOR_TABLE_LUMINANCE_SIZE', 'GL_COLOR_TABLE_INTENSITY_SIZE', 
 'GL_CONVOLUTION_1D', 
 'GL_CONVOLUTION_2D', 'GL_SEPARABLE_2D', 
 'GL_CONVOLUTION_BORDER_MODE', 'GL_CONVOLUTION_FILTER_SCALE', 
 'GL_CONVOLUTION_FILTER_BIAS', 
 'GL_REDUCE', 'GL_CONVOLUTION_FORMAT', 
 'GL_CONVOLUTION_WIDTH', 'GL_CONVOLUTION_HEIGHT', 
 'GL_MAX_CONVOLUTION_WIDTH', 
 'GL_MAX_CONVOLUTION_HEIGHT', 'GL_POST_CONVOLUTION_RED_SCALE', 
 'GL_POST_CONVOLUTION_GREEN_SCALE', 
 'GL_POST_CONVOLUTION_BLUE_SCALE', 
 'GL_POST_CONVOLUTION_ALPHA_SCALE', 'GL_POST_CONVOLUTION_RED_BIAS', 
 'GL_POST_CONVOLUTION_GREEN_BIAS', 
 'GL_POST_CONVOLUTION_BLUE_BIAS', 
 'GL_POST_CONVOLUTION_ALPHA_BIAS', 'GL_CONSTANT_BORDER', 
 'GL_REPLICATE_BORDER', 
 'GL_CONVOLUTION_BORDER_COLOR', 'GL_COLOR_MATRIX', 
 'GL_COLOR_MATRIX_STACK_DEPTH', 
 'GL_MAX_COLOR_MATRIX_STACK_DEPTH', 
 'GL_POST_COLOR_MATRIX_RED_SCALE', 'GL_POST_COLOR_MATRIX_GREEN_SCALE', 
 'GL_POST_COLOR_MATRIX_BLUE_SCALE', 
 'GL_POST_COLOR_MATRIX_ALPHA_SCALE', 
 'GL_POST_COLOR_MATRIX_RED_BIAS', 'GL_POST_COLOR_MATRIX_GREEN_BIAS', 
 'GL_POST_COLOR_MATRIX_BLUE_BIAS', 
 'GL_POST_COLOR_MATRIX_ALPHA_BIAS', 
 'GL_HISTOGRAM', 'GL_PROXY_HISTOGRAM', 
 'GL_HISTOGRAM_WIDTH', 
 'GL_HISTOGRAM_FORMAT', 'GL_HISTOGRAM_RED_SIZE', 'GL_HISTOGRAM_GREEN_SIZE', 
 'GL_HISTOGRAM_BLUE_SIZE', 
 'GL_HISTOGRAM_ALPHA_SIZE', 
 'GL_HISTOGRAM_LUMINANCE_SIZE', 'GL_HISTOGRAM_SINK', 
 'GL_MINMAX', 
 'GL_MINMAX_FORMAT', 'GL_MINMAX_SINK', 'GL_TABLE_TOO_LARGE', 
 'GL_BLEND_EQUATION', 
 'GL_MIN', 'GL_MAX', 'GL_FUNC_ADD', 'GL_FUNC_SUBTRACT', 
 'GL_FUNC_REVERSE_SUBTRACT', 
 'GL_BLEND_COLOR', 'glColorTable', 
 'glColorSubTable', 'glColorTableParameteriv', 
 'glColorTableParameterfv', 
 'glCopyColorSubTable', 'glCopyColorTable', 'glGetColorTable', 
 'glGetColorTableParameterfv', 
 'glGetColorTableParameteriv', 'glBlendEquation', 
 'glBlendColor', 'glHistogram', 
 'glResetHistogram', 'glGetHistogram', 
 'glGetHistogramParameterfv', 'glGetHistogramParameteriv', 
 'glMinmax', 
 'glResetMinmax', 'glGetMinmax', 'glGetMinmaxParameterfv', 
 'glGetMinmaxParameteriv', 
 'glConvolutionFilter1D', 'glConvolutionFilter2D', 
 'glConvolutionParameterf', 
 'glConvolutionParameterfv', 
 'glConvolutionParameteri', 'glConvolutionParameteriv', 
 'glCopyConvolutionFilter1D', 
 'glCopyConvolutionFilter2D', 
 'glGetConvolutionFilter', 'glGetConvolutionParameterfv', 
 'glGetConvolutionParameteriv', 
 'glSeparableFilter2D', 'glGetSeparableFilter', 
 'PFNGLBLENDCOLORPROC', 'PFNGLBLENDEQUATIONPROC', 
 'GL_TEXTURE0', 'GL_TEXTURE1', 
 'GL_TEXTURE2', 'GL_TEXTURE3', 'GL_TEXTURE4', 
 'GL_TEXTURE5', 'GL_TEXTURE6', 
 'GL_TEXTURE7', 'GL_TEXTURE8', 'GL_TEXTURE9', 
 'GL_TEXTURE10', 'GL_TEXTURE11', 
 'GL_TEXTURE12', 'GL_TEXTURE13', 'GL_TEXTURE14', 
 'GL_TEXTURE15', 
 'GL_TEXTURE16', 'GL_TEXTURE17', 'GL_TEXTURE18', 'GL_TEXTURE19', 
 'GL_TEXTURE20', 
 'GL_TEXTURE21', 'GL_TEXTURE22', 'GL_TEXTURE23', 
 'GL_TEXTURE24', 'GL_TEXTURE25', 
 'GL_TEXTURE26', 'GL_TEXTURE27', 
 'GL_TEXTURE28', 'GL_TEXTURE29', 'GL_TEXTURE30', 
 'GL_TEXTURE31', 
 'GL_ACTIVE_TEXTURE', 'GL_CLIENT_ACTIVE_TEXTURE', 'GL_MAX_TEXTURE_UNITS', 
 'GL_NORMAL_MAP', 
 'GL_REFLECTION_MAP', 'GL_TEXTURE_CUBE_MAP', 
 'GL_TEXTURE_BINDING_CUBE_MAP', 
 'GL_TEXTURE_CUBE_MAP_POSITIVE_X', 
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y', 
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y', 
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z', 
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z', 'GL_PROXY_TEXTURE_CUBE_MAP', 
 'GL_MAX_CUBE_MAP_TEXTURE_SIZE', 
 'GL_COMPRESSED_ALPHA', 
 'GL_COMPRESSED_LUMINANCE', 'GL_COMPRESSED_LUMINANCE_ALPHA', 
 'GL_COMPRESSED_INTENSITY', 
 'GL_COMPRESSED_RGB', 'GL_COMPRESSED_RGBA', 
 'GL_TEXTURE_COMPRESSION_HINT', 
 'GL_TEXTURE_COMPRESSED_IMAGE_SIZE', 
 'GL_TEXTURE_COMPRESSED', 'GL_NUM_COMPRESSED_TEXTURE_FORMATS', 
 'GL_COMPRESSED_TEXTURE_FORMATS', 
 'GL_MULTISAMPLE', 
 'GL_SAMPLE_ALPHA_TO_COVERAGE', 'GL_SAMPLE_ALPHA_TO_ONE', 
 'GL_SAMPLE_COVERAGE', 
 'GL_SAMPLE_BUFFERS', 'GL_SAMPLES', 'GL_SAMPLE_COVERAGE_VALUE', 
 'GL_SAMPLE_COVERAGE_INVERT', 
 'GL_MULTISAMPLE_BIT', 
 'GL_TRANSPOSE_MODELVIEW_MATRIX', 'GL_TRANSPOSE_PROJECTION_MATRIX', 
 'GL_TRANSPOSE_TEXTURE_MATRIX', 
 'GL_TRANSPOSE_COLOR_MATRIX', 'GL_COMBINE', 
 'GL_COMBINE_RGB', 'GL_COMBINE_ALPHA', 
 'GL_SOURCE0_RGB', 'GL_SOURCE1_RGB', 
 'GL_SOURCE2_RGB', 'GL_SOURCE0_ALPHA', 
 'GL_SOURCE1_ALPHA', 'GL_SOURCE2_ALPHA', 
 'GL_OPERAND0_RGB', 'GL_OPERAND1_RGB', 
 'GL_OPERAND2_RGB', 'GL_OPERAND0_ALPHA', 
 'GL_OPERAND1_ALPHA', 'GL_OPERAND2_ALPHA', 
 'GL_RGB_SCALE', 'GL_ADD_SIGNED', 
 'GL_INTERPOLATE', 'GL_SUBTRACT', 'GL_CONSTANT', 
 'GL_PRIMARY_COLOR', 
 'GL_PREVIOUS', 'GL_DOT3_RGB', 'GL_DOT3_RGBA', 'GL_CLAMP_TO_BORDER', 
 'glActiveTexture', 
 'glClientActiveTexture', 'glCompressedTexImage1D', 
 'glCompressedTexImage2D', 
 'glCompressedTexImage3D', 
 'glCompressedTexSubImage1D', 'glCompressedTexSubImage2D', 
 'glCompressedTexSubImage3D', 
 'glGetCompressedTexImage', 'glMultiTexCoord1d', 
 'glMultiTexCoord1dv', 'glMultiTexCoord1f', 
 'glMultiTexCoord1fv', 
 'glMultiTexCoord1i', 'glMultiTexCoord1iv', 'glMultiTexCoord1s', 
 'glMultiTexCoord1sv', 
 'glMultiTexCoord2d', 'glMultiTexCoord2dv', 
 'glMultiTexCoord2f', 'glMultiTexCoord2fv', 
 'glMultiTexCoord2i', 
 'glMultiTexCoord2iv', 'glMultiTexCoord2s', 'glMultiTexCoord2sv', 
 'glMultiTexCoord3d', 
 'glMultiTexCoord3dv', 'glMultiTexCoord3f', 
 'glMultiTexCoord3fv', 'glMultiTexCoord3i', 
 'glMultiTexCoord3iv', 
 'glMultiTexCoord3s', 'glMultiTexCoord3sv', 'glMultiTexCoord4d', 
 'glMultiTexCoord4dv', 
 'glMultiTexCoord4f', 'glMultiTexCoord4fv', 
 'glMultiTexCoord4i', 'glMultiTexCoord4iv', 
 'glMultiTexCoord4s', 
 'glMultiTexCoord4sv', 'glLoadTransposeMatrixd', 'glLoadTransposeMatrixf', 
 'glMultTransposeMatrixd', 
 'glMultTransposeMatrixf', 'glSampleCoverage', 
 'PFNGLACTIVETEXTUREPROC', 
 'PFNGLSAMPLECOVERAGEPROC', 
 'PFNGLCOMPRESSEDTEXIMAGE3DPROC', 'PFNGLCOMPRESSEDTEXIMAGE2DPROC', 
 'PFNGLCOMPRESSEDTEXIMAGE1DPROC', 
 'PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC', 
 'PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC', 'PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC', 
 'PFNGLGETCOMPRESSEDTEXIMAGEPROC', 
 'GL_ARB_multitexture', 'GL_TEXTURE0_ARB', 
 'GL_TEXTURE1_ARB', 'GL_TEXTURE2_ARB', 
 'GL_TEXTURE3_ARB', 'GL_TEXTURE4_ARB', 
 'GL_TEXTURE5_ARB', 'GL_TEXTURE6_ARB', 
 'GL_TEXTURE7_ARB', 'GL_TEXTURE8_ARB', 
 'GL_TEXTURE9_ARB', 'GL_TEXTURE10_ARB', 
 'GL_TEXTURE11_ARB', 'GL_TEXTURE12_ARB', 
 'GL_TEXTURE13_ARB', 'GL_TEXTURE14_ARB', 
 'GL_TEXTURE15_ARB', 
 'GL_TEXTURE16_ARB', 'GL_TEXTURE17_ARB', 'GL_TEXTURE18_ARB', 
 'GL_TEXTURE19_ARB', 
 'GL_TEXTURE20_ARB', 'GL_TEXTURE21_ARB', 
 'GL_TEXTURE22_ARB', 'GL_TEXTURE23_ARB', 
 'GL_TEXTURE24_ARB', 
 'GL_TEXTURE25_ARB', 'GL_TEXTURE26_ARB', 'GL_TEXTURE27_ARB', 
 'GL_TEXTURE28_ARB', 
 'GL_TEXTURE29_ARB', 'GL_TEXTURE30_ARB', 
 'GL_TEXTURE31_ARB', 'GL_ACTIVE_TEXTURE_ARB', 
 'GL_CLIENT_ACTIVE_TEXTURE_ARB', 
 'GL_MAX_TEXTURE_UNITS_ARB', 'glActiveTextureARB', 
 'glClientActiveTextureARB', 
 'glMultiTexCoord1dARB', 'glMultiTexCoord1dvARB', 
 'glMultiTexCoord1fARB', 
 'glMultiTexCoord1fvARB', 'glMultiTexCoord1iARB', 
 'glMultiTexCoord1ivARB', 
 'glMultiTexCoord1sARB', 'glMultiTexCoord1svARB', 
 'glMultiTexCoord2dARB', 
 'glMultiTexCoord2dvARB', 'glMultiTexCoord2fARB', 
 'glMultiTexCoord2fvARB', 
 'glMultiTexCoord2iARB', 'glMultiTexCoord2ivARB', 
 'glMultiTexCoord2sARB', 
 'glMultiTexCoord2svARB', 'glMultiTexCoord3dARB', 
 'glMultiTexCoord3dvARB', 
 'glMultiTexCoord3fARB', 'glMultiTexCoord3fvARB', 
 'glMultiTexCoord3iARB', 
 'glMultiTexCoord3ivARB', 'glMultiTexCoord3sARB', 
 'glMultiTexCoord3svARB', 
 'glMultiTexCoord4dARB', 'glMultiTexCoord4dvARB', 
 'glMultiTexCoord4fARB', 
 'glMultiTexCoord4fvARB', 'glMultiTexCoord4iARB', 
 'glMultiTexCoord4ivARB', 
 'glMultiTexCoord4sARB', 'glMultiTexCoord4svARB', 
 'PFNGLACTIVETEXTUREARBPROC', 
 'PFNGLCLIENTACTIVETEXTUREARBPROC', 'PFNGLMULTITEXCOORD1DARBPROC', 
 'PFNGLMULTITEXCOORD1DVARBPROC', 
 'PFNGLMULTITEXCOORD1FARBPROC', 
 'PFNGLMULTITEXCOORD1FVARBPROC', 'PFNGLMULTITEXCOORD1IARBPROC', 
 'PFNGLMULTITEXCOORD1IVARBPROC', 
 'PFNGLMULTITEXCOORD1SARBPROC', 
 'PFNGLMULTITEXCOORD1SVARBPROC', 'PFNGLMULTITEXCOORD2DARBPROC', 
 'PFNGLMULTITEXCOORD2DVARBPROC', 
 'PFNGLMULTITEXCOORD2FARBPROC', 
 'PFNGLMULTITEXCOORD2FVARBPROC', 'PFNGLMULTITEXCOORD2IARBPROC', 
 'PFNGLMULTITEXCOORD2IVARBPROC', 
 'PFNGLMULTITEXCOORD2SARBPROC', 
 'PFNGLMULTITEXCOORD2SVARBPROC', 'PFNGLMULTITEXCOORD3DARBPROC', 
 'PFNGLMULTITEXCOORD3DVARBPROC', 
 'PFNGLMULTITEXCOORD3FARBPROC', 
 'PFNGLMULTITEXCOORD3FVARBPROC', 'PFNGLMULTITEXCOORD3IARBPROC', 
 'PFNGLMULTITEXCOORD3IVARBPROC', 
 'PFNGLMULTITEXCOORD3SARBPROC', 
 'PFNGLMULTITEXCOORD3SVARBPROC', 'PFNGLMULTITEXCOORD4DARBPROC', 
 'PFNGLMULTITEXCOORD4DVARBPROC', 
 'PFNGLMULTITEXCOORD4FARBPROC', 
 'PFNGLMULTITEXCOORD4FVARBPROC', 'PFNGLMULTITEXCOORD4IARBPROC', 
 'PFNGLMULTITEXCOORD4IVARBPROC', 
 'PFNGLMULTITEXCOORD4SARBPROC', 
 'PFNGLMULTITEXCOORD4SVARBPROC', 'GL_MESA_shader_debug', 
 'GL_DEBUG_OBJECT_MESA', 
 'GL_DEBUG_PRINT_MESA', 'GL_DEBUG_ASSERT_MESA', 
 'glCreateDebugObjectMESA', 
 'glClearDebugLogMESA', 'glGetDebugLogMESA', 
 'glGetDebugLogLengthMESA', 'GL_MESA_packed_depth_stencil', 
 'GL_DEPTH_STENCIL_MESA', 
 'GL_UNSIGNED_INT_24_8_MESA', 
 'GL_UNSIGNED_INT_8_24_REV_MESA', 'GL_UNSIGNED_SHORT_15_1_MESA', 
 'GL_UNSIGNED_SHORT_1_15_REV_MESA', 
 'GL_MESA_program_debug', 
 'GL_FRAGMENT_PROGRAM_POSITION_MESA', 'GL_FRAGMENT_PROGRAM_CALLBACK_MESA', 
 'GL_FRAGMENT_PROGRAM_CALLBACK_FUNC_MESA', 
 'GL_FRAGMENT_PROGRAM_CALLBACK_DATA_MESA', 
 'GL_VERTEX_PROGRAM_POSITION_MESA', 
 'GL_VERTEX_PROGRAM_CALLBACK_MESA', 'GL_VERTEX_PROGRAM_CALLBACK_FUNC_MESA', 
 'GL_VERTEX_PROGRAM_CALLBACK_DATA_MESA', 
 'GLprogramcallbackMESA', 
 'glProgramCallbackMESA', 'glGetProgramRegisterfvMESA', 
 'GL_MESA_texture_array', 
 'GL_ATI_blend_equation_separate', 
 'GL_ALPHA_BLEND_EQUATION_ATI', 'glBlendEquationSeparateATI', 
 'PFNGLBLENDEQUATIONSEPARATEATIPROC']
# okay decompiling out\pyglet.gl.gl.pyc
