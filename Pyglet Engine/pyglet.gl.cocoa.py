# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.gl.cocoa
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from pyglet.gl.base import Config, CanvasConfig, Context
from ..pyglet.libs.darwin import *
from pyglet.gl import ContextException
from pyglet.gl import gl
from pyglet.gl import agl
from pyglet.canvas.cocoa import CocoaCanvas
_gl_attributes = {'double_buffer': NSOpenGLPFADoubleBuffer, 
   'stereo': NSOpenGLPFAStereo, 
   'buffer_size': NSOpenGLPFAColorSize, 
   'sample_buffers': NSOpenGLPFASampleBuffers, 
   'samples': NSOpenGLPFASamples, 
   'aux_buffers': NSOpenGLPFAAuxBuffers, 
   'alpha_size': NSOpenGLPFAAlphaSize, 
   'depth_size': NSOpenGLPFADepthSize, 
   'stencil_size': NSOpenGLPFAStencilSize, 
   'all_renderers': NSOpenGLPFAAllRenderers, 
   'fullscreen': NSOpenGLPFAFullScreen, 
   'minimum_policy': NSOpenGLPFAMinimumPolicy, 
   'maximum_policy': NSOpenGLPFAMaximumPolicy, 
   'screen_mask': NSOpenGLPFAScreenMask, 
   'color_float': NSOpenGLPFAColorFloat, 
   'offscreen': NSOpenGLPFAOffScreen, 
   'sample_alpha': NSOpenGLPFASampleAlpha, 
   'multisample': NSOpenGLPFAMultisample, 
   'supersample': NSOpenGLPFASupersample}
_boolean_gl_attributes = frozenset([
 NSOpenGLPFAAllRenderers, 
 NSOpenGLPFADoubleBuffer, 
 NSOpenGLPFAStereo, 
 NSOpenGLPFAMinimumPolicy, 
 NSOpenGLPFAMaximumPolicy, 
 NSOpenGLPFAOffScreen, 
 NSOpenGLPFAFullScreen, 
 NSOpenGLPFAColorFloat, 
 NSOpenGLPFAMultisample, 
 NSOpenGLPFASupersample, 
 NSOpenGLPFASampleAlpha])
_fake_gl_attributes = {'red_size': 0, 
   'green_size': 0, 
   'blue_size': 0, 
   'accum_red_size': 0, 
   'accum_green_size': 0, 
   'accum_blue_size': 0, 
   'accum_alpha_size': 0}

class CocoaConfig(Config):

    def match(self, canvas):
        attrs = []
        for name, value in self.get_gl_attributes():
            attr = _gl_attributes.get(name)
            if not attr or not value:
                continue
            attrs.append(attr)
            if attr not in _boolean_gl_attributes:
                attrs.append(int(value))

        attrs.append(NSOpenGLPFAAllRenderers)
        attrs.append(NSOpenGLPFAMaximumPolicy)
        attrs.append(NSOpenGLPFAFullScreen)
        attrs.append(NSOpenGLPFAScreenMask)
        attrs.append(CGDisplayIDToOpenGLDisplayMask(CGMainDisplayID()))
        attrs.append(0)
        pixel_format = NSOpenGLPixelFormat.alloc().initWithAttributes_(attrs)
        if pixel_format is None:
            return []
        else:
            return [
             CocoaCanvasConfig(canvas, self, pixel_format)]
            return


class CocoaCanvasConfig(CanvasConfig):

    def __init__(self, canvas, config, pixel_format):
        super(CocoaCanvasConfig, self).__init__(canvas, config)
        self._pixel_format = pixel_format
        for name, attr in _gl_attributes.items():
            value = self._pixel_format.getValues_forAttribute_forVirtualScreen_(None, attr, 0)
            if value is not None:
                setattr(self, name, value)

        for name, value in _fake_gl_attributes.items():
            setattr(self, name, value)

        return

    def create_context(self, share):
        if share:
            share_context = share._nscontext
        else:
            share_context = None
        nscontext = NSOpenGLContext.alloc().initWithFormat_shareContext_(self._pixel_format, share_context)
        return CocoaContext(self, nscontext, share)

    def compatible(self, canvas):
        return isinstance(canvas, CocoaCanvas)


class CocoaContext(Context):

    def __init__(self, config, nscontext, share):
        super(CocoaContext, self).__init__(config, share)
        self.config = config
        self._nscontext = nscontext

    def attach(self, canvas):
        super(CocoaContext, self).attach(canvas)
        self._nscontext.setView_(canvas.nsview)
        self.set_current()

    def detach(self):
        super(CocoaContext, self).detach()
        self._nscontext.clearDrawable()

    def set_current(self):
        self._nscontext.makeCurrentContext()
        super(CocoaContext, self).set_current()

    def update_geometry(self):
        self._nscontext.update()

    def set_full_screen(self):
        self._nscontext.makeCurrentContext()
        self._nscontext.setFullScreen()

    def destroy(self):
        super(CocoaContext, self).destroy()
        self._nscontext = None
        return

    def set_vsync(self, vsync=True):
        from objc import __version__ as pyobjc_version
        if float(pyobjc_version[:3]) >= 2.3:
            self._nscontext.setValues_forParameter_(vsync, NSOpenGLCPSwapInterval)

    def get_vsync(self):
        value = self._nscontext.getValues_forParameter_(None, NSOpenGLCPSwapInterval)
        return value

    def flip(self):
        self._nscontext.flushBuffer()
# okay decompiling out\pyglet.gl.cocoa.pyc
