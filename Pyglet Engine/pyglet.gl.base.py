# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.base
import sys as _sys
from pyglet import gl
from pyglet.gl import gl_info
from pyglet.gl import glu_info

class Config(object):
    _attribute_names = [
     'double_buffer', 
     'stereo', 
     'buffer_size', 
     'aux_buffers', 
     'sample_buffers', 
     'samples', 
     'red_size', 
     'green_size', 
     'blue_size', 
     'alpha_size', 
     'depth_size', 
     'stencil_size', 
     'accum_red_size', 
     'accum_green_size', 
     'accum_blue_size', 
     'accum_alpha_size', 
     'major_version', 
     'minor_version', 
     'forward_compatible', 
     'debug']
    major_version = None
    minor_version = None
    forward_compatible = None
    debug = None

    def __init__(self, **kwargs):
        for name in self._attribute_names:
            if name in kwargs:
                setattr(self, name, kwargs[name])
            else:
                setattr(self, name, None)

        return

    def _requires_gl_3(self):
        if self.major_version is not None and self.major_version >= 3:
            return True
        else:
            if self.forward_compatible or self.debug:
                return True
            return False

    def get_gl_attributes(self):
        return [ (name, getattr(self, name)) for name in self._attribute_names ]

    def match(self, canvas):
        raise NotImplementedError('abstract')

    def create_context(self, share):
        raise gl.ConfigException('This config cannot be used to create contexts.  Use Config.match to created a CanvasConfig')

    def is_complete(self):
        return isinstance(self, CanvasConfig)

    def __repr__(self):
        import pprint
        return '%s(%s)' % (self.__class__.__name__,
         pprint.pformat(self.get_gl_attributes()))


class CanvasConfig(Config):

    def __init__(self, canvas, base_config):
        self.canvas = canvas
        self.major_version = base_config.major_version
        self.minor_version = base_config.minor_version
        self.forward_compatible = base_config.forward_compatible
        self.debug = base_config.debug

    def compatible(self, canvas):
        raise NotImplementedError('abstract')

    def create_context(self, share):
        raise NotImplementedError('abstract')

    def is_complete(self):
        return True


class ObjectSpace(object):

    def __init__(self):
        self._doomed_textures = []
        self._doomed_buffers = []


class Context(object):
    CONTEXT_SHARE_NONE = None
    CONTEXT_SHARE_EXISTING = 1
    _gl_begin = False
    _info = None
    _workaround_checks = [
     (
      '_workaround_unpack_row_length',
      (lambda info: info.get_renderer() == 'GDI Generic')),
     (
      '_workaround_vbo',
      (lambda info: info.get_renderer().startswith('ATI Radeon X') or info.get_renderer() == 'Intel 965/963 Graphics Media Accelerator')),
     (
      '_workaround_vbo_finish',
      (lambda info: 'ATI' in info.get_renderer() and info.have_version(1, 5) and _sys.platform == 'darwin'))]

    def __init__(self, config, context_share=None):
        self.config = config
        self.context_share = context_share
        self.canvas = None
        if context_share:
            self.object_space = context_share.object_space
        else:
            self.object_space = ObjectSpace()
        return

    def __repr__(self):
        return '%s()' % self.__class__.__name__

    def attach(self, canvas):
        if self.canvas is not None:
            self.detach()
        if not self.config.compatible(canvas):
            raise RuntimeError('Cannot attach %r to %r' % (canvas, self))
        self.canvas = canvas
        return

    def detach(self):
        self.canvas = None
        return

    def set_current(self):
        if not self.canvas:
            raise RuntimeError('Canvas has not been attached')
        gl.current_context = self
        gl_info.set_active_context()
        glu_info.set_active_context()
        if not self._info:
            self._info = gl_info.GLInfo()
            self._info.set_active_context()
            for attr, check in self._workaround_checks:
                setattr(self, attr, check(self._info))

        if self.object_space._doomed_textures:
            textures = self.object_space._doomed_textures
            textures = (gl.GLuint * len(textures))(*textures)
            gl.glDeleteTextures(len(textures), textures)
            self.object_space._doomed_textures = []
        if self.object_space._doomed_buffers:
            buffers = self.object_space._doomed_buffers
            buffers = (gl.GLuint * len(buffers))(*buffers)
            gl.glDeleteBuffers(len(buffers), buffers)
            self.object_space._doomed_buffers = []

    def destroy(self):
        self.detach()
        if gl.current_context is self:
            gl.current_context = None
            gl_info.remove_active_context()
            if gl._shadow_window is not None:
                gl._shadow_window.switch_to()
        return

    def delete_texture(self, texture_id):
        if self.object_space is gl.current_context.object_space:
            id = gl.GLuint(texture_id)
            gl.glDeleteTextures(1, id)
        else:
            self.object_space._doomed_textures.append(texture_id)

    def delete_buffer(self, buffer_id):
        if self.object_space is gl.current_context.object_space and False:
            id = gl.GLuint(buffer_id)
            gl.glDeleteBuffers(1, id)
        else:
            self.object_space._doomed_buffers.append(buffer_id)

    def get_info(self):
        return self._info
# okay decompiling out\pyglet.gl.base.pyc
