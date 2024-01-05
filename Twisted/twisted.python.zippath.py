# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.zippath
__metaclass__ = type
import os, time, errno, sys
if sys.version_info[:2] >= (2, 6):
    _USE_ZIPFILE = True
    from zipfile import ZipFile
else:
    _USE_ZIPFILE = False
    from twisted.python.zipstream import ChunkingZipFile
from twisted.python.filepath import IFilePath, FilePath, AbstractFilePath
from zope.interface import implementer
ZIP_PATH_SEP = '/'

@implementer(IFilePath)
class ZipPath(AbstractFilePath):
    sep = ZIP_PATH_SEP

    def __init__(self, archive, pathInArchive):
        self.archive = archive
        self.pathInArchive = pathInArchive
        self.path = os.path.join(archive.zipfile.filename, *self.pathInArchive.split(ZIP_PATH_SEP))

    def __cmp__(self, other):
        if not isinstance(other, ZipPath):
            return NotImplemented
        return cmp((self.archive, self.pathInArchive), (
         other.archive, other.pathInArchive))

    def __repr__(self):
        parts = [
         os.path.abspath(self.archive.path)]
        parts.extend(self.pathInArchive.split(ZIP_PATH_SEP))
        path = os.sep.join(parts)
        return "ZipPath('%s')" % (path.encode('string-escape'),)

    def parent(self):
        splitup = self.pathInArchive.split(ZIP_PATH_SEP)
        if len(splitup) == 1:
            return self.archive
        return ZipPath(self.archive, ZIP_PATH_SEP.join(splitup[:-1]))

    def child(self, path):
        return ZipPath(self.archive, ZIP_PATH_SEP.join([self.pathInArchive, path]))

    def sibling(self, path):
        return self.parent().child(path)

    def exists(self):
        return self.isdir() or self.isfile()

    def isdir(self):
        return self.pathInArchive in self.archive.childmap

    def isfile(self):
        return self.pathInArchive in self.archive.zipfile.NameToInfo

    def islink(self):
        return False

    def listdir(self):
        if self.exists():
            if self.isdir():
                return self.archive.childmap[self.pathInArchive].keys()
            raise OSError(errno.ENOTDIR, 'Leaf zip entry listed')
        else:
            raise OSError(errno.ENOENT, 'Non-existent zip entry listed')

    def splitext(self):
        return os.path.splitext(self.path)

    def basename(self):
        return self.pathInArchive.split(ZIP_PATH_SEP)[-1]

    def dirname(self):
        return self.parent().path

    def open(self, mode='r'):
        if _USE_ZIPFILE:
            return self.archive.zipfile.open(self.pathInArchive, mode=mode)
        else:
            self.archive.zipfile.mode = mode
            return self.archive.zipfile.readfile(self.pathInArchive)

    def changed(self):
        pass

    def getsize(self):
        return self.archive.zipfile.NameToInfo[self.pathInArchive].file_size

    def getAccessTime(self):
        return self.archive.getAccessTime()

    def getModificationTime(self):
        return time.mktime(self.archive.zipfile.NameToInfo[self.pathInArchive].date_time + (0,
                                                                                            0,
                                                                                            0))

    def getStatusChangeTime(self):
        return self.getModificationTime()


class ZipArchive(ZipPath):
    archive = property((lambda self: self))

    def __init__(self, archivePathname):
        if _USE_ZIPFILE:
            self.zipfile = ZipFile(archivePathname)
        else:
            self.zipfile = ChunkingZipFile(archivePathname)
        self.path = archivePathname
        self.pathInArchive = ''
        self.childmap = {}
        for name in self.zipfile.namelist():
            name = name.split(ZIP_PATH_SEP)
            for x in range(len(name)):
                child = name[-x]
                parent = ZIP_PATH_SEP.join(name[:-x])
                if parent not in self.childmap:
                    self.childmap[parent] = {}
                self.childmap[parent][child] = 1

            parent = ''

    def child(self, path):
        return ZipPath(self, path)

    def exists(self):
        return FilePath(self.zipfile.filename).exists()

    def getAccessTime(self):
        return FilePath(self.zipfile.filename).getAccessTime()

    def getModificationTime(self):
        return FilePath(self.zipfile.filename).getModificationTime()

    def getStatusChangeTime(self):
        return FilePath(self.zipfile.filename).getStatusChangeTime()

    def __repr__(self):
        return 'ZipArchive(%r)' % (os.path.abspath(self.path),)


__all__ = [
 'ZipArchive', 'ZipPath']
# okay decompiling out\twisted.python.zippath.pyc
