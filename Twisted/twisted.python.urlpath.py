# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.urlpath
from __future__ import division, absolute_import
from twisted.python.compat import urllib_parse as urlparse
from twisted.python.compat import _PY3
if not _PY3:
    from urllib import unquote as unquoteFunc
else:
    from urllib.parse import unquote as unquoteFunc

class URLPath(object):

    def __init__(self, scheme='', netloc='localhost', path='', query='', fragment=''):
        self.scheme = scheme or 'http'
        self.netloc = netloc
        self.path = path or '/'
        self.query = query
        self.fragment = fragment

    _qpathlist = None
    _uqpathlist = None

    def pathList(self, unquote=0, copy=1):
        if self._qpathlist is None:
            self._qpathlist = self.path.split('/')
            self._uqpathlist = map(unquoteFunc, self._qpathlist)
        if unquote:
            result = self._uqpathlist
        else:
            result = self._qpathlist
        if copy:
            return result[:]
        else:
            return result
            return

    def fromString(klass, st):
        t = urlparse.urlsplit(st)
        u = klass(*t)
        return u

    fromString = classmethod(fromString)

    def fromRequest(klass, request):
        return klass.fromString(request.prePathURL())

    fromRequest = classmethod(fromRequest)

    def _pathMod(self, newpathsegs, keepQuery):
        if keepQuery:
            query = self.query
        else:
            query = ''
        return URLPath(self.scheme, self.netloc, ('/').join(newpathsegs), query)

    def sibling(self, path, keepQuery=0):
        l = self.pathList()
        l[-1] = path
        return self._pathMod(l, keepQuery)

    def child(self, path, keepQuery=0):
        l = self.pathList()
        if l[-1] == '':
            l[-1] = path
        else:
            l.append(path)
        return self._pathMod(l, keepQuery)

    def parent(self, keepQuery=0):
        l = self.pathList()
        if l[-1] == '':
            del l[-2]
        else:
            l.pop()
            l[-1] = ''
        return self._pathMod(l, keepQuery)

    def here(self, keepQuery=0):
        l = self.pathList()
        if l[-1] != '':
            l[-1] = ''
        return self._pathMod(l, keepQuery)

    def click(self, st):
        scheme, netloc, path, query, fragment = urlparse.urlsplit(st)
        if not scheme:
            scheme = self.scheme
        if not netloc:
            netloc = self.netloc
            if not path:
                path = self.path
                if not query:
                    query = self.query
            elif path[0] != '/':
                l = self.pathList()
                l[-1] = path
                path = ('/').join(l)
        return URLPath(scheme, netloc, path, query, fragment)

    def __str__(self):
        x = urlparse.urlunsplit((
         self.scheme, self.netloc, self.path,
         self.query, self.fragment))
        return x

    def __repr__(self):
        return 'URLPath(scheme=%r, netloc=%r, path=%r, query=%r, fragment=%r)' % (
         self.scheme, self.netloc, self.path, self.query, self.fragment)
# okay decompiling out\twisted.python.urlpath.pyc
