# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.gdkpixbuf2
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from ..pyglet.gl import *
from ..pyglet.image import *
from ..pyglet.image.codecs import *
from pyglet.image.codecs import gif
import pyglet.lib, pyglet.window
gdk = pyglet.lib.load_library('gdk-x11-2.0')
gdkpixbuf = pyglet.lib.load_library('gdk_pixbuf-2.0')
GdkPixbufLoader = c_void_p
GdkPixbuf = c_void_p
gdkpixbuf.gdk_pixbuf_loader_new.restype = GdkPixbufLoader
gdkpixbuf.gdk_pixbuf_loader_get_pixbuf.restype = GdkPixbuf
gdkpixbuf.gdk_pixbuf_get_pixels.restype = c_void_p
gdkpixbuf.gdk_pixbuf_loader_get_animation.restype = c_void_p
gdkpixbuf.gdk_pixbuf_animation_get_iter.restype = c_void_p
gdkpixbuf.gdk_pixbuf_animation_iter_get_pixbuf.restype = GdkPixbuf

class GTimeVal(Structure):
    _fields_ = [
     (
      'tv_sec', c_long),
     (
      'tv_usec', c_long)]


class GdkPixbuf2ImageDecoder(ImageDecoder):

    def get_file_extensions(self):
        return [
         '.png', '.xpm', '.jpg', '.jpeg', '.tif', '.tiff', 
         '.pnm', 
         '.ras', '.bmp', '.gif']

    def get_animation_file_extensions(self):
        return [
         '.gif', '.ani']

    def _load(self, file, filename, load_func):
        data = file.read()
        loader = gdkpixbuf.gdk_pixbuf_loader_new()
        gdkpixbuf.gdk_pixbuf_loader_write(loader, data, len(data), None)
        if not gdkpixbuf.gdk_pixbuf_loader_close(loader, None):
            raise ImageDecodeException(filename)
        result = load_func(loader)
        if not result:
            raise ImageDecodeException('Unable to load: %s' % filename)
        return result

    def _pixbuf_to_image(self, pixbuf):
        width = gdkpixbuf.gdk_pixbuf_get_width(pixbuf)
        height = gdkpixbuf.gdk_pixbuf_get_height(pixbuf)
        channels = gdkpixbuf.gdk_pixbuf_get_n_channels(pixbuf)
        rowstride = gdkpixbuf.gdk_pixbuf_get_rowstride(pixbuf)
        pixels = gdkpixbuf.gdk_pixbuf_get_pixels(pixbuf)
        buffer = (c_ubyte * (rowstride * height))()
        memmove(buffer, pixels, rowstride * (height - 1) + width * channels)
        gdk.g_object_unref(pixbuf)
        if channels == 3:
            format = 'RGB'
        else:
            format = 'RGBA'
        return ImageData(width, height, format, buffer, -rowstride)

    def decode(self, file, filename):
        pixbuf = self._load(file, filename, gdkpixbuf.gdk_pixbuf_loader_get_pixbuf)
        return self._pixbuf_to_image(pixbuf)

    def decode_animation(self, file, filename):
        gif_stream = gif.read(file)
        delays = [ image.delay for image in gif_stream.images ]
        file.seek(0)
        anim = self._load(file, filename, gdkpixbuf.gdk_pixbuf_loader_get_animation)
        time = GTimeVal(0, 0)
        iter = gdkpixbuf.gdk_pixbuf_animation_get_iter(anim, byref(time))
        frames = []
        for control_delay in delays:
            pixbuf = gdkpixbuf.gdk_pixbuf_animation_iter_get_pixbuf(iter)
            image = self._pixbuf_to_image(pixbuf)
            frames.append(AnimationFrame(image, control_delay))
            gdk_delay = gdkpixbuf.gdk_pixbuf_animation_iter_get_delay_time(iter)
            gdk_delay *= 1000
            if gdk_delay == -1:
                break
            us = time.tv_usec + gdk_delay
            time.tv_sec += us // 1000000
            time.tv_usec = us % 1000000
            gdkpixbuf.gdk_pixbuf_animation_iter_advance(iter, byref(time))

        return Animation(frames)


def get_decoders():
    return [
     GdkPixbuf2ImageDecoder()]


def get_encoders():
    return []


def init():
    gdk.g_type_init()


init()
# okay decompiling out\pyglet.image.codecs.gdkpixbuf2.pyc
