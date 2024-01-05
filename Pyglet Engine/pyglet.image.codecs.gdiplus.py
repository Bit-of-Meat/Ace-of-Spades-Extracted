# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.image.codecs.gdiplus
__docformat__ = 'restructuredtext'
__version__ = '$Id: pil.py 163 2006-11-13 04:15:46Z Alex.Holkner $'
from ..ctypes import *
from pyglet.com import IUnknown
from ..pyglet.gl import *
from ..pyglet.image import *
from ..pyglet.image.codecs import *
from ..pyglet.libs.win32.constants import *
from ..pyglet.libs.win32.types import *
ole32 = windll.ole32
kernel32 = windll.kernel32
gdiplus = windll.gdiplus
LPSTREAM = c_void_p
REAL = c_float
PixelFormat1bppIndexed = 196865
PixelFormat4bppIndexed = 197634
PixelFormat8bppIndexed = 198659
PixelFormat16bppGrayScale = 1052676
PixelFormat16bppRGB555 = 135173
PixelFormat16bppRGB565 = 135174
PixelFormat16bppARGB1555 = 397319
PixelFormat24bppRGB = 137224
PixelFormat32bppRGB = 139273
PixelFormat32bppARGB = 2498570
PixelFormat32bppPARGB = 925707
PixelFormat48bppRGB = 1060876
PixelFormat64bppARGB = 3424269
PixelFormat64bppPARGB = 29622286
PixelFormatMax = 15
ImageLockModeRead = 1
ImageLockModeWrite = 2
ImageLockModeUserInputBuf = 4

class GdiplusStartupInput(Structure):
    _fields_ = [
     (
      'GdiplusVersion', c_uint32),
     (
      'DebugEventCallback', c_void_p),
     (
      'SuppressBackgroundThread', BOOL),
     (
      'SuppressExternalCodecs', BOOL)]


class GdiplusStartupOutput(Structure):
    _fields = [
     (
      'NotificationHookProc', c_void_p),
     (
      'NotificationUnhookProc', c_void_p)]


class BitmapData(Structure):
    _fields_ = [
     (
      'Width', c_uint),
     (
      'Height', c_uint),
     (
      'Stride', c_int),
     (
      'PixelFormat', c_int),
     (
      'Scan0', POINTER(c_byte)),
     (
      'Reserved', POINTER(c_uint))]


class Rect(Structure):
    _fields_ = [
     (
      'X', c_int),
     (
      'Y', c_int),
     (
      'Width', c_int),
     (
      'Height', c_int)]


kernel32.GlobalAlloc.restype = HGLOBAL
kernel32.GlobalLock.restype = c_void_p
PropertyTagFrameDelay = 20736

class PropertyItem(Structure):
    _fields_ = [
     (
      'id', c_uint),
     (
      'length', c_ulong),
     (
      'type', c_short),
     (
      'value', c_void_p)]


class GDIPlusDecoder(ImageDecoder):

    def get_file_extensions(self):
        return [
         '.bmp', '.gif', '.jpg', '.jpeg', '.exif', '.png', 
         '.tif', 
         '.tiff']

    def get_animation_file_extensions(self):
        return [
         '.gif']

    def _load_bitmap(self, file, filename):
        data = file.read()
        hglob = kernel32.GlobalAlloc(GMEM_MOVEABLE, len(data))
        ptr = kernel32.GlobalLock(hglob)
        memmove(ptr, data, len(data))
        kernel32.GlobalUnlock(hglob)
        self.stream = IUnknown()
        ole32.CreateStreamOnHGlobal(hglob, True, byref(self.stream))
        bitmap = c_void_p()
        status = gdiplus.GdipCreateBitmapFromStream(self.stream, byref(bitmap))
        if status != 0:
            self.stream.Release()
            raise ImageDecodeException('GDI+ cannot load %r' % (filename or file))
        return bitmap

    def _get_image(self, bitmap):
        width = REAL()
        height = REAL()
        gdiplus.GdipGetImageDimension(bitmap, byref(width), byref(height))
        width = int(width.value)
        height = int(height.value)
        pf = c_int()
        gdiplus.GdipGetImagePixelFormat(bitmap, byref(pf))
        pf = pf.value
        format = 'BGRA'
        if pf == PixelFormat24bppRGB:
            format = 'BGR'
        elif pf == PixelFormat32bppRGB:
            pass
        elif pf == PixelFormat32bppARGB:
            pass
        elif pf in (PixelFormat16bppARGB1555, PixelFormat32bppPARGB,
         PixelFormat64bppARGB, PixelFormat64bppPARGB):
            pf = PixelFormat32bppARGB
        else:
            format = 'BGR'
            pf = PixelFormat24bppRGB
        rect = Rect()
        rect.X = 0
        rect.Y = 0
        rect.Width = width
        rect.Height = height
        bitmap_data = BitmapData()
        gdiplus.GdipBitmapLockBits(bitmap, byref(rect), ImageLockModeRead, pf, byref(bitmap_data))
        buffer = create_string_buffer(bitmap_data.Stride * height)
        memmove(buffer, bitmap_data.Scan0, len(buffer))
        gdiplus.GdipBitmapUnlockBits(bitmap, byref(bitmap_data))
        return ImageData(width, height, format, buffer, -bitmap_data.Stride)

    def _delete_bitmap(self, bitmap):
        gdiplus.GdipDisposeImage(bitmap)
        self.stream.Release()

    def decode(self, file, filename):
        bitmap = self._load_bitmap(file, filename)
        image = self._get_image(bitmap)
        self._delete_bitmap(bitmap)
        return image

    def decode_animation(self, file, filename):
        bitmap = self._load_bitmap(file, filename)
        dimension_count = c_uint()
        gdiplus.GdipImageGetFrameDimensionsCount(bitmap, byref(dimension_count))
        if dimension_count.value < 1:
            self._delete_bitmap(bitmap)
            raise ImageDecodeException('Image has no frame dimensions')
        dimensions = (c_void_p * dimension_count.value)()
        gdiplus.GdipImageGetFrameDimensionsList(bitmap, dimensions, dimension_count.value)
        frame_count = c_uint()
        gdiplus.GdipImageGetFrameCount(bitmap, dimensions, byref(frame_count))
        prop_id = PropertyTagFrameDelay
        prop_size = c_uint()
        gdiplus.GdipGetPropertyItemSize(bitmap, prop_id, byref(prop_size))
        prop_buffer = c_buffer(prop_size.value)
        prop_item = cast(prop_buffer, POINTER(PropertyItem)).contents
        gdiplus.GdipGetPropertyItem(bitmap, prop_id, prop_size.value, prop_buffer)
        n_delays = prop_item.length / sizeof(c_long)
        delays = cast(prop_item.value, POINTER(c_long * n_delays)).contents
        frames = []
        for i in range(frame_count.value):
            gdiplus.GdipImageSelectActiveFrame(bitmap, dimensions, i)
            image = self._get_image(bitmap)
            delay = delays[i]
            if delay <= 1:
                delay = 10
            frames.append(AnimationFrame(image, delay / 100.0))

        self._delete_bitmap(bitmap)
        return Animation(frames)


def get_decoders():
    return [
     GDIPlusDecoder()]


def get_encoders():
    return []


def init():
    token = c_ulong()
    startup_in = GdiplusStartupInput()
    startup_in.GdiplusVersion = 1
    startup_out = GdiplusStartupOutput()
    gdiplus.GdiplusStartup(byref(token), byref(startup_in), byref(startup_out))


init()
# okay decompiling out\pyglet.image.codecs.gdiplus.pyc
