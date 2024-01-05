# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.glu_info
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
import warnings
from ..pyglet.gl.glu import *
from pyglet.compat import asstr

class GLUInfo(object):
    have_context = False
    version = '0.0.0'
    extensions = []
    _have_info = False

    def set_active_context(self):
        self.have_context = True
        if not self._have_info:
            self.extensions = asstr(cast(gluGetString(GLU_EXTENSIONS), c_char_p).value).split()
            self.version = asstr(cast(gluGetString(GLU_VERSION), c_char_p).value)
            self._have_info = True

    def have_version(self, major, minor=0, release=0):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        ver = '%s.0.0' % self.version.split(' ', 1)[0]
        imajor, iminor, irelease = [ int(v) for v in ver.split('.', 3)[:3] ]
        return imajor > major or imajor == major and iminor > minor or imajor == major and iminor == minor and irelease >= release

    def get_version(self):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return self.version

    def have_extension(self, extension):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return extension in self.extensions

    def get_extensions(self):
        if not self.have_context:
            warnings.warn('No GL context created yet.')
        return self.extensions


_glu_info = GLUInfo()
set_active_context = _glu_info.set_active_context
have_version = _glu_info.have_version
get_version = _glu_info.get_version
have_extension = _glu_info.have_extension
get_extensions = _glu_info.get_extensions
# okay decompiling out\pyglet.gl.glu_info.pyc
