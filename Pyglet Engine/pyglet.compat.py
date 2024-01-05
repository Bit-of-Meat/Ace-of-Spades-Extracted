# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.compat
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import sys, itertools
if sys.version_info[0] == 2:
    if sys.version_info[1] < 6:

        def izip_longest(*args, **kwds):
            fillvalue = kwds.get('fillvalue')

            def sentinel(counter=([fillvalue] * (len(args) - 1)).pop):
                yield counter()

            fillers = itertools.repeat(fillvalue)
            iters = [ itertools.chain(it, sentinel(), fillers) for it in args ]
            try:
                for tup in itertools.izip(*iters):
                    yield tup

            except IndexError:
                pass


    else:
        izip_longest = itertools.izip_longest
else:
    izip_longest = itertools.zip_longest
if sys.version_info[0] >= 3:
    import io

    def asbytes(s):
        if isinstance(s, bytes):
            return s
        return s.encode('utf-8')


    def asstr(s):
        if isinstance(s, str):
            return s
        return s.decode('utf-8')


    bytes_type = bytes
    BytesIO = io.BytesIO
else:
    import StringIO
    asbytes = str
    asstr = str
    bytes_type = str
    BytesIO = StringIO.StringIO
# okay decompiling out\pyglet.compat.pyc
