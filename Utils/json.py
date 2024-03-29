# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\json
__version__ = '2.0.9'
__all__ = [
 'dump', 'dumps', 'load', 'loads', 
 'JSONDecoder', 'JSONEncoder']
__author__ = 'Bob Ippolito <bob@redivi.com>'
from .decoder import JSONDecoder
from .encoder import JSONEncoder
_default_encoder = JSONEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, indent=None, separators=None, encoding='utf-8', default=None)

def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw):
    if not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and encoding == 'utf-8' and default is None and not sort_keys and not kw:
        iterable = _default_encoder.iterencode(obj)
    else:
        if cls is None:
            cls = JSONEncoder
        iterable = cls(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, encoding=encoding, default=default, sort_keys=sort_keys, **kw).iterencode(obj)
    for chunk in iterable:
        fp.write(chunk)

    return


def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw):
    if not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and encoding == 'utf-8' and default is None and not sort_keys and not kw:
        return _default_encoder.encode(obj)
    else:
        if cls is None:
            cls = JSONEncoder
        return cls(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, encoding=encoding, default=default, sort_keys=sort_keys, **kw).encode(obj)


_default_decoder = JSONDecoder(encoding=None, object_hook=None, object_pairs_hook=None)

def load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    return loads(fp.read(), encoding=encoding, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)


def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    if cls is None and encoding is None and object_hook is None and parse_int is None and parse_float is None and parse_constant is None and object_pairs_hook is None and not kw:
        return _default_decoder.decode(s)
    else:
        if cls is None:
            cls = JSONDecoder
        if object_hook is not None:
            kw['object_hook'] = object_hook
        if object_pairs_hook is not None:
            kw['object_pairs_hook'] = object_pairs_hook
        if parse_float is not None:
            kw['parse_float'] = parse_float
        if parse_int is not None:
            kw['parse_int'] = parse_int
        if parse_constant is not None:
            kw['parse_constant'] = parse_constant
        return cls(encoding=encoding, **kw).decode(s)
# okay decompiling out\json.pyc
