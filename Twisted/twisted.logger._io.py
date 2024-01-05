# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._io
import sys
from ._levels import LogLevel

class LoggingFile(object):
    softspace = 0

    def __init__(self, logger, level=LogLevel.info, encoding=None):
        self.level = level
        self.log = logger
        if encoding is None:
            self._encoding = sys.getdefaultencoding()
        else:
            self._encoding = encoding
        self._buffer = ''
        self._closed = False
        return

    @property
    def closed(self):
        return self._closed

    @property
    def encoding(self):
        return self._encoding

    @property
    def mode(self):
        return 'w'

    @property
    def newlines(self):
        return

    @property
    def name(self):
        return ('<{0} {1}#{2}>').format(self.__class__.__name__, self.log.namespace, self.level.name)

    def close(self):
        self._closed = True

    def flush(self):
        pass

    def fileno(self):
        return -1

    def isatty(self):
        return False

    def write(self, string):
        if self._closed:
            raise ValueError('I/O operation on closed file')
        if isinstance(string, bytes):
            string = string.decode(self._encoding)
        lines = (self._buffer + string).split('\n')
        self._buffer = lines[-1]
        lines = lines[0:-1]
        for line in lines:
            self.log.emit(self.level, format='{log_io}', log_io=line)

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def _unsupported(self, *args):
        raise IOError('unsupported operation')

    read = _unsupported
    next = _unsupported
    readline = _unsupported
    readlines = _unsupported
    xreadlines = _unsupported
    seek = _unsupported
    tell = _unsupported
    truncate = _unsupported
# okay decompiling out\twisted.logger._io.pyc
