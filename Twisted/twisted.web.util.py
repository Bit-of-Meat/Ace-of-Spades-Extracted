# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.util
from __future__ import division, absolute_import
import linecache
from twisted.python import urlpath
from twisted.python.compat import _PY3, unicode, nativeString, escape
from twisted.python.reflect import fullyQualifiedName
from twisted.python.modules import getModule
from twisted.web import resource
from twisted.web.template import TagLoader, XMLFile, Element, renderer
from twisted.web.template import flattenString

def _PRE(text):
    return '<pre>%s</pre>' % (escape(text),)


def redirectTo(URL, request):
    if isinstance(URL, unicode):
        raise TypeError('Unicode object not allowed as URL')
    request.setHeader('Content-Type', 'text/html; charset=utf-8')
    request.redirect(URL)
    content = '\n<html>\n    <head>\n        <meta http-equiv="refresh" content="0;URL=%(url)s">\n    </head>\n    <body bgcolor="#FFFFFF" text="#000000">\n    <a href="%(url)s">click here</a>\n    </body>\n</html>\n' % {'url': nativeString(URL)}
    if _PY3:
        content = content.encode('utf8')
    return content


class Redirect(resource.Resource):
    isLeaf = True

    def __init__(self, url):
        resource.Resource.__init__(self)
        self.url = url

    def render(self, request):
        return redirectTo(self.url, request)

    def getChild(self, name, request):
        return self


class ChildRedirector(Redirect):
    isLeaf = 0

    def __init__(self, url):
        if url.find('://') == -1 and not url.startswith('..') and not url.startswith('/'):
            raise ValueError("It seems you've given me a redirect (%s) that is a child of myself! That's not good, it'll cause an infinite redirect." % url)
        Redirect.__init__(self, url)

    def getChild(self, name, request):
        newUrl = self.url
        if not newUrl.endswith('/'):
            newUrl += '/'
        newUrl += name
        return ChildRedirector(newUrl)


class ParentRedirect(resource.Resource):
    isLeaf = 1

    def render(self, request):
        return redirectTo(urlpath.URLPath.fromRequest(request).here(), request)

    def getChild(self, request):
        return self


class DeferredResource(resource.Resource):
    isLeaf = 1

    def __init__(self, d):
        resource.Resource.__init__(self)
        self.d = d

    def getChild(self, name, request):
        return self

    def render(self, request):
        self.d.addCallback(self._cbChild, request).addErrback(self._ebChild, request)
        from twisted.web.server import NOT_DONE_YET
        return NOT_DONE_YET

    def _cbChild(self, child, request):
        request.render(resource.getChildForRequest(child, request))

    def _ebChild(self, reason, request):
        request.processingFailed(reason)
        return reason


class _SourceLineElement(Element):

    def __init__(self, loader, number, source):
        Element.__init__(self, loader)
        self.number = number
        self.source = source

    @renderer
    def sourceLine(self, request, tag):
        return tag(self.source.replace('  ', ' \xa0'))

    @renderer
    def lineNumber(self, request, tag):
        return tag(str(self.number))


class _SourceFragmentElement(Element):

    def __init__(self, loader, frame):
        Element.__init__(self, loader)
        self.frame = frame

    def _getSourceLines(self):
        filename = self.frame[1]
        lineNumber = self.frame[2]
        for snipLineNumber in range(lineNumber - 1, lineNumber + 2):
            yield (
             snipLineNumber,
             linecache.getline(filename, snipLineNumber).rstrip())

    @renderer
    def sourceLines(self, request, tag):
        for lineNumber, sourceLine in self._getSourceLines():
            newTag = tag.clone()
            if lineNumber == self.frame[2]:
                cssClass = 'snippetHighlightLine'
            else:
                cssClass = 'snippetLine'
            loader = TagLoader(newTag(**{'class': cssClass}))
            yield _SourceLineElement(loader, lineNumber, sourceLine)


class _FrameElement(Element):

    def __init__(self, loader, frame):
        Element.__init__(self, loader)
        self.frame = frame

    @renderer
    def filename(self, request, tag):
        return tag(self.frame[1])

    @renderer
    def lineNumber(self, request, tag):
        return tag(str(self.frame[2]))

    @renderer
    def function(self, request, tag):
        return tag(self.frame[0])

    @renderer
    def source(self, request, tag):
        return _SourceFragmentElement(TagLoader(tag), self.frame)


class _StackElement(Element):

    def __init__(self, loader, stackFrames):
        Element.__init__(self, loader)
        self.stackFrames = stackFrames

    @renderer
    def frames(self, request, tag):
        return [ _FrameElement(TagLoader(tag.clone()), frame) for frame in self.stackFrames
               ]


class FailureElement(Element):
    loader = XMLFile(getModule(__name__).filePath.sibling('failure.xhtml'))

    def __init__(self, failure, loader=None):
        Element.__init__(self, loader)
        self.failure = failure

    @renderer
    def type(self, request, tag):
        return tag(fullyQualifiedName(self.failure.type))

    @renderer
    def value(self, request, tag):
        return tag(unicode(self.failure.value).encode('utf8'))

    @renderer
    def traceback(self, request, tag):
        return _StackElement(TagLoader(tag), self.failure.frames)


def formatFailure(myFailure):
    result = []
    flattenString(None, FailureElement(myFailure)).addBoth(result.append)
    if isinstance(result[0], bytes):
        return result[0].decode('utf-8').encode('ascii', 'xmlcharrefreplace')
    else:
        result[0].raiseException()
        return


__all__ = [
 'redirectTo', 'Redirect', 'ChildRedirector', 'ParentRedirect', 
 'DeferredResource', 
 'FailureElement', 'formatFailure']
# okay decompiling out\twisted.web.util.pyc
