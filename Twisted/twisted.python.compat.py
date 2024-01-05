# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.compat
from __future__ import absolute_import, division
import inspect, os, socket, string, struct, sys
from types import MethodType as _MethodType
from io import TextIOBase, IOBase
if sys.version_info < (3, 0):
    _PY3 = False
else:
    _PY3 = True

def currentframe(n=0):
    f = inspect.currentframe()
    for x in range(n + 1):
        f = f.f_back

    return f


def inet_pton(af, addr):
    if af == socket.AF_INET:
        return socket.inet_aton(addr)
    if af == getattr(socket, 'AF_INET6', 'AF_INET6'):
        if [ x for x in addr if x not in string.hexdigits + ':.' ]:
            raise ValueError('Illegal characters: %r' % (('').join(x),))
        parts = addr.split(':')
        elided = parts.count('')
        ipv4Component = '.' in parts[-1]
        if len(parts) > 8 - ipv4Component or elided > 3:
            raise ValueError('Syntactically invalid address')
        if elided == 3:
            return '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        if elided:
            zeros = [
             '0'] * (8 - len(parts) - ipv4Component + elided)
            if addr.startswith('::'):
                parts[:2] = zeros
            elif addr.endswith('::'):
                parts[(-2):] = zeros
            else:
                idx = parts.index('')
                parts[idx:(idx + 1)] = zeros
            if len(parts) != 8 - ipv4Component:
                raise ValueError('Syntactically invalid address')
        elif len(parts) != 8 - ipv4Component:
            raise ValueError('Syntactically invalid address')
        if ipv4Component:
            if parts[-1].count('.') != 3:
                raise ValueError('Syntactically invalid address')
            rawipv4 = socket.inet_aton(parts[-1])
            unpackedipv4 = struct.unpack('!HH', rawipv4)
            parts[(-1):] = [ hex(x)[2:] for x in unpackedipv4 ]
        parts = [ int(x, 16) for x in parts ]
        return struct.pack('!8H', *parts)
    raise socket.error(97, 'Address family not supported by protocol')


def inet_ntop(af, addr):
    if af == socket.AF_INET:
        return socket.inet_ntoa(addr)
    else:
        if af == socket.AF_INET6:
            if len(addr) != 16:
                raise ValueError('address length incorrect')
            parts = struct.unpack('!8H', addr)
            curBase = bestBase = None
            for i in range(8):
                if not parts[i]:
                    if curBase is None:
                        curBase = i
                        curLen = 0
                    curLen += 1
                elif curBase is not None:
                    bestLen = None
                    if bestBase is None or curLen > bestLen:
                        bestBase = curBase
                        bestLen = curLen
                    curBase = None

            if curBase is not None and (bestBase is None or curLen > bestLen):
                bestBase = curBase
                bestLen = curLen
            parts = [ hex(x)[2:] for x in parts ]
            if bestBase is not None:
                parts[bestBase:(bestBase + bestLen)] = [
                 '']
            if parts[0] == '':
                parts.insert(0, '')
            if parts[-1] == '':
                parts.insert(len(parts) - 1, '')
            return (':').join(parts)
        raise socket.error(97, 'Address family not supported by protocol')
        return


try:
    socket.AF_INET6
except AttributeError:
    socket.AF_INET6 = 'AF_INET6'

try:
    socket.inet_pton(socket.AF_INET6, '::')
except (AttributeError, NameError, socket.error):
    socket.inet_pton = inet_pton
    socket.inet_ntop = inet_ntop

adict = dict
if _PY3:
    del adict
    del inet_pton
    del inet_ntop
set = set
frozenset = frozenset
try:
    from functools import reduce
except ImportError:
    reduce = reduce

def execfile(filename, globals, locals=None):
    if locals is None:
        locals = globals
    fin = open(filename, 'rbU')
    try:
        source = fin.read()
    finally:
        fin.close()

    code = compile(source, filename, 'exec')
    exec code in globals, locals
    return


try:
    cmp = cmp
except NameError:

    def cmp(a, b):
        if a < b:
            return -1
        else:
            if a == b:
                return 0
            return 1


def comparable(klass):
    if not _PY3:
        return klass

    def __eq__(self, other):
        c = self.__cmp__(other)
        if c is NotImplemented:
            return c
        return c == 0

    def __ne__(self, other):
        c = self.__cmp__(other)
        if c is NotImplemented:
            return c
        return c != 0

    def __lt__(self, other):
        c = self.__cmp__(other)
        if c is NotImplemented:
            return c
        return c < 0

    def __le__(self, other):
        c = self.__cmp__(other)
        if c is NotImplemented:
            return c
        return c <= 0

    def __gt__(self, other):
        c = self.__cmp__(other)
        if c is NotImplemented:
            return c
        return c > 0

    def __ge__(self, other):
        c = self.__cmp__(other)
        if c is NotImplemented:
            return c
        return c >= 0

    klass.__lt__ = __lt__
    klass.__gt__ = __gt__
    klass.__le__ = __le__
    klass.__ge__ = __ge__
    klass.__eq__ = __eq__
    klass.__ne__ = __ne__
    return klass


if _PY3:
    unicode = str
    long = int
else:
    unicode = unicode
    long = long

def ioType(fileIshObject, default=unicode):
    if isinstance(fileIshObject, TextIOBase):
        return unicode
    else:
        if isinstance(fileIshObject, IOBase):
            return bytes
        encoding = getattr(fileIshObject, 'encoding', None)
        import codecs
        if isinstance(fileIshObject, (codecs.StreamReader, codecs.StreamWriter)):
            if encoding:
                return unicode
            else:
                return bytes

        if not _PY3:
            if isinstance(fileIshObject, file):
                if encoding is not None:
                    return basestring
                else:
                    return bytes

            from cStringIO import InputType, OutputType
            from StringIO import StringIO
            if isinstance(fileIshObject, (StringIO, InputType, OutputType)):
                return bytes
        return default


def nativeString(s):
    if not isinstance(s, (bytes, unicode)):
        raise TypeError('%r is neither bytes nor unicode' % s)
    if _PY3:
        if isinstance(s, bytes):
            return s.decode('ascii')
        s.encode('ascii')
    else:
        if isinstance(s, unicode):
            return s.encode('ascii')
        s.decode('ascii')
    return s


if _PY3:

    def reraise(exception, traceback):
        raise exception.with_traceback(traceback)


else:
    exec 'def reraise(exception, traceback):\n        raise exception.__class__, exception, traceback'
reraise.__doc__ = '\nRe-raise an exception, with an optional traceback, in a way that is compatible\nwith both Python 2 and Python 3.\n\nNote that on Python 3, re-raised exceptions will be mutated, with their\nC{__traceback__} attribute being set.\n\n@param exception: The exception instance.\n@param traceback: The traceback to use, or C{None} indicating a new traceback.\n'
if _PY3:
    from io import StringIO as NativeStringIO
else:
    from io import BytesIO as NativeStringIO
if _PY3:

    def iterbytes(originalBytes):
        for i in range(len(originalBytes)):
            yield originalBytes[i:i + 1]


    def intToBytes(i):
        return ('%d' % i).encode('ascii')


    def lazyByteSlice(object, offset=0, size=None):
        if size is None:
            return object[offset:]
        else:
            return object[offset:offset + size]
            return


    def networkString(s):
        if not isinstance(s, unicode):
            raise TypeError('Can only convert text to bytes on Python 3')
        return s.encode('ascii')


else:

    def iterbytes(originalBytes):
        return originalBytes


    def intToBytes(i):
        return '%d' % i


    lazyByteSlice = buffer

    def networkString(s):
        if not isinstance(s, str):
            raise TypeError('Can only pass-through bytes on Python 2')
        s.decode('ascii')
        return s


iterbytes.__doc__ = '\nReturn an iterable wrapper for a C{bytes} object that provides the behavior of\niterating over C{bytes} on Python 2.\n\nIn particular, the results of iteration are the individual bytes (rather than\nintegers as on Python 3).\n\n@param originalBytes: A C{bytes} object that will be wrapped.\n'
intToBytes.__doc__ = '\nConvert the given integer into C{bytes}, as ASCII-encoded Arab numeral.\n\nIn other words, this is equivalent to calling C{bytes} in Python 2 on an\ninteger.\n\n@param i: The C{int} to convert to C{bytes}.\n@rtype: C{bytes}\n'
networkString.__doc__ = '\nConvert the native string type to C{bytes} if it is not already C{bytes} using\nASCII encoding if conversion is necessary.\n\nThis is useful for sending text-like bytes that are constructed using string\ninterpolation.  For example, this is safe on Python 2 and Python 3:\n\n    networkString("Hello %d" % (n,))\n\n@param s: A native string to convert to bytes if necessary.\n@type s: C{str}\n\n@raise UnicodeError: The input string is not ASCII encodable/decodable.\n@raise TypeError: The input is neither C{bytes} nor C{unicode}.\n\n@rtype: C{bytes}\n'
try:
    StringType = basestring
except NameError:
    StringType = str

try:
    from types import InstanceType
except ImportError:
    InstanceType = object

try:
    from types import FileType
except ImportError:
    FileType = IOBase

if _PY3:
    import urllib.parse as urllib_parse
    from html import escape
    from urllib.parse import quote as urlquote
else:
    import urlparse as urllib_parse
    from cgi import escape
    from urllib import quote as urlquote
if _PY3:

    def iteritems(d):
        return d.items()


    def items(d):
        return list(d.items())


    xrange = range
    izip = zip
else:

    def iteritems(d):
        return d.iteritems()


    def items(d):
        return d.items()


    xrange = xrange
    from itertools import izip
    izip
iteritems.__doc__ = '\nReturn an iterable of the items of C{d}.\n\n@type d: L{dict}\n@rtype: iterable\n'
items.__doc__ = '\nReturn a list of the items of C{d}.\n\n@type d: L{dict}\n@rtype: L{list}\n'

def bytesEnviron():
    if not _PY3:
        return dict(os.environ)
    target = dict()
    for x, y in os.environ.items():
        target[os.environ.encodekey(x)] = os.environ.encodevalue(y)

    return target


def _constructMethod(cls, name, self):
    func = cls.__dict__[name]
    if _PY3:
        return _MethodType(func, self)
    return _MethodType(func, self, cls)


if _PY3:
    from collections import OrderedDict
else:
    from twisted.python.util import OrderedDict
__all__ = ['reraise', 
 'execfile', 
 'frozenset', 
 'reduce', 
 'set', 
 'cmp', 
 'comparable', 
 'nativeString', 
 'NativeStringIO', 
 'networkString', 
 'unicode', 
 'iterbytes', 
 'intToBytes', 
 'lazyByteSlice', 
 'StringType', 
 'InstanceType', 
 'FileType', 
 'items', 
 'iteritems', 
 'xrange', 
 'urllib_parse', 
 'bytesEnviron', 
 'OrderedDict', 
 'escape', 
 'urlquote']
# okay decompiling out\twisted.python.compat.pyc
