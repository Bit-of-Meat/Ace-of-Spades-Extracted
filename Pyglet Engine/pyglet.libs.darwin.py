# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.darwin
import pyglet
if pyglet.options['darwin_cocoa']:
    from Foundation import *
    from Cocoa import *
    from Quartz import *
    NSAnyEventMask = 4294967295
else:
    from types import *
    from constants import *
    carbon = pyglet.lib.load_library(framework='/System/Library/Frameworks/Carbon.framework')
    quicktime = pyglet.lib.load_library(framework='/System/Library/Frameworks/QuickTime.framework')
    carbon.GetEventDispatcherTarget.restype = EventTargetRef
    carbon.ReceiveNextEvent.argtypes = [
     c_uint32, c_void_p, c_double, c_ubyte, POINTER(EventRef)]
    EventHandlerProcPtr = CFUNCTYPE(c_int, c_int, c_void_p, c_void_p)
    carbon.NewEventHandlerUPP.restype = c_void_p
    carbon.GetCurrentKeyModifiers = c_uint32
    carbon.NewRgn.restype = RgnHandle
    carbon.CGDisplayBounds.argtypes = [c_void_p]
    carbon.CGDisplayBounds.restype = CGRect

    def create_cfstring(text):
        return carbon.CFStringCreateWithCString(c_void_p(), text.encode('utf8'), kCFStringEncodingUTF8)


    def _oscheck(result):
        if result != noErr:
            raise RuntimeError('Carbon error %d' % result)
        return result
# okay decompiling out\pyglet.libs.darwin.pyc
