# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.main
from __future__ import division, absolute_import
from twisted.internet import error
CONNECTION_DONE = error.ConnectionDone('Connection done')
CONNECTION_LOST = error.ConnectionLost('Connection lost')

def installReactor(reactor):
    import twisted.internet, sys
    if 'twisted.internet.reactor' in sys.modules:
        raise error.ReactorAlreadyInstalledError('reactor already installed')
    twisted.internet.reactor = reactor
    sys.modules['twisted.internet.reactor'] = reactor


__all__ = [
 'CONNECTION_LOST', 'CONNECTION_DONE', 'installReactor']
# okay decompiling out\twisted.internet.main.pyc
