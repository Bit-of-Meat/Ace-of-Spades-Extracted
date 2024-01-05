# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.canvas.cocoa
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from ..ctypes import *
from ctypes import util
from pyglet import app
from base import Display, Screen, ScreenMode, Canvas
from Cocoa import NSScreen
cf = cdll.LoadLibrary(util.find_library('CoreFoundation'))
quartz = cdll.LoadLibrary(util.find_library('quartz'))
kCFStringEncodingUTF8 = 134217984
cf.CFArrayGetValueAtIndex.restype = c_void_p
quartz.CGDisplayCopyAllDisplayModes.restype = c_void_p
quartz.CGDisplayCopyAllDisplayModes.argtypes = [c_uint32, c_void_p]
quartz.CGDisplayModeGetRefreshRate.restype = c_double
quartz.CGDisplayModeCopyPixelEncoding.restype = c_void_p

def cfstring_to_string(cfstring):
    length = cf.CFStringGetLength(cfstring)
    size = cf.CFStringGetMaximumSizeForEncoding(length, kCFStringEncodingUTF8)
    buffer = c_buffer(size + 1)
    result = cf.CFStringGetCString(cfstring, buffer, len(buffer), kCFStringEncodingUTF8)
    if result:
        return buffer.value


def cfarray_to_list(cfarray):
    count = cf.CFArrayGetCount(cfarray)
    return [ c_void_p(cf.CFArrayGetValueAtIndex(cfarray, i)) for i in range(count)
           ]


class CocoaDisplay(Display):

    def get_screens(self):
        return [ CocoaScreen(self, nsscreen) for nsscreen in NSScreen.screens() ]


class CocoaScreen(Screen):

    def __init__(self, display, nsscreen):
        (x, y), (width, height) = nsscreen.frame()
        super(CocoaScreen, self).__init__(display, int(x), int(y), int(width), int(height))
        self._nsscreen = nsscreen
        self._cg_display_id = self._get_CGDirectDisplayID()
        self._default_mode = self.get_mode()

    def _get_CGDirectDisplayID(self):
        screenInfo = self._nsscreen.deviceDescription()
        return screenInfo.objectForKey_('NSScreenNumber')

    def get_matching_configs(self, template):
        canvas = CocoaCanvas(self.display, self, None)
        return template.match(canvas)

    def get_modes(self):
        cgmodes = c_void_p(quartz.CGDisplayCopyAllDisplayModes(self._cg_display_id, None))
        modes = [ CocoaScreenMode(self, cgmode) for cgmode in cfarray_to_list(cgmodes) ]
        cf.CFRelease(cgmodes)
        return modes

    def get_mode(self):
        quartz.CGDisplayCopyDisplayMode.restype = c_void_p
        cgmode = c_void_p(quartz.CGDisplayCopyDisplayMode(self._cg_display_id))
        mode = CocoaScreenMode(self, cgmode)
        quartz.CGDisplayModeRelease(cgmode)
        return mode

    def set_mode(self, mode):
        quartz.CGDisplayCapture(self._cg_display_id)
        quartz.CGDisplaySetDisplayMode(self._cg_display_id, mode.cgmode, None)
        self.width = mode.width
        self.height = mode.height
        return

    def restore_mode(self):
        quartz.CGDisplaySetDisplayMode(self._cg_display_id, self._default_mode.cgmode, None)
        quartz.CGDisplayRelease(self._cg_display_id)
        return

    def capture_display(self):
        quartz.CGDisplayCapture(self._cg_display_id)

    def release_display(self):
        quartz.CGDisplayRelease(self._cg_display_id)


class CocoaScreenMode(ScreenMode):

    def __init__(self, screen, cgmode):
        super(CocoaScreenMode, self).__init__(screen)
        quartz.CGDisplayModeRetain(cgmode)
        self.cgmode = cgmode
        self.width = int(quartz.CGDisplayModeGetWidth(cgmode))
        self.height = int(quartz.CGDisplayModeGetHeight(cgmode))
        self.depth = self.getBitsPerPixel(cgmode)
        self.rate = quartz.CGDisplayModeGetRefreshRate(cgmode)

    def __del__(self):
        quartz.CGDisplayModeRelease(self.cgmode)
        self.cgmode = None
        return

    def getBitsPerPixel(self, cgmode):
        IO8BitIndexedPixels = 'PPPPPPPP'
        IO16BitDirectPixels = '-RRRRRGGGGGBBBBB'
        IO32BitDirectPixels = '--------RRRRRRRRGGGGGGGGBBBBBBBB'
        cfstring = c_void_p(quartz.CGDisplayModeCopyPixelEncoding(cgmode))
        pixelEncoding = cfstring_to_string(cfstring)
        cf.CFRelease(cfstring)
        if pixelEncoding == IO8BitIndexedPixels:
            return 8
        if pixelEncoding == IO16BitDirectPixels:
            return 16
        if pixelEncoding == IO32BitDirectPixels:
            return 32
        return 0


class CocoaCanvas(Canvas):

    def __init__(self, display, screen, nsview):
        super(CocoaCanvas, self).__init__(display)
        self.screen = screen
        self.nsview = nsview
# okay decompiling out\pyglet.canvas.cocoa.pyc
