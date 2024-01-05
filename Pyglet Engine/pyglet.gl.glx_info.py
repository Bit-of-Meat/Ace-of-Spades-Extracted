# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.glx_info
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from ..pyglet.gl.glx import *
from pyglet.compat import asstr

class GLXInfoException(Exception):
    pass


class GLXInfo(object):

    def __init__(self, display=None):
        if display and not _glx_info.display:
            _glx_info.set_display(display)
        self.display = display

    def set_display(self, display):
        self.display = display

    def check_display(self):
        if not self.display:
            raise GLXInfoException('No X11 display has been set yet.')

    def have_version(self, major, minor=0):
        self.check_display()
        if not glXQueryExtension(self.display, None, None):
            raise GLXInfoException('pyglet requires an X server with GLX')
        server_version = self.get_server_version().split()[0]
        client_version = self.get_client_version().split()[0]
        server = [ int(i) for i in server_version.split('.') ]
        client = [ int(i) for i in client_version.split('.') ]
        return tuple(server) >= (major, minor) and tuple(client) >= (major, minor)

    def get_server_vendor(self):
        self.check_display()
        return asstr(glXQueryServerString(self.display, 0, GLX_VENDOR))

    def get_server_version(self):
        self.check_display()
        major = c_int()
        minor = c_int()
        if not glXQueryVersion(self.display, byref(major), byref(minor)):
            raise GLXInfoException('Could not determine GLX server version')
        return '%s.%s' % (major.value, minor.value)

    def get_server_extensions(self):
        self.check_display()
        return asstr(glXQueryServerString(self.display, 0, GLX_EXTENSIONS)).split()

    def get_client_vendor(self):
        self.check_display()
        return asstr(glXGetClientString(self.display, GLX_VENDOR))

    def get_client_version(self):
        self.check_display()
        return asstr(glXGetClientString(self.display, GLX_VERSION))

    def get_client_extensions(self):
        self.check_display()
        return asstr(glXGetClientString(self.display, GLX_EXTENSIONS)).split()

    def get_extensions(self):
        self.check_display()
        return asstr(glXQueryExtensionsString(self.display, 0)).split()

    def have_extension(self, extension):
        self.check_display()
        if not self.have_version(1, 1):
            return False
        return extension in self.get_extensions()


_glx_info = GLXInfo()
set_display = _glx_info.set_display
check_display = _glx_info.check_display
have_version = _glx_info.have_version
get_server_vendor = _glx_info.get_server_vendor
get_server_version = _glx_info.get_server_version
get_server_extensions = _glx_info.get_server_extensions
get_client_vendor = _glx_info.get_client_vendor
get_client_version = _glx_info.get_client_version
get_client_extensions = _glx_info.get_client_extensions
get_extensions = _glx_info.get_extensions
have_extension = _glx_info.have_extension
# okay decompiling out\pyglet.gl.glx_info.pyc
