# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.glxext_mesa
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import ctypes
from ..ctypes import *
from pyglet.gl.lib import link_GLX as _link_function
glXSwapIntervalMESA = _link_function('glXSwapIntervalMESA', c_int, [c_int], 'MESA_swap_control')
# okay decompiling out\pyglet.gl.glxext_mesa.pyc
