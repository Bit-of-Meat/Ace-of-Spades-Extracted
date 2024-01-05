# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.lib_agl
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from ..ctypes import *
import pyglet.lib
from pyglet.gl.lib import missing_function, decorate_function
__all__ = [
 'link_GL', 'link_GLU', 'link_AGL']
gl_lib = pyglet.lib.load_library(framework='/System/Library/Frameworks/OpenGL.framework')
agl_lib = pyglet.lib.load_library(framework='/System/Library/Frameworks/AGL.framework')

def link_GL(name, restype, argtypes, requires=None, suggestions=None):
    try:
        func = getattr(gl_lib, name)
        func.restype = restype
        func.argtypes = argtypes
        decorate_function(func, name)
        return func
    except AttributeError:
        return missing_function(name, requires, suggestions)


link_GLU = link_GL

def link_AGL(name, restype, argtypes, requires=None, suggestions=None):
    try:
        func = getattr(agl_lib, name)
        func.restype = restype
        func.argtypes = argtypes
        decorate_function(func, name)
        return func
    except AttributeError:
        return missing_function(name, requires, suggestions)
# okay decompiling out\pyglet.gl.lib_agl.pyc
