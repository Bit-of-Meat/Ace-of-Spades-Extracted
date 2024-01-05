# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.quartz
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
from ..ctypes import *
from pyglet.image import ImageData, Animation, AnimationFrame
from ..pyglet.image.codecs import *
import Quartz, CoreFoundation, LaunchServices

class QuartzImageDecoder(ImageDecoder):

    def _get_all_file_extensions(self):
        types = Quartz.CGImageSourceCopyTypeIdentifiers()
        extensions = []
        for uti in types:
            desc = LaunchServices.UTTypeCopyDescription(uti)
            decl = LaunchServices.UTTypeCopyDeclaration(uti)
            try:
                spec = decl['UTTypeTagSpecification']
                ext = spec['public.filename-extension']
                if str(ext) == ext:
                    extensions.append('.' + ext)
                else:
                    extensions.extend([ '.' + x for x in ext ])
            except:
                pass

        return extensions

    def get_file_extensions(self):
        return [
         '.bmp', '.cur', '.gif', '.ico', '.jp2', '.jpg', '.jpeg', 
         '.pcx', 
         '.png', '.tga', '.tif', '.tiff', '.xbm', '.xpm']

    def get_animation_file_extensions(self):
        return [
         '.gif']

    def _get_format(self, imageRef):
        bpp = Quartz.CGImageGetBitsPerPixel(imageRef)
        if bpp == 8:
            return 'L'
        if bpp == 16:
            return 'LA'
        if bpp == 24:
            return 'RGB'
        if bpp == 32:
            info = Quartz.CGImageGetBitmapInfo(imageRef)
            alphaInfo = info & Quartz.kCGBitmapAlphaInfoMask
            if alphaInfo in [Quartz.kCGImageAlphaPremultipliedFirst,
             Quartz.kCGImageAlphaFirst,
             Quartz.kCGImageAlphaNoneSkipFirst]:
                return 'BGRA'
            return 'RGBA'
        raise ImageDecodeException(filename or file)

    def _get_pyglet_ImageData_from_source_at_index(self, sourceRef, index):
        imageRef = Quartz.CGImageSourceCreateImageAtIndex(sourceRef, index, None)
        width = Quartz.CGImageGetWidth(imageRef)
        height = Quartz.CGImageGetHeight(imageRef)
        bytesPerRow = Quartz.CGImageGetBytesPerRow(imageRef)
        format = self._get_format(imageRef)
        imageData = Quartz.CGDataProviderCopyData(Quartz.CGImageGetDataProvider(imageRef))
        bufferSize = CoreFoundation.CFDataGetLength(imageData)
        buffer = (c_byte * bufferSize)()
        imageData.getBytes_length_(buffer, bufferSize)
        del imageRef
        del imageData
        pitch = bytesPerRow
        return ImageData(width, height, format, buffer, -pitch)

    def decode(self, file, filename):
        file_bytes = file.read()
        data = CoreFoundation.CFDataCreate(None, file_bytes, len(file_bytes))
        sourceRef = Quartz.CGImageSourceCreateWithData(data, None)
        image = self._get_pyglet_ImageData_from_source_at_index(sourceRef, 0)
        del data
        del sourceRef
        return image

    def decode_animation(self, file, filename):
        file_bytes = file.read()
        data = CoreFoundation.CFDataCreate(None, file_bytes, len(file_bytes))
        sourceRef = Quartz.CGImageSourceCreateWithData(data, None)
        count = Quartz.CGImageSourceGetCount(sourceRef)
        frames = []
        for index in range(count):
            duration = 0.1
            props = Quartz.CGImageSourceCopyPropertiesAtIndex(sourceRef, index, None)
            if Quartz.kCGImagePropertyGIFDictionary in props:
                gif_props = props[Quartz.kCGImagePropertyGIFDictionary]
                if Quartz.kCGImagePropertyGIFDelayTime in gif_props:
                    duration = gif_props[Quartz.kCGImagePropertyGIFDelayTime]
            image = self._get_pyglet_ImageData_from_source_at_index(sourceRef, index)
            frames.append(AnimationFrame(image, duration))

        del data
        del sourceRef
        return Animation(frames)


def get_decoders():
    return [
     QuartzImageDecoder()]


def get_encoders():
    return []
# okay decompiling out\pyglet.image.codecs.quartz.pyc
