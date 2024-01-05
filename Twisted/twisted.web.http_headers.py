# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.http_headers
from __future__ import division, absolute_import
from collections import MutableMapping
from twisted.python.compat import comparable, cmp

def _dashCapitalize(name):
    return ('-').join([ word.capitalize() for word in name.split('-') ])


class _DictHeaders(MutableMapping):

    def __init__(self, headers):
        self._headers = headers

    def __getitem__(self, key):
        if self._headers.hasHeader(key):
            return self._headers.getRawHeaders(key)[-1]
        raise KeyError(key)

    def __setitem__(self, key, value):
        self._headers.setRawHeaders(key, [value])

    def __delitem__(self, key):
        if self._headers.hasHeader(key):
            self._headers.removeHeader(key)
        else:
            raise KeyError(key)

    def __iter__(self):
        for k, v in self._headers.getAllRawHeaders():
            yield k.lower()

    def __len__(self):
        return len(self._headers._rawHeaders)

    def copy(self):
        return dict(self.items())

    def has_key(self, key):
        return key in self


@comparable
class Headers(object):
    _caseMappings = {'content-md5': 'Content-MD5', 
       'dnt': 'DNT', 
       'etag': 'ETag', 
       'p3p': 'P3P', 
       'te': 'TE', 
       'www-authenticate': 'WWW-Authenticate', 
       'x-xss-protection': 'X-XSS-Protection'}

    def __init__(self, rawHeaders=None):
        self._rawHeaders = {}
        if rawHeaders is not None:
            for name, values in rawHeaders.items():
                self.setRawHeaders(name, values[:])

        return

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._rawHeaders)

    def __cmp__(self, other):
        if isinstance(other, Headers):
            return cmp(sorted(self._rawHeaders.items()), sorted(other._rawHeaders.items()))
        return NotImplemented

    def copy(self):
        return self.__class__(self._rawHeaders)

    def hasHeader(self, name):
        return name.lower() in self._rawHeaders

    def removeHeader(self, name):
        self._rawHeaders.pop(name.lower(), None)
        return

    def setRawHeaders(self, name, values):
        if not isinstance(values, list):
            raise TypeError('Header entry %r should be list but found instance of %r instead' % (
             name, type(values)))
        self._rawHeaders[name.lower()] = values

    def addRawHeader(self, name, value):
        values = self.getRawHeaders(name)
        if values is None:
            self.setRawHeaders(name, [value])
        else:
            values.append(value)
        return

    def getRawHeaders(self, name, default=None):
        return self._rawHeaders.get(name.lower(), default)

    def getAllRawHeaders(self):
        for k, v in self._rawHeaders.items():
            yield (
             self._canonicalNameCaps(k), v)

    def _canonicalNameCaps(self, name):
        return self._caseMappings.get(name, _dashCapitalize(name))


__all__ = [
 'Headers']
# okay decompiling out\twisted.web.http_headers.pyc
