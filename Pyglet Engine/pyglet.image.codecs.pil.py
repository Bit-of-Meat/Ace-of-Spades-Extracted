# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.pil
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import os.path
from ..pyglet.gl import *
from ..pyglet.image import *
from ..pyglet.image.codecs import *
import Image

class PILImageDecoder(ImageDecoder):

    def get_file_extensions(self):
        return [
         '.bmp', '.cur', '.gif', '.ico', '.jpg', '.jpeg', 
         '.pcx', '.png', 
         '.tga', '.tif', '.tiff', 
         '.xbm', '.xpm']

    def decode(self, file, filename):
        try:
            image = Image.open(file)
        except Exception as e:
            raise ImageDecodeException('PIL cannot read %r: %s' % (filename or file, e))

        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        if image.mode in ('1', 'P'):
            image = image.convert()
        if image.mode not in ('L', 'LA', 'RGB', 'RGBA'):
            raise ImageDecodeException('Unsupported mode "%s"' % image.mode)
        type = GL_UNSIGNED_BYTE
        width, height = image.size
        return ImageData(width, height, image.mode, image.tostring())


class PILImageEncoder(ImageEncoder):

    def get_file_extensions(self):
        return [
         '.bmp', '.eps', '.gif', '.jpg', '.jpeg', 
         '.pcx', 
         '.png', '.ppm', '.tiff', '.xbm']

    def encode(self, image, file, filename):
        pil_format = filename and os.path.splitext(filename)[1][1:] or 'png'
        if pil_format.lower() == 'jpg':
            pil_format = 'JPEG'
        image = image.get_image_data()
        format = image.format
        if format != 'RGB':
            format = 'RGBA'
        pitch = -(image.width * len(format))
        pil_image = Image.fromstring(format, (image.width, image.height), image.get_data(format, pitch))
        try:
            pil_image.save(file, pil_format)
        except Exception as e:
            raise ImageEncodeException(e)


def get_decoders():
    return [PILImageDecoder()]


def get_encoders():
    return [
     PILImageEncoder()]
# okay decompiling out\pyglet.image.codecs.pil.pyc
