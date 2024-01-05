# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.gl_info
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from ..ctypes import *
import warnings
from ..pyglet.gl.gl import *
from pyglet.compat import asstr

class GLInfo(object):
    have_context = False
    version = '0.0.0'
    vendor = ''
    renderer = ''
    extensions = set()
    _have_info = False

    def set_active_context(self):
        self.have_context = True
        if not self._have_info:
            self.vendor = asstr(cast(glGetString(GL_VENDOR), c_char_p).value)
            self.renderer = asstr(cast(glGetString(GL_RENDERER), c_char_p).value)
            self.version = asstr(cast(glGetString(GL_VERSION), c_char_p).value)
            if self.have_version(3):
                from pyglet.gl.glext_arb import glGetStringi, GL_NUM_EXTENSIONS
                num_extensions = GLint()
                glGetIntegerv(GL_NUM_EXTENSIONS, num_extensions)
                self.extensions = (asstr(cast(glGetStringi(GL_EXTENSIONS, i), c_char_p).value) for i in range(num_extensions.value))
            else:
                self.extensions = asstr(cast(glGetString(GL_EXTENSIONS), c_char_p).value).split()
            if self.extensions:
                self.extensions = set(self.extensions)
            self._have_info = True

    def remove_active_context(self):
        self.have_context = False
        self._have_info = False

    def have_extension(self, extension):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return extension in self.extensions

    def get_extensions(self):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return self.extensions

    def get_version(self):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return self.version

    def have_version(self, major, minor=0, release=0):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        ver = '%s.0.0' % self.version.split(' ', 1)[0]
        imajor, iminor, irelease = [ int(v) for v in ver.split('.', 3)[:3] ]
        return imajor > major or imajor == major and iminor > minor or imajor == major and iminor == minor and irelease >= release

    def get_renderer(self):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return self.renderer

    def get_vendor(self):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return self.vendor


_gl_info = GLInfo()
set_active_context = _gl_info.set_active_context
remove_active_context = _gl_info.remove_active_context
have_extension = _gl_info.have_extension
get_extensions = _gl_info.get_extensions
get_version = _gl_info.get_version
have_version = _gl_info.have_version
get_renderer = _gl_info.get_renderer
get_vendor = _gl_info.get_vendor

def have_context():
    return _gl_info.have_context
# okay decompiling out\pyglet.gl.gl_info.pyc
