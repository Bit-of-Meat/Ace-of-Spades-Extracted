# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._file
from zope.interface import implementer
from twisted.python.compat import ioType, unicode
from ._observer import ILogObserver
from ._format import formatTime
from ._format import timeFormatRFC3339
from ._format import formatEventAsClassicLogText

@implementer(ILogObserver)
class FileLogObserver(object):

    def __init__(self, outFile, formatEvent):
        if ioType(outFile) is not unicode:
            self._encoding = 'utf-8'
        else:
            self._encoding = None
        self._outFile = outFile
        self.formatEvent = formatEvent
        return

    def __call__(self, event):
        text = self.formatEvent(event)
        if text is None:
            text = ''
        if 'log_failure' in event:
            try:
                traceback = event['log_failure'].getTraceback()
            except Exception:
                traceback = '(UNABLE TO OBTAIN TRACEBACK FROM EVENT)\n'

            text = ('\n').join((text, traceback))
        if self._encoding is not None:
            text = text.encode(self._encoding)
        if text:
            self._outFile.write(text)
            self._outFile.flush()
        return


def textFileLogObserver(outFile, timeFormat=timeFormatRFC3339):

    def formatEvent(event):
        return formatEventAsClassicLogText(event, formatTime=(lambda e: formatTime(e, timeFormat)))

    return FileLogObserver(outFile, formatEvent)
# okay decompiling out\twisted.logger._file.pyc
