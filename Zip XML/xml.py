# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\xml
__all__ = [
 'dom', 'parsers', 'sax', 'etree']
_MINIMUM_XMLPLUS_VERSION = (0, 8, 4)
try:
    import _xmlplus
except ImportError:
    pass

try:
    v = _xmlplus.version_info
except AttributeError:
    pass

if v >= _MINIMUM_XMLPLUS_VERSION:
    import sys
    _xmlplus.__path__.extend(__path__)
    sys.modules[__name__] = _xmlplus
else:
    del v
# okay decompiling out\xml.pyc
