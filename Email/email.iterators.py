# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\email.iterators
__all__ = [
 'body_line_iterator',
 'typed_subpart_iterator',
 'walk']
import sys
from cStringIO import StringIO

def walk(self):
    yield self
    if self.is_multipart():
        for subpart in self.get_payload():
            for subsubpart in subpart.walk():
                yield subsubpart


def body_line_iterator(msg, decode=False):
    for subpart in msg.walk():
        payload = subpart.get_payload(decode=decode)
        if isinstance(payload, basestring):
            for line in StringIO(payload):
                yield line


def typed_subpart_iterator(msg, maintype='text', subtype=None):
    for subpart in msg.walk():
        if subpart.get_content_maintype() == maintype:
            if subtype is None or subpart.get_content_subtype() == subtype:
                yield subpart

    return


def _structure(msg, fp=None, level=0, include_default=False):
    if fp is None:
        fp = sys.stdout
    tab = ' ' * (level * 4)
    print >> fp, tab + msg.get_content_type(),
    if include_default:
        print >> fp, '[%s]' % msg.get_default_type()
    else:
        print >> fp
    if msg.is_multipart():
        for subpart in msg.get_payload():
            _structure(subpart, fp, level + 1, include_default)

    return
# okay decompiling out\email.iterators.pyc
