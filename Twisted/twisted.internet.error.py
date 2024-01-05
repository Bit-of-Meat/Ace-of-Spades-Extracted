# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet.error
from __future__ import division, absolute_import
import socket
from twisted.python import deprecate
from twisted.python.versions import Version

class BindError(Exception):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class CannotListenError(BindError):

    def __init__(self, interface, port, socketError):
        BindError.__init__(self, interface, port, socketError)
        self.interface = interface
        self.port = port
        self.socketError = socketError

    def __str__(self):
        iface = self.interface or 'any'
        return "Couldn't listen on %s:%s: %s." % (iface, self.port,
         self.socketError)


class MulticastJoinError(Exception):
    pass


class MessageLengthError(Exception):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class DNSLookupError(IOError):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class ConnectInProgressError(Exception):
    pass


class ConnectError(Exception):

    def __init__(self, osError=None, string=''):
        self.osError = osError
        Exception.__init__(self, string)

    def __str__(self):
        s = self.__doc__ or self.__class__.__name__
        if self.osError:
            s = '%s: %s' % (s, self.osError)
        if self.args[0]:
            s = '%s: %s' % (s, self.args[0])
        s = '%s.' % s
        return s


class ConnectBindError(ConnectError):
    pass


class UnknownHostError(ConnectError):
    pass


class NoRouteError(ConnectError):
    pass


class ConnectionRefusedError(ConnectError):
    pass


class TCPTimedOutError(ConnectError):
    pass


class BadFileError(ConnectError):
    pass


class ServiceNameUnknownError(ConnectError):
    pass


class UserError(ConnectError):
    pass


class TimeoutError(UserError):
    pass


class SSLError(ConnectError):
    pass


class VerifyError(Exception):
    pass


class PeerVerifyError(VerifyError):
    pass


class CertificateError(Exception):
    pass


try:
    import errno
    errnoMapping = {errno.ENETUNREACH: NoRouteError, 
       errno.ECONNREFUSED: ConnectionRefusedError, 
       errno.ETIMEDOUT: TCPTimedOutError}
    if hasattr(errno, 'WSAECONNREFUSED'):
        errnoMapping[errno.WSAECONNREFUSED] = ConnectionRefusedError
        errnoMapping[errno.WSAENETUNREACH] = NoRouteError
except ImportError:
    errnoMapping = {}

def getConnectError(e):
    if isinstance(e, Exception):
        args = e.args
    else:
        args = e
    try:
        number, string = args
    except ValueError:
        return ConnectError(string=e)

    if hasattr(socket, 'gaierror') and isinstance(e, socket.gaierror):
        klass = UnknownHostError
    else:
        klass = errnoMapping.get(number, ConnectError)
    return klass(number, string)


class ConnectionClosed(Exception):
    pass


class ConnectionLost(ConnectionClosed):

    def __str__(self):
        s = self.__doc__.strip().splitlines()[0]
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class ConnectionAborted(ConnectionLost):
    pass


class ConnectionDone(ConnectionClosed):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class FileDescriptorOverrun(ConnectionLost):
    pass


class ConnectionFdescWentAway(ConnectionLost):
    pass


class AlreadyCalled(ValueError):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class AlreadyCancelled(ValueError):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class PotentialZombieWarning(Warning):
    MESSAGE = 'spawnProcess called, but the SIGCHLD handler is not installed. This probably means you have not yet called reactor.run, or called reactor.run(installSignalHandler=0). You will probably never see this process finish, and it may become a zombie process.'


deprecate.deprecatedModuleAttribute(Version('Twisted', 10, 0, 0), 'There is no longer any potential for zombie process.', __name__, 'PotentialZombieWarning')

class ProcessDone(ConnectionDone):

    def __init__(self, status):
        Exception.__init__(self, 'process finished with exit code 0')
        self.exitCode = 0
        self.signal = None
        self.status = status
        return


class ProcessTerminated(ConnectionLost):

    def __init__(self, exitCode=None, signal=None, status=None):
        self.exitCode = exitCode
        self.signal = signal
        self.status = status
        s = 'process ended'
        if exitCode is not None:
            s = s + ' with exit code %s' % exitCode
        if signal is not None:
            s = s + ' by signal %s' % signal
        Exception.__init__(self, s)
        return


class ProcessExitedAlready(Exception):
    pass


class NotConnectingError(RuntimeError):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class NotListeningError(RuntimeError):

    def __str__(self):
        s = self.__doc__
        if self.args:
            s = '%s: %s' % (s, (' ').join(self.args))
        s = '%s.' % s
        return s


class ReactorNotRunning(RuntimeError):
    pass


class ReactorNotRestartable(RuntimeError):
    pass


class ReactorAlreadyRunning(RuntimeError):
    pass


class ReactorAlreadyInstalledError(AssertionError):
    pass


class ConnectingCancelledError(Exception):

    def __init__(self, address):
        Exception.__init__(self, address)
        self.address = address


class NoProtocol(Exception):
    pass


class UnsupportedAddressFamily(Exception):
    pass


class UnsupportedSocketType(Exception):
    pass


class AlreadyListened(Exception):
    pass


class InvalidAddressError(ValueError):

    def __init__(self, address, message):
        self.address = address
        self.message = message


__all__ = [
 'BindError', 'CannotListenError', 'MulticastJoinError', 
 'MessageLengthError', 
 'DNSLookupError', 'ConnectInProgressError', 
 'ConnectError', 'ConnectBindError', 
 'UnknownHostError', 'NoRouteError', 
 'ConnectionRefusedError', 'TCPTimedOutError', 
 'BadFileError', 
 'ServiceNameUnknownError', 'UserError', 'TimeoutError', 
 'SSLError', 
 'VerifyError', 'PeerVerifyError', 'CertificateError', 
 'getConnectError', 
 'ConnectionClosed', 'ConnectionLost', 
 'ConnectionDone', 'ConnectionFdescWentAway', 
 'AlreadyCalled', 
 'AlreadyCancelled', 'PotentialZombieWarning', 'ProcessDone', 
 'ProcessTerminated', 
 'ProcessExitedAlready', 'NotConnectingError', 
 'NotListeningError', 'ReactorNotRunning', 
 'ReactorAlreadyRunning', 
 'ReactorAlreadyInstalledError', 'ConnectingCancelledError', 
 'UnsupportedAddressFamily', 
 'UnsupportedSocketType', 'InvalidAddressError']
# okay decompiling out\twisted.internet.error.pyc
