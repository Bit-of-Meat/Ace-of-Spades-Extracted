# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.log
from __future__ import division, absolute_import
import sys, time, warnings
from datetime import datetime
from zope.interface import Interface
from twisted.python.compat import unicode, _PY3
from twisted.python import context
from twisted.python import reflect
from twisted.python import util
from twisted.python import failure
from twisted.python.threadable import synchronize
from twisted.logger import Logger as NewLogger, LogLevel as NewLogLevel, STDLibLogObserver as NewSTDLibLogObserver, LegacyLogObserverWrapper, LoggingFile, LogPublisher as NewPublisher, globalLogPublisher as newGlobalLogPublisher, globalLogBeginner as newGlobalLogBeginner
from twisted.logger._global import LogBeginner
from twisted.logger._legacy import publishToNewObserver as _publishNew

class ILogContext:
    pass


class ILogObserver(Interface):

    def __call__(eventDict):
        pass


context.setDefault(ILogContext, {'system': '-'})

def callWithContext(ctx, func, *args, **kw):
    newCtx = context.get(ILogContext).copy()
    newCtx.update(ctx)
    return context.call({ILogContext: newCtx}, func, *args, **kw)


def callWithLogger(logger, func, *args, **kw):
    try:
        lp = logger.logPrefix()
    except KeyboardInterrupt:
        raise
    except:
        lp = '(buggy logPrefix method)'
        err(system=lp)

    try:
        return callWithContext({'system': lp}, func, *args, **kw)
    except KeyboardInterrupt:
        raise
    except:
        err(system=lp)


def err(_stuff=None, _why=None, **kw):
    if _stuff is None:
        _stuff = failure.Failure()
    if isinstance(_stuff, failure.Failure):
        msg(failure=_stuff, why=_why, isError=1, **kw)
    elif isinstance(_stuff, Exception):
        msg(failure=failure.Failure(_stuff), why=_why, isError=1, **kw)
    else:
        msg(repr(_stuff), why=_why, isError=1, **kw)
    return


deferr = err

class Logger:

    def logPrefix(self):
        return '-'


class LogPublisher:
    synchronized = [
     'msg']

    def __init__(self, observerPublisher=None, publishPublisher=None, logBeginner=None, warningsModule=warnings):
        if publishPublisher is None:
            publishPublisher = NewPublisher()
            if observerPublisher is None:
                observerPublisher = publishPublisher
        if observerPublisher is None:
            observerPublisher = NewPublisher()
        self._observerPublisher = observerPublisher
        self._publishPublisher = publishPublisher
        self._legacyObservers = []
        if logBeginner is None:
            beginnerPublisher = NewPublisher()
            beginnerPublisher.addObserver(observerPublisher)
            logBeginner = LogBeginner(beginnerPublisher, NullFile(), sys, warnings)
        self._logBeginner = logBeginner
        self._warningsModule = warningsModule
        self._oldshowwarning = warningsModule.showwarning
        self.showwarning = self._logBeginner.showwarning
        return

    @property
    def observers(self):
        return [ x.legacyObserver for x in self._legacyObservers ]

    def _startLogging(self, other, setStdout):
        wrapped = LegacyLogObserverWrapper(other)
        self._legacyObservers.append(wrapped)
        self._logBeginner.beginLoggingTo([wrapped], True, setStdout)

    def _stopLogging(self):
        if self._warningsModule.showwarning == self.showwarning:
            self._warningsModule.showwarning = self._oldshowwarning

    def addObserver(self, other):
        wrapped = LegacyLogObserverWrapper(other)
        self._legacyObservers.append(wrapped)
        self._observerPublisher.addObserver(wrapped)

    def removeObserver(self, other):
        for observer in self._legacyObservers:
            if observer.legacyObserver == other:
                self._legacyObservers.remove(observer)
                self._observerPublisher.removeObserver(observer)
                break

    def msg(self, *message, **kw):
        actualEventDict = (context.get(ILogContext) or {}).copy()
        actualEventDict.update(kw)
        actualEventDict['message'] = message
        actualEventDict['time'] = time.time()
        if 'isError' not in actualEventDict:
            actualEventDict['isError'] = 0
        _publishNew(self._publishPublisher, actualEventDict, textFromEventDict)


synchronize(LogPublisher)
if 'theLogPublisher' not in globals():

    def _actually(something):

        def decorate(thingWithADocstring):
            return something

        return decorate


    theLogPublisher = LogPublisher(observerPublisher=newGlobalLogPublisher, publishPublisher=newGlobalLogPublisher, logBeginner=newGlobalLogBeginner)

    @_actually(theLogPublisher.addObserver)
    def addObserver(observer):
        pass


    @_actually(theLogPublisher.removeObserver)
    def removeObserver(observer):
        pass


    @_actually(theLogPublisher.msg)
    def msg(*message, **event):
        pass


    @_actually(theLogPublisher.showwarning)
    def showwarning():
        pass


def _safeFormat(fmtString, fmtDict):
    try:
        text = fmtString % fmtDict
    except KeyboardInterrupt:
        raise
    except:
        try:
            text = 'Invalid format string or unformattable object in log message: %r, %s' % (
             fmtString, fmtDict)
        except:
            try:
                text = 'UNFORMATTABLE OBJECT WRITTEN TO LOG with fmt %r, MESSAGE LOST' % (
                 fmtString,)
            except:
                text = 'PATHOLOGICAL ERROR IN BOTH FORMAT STRING AND MESSAGE DETAILS, MESSAGE LOST'

    if _PY3:
        if isinstance(text, bytes):
            text = text.decode('utf-8')
    elif isinstance(text, unicode):
        text = text.encode('utf-8')
    return text


def textFromEventDict(eventDict):
    edm = eventDict['message']
    if not edm:
        if eventDict['isError'] and 'failure' in eventDict:
            why = eventDict.get('why')
            if why:
                why = reflect.safe_str(why)
            else:
                why = 'Unhandled Error'
            try:
                traceback = eventDict['failure'].getTraceback()
            except Exception as e:
                traceback = '(unable to obtain traceback): ' + str(e)

            text = why + '\n' + traceback
        else:
            if 'format' in eventDict:
                text = _safeFormat(eventDict['format'], eventDict)
            else:
                return
    else:
        text = (' ').join(map(reflect.safe_str, edm))
    return text


class _GlobalStartStopMixIn:

    def start(self):
        addObserver(self.emit)

    def stop(self):
        removeObserver(self.emit)


class FileLogObserver(_GlobalStartStopMixIn):
    timeFormat = None

    def __init__(self, f):
        self.write = f.write
        self.flush = f.flush

    def getTimezoneOffset(self, when):
        offset = datetime.utcfromtimestamp(when) - datetime.fromtimestamp(when)
        return offset.days * 86400 + offset.seconds

    def formatTime(self, when):
        if self.timeFormat is not None:
            return datetime.fromtimestamp(when).strftime(self.timeFormat)
        else:
            tzOffset = -self.getTimezoneOffset(when)
            when = datetime.utcfromtimestamp(when + tzOffset)
            tzHour = abs(int(tzOffset / 60 / 60))
            tzMin = abs(int(tzOffset / 60 % 60))
            if tzOffset < 0:
                tzSign = '-'
            else:
                tzSign = '+'
            return '%d-%02d-%02d %02d:%02d:%02d%s%02d%02d' % (
             when.year, when.month, when.day,
             when.hour, when.minute, when.second,
             tzSign, tzHour, tzMin)

    def emit(self, eventDict):
        text = textFromEventDict(eventDict)
        if text is None:
            return
        else:
            timeStr = self.formatTime(eventDict['time'])
            fmtDict = {'system': eventDict['system'], 
               'text': text.replace('\n', '\n\t')}
            msgStr = _safeFormat('[%(system)s] %(text)s\n', fmtDict)
            util.untilConcludes(self.write, timeStr + ' ' + msgStr)
            util.untilConcludes(self.flush)
            return


class PythonLoggingObserver(_GlobalStartStopMixIn, object):

    def __init__(self, loggerName='twisted'):
        self._newObserver = NewSTDLibLogObserver(loggerName)

    def emit(self, eventDict):
        if 'log_format' in eventDict:
            _publishNew(self._newObserver, eventDict, textFromEventDict)


class StdioOnnaStick:
    closed = 0
    softspace = 0
    mode = 'wb'
    name = '<stdio (log)>'

    def __init__(self, isError=0, encoding=None):
        self.isError = isError
        if encoding is None:
            encoding = sys.getdefaultencoding()
        self.encoding = encoding
        self.buf = ''
        return

    def close(self):
        pass

    def fileno(self):
        return -1

    def flush(self):
        pass

    def read(self):
        raise IOError("can't read from the log!")

    readline = read
    readlines = read
    seek = read
    tell = read

    def write(self, data):
        if not _PY3 and isinstance(data, unicode):
            data = data.encode(self.encoding)
        d = (self.buf + data).split('\n')
        self.buf = d[-1]
        messages = d[0:-1]
        for message in messages:
            msg(message, printed=1, isError=self.isError)

    def writelines(self, lines):
        for line in lines:
            if not _PY3 and isinstance(line, unicode):
                line = line.encode(self.encoding)
            msg(line, printed=1, isError=self.isError)


def startLogging(file, *a, **kw):
    if isinstance(file, LoggingFile):
        return
    flo = FileLogObserver(file)
    startLoggingWithObserver(flo.emit, *a, **kw)
    return flo


def startLoggingWithObserver(observer, setStdout=1):
    theLogPublisher._startLogging(observer, setStdout)
    msg('Log opened.')


class NullFile:
    softspace = 0

    def read(self):
        pass

    def write(self, bytes):
        pass

    def flush(self):
        pass

    def close(self):
        pass


def discardLogs():
    global logfile
    logfile = NullFile()


if 'logfile' not in globals():
    logfile = LoggingFile(logger=NewLogger(), level=NewLogLevel.info, encoding=getattr(sys.stdout, 'encoding', None))
    logerr = LoggingFile(logger=NewLogger(), level=NewLogLevel.error, encoding=getattr(sys.stderr, 'encoding', None))

class DefaultObserver(_GlobalStartStopMixIn):
    stderr = sys.stderr

    def emit(self, eventDict):
        if eventDict['isError']:
            text = textFromEventDict(eventDict)
            self.stderr.write(text)
            self.stderr.flush()


if 'defaultObserver' not in globals():
    defaultObserver = DefaultObserver()
# okay decompiling out\twisted.python.log.pyc
