# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web._flatten
from __future__ import division, absolute_import
from io import BytesIO
from sys import exc_info
from types import GeneratorType
from traceback import extract_tb
from twisted.internet.defer import Deferred
from twisted.python.compat import unicode, nativeString, iteritems
from twisted.web._stan import Tag, slot, voidElements, Comment, CDATA, CharRef
from twisted.web.error import UnfilledSlot, UnsupportedType, FlattenerError
from twisted.web.iweb import IRenderable

def escapeForContent(data):
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    data = data.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return data


def attributeEscapingDoneOutside(data):
    if isinstance(data, unicode):
        return data.encode('utf-8')
    return data


def flattenWithAttributeEscaping(root):
    if isinstance(root, bytes):
        root = escapeForContent(root)
        root = root.replace('"', '&quot;')
        yield root
    elif isinstance(root, Deferred):
        yield root.addCallback(flattenWithAttributeEscaping)
    else:
        for subroot in root:
            yield flattenWithAttributeEscaping(subroot)


def escapedCDATA(data):
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    return data.replace(']]>', ']]]]><![CDATA[>')


def escapedComment(data):
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    data = data.replace('--', '- - ').replace('>', '&gt;')
    if data and data[-1:] == '-':
        data += ' '
    return data


def _getSlotValue(name, slotData, default=None):
    for slotFrame in slotData[::-1]:
        if slotFrame is not None and name in slotFrame:
            return slotFrame[name]
    else:
        if default is not None:
            return default
        raise UnfilledSlot(name)

    return


def _flattenElement(request, root, slotData, renderFactory, dataEscaper):

    def keepGoing(newRoot, dataEscaper=dataEscaper, renderFactory=renderFactory):
        return _flattenElement(request, newRoot, slotData, renderFactory, dataEscaper)

    if isinstance(root, (bytes, unicode)):
        yield dataEscaper(root)
    elif isinstance(root, slot):
        slotValue = _getSlotValue(root.name, slotData, root.default)
        yield keepGoing(slotValue)
    elif isinstance(root, CDATA):
        yield '<![CDATA['
        yield escapedCDATA(root.data)
        yield ']]>'
    elif isinstance(root, Comment):
        yield '<!--'
        yield escapedComment(root.data)
        yield '-->'
    elif isinstance(root, Tag):
        slotData.append(root.slotData)
        if root.render is not None:
            rendererName = root.render
            rootClone = root.clone(False)
            rootClone.render = None
            renderMethod = renderFactory.lookupRenderMethod(rendererName)
            result = renderMethod(request, rootClone)
            yield keepGoing(result)
            slotData.pop()
            return
        if not root.tagName:
            yield keepGoing(root.children)
            return
        yield '<'
        if isinstance(root.tagName, unicode):
            tagName = root.tagName.encode('ascii')
        else:
            tagName = root.tagName
        yield tagName
        for k, v in iteritems(root.attributes):
            if isinstance(k, unicode):
                k = k.encode('ascii')
            yield ' ' + k + '="'
            attribute = keepGoing(v, attributeEscapingDoneOutside)
            yield flattenWithAttributeEscaping(attribute)
            yield '"'

        if root.children or nativeString(tagName) not in voidElements:
            yield '>'
            yield keepGoing(root.children, escapeForContent)
            yield '</' + tagName + '>'
        else:
            yield ' />'
    elif isinstance(root, (tuple, list, GeneratorType)):
        for element in root:
            yield keepGoing(element)

    elif isinstance(root, CharRef):
        escaped = '&#%d;' % (root.ordinal,)
        yield escaped.encode('ascii')
    elif isinstance(root, Deferred):
        yield root.addCallback((lambda result: (result, keepGoing(result))))
    elif IRenderable.providedBy(root):
        result = root.render(request)
        yield keepGoing(result, renderFactory=root)
    else:
        raise UnsupportedType(root)
    return


def _flattenTree(request, root):
    stack = [
     _flattenElement(request, root, [], None, escapeForContent)]
    while stack:
        try:
            frame = stack[-1].gi_frame
            element = next(stack[-1])
        except StopIteration:
            stack.pop()
        except Exception as e:
            stack.pop()
            roots = []
            for generator in stack:
                roots.append(generator.gi_frame.f_locals['root'])

            roots.append(frame.f_locals['root'])
            raise FlattenerError(e, roots, extract_tb(exc_info()[2]))
        else:
            if type(element) is bytes:
                yield element
            elif isinstance(element, Deferred):

                def cbx(originalAndToFlatten):
                    original, toFlatten = originalAndToFlatten
                    stack.append(toFlatten)
                    return original

                yield element.addCallback(cbx)
            else:
                stack.append(element)

    return


def _writeFlattenedData(state, write, result):
    while True:
        try:
            element = next(state)
        except StopIteration:
            result.callback(None)
        except:
            result.errback()
        else:
            if type(element) is bytes:
                write(element)
                continue
            else:

                def cby(original):
                    _writeFlattenedData(state, write, result)
                    return original

                element.addCallbacks(cby, result.errback)
            break

    return


def flatten(request, root, write):
    result = Deferred()
    state = _flattenTree(request, root)
    _writeFlattenedData(state, write, result)
    return result


def flattenString(request, root):
    io = BytesIO()
    d = flatten(request, root, io.write)
    d.addCallback((lambda _: io.getvalue()))
    return d
# okay decompiling out\twisted.web._flatten.pyc
