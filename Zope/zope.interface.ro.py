# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface.ro
__docformat__ = 'restructuredtext'

def _mergeOrderings(orderings):
    seen = {}
    result = []
    for ordering in reversed(orderings):
        for o in reversed(ordering):
            if o not in seen:
                seen[o] = 1
                result.insert(0, o)

    return result


def _flatten(ob):
    result = [
     ob]
    i = 0
    for ob in iter(result):
        i += 1
        result[i:i] = ob.__bases__

    return result


def ro(object):
    return _mergeOrderings([_flatten(object)])
# okay decompiling out\zope.interface.ro.pyc
