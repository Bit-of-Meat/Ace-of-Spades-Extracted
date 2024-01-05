# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\email.base64mime
__all__ = [
 'base64_len', 
 'body_decode', 
 'body_encode', 
 'decode', 
 'decodestring', 
 'encode', 
 'encodestring', 
 'header_encode']
from binascii import b2a_base64, a2b_base64
from email.utils import fix_eols
CRLF = '\r\n'
NL = '\n'
EMPTYSTRING = ''
MISC_LEN = 7

def base64_len(s):
    groups_of_3, leftover = divmod(len(s), 3)
    n = groups_of_3 * 4
    if leftover:
        n += 4
    return n


def header_encode(header, charset='iso-8859-1', keep_eols=False, maxlinelen=76, eol=NL):
    if not header:
        return header
    if not keep_eols:
        header = fix_eols(header)
    base64ed = []
    max_encoded = maxlinelen - len(charset) - MISC_LEN
    max_unencoded = max_encoded * 3 // 4
    for i in range(0, len(header), max_unencoded):
        base64ed.append(b2a_base64(header[i:i + max_unencoded]))

    lines = []
    for line in base64ed:
        if line.endswith(NL):
            line = line[:-1]
        lines.append('=?%s?b?%s?=' % (charset, line))

    joiner = eol + ' '
    return joiner.join(lines)


def encode(s, binary=True, maxlinelen=76, eol=NL):
    if not s:
        return s
    if not binary:
        s = fix_eols(s)
    encvec = []
    max_unencoded = maxlinelen * 3 // 4
    for i in range(0, len(s), max_unencoded):
        enc = b2a_base64(s[i:i + max_unencoded])
        if enc.endswith(NL) and eol != NL:
            enc = enc[:-1] + eol
        encvec.append(enc)

    return EMPTYSTRING.join(encvec)


body_encode = encode
encodestring = encode

def decode(s, convert_eols=None):
    if not s:
        return s
    dec = a2b_base64(s)
    if convert_eols:
        return dec.replace(CRLF, convert_eols)
    return dec


body_decode = decode
decodestring = decode
# okay decompiling out\email.base64mime.pyc
