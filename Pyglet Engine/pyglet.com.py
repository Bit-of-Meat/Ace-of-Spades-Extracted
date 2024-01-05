# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.com
import ctypes, sys
if sys.platform != 'win32':
    raise ImportError('pyglet.com requires a Windows build of Python')

class GUID(ctypes.Structure):
    _fields_ = [
     (
      'Data1', ctypes.c_ulong),
     (
      'Data2', ctypes.c_ushort),
     (
      'Data3', ctypes.c_ushort),
     (
      'Data4', ctypes.c_ubyte * 8)]

    def __init__(self, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
        self.Data1 = l
        self.Data2 = w1
        self.Data3 = w2
        self.Data4[:] = (b1, b2, b3, b4, b5, b6, b7, b8)

    def __repr__(self):
        b1, b2, b3, b4, b5, b6, b7, b8 = self.Data4
        return 'GUID(%x, %x, %x, %x, %x, %x, %x, %x, %x, %x, %x)' % (
         self.Data1, self.Data2, self.Data3, b1, b2, b3, b4, b5, b6, b7, b8)


LPGUID = ctypes.POINTER(GUID)
IID = GUID
REFIID = ctypes.POINTER(IID)

class METHOD(object):

    def __init__(self, restype, *args):
        self.restype = restype
        self.argtypes = args

    def get_field(self):
        return ctypes.WINFUNCTYPE(self.restype, *self.argtypes)


class STDMETHOD(METHOD):

    def __init__(self, *args):
        super(STDMETHOD, self).__init__(ctypes.HRESULT, *args)


class COMMethodInstance(object):

    def __init__(self, name, i, method):
        self.name = name
        self.i = i
        self.method = method

    def __get__(self, obj, tp):
        if obj is not None:
            return (lambda *args: self.method.get_field()(self.i, self.name)(obj, *args))
        else:
            raise AttributeError()
            return


class COMInterface(ctypes.Structure):
    _fields_ = [
     (
      'lpVtbl', ctypes.c_void_p)]


class InterfaceMetaclass(type(ctypes.POINTER(COMInterface))):

    def __new__(cls, name, bases, dct):
        methods = []
        for base in bases[::-1]:
            methods.extend(base.__dict__.get('_methods_', ()))

        methods.extend(dct.get('_methods_', ()))
        for i, (n, method) in enumerate(methods):
            dct[n] = COMMethodInstance(n, i, method)

        dct['_type_'] = COMInterface
        return super(InterfaceMetaclass, cls).__new__(cls, name, bases, dct)


class Interface(ctypes.POINTER(COMInterface)):
    __metaclass__ = InterfaceMetaclass


class IUnknown(Interface):
    _methods_ = [
     (
      'QueryInterface', STDMETHOD(REFIID, ctypes.c_void_p)),
     (
      'AddRef', METHOD(ctypes.c_int)),
     (
      'Release', METHOD(ctypes.c_int))]
# okay decompiling out\pyglet.com.pyc
