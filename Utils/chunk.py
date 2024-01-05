# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\chunk


class Chunk:

    def __init__(self, file, align=True, bigendian=True, inclheader=False):
        import struct
        self.closed = False
        self.align = align
        if bigendian:
            strflag = '>'
        else:
            strflag = '<'
        self.file = file
        self.chunkname = file.read(4)
        if len(self.chunkname) < 4:
            raise EOFError
        try:
            self.chunksize = struct.unpack(strflag + 'L', file.read(4))[0]
        except struct.error:
            raise EOFError

        if inclheader:
            self.chunksize = self.chunksize - 8
        self.size_read = 0
        try:
            self.offset = self.file.tell()
        except (AttributeError, IOError):
            self.seekable = False
        else:
            self.seekable = True

    def getname(self):
        return self.chunkname

    def getsize(self):
        return self.chunksize

    def close(self):
        if not self.closed:
            try:
                self.skip()
            finally:
                self.closed = True

    def isatty(self):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        return False

    def seek(self, pos, whence=0):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if not self.seekable:
            raise IOError, 'cannot seek'
        if whence == 1:
            pos = pos + self.size_read
        elif whence == 2:
            pos = pos + self.chunksize
        if pos < 0 or pos > self.chunksize:
            raise RuntimeError
        self.file.seek(self.offset + pos, 0)
        self.size_read = pos

    def tell(self):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        return self.size_read

    def read(self, size=-1):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if self.size_read >= self.chunksize:
            return ''
        if size < 0:
            size = self.chunksize - self.size_read
        if size > self.chunksize - self.size_read:
            size = self.chunksize - self.size_read
        data = self.file.read(size)
        self.size_read = self.size_read + len(data)
        if self.size_read == self.chunksize and self.align and self.chunksize & 1:
            dummy = self.file.read(1)
            self.size_read = self.size_read + len(dummy)
        return data

    def skip(self):
        if self.closed:
            raise ValueError, 'I/O operation on closed file'
        if self.seekable:
            try:
                n = self.chunksize - self.size_read
                if self.align and self.chunksize & 1:
                    n = n + 1
                self.file.seek(n, 1)
                self.size_read = self.size_read + n
                return
            except IOError:
                pass

        while self.size_read < self.chunksize:
            n = min(8192, self.chunksize - self.size_read)
            dummy = self.read(n)
            if not dummy:
                raise EOFError
# okay decompiling out\chunk.pyc
