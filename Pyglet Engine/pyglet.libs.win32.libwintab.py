# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.win32.libwintab
import ctypes
lib = ctypes.windll.wintab32
LONG = ctypes.c_long
BOOL = ctypes.c_int
UINT = ctypes.c_uint
WORD = ctypes.c_uint16
DWORD = ctypes.c_uint32
WCHAR = ctypes.c_wchar
FIX32 = DWORD
WTPKT = DWORD
LCNAMELEN = 40

class AXIS(ctypes.Structure):
    _fields_ = (
     (
      'axMin', LONG),
     (
      'axMax', LONG),
     (
      'axUnits', UINT),
     (
      'axResolution', FIX32))

    def get_scale(self):
        return 1 / float(self.axMax - self.axMin)

    def get_bias(self):
        return -self.axMin


class ORIENTATION(ctypes.Structure):
    _fields_ = (
     (
      'orAzimuth', ctypes.c_int),
     (
      'orAltitude', ctypes.c_int),
     (
      'orTwist', ctypes.c_int))


class ROTATION(ctypes.Structure):
    _fields_ = (
     (
      'roPitch', ctypes.c_int),
     (
      'roRoll', ctypes.c_int),
     (
      'roYaw', ctypes.c_int))


class LOGCONTEXT(ctypes.Structure):
    _fields_ = (
     (
      'lcName', WCHAR * LCNAMELEN),
     (
      'lcOptions', UINT),
     (
      'lcStatus', UINT),
     (
      'lcLocks', UINT),
     (
      'lcMsgBase', UINT),
     (
      'lcDevice', UINT),
     (
      'lcPktRate', UINT),
     (
      'lcPktData', WTPKT),
     (
      'lcPktMode', WTPKT),
     (
      'lcMoveMask', WTPKT),
     (
      'lcBtnDnMask', DWORD),
     (
      'lcBtnUpMask', DWORD),
     (
      'lcInOrgX', LONG),
     (
      'lcInOrgY', LONG),
     (
      'lcInOrgZ', LONG),
     (
      'lcInExtX', LONG),
     (
      'lcInExtY', LONG),
     (
      'lcInExtZ', LONG),
     (
      'lcOutOrgX', LONG),
     (
      'lcOutOrgY', LONG),
     (
      'lcOutOrgZ', LONG),
     (
      'lcOutExtX', LONG),
     (
      'lcOutExtY', LONG),
     (
      'lcOutExtZ', LONG),
     (
      'lcSensX', FIX32),
     (
      'lcSensY', FIX32),
     (
      'lcSensZ', FIX32),
     (
      'lcSysMode', BOOL),
     (
      'lcSysOrgX', ctypes.c_int),
     (
      'lcSysOrgY', ctypes.c_int),
     (
      'lcSysExtX', ctypes.c_int),
     (
      'lcSysExtY', ctypes.c_int),
     (
      'lcSysSensX', FIX32),
     (
      'lcSysSensY', FIX32))


class PACKET(ctypes.Structure):
    _fields_ = (
     (
      'pkChanged', WTPKT),
     (
      'pkCursor', UINT),
     (
      'pkButtons', DWORD),
     (
      'pkX', LONG),
     (
      'pkY', LONG),
     (
      'pkZ', LONG),
     (
      'pkNormalPressure', UINT),
     (
      'pkTangentPressure', UINT),
     (
      'pkOrientation', ORIENTATION))


PK_CONTEXT = 1
PK_STATUS = 2
PK_TIME = 4
PK_CHANGED = 8
PK_SERIAL_NUMBER = 16
PK_CURSOR = 32
PK_BUTTONS = 64
PK_X = 128
PK_Y = 256
PK_Z = 512
PK_NORMAL_PRESSURE = 1024
PK_TANGENT_PRESSURE = 2048
PK_ORIENTATION = 4096
PK_ROTATION = 8192
TU_NONE = 0
TU_INCHES = 1
TU_CENTIMETERS = 2
TU_CIRCLE = 3
WT_DEFBASE = 32752
WT_MAXOFFSET = 15
WT_PACKET = 0
WT_CTXOPEN = 1
WT_CTXCLOSE = 2
WT_CTXUPDATE = 3
WT_CTXOVERLAP = 4
WT_PROXIMITY = 5
WT_INFOCHANGE = 6
WT_CSRCHANGE = 7
SBN_NONE = 0
SBN_LCLICK = 1
SBN_LDBLCLICK = 2
SBN_LDRAG = 3
SBN_RCLICK = 4
SBN_RDBLCLICK = 5
SBN_RDRAG = 6
SBN_MCLICK = 7
SBN_MDBLCLICK = 8
SBN_MDRAG = 9
SBN_PTCLICK = 16
SBN_PTDBLCLICK = 32
SBN_PTDRAG = 48
SBN_PNCLICK = 64
SBN_PNDBLCLICK = 80
SBN_PNDRAG = 96
SBN_P1CLICK = 112
SBN_P1DBLCLICK = 128
SBN_P1DRAG = 144
SBN_P2CLICK = 160
SBN_P2DBLCLICK = 176
SBN_P2DRAG = 192
SBN_P3CLICK = 208
SBN_P3DBLCLICK = 224
SBN_P3DRAG = 240
HWC_INTEGRATED = 1
HWC_TOUCH = 2
HWC_HARDPROX = 4
HWC_PHYSID_CURSORS = 8
CRC_MULTIMODE = 1
CRC_AGGREGATE = 2
CRC_INVERT = 4
WTI_INTERFACE = 1
IFC_WINTABID = 1
IFC_SPECVERSION = 2
IFC_IMPLVERSION = 3
IFC_NDEVICES = 4
IFC_NCURSORS = 5
IFC_NCONTEXTS = 6
IFC_CTXOPTIONS = 7
IFC_CTXSAVESIZE = 8
IFC_NEXTENSIONS = 9
IFC_NMANAGERS = 10
IFC_MAX = 10
WTI_STATUS = 2
STA_CONTEXTS = 1
STA_SYSCTXS = 2
STA_PKTRATE = 3
STA_PKTDATA = 4
STA_MANAGERS = 5
STA_SYSTEM = 6
STA_BUTTONUSE = 7
STA_SYSBTNUSE = 8
STA_MAX = 8
WTI_DEFCONTEXT = 3
WTI_DEFSYSCTX = 4
WTI_DDCTXS = 400
WTI_DSCTXS = 500
CTX_NAME = 1
CTX_OPTIONS = 2
CTX_STATUS = 3
CTX_LOCKS = 4
CTX_MSGBASE = 5
CTX_DEVICE = 6
CTX_PKTRATE = 7
CTX_PKTDATA = 8
CTX_PKTMODE = 9
CTX_MOVEMASK = 10
CTX_BTNDNMASK = 11
CTX_BTNUPMASK = 12
CTX_INORGX = 13
CTX_INORGY = 14
CTX_INORGZ = 15
CTX_INEXTX = 16
CTX_INEXTY = 17
CTX_INEXTZ = 18
CTX_OUTORGX = 19
CTX_OUTORGY = 20
CTX_OUTORGZ = 21
CTX_OUTEXTX = 22
CTX_OUTEXTY = 23
CTX_OUTEXTZ = 24
CTX_SENSX = 25
CTX_SENSY = 26
CTX_SENSZ = 27
CTX_SYSMODE = 28
CTX_SYSORGX = 29
CTX_SYSORGY = 30
CTX_SYSEXTX = 31
CTX_SYSEXTY = 32
CTX_SYSSENSX = 33
CTX_SYSSENSY = 34
CTX_MAX = 34
WTI_DEVICES = 100
DVC_NAME = 1
DVC_HARDWARE = 2
DVC_NCSRTYPES = 3
DVC_FIRSTCSR = 4
DVC_PKTRATE = 5
DVC_PKTDATA = 6
DVC_PKTMODE = 7
DVC_CSRDATA = 8
DVC_XMARGIN = 9
DVC_YMARGIN = 10
DVC_ZMARGIN = 11
DVC_X = 12
DVC_Y = 13
DVC_Z = 14
DVC_NPRESSURE = 15
DVC_TPRESSURE = 16
DVC_ORIENTATION = 17
DVC_ROTATION = 18
DVC_PNPID = 19
DVC_MAX = 19
WTI_CURSORS = 200
CSR_NAME = 1
CSR_ACTIVE = 2
CSR_PKTDATA = 3
CSR_BUTTONS = 4
CSR_BUTTONBITS = 5
CSR_BTNNAMES = 6
CSR_BUTTONMAP = 7
CSR_SYSBTNMAP = 8
CSR_NPBUTTON = 9
CSR_NPBTNMARKS = 10
CSR_NPRESPONSE = 11
CSR_TPBUTTON = 12
CSR_TPBTNMARKS = 13
CSR_TPRESPONSE = 14
CSR_PHYSID = 15
CSR_MODE = 16
CSR_MINPKTDATA = 17
CSR_MINBUTTONS = 18
CSR_CAPABILITIES = 19
CSR_TYPE = 20
CSR_MAX = 20
WTI_EXTENSIONS = 300
EXT_NAME = 1
EXT_TAG = 2
EXT_MASK = 3
EXT_SIZE = 4
EXT_AXES = 5
EXT_DEFAULT = 6
EXT_DEFCONTEXT = 7
EXT_DEFSYSCTX = 8
EXT_CURSORS = 9
EXT_MAX = 109
CXO_SYSTEM = 1
CXO_PEN = 2
CXO_MESSAGES = 4
CXO_MARGIN = 32768
CXO_MGNINSIDE = 16384
CXO_CSRMESSAGES = 8
CXS_DISABLED = 1
CXS_OBSCURED = 2
CXS_ONTOP = 4
CXL_INSIZE = 1
CXL_INASPECT = 2
CXL_SENSITIVITY = 4
CXL_MARGIN = 8
CXL_SYSOUT = 16
TPS_PROXIMITY = 1
TPS_QUEUE_ERR = 2
TPS_MARGIN = 4
TPS_GRAB = 8
TPS_INVERT = 16
TBN_NONE = 0
TBN_UP = 1
TBN_DOWN = 2
PKEXT_ABSOLUTE = 1
PKEXT_RELATIVE = 2
WTX_OBT = 0
WTX_FKEYS = 1
WTX_TILT = 2
WTX_CSRMASK = 3
WTX_XBTNMASK = 4
WTX_EXPKEYS = 5
# okay decompiling out\pyglet.libs.win32.libwintab.pyc
