# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.filepath
from __future__ import division, absolute_import
import os, sys, errno, base64
from hashlib import sha1
from warnings import warn
from os.path import isabs, exists, normpath, abspath, splitext
from os.path import basename, dirname, join as joinpath
from os import listdir, utime, stat
from stat import S_ISREG, S_ISDIR, S_IMODE, S_ISBLK, S_ISSOCK
from stat import S_IRUSR, S_IWUSR, S_IXUSR
from stat import S_IRGRP, S_IWGRP, S_IXGRP
from stat import S_IROTH, S_IWOTH, S_IXOTH
from zope.interface import Interface, Attribute, implementer
from twisted.python.compat import comparable, cmp, unicode
from twisted.python.deprecate import deprecated
from twisted.python.runtime import platform
from twisted.python.versions import Version
from twisted.python.win32 import ERROR_FILE_NOT_FOUND, ERROR_PATH_NOT_FOUND
from twisted.python.win32 import ERROR_INVALID_NAME, ERROR_DIRECTORY, O_BINARY
from twisted.python.win32 import WindowsError
from twisted.python.util import FancyEqMixin
_CREATE_FLAGS = os.O_EXCL | os.O_CREAT | os.O_RDWR | O_BINARY

def _stub_islink(path):
    return False


islink = getattr(os.path, 'islink', _stub_islink)
randomBytes = os.urandom
armor = base64.urlsafe_b64encode

class IFilePath(Interface):
    sep = Attribute('The path separator to use in string representations')

    def child(name):
        pass

    def open(mode='r'):
        pass

    def changed():
        pass

    def getsize():
        pass

    def getModificationTime():
        pass

    def getStatusChangeTime():
        pass

    def getAccessTime():
        pass

    def exists():
        pass

    def isdir():
        pass

    def isfile():
        pass

    def children():
        pass

    def basename():
        pass

    def parent():
        pass

    def sibling(name):
        pass


class InsecurePath(Exception):
    pass


class LinkError(Exception):
    pass


class UnlistableError(OSError):

    def __init__(self, originalException):
        self.__dict__.update(originalException.__dict__)
        self.originalException = originalException


class _WindowsUnlistableError(UnlistableError, WindowsError):
    pass


def _secureEnoughString(path):
    secureishString = armor(sha1(randomBytes(64)).digest())[:16]
    return _coerceToFilesystemEncoding(path, secureishString)


class AbstractFilePath(object):

    def getContent(self):
        fp = self.open()
        try:
            return fp.read()
        finally:
            fp.close()

    def parents(self):
        path = self
        parent = path.parent()
        while path != parent:
            yield parent
            path = parent
            parent = parent.parent()

    def children(self):
        try:
            subnames = self.listdir()
        except WindowsError as winErrObj:
            winerror = getattr(winErrObj, 'winerror', winErrObj.errno)
            if winerror not in (ERROR_PATH_NOT_FOUND,
             ERROR_FILE_NOT_FOUND,
             ERROR_INVALID_NAME,
             ERROR_DIRECTORY):
                raise
            raise _WindowsUnlistableError(winErrObj)
        except OSError as ose:
            if ose.errno not in (errno.ENOENT, errno.ENOTDIR):
                raise
            raise UnlistableError(ose)

        return map(self.child, subnames)

    def walk(self, descend=None):
        yield self
        if self.isdir():
            for c in self.children():
                if descend is None or descend(c):
                    for subc in c.walk(descend):
                        if os.path.realpath(self.path).startswith(os.path.realpath(subc.path)):
                            raise LinkError('Cycle in file graph.')
                        yield subc

                else:
                    yield c

        return

    def sibling(self, path):
        return self.parent().child(path)

    def descendant(self, segments):
        path = self
        for name in segments:
            path = path.child(name)

        return path

    def segmentsFrom(self, ancestor):
        f = self
        p = f.parent()
        segments = []
        while f != ancestor and p != f:
            segments[0:0] = [
             f.basename()]
            f = p
            p = p.parent()

        if f == ancestor and segments:
            return segments
        raise ValueError('%r not parent of %r' % (ancestor, self))

    def __hash__(self):
        return hash((self.__class__, self.path))

    def getmtime(self):
        return int(self.getModificationTime())

    def getatime(self):
        return int(self.getAccessTime())

    def getctime(self):
        return int(self.getStatusChangeTime())


class RWX(FancyEqMixin, object):
    compareAttributes = ('read', 'write', 'execute')

    def __init__(self, readable, writable, executable):
        self.read = readable
        self.write = writable
        self.execute = executable

    def __repr__(self):
        return 'RWX(read=%s, write=%s, execute=%s)' % (
         self.read, self.write, self.execute)

    def shorthand(self):
        returnval = [
         'r', 'w', 'x']
        i = 0
        for val in (self.read, self.write, self.execute):
            if not val:
                returnval[i] = '-'
            i += 1

        return ('').join(returnval)


class Permissions(FancyEqMixin, object):
    compareAttributes = ('user', 'group', 'other')

    def __init__(self, statModeInt):
        self.user, self.group, self.other = [ RWX(*[ statModeInt & bit > 0 for bit in bitGroup ]) for bitGroup in [
         [
          S_IRUSR, S_IWUSR, S_IXUSR],
         [
          S_IRGRP, S_IWGRP, S_IXGRP],
         [
          S_IROTH, S_IWOTH, S_IXOTH]]
                                            ]

    def __repr__(self):
        return '[%s | %s | %s]' % (
         str(self.user), str(self.group), str(self.other))

    def shorthand(self):
        return ('').join([ x.shorthand() for x in (self.user, self.group, self.other) ])


class _SpecialNoValue(object):
    pass


def _asFilesystemBytes(path, encoding=None):
    if type(path) == bytes:
        return path
    else:
        if encoding is None:
            encoding = sys.getfilesystemencoding()
        return path.encode(encoding)
        return


def _asFilesystemText(path, encoding=None):
    if type(path) == unicode:
        return path
    else:
        if encoding is None:
            encoding = sys.getfilesystemencoding()
        return path.decode(encoding)
        return


def _coerceToFilesystemEncoding(path, newpath, encoding=None):
    if type(path) == bytes:
        return _asFilesystemBytes(newpath, encoding=encoding)
    else:
        return _asFilesystemText(newpath, encoding=encoding)


@comparable
@implementer(IFilePath)
class FilePath(AbstractFilePath):
    _statinfo = None
    path = None

    def __init__(self, path, alwaysCreate=False):
        self.path = abspath(path)
        self.alwaysCreate = alwaysCreate
        if type(self.path) != type(path):
            warn('os.path.abspath is broken on Python versions below 2.6.5 and coerces Unicode paths to bytes. Please update your Python.', DeprecationWarning)
            self.path = self._getPathAsSameTypeAs(path)

    def __getstate__(self):
        d = self.__dict__.copy()
        if '_statinfo' in d:
            del d['_statinfo']
        return d

    @property
    def sep(self):
        return _coerceToFilesystemEncoding(self.path, os.sep)

    def _asBytesPath(self, encoding=None):
        return _asFilesystemBytes(self.path, encoding=encoding)

    def _asTextPath(self, encoding=None):
        return _asFilesystemText(self.path, encoding=encoding)

    def asBytesMode(self, encoding=None):
        if type(self.path) == unicode:
            return self.clonePath(self._asBytesPath(encoding=encoding))
        return self

    def asTextMode(self, encoding=None):
        if type(self.path) == bytes:
            return self.clonePath(self._asTextPath(encoding=encoding))
        return self

    def _getPathAsSameTypeAs(self, pattern):
        if type(pattern) == bytes:
            return self._asBytesPath()
        else:
            return self._asTextPath()

    def child(self, path):
        colon = _coerceToFilesystemEncoding(path, ':')
        sep = _coerceToFilesystemEncoding(path, os.sep)
        ourPath = self._getPathAsSameTypeAs(path)
        if platform.isWindows() and path.count(colon):
            raise InsecurePath('%r contains a colon.' % (path,))
        norm = normpath(path)
        if sep in norm:
            raise InsecurePath('%r contains one or more directory separators' % (
             path,))
        newpath = abspath(joinpath(ourPath, norm))
        if not newpath.startswith(ourPath):
            raise InsecurePath('%r is not a child of %s' % (
             newpath, ourPath))
        return self.clonePath(newpath)

    def preauthChild(self, path):
        ourPath = self._getPathAsSameTypeAs(path)
        newpath = abspath(joinpath(ourPath, normpath(path)))
        if not newpath.startswith(ourPath):
            raise InsecurePath('%s is not a child of %s' % (
             newpath, ourPath))
        return self.clonePath(newpath)

    def childSearchPreauth(self, *paths):
        for child in paths:
            p = self._getPathAsSameTypeAs(child)
            jp = joinpath(p, child)
            if exists(jp):
                return self.clonePath(jp)

    def siblingExtensionSearch(self, *exts):
        for ext in exts:
            if not ext and self.exists():
                return self
            p = self._getPathAsSameTypeAs(ext)
            star = _coerceToFilesystemEncoding(ext, '*')
            dot = _coerceToFilesystemEncoding(ext, '.')
            if ext == star:
                basedot = basename(p) + dot
                for fn in listdir(dirname(p)):
                    if fn.startswith(basedot):
                        return self.clonePath(joinpath(dirname(p), fn))

            p2 = p + ext
            if exists(p2):
                return self.clonePath(p2)

    def realpath(self):
        if self.islink():
            result = os.path.realpath(self.path)
            if result == self.path:
                raise LinkError('Cyclical link - will loop forever')
            return self.clonePath(result)
        return self

    def siblingExtension(self, ext):
        ourPath = self._getPathAsSameTypeAs(ext)
        return self.clonePath(ourPath + ext)

    def linkTo(self, linkFilePath):
        os.symlink(self.path, linkFilePath.path)

    def open(self, mode='r'):
        if self.alwaysCreate:
            return self.create()
        mode = mode.replace('b', '')
        return open(self.path, mode + 'b')

    def restat(self, reraise=True):
        try:
            self._statinfo = stat(self.path)
        except OSError:
            self._statinfo = 0
            if reraise:
                raise

    def changed(self):
        self._statinfo = None
        return

    def chmod(self, mode):
        os.chmod(self.path, mode)

    def getsize(self):
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return st.st_size

    def getModificationTime(self):
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return float(st.st_mtime)

    def getStatusChangeTime(self):
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return float(st.st_ctime)

    def getAccessTime(self):
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return float(st.st_atime)

    def getInodeNumber(self):
        if platform.isWindows():
            raise NotImplementedError
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return st.st_ino

    def getDevice(self):
        if platform.isWindows():
            raise NotImplementedError
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return st.st_dev

    def getNumberOfHardLinks(self):
        if platform.isWindows():
            raise NotImplementedError
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return st.st_nlink

    def getUserID(self):
        if platform.isWindows():
            raise NotImplementedError
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return st.st_uid

    def getGroupID(self):
        if platform.isWindows():
            raise NotImplementedError
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return st.st_gid

    def getPermissions(self):
        st = self._statinfo
        if not st:
            self.restat()
            st = self._statinfo
        return Permissions(S_IMODE(st.st_mode))

    def exists(self):
        if self._statinfo:
            return True
        else:
            self.restat(False)
            if self._statinfo:
                return True
            return False

    def isdir(self):
        st = self._statinfo
        if not st:
            self.restat(False)
            st = self._statinfo
            if not st:
                return False
        return S_ISDIR(st.st_mode)

    def isfile(self):
        st = self._statinfo
        if not st:
            self.restat(False)
            st = self._statinfo
            if not st:
                return False
        return S_ISREG(st.st_mode)

    def isBlockDevice(self):
        st = self._statinfo
        if not st:
            self.restat(False)
            st = self._statinfo
            if not st:
                return False
        return S_ISBLK(st.st_mode)

    def isSocket(self):
        st = self._statinfo
        if not st:
            self.restat(False)
            st = self._statinfo
            if not st:
                return False
        return S_ISSOCK(st.st_mode)

    def islink(self):
        return islink(self.path)

    def isabs(self):
        return isabs(self.path)

    def listdir(self):
        return listdir(self.path)

    def splitext(self):
        return splitext(self.path)

    def __repr__(self):
        return 'FilePath(%r)' % (self.path,)

    def touch(self):
        try:
            self.open('a').close()
        except IOError:
            pass

        utime(self.path, None)
        return

    def remove(self):
        if self.isdir() and not self.islink():
            for child in self.children():
                child.remove()

            os.rmdir(self.path)
        else:
            os.remove(self.path)
        self.changed()

    def makedirs(self):
        return os.makedirs(self.path)

    def globChildren(self, pattern):
        sep = _coerceToFilesystemEncoding(pattern, os.sep)
        ourPath = self._getPathAsSameTypeAs(pattern)
        import glob
        path = ourPath[-1] == sep and ourPath + pattern or sep.join([ourPath, pattern])
        return list(map(self.clonePath, glob.glob(path)))

    def basename(self):
        return basename(self.path)

    def dirname(self):
        return dirname(self.path)

    def parent(self):
        return self.clonePath(self.dirname())

    def setContent(self, content, ext='.new'):
        sib = self.temporarySibling(ext)
        f = sib.open('w')
        try:
            f.write(content)
        finally:
            f.close()

        if platform.isWindows() and exists(self.path):
            os.unlink(self.path)
        os.rename(sib.path, self.path)

    def __cmp__(self, other):
        if not isinstance(other, FilePath):
            return NotImplemented
        return cmp(self.path, other.path)

    def createDirectory(self):
        os.mkdir(self.path)

    def requireCreate(self, val=1):
        self.alwaysCreate = val

    def create(self):
        fdint = os.open(self.path, _CREATE_FLAGS)
        return os.fdopen(fdint, 'w+b')

    def temporarySibling(self, extension=''):
        ourPath = self._getPathAsSameTypeAs(extension)
        sib = self.sibling(_secureEnoughString(ourPath) + self.clonePath(ourPath).basename() + extension)
        sib.requireCreate()
        return sib

    _chunkSize = 2 ** (2 ** 4)

    def copyTo(self, destination, followLinks=True):
        if self.islink() and not followLinks:
            os.symlink(os.readlink(self.path), destination.path)
            return
        if self.isdir():
            if not destination.exists():
                destination.createDirectory()
            for child in self.children():
                destChild = destination.child(child.basename())
                child.copyTo(destChild, followLinks)

        elif self.isfile():
            writefile = destination.open('w')
            try:
                readfile = self.open()
                try:
                    while 1:
                        chunk = readfile.read(self._chunkSize)
                        writefile.write(chunk)
                        if len(chunk) < self._chunkSize:
                            break

                finally:
                    readfile.close()

            finally:
                writefile.close()

        elif not self.exists():
            raise OSError(errno.ENOENT, 'No such file or directory')
        else:
            raise NotImplementedError('Only copying of files and directories supported')

    def moveTo(self, destination, followLinks=True):
        try:
            os.rename(self.path, destination.path)
        except OSError as ose:
            if ose.errno == errno.EXDEV:
                secsib = destination.temporarySibling()
                self.copyTo(secsib, followLinks)
                secsib.moveTo(destination, followLinks)
                mysecsib = self.temporarySibling()
                self.moveTo(mysecsib, followLinks)
                mysecsib.remove()
            else:
                raise
        else:
            self.changed()
            destination.changed()

    def statinfo(self, value=_SpecialNoValue):
        if value is _SpecialNoValue:
            return self._statinfo
        self._statinfo = value


_tmp = deprecated(Version('Twisted', 15, 0, 0), 'other FilePath methods such as getsize(), isdir(), getModificationTime(), etc.')(FilePath.statinfo)
FilePath.statinfo = property(_tmp, _tmp)
FilePath.clonePath = FilePath
# okay decompiling out\twisted.python.filepath.pyc
