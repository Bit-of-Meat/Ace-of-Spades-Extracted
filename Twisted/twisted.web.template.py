# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.template
from __future__ import division, absolute_import
__all__ = [
 'TEMPLATE_NAMESPACE', 'VALID_HTML_TAG_NAMES', 'Element', 'TagLoader', 
 'XMLString', 
 'XMLFile', 'renderer', 'flatten', 'flattenString', 'tags', 
 'Comment', 
 'CDATA', 'Tag', 'slot', 'CharRef', 'renderElement']
import warnings
from zope.interface import implementer
from xml.sax import make_parser, handler
from twisted.python import log
from twisted.python.compat import NativeStringIO, items, OrderedDict
from twisted.python.filepath import FilePath
from twisted.web._stan import Tag, slot, Comment, CDATA, CharRef
from twisted.web.iweb import ITemplateLoader
TEMPLATE_NAMESPACE = 'http://twistedmatrix.com/ns/twisted.web.template/0.1'
NOT_DONE_YET = 1

class _NSContext(object):

    def __init__(self, parent=None):
        self.parent = parent
        if parent is not None:
            self.nss = OrderedDict(parent.nss)
        else:
            self.nss = {'http://www.w3.org/XML/1998/namespace': 'xml'}
        return

    def get(self, k, d=None):
        return self.nss.get(k, d)

    def __setitem__(self, k, v):
        self.nss.__setitem__(k, v)

    def __getitem__(self, k):
        return self.nss.__getitem__(k)


class _ToStan(handler.ContentHandler, handler.EntityResolver):

    def __init__(self, sourceFilename):
        self.sourceFilename = sourceFilename
        self.prefixMap = _NSContext()
        self.inCDATA = False

    def setDocumentLocator(self, locator):
        self.locator = locator

    def startDocument(self):
        self.document = []
        self.current = self.document
        self.stack = []
        self.xmlnsAttrs = []

    def endDocument(self):
        pass

    def processingInstruction(self, target, data):
        pass

    def startPrefixMapping(self, prefix, uri):
        self.prefixMap = _NSContext(self.prefixMap)
        self.prefixMap[uri] = prefix
        if uri == TEMPLATE_NAMESPACE:
            return
        else:
            if prefix is None:
                self.xmlnsAttrs.append(('xmlns', uri))
            else:
                self.xmlnsAttrs.append(('xmlns:%s' % prefix, uri))
            return

    def endPrefixMapping(self, prefix):
        self.prefixMap = self.prefixMap.parent

    def startElementNS(self, namespaceAndName, qname, attrs):
        filename = self.sourceFilename
        lineNumber = self.locator.getLineNumber()
        columnNumber = self.locator.getColumnNumber()
        ns, name = namespaceAndName
        if ns == TEMPLATE_NAMESPACE:
            if name == 'transparent':
                name = ''
            elif name == 'slot':
                try:
                    default = attrs[(None, 'default')]
                except KeyError:
                    default = None

                el = slot(attrs[(None, 'name')], default=default, filename=filename, lineNumber=lineNumber, columnNumber=columnNumber)
                self.stack.append(el)
                self.current.append(el)
                self.current = el.children
                return
        render = None
        attrs = OrderedDict(attrs)
        for k, v in items(attrs):
            attrNS, justTheName = k
            if attrNS != TEMPLATE_NAMESPACE:
                continue
            if justTheName == 'render':
                render = v
                del attrs[k]

        nonTemplateAttrs = OrderedDict()
        for (attrNs, attrName), v in items(attrs):
            nsPrefix = self.prefixMap.get(attrNs)
            if nsPrefix is None:
                attrKey = attrName
            else:
                attrKey = '%s:%s' % (nsPrefix, attrName)
            nonTemplateAttrs[attrKey] = v

        if ns == TEMPLATE_NAMESPACE and name == 'attr':
            assert self.stack, '<{%s}attr> as top-level element' % (TEMPLATE_NAMESPACE,)
            if 'name' not in nonTemplateAttrs:
                raise AssertionError('<{%s}attr> requires a name attribute' % (TEMPLATE_NAMESPACE,))
            el = Tag('', render=render, filename=filename, lineNumber=lineNumber, columnNumber=columnNumber)
            self.stack[-1].attributes[nonTemplateAttrs['name']] = el
            self.stack.append(el)
            self.current = el.children
            return
        else:
            if self.xmlnsAttrs:
                nonTemplateAttrs.update(OrderedDict(self.xmlnsAttrs))
                self.xmlnsAttrs = []
            if ns != TEMPLATE_NAMESPACE and ns is not None:
                prefix = self.prefixMap[ns]
                if prefix is not None:
                    name = '%s:%s' % (self.prefixMap[ns], name)
            el = Tag(name, attributes=OrderedDict(nonTemplateAttrs), render=render, filename=filename, lineNumber=lineNumber, columnNumber=columnNumber)
            self.stack.append(el)
            self.current.append(el)
            self.current = el.children
            return

    def characters(self, ch):
        if self.inCDATA:
            self.stack[-1].append(ch)
            return
        self.current.append(ch)

    def endElementNS(self, name, qname):
        self.stack.pop()
        if self.stack:
            self.current = self.stack[-1].children
        else:
            self.current = self.document

    def startDTD(self, name, publicId, systemId):
        pass

    def endDTD(self, *args):
        pass

    def startCDATA(self):
        self.inCDATA = True
        self.stack.append([])

    def endCDATA(self):
        self.inCDATA = False
        comment = ('').join(self.stack.pop())
        self.current.append(CDATA(comment))

    def comment(self, content):
        self.current.append(Comment(content))


def _flatsaxParse(fl):
    parser = make_parser()
    parser.setFeature(handler.feature_validation, 0)
    parser.setFeature(handler.feature_namespaces, 1)
    parser.setFeature(handler.feature_external_ges, 0)
    parser.setFeature(handler.feature_external_pes, 0)
    s = _ToStan(getattr(fl, 'name', None))
    parser.setContentHandler(s)
    parser.setEntityResolver(s)
    parser.setProperty(handler.property_lexical_handler, s)
    parser.parse(fl)
    return s.document


@implementer(ITemplateLoader)
class TagLoader(object):

    def __init__(self, tag):
        self.tag = tag

    def load(self):
        return [
         self.tag]


@implementer(ITemplateLoader)
class XMLString(object):

    def __init__(self, s):
        if not isinstance(s, str):
            s = s.decode('utf8')
        self._loadedTemplate = _flatsaxParse(NativeStringIO(s))

    def load(self):
        return self._loadedTemplate


@implementer(ITemplateLoader)
class XMLFile(object):

    def __init__(self, path):
        if not isinstance(path, FilePath):
            warnings.warn('Passing filenames or file objects to XMLFile is deprecated since Twisted 12.1.  Pass a FilePath instead.', category=DeprecationWarning, stacklevel=2)
        self._loadedTemplate = None
        self._path = path
        return

    def _loadDoc(self):
        if not isinstance(self._path, FilePath):
            return _flatsaxParse(self._path)
        f = self._path.open('r')
        try:
            return _flatsaxParse(f)
        finally:
            f.close()

    def __repr__(self):
        return '<XMLFile of %r>' % (self._path,)

    def load(self):
        if self._loadedTemplate is None:
            self._loadedTemplate = self._loadDoc()
        return self._loadedTemplate


VALID_HTML_TAG_NAMES = set([
 'a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 
 'audio', 
 'b', 'base', 'basefont', 'bdi', 'bdo', 'big', 'blockquote', 
 'body', 
 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code', 
 'col', 
 'colgroup', 'command', 'datalist', 'dd', 'del', 'details', 'dfn', 
 'dir', 
 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 
 'figure', 
 'font', 'footer', 'form', 'frame', 'frameset', 'h1', 'h2', 'h3', 
 'h4', 
 'h5', 'h6', 'head', 'header', 'hgroup', 'hr', 'html', 'i', 'iframe', 
 'img', 
 'input', 'ins', 'isindex', 'keygen', 'kbd', 'label', 'legend', 
 'li', 
 'link', 'map', 'mark', 'menu', 'meta', 'meter', 'nav', 'noframes', 
 'noscript', 
 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 
 'pre', 
 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 
 'section', 
 'select', 'small', 'source', 'span', 'strike', 'strong', 
 'style', 'sub', 
 'summary', 'sup', 'table', 'tbody', 'td', 'textarea', 
 'tfoot', 'th', 
 'thead', 'time', 'title', 'tr', 'tt', 'u', 'ul', 'var', 
 'video', 'wbr'])

class _TagFactory(object):

    def __getattr__(self, tagName):
        if tagName == 'transparent':
            return Tag('')
        tagName = tagName.rstrip('_')
        if tagName not in VALID_HTML_TAG_NAMES:
            raise AttributeError('unknown tag %r' % (tagName,))
        return Tag(tagName)


tags = _TagFactory()

def renderElement(request, element, doctype='<!DOCTYPE html>', _failElement=None):
    if doctype is not None:
        request.write(doctype)
        request.write('\n')
    if _failElement is None:
        _failElement = twisted.web.util.FailureElement
    d = flatten(request, element, request.write)

    def eb(failure):
        log.err(failure, 'An error occurred while rendering the response.')
        if request.site.displayTracebacks:
            return flatten(request, _failElement(failure), request.write).encode('utf8')
        request.write('<div style="font-size:800%;background-color:#FFF;color:#F00">An error occurred while rendering the response.</div>')

    d.addErrback(eb)
    d.addBoth((lambda _: request.finish()))
    return NOT_DONE_YET


from twisted.web._element import Element, renderer
from twisted.web._flatten import flatten, flattenString
import twisted.web.util
# okay decompiling out\twisted.web.template.pyc
