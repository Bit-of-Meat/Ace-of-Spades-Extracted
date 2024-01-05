# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.libs.x11.xinerama
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
import pyglet.lib
_lib = pyglet.lib.load_library('Xinerama')
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


import pyglet.libs.x11.xlib

class struct_anon_93(Structure):
    __slots__ = [
     'screen_number', 
     'x_org', 
     'y_org', 
     'width', 
     'height']


struct_anon_93._fields_ = [
 (
  'screen_number', c_int),
 (
  'x_org', c_short),
 (
  'y_org', c_short),
 (
  'width', c_short),
 (
  'height', c_short)]
XineramaScreenInfo = struct_anon_93
Display = pyglet.libs.x11.xlib.Display
XineramaQueryExtension = _lib.XineramaQueryExtension
XineramaQueryExtension.restype = c_int
XineramaQueryExtension.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XineramaQueryVersion = _lib.XineramaQueryVersion
XineramaQueryVersion.restype = c_int
XineramaQueryVersion.argtypes = [POINTER(Display), POINTER(c_int), POINTER(c_int)]
XineramaIsActive = _lib.XineramaIsActive
XineramaIsActive.restype = c_int
XineramaIsActive.argtypes = [POINTER(Display)]
XineramaQueryScreens = _lib.XineramaQueryScreens
XineramaQueryScreens.restype = POINTER(XineramaScreenInfo)
XineramaQueryScreens.argtypes = [POINTER(Display), POINTER(c_int)]
__all__ = [
 'XineramaScreenInfo', 'XineramaQueryExtension', 
 'XineramaQueryVersion', 'XineramaIsActive', 
 'XineramaQueryScreens']
# okay decompiling out\pyglet.libs.x11.xinerama.pyc
