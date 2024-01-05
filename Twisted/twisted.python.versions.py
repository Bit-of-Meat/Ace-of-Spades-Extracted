# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.versions
from __future__ import division, absolute_import
import sys, os
from twisted.python.compat import cmp, comparable, nativeString

@comparable
class _inf(object):

    def __cmp__(self, other):
        if other is _inf:
            return 0
        return 1


_inf = _inf()

class IncomparableVersions(TypeError):
    pass


@comparable
class Version(object):

    def __init__(self, package, major, minor, micro, prerelease=None):
        self.package = package
        self.major = major
        self.minor = minor
        self.micro = micro
        self.prerelease = prerelease

    def short(self):
        s = self.base()
        svnver = self._getSVNVersion()
        if svnver:
            s += '+r' + nativeString(svnver)
        return s

    def base(self):
        if self.prerelease is None:
            pre = ''
        else:
            pre = 'pre%s' % (self.prerelease,)
        return '%d.%d.%d%s' % (self.major,
         self.minor,
         self.micro,
         pre)

    def __repr__(self):
        svnver = self._formatSVNVersion()
        if svnver:
            svnver = '  #' + svnver
        if self.prerelease is None:
            prerelease = ''
        else:
            prerelease = ', prerelease=%r' % (self.prerelease,)
        return '%s(%r, %d, %d, %d%s)%s' % (
         self.__class__.__name__,
         self.package,
         self.major,
         self.minor,
         self.micro,
         prerelease,
         svnver)

    def __str__(self):
        return '[%s, version %s]' % (
         self.package,
         self.short())

    def __cmp__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            if self.package != other.package:
                raise IncomparableVersions('%r != %r' % (
                 self.package, other.package))
            if self.prerelease is None:
                prerelease = _inf
            else:
                prerelease = self.prerelease
            if other.prerelease is None:
                otherpre = _inf
            else:
                otherpre = other.prerelease
            x = cmp((self.major,
             self.minor,
             self.micro,
             prerelease), (
             other.major,
             other.minor,
             other.micro,
             otherpre))
            return x

    def _parseSVNEntries_4(self, entriesFile):
        from xml.dom.minidom import parse
        doc = parse(entriesFile).documentElement
        for node in doc.childNodes:
            if hasattr(node, 'getAttribute'):
                rev = node.getAttribute('revision')
                if rev is not None:
                    return rev.encode('ascii')

        return

    def _parseSVNEntries_8(self, entriesFile):
        entriesFile.readline()
        entriesFile.readline()
        entriesFile.readline()
        return entriesFile.readline().strip()

    _parseSVNEntries_9 = _parseSVNEntries_8
    _parseSVNEntriesTenPlus = _parseSVNEntries_8

    def _getSVNVersion(self):
        mod = sys.modules.get(self.package)
        if mod:
            svn = os.path.join(os.path.dirname(mod.__file__), '.svn')
            if not os.path.exists(svn):
                return
            formatFile = os.path.join(svn, 'format')
            if os.path.exists(formatFile):
                with open(formatFile, 'rb') as (fObj):
                    format = fObj.read().strip()
                parser = getattr(self, '_parseSVNEntries_' + format.decode('ascii'), None)
            else:
                parser = self._parseSVNEntriesTenPlus
            if parser is None:
                return 'Unknown'
            entriesFile = os.path.join(svn, 'entries')
            entries = open(entriesFile, 'rb')
            try:
                try:
                    return parser(entries)
                finally:
                    entries.close()

            except:
                return 'Unknown'

        return

    def _formatSVNVersion(self):
        ver = self._getSVNVersion()
        if ver is None:
            return ''
        else:
            return ' (SVN r%s)' % (ver,)


def getVersionString(version):
    result = '%s %s' % (version.package, version.short())
    return result
# okay decompiling out\twisted.python.versions.pyc
