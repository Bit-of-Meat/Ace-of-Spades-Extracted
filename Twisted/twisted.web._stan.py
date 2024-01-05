# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web._stan
from __future__ import absolute_import, division
from twisted.python.compat import iteritems

class slot(object):

    def __init__(self, name, default=None, filename=None, lineNumber=None, columnNumber=None):
        self.name = name
        self.children = []
        self.default = default
        self.filename = filename
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

    def __repr__(self):
        return 'slot(%r)' % (self.name,)


class Tag(object):
    slotData = None
    filename = None
    lineNumber = None
    columnNumber = None

    def __init__(self, tagName, attributes=None, children=None, render=None, filename=None, lineNumber=None, columnNumber=None):
        self.tagName = tagName
        self.render = render
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes
        if children is None:
            self.children = []
        else:
            self.children = children
        if filename is not None:
            self.filename = filename
        if lineNumber is not None:
            self.lineNumber = lineNumber
        if columnNumber is not None:
            self.columnNumber = columnNumber
        return

    def fillSlots(self, **slots):
        if self.slotData is None:
            self.slotData = {}
        self.slotData.update(slots)
        return self

    def __call__(self, *children, **kw):
        self.children.extend(children)
        for k, v in iteritems(kw):
            if k[-1] == '_':
                k = k[:-1]
            if k == 'render':
                self.render = v
            else:
                self.attributes[k] = v

        return self

    def _clone(self, obj, deep):
        if hasattr(obj, 'clone'):
            return obj.clone(deep)
        else:
            if isinstance(obj, (list, tuple)):
                return [ self._clone(x, deep) for x in obj ]
            return obj

    def clone(self, deep=True):
        if deep:
            newchildren = [ self._clone(x, True) for x in self.children ]
        else:
            newchildren = self.children[:]
        newattrs = self.attributes.copy()
        for key in newattrs.keys():
            newattrs[key] = self._clone(newattrs[key], True)

        newslotdata = None
        if self.slotData:
            newslotdata = self.slotData.copy()
            for key in newslotdata:
                newslotdata[key] = self._clone(newslotdata[key], True)

        newtag = Tag(self.tagName, attributes=newattrs, children=newchildren, render=self.render, filename=self.filename, lineNumber=self.lineNumber, columnNumber=self.columnNumber)
        newtag.slotData = newslotdata
        return newtag

    def clear(self):
        self.children = []
        return self

    def __repr__(self):
        rstr = ''
        if self.attributes:
            rstr += ', attributes=%r' % self.attributes
        if self.children:
            rstr += ', children=%r' % self.children
        return 'Tag(%r%s)' % (self.tagName, rstr)


voidElements = ('img', 'br', 'hr', 'base', 'meta', 'link', 'param', 'area', 'input',
                'col', 'basefont', 'isindex', 'frame', 'command', 'embed', 'keygen',
                'source', 'track', 'wbs')

class CDATA(object):

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return 'CDATA(%r)' % (self.data,)


class Comment(object):

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return 'Comment(%r)' % (self.data,)


class CharRef(object):

    def __init__(self, ordinal):
        self.ordinal = ordinal

    def __repr__(self):
        return 'CharRef(%d)' % (self.ordinal,)
# okay decompiling out\twisted.web._stan.pyc
