# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.wgl_info
__docformat__ = 'restructuredtext'
__version__ = '$Id: glx_info.py 615 2007-02-07 13:17:05Z Alex.Holkner $'
from ..ctypes import *
import warnings
from pyglet.gl.lib import MissingFunctionException
from ..pyglet.gl.gl import *
from pyglet.gl import gl_info
from ..pyglet.gl.wgl import *
from ..pyglet.gl.wglext_arb import *
from pyglet.compat import asstr

class WGLInfoException(Exception):
    pass


class WGLInfo(object):

    def get_extensions(self):
        if not gl_info.have_context():
            warnings.warn("Can't query WGL until a context is created.")
            return []
        try:
            return asstr(wglGetExtensionsStringEXT()).split()
        except MissingFunctionException:
            return asstr(cast(glGetString(GL_EXTENSIONS), c_char_p).value).split()

    def have_extension(self, extension):
        return extension in self.get_extensions()


_wgl_info = WGLInfo()
get_extensions = _wgl_info.get_extensions
have_extension = _wgl_info.have_extension
# okay decompiling out\pyglet.gl.wgl_info.pyc
