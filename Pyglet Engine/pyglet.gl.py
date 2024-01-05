# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from pyglet.gl.lib import GLException
from ..pyglet.gl.gl import *
from ..pyglet.gl.glu import *
from ..pyglet.gl.glext_arb import *
from pyglet.gl import gl_info
import sys as _sys
_is_epydoc = hasattr(_sys, 'is_epydoc') and _sys.is_epydoc
current_context = None

def get_current_context():
    return current_context


class ContextException(Exception):
    pass


class ConfigException(Exception):
    pass


import pyglet as _pyglet
if _pyglet.options['debug_texture']:
    _debug_texture_total = 0
    _debug_texture_sizes = {}
    _debug_texture = None

    def _debug_texture_alloc(texture, size):
        global _debug_texture_total
        _debug_texture_sizes[texture] = size
        _debug_texture_total += size
        print '%d (+%d)' % (_debug_texture_total, size)


    def _debug_texture_dealloc(texture):
        global _debug_texture_total
        size = _debug_texture_sizes[texture]
        del _debug_texture_sizes[texture]
        _debug_texture_total -= size
        print '%d (-%d)' % (_debug_texture_total, size)


    _glBindTexture = glBindTexture

    def glBindTexture(target, texture):
        global _debug_texture
        _debug_texture = texture
        return _glBindTexture(target, texture)


    _glTexImage2D = glTexImage2D

    def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
        try:
            _debug_texture_dealloc(_debug_texture)
        except KeyError:
            pass

        if internalformat in (1, GL_ALPHA, GL_INTENSITY, GL_LUMINANCE):
            depth = 1
        elif internalformat in (2, GL_RGB16, GL_RGBA16):
            depth = 2
        elif internalformat in (3, GL_RGB):
            depth = 3
        else:
            depth = 4
        size = (width + 2 * border) * (height + 2 * border) * depth
        _debug_texture_alloc(_debug_texture, size)
        return _glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)


    _glDeleteTextures = glDeleteTextures

    def glDeleteTextures(n, textures):
        if not hasattr(textures, '__len__'):
            _debug_texture_dealloc(textures.value)
        else:
            for i in range(n):
                _debug_texture_dealloc(textures[i].value)

        return _glDeleteTextures(n, textures)


def _create_shadow_window():
    global _shadow_window
    import pyglet
    if not pyglet.options['shadow_window'] or _is_epydoc:
        return
    from pyglet.window import Window
    _shadow_window = Window(width=1, height=1, visible=False)
    _shadow_window.switch_to()
    from pyglet import app
    app.windows.remove(_shadow_window)


from base import ObjectSpace, CanvasConfig, Context
if _is_epydoc:
    from base import Config
elif _sys.platform in ('win32', 'cygwin'):
    from win32 import Win32Config as Config
elif _sys.platform == 'linux2':
    from xlib import XlibConfig as Config
elif _sys.platform == 'darwin':
    if _pyglet.options['darwin_cocoa']:
        from cocoa import CocoaConfig as Config
    else:
        from carbon import CarbonConfig as Config
del base
_shadow_window = None
if not _is_epydoc and 'pyglet.window' not in _sys.modules and _pyglet.options['shadow_window']:
    _pyglet.gl = _sys.modules[__name__]
    import pyglet.window
# okay decompiling out\pyglet.gl.pyc
