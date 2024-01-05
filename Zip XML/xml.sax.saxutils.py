# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\xml.sax.saxutils
import os, urlparse, urllib, types, io, sys, handler, xmlreader
try:
    _StringTypes = [
     types.StringType, types.UnicodeType]
except AttributeError:
    _StringTypes = [
     types.StringType]

def __dict_replace(s, d):
    for key, value in d.items():
        s = s.replace(key, value)

    return s


def escape(data, entities={}):
    data = data.replace('&', '&amp;')
    data = data.replace('>', '&gt;')
    data = data.replace('<', '&lt;')
    if entities:
        data = __dict_replace(data, entities)
    return data


def unescape(data, entities={}):
    data = data.replace('&lt;', '<')
    data = data.replace('&gt;', '>')
    if entities:
        data = __dict_replace(data, entities)
    return data.replace('&amp;', '&')


def quoteattr(data, entities={}):
    entities = entities.copy()
    entities.update({'\n': '&#10;', '\r': '&#13;', '\t': '&#9;'})
    data = escape(data, entities)
    if '"' in data:
        if "'" in data:
            data = '"%s"' % data.replace('"', '&quot;')
        else:
            data = "'%s'" % data
    else:
        data = '"%s"' % data
    return data


def _gettextwriter(out, encoding):
    if out is None:
        import sys
        out = sys.stdout
    if isinstance(out, io.RawIOBase):
        buffer = io.BufferedIOBase(out)
        buffer.close = lambda : None
    else:
        buffer = io.BufferedIOBase()
        buffer.writable = lambda : True
        buffer.write = out.write
        try:
            buffer.seekable = out.seekable
            buffer.tell = out.tell
        except AttributeError:
            pass

    return _UnbufferedTextIOWrapper(buffer, encoding=encoding, errors='xmlcharrefreplace', newline='\n')


class _UnbufferedTextIOWrapper(io.TextIOWrapper):

    def write(self, s):
        super(_UnbufferedTextIOWrapper, self).write(s)
        self.flush()


class XMLGenerator(handler.ContentHandler):

    def __init__(self, out=None, encoding='iso-8859-1'):
        handler.ContentHandler.__init__(self)
        out = _gettextwriter(out, encoding)
        self._write = out.write
        self._flush = out.flush
        self._ns_contexts = [{}]
        self._current_context = self._ns_contexts[-1]
        self._undeclared_ns_maps = []
        self._encoding = encoding

    def _qname(self, name):
        if name[0]:
            if 'http://www.w3.org/XML/1998/namespace' == name[0]:
                return 'xml:' + name[1]
            prefix = self._current_context[name[0]]
            if prefix:
                return prefix + ':' + name[1]
        return name[1]

    def startDocument(self):
        self._write('<?xml version="1.0" encoding="%s"?>\n' % self._encoding)

    def endDocument(self):
        self._flush()

    def startPrefixMapping(self, prefix, uri):
        self._ns_contexts.append(self._current_context.copy())
        self._current_context[uri] = prefix
        self._undeclared_ns_maps.append((prefix, uri))

    def endPrefixMapping(self, prefix):
        self._current_context = self._ns_contexts[-1]
        del self._ns_contexts[-1]

    def startElement(self, name, attrs):
        self._write('<' + name)
        for name, value in attrs.items():
            self._write(' %s=%s' % (name, quoteattr(value)))

        self._write('>')

    def endElement(self, name):
        self._write('</%s>' % name)

    def startElementNS(self, name, qname, attrs):
        self._write('<' + self._qname(name))
        for prefix, uri in self._undeclared_ns_maps:
            if prefix:
                self._write(' xmlns:%s="%s"' % (prefix, uri))
            else:
                self._write(' xmlns="%s"' % uri)

        self._undeclared_ns_maps = []
        for name, value in attrs.items():
            self._write(' %s=%s' % (self._qname(name), quoteattr(value)))

        self._write('>')

    def endElementNS(self, name, qname):
        self._write('</%s>' % self._qname(name))

    def characters(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        self._write(escape(content))

    def ignorableWhitespace(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        self._write(content)

    def processingInstruction(self, target, data):
        self._write('<?%s %s?>' % (target, data))


class XMLFilterBase(xmlreader.XMLReader):

    def __init__(self, parent=None):
        xmlreader.XMLReader.__init__(self)
        self._parent = parent

    def error(self, exception):
        self._err_handler.error(exception)

    def fatalError(self, exception):
        self._err_handler.fatalError(exception)

    def warning(self, exception):
        self._err_handler.warning(exception)

    def setDocumentLocator(self, locator):
        self._cont_handler.setDocumentLocator(locator)

    def startDocument(self):
        self._cont_handler.startDocument()

    def endDocument(self):
        self._cont_handler.endDocument()

    def startPrefixMapping(self, prefix, uri):
        self._cont_handler.startPrefixMapping(prefix, uri)

    def endPrefixMapping(self, prefix):
        self._cont_handler.endPrefixMapping(prefix)

    def startElement(self, name, attrs):
        self._cont_handler.startElement(name, attrs)

    def endElement(self, name):
        self._cont_handler.endElement(name)

    def startElementNS(self, name, qname, attrs):
        self._cont_handler.startElementNS(name, qname, attrs)

    def endElementNS(self, name, qname):
        self._cont_handler.endElementNS(name, qname)

    def characters(self, content):
        self._cont_handler.characters(content)

    def ignorableWhitespace(self, chars):
        self._cont_handler.ignorableWhitespace(chars)

    def processingInstruction(self, target, data):
        self._cont_handler.processingInstruction(target, data)

    def skippedEntity(self, name):
        self._cont_handler.skippedEntity(name)

    def notationDecl(self, name, publicId, systemId):
        self._dtd_handler.notationDecl(name, publicId, systemId)

    def unparsedEntityDecl(self, name, publicId, systemId, ndata):
        self._dtd_handler.unparsedEntityDecl(name, publicId, systemId, ndata)

    def resolveEntity(self, publicId, systemId):
        return self._ent_handler.resolveEntity(publicId, systemId)

    def parse(self, source):
        self._parent.setContentHandler(self)
        self._parent.setErrorHandler(self)
        self._parent.setEntityResolver(self)
        self._parent.setDTDHandler(self)
        self._parent.parse(source)

    def setLocale(self, locale):
        self._parent.setLocale(locale)

    def getFeature(self, name):
        return self._parent.getFeature(name)

    def setFeature(self, name, state):
        self._parent.setFeature(name, state)

    def getProperty(self, name):
        return self._parent.getProperty(name)

    def setProperty(self, name, value):
        self._parent.setProperty(name, value)

    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent


def prepare_input_source(source, base=''):
    if type(source) in _StringTypes:
        source = xmlreader.InputSource(source)
    elif hasattr(source, 'read'):
        f = source
        source = xmlreader.InputSource()
        source.setByteStream(f)
        if hasattr(f, 'name'):
            source.setSystemId(f.name)
    if source.getByteStream() is None:
        try:
            sysid = source.getSystemId()
            basehead = os.path.dirname(os.path.normpath(base))
            encoding = sys.getfilesystemencoding()
            if isinstance(sysid, unicode):
                if not isinstance(basehead, unicode):
                    try:
                        basehead = basehead.decode(encoding)
                    except UnicodeDecodeError:
                        sysid = sysid.encode(encoding)

            elif isinstance(basehead, unicode):
                try:
                    sysid = sysid.decode(encoding)
                except UnicodeDecodeError:
                    basehead = basehead.encode(encoding)

            sysidfilename = os.path.join(basehead, sysid)
            isfile = os.path.isfile(sysidfilename)
        except UnicodeError:
            isfile = False

        if isfile:
            source.setSystemId(sysidfilename)
            f = open(sysidfilename, 'rb')
        else:
            source.setSystemId(urlparse.urljoin(base, source.getSystemId()))
            f = urllib.urlopen(source.getSystemId())
        source.setByteStream(f)
    return source
# okay decompiling out\xml.sax.saxutils.pyc
