# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.formats.plaintext
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import pyglet

class PlainTextDecoder(pyglet.text.DocumentDecoder):

    def decode(self, text, location=None):
        document = pyglet.text.document.UnformattedDocument()
        document.insert_text(0, text)
        return document
# okay decompiling out\pyglet.text.formats.plaintext.pyc
