# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import os.path, sys
_decoders = []
_decoder_extensions = {}
_decoder_animation_extensions = {}
_encoders = []
_encoder_extensions = {}

class ImageDecodeException(Exception):
    exception_priority = 10


class ImageEncodeException(Exception):
    pass


class ImageDecoder(object):

    def get_file_extensions(self):
        return []

    def get_animation_file_extensions(self):
        return []

    def decode(self, file, filename):
        raise NotImplementedError()

    def decode_animation(self, file, filename):
        raise ImageDecodeException('This decoder cannot decode animations.')


class ImageEncoder(object):

    def get_file_extensions(self):
        return []

    def encode(self, image, file, filename, options={}):
        raise NotImplementedError()


def get_encoders(filename=None):
    encoders = []
    if filename:
        extension = os.path.splitext(filename)[1].lower()
        encoders += _encoder_extensions.get(extension, [])
    encoders += [ e for e in _encoders if e not in encoders ]
    return encoders


def get_decoders(filename=None):
    decoders = []
    if filename:
        extension = os.path.splitext(filename)[1].lower()
        decoders += _decoder_extensions.get(extension, [])
    decoders += [ e for e in _decoders if e not in decoders ]
    return decoders


def get_animation_decoders(filename=None):
    decoders = []
    if filename:
        extension = os.path.splitext(filename)[1].lower()
        decoders += _decoder_animation_extensions.get(extension, [])
    decoders += [ e for e in _decoders if e not in decoders ]
    return decoders


def add_decoders(module):
    for decoder in module.get_decoders():
        _decoders.append(decoder)
        for extension in decoder.get_file_extensions():
            if extension not in _decoder_extensions:
                _decoder_extensions[extension] = []
            _decoder_extensions[extension].append(decoder)

        for extension in decoder.get_animation_file_extensions():
            if extension not in _decoder_animation_extensions:
                _decoder_animation_extensions[extension] = []
            _decoder_animation_extensions[extension].append(decoder)


def add_encoders(module):
    for encoder in module.get_encoders():
        _encoders.append(encoder)
        for extension in encoder.get_file_extensions():
            if extension not in _encoder_extensions:
                _encoder_extensions[extension] = []
            _encoder_extensions[extension].append(encoder)


def add_default_image_codecs():
    try:
        from pyglet.image.codecs import dds
        add_encoders(dds)
        add_decoders(dds)
    except ImportError:
        pass

    if sys.platform == 'darwin':
        try:
            from pyglet import options as pyglet_options
            if pyglet_options['darwin_cocoa']:
                import pyglet.image.codecs.quartz
                add_encoders(quartz)
                add_decoders(quartz)
            else:
                import pyglet.image.codecs.quicktime
                add_encoders(quicktime)
                add_decoders(quicktime)
        except ImportError:
            pass

    if sys.platform in ('win32', 'cygwin'):
        try:
            import pyglet.image.codecs.gdiplus
            add_encoders(gdiplus)
            add_decoders(gdiplus)
        except ImportError:
            pass

    if sys.platform == 'linux2':
        try:
            import pyglet.image.codecs.gdkpixbuf2
            add_encoders(gdkpixbuf2)
            add_decoders(gdkpixbuf2)
        except ImportError:
            pass

    try:
        import pyglet.image.codecs.pil
        add_encoders(pil)
        add_decoders(pil)
    except ImportError:
        pass

    try:
        import pyglet.image.codecs.png
        add_encoders(png)
        add_decoders(png)
    except ImportError:
        pass

    try:
        import pyglet.image.codecs.bmp
        add_encoders(bmp)
        add_decoders(bmp)
    except ImportError:
        pass
# okay decompiling out\pyglet.image.codecs.pyc
