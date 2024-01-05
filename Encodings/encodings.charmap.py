# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\encodings.charmap
import codecs

class Codec(codecs.Codec):
    encode = codecs.charmap_encode
    decode = codecs.charmap_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def __init__(self, errors='strict', mapping=None):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.mapping = mapping

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, self.mapping)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def __init__(self, errors='strict', mapping=None):
        codecs.IncrementalDecoder.__init__(self, errors)
        self.mapping = mapping

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, self.mapping)[0]


class StreamWriter(Codec, codecs.StreamWriter):

    def __init__(self, stream, errors='strict', mapping=None):
        codecs.StreamWriter.__init__(self, stream, errors)
        self.mapping = mapping

    def encode(self, input, errors='strict'):
        return Codec.encode(input, errors, self.mapping)


class StreamReader(Codec, codecs.StreamReader):

    def __init__(self, stream, errors='strict', mapping=None):
        codecs.StreamReader.__init__(self, stream, errors)
        self.mapping = mapping

    def decode(self, input, errors='strict'):
        return Codec.decode(input, errors, self.mapping)


def getregentry():
    return codecs.CodecInfo(name='charmap', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)
# okay decompiling out\encodings.charmap.pyc
