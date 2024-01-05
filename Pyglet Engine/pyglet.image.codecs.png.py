# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.png
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import array
from ..pyglet.gl import *
from ..pyglet.image import *
from ..pyglet.image.codecs import *
import pyglet.image.codecs.pypng

class PNGImageDecoder(ImageDecoder):

    def get_file_extensions(self):
        return [
         '.png']

    def decode(self, file, filename):
        try:
            reader = pyglet.image.codecs.pypng.Reader(file=file)
            width, height, pixels, metadata = reader.read()
        except Exception as e:
            raise ImageDecodeException('PyPNG cannot read %r: %s' % (filename or file, e))

        if metadata['greyscale']:
            if metadata['has_alpha']:
                format = 'LA'
            else:
                format = 'L'
        elif metadata['has_alpha']:
            format = 'RGBA'
        else:
            format = 'RGB'
        pitch = len(format) * width
        return ImageData(width, height, format, pixels.tostring(), -pitch)


class PNGImageEncoder(ImageEncoder):

    def get_file_extensions(self):
        return [
         '.png']

    def encode(self, image, file, filename):
        image = image.get_image_data()
        has_alpha = 'A' in image.format
        greyscale = len(image.format) < 3
        if has_alpha:
            if greyscale:
                image.format = 'LA'
            else:
                image.format = 'RGBA'
        elif greyscale:
            image.format = 'L'
        else:
            image.format = 'RGB'
        image.pitch = -(image.width * len(image.format))
        writer = pyglet.image.codecs.pypng.Writer(image.width, image.height, bytes_per_sample=1, greyscale=greyscale, has_alpha=has_alpha)
        data = array.array('B')
        data.fromstring(image.data)
        writer.write_array(file, data)


def get_decoders():
    return [
     PNGImageDecoder()]


def get_encoders():
    return [
     PNGImageEncoder()]
# okay decompiling out\pyglet.image.codecs.png.pyc
