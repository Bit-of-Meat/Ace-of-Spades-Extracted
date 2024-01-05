# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.error
from __future__ import division, absolute_import
try:
    from future_builtins import ascii
except ImportError:
    pass

__all__ = [
 'Error', 'PageRedirect', 'InfiniteRedirection', 'RenderError', 
 'MissingRenderMethod', 
 'MissingTemplateLoader', 'UnexposedMethodError', 
 'UnfilledSlot', 'UnsupportedType', 
 'FlattenerError', 
 'RedirectWithNoLocation']
from collections import Sequence
from twisted.web._responses import RESPONSES
from twisted.python.compat import unicode

def _codeToMessage(code):
    try:
        return RESPONSES.get(int(code)).decode('ascii')
    except (ValueError, AttributeError):
        return

    return


class Error(Exception):

    def __init__(self, code, message=None, response=None):
        message = message or _codeToMessage(code)
        Exception.__init__(self, code, message, response)
        self.status = code
        self.message = message
        self.response = response

    def __str__(self):
        return '%s %s' % (self.status, self.message)


class PageRedirect(Error):

    def __init__(self, code, message=None, response=None, location=None):
        Error.__init__(self, code, message, response)
        if self.message and location:
            self.message = '%s to %s' % (self.message, location)
        self.location = location


class InfiniteRedirection(Error):

    def __init__(self, code, message=None, response=None, location=None):
        Error.__init__(self, code, message, response)
        if self.message and location:
            self.message = '%s to %s' % (self.message, location)
        self.location = location


class RedirectWithNoLocation(Error):

    def __init__(self, code, message, uri):
        message = '%s to %s' % (message, uri)
        Error.__init__(self, code, message)
        self.uri = uri


class UnsupportedMethod(Exception):
    allowedMethods = ()

    def __init__(self, allowedMethods, *args):
        Exception.__init__(self, allowedMethods, *args)
        self.allowedMethods = allowedMethods
        if not isinstance(allowedMethods, Sequence):
            raise TypeError('First argument must be a sequence of supported methods, but my first argument is not a sequence.')


class SchemeNotSupported(Exception):
    pass


class RenderError(Exception):
    pass


class MissingRenderMethod(RenderError):

    def __init__(self, element, renderName):
        RenderError.__init__(self, element, renderName)
        self.element = element
        self.renderName = renderName

    def __repr__(self):
        return '%r: %r had no render method named %r' % (
         self.__class__.__name__, self.element, self.renderName)


class MissingTemplateLoader(RenderError):

    def __init__(self, element):
        RenderError.__init__(self, element)
        self.element = element

    def __repr__(self):
        return '%r: %r had no loader' % (self.__class__.__name__,
         self.element)


class UnexposedMethodError(Exception):
    pass


class UnfilledSlot(Exception):
    pass


class UnsupportedType(Exception):
    pass


class FlattenerError(Exception):

    def __init__(self, exception, roots, traceback):
        self._exception = exception
        self._roots = roots
        self._traceback = traceback
        Exception.__init__(self, exception, roots, traceback)

    def _formatRoot(self, obj):
        from twisted.web.template import Tag
        if isinstance(obj, (bytes, str, unicode)):
            if len(obj) > 40:
                if isinstance(obj, unicode):
                    ellipsis = '<...>'
                else:
                    ellipsis = '<...>'
                return ascii(obj[:20] + ellipsis + obj[-20:])
            else:
                return ascii(obj)

        elif isinstance(obj, Tag):
            if obj.filename is None:
                return 'Tag <' + obj.tagName + '>'
            else:
                return 'File "%s", line %d, column %d, in "%s"' % (
                 obj.filename, obj.lineNumber,
                 obj.columnNumber, obj.tagName)

        else:
            return ascii(obj)
        return

    def __repr__(self):
        from traceback import format_list
        if self._roots:
            roots = '  ' + ('\n  ').join([ self._formatRoot(r) for r in self._roots ]) + '\n'
        else:
            roots = ''
        if self._traceback:
            traceback = ('\n').join([ line for entry in format_list(self._traceback) for line in entry.splitlines()
                                    ]) + '\n'
        else:
            traceback = ''
        return 'Exception while flattening:\n' + roots + traceback + self._exception.__class__.__name__ + ': ' + str(self._exception) + '\n'

    def __str__(self):
        return repr(self)
# okay decompiling out\twisted.web.error.pyc
