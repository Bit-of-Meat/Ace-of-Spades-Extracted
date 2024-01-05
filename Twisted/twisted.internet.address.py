# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.address
from __future__ import division, absolute_import
import warnings, os
from zope.interface import implementer
from twisted.internet.interfaces import IAddress
from twisted.python.filepath import _asFilesystemBytes
from twisted.python.filepath import _coerceToFilesystemEncoding
from twisted.python.util import FancyEqMixin
from twisted.python.runtime import platform
from twisted.python.compat import _PY3

@implementer(IAddress)
class _IPAddress(FancyEqMixin, object):
    compareAttributes = ('type', 'host', 'port')

    def __init__(self, type, host, port):
        self.type = type
        self.host = host
        self.port = port

    def __repr__(self):
        return '%s(%s, %r, %d)' % (
         self.__class__.__name__, self.type, self.host, self.port)

    def __hash__(self):
        return hash((self.type, self.host, self.port))


class IPv4Address(_IPAddress):

    def __init__(self, type, host, port, _bwHack=None):
        _IPAddress.__init__(self, type, host, port)
        if _bwHack is not None:
            warnings.warn('twisted.internet.address.IPv4Address._bwHack is deprecated since Twisted 11.0', DeprecationWarning, stacklevel=2)
        return


class IPv6Address(_IPAddress):
    pass


@implementer(IAddress)
class _ProcessAddress(object):
    pass


@implementer(IAddress)
class HostnameAddress(FancyEqMixin, object):
    compareAttributes = ('hostname', 'port')

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def __repr__(self):
        return '%s(%s, %d)' % (
         self.__class__.__name__, self.hostname, self.port)

    def __hash__(self):
        return hash((self.hostname, self.port))


@implementer(IAddress)
class UNIXAddress(FancyEqMixin, object):
    compareAttributes = ('name', )

    def __init__(self, name, _bwHack=None):
        self.name = name
        if _bwHack is not None:
            warnings.warn('twisted.internet.address.UNIXAddress._bwHack is deprecated since Twisted 11.0', DeprecationWarning, stacklevel=2)
        return

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None:
            self._name = _asFilesystemBytes(name)
        else:
            self._name = None
        return

    if getattr(os.path, 'samefile', None) is not None:

        def __eq__(self, other):
            res = super(UNIXAddress, self).__eq__(other)
            if not res and self.name and other.name:
                try:
                    return os.path.samefile(self.name, other.name)
                except OSError:
                    pass
                except (TypeError, ValueError) as e:
                    if not _PY3 and not platform.isLinux():
                        raise e

            return res

    def __repr__(self):
        name = self.name
        if name:
            name = _coerceToFilesystemEncoding('', self.name)
        return 'UNIXAddress(%r)' % (name,)

    def __hash__(self):
        if self.name is None:
            return hash((self.__class__, None))
        else:
            try:
                s1 = os.stat(self.name)
                return hash((s1.st_ino, s1.st_dev))
            except OSError:
                return hash(self.name)

            return


class _ServerFactoryIPv4Address(IPv4Address):

    def __eq__(self, other):
        if isinstance(other, tuple):
            warnings.warn('IPv4Address.__getitem__ is deprecated.  Use attributes instead.', category=DeprecationWarning, stacklevel=2)
            return (
             self.host, self.port) == other
        if isinstance(other, IPv4Address):
            a = (
             self.type, self.host, self.port)
            b = (other.type, other.host, other.port)
            return a == b
        return False
# okay decompiling out\twisted.internet.address.pyc
