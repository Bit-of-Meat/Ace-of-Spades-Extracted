# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.randbytes
from __future__ import division, absolute_import
import warnings, os, random, string
from twisted.python.compat import _PY3
getrandbits = getattr(random, 'getrandbits', None)
if _PY3:
    _fromhex = bytes.fromhex
else:

    def _fromhex(hexBytes):
        return hexBytes.decode('hex')


class SecureRandomNotAvailable(RuntimeError):
    pass


class SourceNotAvailable(RuntimeError):
    pass


class RandomFactory(object):
    randomSources = ()
    getrandbits = getrandbits

    def _osUrandom(self, nbytes):
        try:
            return os.urandom(nbytes)
        except (AttributeError, NotImplementedError) as e:
            raise SourceNotAvailable(e)

    def secureRandom(self, nbytes, fallback=False):
        try:
            return self._osUrandom(nbytes)
        except SourceNotAvailable:
            pass

        if fallback:
            warnings.warn('urandom unavailable - proceeding with non-cryptographically secure random source', category=RuntimeWarning, stacklevel=2)
            return self.insecureRandom(nbytes)
        raise SecureRandomNotAvailable('No secure random source available')

    def _randBits(self, nbytes):
        if self.getrandbits is not None:
            n = self.getrandbits(nbytes * 8)
            hexBytes = '%%0%dx' % (nbytes * 2) % n
            return _fromhex(hexBytes)
        else:
            raise SourceNotAvailable('random.getrandbits is not available')
            return

    if _PY3:
        _maketrans = bytes.maketrans

        def _randModule(self, nbytes):
            return ('').join([ bytes([random.choice(self._BYTES)]) for i in range(nbytes) ])

    else:
        _maketrans = string.maketrans

        def _randModule(self, nbytes):
            return ('').join([ random.choice(self._BYTES) for i in range(nbytes) ])

    _BYTES = _maketrans('', '')

    def insecureRandom(self, nbytes):
        for src in ('_randBits', '_randModule'):
            try:
                return getattr(self, src)(nbytes)
            except SourceNotAvailable:
                pass


factory = RandomFactory()
secureRandom = factory.secureRandom
insecureRandom = factory.insecureRandom
del factory
__all__ = [
 'secureRandom', 'insecureRandom', 'SecureRandomNotAvailable']
# okay decompiling out\twisted.python.randbytes.pyc
