# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.zipstream
import zipfile, os.path, zlib, struct
_fileHeaderSize = struct.calcsize(zipfile.structFileHeader)

class ChunkingZipFile(zipfile.ZipFile):

    def readfile(self, name):
        if self.mode not in ('r', 'a'):
            raise RuntimeError('read() requires mode "r" or "a"')
        if not self.fp:
            raise RuntimeError('Attempt to read ZIP archive that was already closed')
        zinfo = self.getinfo(name)
        self.fp.seek(zinfo.header_offset, 0)
        fheader = self.fp.read(_fileHeaderSize)
        if fheader[0:4] != zipfile.stringFileHeader:
            raise zipfile.BadZipfile('Bad magic number for file header')
        fheader = struct.unpack(zipfile.structFileHeader, fheader)
        fname = self.fp.read(fheader[zipfile._FH_FILENAME_LENGTH])
        if fheader[zipfile._FH_EXTRA_FIELD_LENGTH]:
            self.fp.read(fheader[zipfile._FH_EXTRA_FIELD_LENGTH])
        if fname != zinfo.orig_filename:
            raise zipfile.BadZipfile('File name in directory "%s" and header "%s" differ.' % (
             zinfo.orig_filename, fname))
        if zinfo.compress_type == zipfile.ZIP_STORED:
            return ZipFileEntry(self, zinfo.compress_size)
        if zinfo.compress_type == zipfile.ZIP_DEFLATED:
            return DeflatedZipFileEntry(self, zinfo.compress_size)
        raise zipfile.BadZipfile('Unsupported compression method %d for file %s' % (
         zinfo.compress_type, name))


class _FileEntry(object):

    def __init__(self, chunkingZipFile, length):
        self.chunkingZipFile = chunkingZipFile
        self.fp = self.chunkingZipFile.fp
        self.length = length
        self.finished = 0
        self.closed = False

    def isatty(self):
        return False

    def close(self):
        self.closed = True
        self.finished = 1
        del self.fp

    def readline(self):
        bytes = ''
        for byte in iter((lambda : self.read(1)), ''):
            bytes += byte
            if byte == '\n':
                break

        return bytes

    def next(self):
        nextline = self.readline()
        if nextline:
            return nextline
        raise StopIteration()

    def readlines(self):
        return list(self)

    def xreadlines(self):
        return self

    def __iter__(self):
        return self


class ZipFileEntry(_FileEntry):

    def __init__(self, chunkingZipFile, length):
        _FileEntry.__init__(self, chunkingZipFile, length)
        self.readBytes = 0

    def tell(self):
        return self.readBytes

    def read(self, n=None):
        if n is None:
            n = self.length - self.readBytes
        if n == 0 or self.finished:
            return ''
        data = self.chunkingZipFile.fp.read(min(n, self.length - self.readBytes))
        self.readBytes += len(data)
        if self.readBytes == self.length or len(data) < n:
            self.finished = 1
        return data


class DeflatedZipFileEntry(_FileEntry):

    def __init__(self, chunkingZipFile, length):
        _FileEntry.__init__(self, chunkingZipFile, length)
        self.returnedBytes = 0
        self.readBytes = 0
        self.decomp = zlib.decompressobj(-15)
        self.buffer = ''

    def tell(self):
        return self.returnedBytes

    def read(self, n=None):
        if self.finished:
            return ''
        else:
            if n is None:
                result = [
                 self.buffer]
                result.append(self.decomp.decompress(self.chunkingZipFile.fp.read(self.length - self.readBytes)))
                result.append(self.decomp.decompress('Z'))
                result.append(self.decomp.flush())
                self.buffer = ''
                self.finished = 1
                result = ('').join(result)
                self.returnedBytes += len(result)
                return result
            else:
                while len(self.buffer) < n:
                    data = self.chunkingZipFile.fp.read(min(n, 1024, self.length - self.readBytes))
                    self.readBytes += len(data)
                    if not data:
                        result = self.buffer + self.decomp.decompress('Z') + self.decomp.flush()
                        self.finished = 1
                        self.buffer = ''
                        self.returnedBytes += len(result)
                        return result
                    self.buffer += self.decomp.decompress(data)

                result = self.buffer[:n]
                self.buffer = self.buffer[n:]
                self.returnedBytes += len(result)
                return result

            return


DIR_BIT = 16

def countZipFileChunks(filename, chunksize):
    totalchunks = 0
    zf = ChunkingZipFile(filename)
    for info in zf.infolist():
        totalchunks += countFileChunks(info, chunksize)

    return totalchunks


def countFileChunks(zipinfo, chunksize):
    count, extra = divmod(zipinfo.file_size, chunksize)
    if extra > 0:
        count += 1
    return count or 1


def unzipIterChunky(filename, directory='.', overwrite=0, chunksize=4096):
    czf = ChunkingZipFile(filename, 'r')
    if not os.path.exists(directory):
        os.makedirs(directory)
    remaining = countZipFileChunks(filename, chunksize)
    names = czf.namelist()
    infos = czf.infolist()
    for entry, info in zip(names, infos):
        isdir = info.external_attr & DIR_BIT
        f = os.path.join(directory, entry)
        if isdir:
            if not os.path.exists(f):
                os.makedirs(f)
            remaining -= 1
            yield remaining
        else:
            fdir = os.path.split(f)[0]
            if not os.path.exists(fdir):
                os.makedirs(fdir)
            if overwrite or not os.path.exists(f):
                outfile = file(f, 'wb')
                fp = czf.readfile(entry)
                if info.file_size == 0:
                    remaining -= 1
                    yield remaining
                while fp.tell() < info.file_size:
                    hunk = fp.read(chunksize)
                    outfile.write(hunk)
                    remaining -= 1
                    yield remaining

                outfile.close()
            else:
                remaining -= countFileChunks(info, chunksize)
                yield remaining
# okay decompiling out\twisted.python.zipstream.pyc
