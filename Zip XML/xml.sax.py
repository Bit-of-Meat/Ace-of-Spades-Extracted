# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\xml.sax
from xmlreader import InputSource
from handler import ContentHandler, ErrorHandler
from _exceptions import SAXException, SAXNotRecognizedException, SAXParseException, SAXNotSupportedException, SAXReaderNotAvailable

def parse(source, handler, errorHandler=ErrorHandler()):
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.setErrorHandler(errorHandler)
    parser.parse(source)


def parseString(string, handler, errorHandler=ErrorHandler()):
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    if errorHandler is None:
        errorHandler = ErrorHandler()
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.setErrorHandler(errorHandler)
    inpsrc = InputSource()
    inpsrc.setByteStream(StringIO(string))
    parser.parse(inpsrc)
    return


default_parser_list = [
 'xml.sax.expatreader']
_false = 0
if _false:
    import xml.sax.expatreader
import os, sys
if 'PY_SAX_PARSER' in os.environ:
    default_parser_list = os.environ['PY_SAX_PARSER'].split(',')
del os
_key = 'python.xml.sax.parser'
if sys.platform[:4] == 'java' and sys.registry.containsKey(_key):
    default_parser_list = sys.registry.getProperty(_key).split(',')

def make_parser(parser_list=[]):
    for parser_name in parser_list + default_parser_list:
        try:
            return _create_parser(parser_name)
        except ImportError as e:
            import sys
            if parser_name in sys.modules:
                raise
        except SAXReaderNotAvailable:
            pass

    raise SAXReaderNotAvailable('No parsers found', None)
    return


if sys.platform[:4] == 'java':

    def _create_parser(parser_name):
        from org.python.core import imp
        drv_module = imp.importName(parser_name, 0, globals())
        return drv_module.create_parser()


else:

    def _create_parser(parser_name):
        drv_module = __import__(parser_name, {}, {}, ['create_parser'])
        return drv_module.create_parser()


del sys
# okay decompiling out\xml.sax.pyc