# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.process
from __future__ import division, absolute_import, print_function
import errno, gc, os, io, select, signal, stat, sys, traceback
try:
    import pty
except ImportError:
    pty = None

try:
    import fcntl, termios
except ImportError:
    fcntl = None

from zope.interface import implementer
from twisted.python import log, failure
from twisted.python.util import switchUID
from twisted.python.compat import items, xrange, _PY3
from twisted.internet import fdesc, abstract, error
from twisted.internet.main import CONNECTION_LOST, CONNECTION_DONE
from twisted.internet._baseprocess import BaseProcess
from twisted.internet.interfaces import IProcessTransport
ProcessExitedAlready = error.ProcessExitedAlready
reapProcessHandlers = {}

def reapAllProcesses():
    for process in list(reapProcessHandlers.values()):
        process.reapProcess()


def registerReapProcessHandler(pid, process):
    if pid in reapProcessHandlers:
        raise RuntimeError('Try to register an already registered process.')
    try:
        auxPID, status = os.waitpid(pid, os.WNOHANG)
    except:
        log.msg('Failed to reap %d:' % pid)
        log.err()
        auxPID = None

    if auxPID:
        process.processEnded(status)
    else:
        reapProcessHandlers[pid] = process
    return


def unregisterReapProcessHandler(pid, process):
    if not (pid in reapProcessHandlers and reapProcessHandlers[pid] == process):
        raise RuntimeError('Try to unregister a process not registered.')
    del reapProcessHandlers[pid]


def detectLinuxBrokenPipeBehavior():
    r, w = os.pipe()
    os.write(w, 'a')
    reads, writes, exes = select.select([w], [], [], 0)
    if reads:
        brokenPipeBehavior = True
    else:
        brokenPipeBehavior = False
    os.close(r)
    os.close(w)
    return brokenPipeBehavior


brokenLinuxPipeBehavior = detectLinuxBrokenPipeBehavior()

class ProcessWriter(abstract.FileDescriptor):
    connected = 1
    ic = 0
    enableReadHack = False

    def __init__(self, reactor, proc, name, fileno, forceReadHack=False):
        abstract.FileDescriptor.__init__(self, reactor)
        fdesc.setNonBlocking(fileno)
        self.proc = proc
        self.name = name
        self.fd = fileno
        if not stat.S_ISFIFO(os.fstat(self.fileno()).st_mode):
            self.enableReadHack = False
        elif forceReadHack:
            self.enableReadHack = True
        else:
            try:
                os.read(self.fileno(), 0)
            except OSError:
                self.enableReadHack = True

        if self.enableReadHack:
            self.startReading()

    def fileno(self):
        return self.fd

    def writeSomeData(self, data):
        rv = fdesc.writeToFD(self.fd, data)
        if rv == len(data) and self.enableReadHack:
            self.startReading()
        return rv

    def write(self, data):
        self.stopReading()
        abstract.FileDescriptor.write(self, data)

    def doRead(self):
        if self.enableReadHack:
            if brokenLinuxPipeBehavior:
                fd = self.fd
                r, w, x = select.select([fd], [fd], [], 0)
                if r and w:
                    return CONNECTION_LOST
            else:
                return CONNECTION_LOST
        else:
            self.stopReading()

    def connectionLost(self, reason):
        fdesc.setBlocking(self.fd)
        abstract.FileDescriptor.connectionLost(self, reason)
        self.proc.childConnectionLost(self.name, reason)


class ProcessReader(abstract.FileDescriptor):
    connected = 1

    def __init__(self, reactor, proc, name, fileno):
        abstract.FileDescriptor.__init__(self, reactor)
        fdesc.setNonBlocking(fileno)
        self.proc = proc
        self.name = name
        self.fd = fileno
        self.startReading()

    def fileno(self):
        return self.fd

    def writeSomeData(self, data):
        return CONNECTION_LOST

    def doRead(self):
        return fdesc.readFromFD(self.fd, self.dataReceived)

    def dataReceived(self, data):
        self.proc.childDataReceived(self.name, data)

    def loseConnection(self):
        if self.connected and not self.disconnecting:
            self.disconnecting = 1
            self.stopReading()
            self.reactor.callLater(0, self.connectionLost, failure.Failure(CONNECTION_DONE))

    def connectionLost(self, reason):
        abstract.FileDescriptor.connectionLost(self, reason)
        self.proc.childConnectionLost(self.name, reason)


class _BaseProcess(BaseProcess, object):
    status = None
    pid = None

    def reapProcess(self):
        try:
            try:
                pid, status = os.waitpid(self.pid, os.WNOHANG)
            except OSError as e:
                if e.errno == errno.ECHILD:
                    pid = None
                else:
                    raise

        except:
            log.msg('Failed to reap %d:' % self.pid)
            log.err()
            pid = None

        if pid:
            self.processEnded(status)
            unregisterReapProcessHandler(pid, self)
        return

    def _getReason(self, status):
        exitCode = sig = None
        if os.WIFEXITED(status):
            exitCode = os.WEXITSTATUS(status)
        else:
            sig = os.WTERMSIG(status)
        if exitCode or sig:
            return error.ProcessTerminated(exitCode, sig, status)
        else:
            return error.ProcessDone(status)

    def signalProcess(self, signalID):
        if signalID in ('HUP', 'STOP', 'INT', 'KILL', 'TERM'):
            signalID = getattr(signal, 'SIG%s' % (signalID,))
        if self.pid is None:
            raise ProcessExitedAlready()
        try:
            os.kill(self.pid, signalID)
        except OSError as e:
            if e.errno == errno.ESRCH:
                raise ProcessExitedAlready()
            else:
                raise

        return

    def _resetSignalDisposition(self):
        for signalnum in xrange(1, signal.NSIG):
            if signal.getsignal(signalnum) == signal.SIG_IGN:
                signal.signal(signalnum, signal.SIG_DFL)

    def _fork(self, path, uid, gid, executable, args, environment, **kwargs):
        collectorEnabled = gc.isenabled()
        gc.disable()
        try:
            self.pid = os.fork()
        except:
            if collectorEnabled:
                gc.enable()
            raise

        if self.pid == 0:
            try:
                sys.settrace(None)
                self._setupChild(**kwargs)
                self._execChild(path, uid, gid, executable, args, environment)
            except:
                try:
                    stderr = os.fdopen(2, 'wb')
                    msg = ('Upon execvpe {0} {1} in environment id {2}\n:').format(executable, str(args), id(environment))
                    if _PY3:
                        stderr = io.TextIOWrapper(stderr, encoding='utf-8')
                    stderr.write(msg)
                    traceback.print_exc(file=stderr)
                    stderr.flush()
                    for fd in xrange(3):
                        os.close(fd)

                except:
                    pass

            os._exit(1)
        if collectorEnabled:
            gc.enable()
        self.status = -1
        return

    def _setupChild(self, *args, **kwargs):
        raise NotImplementedError()

    def _execChild(self, path, uid, gid, executable, args, environment):
        if path:
            os.chdir(path)
        if uid is not None or gid is not None:
            if uid is None:
                uid = os.geteuid()
            if gid is None:
                gid = os.getegid()
            os.setuid(0)
            os.setgid(0)
            switchUID(uid, gid)
        os.execvpe(executable, args, environment)
        return

    def __repr__(self):
        return '<%s pid=%s status=%s>' % (self.__class__.__name__,
         self.pid, self.status)


class _FDDetector(object):
    listdir = os.listdir
    getpid = os.getpid
    openfile = open

    def __init__(self):
        self._implementations = [
         self._procFDImplementation, self._devFDImplementation,
         self._fallbackFDImplementation]

    def _listOpenFDs(self):
        self._listOpenFDs = self._getImplementation()
        return self._listOpenFDs()

    def _getImplementation(self):
        for impl in self._implementations:
            try:
                before = impl()
            except:
                continue

            try:
                fp = self.openfile('/dev/null', 'r')
                after = impl()
            finally:
                fp.close()

            if before != after:
                return impl

        return impl

    def _devFDImplementation(self):
        dname = '/dev/fd'
        result = [ int(fd) for fd in self.listdir(dname) ]
        return result

    def _procFDImplementation(self):
        dname = '/proc/%d/fd' % (self.getpid(),)
        return [ int(fd) for fd in self.listdir(dname) ]

    def _fallbackFDImplementation(self):
        try:
            import resource
        except ImportError:
            maxfds = 1024
        else:
            maxfds = min(1024, resource.getrlimit(resource.RLIMIT_NOFILE)[1])

        return range(maxfds)


detector = _FDDetector()

def _listOpenFDs():
    return detector._listOpenFDs()


@implementer(IProcessTransport)
class Process(_BaseProcess):
    debug = False
    debug_child = False
    status = -1
    pid = None
    processWriterFactory = ProcessWriter
    processReaderFactory = ProcessReader

    def __init__(self, reactor, executable, args, environment, path, proto, uid=None, gid=None, childFDs=None):
        if not proto:
            pass
        _BaseProcess.__init__(self, proto)
        self.pipes = {}
        helpers = {}
        if childFDs is None:
            childFDs = {0: 'w', 1: 'r', 2: 'r'}
        debug = self.debug
        if debug:
            print('childFDs', childFDs)
        _openedPipes = []

        def pipe():
            r, w = os.pipe()
            _openedPipes.extend([r, w])
            return (r, w)

        fdmap = {}
        try:
            for childFD, target in items(childFDs):
                if debug:
                    print('[%d]' % childFD, target)
                if target == 'r':
                    readFD, writeFD = pipe()
                    if debug:
                        print('readFD=%d, writeFD=%d' % (readFD, writeFD))
                    fdmap[childFD] = writeFD
                    helpers[childFD] = readFD
                elif target == 'w':
                    readFD, writeFD = pipe()
                    if debug:
                        print('readFD=%d, writeFD=%d' % (readFD, writeFD))
                    fdmap[childFD] = readFD
                    helpers[childFD] = writeFD
                else:
                    fdmap[childFD] = target

            if debug:
                print('fdmap', fdmap)
            if debug:
                print('helpers', helpers)
            self._fork(path, uid, gid, executable, args, environment, fdmap=fdmap)
        except:
            for pipe in _openedPipes:
                os.close(pipe)

            raise

        self.proto = proto
        for childFD, parentFD in items(helpers):
            os.close(fdmap[childFD])
            if childFDs[childFD] == 'r':
                reader = self.processReaderFactory(reactor, self, childFD, parentFD)
                self.pipes[childFD] = reader
            if childFDs[childFD] == 'w':
                writer = self.processWriterFactory(reactor, self, childFD, parentFD, forceReadHack=True)
                self.pipes[childFD] = writer

        try:
            if self.proto is not None:
                self.proto.makeConnection(self)
        except:
            log.err()

        registerReapProcessHandler(self.pid, self)
        return

    def _setupChild(self, fdmap):
        debug = self.debug_child
        if debug:
            errfd = sys.stderr
            errfd.write('starting _setupChild\n')
        destList = fdmap.values()
        for fd in _listOpenFDs():
            if fd in destList:
                continue
            if debug and fd == errfd.fileno():
                continue
            try:
                os.close(fd)
            except:
                pass

        if debug:
            print('fdmap', fdmap, file=errfd)
        for child in sorted(fdmap.keys()):
            target = fdmap[child]
            if target == child:
                if debug:
                    print('%d already in place' % target, file=errfd)
                fdesc._unsetCloseOnExec(child)
            else:
                if child in fdmap.values():
                    newtarget = os.dup(child)
                    if debug:
                        print('os.dup(%d) -> %d' % (child, newtarget), file=errfd)
                    os.close(child)
                    for c, p in items(fdmap):
                        if p == child:
                            fdmap[c] = newtarget

                if debug:
                    print('os.dup2(%d,%d)' % (target, child), file=errfd)
                os.dup2(target, child)

        old = []
        for fd in fdmap.values():
            if fd not in old:
                if fd not in fdmap.keys():
                    old.append(fd)

        if debug:
            print('old', old, file=errfd)
        for fd in old:
            os.close(fd)

        self._resetSignalDisposition()

    def writeToChild(self, childFD, data):
        self.pipes[childFD].write(data)

    def closeChildFD(self, childFD):
        if childFD in self.pipes:
            self.pipes[childFD].loseConnection()

    def pauseProducing(self):
        for p in self.pipes.itervalues():
            if isinstance(p, ProcessReader):
                p.stopReading()

    def resumeProducing(self):
        for p in self.pipes.itervalues():
            if isinstance(p, ProcessReader):
                p.startReading()

    def closeStdin(self):
        self.closeChildFD(0)

    def closeStdout(self):
        self.closeChildFD(1)

    def closeStderr(self):
        self.closeChildFD(2)

    def loseConnection(self):
        self.closeStdin()
        self.closeStderr()
        self.closeStdout()

    def write(self, data):
        if 0 in self.pipes:
            self.pipes[0].write(data)

    def registerProducer(self, producer, streaming):
        if 0 in self.pipes:
            self.pipes[0].registerProducer(producer, streaming)
        else:
            producer.stopProducing()

    def unregisterProducer(self):
        if 0 in self.pipes:
            self.pipes[0].unregisterProducer()

    def writeSequence(self, seq):
        if 0 in self.pipes:
            self.pipes[0].writeSequence(seq)

    def childDataReceived(self, name, data):
        self.proto.childDataReceived(name, data)

    def childConnectionLost(self, childFD, reason):
        os.close(self.pipes[childFD].fileno())
        del self.pipes[childFD]
        try:
            self.proto.childConnectionLost(childFD)
        except:
            log.err()

        self.maybeCallProcessEnded()

    def maybeCallProcessEnded(self):
        if self.pipes:
            return
        if not self.lostProcess:
            self.reapProcess()
            return
        _BaseProcess.maybeCallProcessEnded(self)


@implementer(IProcessTransport)
class PTYProcess(abstract.FileDescriptor, _BaseProcess):
    status = -1
    pid = None

    def __init__(self, reactor, executable, args, environment, path, proto, uid=None, gid=None, usePTY=None):
        if pty is None and not isinstance(usePTY, (tuple, list)):
            raise NotImplementedError('cannot use PTYProcess on platforms without the pty module.')
        abstract.FileDescriptor.__init__(self, reactor)
        _BaseProcess.__init__(self, proto)
        if isinstance(usePTY, (tuple, list)):
            masterfd, slavefd, ttyname = usePTY
        else:
            masterfd, slavefd = pty.openpty()
            ttyname = os.ttyname(slavefd)
        try:
            self._fork(path, uid, gid, executable, args, environment, masterfd=masterfd, slavefd=slavefd)
        except:
            if not isinstance(usePTY, (tuple, list)):
                os.close(masterfd)
                os.close(slavefd)
            raise

        os.close(slavefd)
        fdesc.setNonBlocking(masterfd)
        self.fd = masterfd
        self.startReading()
        self.connected = 1
        self.status = -1
        try:
            self.proto.makeConnection(self)
        except:
            log.err()

        registerReapProcessHandler(self.pid, self)
        return

    def _setupChild(self, masterfd, slavefd):
        os.close(masterfd)
        os.setsid()
        fcntl.ioctl(slavefd, termios.TIOCSCTTY, '')
        for fd in range(3):
            if fd != slavefd:
                os.close(fd)

        os.dup2(slavefd, 0)
        os.dup2(slavefd, 1)
        os.dup2(slavefd, 2)
        for fd in _listOpenFDs():
            if fd > 2:
                try:
                    os.close(fd)
                except:
                    pass

        self._resetSignalDisposition()

    def closeStdin(self):
        pass

    def closeStdout(self):
        pass

    def closeStderr(self):
        pass

    def doRead(self):
        return fdesc.readFromFD(self.fd, (lambda data: self.proto.childDataReceived(1, data)))

    def fileno(self):
        return self.fd

    def maybeCallProcessEnded(self):
        if self.lostProcess == 2:
            _BaseProcess.maybeCallProcessEnded(self)

    def connectionLost(self, reason):
        abstract.FileDescriptor.connectionLost(self, reason)
        os.close(self.fd)
        self.lostProcess += 1
        self.maybeCallProcessEnded()

    def writeSomeData(self, data):
        return fdesc.writeToFD(self.fd, data)
# okay decompiling out\twisted.internet.process.pyc
