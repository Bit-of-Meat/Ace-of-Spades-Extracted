# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web._element
from __future__ import division, absolute_import
from zope.interface import implementer
from twisted.web.iweb import IRenderable
from twisted.web.error import MissingRenderMethod, UnexposedMethodError
from twisted.web.error import MissingTemplateLoader

class Expose(object):

    def __init__(self, doc=None):
        self.doc = doc

    def __call__(self, *funcObjs):
        if not funcObjs:
            raise TypeError('expose() takes at least 1 argument (0 given)')
        for fObj in funcObjs:
            fObj.exposedThrough = getattr(fObj, 'exposedThrough', [])
            fObj.exposedThrough.append(self)

        return funcObjs[0]

    _nodefault = object()

    def get(self, instance, methodName, default=_nodefault):
        method = getattr(instance, methodName, None)
        exposedThrough = getattr(method, 'exposedThrough', [])
        if self not in exposedThrough:
            if default is self._nodefault:
                raise UnexposedMethodError(self, methodName)
            return default
        return method

    @classmethod
    def _withDocumentation(cls, thunk):
        return cls(thunk.__doc__)


exposer = Expose._withDocumentation

@exposer
def renderer():
    pass


@implementer(IRenderable)
class Element(object):
    loader = None

    def __init__(self, loader=None):
        if loader is not None:
            self.loader = loader
        return

    def lookupRenderMethod(self, name):
        method = renderer.get(self, name, None)
        if method is None:
            raise MissingRenderMethod(self, name)
        return method

    def render(self, request):
        loader = self.loader
        if loader is None:
            raise MissingTemplateLoader(self)
        return loader.load()
# okay decompiling out\twisted.web._element.pyc
