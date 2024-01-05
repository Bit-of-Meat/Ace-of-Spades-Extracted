# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.logfile
from __future__ import division, absolute_import
import os, glob, time, stat
from twisted.python import threadable

class BaseLogFile:
    synchronized = [
     'write', 'rotate']

    def __init__(self, name, directory, defaultMode=None):
        self.directory = directory
        self.name = name
        self.path = os.path.join(directory, name)
        if defaultMode is None and os.path.exists(self.path):
            self.defaultMode = stat.S_IMODE(os.stat(self.path)[stat.ST_MODE])
        else:
            self.defaultMode = defaultMode
        self._openFile()
        return

    def fromFullPath(cls, filename, *args, **kwargs):
        logPath = os.path.abspath(filename)
        return cls(os.path.basename(logPath), os.path.dirname(logPath), *args, **kwargs)

    fromFullPath = classmethod(fromFullPath)

    def shouldRotate(self):
        raise NotImplementedError

    def _openFile(self):
        self.closed = False
        if os.path.exists(self.path):
            self._file = open(self.path, 'r+', 1)
            self._file.seek(0, 2)
        elif self.defaultMode is not None:
            oldUmask = os.umask(511)
            try:
                self._file = open(self.path, 'w+', 1)
            finally:
                os.umask(oldUmask)

        else:
            self._file = open(self.path, 'w+', 1)
        if self.defaultMode is not None:
            try:
                os.chmod(self.path, self.defaultMode)
            except OSError:
                pass

        return

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_file']
        return state

    def __setstate__(self, state):
        self.__dict__ = state
        self._openFile()

    def write(self, data):
        if self.shouldRotate():
            self.flush()
            self.rotate()
        self._file.write(data)

    def flush(self):
        self._file.flush()

    def close(self):
        self.closed = True
        self._file.close()
        self._file = None
        return

    def reopen(self):
        self.close()
        self._openFile()

    def getCurrentLog(self):
        return LogReader(self.path)


class LogFile(BaseLogFile):

    def __init__(self, name, directory, rotateLength=1000000, defaultMode=None, maxRotatedFiles=None):
        BaseLogFile.__init__(self, name, directory, defaultMode)
        self.rotateLength = rotateLength
        self.maxRotatedFiles = maxRotatedFiles

    def _openFile(self):
        BaseLogFile._openFile(self)
        self.size = self._file.tell()

    def shouldRotate(self):
        return self.rotateLength and self.size >= self.rotateLength

    def getLog(self, identifier):
        filename = '%s.%d' % (self.path, identifier)
        if not os.path.exists(filename):
            raise ValueError('no such logfile exists')
        return LogReader(filename)

    def write(self, data):
        BaseLogFile.write(self, data)
        self.size += len(data)

    def rotate(self):
        if not (os.access(self.directory, os.W_OK) and os.access(self.path, os.W_OK)):
            return
        else:
            logs = self.listLogs()
            logs.reverse()
            for i in logs:
                if self.maxRotatedFiles is not None and i >= self.maxRotatedFiles:
                    os.remove('%s.%d' % (self.path, i))
                else:
                    os.rename('%s.%d' % (self.path, i), '%s.%d' % (self.path, i + 1))

            self._file.close()
            os.rename(self.path, '%s.1' % self.path)
            self._openFile()
            return

    def listLogs(self):
        result = []
        for name in glob.glob('%s.*' % self.path):
            try:
                counter = int(name.split('.')[-1])
                if counter:
                    result.append(counter)
            except ValueError:
                pass

        result.sort()
        return result

    def __getstate__(self):
        state = BaseLogFile.__getstate__(self)
        del state['size']
        return state


threadable.synchronize(LogFile)

class DailyLogFile(BaseLogFile):

    def _openFile(self):
        BaseLogFile._openFile(self)
        self.lastDate = self.toDate(os.stat(self.path)[8])

    def shouldRotate(self):
        return self.toDate() > self.lastDate

    def toDate(self, *args):
        return time.localtime(*args)[:3]

    def suffix(self, tupledate):
        try:
            return ('_').join(map(str, tupledate))
        except:
            return ('_').join(map(str, self.toDate(tupledate)))

    def getLog(self, identifier):
        if self.toDate(identifier) == self.lastDate:
            return self.getCurrentLog()
        filename = '%s.%s' % (self.path, self.suffix(identifier))
        if not os.path.exists(filename):
            raise ValueError('no such logfile exists')
        return LogReader(filename)

    def write(self, data):
        BaseLogFile.write(self, data)
        self.lastDate = max(self.lastDate, self.toDate())

    def rotate(self):
        if not (os.access(self.directory, os.W_OK) and os.access(self.path, os.W_OK)):
            return
        newpath = '%s.%s' % (self.path, self.suffix(self.lastDate))
        if os.path.exists(newpath):
            return
        self._file.close()
        os.rename(self.path, newpath)
        self._openFile()

    def __getstate__(self):
        state = BaseLogFile.__getstate__(self)
        del state['lastDate']
        return state


threadable.synchronize(DailyLogFile)

class LogReader:

    def __init__(self, name):
        self._file = open(name, 'r')

    def readLines(self, lines=10):
        result = []
        for i in range(lines):
            line = self._file.readline()
            if not line:
                break
            result.append(line)

        return result

    def close(self):
        self._file.close()
# okay decompiling out\twisted.python.logfile.pyc
