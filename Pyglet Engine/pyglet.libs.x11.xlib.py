# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.x11.xlib
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
import pyglet.lib
_lib = pyglet.lib.load_library('X11')
_int_types = (
 c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t

class c_void(Structure):
    _fields_ = [
     (
      'dummy', c_int)]


XlibSpecificationRelease = 6
X_PROTOCOL = 11
X_PROTOCOL_REVISION = 0
XID = c_ulong
Mask = c_ulong
Atom = c_ulong
VisualID = c_ulong
Time = c_ulong
Window = XID
Drawable = XID
Font = XID
Pixmap = XID
Cursor = XID
Colormap = XID
GContext = XID
KeySym = XID
KeyCode = c_ubyte
None_ = 0
ParentRelative = 1
CopyFromParent = 0
PointerWindow = 0
InputFocus = 1
PointerRoot = 1
AnyPropertyType = 0
AnyKey = 0
AnyButton = 0
AllTemporary = 0
CurrentTime = 0
NoSymbol = 0
NoEventMask = 0
KeyPressMask = 1
KeyReleaseMask = 2
ButtonPressMask = 4
ButtonReleaseMask = 8
EnterWindowMask = 16
LeaveWindowMask = 32
PointerMotionMask = 64
PointerMotionHintMask = 128
Button1MotionMask = 256
Button2MotionMask = 512
Button3MotionMask = 1024
Button4MotionMask = 2048
Button5MotionMask = 4096
ButtonMotionMask = 8192
KeymapStateMask = 16384
ExposureMask = 32768
VisibilityChangeMask = 65536
StructureNotifyMask = 131072
ResizeRedirectMask = 262144
SubstructureNotifyMask = 524288
SubstructureRedirectMask = 1048576
FocusChangeMask = 2097152
PropertyChangeMask = 4194304
ColormapChangeMask = 8388608
OwnerGrabButtonMask = 16777216
KeyPress = 2
KeyRelease = 3
ButtonPress = 4
ButtonRelease = 5
MotionNotify = 6
EnterNotify = 7
LeaveNotify = 8
FocusIn = 9
FocusOut = 10
KeymapNotify = 11
Expose = 12
GraphicsExpose = 13
NoExpose = 14
VisibilityNotify = 15
CreateNotify = 16
DestroyNotify = 17
UnmapNotify = 18
MapNotify = 19
MapRequest = 20
ReparentNotify = 21
ConfigureNotify = 22
ConfigureRequest = 23
GravityNotify = 24
ResizeRequest = 25
CirculateNotify = 26
CirculateRequest = 27
PropertyNotify = 28
SelectionClear = 29
SelectionRequest = 30
SelectionNotify = 31
ColormapNotify = 32
ClientMessage = 33
MappingNotify = 34
GenericEvent = 35
LASTEvent = 36
ShiftMask = 1
LockMask = 2
ControlMask = 4
Mod1Mask = 8
Mod2Mask = 16
Mod3Mask = 32
Mod4Mask = 64
Mod5Mask = 128
ShiftMapIndex = 0
LockMapIndex = 1
ControlMapIndex = 2
Mod1MapIndex = 3
Mod2MapIndex = 4
Mod3MapIndex = 5
Mod4MapIndex = 6
Mod5MapIndex = 7
Button1Mask = 256
Button2Mask = 512
Button3Mask = 1024
Button4Mask = 2048
Button5Mask = 4096
AnyModifier = 32768
Button1 = 1
Button2 = 2
Button3 = 3
Button4 = 4
Button5 = 5
NotifyNormal = 0
NotifyGrab = 1
NotifyUngrab = 2
NotifyWhileGrabbed = 3
NotifyHint = 1
NotifyAncestor = 0
NotifyVirtual = 1
NotifyInferior = 2
NotifyNonlinear = 3
NotifyNonlinearVirtual = 4
NotifyPointer = 5
NotifyPointerRoot = 6
NotifyDetailNone = 7
VisibilityUnobscured = 0
VisibilityPartiallyObscured = 1
VisibilityFullyObscured = 2
PlaceOnTop = 0
PlaceOnBottom = 1
FamilyInternet = 0
FamilyDECnet = 1
FamilyChaos = 2
FamilyInternet6 = 6
FamilyServerInterpreted = 5
PropertyNewValue = 0
PropertyDelete = 1
ColormapUninstalled = 0
ColormapInstalled = 1
GrabModeSync = 0
GrabModeAsync = 1
GrabSuccess = 0
AlreadyGrabbed = 1
GrabInvalidTime = 2
GrabNotViewable = 3
GrabFrozen = 4
AsyncPointer = 0
SyncPointer = 1
ReplayPointer = 2
AsyncKeyboard = 3
SyncKeyboard = 4
ReplayKeyboard = 5
AsyncBoth = 6
SyncBoth = 7
RevertToParent = 2
Success = 0
BadRequest = 1
BadValue = 2
BadWindow = 3
BadPixmap = 4
BadAtom = 5
BadCursor = 6
BadFont = 7
BadMatch = 8
BadDrawable = 9
BadAccess = 10
BadAlloc = 11
BadColor = 12
BadGC = 13
BadIDChoice = 14
BadName = 15
BadLength = 16
BadImplementation = 17
FirstExtensionError = 128
LastExtensionError = 255
InputOutput = 1
InputOnly = 2
CWBackPixmap = 1
CWBackPixel = 2
CWBorderPixmap = 4
CWBorderPixel = 8
CWBitGravity = 16
CWWinGravity = 32
CWBackingStore = 64
CWBackingPlanes = 128
CWBackingPixel = 256
CWOverrideRedirect = 512
CWSaveUnder = 1024
CWEventMask = 2048
CWDontPropagate = 4096
CWColormap = 8192
CWCursor = 16384
CWX = 1
CWY = 2
CWWidth = 4
CWHeight = 8
CWBorderWidth = 16
CWSibling = 32
CWStackMode = 64
ForgetGravity = 0
NorthWestGravity = 1
NorthGravity = 2
NorthEastGravity = 3
WestGravity = 4
CenterGravity = 5
EastGravity = 6
SouthWestGravity = 7
SouthGravity = 8
SouthEastGravity = 9
StaticGravity = 10
UnmapGravity = 0
NotUseful = 0
WhenMapped = 1
Always = 2
IsUnmapped = 0
IsUnviewable = 1
IsViewable = 2
SetModeInsert = 0
SetModeDelete = 1
DestroyAll = 0
RetainPermanent = 1
RetainTemporary = 2
Above = 0
Below = 1
TopIf = 2
BottomIf = 3
Opposite = 4
RaiseLowest = 0
LowerHighest = 1
PropModeReplace = 0
PropModePrepend = 1
PropModeAppend = 2
GXclear = 0
GXand = 1
GXandReverse = 2
GXcopy = 3
GXandInverted = 4
GXnoop = 5
GXxor = 6
GXor = 7
GXnor = 8
GXequiv = 9
GXinvert = 10
GXorReverse = 11
GXcopyInverted = 12
GXorInverted = 13
GXnand = 14
GXset = 15
LineSolid = 0
LineOnOffDash = 1
LineDoubleDash = 2
CapNotLast = 0
CapButt = 1
CapRound = 2
CapProjecting = 3
JoinMiter = 0
JoinRound = 1
JoinBevel = 2
FillSolid = 0
FillTiled = 1
FillStippled = 2
FillOpaqueStippled = 3
EvenOddRule = 0
WindingRule = 1
ClipByChildren = 0
IncludeInferiors = 1
Unsorted = 0
YSorted = 1
YXSorted = 2
YXBanded = 3
CoordModeOrigin = 0
CoordModePrevious = 1
Complex = 0
Nonconvex = 1
Convex = 2
ArcChord = 0
ArcPieSlice = 1
GCFunction = 1
GCPlaneMask = 2
GCForeground = 4
GCBackground = 8
GCLineWidth = 16
GCLineStyle = 32
GCCapStyle = 64
GCJoinStyle = 128
GCFillStyle = 256
GCFillRule = 512
GCTile = 1024
GCStipple = 2048
GCTileStipXOrigin = 4096
GCTileStipYOrigin = 8192
GCFont = 16384
GCSubwindowMode = 32768
GCGraphicsExposures = 65536
GCClipXOrigin = 131072
GCClipYOrigin = 262144
GCClipMask = 524288
GCDashOffset = 1048576
GCDashList = 2097152
GCArcMode = 4194304
GCLastBit = 22
FontLeftToRight = 0
FontRightToLeft = 1
FontChange = 255
XYBitmap = 0
XYPixmap = 1
ZPixmap = 2
AllocNone = 0
AllocAll = 1
DoRed = 1
DoGreen = 2
DoBlue = 4
CursorShape = 0
TileShape = 1
StippleShape = 2
AutoRepeatModeOff = 0
AutoRepeatModeOn = 1
AutoRepeatModeDefault = 2
LedModeOff = 0
LedModeOn = 1
KBKeyClickPercent = 1
KBBellPercent = 2
KBBellPitch = 4
KBBellDuration = 8
KBLed = 16
KBLedMode = 32
KBKey = 64
KBAutoRepeatMode = 128
MappingSuccess = 0
MappingBusy = 1
MappingFailed = 2
MappingModifier = 0
MappingKeyboard = 1
MappingPointer = 2
DontPreferBlanking = 0
PreferBlanking = 1
DefaultBlanking = 2
DisableScreenSaver = 0
DisableScreenInterval = 0
DontAllowExposures = 0
AllowExposures = 1
DefaultExposures = 2
ScreenSaverReset = 0
ScreenSaverActive = 1
HostInsert = 0
HostDelete = 1
EnableAccess = 1
DisableAccess = 0
StaticGray = 0
GrayScale = 1
StaticColor = 2
PseudoColor = 3
TrueColor = 4
DirectColor = 5
LSBFirst = 0
MSBFirst = 1
_Xmblen = _lib._Xmblen
_Xmblen.restype = c_int
_Xmblen.argtypes = [c_char_p, c_int]
X_HAVE_UTF8_STRING = 1
XPointer = c_char_p
Bool = c_int
Status = c_int
True_ = 1
False_ = 0
QueuedAlready = 0
QueuedAfterReading = 1
QueuedAfterFlush = 2

class struct__XExtData(Structure):
    __slots__ = [
     'number',
     'next',
     'free_private',
     'private_data']


struct__XExtData._fields_ = [
 (
  'number', c_int),
 (
  'next', POINTER(struct__XExtData)),
 (
  'free_private', POINTER(CFUNCTYPE(c_int, POINTER(struct__XExtData)))),
 (
  'private_data', XPointer)]
XExtData = struct__XExtData

class struct_anon_15(Structure):
    __slots__ = [
     'extension',
     'major_opcode',
     'first_event',
     'first_error']


struct_anon_15._fields_ = [
 (
  'extension', c_int),
 (
  'major_opcode', c_int),
 (
  'first_event', c_int),
 (
  'first_error', c_int)]
XExtCodes = struct_anon_15

class struct_anon_16(Structure):
    __slots__ = [
     'depth',
     'bits_per_pixel',
     'scanline_pad']


struct_anon_16._fields_ = [
 (
  'depth', c_int),
 (
  'bits_per_pixel', c_int),
 (
  'scanline_pad', c_int)]
XPixmapFormatValues = struct_anon_16

class struct_anon_17(Structure):
    __slots__ = [
     'function', 
     'plane_mask', 
     'foreground', 
     'background', 
     'line_width', 
     'line_style', 
     'cap_style', 
     'join_style', 
     'fill_style', 
     'fill_rule', 
     'arc_mode', 
     'tile', 
     'stipple', 
     'ts_x_origin', 
     'ts_y_origin', 
     'font', 
     'subwindow_mode', 
     'graphics_exposures', 
     'clip_x_origin', 
     'clip_y_origin', 
     'clip_mask', 
     'dash_offset', 
     'dashes']


struct_anon_17._fields_ = [
 (
  'function', c_int),
 (
  'plane_mask', c_ulong),
 (
  'foreground', c_ulong),
 (
  'background', c_ulong),
 (
  'line_width', c_int),
 (
  'line_style', c_int),
 (
  'cap_style', c_int),
 (
  'join_style', c_int),
 (
  'fill_style', c_int),
 (
  'fill_rule', c_int),
 (
  'arc_mode', c_int),
 (
  'tile', Pixmap),
 (
  'stipple', Pixmap),
 (
  'ts_x_origin', c_int),
 (
  'ts_y_origin', c_int),
 (
  'font', Font),
 (
  'subwindow_mode', c_int),
 (
  'graphics_exposures', c_int),
 (
  'clip_x_origin', c_int),
 (
  'clip_y_origin', c_int),
 (
  'clip_mask', Pixmap),
 (
  'dash_offset', c_int),
 (
  'dashes', c_char)]
XGCValues = struct_anon_17

class struct__XGC(Structure):
    __slots__ = []


struct__XGC._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XGC(Structure):
    __slots__ = []


struct__XGC._fields_ = [
 (
  '_opaque_struct', c_int)]
GC = POINTER(struct__XGC)

class struct_anon_18(Structure):
    __slots__ = [
     'ext_data', 
     'visualid', 
     'class', 
     'red_mask', 
     'green_mask', 
     'blue_mask', 
     'bits_per_rgb', 
     'map_entries']


struct_anon_18._fields_ = [
 (
  'ext_data', POINTER(XExtData)),
 (
  'visualid', VisualID),
 (
  'class', c_int),
 (
  'red_mask', c_ulong),
 (
  'green_mask', c_ulong),
 (
  'blue_mask', c_ulong),
 (
  'bits_per_rgb', c_int),
 (
  'map_entries', c_int)]
Visual = struct_anon_18

class struct_anon_19(Structure):
    __slots__ = [
     'depth',
     'nvisuals',
     'visuals']


struct_anon_19._fields_ = [
 (
  'depth', c_int),
 (
  'nvisuals', c_int),
 (
  'visuals', POINTER(Visual))]
Depth = struct_anon_19

class struct_anon_20(Structure):
    __slots__ = [
     'ext_data', 
     'display', 
     'root', 
     'width', 
     'height', 
     'mwidth', 
     'mheight', 
     'ndepths', 
     'depths', 
     'root_depth', 
     'root_visual', 
     'default_gc', 
     'cmap', 
     'white_pixel', 
     'black_pixel', 
     'max_maps', 
     'min_maps', 
     'backing_store', 
     'save_unders', 
     'root_input_mask']


class struct__XDisplay(Structure):
    __slots__ = []


struct__XDisplay._fields_ = [
 (
  '_opaque_struct', c_int)]
struct_anon_20._fields_ = [
 (
  'ext_data', POINTER(XExtData)),
 (
  'display', POINTER(struct__XDisplay)),
 (
  'root', Window),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'mwidth', c_int),
 (
  'mheight', c_int),
 (
  'ndepths', c_int),
 (
  'depths', POINTER(Depth)),
 (
  'root_depth', c_int),
 (
  'root_visual', POINTER(Visual)),
 (
  'default_gc', GC),
 (
  'cmap', Colormap),
 (
  'white_pixel', c_ulong),
 (
  'black_pixel', c_ulong),
 (
  'max_maps', c_int),
 (
  'min_maps', c_int),
 (
  'backing_store', c_int),
 (
  'save_unders', c_int),
 (
  'root_input_mask', c_long)]
Screen = struct_anon_20

class struct_anon_21(Structure):
    __slots__ = [
     'ext_data',
     'depth',
     'bits_per_pixel',
     'scanline_pad']


struct_anon_21._fields_ = [
 (
  'ext_data', POINTER(XExtData)),
 (
  'depth', c_int),
 (
  'bits_per_pixel', c_int),
 (
  'scanline_pad', c_int)]
ScreenFormat = struct_anon_21

class struct_anon_22(Structure):
    __slots__ = [
     'background_pixmap', 
     'background_pixel', 
     'border_pixmap', 
     'border_pixel', 
     'bit_gravity', 
     'win_gravity', 
     'backing_store', 
     'backing_planes', 
     'backing_pixel', 
     'save_under', 
     'event_mask', 
     'do_not_propagate_mask', 
     'override_redirect', 
     'colormap', 
     'cursor']


struct_anon_22._fields_ = [
 (
  'background_pixmap', Pixmap),
 (
  'background_pixel', c_ulong),
 (
  'border_pixmap', Pixmap),
 (
  'border_pixel', c_ulong),
 (
  'bit_gravity', c_int),
 (
  'win_gravity', c_int),
 (
  'backing_store', c_int),
 (
  'backing_planes', c_ulong),
 (
  'backing_pixel', c_ulong),
 (
  'save_under', c_int),
 (
  'event_mask', c_long),
 (
  'do_not_propagate_mask', c_long),
 (
  'override_redirect', c_int),
 (
  'colormap', Colormap),
 (
  'cursor', Cursor)]
XSetWindowAttributes = struct_anon_22

class struct_anon_23(Structure):
    __slots__ = [
     'x', 
     'y', 
     'width', 
     'height', 
     'border_width', 
     'depth', 
     'visual', 
     'root', 
     'class', 
     'bit_gravity', 
     'win_gravity', 
     'backing_store', 
     'backing_planes', 
     'backing_pixel', 
     'save_under', 
     'colormap', 
     'map_installed', 
     'map_state', 
     'all_event_masks', 
     'your_event_mask', 
     'do_not_propagate_mask', 
     'override_redirect', 
     'screen']


struct_anon_23._fields_ = [
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'border_width', c_int),
 (
  'depth', c_int),
 (
  'visual', POINTER(Visual)),
 (
  'root', Window),
 (
  'class', c_int),
 (
  'bit_gravity', c_int),
 (
  'win_gravity', c_int),
 (
  'backing_store', c_int),
 (
  'backing_planes', c_ulong),
 (
  'backing_pixel', c_ulong),
 (
  'save_under', c_int),
 (
  'colormap', Colormap),
 (
  'map_installed', c_int),
 (
  'map_state', c_int),
 (
  'all_event_masks', c_long),
 (
  'your_event_mask', c_long),
 (
  'do_not_propagate_mask', c_long),
 (
  'override_redirect', c_int),
 (
  'screen', POINTER(Screen))]
XWindowAttributes = struct_anon_23

class struct_anon_24(Structure):
    __slots__ = [
     'family',
     'length',
     'address']


struct_anon_24._fields_ = [
 (
  'family', c_int),
 (
  'length', c_int),
 (
  'address', c_char_p)]
XHostAddress = struct_anon_24

class struct_anon_25(Structure):
    __slots__ = [
     'typelength',
     'valuelength',
     'type',
     'value']


struct_anon_25._fields_ = [
 (
  'typelength', c_int),
 (
  'valuelength', c_int),
 (
  'type', c_char_p),
 (
  'value', c_char_p)]
XServerInterpretedAddress = struct_anon_25

class struct__XImage(Structure):
    __slots__ = [
     'width', 
     'height', 
     'xoffset', 
     'format', 
     'data', 
     'byte_order', 
     'bitmap_unit', 
     'bitmap_bit_order', 
     'bitmap_pad', 
     'depth', 
     'bytes_per_line', 
     'bits_per_pixel', 
     'red_mask', 
     'green_mask', 
     'blue_mask', 
     'obdata', 
     'f']


class struct_funcs(Structure):
    __slots__ = [
     'create_image', 
     'destroy_image', 
     'get_pixel', 
     'put_pixel', 
     'sub_image', 
     'add_pixel']


class struct__XDisplay(Structure):
    __slots__ = []


struct__XDisplay._fields_ = [
 (
  '_opaque_struct', c_int)]
struct_funcs._fields_ = [
 (
  'create_image', POINTER(CFUNCTYPE(POINTER(struct__XImage), POINTER(struct__XDisplay), POINTER(Visual), c_uint, c_int, c_int, c_char_p, c_uint, c_uint, c_int, c_int))),
 (
  'destroy_image', POINTER(CFUNCTYPE(c_int, POINTER(struct__XImage)))),
 (
  'get_pixel', POINTER(CFUNCTYPE(c_ulong, POINTER(struct__XImage), c_int, c_int))),
 (
  'put_pixel', POINTER(CFUNCTYPE(c_int, POINTER(struct__XImage), c_int, c_int, c_ulong))),
 (
  'sub_image', POINTER(CFUNCTYPE(POINTER(struct__XImage), POINTER(struct__XImage), c_int, c_int, c_uint, c_uint))),
 (
  'add_pixel', POINTER(CFUNCTYPE(c_int, POINTER(struct__XImage), c_long)))]
struct__XImage._fields_ = [
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'xoffset', c_int),
 (
  'format', c_int),
 (
  'data', c_char_p),
 (
  'byte_order', c_int),
 (
  'bitmap_unit', c_int),
 (
  'bitmap_bit_order', c_int),
 (
  'bitmap_pad', c_int),
 (
  'depth', c_int),
 (
  'bytes_per_line', c_int),
 (
  'bits_per_pixel', c_int),
 (
  'red_mask', c_ulong),
 (
  'green_mask', c_ulong),
 (
  'blue_mask', c_ulong),
 (
  'obdata', XPointer),
 (
  'f', struct_funcs)]
XImage = struct__XImage

class struct_anon_26(Structure):
    __slots__ = [
     'x', 
     'y', 
     'width', 
     'height', 
     'border_width', 
     'sibling', 
     'stack_mode']


struct_anon_26._fields_ = [
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'border_width', c_int),
 (
  'sibling', Window),
 (
  'stack_mode', c_int)]
XWindowChanges = struct_anon_26

class struct_anon_27(Structure):
    __slots__ = [
     'pixel', 
     'red', 
     'green', 
     'blue', 
     'flags', 
     'pad']


struct_anon_27._fields_ = [
 (
  'pixel', c_ulong),
 (
  'red', c_ushort),
 (
  'green', c_ushort),
 (
  'blue', c_ushort),
 (
  'flags', c_char),
 (
  'pad', c_char)]
XColor = struct_anon_27

class struct_anon_28(Structure):
    __slots__ = [
     'x1',
     'y1',
     'x2',
     'y2']


struct_anon_28._fields_ = [
 (
  'x1', c_short),
 (
  'y1', c_short),
 (
  'x2', c_short),
 (
  'y2', c_short)]
XSegment = struct_anon_28

class struct_anon_29(Structure):
    __slots__ = [
     'x',
     'y']


struct_anon_29._fields_ = [
 (
  'x', c_short),
 (
  'y', c_short)]
XPoint = struct_anon_29

class struct_anon_30(Structure):
    __slots__ = [
     'x',
     'y',
     'width',
     'height']


struct_anon_30._fields_ = [
 (
  'x', c_short),
 (
  'y', c_short),
 (
  'width', c_ushort),
 (
  'height', c_ushort)]
XRectangle = struct_anon_30

class struct_anon_31(Structure):
    __slots__ = [
     'x', 
     'y', 
     'width', 
     'height', 
     'angle1', 
     'angle2']


struct_anon_31._fields_ = [
 (
  'x', c_short),
 (
  'y', c_short),
 (
  'width', c_ushort),
 (
  'height', c_ushort),
 (
  'angle1', c_short),
 (
  'angle2', c_short)]
XArc = struct_anon_31

class struct_anon_32(Structure):
    __slots__ = [
     'key_click_percent', 
     'bell_percent', 
     'bell_pitch', 
     'bell_duration', 
     'led', 
     'led_mode', 
     'key', 
     'auto_repeat_mode']


struct_anon_32._fields_ = [
 (
  'key_click_percent', c_int),
 (
  'bell_percent', c_int),
 (
  'bell_pitch', c_int),
 (
  'bell_duration', c_int),
 (
  'led', c_int),
 (
  'led_mode', c_int),
 (
  'key', c_int),
 (
  'auto_repeat_mode', c_int)]
XKeyboardControl = struct_anon_32

class struct_anon_33(Structure):
    __slots__ = [
     'key_click_percent', 
     'bell_percent', 
     'bell_pitch', 
     'bell_duration', 
     'led_mask', 
     'global_auto_repeat', 
     'auto_repeats']


struct_anon_33._fields_ = [
 (
  'key_click_percent', c_int),
 (
  'bell_percent', c_int),
 (
  'bell_pitch', c_uint),
 (
  'bell_duration', c_uint),
 (
  'led_mask', c_ulong),
 (
  'global_auto_repeat', c_int),
 (
  'auto_repeats', c_char * 32)]
XKeyboardState = struct_anon_33

class struct_anon_34(Structure):
    __slots__ = [
     'time',
     'x',
     'y']


struct_anon_34._fields_ = [
 (
  'time', Time),
 (
  'x', c_short),
 (
  'y', c_short)]
XTimeCoord = struct_anon_34

class struct_anon_35(Structure):
    __slots__ = [
     'max_keypermod',
     'modifiermap']


struct_anon_35._fields_ = [
 (
  'max_keypermod', c_int),
 (
  'modifiermap', POINTER(KeyCode))]
XModifierKeymap = struct_anon_35

class struct__XDisplay(Structure):
    __slots__ = []


struct__XDisplay._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XDisplay(Structure):
    __slots__ = []


struct__XDisplay._fields_ = [
 (
  '_opaque_struct', c_int)]
Display = struct__XDisplay

class struct_anon_36(Structure):
    __slots__ = [
     'ext_data', 
     'private1', 
     'fd', 
     'private2', 
     'proto_major_version', 
     'proto_minor_version', 
     'vendor', 
     'private3', 
     'private4', 
     'private5', 
     'private6', 
     'resource_alloc', 
     'byte_order', 
     'bitmap_unit', 
     'bitmap_pad', 
     'bitmap_bit_order', 
     'nformats', 
     'pixmap_format', 
     'private8', 
     'release', 
     'private9', 
     'private10', 
     'qlen', 
     'last_request_read', 
     'request', 
     'private11', 
     'private12', 
     'private13', 
     'private14', 
     'max_request_size', 
     'db', 
     'private15', 
     'display_name', 
     'default_screen', 
     'nscreens', 
     'screens', 
     'motion_buffer', 
     'private16', 
     'min_keycode', 
     'max_keycode', 
     'private17', 
     'private18', 
     'private19', 
     'xdefaults']


class struct__XPrivate(Structure):
    __slots__ = []


struct__XPrivate._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XDisplay(Structure):
    __slots__ = []


struct__XDisplay._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XPrivate(Structure):
    __slots__ = []


struct__XPrivate._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XPrivate(Structure):
    __slots__ = []


struct__XPrivate._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XrmHashBucketRec(Structure):
    __slots__ = []


struct__XrmHashBucketRec._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XDisplay(Structure):
    __slots__ = []


struct__XDisplay._fields_ = [
 (
  '_opaque_struct', c_int)]
struct_anon_36._fields_ = [
 (
  'ext_data', POINTER(XExtData)),
 (
  'private1', POINTER(struct__XPrivate)),
 (
  'fd', c_int),
 (
  'private2', c_int),
 (
  'proto_major_version', c_int),
 (
  'proto_minor_version', c_int),
 (
  'vendor', c_char_p),
 (
  'private3', XID),
 (
  'private4', XID),
 (
  'private5', XID),
 (
  'private6', c_int),
 (
  'resource_alloc', POINTER(CFUNCTYPE(XID, POINTER(struct__XDisplay)))),
 (
  'byte_order', c_int),
 (
  'bitmap_unit', c_int),
 (
  'bitmap_pad', c_int),
 (
  'bitmap_bit_order', c_int),
 (
  'nformats', c_int),
 (
  'pixmap_format', POINTER(ScreenFormat)),
 (
  'private8', c_int),
 (
  'release', c_int),
 (
  'private9', POINTER(struct__XPrivate)),
 (
  'private10', POINTER(struct__XPrivate)),
 (
  'qlen', c_int),
 (
  'last_request_read', c_ulong),
 (
  'request', c_ulong),
 (
  'private11', XPointer),
 (
  'private12', XPointer),
 (
  'private13', XPointer),
 (
  'private14', XPointer),
 (
  'max_request_size', c_uint),
 (
  'db', POINTER(struct__XrmHashBucketRec)),
 (
  'private15', POINTER(CFUNCTYPE(c_int, POINTER(struct__XDisplay)))),
 (
  'display_name', c_char_p),
 (
  'default_screen', c_int),
 (
  'nscreens', c_int),
 (
  'screens', POINTER(Screen)),
 (
  'motion_buffer', c_ulong),
 (
  'private16', c_ulong),
 (
  'min_keycode', c_int),
 (
  'max_keycode', c_int),
 (
  'private17', XPointer),
 (
  'private18', XPointer),
 (
  'private19', c_int),
 (
  'xdefaults', c_char_p)]
_XPrivDisplay = POINTER(struct_anon_36)

class struct_anon_37(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'keycode', 
     'same_screen']


struct_anon_37._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'keycode', c_uint),
 (
  'same_screen', c_int)]
XKeyEvent = struct_anon_37
XKeyPressedEvent = XKeyEvent
XKeyReleasedEvent = XKeyEvent

class struct_anon_38(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'button', 
     'same_screen']


struct_anon_38._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'button', c_uint),
 (
  'same_screen', c_int)]
XButtonEvent = struct_anon_38
XButtonPressedEvent = XButtonEvent
XButtonReleasedEvent = XButtonEvent

class struct_anon_39(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'state', 
     'is_hint', 
     'same_screen']


struct_anon_39._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'state', c_uint),
 (
  'is_hint', c_char),
 (
  'same_screen', c_int)]
XMotionEvent = struct_anon_39
XPointerMovedEvent = XMotionEvent

class struct_anon_40(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'root', 
     'subwindow', 
     'time', 
     'x', 
     'y', 
     'x_root', 
     'y_root', 
     'mode', 
     'detail', 
     'same_screen', 
     'focus', 
     'state']


struct_anon_40._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'root', Window),
 (
  'subwindow', Window),
 (
  'time', Time),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'x_root', c_int),
 (
  'y_root', c_int),
 (
  'mode', c_int),
 (
  'detail', c_int),
 (
  'same_screen', c_int),
 (
  'focus', c_int),
 (
  'state', c_uint)]
XCrossingEvent = struct_anon_40
XEnterWindowEvent = XCrossingEvent
XLeaveWindowEvent = XCrossingEvent

class struct_anon_41(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'mode', 
     'detail']


struct_anon_41._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'mode', c_int),
 (
  'detail', c_int)]
XFocusChangeEvent = struct_anon_41
XFocusInEvent = XFocusChangeEvent
XFocusOutEvent = XFocusChangeEvent

class struct_anon_42(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'key_vector']


struct_anon_42._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'key_vector', c_char * 32)]
XKeymapEvent = struct_anon_42

class struct_anon_43(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'x', 
     'y', 
     'width', 
     'height', 
     'count']


struct_anon_43._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
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
XExposeEvent = struct_anon_43

class struct_anon_44(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'drawable', 
     'x', 
     'y', 
     'width', 
     'height', 
     'count', 
     'major_code', 
     'minor_code']


struct_anon_44._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'drawable', Drawable),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'count', c_int),
 (
  'major_code', c_int),
 (
  'minor_code', c_int)]
XGraphicsExposeEvent = struct_anon_44

class struct_anon_45(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'drawable', 
     'major_code', 
     'minor_code']


struct_anon_45._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'drawable', Drawable),
 (
  'major_code', c_int),
 (
  'minor_code', c_int)]
XNoExposeEvent = struct_anon_45

class struct_anon_46(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'state']


struct_anon_46._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'state', c_int)]
XVisibilityEvent = struct_anon_46

class struct_anon_47(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'parent', 
     'window', 
     'x', 
     'y', 
     'width', 
     'height', 
     'border_width', 
     'override_redirect']


struct_anon_47._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'parent', Window),
 (
  'window', Window),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'border_width', c_int),
 (
  'override_redirect', c_int)]
XCreateWindowEvent = struct_anon_47

class struct_anon_48(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window']


struct_anon_48._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window)]
XDestroyWindowEvent = struct_anon_48

class struct_anon_49(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window', 
     'from_configure']


struct_anon_49._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window),
 (
  'from_configure', c_int)]
XUnmapEvent = struct_anon_49

class struct_anon_50(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window', 
     'override_redirect']


struct_anon_50._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window),
 (
  'override_redirect', c_int)]
XMapEvent = struct_anon_50

class struct_anon_51(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'parent', 
     'window']


struct_anon_51._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'parent', Window),
 (
  'window', Window)]
XMapRequestEvent = struct_anon_51

class struct_anon_52(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window', 
     'parent', 
     'x', 
     'y', 
     'override_redirect']


struct_anon_52._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window),
 (
  'parent', Window),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'override_redirect', c_int)]
XReparentEvent = struct_anon_52

class struct_anon_53(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window', 
     'x', 
     'y', 
     'width', 
     'height', 
     'border_width', 
     'above', 
     'override_redirect']


struct_anon_53._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'border_width', c_int),
 (
  'above', Window),
 (
  'override_redirect', c_int)]
XConfigureEvent = struct_anon_53

class struct_anon_54(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window', 
     'x', 
     'y']


struct_anon_54._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window),
 (
  'x', c_int),
 (
  'y', c_int)]
XGravityEvent = struct_anon_54

class struct_anon_55(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'width', 
     'height']


struct_anon_55._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'width', c_int),
 (
  'height', c_int)]
XResizeRequestEvent = struct_anon_55

class struct_anon_56(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'parent', 
     'window', 
     'x', 
     'y', 
     'width', 
     'height', 
     'border_width', 
     'above', 
     'detail', 
     'value_mask']


struct_anon_56._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'parent', Window),
 (
  'window', Window),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'border_width', c_int),
 (
  'above', Window),
 (
  'detail', c_int),
 (
  'value_mask', c_ulong)]
XConfigureRequestEvent = struct_anon_56

class struct_anon_57(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'event', 
     'window', 
     'place']


struct_anon_57._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'event', Window),
 (
  'window', Window),
 (
  'place', c_int)]
XCirculateEvent = struct_anon_57

class struct_anon_58(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'parent', 
     'window', 
     'place']


struct_anon_58._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'parent', Window),
 (
  'window', Window),
 (
  'place', c_int)]
XCirculateRequestEvent = struct_anon_58

class struct_anon_59(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'atom', 
     'time', 
     'state']


struct_anon_59._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'atom', Atom),
 (
  'time', Time),
 (
  'state', c_int)]
XPropertyEvent = struct_anon_59

class struct_anon_60(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'selection', 
     'time']


struct_anon_60._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'selection', Atom),
 (
  'time', Time)]
XSelectionClearEvent = struct_anon_60

class struct_anon_61(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'owner', 
     'requestor', 
     'selection', 
     'target', 
     'property', 
     'time']


struct_anon_61._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'owner', Window),
 (
  'requestor', Window),
 (
  'selection', Atom),
 (
  'target', Atom),
 (
  'property', Atom),
 (
  'time', Time)]
XSelectionRequestEvent = struct_anon_61

class struct_anon_62(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'requestor', 
     'selection', 
     'target', 
     'property', 
     'time']


struct_anon_62._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'requestor', Window),
 (
  'selection', Atom),
 (
  'target', Atom),
 (
  'property', Atom),
 (
  'time', Time)]
XSelectionEvent = struct_anon_62

class struct_anon_63(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'colormap', 
     'new', 
     'state']


struct_anon_63._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'colormap', Colormap),
 (
  'new', c_int),
 (
  'state', c_int)]
XColormapEvent = struct_anon_63

class struct_anon_64(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'message_type', 
     'format', 
     'data']


class struct_anon_65(Union):
    __slots__ = [
     'b',
     's',
     'l']


struct_anon_65._fields_ = [
 (
  'b', c_char * 20),
 (
  's', c_short * 10),
 (
  'l', c_long * 5)]
struct_anon_64._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'message_type', Atom),
 (
  'format', c_int),
 (
  'data', struct_anon_65)]
XClientMessageEvent = struct_anon_64

class struct_anon_66(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window', 
     'request', 
     'first_keycode', 
     'count']


struct_anon_66._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window),
 (
  'request', c_int),
 (
  'first_keycode', c_int),
 (
  'count', c_int)]
XMappingEvent = struct_anon_66

class struct_anon_67(Structure):
    __slots__ = [
     'type', 
     'display', 
     'resourceid', 
     'serial', 
     'error_code', 
     'request_code', 
     'minor_code']


struct_anon_67._fields_ = [
 (
  'type', c_int),
 (
  'display', POINTER(Display)),
 (
  'resourceid', XID),
 (
  'serial', c_ulong),
 (
  'error_code', c_ubyte),
 (
  'request_code', c_ubyte),
 (
  'minor_code', c_ubyte)]
XErrorEvent = struct_anon_67

class struct_anon_68(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'window']


struct_anon_68._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'window', Window)]
XAnyEvent = struct_anon_68

class struct_anon_69(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'extension', 
     'evtype']


struct_anon_69._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'extension', c_int),
 (
  'evtype', c_int)]
XGenericEvent = struct_anon_69

class struct_anon_70(Structure):
    __slots__ = [
     'type', 
     'serial', 
     'send_event', 
     'display', 
     'extension', 
     'evtype', 
     'cookie', 
     'data']


struct_anon_70._fields_ = [
 (
  'type', c_int),
 (
  'serial', c_ulong),
 (
  'send_event', c_int),
 (
  'display', POINTER(Display)),
 (
  'extension', c_int),
 (
  'evtype', c_int),
 (
  'cookie', c_uint),
 (
  'data', POINTER(None))]
XGenericEventCookie = struct_anon_70

class struct__XEvent(Union):
    __slots__ = [
     'type', 
     'xany', 
     'xkey', 
     'xbutton', 
     'xmotion', 
     'xcrossing', 
     'xfocus', 
     'xexpose', 
     'xgraphicsexpose', 
     'xnoexpose', 
     'xvisibility', 
     'xcreatewindow', 
     'xdestroywindow', 
     'xunmap', 
     'xmap', 
     'xmaprequest', 
     'xreparent', 
     'xconfigure', 
     'xgravity', 
     'xresizerequest', 
     'xconfigurerequest', 
     'xcirculate', 
     'xcirculaterequest', 
     'xproperty', 
     'xselectionclear', 
     'xselectionrequest', 
     'xselection', 
     'xcolormap', 
     'xclient', 
     'xmapping', 
     'xerror', 
     'xkeymap', 
     'xgeneric', 
     'xcookie', 
     'pad']


struct__XEvent._fields_ = [
 (
  'type', c_int),
 (
  'xany', XAnyEvent),
 (
  'xkey', XKeyEvent),
 (
  'xbutton', XButtonEvent),
 (
  'xmotion', XMotionEvent),
 (
  'xcrossing', XCrossingEvent),
 (
  'xfocus', XFocusChangeEvent),
 (
  'xexpose', XExposeEvent),
 (
  'xgraphicsexpose', XGraphicsExposeEvent),
 (
  'xnoexpose', XNoExposeEvent),
 (
  'xvisibility', XVisibilityEvent),
 (
  'xcreatewindow', XCreateWindowEvent),
 (
  'xdestroywindow', XDestroyWindowEvent),
 (
  'xunmap', XUnmapEvent),
 (
  'xmap', XMapEvent),
 (
  'xmaprequest', XMapRequestEvent),
 (
  'xreparent', XReparentEvent),
 (
  'xconfigure', XConfigureEvent),
 (
  'xgravity', XGravityEvent),
 (
  'xresizerequest', XResizeRequestEvent),
 (
  'xconfigurerequest', XConfigureRequestEvent),
 (
  'xcirculate', XCirculateEvent),
 (
  'xcirculaterequest', XCirculateRequestEvent),
 (
  'xproperty', XPropertyEvent),
 (
  'xselectionclear', XSelectionClearEvent),
 (
  'xselectionrequest', XSelectionRequestEvent),
 (
  'xselection', XSelectionEvent),
 (
  'xcolormap', XColormapEvent),
 (
  'xclient', XClientMessageEvent),
 (
  'xmapping', XMappingEvent),
 (
  'xerror', XErrorEvent),
 (
  'xkeymap', XKeymapEvent),
 (
  'xgeneric', XGenericEvent),
 (
  'xcookie', XGenericEventCookie),
 (
  'pad', c_long * 24)]
XEvent = struct__XEvent

class struct_anon_71(Structure):
    __slots__ = [
     'lbearing', 
     'rbearing', 
     'width', 
     'ascent', 
     'descent', 
     'attributes']


struct_anon_71._fields_ = [
 (
  'lbearing', c_short),
 (
  'rbearing', c_short),
 (
  'width', c_short),
 (
  'ascent', c_short),
 (
  'descent', c_short),
 (
  'attributes', c_ushort)]
XCharStruct = struct_anon_71

class struct_anon_72(Structure):
    __slots__ = [
     'name',
     'card32']


struct_anon_72._fields_ = [
 (
  'name', Atom),
 (
  'card32', c_ulong)]
XFontProp = struct_anon_72

class struct_anon_73(Structure):
    __slots__ = [
     'ext_data', 
     'fid', 
     'direction', 
     'min_char_or_byte2', 
     'max_char_or_byte2', 
     'min_byte1', 
     'max_byte1', 
     'all_chars_exist', 
     'default_char', 
     'n_properties', 
     'properties', 
     'min_bounds', 
     'max_bounds', 
     'per_char', 
     'ascent', 
     'descent']


struct_anon_73._fields_ = [
 (
  'ext_data', POINTER(XExtData)),
 (
  'fid', Font),
 (
  'direction', c_uint),
 (
  'min_char_or_byte2', c_uint),
 (
  'max_char_or_byte2', c_uint),
 (
  'min_byte1', c_uint),
 (
  'max_byte1', c_uint),
 (
  'all_chars_exist', c_int),
 (
  'default_char', c_uint),
 (
  'n_properties', c_int),
 (
  'properties', POINTER(XFontProp)),
 (
  'min_bounds', XCharStruct),
 (
  'max_bounds', XCharStruct),
 (
  'per_char', POINTER(XCharStruct)),
 (
  'ascent', c_int),
 (
  'descent', c_int)]
XFontStruct = struct_anon_73

class struct_anon_74(Structure):
    __slots__ = [
     'chars',
     'nchars',
     'delta',
     'font']


struct_anon_74._fields_ = [
 (
  'chars', c_char_p),
 (
  'nchars', c_int),
 (
  'delta', c_int),
 (
  'font', Font)]
XTextItem = struct_anon_74

class struct_anon_75(Structure):
    __slots__ = [
     'byte1',
     'byte2']


struct_anon_75._fields_ = [
 (
  'byte1', c_ubyte),
 (
  'byte2', c_ubyte)]
XChar2b = struct_anon_75

class struct_anon_76(Structure):
    __slots__ = [
     'chars',
     'nchars',
     'delta',
     'font']


struct_anon_76._fields_ = [
 (
  'chars', POINTER(XChar2b)),
 (
  'nchars', c_int),
 (
  'delta', c_int),
 (
  'font', Font)]
XTextItem16 = struct_anon_76

class struct_anon_77(Union):
    __slots__ = [
     'display', 
     'gc', 
     'visual', 
     'screen', 
     'pixmap_format', 
     'font']


struct_anon_77._fields_ = [
 (
  'display', POINTER(Display)),
 (
  'gc', GC),
 (
  'visual', POINTER(Visual)),
 (
  'screen', POINTER(Screen)),
 (
  'pixmap_format', POINTER(ScreenFormat)),
 (
  'font', POINTER(XFontStruct))]
XEDataObject = struct_anon_77

class struct_anon_78(Structure):
    __slots__ = [
     'max_ink_extent',
     'max_logical_extent']


struct_anon_78._fields_ = [
 (
  'max_ink_extent', XRectangle),
 (
  'max_logical_extent', XRectangle)]
XFontSetExtents = struct_anon_78

class struct__XOM(Structure):
    __slots__ = []


struct__XOM._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XOM(Structure):
    __slots__ = []


struct__XOM._fields_ = [
 (
  '_opaque_struct', c_int)]
XOM = POINTER(struct__XOM)

class struct__XOC(Structure):
    __slots__ = []


struct__XOC._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XOC(Structure):
    __slots__ = []


struct__XOC._fields_ = [
 (
  '_opaque_struct', c_int)]
XOC = POINTER(struct__XOC)

class struct__XOC(Structure):
    __slots__ = []


struct__XOC._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XOC(Structure):
    __slots__ = []


struct__XOC._fields_ = [
 (
  '_opaque_struct', c_int)]
XFontSet = POINTER(struct__XOC)

class struct_anon_79(Structure):
    __slots__ = [
     'chars',
     'nchars',
     'delta',
     'font_set']


struct_anon_79._fields_ = [
 (
  'chars', c_char_p),
 (
  'nchars', c_int),
 (
  'delta', c_int),
 (
  'font_set', XFontSet)]
XmbTextItem = struct_anon_79

class struct_anon_80(Structure):
    __slots__ = [
     'chars',
     'nchars',
     'delta',
     'font_set']


struct_anon_80._fields_ = [
 (
  'chars', c_wchar_p),
 (
  'nchars', c_int),
 (
  'delta', c_int),
 (
  'font_set', XFontSet)]
XwcTextItem = struct_anon_80

class struct_anon_81(Structure):
    __slots__ = [
     'charset_count',
     'charset_list']


struct_anon_81._fields_ = [
 (
  'charset_count', c_int),
 (
  'charset_list', POINTER(c_char_p))]
XOMCharSetList = struct_anon_81
enum_anon_82 = c_int
XOMOrientation_LTR_TTB = 0
XOMOrientation_RTL_TTB = 1
XOMOrientation_TTB_LTR = 2
XOMOrientation_TTB_RTL = 3
XOMOrientation_Context = 4
XOrientation = enum_anon_82

class struct_anon_83(Structure):
    __slots__ = [
     'num_orientation',
     'orientation']


struct_anon_83._fields_ = [
 (
  'num_orientation', c_int),
 (
  'orientation', POINTER(XOrientation))]
XOMOrientation = struct_anon_83

class struct_anon_84(Structure):
    __slots__ = [
     'num_font',
     'font_struct_list',
     'font_name_list']


struct_anon_84._fields_ = [
 (
  'num_font', c_int),
 (
  'font_struct_list', POINTER(POINTER(XFontStruct))),
 (
  'font_name_list', POINTER(c_char_p))]
XOMFontInfo = struct_anon_84

class struct__XIM(Structure):
    __slots__ = []


struct__XIM._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XIM(Structure):
    __slots__ = []


struct__XIM._fields_ = [
 (
  '_opaque_struct', c_int)]
XIM = POINTER(struct__XIM)

class struct__XIC(Structure):
    __slots__ = []


struct__XIC._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XIC(Structure):
    __slots__ = []


struct__XIC._fields_ = [
 (
  '_opaque_struct', c_int)]
XIC = POINTER(struct__XIC)
XIMProc = CFUNCTYPE(None, XIM, XPointer, XPointer)
XICProc = CFUNCTYPE(c_int, XIC, XPointer, XPointer)
XIDProc = CFUNCTYPE(None, POINTER(Display), XPointer, XPointer)
XIMStyle = c_ulong

class struct_anon_85(Structure):
    __slots__ = [
     'count_styles',
     'supported_styles']


struct_anon_85._fields_ = [
 (
  'count_styles', c_ushort),
 (
  'supported_styles', POINTER(XIMStyle))]
XIMStyles = struct_anon_85
XIMPreeditArea = 1
XIMPreeditCallbacks = 2
XIMPreeditPosition = 4
XIMPreeditNothing = 8
XIMPreeditNone = 16
XIMStatusArea = 256
XIMStatusCallbacks = 512
XIMStatusNothing = 1024
XIMStatusNone = 2048
XBufferOverflow = -1
XLookupNone = 1
XLookupChars = 2
XLookupKeySym = 3
XLookupBoth = 4
XVaNestedList = POINTER(None)

class struct_anon_86(Structure):
    __slots__ = [
     'client_data',
     'callback']


struct_anon_86._fields_ = [
 (
  'client_data', XPointer),
 (
  'callback', XIMProc)]
XIMCallback = struct_anon_86

class struct_anon_87(Structure):
    __slots__ = [
     'client_data',
     'callback']


struct_anon_87._fields_ = [
 (
  'client_data', XPointer),
 (
  'callback', XICProc)]
XICCallback = struct_anon_87
XIMFeedback = c_ulong
XIMReverse = 1
XIMUnderline = 2
XIMHighlight = 4
XIMPrimary = 32
XIMSecondary = 64
XIMTertiary = 128
XIMVisibleToForward = 256
XIMVisibleToBackword = 512
XIMVisibleToCenter = 1024

class struct__XIMText(Structure):
    __slots__ = [
     'length',
     'feedback',
     'encoding_is_wchar',
     'string']


class struct_anon_88(Union):
    __slots__ = [
     'multi_byte',
     'wide_char']


struct_anon_88._fields_ = [
 (
  'multi_byte', c_char_p),
 (
  'wide_char', c_wchar_p)]
struct__XIMText._fields_ = [
 (
  'length', c_ushort),
 (
  'feedback', POINTER(XIMFeedback)),
 (
  'encoding_is_wchar', c_int),
 (
  'string', struct_anon_88)]
XIMText = struct__XIMText
XIMPreeditState = c_ulong
XIMPreeditUnKnown = 0
XIMPreeditEnable = 1
XIMPreeditDisable = 2

class struct__XIMPreeditStateNotifyCallbackStruct(Structure):
    __slots__ = [
     'state']


struct__XIMPreeditStateNotifyCallbackStruct._fields_ = [
 (
  'state', XIMPreeditState)]
XIMPreeditStateNotifyCallbackStruct = struct__XIMPreeditStateNotifyCallbackStruct
XIMResetState = c_ulong
XIMInitialState = 1
XIMPreserveState = 2
XIMStringConversionFeedback = c_ulong
XIMStringConversionLeftEdge = 1
XIMStringConversionRightEdge = 2
XIMStringConversionTopEdge = 4
XIMStringConversionBottomEdge = 8
XIMStringConversionConcealed = 16
XIMStringConversionWrapped = 32

class struct__XIMStringConversionText(Structure):
    __slots__ = [
     'length',
     'feedback',
     'encoding_is_wchar',
     'string']


class struct_anon_89(Union):
    __slots__ = [
     'mbs',
     'wcs']


struct_anon_89._fields_ = [
 (
  'mbs', c_char_p),
 (
  'wcs', c_wchar_p)]
struct__XIMStringConversionText._fields_ = [
 (
  'length', c_ushort),
 (
  'feedback', POINTER(XIMStringConversionFeedback)),
 (
  'encoding_is_wchar', c_int),
 (
  'string', struct_anon_89)]
XIMStringConversionText = struct__XIMStringConversionText
XIMStringConversionPosition = c_ushort
XIMStringConversionType = c_ushort
XIMStringConversionBuffer = 1
XIMStringConversionLine = 2
XIMStringConversionWord = 3
XIMStringConversionChar = 4
XIMStringConversionOperation = c_ushort
XIMStringConversionSubstitution = 1
XIMStringConversionRetrieval = 2
enum_anon_90 = c_int
XIMForwardChar = 0
XIMBackwardChar = 1
XIMForwardWord = 2
XIMBackwardWord = 3
XIMCaretUp = 4
XIMCaretDown = 5
XIMNextLine = 6
XIMPreviousLine = 7
XIMLineStart = 8
XIMLineEnd = 9
XIMAbsolutePosition = 10
XIMDontChange = 11
XIMCaretDirection = enum_anon_90

class struct__XIMStringConversionCallbackStruct(Structure):
    __slots__ = [
     'position', 
     'direction', 
     'operation', 
     'factor', 
     'text']


struct__XIMStringConversionCallbackStruct._fields_ = [
 (
  'position', XIMStringConversionPosition),
 (
  'direction', XIMCaretDirection),
 (
  'operation', XIMStringConversionOperation),
 (
  'factor', c_ushort),
 (
  'text', POINTER(XIMStringConversionText))]
XIMStringConversionCallbackStruct = struct__XIMStringConversionCallbackStruct

class struct__XIMPreeditDrawCallbackStruct(Structure):
    __slots__ = [
     'caret',
     'chg_first',
     'chg_length',
     'text']


struct__XIMPreeditDrawCallbackStruct._fields_ = [
 (
  'caret', c_int),
 (
  'chg_first', c_int),
 (
  'chg_length', c_int),
 (
  'text', POINTER(XIMText))]
XIMPreeditDrawCallbackStruct = struct__XIMPreeditDrawCallbackStruct
enum_anon_91 = c_int
XIMIsInvisible = 0
XIMIsPrimary = 1
XIMIsSecondary = 2
XIMCaretStyle = enum_anon_91

class struct__XIMPreeditCaretCallbackStruct(Structure):
    __slots__ = [
     'position',
     'direction',
     'style']


struct__XIMPreeditCaretCallbackStruct._fields_ = [
 (
  'position', c_int),
 (
  'direction', XIMCaretDirection),
 (
  'style', XIMCaretStyle)]
XIMPreeditCaretCallbackStruct = struct__XIMPreeditCaretCallbackStruct
enum_anon_92 = c_int
XIMTextType = 0
XIMBitmapType = 1
XIMStatusDataType = enum_anon_92

class struct__XIMStatusDrawCallbackStruct(Structure):
    __slots__ = [
     'type',
     'data']


class struct_anon_93(Union):
    __slots__ = [
     'text',
     'bitmap']


struct_anon_93._fields_ = [
 (
  'text', POINTER(XIMText)),
 (
  'bitmap', Pixmap)]
struct__XIMStatusDrawCallbackStruct._fields_ = [
 (
  'type', XIMStatusDataType),
 (
  'data', struct_anon_93)]
XIMStatusDrawCallbackStruct = struct__XIMStatusDrawCallbackStruct

class struct__XIMHotKeyTrigger(Structure):
    __slots__ = [
     'keysym',
     'modifier',
     'modifier_mask']


struct__XIMHotKeyTrigger._fields_ = [
 (
  'keysym', KeySym),
 (
  'modifier', c_int),
 (
  'modifier_mask', c_int)]
XIMHotKeyTrigger = struct__XIMHotKeyTrigger

class struct__XIMHotKeyTriggers(Structure):
    __slots__ = [
     'num_hot_key',
     'key']


struct__XIMHotKeyTriggers._fields_ = [
 (
  'num_hot_key', c_int),
 (
  'key', POINTER(XIMHotKeyTrigger))]
XIMHotKeyTriggers = struct__XIMHotKeyTriggers
XIMHotKeyState = c_ulong
XIMHotKeyStateON = 1
XIMHotKeyStateOFF = 2

class struct_anon_94(Structure):
    __slots__ = [
     'count_values',
     'supported_values']


struct_anon_94._fields_ = [
 (
  'count_values', c_ushort),
 (
  'supported_values', POINTER(c_char_p))]
XIMValuesList = struct_anon_94
XLoadQueryFont = _lib.XLoadQueryFont
XLoadQueryFont.restype = POINTER(XFontStruct)
XLoadQueryFont.argtypes = [POINTER(Display), c_char_p]
XQueryFont = _lib.XQueryFont
XQueryFont.restype = POINTER(XFontStruct)
XQueryFont.argtypes = [POINTER(Display), XID]
XGetMotionEvents = _lib.XGetMotionEvents
XGetMotionEvents.restype = POINTER(XTimeCoord)
XGetMotionEvents.argtypes = [POINTER(Display), Window, Time, Time, POINTER(c_int)]
XDeleteModifiermapEntry = _lib.XDeleteModifiermapEntry
XDeleteModifiermapEntry.restype = POINTER(XModifierKeymap)
XDeleteModifiermapEntry.argtypes = [POINTER(XModifierKeymap), KeyCode, c_int]
XGetModifierMapping = _lib.XGetModifierMapping
XGetModifierMapping.restype = POINTER(XModifierKeymap)
XGetModifierMapping.argtypes = [POINTER(Display)]
XInsertModifiermapEntry = _lib.XInsertModifiermapEntry
XInsertModifiermapEntry.restype = POINTER(XModifierKeymap)
XInsertModifiermapEntry.argtypes = [POINTER(XModifierKeymap), KeyCode, c_int]
XNewModifiermap = _lib.XNewModifiermap
XNewModifiermap.restype = POINTER(XModifierKeymap)
XNewModifiermap.argtypes = [c_int]
XCreateImage = _lib.XCreateImage
XCreateImage.restype = POINTER(XImage)
XCreateImage.argtypes = [POINTER(Display), POINTER(Visual), c_uint, c_int, c_int, c_char_p, c_uint, c_uint, c_int, c_int]
XInitImage = _lib.XInitImage
XInitImage.restype = c_int
XInitImage.argtypes = [POINTER(XImage)]
XGetImage = _lib.XGetImage
XGetImage.restype = POINTER(XImage)
XGetImage.argtypes = [POINTER(Display), Drawable, c_int, c_int, c_uint, c_uint, c_ulong, c_int]
XGetSubImage = _lib.XGetSubImage
XGetSubImage.restype = POINTER(XImage)
XGetSubImage.argtypes = [POINTER(Display), Drawable, c_int, c_int, c_uint, c_uint, c_ulong, c_int, POINTER(XImage), c_int, c_int]
XOpenDisplay = _lib.XOpenDisplay
XOpenDisplay.restype = POINTER(Display)
XOpenDisplay.argtypes = [c_char_p]
XrmInitialize = _lib.XrmInitialize
XrmInitialize.restype = None
XrmInitialize.argtypes = []
XFetchBytes = _lib.XFetchBytes
XFetchBytes.restype = c_char_p
XFetchBytes.argtypes = [POINTER(Display), POINTER(c_int)]
XFetchBuffer = _lib.XFetchBuffer
XFetchBuffer.restype = c_char_p
XFetchBuffer.argtypes = [POINTER(Display), POINTER(c_int), c_int]
XGetAtomName = _lib.XGetAtomName
XGetAtomName.restype = c_char_p
XGetAtomName.argtypes = [POINTER(Display), Atom]
XGetAtomNames = _lib.XGetAtomNames
XGetAtomNames.restype = c_int
XGetAtomNames.argtypes = [POINTER(Display), POINTER(Atom), c_int, POINTER(c_char_p)]
XGetDefault = _lib.XGetDefault
XGetDefault.restype = c_char_p
XGetDefault.argtypes = [POINTER(Display), c_char_p, c_char_p]
XDisplayName = _lib.XDisplayName
XDisplayName.restype = c_char_p
XDisplayName.argtypes = [c_char_p]
XKeysymToString = _lib.XKeysymToString
XKeysymToString.restype = c_char_p
XKeysymToString.argtypes = [KeySym]
XSynchronize = _lib.XSynchronize
XSynchronize.restype = POINTER(CFUNCTYPE(c_int, POINTER(Display)))
XSynchronize.argtypes = [POINTER(Display), c_int]
XSetAfterFunction = _lib.XSetAfterFunction
XSetAfterFunction.restype = POINTER(CFUNCTYPE(c_int, POINTER(Display)))
XSetAfterFunction.argtypes = [POINTER(Display), CFUNCTYPE(c_int, POINTER(Display))]
XInternAtom = _lib.XInternAtom
XInternAtom.restype = Atom
XInternAtom.argtypes = [POINTER(Display), c_char_p, c_int]
XInternAtoms = _lib.XInternAtoms
XInternAtoms.restype = c_int
XInternAtoms.argtypes = [POINTER(Display), POINTER(c_char_p), c_int, c_int, POINTER(Atom)]
XCopyColormapAndFree = _lib.XCopyColormapAndFree
XCopyColormapAndFree.restype = Colormap
XCopyColormapAndFree.argtypes = [POINTER(Display), Colormap]
XCreateColormap = _lib.XCreateColormap
XCreateColormap.restype = Colormap
XCreateColormap.argtypes = [POINTER(Display), Window, POINTER(Visual), c_int]
XCreatePixmapCursor = _lib.XCreatePixmapCursor
XCreatePixmapCursor.restype = Cursor
XCreatePixmapCursor.argtypes = [POINTER(Display), Pixmap, Pixmap, POINTER(XColor), POINTER(XColor), c_uint, c_uint]
XCreateGlyphCursor = _lib.XCreateGlyphCursor
XCreateGlyphCursor.restype = Cursor
XCreateGlyphCursor.argtypes = [POINTER(Display), Font, Font, c_uint, c_uint, POINTER(XColor), POINTER(XColor)]
XCreateFontCursor = _lib.XCreateFontCursor
XCreateFontCursor.restype = Cursor
XCreateFontCursor.argtypes = [POINTER(Display), c_uint]
XLoadFont = _lib.XLoadFont
XLoadFont.restype = Font
XLoadFont.argtypes = [POINTER(Display), c_char_p]
XCreateGC = _lib.XCreateGC
XCreateGC.restype = GC
XCreateGC.argtypes = [POINTER(Display), Drawable, c_ulong, POINTER(XGCValues)]
XGContextFromGC = _lib.XGContextFromGC
XGContextFromGC.restype = GContext
XGContextFromGC.argtypes = [GC]
XFlushGC = _lib.XFlushGC
XFlushGC.restype = None
XFlushGC.argtypes = [POINTER(Display), GC]
XCreatePixmap = _lib.XCreatePixmap
XCreatePixmap.restype = Pixmap
XCreatePixmap.argtypes = [POINTER(Display), Drawable, c_uint, c_uint, c_uint]
XCreateBitmapFromData = _lib.XCreateBitmapFromData
XCreateBitmapFromData.restype = Pixmap
XCreateBitmapFromData.argtypes = [POINTER(Display), Drawable, c_char_p, c_uint, c_uint]
XCreatePixmapFromBitmapData = _lib.XCreatePixmapFromBitmapData
XCreatePixmapFromBitmapData.restype = Pixmap
XCreatePixmapFromBitmapData.argtypes = [POINTER(Display), Drawable, c_char_p, c_uint, c_uint, c_ulong, c_ulong, c_uint]
XCreateSimpleWindow = _lib.XCreateSimpleWindow
XCreateSimpleWindow.restype = Window
XCreateSimpleWindow.argtypes = [POINTER(Display), Window, c_int, c_int, c_uint, c_uint, c_uint, c_ulong, c_ulong]
XGetSelectionOwner = _lib.XGetSelectionOwner
XGetSelectionOwner.restype = Window
XGetSelectionOwner.argtypes = [POINTER(Display), Atom]
XCreateWindow = _lib.XCreateWindow
XCreateWindow.restype = Window
XCreateWindow.argtypes = [POINTER(Display), Window, c_int, c_int, c_uint, c_uint, c_uint, c_int, c_uint, POINTER(Visual), c_ulong, POINTER(XSetWindowAttributes)]
XListInstalledColormaps = _lib.XListInstalledColormaps
XListInstalledColormaps.restype = POINTER(Colormap)
XListInstalledColormaps.argtypes = [POINTER(Display), Window, POINTER(c_int)]
XListFonts = _lib.XListFonts
XListFonts.restype = POINTER(c_char_p)
XListFonts.argtypes = [POINTER(Display), c_char_p, c_int, POINTER(c_int)]
XListFontsWithInfo = _lib.XListFontsWithInfo
XListFontsWithInfo.restype = POINTER(c_char_p)
XListFontsWithInfo.argtypes = [POINTER(Display), c_char_p, c_int, POINTER(c_int), POINTER(POINTER(XFontStruct))]
XGetFontPath = _lib.XGetFontPath
XGetFontPath.restype = POINTER(c_char_p)
XGetFontPath.argtypes = [POINTER(Display), POINTER(c_int)]
XListExtensions = _lib.XListExtensions
XListExtensions.restype = POINTER(c_char_p)
XListExtensions.argtypes = [POINTER(Display), POINTER(c_int)]
XListProperties = _lib.XListProperties
XListProperties.restype = POINTER(Atom)
XListProperties.argtypes = [POINTER(Display), Window, POINTER(c_int)]
XListHosts = _lib.XListHosts
XListHosts.restype = POINTER(XHostAddress)
XListHosts.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XKeycodeToKeysym = _lib.XKeycodeToKeysym
XKeycodeToKeysym.restype = KeySym
XKeycodeToKeysym.argtypes = [POINTER(Display), KeyCode, c_int]
XLookupKeysym = _lib.XLookupKeysym
XLookupKeysym.restype = KeySym
XLookupKeysym.argtypes = [POINTER(XKeyEvent), c_int]
XGetKeyboardMapping = _lib.XGetKeyboardMapping
XGetKeyboardMapping.restype = POINTER(KeySym)
XGetKeyboardMapping.argtypes = [POINTER(Display), KeyCode, c_int, POINTER(c_int)]
XStringToKeysym = _lib.XStringToKeysym
XStringToKeysym.restype = KeySym
XStringToKeysym.argtypes = [c_char_p]
XMaxRequestSize = _lib.XMaxRequestSize
XMaxRequestSize.restype = c_long
XMaxRequestSize.argtypes = [POINTER(Display)]
XExtendedMaxRequestSize = _lib.XExtendedMaxRequestSize
XExtendedMaxRequestSize.restype = c_long
XExtendedMaxRequestSize.argtypes = [POINTER(Display)]
XResourceManagerString = _lib.XResourceManagerString
XResourceManagerString.restype = c_char_p
XResourceManagerString.argtypes = [POINTER(Display)]
XScreenResourceString = _lib.XScreenResourceString
XScreenResourceString.restype = c_char_p
XScreenResourceString.argtypes = [POINTER(Screen)]
XDisplayMotionBufferSize = _lib.XDisplayMotionBufferSize
XDisplayMotionBufferSize.restype = c_ulong
XDisplayMotionBufferSize.argtypes = [POINTER(Display)]
XVisualIDFromVisual = _lib.XVisualIDFromVisual
XVisualIDFromVisual.restype = VisualID
XVisualIDFromVisual.argtypes = [POINTER(Visual)]
XInitThreads = _lib.XInitThreads
XInitThreads.restype = c_int
XInitThreads.argtypes = []
XLockDisplay = _lib.XLockDisplay
XLockDisplay.restype = None
XLockDisplay.argtypes = [POINTER(Display)]
XUnlockDisplay = _lib.XUnlockDisplay
XUnlockDisplay.restype = None
XUnlockDisplay.argtypes = [POINTER(Display)]
XInitExtension = _lib.XInitExtension
XInitExtension.restype = POINTER(XExtCodes)
XInitExtension.argtypes = [POINTER(Display), c_char_p]
XAddExtension = _lib.XAddExtension
XAddExtension.restype = POINTER(XExtCodes)
XAddExtension.argtypes = [POINTER(Display)]
XFindOnExtensionList = _lib.XFindOnExtensionList
XFindOnExtensionList.restype = POINTER(XExtData)
XFindOnExtensionList.argtypes = [POINTER(POINTER(XExtData)), c_int]
XEHeadOfExtensionList = _lib.XEHeadOfExtensionList
XEHeadOfExtensionList.restype = POINTER(POINTER(XExtData))
XEHeadOfExtensionList.argtypes = [XEDataObject]
XRootWindow = _lib.XRootWindow
XRootWindow.restype = Window
XRootWindow.argtypes = [POINTER(Display), c_int]
XDefaultRootWindow = _lib.XDefaultRootWindow
XDefaultRootWindow.restype = Window
XDefaultRootWindow.argtypes = [POINTER(Display)]
XRootWindowOfScreen = _lib.XRootWindowOfScreen
XRootWindowOfScreen.restype = Window
XRootWindowOfScreen.argtypes = [POINTER(Screen)]
XDefaultVisual = _lib.XDefaultVisual
XDefaultVisual.restype = POINTER(Visual)
XDefaultVisual.argtypes = [POINTER(Display), c_int]
XDefaultVisualOfScreen = _lib.XDefaultVisualOfScreen
XDefaultVisualOfScreen.restype = POINTER(Visual)
XDefaultVisualOfScreen.argtypes = [POINTER(Screen)]
XDefaultGC = _lib.XDefaultGC
XDefaultGC.restype = GC
XDefaultGC.argtypes = [POINTER(Display), c_int]
XDefaultGCOfScreen = _lib.XDefaultGCOfScreen
XDefaultGCOfScreen.restype = GC
XDefaultGCOfScreen.argtypes = [POINTER(Screen)]
XBlackPixel = _lib.XBlackPixel
XBlackPixel.restype = c_ulong
XBlackPixel.argtypes = [POINTER(Display), c_int]
XWhitePixel = _lib.XWhitePixel
XWhitePixel.restype = c_ulong
XWhitePixel.argtypes = [POINTER(Display), c_int]
XAllPlanes = _lib.XAllPlanes
XAllPlanes.restype = c_ulong
XAllPlanes.argtypes = []
XBlackPixelOfScreen = _lib.XBlackPixelOfScreen
XBlackPixelOfScreen.restype = c_ulong
XBlackPixelOfScreen.argtypes = [POINTER(Screen)]
XWhitePixelOfScreen = _lib.XWhitePixelOfScreen
XWhitePixelOfScreen.restype = c_ulong
XWhitePixelOfScreen.argtypes = [POINTER(Screen)]
XNextRequest = _lib.XNextRequest
XNextRequest.restype = c_ulong
XNextRequest.argtypes = [POINTER(Display)]
XLastKnownRequestProcessed = _lib.XLastKnownRequestProcessed
XLastKnownRequestProcessed.restype = c_ulong
XLastKnownRequestProcessed.argtypes = [POINTER(Display)]
XServerVendor = _lib.XServerVendor
XServerVendor.restype = c_char_p
XServerVendor.argtypes = [POINTER(Display)]
XDisplayString = _lib.XDisplayString
XDisplayString.restype = c_char_p
XDisplayString.argtypes = [POINTER(Display)]
XDefaultColormap = _lib.XDefaultColormap
XDefaultColormap.restype = Colormap
XDefaultColormap.argtypes = [POINTER(Display), c_int]
XDefaultColormapOfScreen = _lib.XDefaultColormapOfScreen
XDefaultColormapOfScreen.restype = Colormap
XDefaultColormapOfScreen.argtypes = [POINTER(Screen)]
XDisplayOfScreen = _lib.XDisplayOfScreen
XDisplayOfScreen.restype = POINTER(Display)
XDisplayOfScreen.argtypes = [POINTER(Screen)]
XScreenOfDisplay = _lib.XScreenOfDisplay
XScreenOfDisplay.restype = POINTER(Screen)
XScreenOfDisplay.argtypes = [POINTER(Display), c_int]
XDefaultScreenOfDisplay = _lib.XDefaultScreenOfDisplay
XDefaultScreenOfDisplay.restype = POINTER(Screen)
XDefaultScreenOfDisplay.argtypes = [POINTER(Display)]
XEventMaskOfScreen = _lib.XEventMaskOfScreen
XEventMaskOfScreen.restype = c_long
XEventMaskOfScreen.argtypes = [POINTER(Screen)]
XScreenNumberOfScreen = _lib.XScreenNumberOfScreen
XScreenNumberOfScreen.restype = c_int
XScreenNumberOfScreen.argtypes = [POINTER(Screen)]
XErrorHandler = CFUNCTYPE(c_int, POINTER(Display), POINTER(XErrorEvent))
XSetErrorHandler = _lib.XSetErrorHandler
XSetErrorHandler.restype = XErrorHandler
XSetErrorHandler.argtypes = [XErrorHandler]
XIOErrorHandler = CFUNCTYPE(c_int, POINTER(Display))
XSetIOErrorHandler = _lib.XSetIOErrorHandler
XSetIOErrorHandler.restype = XIOErrorHandler
XSetIOErrorHandler.argtypes = [XIOErrorHandler]
XListPixmapFormats = _lib.XListPixmapFormats
XListPixmapFormats.restype = POINTER(XPixmapFormatValues)
XListPixmapFormats.argtypes = [POINTER(Display), POINTER(c_int)]
XListDepths = _lib.XListDepths
XListDepths.restype = POINTER(c_int)
XListDepths.argtypes = [POINTER(Display), c_int, POINTER(c_int)]
XReconfigureWMWindow = _lib.XReconfigureWMWindow
XReconfigureWMWindow.restype = c_int
XReconfigureWMWindow.argtypes = [POINTER(Display), Window, c_int, c_uint, POINTER(XWindowChanges)]
XGetWMProtocols = _lib.XGetWMProtocols
XGetWMProtocols.restype = c_int
XGetWMProtocols.argtypes = [POINTER(Display), Window, POINTER(POINTER(Atom)), POINTER(c_int)]
XSetWMProtocols = _lib.XSetWMProtocols
XSetWMProtocols.restype = c_int
XSetWMProtocols.argtypes = [POINTER(Display), Window, POINTER(Atom), c_int]
XIconifyWindow = _lib.XIconifyWindow
XIconifyWindow.restype = c_int
XIconifyWindow.argtypes = [POINTER(Display), Window, c_int]
XWithdrawWindow = _lib.XWithdrawWindow
XWithdrawWindow.restype = c_int
XWithdrawWindow.argtypes = [POINTER(Display), Window, c_int]
XGetCommand = _lib.XGetCommand
XGetCommand.restype = c_int
XGetCommand.argtypes = [POINTER(Display), Window, POINTER(POINTER(c_char_p)), POINTER(c_int)]
XGetWMColormapWindows = _lib.XGetWMColormapWindows
XGetWMColormapWindows.restype = c_int
XGetWMColormapWindows.argtypes = [POINTER(Display), Window, POINTER(POINTER(Window)), POINTER(c_int)]
XSetWMColormapWindows = _lib.XSetWMColormapWindows
XSetWMColormapWindows.restype = c_int
XSetWMColormapWindows.argtypes = [POINTER(Display), Window, POINTER(Window), c_int]
XFreeStringList = _lib.XFreeStringList
XFreeStringList.restype = None
XFreeStringList.argtypes = [POINTER(c_char_p)]
XSetTransientForHint = _lib.XSetTransientForHint
XSetTransientForHint.restype = c_int
XSetTransientForHint.argtypes = [POINTER(Display), Window, Window]
XActivateScreenSaver = _lib.XActivateScreenSaver
XActivateScreenSaver.restype = c_int
XActivateScreenSaver.argtypes = [POINTER(Display)]
XAddHost = _lib.XAddHost
XAddHost.restype = c_int
XAddHost.argtypes = [POINTER(Display), POINTER(XHostAddress)]
XAddHosts = _lib.XAddHosts
XAddHosts.restype = c_int
XAddHosts.argtypes = [POINTER(Display), POINTER(XHostAddress), c_int]
XAddToExtensionList = _lib.XAddToExtensionList
XAddToExtensionList.restype = c_int
XAddToExtensionList.argtypes = [POINTER(POINTER(struct__XExtData)), POINTER(XExtData)]
XAddToSaveSet = _lib.XAddToSaveSet
XAddToSaveSet.restype = c_int
XAddToSaveSet.argtypes = [POINTER(Display), Window]
XAllocColor = _lib.XAllocColor
XAllocColor.restype = c_int
XAllocColor.argtypes = [POINTER(Display), Colormap, POINTER(XColor)]
XAllocColorCells = _lib.XAllocColorCells
XAllocColorCells.restype = c_int
XAllocColorCells.argtypes = [POINTER(Display), Colormap, c_int, POINTER(c_ulong), c_uint, POINTER(c_ulong), c_uint]
XAllocColorPlanes = _lib.XAllocColorPlanes
XAllocColorPlanes.restype = c_int
XAllocColorPlanes.argtypes = [POINTER(Display), Colormap, c_int, POINTER(c_ulong), c_int, c_int, c_int, c_int, POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong)]
XAllocNamedColor = _lib.XAllocNamedColor
XAllocNamedColor.restype = c_int
XAllocNamedColor.argtypes = [POINTER(Display), Colormap, c_char_p, POINTER(XColor), POINTER(XColor)]
XAllowEvents = _lib.XAllowEvents
XAllowEvents.restype = c_int
XAllowEvents.argtypes = [POINTER(Display), c_int, Time]
XAutoRepeatOff = _lib.XAutoRepeatOff
XAutoRepeatOff.restype = c_int
XAutoRepeatOff.argtypes = [POINTER(Display)]
XAutoRepeatOn = _lib.XAutoRepeatOn
XAutoRepeatOn.restype = c_int
XAutoRepeatOn.argtypes = [POINTER(Display)]
XBell = _lib.XBell
XBell.restype = c_int
XBell.argtypes = [POINTER(Display), c_int]
XBitmapBitOrder = _lib.XBitmapBitOrder
XBitmapBitOrder.restype = c_int
XBitmapBitOrder.argtypes = [POINTER(Display)]
XBitmapPad = _lib.XBitmapPad
XBitmapPad.restype = c_int
XBitmapPad.argtypes = [POINTER(Display)]
XBitmapUnit = _lib.XBitmapUnit
XBitmapUnit.restype = c_int
XBitmapUnit.argtypes = [POINTER(Display)]
XCellsOfScreen = _lib.XCellsOfScreen
XCellsOfScreen.restype = c_int
XCellsOfScreen.argtypes = [POINTER(Screen)]
XChangeActivePointerGrab = _lib.XChangeActivePointerGrab
XChangeActivePointerGrab.restype = c_int
XChangeActivePointerGrab.argtypes = [POINTER(Display), c_uint, Cursor, Time]
XChangeGC = _lib.XChangeGC
XChangeGC.restype = c_int
XChangeGC.argtypes = [POINTER(Display), GC, c_ulong, POINTER(XGCValues)]
XChangeKeyboardControl = _lib.XChangeKeyboardControl
XChangeKeyboardControl.restype = c_int
XChangeKeyboardControl.argtypes = [POINTER(Display), c_ulong, POINTER(XKeyboardControl)]
XChangeKeyboardMapping = _lib.XChangeKeyboardMapping
XChangeKeyboardMapping.restype = c_int
XChangeKeyboardMapping.argtypes = [POINTER(Display), c_int, c_int, POINTER(KeySym), c_int]
XChangePointerControl = _lib.XChangePointerControl
XChangePointerControl.restype = c_int
XChangePointerControl.argtypes = [POINTER(Display), c_int, c_int, c_int, c_int, c_int]
XChangeProperty = _lib.XChangeProperty
XChangeProperty.restype = c_int
XChangeProperty.argtypes = [POINTER(Display), Window, Atom, Atom, c_int, c_int, POINTER(c_ubyte), c_int]
XChangeSaveSet = _lib.XChangeSaveSet
XChangeSaveSet.restype = c_int
XChangeSaveSet.argtypes = [POINTER(Display), Window, c_int]
XChangeWindowAttributes = _lib.XChangeWindowAttributes
XChangeWindowAttributes.restype = c_int
XChangeWindowAttributes.argtypes = [POINTER(Display), Window, c_ulong, POINTER(XSetWindowAttributes)]
XCheckIfEvent = _lib.XCheckIfEvent
XCheckIfEvent.restype = c_int
XCheckIfEvent.argtypes = [POINTER(Display), POINTER(XEvent), CFUNCTYPE(c_int, POINTER(Display), POINTER(XEvent), XPointer), XPointer]
XCheckMaskEvent = _lib.XCheckMaskEvent
XCheckMaskEvent.restype = c_int
XCheckMaskEvent.argtypes = [POINTER(Display), c_long, POINTER(XEvent)]
XCheckTypedEvent = _lib.XCheckTypedEvent
XCheckTypedEvent.restype = c_int
XCheckTypedEvent.argtypes = [POINTER(Display), c_int, POINTER(XEvent)]
XCheckTypedWindowEvent = _lib.XCheckTypedWindowEvent
XCheckTypedWindowEvent.restype = c_int
XCheckTypedWindowEvent.argtypes = [POINTER(Display), Window, c_int, POINTER(XEvent)]
XCheckWindowEvent = _lib.XCheckWindowEvent
XCheckWindowEvent.restype = c_int
XCheckWindowEvent.argtypes = [POINTER(Display), Window, c_long, POINTER(XEvent)]
XCirculateSubwindows = _lib.XCirculateSubwindows
XCirculateSubwindows.restype = c_int
XCirculateSubwindows.argtypes = [POINTER(Display), Window, c_int]
XCirculateSubwindowsDown = _lib.XCirculateSubwindowsDown
XCirculateSubwindowsDown.restype = c_int
XCirculateSubwindowsDown.argtypes = [POINTER(Display), Window]
XCirculateSubwindowsUp = _lib.XCirculateSubwindowsUp
XCirculateSubwindowsUp.restype = c_int
XCirculateSubwindowsUp.argtypes = [POINTER(Display), Window]
XClearArea = _lib.XClearArea
XClearArea.restype = c_int
XClearArea.argtypes = [POINTER(Display), Window, c_int, c_int, c_uint, c_uint, c_int]
XClearWindow = _lib.XClearWindow
XClearWindow.restype = c_int
XClearWindow.argtypes = [POINTER(Display), Window]
XCloseDisplay = _lib.XCloseDisplay
XCloseDisplay.restype = c_int
XCloseDisplay.argtypes = [POINTER(Display)]
XConfigureWindow = _lib.XConfigureWindow
XConfigureWindow.restype = c_int
XConfigureWindow.argtypes = [POINTER(Display), Window, c_uint, POINTER(XWindowChanges)]
XConnectionNumber = _lib.XConnectionNumber
XConnectionNumber.restype = c_int
XConnectionNumber.argtypes = [POINTER(Display)]
XConvertSelection = _lib.XConvertSelection
XConvertSelection.restype = c_int
XConvertSelection.argtypes = [POINTER(Display), Atom, Atom, Atom, Window, Time]
XCopyArea = _lib.XCopyArea
XCopyArea.restype = c_int
XCopyArea.argtypes = [POINTER(Display), Drawable, Drawable, GC, c_int, c_int, c_uint, c_uint, c_int, c_int]
XCopyGC = _lib.XCopyGC
XCopyGC.restype = c_int
XCopyGC.argtypes = [POINTER(Display), GC, c_ulong, GC]
XCopyPlane = _lib.XCopyPlane
XCopyPlane.restype = c_int
XCopyPlane.argtypes = [POINTER(Display), Drawable, Drawable, GC, c_int, c_int, c_uint, c_uint, c_int, c_int, c_ulong]
XDefaultDepth = _lib.XDefaultDepth
XDefaultDepth.restype = c_int
XDefaultDepth.argtypes = [POINTER(Display), c_int]
XDefaultDepthOfScreen = _lib.XDefaultDepthOfScreen
XDefaultDepthOfScreen.restype = c_int
XDefaultDepthOfScreen.argtypes = [POINTER(Screen)]
XDefaultScreen = _lib.XDefaultScreen
XDefaultScreen.restype = c_int
XDefaultScreen.argtypes = [POINTER(Display)]
XDefineCursor = _lib.XDefineCursor
XDefineCursor.restype = c_int
XDefineCursor.argtypes = [POINTER(Display), Window, Cursor]
XDeleteProperty = _lib.XDeleteProperty
XDeleteProperty.restype = c_int
XDeleteProperty.argtypes = [POINTER(Display), Window, Atom]
XDestroyWindow = _lib.XDestroyWindow
XDestroyWindow.restype = c_int
XDestroyWindow.argtypes = [POINTER(Display), Window]
XDestroySubwindows = _lib.XDestroySubwindows
XDestroySubwindows.restype = c_int
XDestroySubwindows.argtypes = [POINTER(Display), Window]
XDoesBackingStore = _lib.XDoesBackingStore
XDoesBackingStore.restype = c_int
XDoesBackingStore.argtypes = [POINTER(Screen)]
XDoesSaveUnders = _lib.XDoesSaveUnders
XDoesSaveUnders.restype = c_int
XDoesSaveUnders.argtypes = [POINTER(Screen)]
XDisableAccessControl = _lib.XDisableAccessControl
XDisableAccessControl.restype = c_int
XDisableAccessControl.argtypes = [POINTER(Display)]
XDisplayCells = _lib.XDisplayCells
XDisplayCells.restype = c_int
XDisplayCells.argtypes = [POINTER(Display), c_int]
XDisplayHeight = _lib.XDisplayHeight
XDisplayHeight.restype = c_int
XDisplayHeight.argtypes = [POINTER(Display), c_int]
XDisplayHeightMM = _lib.XDisplayHeightMM
XDisplayHeightMM.restype = c_int
XDisplayHeightMM.argtypes = [POINTER(Display), c_int]
XDisplayKeycodes = _lib.XDisplayKeycodes
XDisplayKeycodes.restype = c_int
XDisplayKeycodes.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XDisplayPlanes = _lib.XDisplayPlanes
XDisplayPlanes.restype = c_int
XDisplayPlanes.argtypes = [POINTER(Display), c_int]
XDisplayWidth = _lib.XDisplayWidth
XDisplayWidth.restype = c_int
XDisplayWidth.argtypes = [POINTER(Display), c_int]
XDisplayWidthMM = _lib.XDisplayWidthMM
XDisplayWidthMM.restype = c_int
XDisplayWidthMM.argtypes = [POINTER(Display), c_int]
XDrawArc = _lib.XDrawArc
XDrawArc.restype = c_int
XDrawArc.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_uint, c_uint, c_int, c_int]
XDrawArcs = _lib.XDrawArcs
XDrawArcs.restype = c_int
XDrawArcs.argtypes = [POINTER(Display), Drawable, GC, POINTER(XArc), c_int]
XDrawImageString = _lib.XDrawImageString
XDrawImageString.restype = c_int
XDrawImageString.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_char_p, c_int]
XDrawImageString16 = _lib.XDrawImageString16
XDrawImageString16.restype = c_int
XDrawImageString16.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XChar2b), c_int]
XDrawLine = _lib.XDrawLine
XDrawLine.restype = c_int
XDrawLine.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_int, c_int]
XDrawLines = _lib.XDrawLines
XDrawLines.restype = c_int
XDrawLines.argtypes = [POINTER(Display), Drawable, GC, POINTER(XPoint), c_int, c_int]
XDrawPoint = _lib.XDrawPoint
XDrawPoint.restype = c_int
XDrawPoint.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int]
XDrawPoints = _lib.XDrawPoints
XDrawPoints.restype = c_int
XDrawPoints.argtypes = [POINTER(Display), Drawable, GC, POINTER(XPoint), c_int, c_int]
XDrawRectangle = _lib.XDrawRectangle
XDrawRectangle.restype = c_int
XDrawRectangle.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_uint, c_uint]
XDrawRectangles = _lib.XDrawRectangles
XDrawRectangles.restype = c_int
XDrawRectangles.argtypes = [POINTER(Display), Drawable, GC, POINTER(XRectangle), c_int]
XDrawSegments = _lib.XDrawSegments
XDrawSegments.restype = c_int
XDrawSegments.argtypes = [POINTER(Display), Drawable, GC, POINTER(XSegment), c_int]
XDrawString = _lib.XDrawString
XDrawString.restype = c_int
XDrawString.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_char_p, c_int]
XDrawString16 = _lib.XDrawString16
XDrawString16.restype = c_int
XDrawString16.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XChar2b), c_int]
XDrawText = _lib.XDrawText
XDrawText.restype = c_int
XDrawText.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XTextItem), c_int]
XDrawText16 = _lib.XDrawText16
XDrawText16.restype = c_int
XDrawText16.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XTextItem16), c_int]
XEnableAccessControl = _lib.XEnableAccessControl
XEnableAccessControl.restype = c_int
XEnableAccessControl.argtypes = [POINTER(Display)]
XEventsQueued = _lib.XEventsQueued
XEventsQueued.restype = c_int
XEventsQueued.argtypes = [POINTER(Display), c_int]
XFetchName = _lib.XFetchName
XFetchName.restype = c_int
XFetchName.argtypes = [POINTER(Display), Window, POINTER(c_char_p)]
XFillArc = _lib.XFillArc
XFillArc.restype = c_int
XFillArc.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_uint, c_uint, c_int, c_int]
XFillArcs = _lib.XFillArcs
XFillArcs.restype = c_int
XFillArcs.argtypes = [POINTER(Display), Drawable, GC, POINTER(XArc), c_int]
XFillPolygon = _lib.XFillPolygon
XFillPolygon.restype = c_int
XFillPolygon.argtypes = [POINTER(Display), Drawable, GC, POINTER(XPoint), c_int, c_int, c_int]
XFillRectangle = _lib.XFillRectangle
XFillRectangle.restype = c_int
XFillRectangle.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, c_uint, c_uint]
XFillRectangles = _lib.XFillRectangles
XFillRectangles.restype = c_int
XFillRectangles.argtypes = [POINTER(Display), Drawable, GC, POINTER(XRectangle), c_int]
XFlush = _lib.XFlush
XFlush.restype = c_int
XFlush.argtypes = [POINTER(Display)]
XForceScreenSaver = _lib.XForceScreenSaver
XForceScreenSaver.restype = c_int
XForceScreenSaver.argtypes = [POINTER(Display), c_int]
XFree = _lib.XFree
XFree.restype = c_int
XFree.argtypes = [POINTER(None)]
XFreeColormap = _lib.XFreeColormap
XFreeColormap.restype = c_int
XFreeColormap.argtypes = [POINTER(Display), Colormap]
XFreeColors = _lib.XFreeColors
XFreeColors.restype = c_int
XFreeColors.argtypes = [POINTER(Display), Colormap, POINTER(c_ulong), c_int, c_ulong]
XFreeCursor = _lib.XFreeCursor
XFreeCursor.restype = c_int
XFreeCursor.argtypes = [POINTER(Display), Cursor]
XFreeExtensionList = _lib.XFreeExtensionList
XFreeExtensionList.restype = c_int
XFreeExtensionList.argtypes = [POINTER(c_char_p)]
XFreeFont = _lib.XFreeFont
XFreeFont.restype = c_int
XFreeFont.argtypes = [POINTER(Display), POINTER(XFontStruct)]
XFreeFontInfo = _lib.XFreeFontInfo
XFreeFontInfo.restype = c_int
XFreeFontInfo.argtypes = [POINTER(c_char_p), POINTER(XFontStruct), c_int]
XFreeFontNames = _lib.XFreeFontNames
XFreeFontNames.restype = c_int
XFreeFontNames.argtypes = [POINTER(c_char_p)]
XFreeFontPath = _lib.XFreeFontPath
XFreeFontPath.restype = c_int
XFreeFontPath.argtypes = [POINTER(c_char_p)]
XFreeGC = _lib.XFreeGC
XFreeGC.restype = c_int
XFreeGC.argtypes = [POINTER(Display), GC]
XFreeModifiermap = _lib.XFreeModifiermap
XFreeModifiermap.restype = c_int
XFreeModifiermap.argtypes = [POINTER(XModifierKeymap)]
XFreePixmap = _lib.XFreePixmap
XFreePixmap.restype = c_int
XFreePixmap.argtypes = [POINTER(Display), Pixmap]
XGeometry = _lib.XGeometry
XGeometry.restype = c_int
XGeometry.argtypes = [POINTER(Display), c_int, c_char_p, c_char_p, c_uint, c_uint, c_uint, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
XGetErrorDatabaseText = _lib.XGetErrorDatabaseText
XGetErrorDatabaseText.restype = c_int
XGetErrorDatabaseText.argtypes = [POINTER(Display), c_char_p, c_char_p, c_char_p, c_char_p, c_int]
XGetErrorText = _lib.XGetErrorText
XGetErrorText.restype = c_int
XGetErrorText.argtypes = [POINTER(Display), c_int, c_char_p, c_int]
XGetFontProperty = _lib.XGetFontProperty
XGetFontProperty.restype = c_int
XGetFontProperty.argtypes = [POINTER(XFontStruct), Atom, POINTER(c_ulong)]
XGetGCValues = _lib.XGetGCValues
XGetGCValues.restype = c_int
XGetGCValues.argtypes = [POINTER(Display), GC, c_ulong, POINTER(XGCValues)]
XGetGeometry = _lib.XGetGeometry
XGetGeometry.restype = c_int
XGetGeometry.argtypes = [POINTER(Display), Drawable, POINTER(Window), POINTER(c_int), POINTER(c_int), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
XGetIconName = _lib.XGetIconName
XGetIconName.restype = c_int
XGetIconName.argtypes = [POINTER(Display), Window, POINTER(c_char_p)]
XGetInputFocus = _lib.XGetInputFocus
XGetInputFocus.restype = c_int
XGetInputFocus.argtypes = [POINTER(Display), POINTER(Window), POINTER(c_int)]
XGetKeyboardControl = _lib.XGetKeyboardControl
XGetKeyboardControl.restype = c_int
XGetKeyboardControl.argtypes = [POINTER(Display), POINTER(XKeyboardState)]
XGetPointerControl = _lib.XGetPointerControl
XGetPointerControl.restype = c_int
XGetPointerControl.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
XGetPointerMapping = _lib.XGetPointerMapping
XGetPointerMapping.restype = c_int
XGetPointerMapping.argtypes = [POINTER(Display), POINTER(c_ubyte), c_int]
XGetScreenSaver = _lib.XGetScreenSaver
XGetScreenSaver.restype = c_int
XGetScreenSaver.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
XGetTransientForHint = _lib.XGetTransientForHint
XGetTransientForHint.restype = c_int
XGetTransientForHint.argtypes = [POINTER(Display), Window, POINTER(Window)]
XGetWindowProperty = _lib.XGetWindowProperty
XGetWindowProperty.restype = c_int
XGetWindowProperty.argtypes = [POINTER(Display), Window, Atom, c_long, c_long, c_int, Atom, POINTER(Atom), POINTER(c_int), POINTER(c_ulong), POINTER(c_ulong), POINTER(POINTER(c_ubyte))]
XGetWindowAttributes = _lib.XGetWindowAttributes
XGetWindowAttributes.restype = c_int
XGetWindowAttributes.argtypes = [POINTER(Display), Window, POINTER(XWindowAttributes)]
XGrabButton = _lib.XGrabButton
XGrabButton.restype = c_int
XGrabButton.argtypes = [POINTER(Display), c_uint, c_uint, Window, c_int, c_uint, c_int, c_int, Window, Cursor]
XGrabKey = _lib.XGrabKey
XGrabKey.restype = c_int
XGrabKey.argtypes = [POINTER(Display), c_int, c_uint, Window, c_int, c_int, c_int]
XGrabKeyboard = _lib.XGrabKeyboard
XGrabKeyboard.restype = c_int
XGrabKeyboard.argtypes = [POINTER(Display), Window, c_int, c_int, c_int, Time]
XGrabPointer = _lib.XGrabPointer
XGrabPointer.restype = c_int
XGrabPointer.argtypes = [POINTER(Display), Window, c_int, c_uint, c_int, c_int, Window, Cursor, Time]
XGrabServer = _lib.XGrabServer
XGrabServer.restype = c_int
XGrabServer.argtypes = [POINTER(Display)]
XHeightMMOfScreen = _lib.XHeightMMOfScreen
XHeightMMOfScreen.restype = c_int
XHeightMMOfScreen.argtypes = [POINTER(Screen)]
XHeightOfScreen = _lib.XHeightOfScreen
XHeightOfScreen.restype = c_int
XHeightOfScreen.argtypes = [POINTER(Screen)]
XIfEvent = _lib.XIfEvent
XIfEvent.restype = c_int
XIfEvent.argtypes = [POINTER(Display), POINTER(XEvent), CFUNCTYPE(c_int, POINTER(Display), POINTER(XEvent), XPointer), XPointer]
XImageByteOrder = _lib.XImageByteOrder
XImageByteOrder.restype = c_int
XImageByteOrder.argtypes = [POINTER(Display)]
XInstallColormap = _lib.XInstallColormap
XInstallColormap.restype = c_int
XInstallColormap.argtypes = [POINTER(Display), Colormap]
XKeysymToKeycode = _lib.XKeysymToKeycode
XKeysymToKeycode.restype = KeyCode
XKeysymToKeycode.argtypes = [POINTER(Display), KeySym]
XKillClient = _lib.XKillClient
XKillClient.restype = c_int
XKillClient.argtypes = [POINTER(Display), XID]
XLookupColor = _lib.XLookupColor
XLookupColor.restype = c_int
XLookupColor.argtypes = [POINTER(Display), Colormap, c_char_p, POINTER(XColor), POINTER(XColor)]
XLowerWindow = _lib.XLowerWindow
XLowerWindow.restype = c_int
XLowerWindow.argtypes = [POINTER(Display), Window]
XMapRaised = _lib.XMapRaised
XMapRaised.restype = c_int
XMapRaised.argtypes = [POINTER(Display), Window]
XMapSubwindows = _lib.XMapSubwindows
XMapSubwindows.restype = c_int
XMapSubwindows.argtypes = [POINTER(Display), Window]
XMapWindow = _lib.XMapWindow
XMapWindow.restype = c_int
XMapWindow.argtypes = [POINTER(Display), Window]
XMaskEvent = _lib.XMaskEvent
XMaskEvent.restype = c_int
XMaskEvent.argtypes = [POINTER(Display), c_long, POINTER(XEvent)]
XMaxCmapsOfScreen = _lib.XMaxCmapsOfScreen
XMaxCmapsOfScreen.restype = c_int
XMaxCmapsOfScreen.argtypes = [POINTER(Screen)]
XMinCmapsOfScreen = _lib.XMinCmapsOfScreen
XMinCmapsOfScreen.restype = c_int
XMinCmapsOfScreen.argtypes = [POINTER(Screen)]
XMoveResizeWindow = _lib.XMoveResizeWindow
XMoveResizeWindow.restype = c_int
XMoveResizeWindow.argtypes = [POINTER(Display), Window, c_int, c_int, c_uint, c_uint]
XMoveWindow = _lib.XMoveWindow
XMoveWindow.restype = c_int
XMoveWindow.argtypes = [POINTER(Display), Window, c_int, c_int]
XNextEvent = _lib.XNextEvent
XNextEvent.restype = c_int
XNextEvent.argtypes = [POINTER(Display), POINTER(XEvent)]
XNoOp = _lib.XNoOp
XNoOp.restype = c_int
XNoOp.argtypes = [POINTER(Display)]
XParseColor = _lib.XParseColor
XParseColor.restype = c_int
XParseColor.argtypes = [POINTER(Display), Colormap, c_char_p, POINTER(XColor)]
XParseGeometry = _lib.XParseGeometry
XParseGeometry.restype = c_int
XParseGeometry.argtypes = [c_char_p, POINTER(c_int), POINTER(c_int), POINTER(c_uint), POINTER(c_uint)]
XPeekEvent = _lib.XPeekEvent
XPeekEvent.restype = c_int
XPeekEvent.argtypes = [POINTER(Display), POINTER(XEvent)]
XPeekIfEvent = _lib.XPeekIfEvent
XPeekIfEvent.restype = c_int
XPeekIfEvent.argtypes = [POINTER(Display), POINTER(XEvent), CFUNCTYPE(c_int, POINTER(Display), POINTER(XEvent), XPointer), XPointer]
XPending = _lib.XPending
XPending.restype = c_int
XPending.argtypes = [POINTER(Display)]
XPlanesOfScreen = _lib.XPlanesOfScreen
XPlanesOfScreen.restype = c_int
XPlanesOfScreen.argtypes = [POINTER(Screen)]
XProtocolRevision = _lib.XProtocolRevision
XProtocolRevision.restype = c_int
XProtocolRevision.argtypes = [POINTER(Display)]
XProtocolVersion = _lib.XProtocolVersion
XProtocolVersion.restype = c_int
XProtocolVersion.argtypes = [POINTER(Display)]
XPutBackEvent = _lib.XPutBackEvent
XPutBackEvent.restype = c_int
XPutBackEvent.argtypes = [POINTER(Display), POINTER(XEvent)]
XPutImage = _lib.XPutImage
XPutImage.restype = c_int
XPutImage.argtypes = [POINTER(Display), Drawable, GC, POINTER(XImage), c_int, c_int, c_int, c_int, c_uint, c_uint]
XQLength = _lib.XQLength
XQLength.restype = c_int
XQLength.argtypes = [POINTER(Display)]
XQueryBestCursor = _lib.XQueryBestCursor
XQueryBestCursor.restype = c_int
XQueryBestCursor.argtypes = [POINTER(Display), Drawable, c_uint, c_uint, POINTER(c_uint), POINTER(c_uint)]
XQueryBestSize = _lib.XQueryBestSize
XQueryBestSize.restype = c_int
XQueryBestSize.argtypes = [POINTER(Display), c_int, Drawable, c_uint, c_uint, POINTER(c_uint), POINTER(c_uint)]
XQueryBestStipple = _lib.XQueryBestStipple
XQueryBestStipple.restype = c_int
XQueryBestStipple.argtypes = [POINTER(Display), Drawable, c_uint, c_uint, POINTER(c_uint), POINTER(c_uint)]
XQueryBestTile = _lib.XQueryBestTile
XQueryBestTile.restype = c_int
XQueryBestTile.argtypes = [POINTER(Display), Drawable, c_uint, c_uint, POINTER(c_uint), POINTER(c_uint)]
XQueryColor = _lib.XQueryColor
XQueryColor.restype = c_int
XQueryColor.argtypes = [POINTER(Display), Colormap, POINTER(XColor)]
XQueryColors = _lib.XQueryColors
XQueryColors.restype = c_int
XQueryColors.argtypes = [POINTER(Display), Colormap, POINTER(XColor), c_int]
XQueryExtension = _lib.XQueryExtension
XQueryExtension.restype = c_int
XQueryExtension.argtypes = [POINTER(Display), c_char_p, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
XQueryKeymap = _lib.XQueryKeymap
XQueryKeymap.restype = c_int
XQueryKeymap.argtypes = [POINTER(Display), c_char * 32]
XQueryPointer = _lib.XQueryPointer
XQueryPointer.restype = c_int
XQueryPointer.argtypes = [POINTER(Display), Window, POINTER(Window), POINTER(Window), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_uint)]
XQueryTextExtents = _lib.XQueryTextExtents
XQueryTextExtents.restype = c_int
XQueryTextExtents.argtypes = [POINTER(Display), XID, c_char_p, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(XCharStruct)]
XQueryTextExtents16 = _lib.XQueryTextExtents16
XQueryTextExtents16.restype = c_int
XQueryTextExtents16.argtypes = [POINTER(Display), XID, POINTER(XChar2b), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(XCharStruct)]
XQueryTree = _lib.XQueryTree
XQueryTree.restype = c_int
XQueryTree.argtypes = [POINTER(Display), Window, POINTER(Window), POINTER(Window), POINTER(POINTER(Window)), POINTER(c_uint)]
XRaiseWindow = _lib.XRaiseWindow
XRaiseWindow.restype = c_int
XRaiseWindow.argtypes = [POINTER(Display), Window]
XReadBitmapFile = _lib.XReadBitmapFile
XReadBitmapFile.restype = c_int
XReadBitmapFile.argtypes = [POINTER(Display), Drawable, c_char_p, POINTER(c_uint), POINTER(c_uint), POINTER(Pixmap), POINTER(c_int), POINTER(c_int)]
XReadBitmapFileData = _lib.XReadBitmapFileData
XReadBitmapFileData.restype = c_int
XReadBitmapFileData.argtypes = [c_char_p, POINTER(c_uint), POINTER(c_uint), POINTER(POINTER(c_ubyte)), POINTER(c_int), POINTER(c_int)]
XRebindKeysym = _lib.XRebindKeysym
XRebindKeysym.restype = c_int
XRebindKeysym.argtypes = [POINTER(Display), KeySym, POINTER(KeySym), c_int, POINTER(c_ubyte), c_int]
XRecolorCursor = _lib.XRecolorCursor
XRecolorCursor.restype = c_int
XRecolorCursor.argtypes = [POINTER(Display), Cursor, POINTER(XColor), POINTER(XColor)]
XRefreshKeyboardMapping = _lib.XRefreshKeyboardMapping
XRefreshKeyboardMapping.restype = c_int
XRefreshKeyboardMapping.argtypes = [POINTER(XMappingEvent)]
XRemoveFromSaveSet = _lib.XRemoveFromSaveSet
XRemoveFromSaveSet.restype = c_int
XRemoveFromSaveSet.argtypes = [POINTER(Display), Window]
XRemoveHost = _lib.XRemoveHost
XRemoveHost.restype = c_int
XRemoveHost.argtypes = [POINTER(Display), POINTER(XHostAddress)]
XRemoveHosts = _lib.XRemoveHosts
XRemoveHosts.restype = c_int
XRemoveHosts.argtypes = [POINTER(Display), POINTER(XHostAddress), c_int]
XReparentWindow = _lib.XReparentWindow
XReparentWindow.restype = c_int
XReparentWindow.argtypes = [POINTER(Display), Window, Window, c_int, c_int]
XResetScreenSaver = _lib.XResetScreenSaver
XResetScreenSaver.restype = c_int
XResetScreenSaver.argtypes = [POINTER(Display)]
XResizeWindow = _lib.XResizeWindow
XResizeWindow.restype = c_int
XResizeWindow.argtypes = [POINTER(Display), Window, c_uint, c_uint]
XRestackWindows = _lib.XRestackWindows
XRestackWindows.restype = c_int
XRestackWindows.argtypes = [POINTER(Display), POINTER(Window), c_int]
XRotateBuffers = _lib.XRotateBuffers
XRotateBuffers.restype = c_int
XRotateBuffers.argtypes = [POINTER(Display), c_int]
XRotateWindowProperties = _lib.XRotateWindowProperties
XRotateWindowProperties.restype = c_int
XRotateWindowProperties.argtypes = [POINTER(Display), Window, POINTER(Atom), c_int, c_int]
XScreenCount = _lib.XScreenCount
XScreenCount.restype = c_int
XScreenCount.argtypes = [POINTER(Display)]
XSelectInput = _lib.XSelectInput
XSelectInput.restype = c_int
XSelectInput.argtypes = [POINTER(Display), Window, c_long]
XSendEvent = _lib.XSendEvent
XSendEvent.restype = c_int
XSendEvent.argtypes = [POINTER(Display), Window, c_int, c_long, POINTER(XEvent)]
XSetAccessControl = _lib.XSetAccessControl
XSetAccessControl.restype = c_int
XSetAccessControl.argtypes = [POINTER(Display), c_int]
XSetArcMode = _lib.XSetArcMode
XSetArcMode.restype = c_int
XSetArcMode.argtypes = [POINTER(Display), GC, c_int]
XSetBackground = _lib.XSetBackground
XSetBackground.restype = c_int
XSetBackground.argtypes = [POINTER(Display), GC, c_ulong]
XSetClipMask = _lib.XSetClipMask
XSetClipMask.restype = c_int
XSetClipMask.argtypes = [POINTER(Display), GC, Pixmap]
XSetClipOrigin = _lib.XSetClipOrigin
XSetClipOrigin.restype = c_int
XSetClipOrigin.argtypes = [POINTER(Display), GC, c_int, c_int]
XSetClipRectangles = _lib.XSetClipRectangles
XSetClipRectangles.restype = c_int
XSetClipRectangles.argtypes = [POINTER(Display), GC, c_int, c_int, POINTER(XRectangle), c_int, c_int]
XSetCloseDownMode = _lib.XSetCloseDownMode
XSetCloseDownMode.restype = c_int
XSetCloseDownMode.argtypes = [POINTER(Display), c_int]
XSetCommand = _lib.XSetCommand
XSetCommand.restype = c_int
XSetCommand.argtypes = [POINTER(Display), Window, POINTER(c_char_p), c_int]
XSetDashes = _lib.XSetDashes
XSetDashes.restype = c_int
XSetDashes.argtypes = [POINTER(Display), GC, c_int, c_char_p, c_int]
XSetFillRule = _lib.XSetFillRule
XSetFillRule.restype = c_int
XSetFillRule.argtypes = [POINTER(Display), GC, c_int]
XSetFillStyle = _lib.XSetFillStyle
XSetFillStyle.restype = c_int
XSetFillStyle.argtypes = [POINTER(Display), GC, c_int]
XSetFont = _lib.XSetFont
XSetFont.restype = c_int
XSetFont.argtypes = [POINTER(Display), GC, Font]
XSetFontPath = _lib.XSetFontPath
XSetFontPath.restype = c_int
XSetFontPath.argtypes = [POINTER(Display), POINTER(c_char_p), c_int]
XSetForeground = _lib.XSetForeground
XSetForeground.restype = c_int
XSetForeground.argtypes = [POINTER(Display), GC, c_ulong]
XSetFunction = _lib.XSetFunction
XSetFunction.restype = c_int
XSetFunction.argtypes = [POINTER(Display), GC, c_int]
XSetGraphicsExposures = _lib.XSetGraphicsExposures
XSetGraphicsExposures.restype = c_int
XSetGraphicsExposures.argtypes = [POINTER(Display), GC, c_int]
XSetIconName = _lib.XSetIconName
XSetIconName.restype = c_int
XSetIconName.argtypes = [POINTER(Display), Window, c_char_p]
XSetInputFocus = _lib.XSetInputFocus
XSetInputFocus.restype = c_int
XSetInputFocus.argtypes = [POINTER(Display), Window, c_int, Time]
XSetLineAttributes = _lib.XSetLineAttributes
XSetLineAttributes.restype = c_int
XSetLineAttributes.argtypes = [POINTER(Display), GC, c_uint, c_int, c_int, c_int]
XSetModifierMapping = _lib.XSetModifierMapping
XSetModifierMapping.restype = c_int
XSetModifierMapping.argtypes = [POINTER(Display), POINTER(XModifierKeymap)]
XSetPlaneMask = _lib.XSetPlaneMask
XSetPlaneMask.restype = c_int
XSetPlaneMask.argtypes = [POINTER(Display), GC, c_ulong]
XSetPointerMapping = _lib.XSetPointerMapping
XSetPointerMapping.restype = c_int
XSetPointerMapping.argtypes = [POINTER(Display), POINTER(c_ubyte), c_int]
XSetScreenSaver = _lib.XSetScreenSaver
XSetScreenSaver.restype = c_int
XSetScreenSaver.argtypes = [POINTER(Display), c_int, c_int, c_int, c_int]
XSetSelectionOwner = _lib.XSetSelectionOwner
XSetSelectionOwner.restype = c_int
XSetSelectionOwner.argtypes = [POINTER(Display), Atom, Window, Time]
XSetState = _lib.XSetState
XSetState.restype = c_int
XSetState.argtypes = [POINTER(Display), GC, c_ulong, c_ulong, c_int, c_ulong]
XSetStipple = _lib.XSetStipple
XSetStipple.restype = c_int
XSetStipple.argtypes = [POINTER(Display), GC, Pixmap]
XSetSubwindowMode = _lib.XSetSubwindowMode
XSetSubwindowMode.restype = c_int
XSetSubwindowMode.argtypes = [POINTER(Display), GC, c_int]
XSetTSOrigin = _lib.XSetTSOrigin
XSetTSOrigin.restype = c_int
XSetTSOrigin.argtypes = [POINTER(Display), GC, c_int, c_int]
XSetTile = _lib.XSetTile
XSetTile.restype = c_int
XSetTile.argtypes = [POINTER(Display), GC, Pixmap]
XSetWindowBackground = _lib.XSetWindowBackground
XSetWindowBackground.restype = c_int
XSetWindowBackground.argtypes = [POINTER(Display), Window, c_ulong]
XSetWindowBackgroundPixmap = _lib.XSetWindowBackgroundPixmap
XSetWindowBackgroundPixmap.restype = c_int
XSetWindowBackgroundPixmap.argtypes = [POINTER(Display), Window, Pixmap]
XSetWindowBorder = _lib.XSetWindowBorder
XSetWindowBorder.restype = c_int
XSetWindowBorder.argtypes = [POINTER(Display), Window, c_ulong]
XSetWindowBorderPixmap = _lib.XSetWindowBorderPixmap
XSetWindowBorderPixmap.restype = c_int
XSetWindowBorderPixmap.argtypes = [POINTER(Display), Window, Pixmap]
XSetWindowBorderWidth = _lib.XSetWindowBorderWidth
XSetWindowBorderWidth.restype = c_int
XSetWindowBorderWidth.argtypes = [POINTER(Display), Window, c_uint]
XSetWindowColormap = _lib.XSetWindowColormap
XSetWindowColormap.restype = c_int
XSetWindowColormap.argtypes = [POINTER(Display), Window, Colormap]
XStoreBuffer = _lib.XStoreBuffer
XStoreBuffer.restype = c_int
XStoreBuffer.argtypes = [POINTER(Display), c_char_p, c_int, c_int]
XStoreBytes = _lib.XStoreBytes
XStoreBytes.restype = c_int
XStoreBytes.argtypes = [POINTER(Display), c_char_p, c_int]
XStoreColor = _lib.XStoreColor
XStoreColor.restype = c_int
XStoreColor.argtypes = [POINTER(Display), Colormap, POINTER(XColor)]
XStoreColors = _lib.XStoreColors
XStoreColors.restype = c_int
XStoreColors.argtypes = [POINTER(Display), Colormap, POINTER(XColor), c_int]
XStoreName = _lib.XStoreName
XStoreName.restype = c_int
XStoreName.argtypes = [POINTER(Display), Window, c_char_p]
XStoreNamedColor = _lib.XStoreNamedColor
XStoreNamedColor.restype = c_int
XStoreNamedColor.argtypes = [POINTER(Display), Colormap, c_char_p, c_ulong, c_int]
XSync = _lib.XSync
XSync.restype = c_int
XSync.argtypes = [POINTER(Display), c_int]
XTextExtents = _lib.XTextExtents
XTextExtents.restype = c_int
XTextExtents.argtypes = [POINTER(XFontStruct), c_char_p, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(XCharStruct)]
XTextExtents16 = _lib.XTextExtents16
XTextExtents16.restype = c_int
XTextExtents16.argtypes = [POINTER(XFontStruct), POINTER(XChar2b), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(XCharStruct)]
XTextWidth = _lib.XTextWidth
XTextWidth.restype = c_int
XTextWidth.argtypes = [POINTER(XFontStruct), c_char_p, c_int]
XTextWidth16 = _lib.XTextWidth16
XTextWidth16.restype = c_int
XTextWidth16.argtypes = [POINTER(XFontStruct), POINTER(XChar2b), c_int]
XTranslateCoordinates = _lib.XTranslateCoordinates
XTranslateCoordinates.restype = c_int
XTranslateCoordinates.argtypes = [POINTER(Display), Window, Window, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(Window)]
XUndefineCursor = _lib.XUndefineCursor
XUndefineCursor.restype = c_int
XUndefineCursor.argtypes = [POINTER(Display), Window]
XUngrabButton = _lib.XUngrabButton
XUngrabButton.restype = c_int
XUngrabButton.argtypes = [POINTER(Display), c_uint, c_uint, Window]
XUngrabKey = _lib.XUngrabKey
XUngrabKey.restype = c_int
XUngrabKey.argtypes = [POINTER(Display), c_int, c_uint, Window]
XUngrabKeyboard = _lib.XUngrabKeyboard
XUngrabKeyboard.restype = c_int
XUngrabKeyboard.argtypes = [POINTER(Display), Time]
XUngrabPointer = _lib.XUngrabPointer
XUngrabPointer.restype = c_int
XUngrabPointer.argtypes = [POINTER(Display), Time]
XUngrabServer = _lib.XUngrabServer
XUngrabServer.restype = c_int
XUngrabServer.argtypes = [POINTER(Display)]
XUninstallColormap = _lib.XUninstallColormap
XUninstallColormap.restype = c_int
XUninstallColormap.argtypes = [POINTER(Display), Colormap]
XUnloadFont = _lib.XUnloadFont
XUnloadFont.restype = c_int
XUnloadFont.argtypes = [POINTER(Display), Font]
XUnmapSubwindows = _lib.XUnmapSubwindows
XUnmapSubwindows.restype = c_int
XUnmapSubwindows.argtypes = [POINTER(Display), Window]
XUnmapWindow = _lib.XUnmapWindow
XUnmapWindow.restype = c_int
XUnmapWindow.argtypes = [POINTER(Display), Window]
XVendorRelease = _lib.XVendorRelease
XVendorRelease.restype = c_int
XVendorRelease.argtypes = [POINTER(Display)]
XWarpPointer = _lib.XWarpPointer
XWarpPointer.restype = c_int
XWarpPointer.argtypes = [POINTER(Display), Window, Window, c_int, c_int, c_uint, c_uint, c_int, c_int]
XWidthMMOfScreen = _lib.XWidthMMOfScreen
XWidthMMOfScreen.restype = c_int
XWidthMMOfScreen.argtypes = [POINTER(Screen)]
XWidthOfScreen = _lib.XWidthOfScreen
XWidthOfScreen.restype = c_int
XWidthOfScreen.argtypes = [POINTER(Screen)]
XWindowEvent = _lib.XWindowEvent
XWindowEvent.restype = c_int
XWindowEvent.argtypes = [POINTER(Display), Window, c_long, POINTER(XEvent)]
XWriteBitmapFile = _lib.XWriteBitmapFile
XWriteBitmapFile.restype = c_int
XWriteBitmapFile.argtypes = [POINTER(Display), c_char_p, Pixmap, c_uint, c_uint, c_int, c_int]
XSupportsLocale = _lib.XSupportsLocale
XSupportsLocale.restype = c_int
XSupportsLocale.argtypes = []
XSetLocaleModifiers = _lib.XSetLocaleModifiers
XSetLocaleModifiers.restype = c_char_p
XSetLocaleModifiers.argtypes = [c_char_p]

class struct__XrmHashBucketRec(Structure):
    __slots__ = []


struct__XrmHashBucketRec._fields_ = [
 (
  '_opaque_struct', c_int)]
XOpenOM = _lib.XOpenOM
XOpenOM.restype = XOM
XOpenOM.argtypes = [POINTER(Display), POINTER(struct__XrmHashBucketRec), c_char_p, c_char_p]
XCloseOM = _lib.XCloseOM
XCloseOM.restype = c_int
XCloseOM.argtypes = [XOM]
XSetOMValues = _lib.XSetOMValues
XSetOMValues.restype = c_char_p
XSetOMValues.argtypes = [XOM]
XGetOMValues = _lib.XGetOMValues
XGetOMValues.restype = c_char_p
XGetOMValues.argtypes = [XOM]
XDisplayOfOM = _lib.XDisplayOfOM
XDisplayOfOM.restype = POINTER(Display)
XDisplayOfOM.argtypes = [XOM]
XLocaleOfOM = _lib.XLocaleOfOM
XLocaleOfOM.restype = c_char_p
XLocaleOfOM.argtypes = [XOM]
XCreateOC = _lib.XCreateOC
XCreateOC.restype = XOC
XCreateOC.argtypes = [XOM]
XDestroyOC = _lib.XDestroyOC
XDestroyOC.restype = None
XDestroyOC.argtypes = [XOC]
XOMOfOC = _lib.XOMOfOC
XOMOfOC.restype = XOM
XOMOfOC.argtypes = [XOC]
XSetOCValues = _lib.XSetOCValues
XSetOCValues.restype = c_char_p
XSetOCValues.argtypes = [XOC]
XGetOCValues = _lib.XGetOCValues
XGetOCValues.restype = c_char_p
XGetOCValues.argtypes = [XOC]
XCreateFontSet = _lib.XCreateFontSet
XCreateFontSet.restype = XFontSet
XCreateFontSet.argtypes = [POINTER(Display), c_char_p, POINTER(POINTER(c_char_p)), POINTER(c_int), POINTER(c_char_p)]
XFreeFontSet = _lib.XFreeFontSet
XFreeFontSet.restype = None
XFreeFontSet.argtypes = [POINTER(Display), XFontSet]
XFontsOfFontSet = _lib.XFontsOfFontSet
XFontsOfFontSet.restype = c_int
XFontsOfFontSet.argtypes = [XFontSet, POINTER(POINTER(POINTER(XFontStruct))), POINTER(POINTER(c_char_p))]
XBaseFontNameListOfFontSet = _lib.XBaseFontNameListOfFontSet
XBaseFontNameListOfFontSet.restype = c_char_p
XBaseFontNameListOfFontSet.argtypes = [XFontSet]
XLocaleOfFontSet = _lib.XLocaleOfFontSet
XLocaleOfFontSet.restype = c_char_p
XLocaleOfFontSet.argtypes = [XFontSet]
XContextDependentDrawing = _lib.XContextDependentDrawing
XContextDependentDrawing.restype = c_int
XContextDependentDrawing.argtypes = [XFontSet]
XDirectionalDependentDrawing = _lib.XDirectionalDependentDrawing
XDirectionalDependentDrawing.restype = c_int
XDirectionalDependentDrawing.argtypes = [XFontSet]
XContextualDrawing = _lib.XContextualDrawing
XContextualDrawing.restype = c_int
XContextualDrawing.argtypes = [XFontSet]
XExtentsOfFontSet = _lib.XExtentsOfFontSet
XExtentsOfFontSet.restype = POINTER(XFontSetExtents)
XExtentsOfFontSet.argtypes = [XFontSet]
XmbTextEscapement = _lib.XmbTextEscapement
XmbTextEscapement.restype = c_int
XmbTextEscapement.argtypes = [XFontSet, c_char_p, c_int]
XwcTextEscapement = _lib.XwcTextEscapement
XwcTextEscapement.restype = c_int
XwcTextEscapement.argtypes = [XFontSet, c_wchar_p, c_int]
Xutf8TextEscapement = _lib.Xutf8TextEscapement
Xutf8TextEscapement.restype = c_int
Xutf8TextEscapement.argtypes = [XFontSet, c_char_p, c_int]
XmbTextExtents = _lib.XmbTextExtents
XmbTextExtents.restype = c_int
XmbTextExtents.argtypes = [XFontSet, c_char_p, c_int, POINTER(XRectangle), POINTER(XRectangle)]
XwcTextExtents = _lib.XwcTextExtents
XwcTextExtents.restype = c_int
XwcTextExtents.argtypes = [XFontSet, c_wchar_p, c_int, POINTER(XRectangle), POINTER(XRectangle)]
Xutf8TextExtents = _lib.Xutf8TextExtents
Xutf8TextExtents.restype = c_int
Xutf8TextExtents.argtypes = [XFontSet, c_char_p, c_int, POINTER(XRectangle), POINTER(XRectangle)]
XmbTextPerCharExtents = _lib.XmbTextPerCharExtents
XmbTextPerCharExtents.restype = c_int
XmbTextPerCharExtents.argtypes = [XFontSet, c_char_p, c_int, POINTER(XRectangle), POINTER(XRectangle), c_int, POINTER(c_int), POINTER(XRectangle), POINTER(XRectangle)]
XwcTextPerCharExtents = _lib.XwcTextPerCharExtents
XwcTextPerCharExtents.restype = c_int
XwcTextPerCharExtents.argtypes = [XFontSet, c_wchar_p, c_int, POINTER(XRectangle), POINTER(XRectangle), c_int, POINTER(c_int), POINTER(XRectangle), POINTER(XRectangle)]
Xutf8TextPerCharExtents = _lib.Xutf8TextPerCharExtents
Xutf8TextPerCharExtents.restype = c_int
Xutf8TextPerCharExtents.argtypes = [XFontSet, c_char_p, c_int, POINTER(XRectangle), POINTER(XRectangle), c_int, POINTER(c_int), POINTER(XRectangle), POINTER(XRectangle)]
XmbDrawText = _lib.XmbDrawText
XmbDrawText.restype = None
XmbDrawText.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XmbTextItem), c_int]
XwcDrawText = _lib.XwcDrawText
XwcDrawText.restype = None
XwcDrawText.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XwcTextItem), c_int]
Xutf8DrawText = _lib.Xutf8DrawText
Xutf8DrawText.restype = None
Xutf8DrawText.argtypes = [POINTER(Display), Drawable, GC, c_int, c_int, POINTER(XmbTextItem), c_int]
XmbDrawString = _lib.XmbDrawString
XmbDrawString.restype = None
XmbDrawString.argtypes = [POINTER(Display), Drawable, XFontSet, GC, c_int, c_int, c_char_p, c_int]
XwcDrawString = _lib.XwcDrawString
XwcDrawString.restype = None
XwcDrawString.argtypes = [POINTER(Display), Drawable, XFontSet, GC, c_int, c_int, c_wchar_p, c_int]
Xutf8DrawString = _lib.Xutf8DrawString
Xutf8DrawString.restype = None
Xutf8DrawString.argtypes = [POINTER(Display), Drawable, XFontSet, GC, c_int, c_int, c_char_p, c_int]
XmbDrawImageString = _lib.XmbDrawImageString
XmbDrawImageString.restype = None
XmbDrawImageString.argtypes = [POINTER(Display), Drawable, XFontSet, GC, c_int, c_int, c_char_p, c_int]
XwcDrawImageString = _lib.XwcDrawImageString
XwcDrawImageString.restype = None
XwcDrawImageString.argtypes = [POINTER(Display), Drawable, XFontSet, GC, c_int, c_int, c_wchar_p, c_int]
Xutf8DrawImageString = _lib.Xutf8DrawImageString
Xutf8DrawImageString.restype = None
Xutf8DrawImageString.argtypes = [POINTER(Display), Drawable, XFontSet, GC, c_int, c_int, c_char_p, c_int]

class struct__XrmHashBucketRec(Structure):
    __slots__ = []


struct__XrmHashBucketRec._fields_ = [
 (
  '_opaque_struct', c_int)]
XOpenIM = _lib.XOpenIM
XOpenIM.restype = XIM
XOpenIM.argtypes = [POINTER(Display), POINTER(struct__XrmHashBucketRec), c_char_p, c_char_p]
XCloseIM = _lib.XCloseIM
XCloseIM.restype = c_int
XCloseIM.argtypes = [XIM]
XGetIMValues = _lib.XGetIMValues
XGetIMValues.restype = c_char_p
XGetIMValues.argtypes = [XIM]
XSetIMValues = _lib.XSetIMValues
XSetIMValues.restype = c_char_p
XSetIMValues.argtypes = [XIM]
XDisplayOfIM = _lib.XDisplayOfIM
XDisplayOfIM.restype = POINTER(Display)
XDisplayOfIM.argtypes = [XIM]
XLocaleOfIM = _lib.XLocaleOfIM
XLocaleOfIM.restype = c_char_p
XLocaleOfIM.argtypes = [XIM]
XCreateIC = _lib.XCreateIC
XCreateIC.restype = XIC
XCreateIC.argtypes = [XIM]
XDestroyIC = _lib.XDestroyIC
XDestroyIC.restype = None
XDestroyIC.argtypes = [XIC]
XSetICFocus = _lib.XSetICFocus
XSetICFocus.restype = None
XSetICFocus.argtypes = [XIC]
XUnsetICFocus = _lib.XUnsetICFocus
XUnsetICFocus.restype = None
XUnsetICFocus.argtypes = [XIC]
XwcResetIC = _lib.XwcResetIC
XwcResetIC.restype = c_wchar_p
XwcResetIC.argtypes = [XIC]
XmbResetIC = _lib.XmbResetIC
XmbResetIC.restype = c_char_p
XmbResetIC.argtypes = [XIC]
Xutf8ResetIC = _lib.Xutf8ResetIC
Xutf8ResetIC.restype = c_char_p
Xutf8ResetIC.argtypes = [XIC]
XSetICValues = _lib.XSetICValues
XSetICValues.restype = c_char_p
XSetICValues.argtypes = [XIC]
XGetICValues = _lib.XGetICValues
XGetICValues.restype = c_char_p
XGetICValues.argtypes = [XIC]
XIMOfIC = _lib.XIMOfIC
XIMOfIC.restype = XIM
XIMOfIC.argtypes = [XIC]
XFilterEvent = _lib.XFilterEvent
XFilterEvent.restype = c_int
XFilterEvent.argtypes = [POINTER(XEvent), Window]
XmbLookupString = _lib.XmbLookupString
XmbLookupString.restype = c_int
XmbLookupString.argtypes = [XIC, POINTER(XKeyPressedEvent), c_char_p, c_int, POINTER(KeySym), POINTER(c_int)]
XwcLookupString = _lib.XwcLookupString
XwcLookupString.restype = c_int
XwcLookupString.argtypes = [XIC, POINTER(XKeyPressedEvent), c_wchar_p, c_int, POINTER(KeySym), POINTER(c_int)]
Xutf8LookupString = _lib.Xutf8LookupString
Xutf8LookupString.restype = c_int
Xutf8LookupString.argtypes = [XIC, POINTER(XKeyPressedEvent), c_char_p, c_int, POINTER(KeySym), POINTER(c_int)]
XVaCreateNestedList = _lib.XVaCreateNestedList
XVaCreateNestedList.restype = XVaNestedList
XVaCreateNestedList.argtypes = [c_int]

class struct__XrmHashBucketRec(Structure):
    __slots__ = []


struct__XrmHashBucketRec._fields_ = [
 (
  '_opaque_struct', c_int)]
XRegisterIMInstantiateCallback = _lib.XRegisterIMInstantiateCallback
XRegisterIMInstantiateCallback.restype = c_int
XRegisterIMInstantiateCallback.argtypes = [POINTER(Display), POINTER(struct__XrmHashBucketRec), c_char_p, c_char_p, XIDProc, XPointer]

class struct__XrmHashBucketRec(Structure):
    __slots__ = []


struct__XrmHashBucketRec._fields_ = [
 (
  '_opaque_struct', c_int)]
XUnregisterIMInstantiateCallback = _lib.XUnregisterIMInstantiateCallback
XUnregisterIMInstantiateCallback.restype = c_int
XUnregisterIMInstantiateCallback.argtypes = [POINTER(Display), POINTER(struct__XrmHashBucketRec), c_char_p, c_char_p, XIDProc, XPointer]
XConnectionWatchProc = CFUNCTYPE(None, POINTER(Display), XPointer, c_int, c_int, POINTER(XPointer))
XInternalConnectionNumbers = _lib.XInternalConnectionNumbers
XInternalConnectionNumbers.restype = c_int
XInternalConnectionNumbers.argtypes = [POINTER(Display), POINTER(POINTER(c_int)), POINTER(c_int)]
XProcessInternalConnection = _lib.XProcessInternalConnection
XProcessInternalConnection.restype = None
XProcessInternalConnection.argtypes = [POINTER(Display), c_int]
XAddConnectionWatch = _lib.XAddConnectionWatch
XAddConnectionWatch.restype = c_int
XAddConnectionWatch.argtypes = [POINTER(Display), XConnectionWatchProc, XPointer]
XRemoveConnectionWatch = _lib.XRemoveConnectionWatch
XRemoveConnectionWatch.restype = None
XRemoveConnectionWatch.argtypes = [POINTER(Display), XConnectionWatchProc, XPointer]
XSetAuthorization = _lib.XSetAuthorization
XSetAuthorization.restype = None
XSetAuthorization.argtypes = [c_char_p, c_int, c_char_p, c_int]
_Xmbtowc = _lib._Xmbtowc
_Xmbtowc.restype = c_int
_Xmbtowc.argtypes = [c_wchar_p, c_char_p, c_int]
_Xwctomb = _lib._Xwctomb
_Xwctomb.restype = c_int
_Xwctomb.argtypes = [c_char_p, c_wchar]
XGetEventData = _lib.XGetEventData
XGetEventData.restype = c_int
XGetEventData.argtypes = [POINTER(Display), POINTER(XGenericEventCookie)]
XFreeEventData = _lib.XFreeEventData
XFreeEventData.restype = None
XFreeEventData.argtypes = [POINTER(Display), POINTER(XGenericEventCookie)]
NoValue = 0
XValue = 1
YValue = 2
WidthValue = 4
HeightValue = 8
AllValues = 15
XNegative = 16
YNegative = 32

class struct_anon_95(Structure):
    __slots__ = [
     'flags', 
     'x', 
     'y', 
     'width', 
     'height', 
     'min_width', 
     'min_height', 
     'max_width', 
     'max_height', 
     'width_inc', 
     'height_inc', 
     'min_aspect', 
     'max_aspect', 
     'base_width', 
     'base_height', 
     'win_gravity']


class struct_anon_96(Structure):
    __slots__ = [
     'x',
     'y']


struct_anon_96._fields_ = [
 (
  'x', c_int),
 (
  'y', c_int)]

class struct_anon_97(Structure):
    __slots__ = [
     'x',
     'y']


struct_anon_97._fields_ = [
 (
  'x', c_int),
 (
  'y', c_int)]
struct_anon_95._fields_ = [
 (
  'flags', c_long),
 (
  'x', c_int),
 (
  'y', c_int),
 (
  'width', c_int),
 (
  'height', c_int),
 (
  'min_width', c_int),
 (
  'min_height', c_int),
 (
  'max_width', c_int),
 (
  'max_height', c_int),
 (
  'width_inc', c_int),
 (
  'height_inc', c_int),
 (
  'min_aspect', struct_anon_96),
 (
  'max_aspect', struct_anon_97),
 (
  'base_width', c_int),
 (
  'base_height', c_int),
 (
  'win_gravity', c_int)]
XSizeHints = struct_anon_95
USPosition = 1
USSize = 2
PPosition = 4
PSize = 8
PMinSize = 16
PMaxSize = 32
PResizeInc = 64
PAspect = 128
PBaseSize = 256
PWinGravity = 512
PAllHints = 252

class struct_anon_98(Structure):
    __slots__ = [
     'flags', 
     'input', 
     'initial_state', 
     'icon_pixmap', 
     'icon_window', 
     'icon_x', 
     'icon_y', 
     'icon_mask', 
     'window_group']


struct_anon_98._fields_ = [
 (
  'flags', c_long),
 (
  'input', c_int),
 (
  'initial_state', c_int),
 (
  'icon_pixmap', Pixmap),
 (
  'icon_window', Window),
 (
  'icon_x', c_int),
 (
  'icon_y', c_int),
 (
  'icon_mask', Pixmap),
 (
  'window_group', XID)]
XWMHints = struct_anon_98
InputHint = 1
StateHint = 2
IconPixmapHint = 4
IconWindowHint = 8
IconPositionHint = 16
IconMaskHint = 32
WindowGroupHint = 64
AllHints = 127
XUrgencyHint = 256
WithdrawnState = 0
NormalState = 1
IconicState = 3
DontCareState = 0
ZoomState = 2
InactiveState = 4

class struct_anon_99(Structure):
    __slots__ = [
     'value',
     'encoding',
     'format',
     'nitems']


struct_anon_99._fields_ = [
 (
  'value', POINTER(c_ubyte)),
 (
  'encoding', Atom),
 (
  'format', c_int),
 (
  'nitems', c_ulong)]
XTextProperty = struct_anon_99
XNoMemory = -1
XLocaleNotSupported = -2
XConverterNotFound = -3
enum_anon_100 = c_int
XStringStyle = 0
XCompoundTextStyle = 1
XTextStyle = 2
XStdICCTextStyle = 3
XUTF8StringStyle = 4
XICCEncodingStyle = enum_anon_100

class struct_anon_101(Structure):
    __slots__ = [
     'min_width', 
     'min_height', 
     'max_width', 
     'max_height', 
     'width_inc', 
     'height_inc']


struct_anon_101._fields_ = [
 (
  'min_width', c_int),
 (
  'min_height', c_int),
 (
  'max_width', c_int),
 (
  'max_height', c_int),
 (
  'width_inc', c_int),
 (
  'height_inc', c_int)]
XIconSize = struct_anon_101

class struct_anon_102(Structure):
    __slots__ = [
     'res_name',
     'res_class']


struct_anon_102._fields_ = [
 (
  'res_name', c_char_p),
 (
  'res_class', c_char_p)]
XClassHint = struct_anon_102

class struct__XComposeStatus(Structure):
    __slots__ = [
     'compose_ptr',
     'chars_matched']


struct__XComposeStatus._fields_ = [
 (
  'compose_ptr', XPointer),
 (
  'chars_matched', c_int)]
XComposeStatus = struct__XComposeStatus

class struct__XRegion(Structure):
    __slots__ = []


struct__XRegion._fields_ = [
 (
  '_opaque_struct', c_int)]

class struct__XRegion(Structure):
    __slots__ = []


struct__XRegion._fields_ = [
 (
  '_opaque_struct', c_int)]
Region = POINTER(struct__XRegion)
RectangleOut = 0
RectangleIn = 1
RectanglePart = 2

class struct_anon_103(Structure):
    __slots__ = [
     'visual', 
     'visualid', 
     'screen', 
     'depth', 
     'class', 
     'red_mask', 
     'green_mask', 
     'blue_mask', 
     'colormap_size', 
     'bits_per_rgb']


struct_anon_103._fields_ = [
 (
  'visual', POINTER(Visual)),
 (
  'visualid', VisualID),
 (
  'screen', c_int),
 (
  'depth', c_int),
 (
  'class', c_int),
 (
  'red_mask', c_ulong),
 (
  'green_mask', c_ulong),
 (
  'blue_mask', c_ulong),
 (
  'colormap_size', c_int),
 (
  'bits_per_rgb', c_int)]
XVisualInfo = struct_anon_103
VisualNoMask = 0
VisualIDMask = 1
VisualScreenMask = 2
VisualDepthMask = 4
VisualClassMask = 8
VisualRedMaskMask = 16
VisualGreenMaskMask = 32
VisualBlueMaskMask = 64
VisualColormapSizeMask = 128
VisualBitsPerRGBMask = 256
VisualAllMask = 511

class struct_anon_104(Structure):
    __slots__ = [
     'colormap', 
     'red_max', 
     'red_mult', 
     'green_max', 
     'green_mult', 
     'blue_max', 
     'blue_mult', 
     'base_pixel', 
     'visualid', 
     'killid']


struct_anon_104._fields_ = [
 (
  'colormap', Colormap),
 (
  'red_max', c_ulong),
 (
  'red_mult', c_ulong),
 (
  'green_max', c_ulong),
 (
  'green_mult', c_ulong),
 (
  'blue_max', c_ulong),
 (
  'blue_mult', c_ulong),
 (
  'base_pixel', c_ulong),
 (
  'visualid', VisualID),
 (
  'killid', XID)]
XStandardColormap = struct_anon_104
BitmapSuccess = 0
BitmapOpenFailed = 1
BitmapFileInvalid = 2
BitmapNoMemory = 3
XCSUCCESS = 0
XCNOMEM = 1
XCNOENT = 2
XContext = c_int
XAllocClassHint = _lib.XAllocClassHint
XAllocClassHint.restype = POINTER(XClassHint)
XAllocClassHint.argtypes = []
XAllocIconSize = _lib.XAllocIconSize
XAllocIconSize.restype = POINTER(XIconSize)
XAllocIconSize.argtypes = []
XAllocSizeHints = _lib.XAllocSizeHints
XAllocSizeHints.restype = POINTER(XSizeHints)
XAllocSizeHints.argtypes = []
XAllocStandardColormap = _lib.XAllocStandardColormap
XAllocStandardColormap.restype = POINTER(XStandardColormap)
XAllocStandardColormap.argtypes = []
XAllocWMHints = _lib.XAllocWMHints
XAllocWMHints.restype = POINTER(XWMHints)
XAllocWMHints.argtypes = []
XClipBox = _lib.XClipBox
XClipBox.restype = c_int
XClipBox.argtypes = [Region, POINTER(XRectangle)]
XCreateRegion = _lib.XCreateRegion
XCreateRegion.restype = Region
XCreateRegion.argtypes = []
XDefaultString = _lib.XDefaultString
XDefaultString.restype = c_char_p
XDefaultString.argtypes = []
XDeleteContext = _lib.XDeleteContext
XDeleteContext.restype = c_int
XDeleteContext.argtypes = [POINTER(Display), XID, XContext]
XDestroyRegion = _lib.XDestroyRegion
XDestroyRegion.restype = c_int
XDestroyRegion.argtypes = [Region]
XEmptyRegion = _lib.XEmptyRegion
XEmptyRegion.restype = c_int
XEmptyRegion.argtypes = [Region]
XEqualRegion = _lib.XEqualRegion
XEqualRegion.restype = c_int
XEqualRegion.argtypes = [Region, Region]
XFindContext = _lib.XFindContext
XFindContext.restype = c_int
XFindContext.argtypes = [POINTER(Display), XID, XContext, POINTER(XPointer)]
XGetClassHint = _lib.XGetClassHint
XGetClassHint.restype = c_int
XGetClassHint.argtypes = [POINTER(Display), Window, POINTER(XClassHint)]
XGetIconSizes = _lib.XGetIconSizes
XGetIconSizes.restype = c_int
XGetIconSizes.argtypes = [POINTER(Display), Window, POINTER(POINTER(XIconSize)), POINTER(c_int)]
XGetNormalHints = _lib.XGetNormalHints
XGetNormalHints.restype = c_int
XGetNormalHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints)]
XGetRGBColormaps = _lib.XGetRGBColormaps
XGetRGBColormaps.restype = c_int
XGetRGBColormaps.argtypes = [POINTER(Display), Window, POINTER(POINTER(XStandardColormap)), POINTER(c_int), Atom]
XGetSizeHints = _lib.XGetSizeHints
XGetSizeHints.restype = c_int
XGetSizeHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints), Atom]
XGetStandardColormap = _lib.XGetStandardColormap
XGetStandardColormap.restype = c_int
XGetStandardColormap.argtypes = [POINTER(Display), Window, POINTER(XStandardColormap), Atom]
XGetTextProperty = _lib.XGetTextProperty
XGetTextProperty.restype = c_int
XGetTextProperty.argtypes = [POINTER(Display), Window, POINTER(XTextProperty), Atom]
XGetVisualInfo = _lib.XGetVisualInfo
XGetVisualInfo.restype = POINTER(XVisualInfo)
XGetVisualInfo.argtypes = [POINTER(Display), c_long, POINTER(XVisualInfo), POINTER(c_int)]
XGetWMClientMachine = _lib.XGetWMClientMachine
XGetWMClientMachine.restype = c_int
XGetWMClientMachine.argtypes = [POINTER(Display), Window, POINTER(XTextProperty)]
XGetWMHints = _lib.XGetWMHints
XGetWMHints.restype = POINTER(XWMHints)
XGetWMHints.argtypes = [POINTER(Display), Window]
XGetWMIconName = _lib.XGetWMIconName
XGetWMIconName.restype = c_int
XGetWMIconName.argtypes = [POINTER(Display), Window, POINTER(XTextProperty)]
XGetWMName = _lib.XGetWMName
XGetWMName.restype = c_int
XGetWMName.argtypes = [POINTER(Display), Window, POINTER(XTextProperty)]
XGetWMNormalHints = _lib.XGetWMNormalHints
XGetWMNormalHints.restype = c_int
XGetWMNormalHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints), POINTER(c_long)]
XGetWMSizeHints = _lib.XGetWMSizeHints
XGetWMSizeHints.restype = c_int
XGetWMSizeHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints), POINTER(c_long), Atom]
XGetZoomHints = _lib.XGetZoomHints
XGetZoomHints.restype = c_int
XGetZoomHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints)]
XIntersectRegion = _lib.XIntersectRegion
XIntersectRegion.restype = c_int
XIntersectRegion.argtypes = [Region, Region, Region]
XConvertCase = _lib.XConvertCase
XConvertCase.restype = None
XConvertCase.argtypes = [KeySym, POINTER(KeySym), POINTER(KeySym)]
XLookupString = _lib.XLookupString
XLookupString.restype = c_int
XLookupString.argtypes = [POINTER(XKeyEvent), c_char_p, c_int, POINTER(KeySym), POINTER(XComposeStatus)]
XMatchVisualInfo = _lib.XMatchVisualInfo
XMatchVisualInfo.restype = c_int
XMatchVisualInfo.argtypes = [POINTER(Display), c_int, c_int, c_int, POINTER(XVisualInfo)]
XOffsetRegion = _lib.XOffsetRegion
XOffsetRegion.restype = c_int
XOffsetRegion.argtypes = [Region, c_int, c_int]
XPointInRegion = _lib.XPointInRegion
XPointInRegion.restype = c_int
XPointInRegion.argtypes = [Region, c_int, c_int]
XPolygonRegion = _lib.XPolygonRegion
XPolygonRegion.restype = Region
XPolygonRegion.argtypes = [POINTER(XPoint), c_int, c_int]
XRectInRegion = _lib.XRectInRegion
XRectInRegion.restype = c_int
XRectInRegion.argtypes = [Region, c_int, c_int, c_uint, c_uint]
XSaveContext = _lib.XSaveContext
XSaveContext.restype = c_int
XSaveContext.argtypes = [POINTER(Display), XID, XContext, c_char_p]
XSetClassHint = _lib.XSetClassHint
XSetClassHint.restype = c_int
XSetClassHint.argtypes = [POINTER(Display), Window, POINTER(XClassHint)]
XSetIconSizes = _lib.XSetIconSizes
XSetIconSizes.restype = c_int
XSetIconSizes.argtypes = [POINTER(Display), Window, POINTER(XIconSize), c_int]
XSetNormalHints = _lib.XSetNormalHints
XSetNormalHints.restype = c_int
XSetNormalHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints)]
XSetRGBColormaps = _lib.XSetRGBColormaps
XSetRGBColormaps.restype = None
XSetRGBColormaps.argtypes = [POINTER(Display), Window, POINTER(XStandardColormap), c_int, Atom]
XSetSizeHints = _lib.XSetSizeHints
XSetSizeHints.restype = c_int
XSetSizeHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints), Atom]
XSetStandardProperties = _lib.XSetStandardProperties
XSetStandardProperties.restype = c_int
XSetStandardProperties.argtypes = [POINTER(Display), Window, c_char_p, c_char_p, Pixmap, POINTER(c_char_p), c_int, POINTER(XSizeHints)]
XSetTextProperty = _lib.XSetTextProperty
XSetTextProperty.restype = None
XSetTextProperty.argtypes = [POINTER(Display), Window, POINTER(XTextProperty), Atom]
XSetWMClientMachine = _lib.XSetWMClientMachine
XSetWMClientMachine.restype = None
XSetWMClientMachine.argtypes = [POINTER(Display), Window, POINTER(XTextProperty)]
XSetWMHints = _lib.XSetWMHints
XSetWMHints.restype = c_int
XSetWMHints.argtypes = [POINTER(Display), Window, POINTER(XWMHints)]
XSetWMIconName = _lib.XSetWMIconName
XSetWMIconName.restype = None
XSetWMIconName.argtypes = [POINTER(Display), Window, POINTER(XTextProperty)]
XSetWMName = _lib.XSetWMName
XSetWMName.restype = None
XSetWMName.argtypes = [POINTER(Display), Window, POINTER(XTextProperty)]
XSetWMNormalHints = _lib.XSetWMNormalHints
XSetWMNormalHints.restype = None
XSetWMNormalHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints)]
XSetWMProperties = _lib.XSetWMProperties
XSetWMProperties.restype = None
XSetWMProperties.argtypes = [POINTER(Display), Window, POINTER(XTextProperty), POINTER(XTextProperty), POINTER(c_char_p), c_int, POINTER(XSizeHints), POINTER(XWMHints), POINTER(XClassHint)]
XmbSetWMProperties = _lib.XmbSetWMProperties
XmbSetWMProperties.restype = None
XmbSetWMProperties.argtypes = [POINTER(Display), Window, c_char_p, c_char_p, POINTER(c_char_p), c_int, POINTER(XSizeHints), POINTER(XWMHints), POINTER(XClassHint)]
Xutf8SetWMProperties = _lib.Xutf8SetWMProperties
Xutf8SetWMProperties.restype = None
Xutf8SetWMProperties.argtypes = [POINTER(Display), Window, c_char_p, c_char_p, POINTER(c_char_p), c_int, POINTER(XSizeHints), POINTER(XWMHints), POINTER(XClassHint)]
XSetWMSizeHints = _lib.XSetWMSizeHints
XSetWMSizeHints.restype = None
XSetWMSizeHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints), Atom]
XSetRegion = _lib.XSetRegion
XSetRegion.restype = c_int
XSetRegion.argtypes = [POINTER(Display), GC, Region]
XSetStandardColormap = _lib.XSetStandardColormap
XSetStandardColormap.restype = None
XSetStandardColormap.argtypes = [POINTER(Display), Window, POINTER(XStandardColormap), Atom]
XSetZoomHints = _lib.XSetZoomHints
XSetZoomHints.restype = c_int
XSetZoomHints.argtypes = [POINTER(Display), Window, POINTER(XSizeHints)]
XShrinkRegion = _lib.XShrinkRegion
XShrinkRegion.restype = c_int
XShrinkRegion.argtypes = [Region, c_int, c_int]
XStringListToTextProperty = _lib.XStringListToTextProperty
XStringListToTextProperty.restype = c_int
XStringListToTextProperty.argtypes = [POINTER(c_char_p), c_int, POINTER(XTextProperty)]
XSubtractRegion = _lib.XSubtractRegion
XSubtractRegion.restype = c_int
XSubtractRegion.argtypes = [Region, Region, Region]
XmbTextListToTextProperty = _lib.XmbTextListToTextProperty
XmbTextListToTextProperty.restype = c_int
XmbTextListToTextProperty.argtypes = [POINTER(Display), POINTER(c_char_p), c_int, XICCEncodingStyle, POINTER(XTextProperty)]
XwcTextListToTextProperty = _lib.XwcTextListToTextProperty
XwcTextListToTextProperty.restype = c_int
XwcTextListToTextProperty.argtypes = [POINTER(Display), POINTER(c_wchar_p), c_int, XICCEncodingStyle, POINTER(XTextProperty)]
Xutf8TextListToTextProperty = _lib.Xutf8TextListToTextProperty
Xutf8TextListToTextProperty.restype = c_int
Xutf8TextListToTextProperty.argtypes = [POINTER(Display), POINTER(c_char_p), c_int, XICCEncodingStyle, POINTER(XTextProperty)]
XwcFreeStringList = _lib.XwcFreeStringList
XwcFreeStringList.restype = None
XwcFreeStringList.argtypes = [POINTER(c_wchar_p)]
XTextPropertyToStringList = _lib.XTextPropertyToStringList
XTextPropertyToStringList.restype = c_int
XTextPropertyToStringList.argtypes = [POINTER(XTextProperty), POINTER(POINTER(c_char_p)), POINTER(c_int)]
XmbTextPropertyToTextList = _lib.XmbTextPropertyToTextList
XmbTextPropertyToTextList.restype = c_int
XmbTextPropertyToTextList.argtypes = [POINTER(Display), POINTER(XTextProperty), POINTER(POINTER(c_char_p)), POINTER(c_int)]
XwcTextPropertyToTextList = _lib.XwcTextPropertyToTextList
XwcTextPropertyToTextList.restype = c_int
XwcTextPropertyToTextList.argtypes = [POINTER(Display), POINTER(XTextProperty), POINTER(POINTER(c_wchar_p)), POINTER(c_int)]
Xutf8TextPropertyToTextList = _lib.Xutf8TextPropertyToTextList
Xutf8TextPropertyToTextList.restype = c_int
Xutf8TextPropertyToTextList.argtypes = [POINTER(Display), POINTER(XTextProperty), POINTER(POINTER(c_char_p)), POINTER(c_int)]
XUnionRectWithRegion = _lib.XUnionRectWithRegion
XUnionRectWithRegion.restype = c_int
XUnionRectWithRegion.argtypes = [POINTER(XRectangle), Region, Region]
XUnionRegion = _lib.XUnionRegion
XUnionRegion.restype = c_int
XUnionRegion.argtypes = [Region, Region, Region]
XWMGeometry = _lib.XWMGeometry
XWMGeometry.restype = c_int
XWMGeometry.argtypes = [POINTER(Display), c_int, c_char_p, c_char_p, c_uint, POINTER(XSizeHints), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
XXorRegion = _lib.XXorRegion
XXorRegion.restype = c_int
XXorRegion.argtypes = [Region, Region, Region]
__all__ = [
 'XlibSpecificationRelease', 'X_PROTOCOL', 'X_PROTOCOL_REVISION', 
 'XID', 
 'Mask', 'Atom', 'VisualID', 'Time', 'Window', 'Drawable', 'Font', 
 'Pixmap', 
 'Cursor', 'Colormap', 'GContext', 'KeySym', 'KeyCode', 'None_', 
 'ParentRelative', 
 'CopyFromParent', 'PointerWindow', 'InputFocus', 
 'PointerRoot', 'AnyPropertyType', 
 'AnyKey', 'AnyButton', 'AllTemporary', 
 'CurrentTime', 'NoSymbol', 'NoEventMask', 
 'KeyPressMask', 'KeyReleaseMask', 
 'ButtonPressMask', 'ButtonReleaseMask', 
 'EnterWindowMask', 'LeaveWindowMask', 
 'PointerMotionMask', 'PointerMotionHintMask', 
 'Button1MotionMask', 
 'Button2MotionMask', 'Button3MotionMask', 'Button4MotionMask', 
 'Button5MotionMask', 
 'ButtonMotionMask', 'KeymapStateMask', 'ExposureMask', 
 'VisibilityChangeMask', 
 'StructureNotifyMask', 'ResizeRedirectMask', 
 'SubstructureNotifyMask', 'SubstructureRedirectMask', 
 'FocusChangeMask', 
 'PropertyChangeMask', 'ColormapChangeMask', 'OwnerGrabButtonMask', 
 'KeyPress', 
 'KeyRelease', 'ButtonPress', 'ButtonRelease', 'MotionNotify', 
 'EnterNotify', 
 'LeaveNotify', 'FocusIn', 'FocusOut', 'KeymapNotify', 'Expose', 
 'GraphicsExpose', 
 'NoExpose', 'VisibilityNotify', 'CreateNotify', 
 'DestroyNotify', 'UnmapNotify', 
 'MapNotify', 'MapRequest', 'ReparentNotify', 
 'ConfigureNotify', 'ConfigureRequest', 
 'GravityNotify', 'ResizeRequest', 
 'CirculateNotify', 'CirculateRequest', 
 'PropertyNotify', 'SelectionClear', 
 'SelectionRequest', 'SelectionNotify', 
 'ColormapNotify', 'ClientMessage', 
 'MappingNotify', 'GenericEvent', 'LASTEvent', 
 'ShiftMask', 'LockMask', 
 'ControlMask', 'Mod1Mask', 'Mod2Mask', 'Mod3Mask', 
 'Mod4Mask', 'Mod5Mask', 
 'ShiftMapIndex', 'LockMapIndex', 'ControlMapIndex', 
 'Mod1MapIndex', 
 'Mod2MapIndex', 'Mod3MapIndex', 'Mod4MapIndex', 'Mod5MapIndex', 
 'Button1Mask', 
 'Button2Mask', 'Button3Mask', 'Button4Mask', 'Button5Mask', 
 'AnyModifier', 
 'Button1', 'Button2', 'Button3', 'Button4', 'Button5', 
 'NotifyNormal', 
 'NotifyGrab', 'NotifyUngrab', 'NotifyWhileGrabbed', 'NotifyHint', 
 'NotifyAncestor', 
 'NotifyVirtual', 'NotifyInferior', 'NotifyNonlinear', 
 'NotifyNonlinearVirtual', 
 'NotifyPointer', 'NotifyPointerRoot', 
 'NotifyDetailNone', 'VisibilityUnobscured', 
 'VisibilityPartiallyObscured', 
 'VisibilityFullyObscured', 'PlaceOnTop', 
 'PlaceOnBottom', 'FamilyInternet', 
 'FamilyDECnet', 'FamilyChaos', 'FamilyInternet6', 
 'FamilyServerInterpreted', 
 'PropertyNewValue', 'PropertyDelete', 'ColormapUninstalled', 
 'ColormapInstalled', 
 'GrabModeSync', 'GrabModeAsync', 'GrabSuccess', 
 'AlreadyGrabbed', 'GrabInvalidTime', 
 'GrabNotViewable', 'GrabFrozen', 
 'AsyncPointer', 'SyncPointer', 'ReplayPointer', 
 'AsyncKeyboard', 
 'SyncKeyboard', 'ReplayKeyboard', 'AsyncBoth', 'SyncBoth', 
 'RevertToParent', 
 'Success', 'BadRequest', 'BadValue', 'BadWindow', 'BadPixmap', 
 'BadAtom', 
 'BadCursor', 'BadFont', 'BadMatch', 'BadDrawable', 'BadAccess', 
 'BadAlloc', 
 'BadColor', 'BadGC', 'BadIDChoice', 'BadName', 'BadLength', 
 'BadImplementation', 
 'FirstExtensionError', 'LastExtensionError', 
 'InputOutput', 'InputOnly', 
 'CWBackPixmap', 'CWBackPixel', 'CWBorderPixmap', 
 'CWBorderPixel', 'CWBitGravity', 
 'CWWinGravity', 'CWBackingStore', 
 'CWBackingPlanes', 'CWBackingPixel', 
 'CWOverrideRedirect', 'CWSaveUnder', 
 'CWEventMask', 'CWDontPropagate', 
 'CWColormap', 'CWCursor', 'CWX', 'CWY', 
 'CWWidth', 'CWHeight', 'CWBorderWidth', 
 'CWSibling', 'CWStackMode', 
 'ForgetGravity', 'NorthWestGravity', 'NorthGravity', 
 'NorthEastGravity', 
 'WestGravity', 'CenterGravity', 'EastGravity', 'SouthWestGravity', 
 'SouthGravity', 
 'SouthEastGravity', 'StaticGravity', 'UnmapGravity', 
 'NotUseful', 'WhenMapped', 
 'Always', 'IsUnmapped', 'IsUnviewable', 
 'IsViewable', 'SetModeInsert', 
 'SetModeDelete', 'DestroyAll', 
 'RetainPermanent', 'RetainTemporary', 'Above', 
 'Below', 'TopIf', 'BottomIf', 
 'Opposite', 'RaiseLowest', 'LowerHighest', 
 'PropModeReplace', 
 'PropModePrepend', 'PropModeAppend', 'GXclear', 'GXand', 
 'GXandReverse', 
 'GXcopy', 'GXandInverted', 'GXnoop', 'GXxor', 'GXor', 
 'GXnor', 'GXequiv', 
 'GXinvert', 'GXorReverse', 'GXcopyInverted', 'GXorInverted', 
 'GXnand', 
 'GXset', 'LineSolid', 'LineOnOffDash', 'LineDoubleDash', 'CapNotLast', 
 'CapButt', 
 'CapRound', 'CapProjecting', 'JoinMiter', 'JoinRound', 'JoinBevel', 
 'FillSolid', 
 'FillTiled', 'FillStippled', 'FillOpaqueStippled', 'EvenOddRule', 
 'WindingRule', 
 'ClipByChildren', 'IncludeInferiors', 'Unsorted', 'YSorted', 
 'YXSorted', 
 'YXBanded', 'CoordModeOrigin', 'CoordModePrevious', 'Complex', 
 'Nonconvex', 
 'Convex', 'ArcChord', 'ArcPieSlice', 'GCFunction', 'GCPlaneMask', 
 'GCForeground', 
 'GCBackground', 'GCLineWidth', 'GCLineStyle', 'GCCapStyle', 
 'GCJoinStyle', 
 'GCFillStyle', 'GCFillRule', 'GCTile', 'GCStipple', 
 'GCTileStipXOrigin', 
 'GCTileStipYOrigin', 'GCFont', 'GCSubwindowMode', 
 'GCGraphicsExposures', 
 'GCClipXOrigin', 'GCClipYOrigin', 'GCClipMask', 
 'GCDashOffset', 'GCDashList', 
 'GCArcMode', 'GCLastBit', 'FontLeftToRight', 
 'FontRightToLeft', 'FontChange', 
 'XYBitmap', 'XYPixmap', 'ZPixmap', 
 'AllocNone', 'AllocAll', 'DoRed', 
 'DoGreen', 'DoBlue', 'CursorShape', 
 'TileShape', 'StippleShape', 'AutoRepeatModeOff', 
 'AutoRepeatModeOn', 
 'AutoRepeatModeDefault', 'LedModeOff', 'LedModeOn', 
 'KBKeyClickPercent', 
 'KBBellPercent', 'KBBellPitch', 'KBBellDuration', 
 'KBLed', 'KBLedMode', 
 'KBKey', 'KBAutoRepeatMode', 'MappingSuccess', 'MappingBusy', 
 'MappingFailed', 
 'MappingModifier', 'MappingKeyboard', 'MappingPointer', 
 'DontPreferBlanking', 
 'PreferBlanking', 'DefaultBlanking', 'DisableScreenSaver', 
 'DisableScreenInterval', 
 'DontAllowExposures', 'AllowExposures', 
 'DefaultExposures', 'ScreenSaverReset', 
 'ScreenSaverActive', 'HostInsert', 
 'HostDelete', 'EnableAccess', 'DisableAccess', 
 'StaticGray', 'GrayScale', 
 'StaticColor', 'PseudoColor', 'TrueColor', 
 'DirectColor', 'LSBFirst', 
 'MSBFirst', '_Xmblen', 'X_HAVE_UTF8_STRING', 
 'XPointer', 'Bool', 'Status', 
 'True_', 'False_', 'QueuedAlready', 'QueuedAfterReading', 
 'QueuedAfterFlush', 
 'XExtData', 'XExtCodes', 'XPixmapFormatValues', 'XGCValues', 
 'GC', 'Visual', 
 'Depth', 'Screen', 'ScreenFormat', 'XSetWindowAttributes', 
 'XWindowAttributes', 
 'XHostAddress', 'XServerInterpretedAddress', 'XImage', 
 'XWindowChanges', 
 'XColor', 'XSegment', 'XPoint', 'XRectangle', 'XArc', 
 'XKeyboardControl', 
 'XKeyboardState', 'XTimeCoord', 'XModifierKeymap', 
 'Display', '_XPrivDisplay', 
 'XKeyEvent', 'XKeyPressedEvent', 
 'XKeyReleasedEvent', 'XButtonEvent', 'XButtonPressedEvent', 
 'XButtonReleasedEvent', 
 'XMotionEvent', 'XPointerMovedEvent', 
 'XCrossingEvent', 'XEnterWindowEvent', 
 'XLeaveWindowEvent', 
 'XFocusChangeEvent', 'XFocusInEvent', 'XFocusOutEvent', 
 'XKeymapEvent', 
 'XExposeEvent', 'XGraphicsExposeEvent', 'XNoExposeEvent', 
 'XVisibilityEvent', 
 'XCreateWindowEvent', 'XDestroyWindowEvent', 'XUnmapEvent', 
 'XMapEvent', 
 'XMapRequestEvent', 'XReparentEvent', 'XConfigureEvent', 'XGravityEvent', 
 'XResizeRequestEvent', 
 'XConfigureRequestEvent', 'XCirculateEvent', 
 'XCirculateRequestEvent', 'XPropertyEvent', 
 'XSelectionClearEvent', 
 'XSelectionRequestEvent', 'XSelectionEvent', 'XColormapEvent', 
 'XClientMessageEvent', 
 'XMappingEvent', 'XErrorEvent', 'XAnyEvent', 
 'XGenericEvent', 'XGenericEventCookie', 
 'XEvent', 'XCharStruct', 'XFontProp', 
 'XFontStruct', 'XTextItem', 'XChar2b', 
 'XTextItem16', 'XEDataObject', 
 'XFontSetExtents', 'XOM', 'XOC', 'XFontSet', 
 'XmbTextItem', 'XwcTextItem', 
 'XOMCharSetList', 'XOrientation', 'XOMOrientation_LTR_TTB', 
 'XOMOrientation_RTL_TTB', 
 'XOMOrientation_TTB_LTR', 'XOMOrientation_TTB_RTL', 
 'XOMOrientation_Context', 
 'XOMOrientation', 'XOMFontInfo', 'XIM', 'XIC', 
 'XIMProc', 'XICProc', 
 'XIDProc', 'XIMStyle', 'XIMStyles', 'XIMPreeditArea', 
 'XIMPreeditCallbacks', 
 'XIMPreeditPosition', 'XIMPreeditNothing', 
 'XIMPreeditNone', 'XIMStatusArea', 
 'XIMStatusCallbacks', 'XIMStatusNothing', 
 'XIMStatusNone', 'XBufferOverflow', 
 'XLookupNone', 'XLookupChars', 
 'XLookupKeySym', 'XLookupBoth', 'XVaNestedList', 
 'XIMCallback', 'XICCallback', 
 'XIMFeedback', 'XIMReverse', 'XIMUnderline', 
 'XIMHighlight', 'XIMPrimary', 
 'XIMSecondary', 'XIMTertiary', 'XIMVisibleToForward', 
 'XIMVisibleToBackword', 
 'XIMVisibleToCenter', 'XIMText', 'XIMPreeditState', 
 'XIMPreeditUnKnown', 
 'XIMPreeditEnable', 'XIMPreeditDisable', 
 'XIMPreeditStateNotifyCallbackStruct', 
 'XIMResetState', 'XIMInitialState', 
 'XIMPreserveState', 'XIMStringConversionFeedback', 
 'XIMStringConversionLeftEdge', 
 'XIMStringConversionRightEdge', 
 'XIMStringConversionTopEdge', 'XIMStringConversionBottomEdge', 
 'XIMStringConversionConcealed', 
 'XIMStringConversionWrapped', 
 'XIMStringConversionText', 'XIMStringConversionPosition', 
 'XIMStringConversionType', 
 'XIMStringConversionBuffer', 
 'XIMStringConversionLine', 'XIMStringConversionWord', 
 'XIMStringConversionChar', 
 'XIMStringConversionOperation', 
 'XIMStringConversionSubstitution', 'XIMStringConversionRetrieval', 
 'XIMCaretDirection', 
 'XIMForwardChar', 'XIMBackwardChar', 'XIMForwardWord', 
 'XIMBackwardWord', 
 'XIMCaretUp', 'XIMCaretDown', 'XIMNextLine', 
 'XIMPreviousLine', 'XIMLineStart', 
 'XIMLineEnd', 'XIMAbsolutePosition', 
 'XIMDontChange', 'XIMStringConversionCallbackStruct', 
 'XIMPreeditDrawCallbackStruct', 
 'XIMCaretStyle', 'XIMIsInvisible', 
 'XIMIsPrimary', 'XIMIsSecondary', 'XIMPreeditCaretCallbackStruct', 
 'XIMStatusDataType', 
 'XIMTextType', 'XIMBitmapType', 
 'XIMStatusDrawCallbackStruct', 'XIMHotKeyTrigger', 
 'XIMHotKeyTriggers', 
 'XIMHotKeyState', 'XIMHotKeyStateON', 'XIMHotKeyStateOFF', 
 'XIMValuesList', 
 'XLoadQueryFont', 'XQueryFont', 'XGetMotionEvents', 'XDeleteModifiermapEntry', 
 'XGetModifierMapping', 
 'XInsertModifiermapEntry', 'XNewModifiermap', 
 'XCreateImage', 'XInitImage', 
 'XGetImage', 'XGetSubImage', 'XOpenDisplay', 
 'XrmInitialize', 'XFetchBytes', 
 'XFetchBuffer', 'XGetAtomName', 
 'XGetAtomNames', 'XGetDefault', 'XDisplayName', 
 'XKeysymToString', 
 'XSynchronize', 'XSetAfterFunction', 'XInternAtom', 
 'XInternAtoms', 
 'XCopyColormapAndFree', 'XCreateColormap', 'XCreatePixmapCursor', 
 'XCreateGlyphCursor', 
 'XCreateFontCursor', 'XLoadFont', 'XCreateGC', 
 'XGContextFromGC', 'XFlushGC', 
 'XCreatePixmap', 'XCreateBitmapFromData', 
 'XCreatePixmapFromBitmapData', 
 'XCreateSimpleWindow', 'XGetSelectionOwner', 
 'XCreateWindow', 'XListInstalledColormaps', 
 'XListFonts', 
 'XListFontsWithInfo', 'XGetFontPath', 'XListExtensions', 
 'XListProperties', 
 'XListHosts', 'XKeycodeToKeysym', 'XLookupKeysym', 'XGetKeyboardMapping', 
 'XStringToKeysym', 
 'XMaxRequestSize', 'XExtendedMaxRequestSize', 
 'XResourceManagerString', 
 'XScreenResourceString', 'XDisplayMotionBufferSize', 
 'XVisualIDFromVisual', 
 'XInitThreads', 'XLockDisplay', 'XUnlockDisplay', 
 'XInitExtension', 'XAddExtension', 
 'XFindOnExtensionList', 
 'XEHeadOfExtensionList', 'XRootWindow', 'XDefaultRootWindow', 
 'XRootWindowOfScreen', 
 'XDefaultVisual', 'XDefaultVisualOfScreen', 
 'XDefaultGC', 'XDefaultGCOfScreen', 
 'XBlackPixel', 'XWhitePixel', 
 'XAllPlanes', 'XBlackPixelOfScreen', 'XWhitePixelOfScreen', 
 'XNextRequest', 
 'XLastKnownRequestProcessed', 'XServerVendor', 'XDisplayString', 
 'XDefaultColormap', 
 'XDefaultColormapOfScreen', 'XDisplayOfScreen', 
 'XScreenOfDisplay', 'XDefaultScreenOfDisplay', 
 'XEventMaskOfScreen', 
 'XScreenNumberOfScreen', 'XErrorHandler', 'XSetErrorHandler', 
 'XIOErrorHandler', 
 'XSetIOErrorHandler', 'XListPixmapFormats', 'XListDepths', 
 'XReconfigureWMWindow', 
 'XGetWMProtocols', 'XSetWMProtocols', 
 'XIconifyWindow', 'XWithdrawWindow', 
 'XGetCommand', 'XGetWMColormapWindows', 
 'XSetWMColormapWindows', 'XFreeStringList', 
 'XSetTransientForHint', 
 'XActivateScreenSaver', 'XAddHost', 'XAddHosts', 
 'XAddToExtensionList', 
 'XAddToSaveSet', 'XAllocColor', 'XAllocColorCells', 
 'XAllocColorPlanes', 
 'XAllocNamedColor', 'XAllowEvents', 'XAutoRepeatOff', 
 'XAutoRepeatOn', 
 'XBell', 'XBitmapBitOrder', 'XBitmapPad', 'XBitmapUnit', 
 'XCellsOfScreen', 
 'XChangeActivePointerGrab', 'XChangeGC', 'XChangeKeyboardControl', 
 'XChangeKeyboardMapping', 
 'XChangePointerControl', 'XChangeProperty', 
 'XChangeSaveSet', 'XChangeWindowAttributes', 
 'XCheckIfEvent', 
 'XCheckMaskEvent', 'XCheckTypedEvent', 'XCheckTypedWindowEvent', 
 'XCheckWindowEvent', 
 'XCirculateSubwindows', 'XCirculateSubwindowsDown', 
 'XCirculateSubwindowsUp', 
 'XClearArea', 'XClearWindow', 'XCloseDisplay', 
 'XConfigureWindow', 'XConnectionNumber', 
 'XConvertSelection', 'XCopyArea', 
 'XCopyGC', 'XCopyPlane', 'XDefaultDepth', 
 'XDefaultDepthOfScreen', 
 'XDefaultScreen', 'XDefineCursor', 'XDeleteProperty', 
 'XDestroyWindow', 
 'XDestroySubwindows', 'XDoesBackingStore', 'XDoesSaveUnders', 
 'XDisableAccessControl', 
 'XDisplayCells', 'XDisplayHeight', 
 'XDisplayHeightMM', 'XDisplayKeycodes', 
 'XDisplayPlanes', 'XDisplayWidth', 
 'XDisplayWidthMM', 'XDrawArc', 'XDrawArcs', 
 'XDrawImageString', 
 'XDrawImageString16', 'XDrawLine', 'XDrawLines', 'XDrawPoint', 
 'XDrawPoints', 
 'XDrawRectangle', 'XDrawRectangles', 'XDrawSegments', 'XDrawString', 
 'XDrawString16', 
 'XDrawText', 'XDrawText16', 'XEnableAccessControl', 
 'XEventsQueued', 'XFetchName', 
 'XFillArc', 'XFillArcs', 'XFillPolygon', 
 'XFillRectangle', 'XFillRectangles', 
 'XFlush', 'XForceScreenSaver', 'XFree', 
 'XFreeColormap', 'XFreeColors', 
 'XFreeCursor', 'XFreeExtensionList', 
 'XFreeFont', 'XFreeFontInfo', 'XFreeFontNames', 
 'XFreeFontPath', 'XFreeGC', 
 'XFreeModifiermap', 'XFreePixmap', 'XGeometry', 
 'XGetErrorDatabaseText', 
 'XGetErrorText', 'XGetFontProperty', 'XGetGCValues', 
 'XGetGeometry', 
 'XGetIconName', 'XGetInputFocus', 'XGetKeyboardControl', 
 'XGetPointerControl', 
 'XGetPointerMapping', 'XGetScreenSaver', 'XGetTransientForHint', 
 'XGetWindowProperty', 
 'XGetWindowAttributes', 'XGrabButton', 'XGrabKey', 
 'XGrabKeyboard', 'XGrabPointer', 
 'XGrabServer', 'XHeightMMOfScreen', 
 'XHeightOfScreen', 'XIfEvent', 'XImageByteOrder', 
 'XInstallColormap', 
 'XKeysymToKeycode', 'XKillClient', 'XLookupColor', 
 'XLowerWindow', 
 'XMapRaised', 'XMapSubwindows', 'XMapWindow', 'XMaskEvent', 
 'XMaxCmapsOfScreen', 
 'XMinCmapsOfScreen', 'XMoveResizeWindow', 'XMoveWindow', 
 'XNextEvent', 
 'XNoOp', 'XParseColor', 'XParseGeometry', 'XPeekEvent', 
 'XPeekIfEvent', 
 'XPending', 'XPlanesOfScreen', 'XProtocolRevision', 
 'XProtocolVersion', 
 'XPutBackEvent', 'XPutImage', 'XQLength', 
 'XQueryBestCursor', 'XQueryBestSize', 
 'XQueryBestStipple', 'XQueryBestTile', 
 'XQueryColor', 'XQueryColors', 'XQueryExtension', 
 'XQueryKeymap', 
 'XQueryPointer', 'XQueryTextExtents', 'XQueryTextExtents16', 
 'XQueryTree', 
 'XRaiseWindow', 'XReadBitmapFile', 'XReadBitmapFileData', 
 'XRebindKeysym', 
 'XRecolorCursor', 'XRefreshKeyboardMapping', 'XRemoveFromSaveSet', 
 'XRemoveHost', 
 'XRemoveHosts', 'XReparentWindow', 'XResetScreenSaver', 
 'XResizeWindow', 
 'XRestackWindows', 'XRotateBuffers', 
 'XRotateWindowProperties', 'XScreenCount', 
 'XSelectInput', 'XSendEvent', 
 'XSetAccessControl', 'XSetArcMode', 'XSetBackground', 
 'XSetClipMask', 
 'XSetClipOrigin', 'XSetClipRectangles', 'XSetCloseDownMode', 
 'XSetCommand', 
 'XSetDashes', 'XSetFillRule', 'XSetFillStyle', 'XSetFont', 
 'XSetFontPath', 
 'XSetForeground', 'XSetFunction', 'XSetGraphicsExposures', 
 'XSetIconName', 
 'XSetInputFocus', 'XSetLineAttributes', 'XSetModifierMapping', 
 'XSetPlaneMask', 
 'XSetPointerMapping', 'XSetScreenSaver', 
 'XSetSelectionOwner', 'XSetState', 
 'XSetStipple', 'XSetSubwindowMode', 
 'XSetTSOrigin', 'XSetTile', 'XSetWindowBackground', 
 'XSetWindowBackgroundPixmap', 
 'XSetWindowBorder', 'XSetWindowBorderPixmap', 
 'XSetWindowBorderWidth', 'XSetWindowColormap', 
 'XStoreBuffer', 'XStoreBytes', 
 'XStoreColor', 'XStoreColors', 'XStoreName', 
 'XStoreNamedColor', 'XSync', 
 'XTextExtents', 'XTextExtents16', 'XTextWidth', 
 'XTextWidth16', 
 'XTranslateCoordinates', 'XUndefineCursor', 'XUngrabButton', 
 'XUngrabKey', 
 'XUngrabKeyboard', 'XUngrabPointer', 'XUngrabServer', 'XUninstallColormap', 
 'XUnloadFont', 
 'XUnmapSubwindows', 'XUnmapWindow', 'XVendorRelease', 
 'XWarpPointer', 'XWidthMMOfScreen', 
 'XWidthOfScreen', 'XWindowEvent', 
 'XWriteBitmapFile', 'XSupportsLocale', 
 'XSetLocaleModifiers', 'XOpenOM', 
 'XCloseOM', 'XSetOMValues', 'XGetOMValues', 
 'XDisplayOfOM', 'XLocaleOfOM', 
 'XCreateOC', 'XDestroyOC', 'XOMOfOC', 'XSetOCValues', 
 'XGetOCValues', 
 'XCreateFontSet', 'XFreeFontSet', 'XFontsOfFontSet', 
 'XBaseFontNameListOfFontSet', 
 'XLocaleOfFontSet', 'XContextDependentDrawing', 
 'XDirectionalDependentDrawing', 
 'XContextualDrawing', 'XExtentsOfFontSet', 
 'XmbTextEscapement', 'XwcTextEscapement', 
 'Xutf8TextEscapement', 
 'XmbTextExtents', 'XwcTextExtents', 'Xutf8TextExtents', 
 'XmbTextPerCharExtents', 
 'XwcTextPerCharExtents', 'Xutf8TextPerCharExtents', 
 'XmbDrawText', 'XwcDrawText', 
 'Xutf8DrawText', 'XmbDrawString', 
 'XwcDrawString', 'Xutf8DrawString', 'XmbDrawImageString', 
 'XwcDrawImageString', 
 'Xutf8DrawImageString', 'XOpenIM', 'XCloseIM', 
 'XGetIMValues', 'XSetIMValues', 
 'XDisplayOfIM', 'XLocaleOfIM', 'XCreateIC', 
 'XDestroyIC', 'XSetICFocus', 
 'XUnsetICFocus', 'XwcResetIC', 'XmbResetIC', 
 'Xutf8ResetIC', 'XSetICValues', 
 'XGetICValues', 'XIMOfIC', 'XFilterEvent', 
 'XmbLookupString', 'XwcLookupString', 
 'Xutf8LookupString', 
 'XVaCreateNestedList', 'XRegisterIMInstantiateCallback', 
 'XUnregisterIMInstantiateCallback', 
 'XConnectionWatchProc', 
 'XInternalConnectionNumbers', 'XProcessInternalConnection', 
 'XAddConnectionWatch', 
 'XRemoveConnectionWatch', 'XSetAuthorization', 
 '_Xmbtowc', '_Xwctomb', 
 'XGetEventData', 'XFreeEventData', 'NoValue', 
 'XValue', 'YValue', 'WidthValue', 
 'HeightValue', 'AllValues', 'XNegative', 
 'YNegative', 'XSizeHints', 'USPosition', 
 'USSize', 'PPosition', 'PSize', 
 'PMinSize', 'PMaxSize', 'PResizeInc', 
 'PAspect', 'PBaseSize', 'PWinGravity', 
 'PAllHints', 'XWMHints', 'InputHint', 
 'StateHint', 'IconPixmapHint', 
 'IconWindowHint', 'IconPositionHint', 'IconMaskHint', 
 'WindowGroupHint', 
 'AllHints', 'XUrgencyHint', 'WithdrawnState', 'NormalState', 
 'IconicState', 
 'DontCareState', 'ZoomState', 'InactiveState', 'XTextProperty', 
 'XNoMemory', 
 'XLocaleNotSupported', 'XConverterNotFound', 'XICCEncodingStyle', 
 'XStringStyle', 
 'XCompoundTextStyle', 'XTextStyle', 'XStdICCTextStyle', 
 'XUTF8StringStyle', 
 'XIconSize', 'XClassHint', 'XComposeStatus', 'Region', 
 'RectangleOut', 
 'RectangleIn', 'RectanglePart', 'XVisualInfo', 'VisualNoMask', 
 'VisualIDMask', 
 'VisualScreenMask', 'VisualDepthMask', 'VisualClassMask', 
 'VisualRedMaskMask', 
 'VisualGreenMaskMask', 'VisualBlueMaskMask', 
 'VisualColormapSizeMask', 'VisualBitsPerRGBMask', 
 'VisualAllMask', 
 'XStandardColormap', 'BitmapSuccess', 'BitmapOpenFailed', 
 'BitmapFileInvalid', 
 'BitmapNoMemory', 'XCSUCCESS', 'XCNOMEM', 'XCNOENT', 
 'XContext', 
 'XAllocClassHint', 'XAllocIconSize', 'XAllocSizeHints', 
 'XAllocStandardColormap', 
 'XAllocWMHints', 'XClipBox', 'XCreateRegion', 
 'XDefaultString', 'XDeleteContext', 
 'XDestroyRegion', 'XEmptyRegion', 
 'XEqualRegion', 'XFindContext', 'XGetClassHint', 
 'XGetIconSizes', 
 'XGetNormalHints', 'XGetRGBColormaps', 'XGetSizeHints', 
 'XGetStandardColormap', 
 'XGetTextProperty', 'XGetVisualInfo', 
 'XGetWMClientMachine', 'XGetWMHints', 
 'XGetWMIconName', 'XGetWMName', 
 'XGetWMNormalHints', 'XGetWMSizeHints', 
 'XGetZoomHints', 'XIntersectRegion', 
 'XConvertCase', 'XLookupString', 'XMatchVisualInfo', 
 'XOffsetRegion', 
 'XPointInRegion', 'XPolygonRegion', 'XRectInRegion', 'XSaveContext', 
 'XSetClassHint', 
 'XSetIconSizes', 'XSetNormalHints', 'XSetRGBColormaps', 
 'XSetSizeHints', 
 'XSetStandardProperties', 'XSetTextProperty', 
 'XSetWMClientMachine', 'XSetWMHints', 
 'XSetWMIconName', 'XSetWMName', 
 'XSetWMNormalHints', 'XSetWMProperties', 
 'XmbSetWMProperties', 
 'Xutf8SetWMProperties', 'XSetWMSizeHints', 'XSetRegion', 
 'XSetStandardColormap', 
 'XSetZoomHints', 'XShrinkRegion', 
 'XStringListToTextProperty', 'XSubtractRegion', 
 'XmbTextListToTextProperty', 
 'XwcTextListToTextProperty', 'Xutf8TextListToTextProperty', 
 'XwcFreeStringList', 
 'XTextPropertyToStringList', 'XmbTextPropertyToTextList', 
 'XwcTextPropertyToTextList', 
 'Xutf8TextPropertyToTextList', 
 'XUnionRectWithRegion', 'XUnionRegion', 'XWMGeometry', 
 'XXorRegion']
# okay decompiling out\pyglet.libs.x11.xlib.pyc
