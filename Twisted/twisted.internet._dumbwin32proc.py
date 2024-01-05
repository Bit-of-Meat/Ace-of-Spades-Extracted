# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._dumbwin32proc
import os, win32api, win32con, win32event, win32file, win32pipe, win32process, win32security, pywintypes
PIPE_ATTRS_INHERITABLE = win32security.SECURITY_ATTRIBUTES()
PIPE_ATTRS_INHERITABLE.bInheritHandle = 1
from zope.interface import implements
from twisted.internet.interfaces import IProcessTransport, IConsumer, IProducer
from twisted.python.win32 import quoteArguments
from twisted.internet import error
from twisted.internet import _pollingfile
from twisted.internet._baseprocess import BaseProcess

def debug(msg):
    import sys
    print msg
    sys.stdout.flush()


class _Reaper(_pollingfile._PollableResource):

    def __init__(self, proc):
        self.proc = proc

    def checkWork(self):
        if win32event.WaitForSingleObject(self.proc.hProcess, 0) != win32event.WAIT_OBJECT_0:
            return 0
        exitCode = win32process.GetExitCodeProcess(self.proc.hProcess)
        self.deactivate()
        self.proc.processEnded(exitCode)
        return 0


def _findShebang(filename):
    f = file(filename, 'rU')
    if f.read(2) == '#!':
        exe = f.readline(1024).strip('\n')
        return exe


def _invalidWin32App(pywinerr):
    return pywinerr.args[0] == 193


class Process(_pollingfile._PollingTimer, BaseProcess):
    implements(IProcessTransport, IConsumer, IProducer)
    closedNotifies = 0

    def __init__(self, reactor, protocol, command, args, environment, path):
        _pollingfile._PollingTimer.__init__(self, reactor)
        BaseProcess.__init__(self, protocol)
        sAttrs = win32security.SECURITY_ATTRIBUTES()
        sAttrs.bInheritHandle = 1
        self.hStdoutR, hStdoutW = win32pipe.CreatePipe(sAttrs, 0)
        self.hStderrR, hStderrW = win32pipe.CreatePipe(sAttrs, 0)
        hStdinR, self.hStdinW = win32pipe.CreatePipe(sAttrs, 0)
        win32pipe.SetNamedPipeHandleState(self.hStdinW, win32pipe.PIPE_NOWAIT, None, None)
        StartupInfo = win32process.STARTUPINFO()
        StartupInfo.hStdOutput = hStdoutW
        StartupInfo.hStdError = hStderrW
        StartupInfo.hStdInput = hStdinR
        StartupInfo.dwFlags = win32process.STARTF_USESTDHANDLES
        currentPid = win32api.GetCurrentProcess()
        tmp = win32api.DuplicateHandle(currentPid, self.hStdoutR, currentPid, 0, 0, win32con.DUPLICATE_SAME_ACCESS)
        win32file.CloseHandle(self.hStdoutR)
        self.hStdoutR = tmp
        tmp = win32api.DuplicateHandle(currentPid, self.hStderrR, currentPid, 0, 0, win32con.DUPLICATE_SAME_ACCESS)
        win32file.CloseHandle(self.hStderrR)
        self.hStderrR = tmp
        tmp = win32api.DuplicateHandle(currentPid, self.hStdinW, currentPid, 0, 0, win32con.DUPLICATE_SAME_ACCESS)
        win32file.CloseHandle(self.hStdinW)
        self.hStdinW = tmp
        env = os.environ.copy()
        env.update(environment or {})
        cmdline = quoteArguments(args)

        def doCreate():
            self.hProcess, self.hThread, self.pid, dwTid = win32process.CreateProcess(command, cmdline, None, None, 1, 0, env, path, StartupInfo)
            return

        try:
            try:
                doCreate()
            except TypeError as e:
                if e.args != ('All dictionary items must be strings, or all must be unicode', ):
                    raise
                newenv = {}
                for key, value in env.items():
                    newenv[unicode(key)] = unicode(value)

                env = newenv
                doCreate()

        except pywintypes.error as pwte:
            if not _invalidWin32App(pwte):
                raise OSError(pwte)
            else:
                sheb = _findShebang(command)
                if sheb is None:
                    raise OSError('%r is neither a Windows executable, nor a script with a shebang line' % command)
                else:
                    args = list(args)
                    args.insert(0, command)
                    cmdline = quoteArguments(args)
                    origcmd = command
                    command = sheb
                    try:
                        doCreate()
                    except pywintypes.error as pwte2:
                        if _invalidWin32App(pwte2):
                            raise OSError('%r has an invalid shebang line: %r is not a valid executable' % (
                             origcmd, sheb))
                        raise OSError(pwte2)

        win32file.CloseHandle(hStderrW)
        win32file.CloseHandle(hStdoutW)
        win32file.CloseHandle(hStdinR)
        self.stdout = _pollingfile._PollableReadPipe(self.hStdoutR, (lambda data: self.proto.childDataReceived(1, data)), self.outConnectionLost)
        self.stderr = _pollingfile._PollableReadPipe(self.hStderrR, (lambda data: self.proto.childDataReceived(2, data)), self.errConnectionLost)
        self.stdin = _pollingfile._PollableWritePipe(self.hStdinW, self.inConnectionLost)
        for pipewatcher in (self.stdout, self.stderr, self.stdin):
            self._addPollableResource(pipewatcher)

        self.proto.makeConnection(self)
        self._addPollableResource(_Reaper(self))
        return

    def signalProcess(self, signalID):
        if self.pid is None:
            raise error.ProcessExitedAlready()
        if signalID in ('INT', 'TERM', 'KILL'):
            win32process.TerminateProcess(self.hProcess, 1)
        return

    def _getReason(self, status):
        if status == 0:
            return error.ProcessDone(status)
        return error.ProcessTerminated(status)

    def write(self, data):
        self.stdin.write(data)

    def writeSequence(self, seq):
        self.stdin.writeSequence(seq)

    def writeToChild(self, fd, data):
        if fd == 0:
            self.stdin.write(data)
        else:
            raise KeyError(fd)

    def closeChildFD(self, fd):
        if fd == 0:
            self.closeStdin()
        elif fd == 1:
            self.closeStdout()
        elif fd == 2:
            self.closeStderr()
        else:
            raise NotImplementedError('Only standard-IO file descriptors available on win32')

    def closeStdin(self):
        self.stdin.close()

    def closeStderr(self):
        self.stderr.close()

    def closeStdout(self):
        self.stdout.close()

    def loseConnection(self):
        self.closeStdin()
        self.closeStdout()
        self.closeStderr()

    def outConnectionLost(self):
        self.proto.childConnectionLost(1)
        self.connectionLostNotify()

    def errConnectionLost(self):
        self.proto.childConnectionLost(2)
        self.connectionLostNotify()

    def inConnectionLost(self):
        self.proto.childConnectionLost(0)
        self.connectionLostNotify()

    def connectionLostNotify(self):
        self.closedNotifies += 1
        self.maybeCallProcessEnded()

    def maybeCallProcessEnded(self):
        if self.closedNotifies == 3 and self.lostProcess:
            win32file.CloseHandle(self.hProcess)
            win32file.CloseHandle(self.hThread)
            self.hProcess = None
            self.hThread = None
            BaseProcess.maybeCallProcessEnded(self)
        return

    def registerProducer(self, producer, streaming):
        self.stdin.registerProducer(producer, streaming)

    def unregisterProducer(self):
        self.stdin.unregisterProducer()

    def pauseProducing(self):
        self._pause()

    def resumeProducing(self):
        self._unpause()

    def stopProducing(self):
        self.loseConnection()

    def __repr__(self):
        return '<%s pid=%s>' % (self.__class__.__name__, self.pid)
# okay decompiling out\twisted.internet._dumbwin32proc.pyc
