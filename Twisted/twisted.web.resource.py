# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.resource
from __future__ import division, absolute_import
__all__ = [
 'IResource', 'getChildForRequest', 
 'Resource', 'ErrorPage', 'NoResource', 
 'ForbiddenResource', 
 'EncodingResourceWrapper']
import warnings
from zope.interface import Attribute, Interface, implementer
from twisted.python.compat import nativeString, unicode
from twisted.python.reflect import prefixedMethodNames
from twisted.python.components import proxyForInterface
from twisted.web._responses import FORBIDDEN, NOT_FOUND
from twisted.web.error import UnsupportedMethod

class IResource(Interface):
    isLeaf = Attribute('\n        Signal if this IResource implementor is a "leaf node" or not. If True,\n        getChildWithDefault will not be called on this Resource.\n        ')

    def getChildWithDefault(name, request):
        pass

    def putChild(path, child):
        pass

    def render(request):
        pass


def getChildForRequest(resource, request):
    while request.postpath and not resource.isLeaf:
        pathElement = request.postpath.pop(0)
        request.prepath.append(pathElement)
        resource = resource.getChildWithDefault(pathElement, request)

    return resource


@implementer(IResource)
class Resource:
    entityType = IResource
    server = None

    def __init__(self):
        self.children = {}

    isLeaf = 0

    def listStaticNames(self):
        return list(self.children.keys())

    def listStaticEntities(self):
        return list(self.children.items())

    def listNames(self):
        return list(self.listStaticNames()) + self.listDynamicNames()

    def listEntities(self):
        return list(self.listStaticEntities()) + self.listDynamicEntities()

    def listDynamicNames(self):
        return []

    def listDynamicEntities(self, request=None):
        return []

    def getStaticEntity(self, name):
        return self.children.get(name)

    def getDynamicEntity(self, name, request):
        if not self.children.has_key(name):
            return self.getChild(name, request)
        else:
            return
            return

    def delEntity(self, name):
        del self.children[name]

    def reallyPutEntity(self, name, entity):
        self.children[name] = entity

    def getChild(self, path, request):
        return NoResource('No such child resource.')

    def getChildWithDefault(self, path, request):
        if path in self.children:
            return self.children[path]
        return self.getChild(path, request)

    def getChildForRequest(self, request):
        warnings.warn('Please use module level getChildForRequest.', DeprecationWarning, 2)
        return getChildForRequest(self, request)

    def putChild(self, path, child):
        self.children[path] = child
        child.server = self.server

    def render(self, request):
        m = getattr(self, 'render_' + nativeString(request.method), None)
        if not m:
            try:
                allowedMethods = self.allowedMethods
            except AttributeError:
                allowedMethods = _computeAllowedMethods(self)

            raise UnsupportedMethod(allowedMethods)
        return m(request)

    def render_HEAD(self, request):
        return self.render_GET(request)


def _computeAllowedMethods(resource):
    allowedMethods = []
    for name in prefixedMethodNames(resource.__class__, 'render_'):
        allowedMethods.append(name.encode('ascii'))

    return allowedMethods


class ErrorPage(Resource):
    template = '\n<html>\n  <head><title>%(code)s - %(brief)s</title></head>\n  <body>\n    <h1>%(brief)s</h1>\n    <p>%(detail)s</p>\n  </body>\n</html>\n'

    def __init__(self, status, brief, detail):
        Resource.__init__(self)
        self.code = status
        self.brief = brief
        self.detail = detail

    def render(self, request):
        request.setResponseCode(self.code)
        request.setHeader('content-type', 'text/html; charset=utf-8')
        interpolated = self.template % dict(code=self.code, brief=self.brief, detail=self.detail)
        if isinstance(interpolated, unicode):
            return interpolated.encode('utf-8')
        return interpolated

    def getChild(self, chnam, request):
        return self


class NoResource(ErrorPage):

    def __init__(self, message='Sorry. No luck finding that resource.'):
        ErrorPage.__init__(self, NOT_FOUND, 'No Such Resource', message)


class ForbiddenResource(ErrorPage):

    def __init__(self, message='Sorry, resource is forbidden.'):
        ErrorPage.__init__(self, FORBIDDEN, 'Forbidden Resource', message)


class _IEncodingResource(Interface):

    def getEncoder(request):
        pass


@implementer(_IEncodingResource)
class EncodingResourceWrapper(proxyForInterface(IResource)):

    def __init__(self, original, encoders):
        super(EncodingResourceWrapper, self).__init__(original)
        self._encoders = encoders

    def getEncoder(self, request):
        for encoderFactory in self._encoders:
            encoder = encoderFactory.encoderForRequest(request)
            if encoder is not None:
                return encoder

        return
# okay decompiling out\twisted.web.resource.pyc
