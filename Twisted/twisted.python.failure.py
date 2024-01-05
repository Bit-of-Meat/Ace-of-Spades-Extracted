# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.failure
from __future__ import division, absolute_import
import sys, linecache, inspect, opcode
from inspect import getmro
from twisted.python.compat import _PY3, NativeStringIO as StringIO
from twisted.python import reflect
count = 0
traceupLength = 4

class DefaultException(Exception):
    pass


def format_frames(frames, write, detail='default'):
    if detail not in ('default', 'brief', 'verbose', 'verbose-vars-not-captured'):
        raise ValueError('Detail must be default, brief, verbose, or verbose-vars-not-captured. (not %r)' % (
         detail,))
    w = write
    if detail == 'brief':
        for method, filename, lineno, localVars, globalVars in frames:
            w('%s:%s:%s\n' % (filename, lineno, method))

    elif detail == 'default':
        for method, filename, lineno, localVars, globalVars in frames:
            w('  File "%s", line %s, in %s\n' % (filename, lineno, method))
            w('    %s\n' % linecache.getline(filename, lineno).strip())

    elif detail == 'verbose-vars-not-captured':
        for method, filename, lineno, localVars, globalVars in frames:
            w('%s:%d: %s(...)\n' % (filename, lineno, method))

        w(' [Capture of Locals and Globals disabled (use captureVars=True)]\n')
    elif detail == 'verbose':
        for method, filename, lineno, localVars, globalVars in frames:
            w('%s:%d: %s(...)\n' % (filename, lineno, method))
            w(' [ Locals ]\n')
            for name, val in localVars:
                w('  %s : %s\n' % (name, repr(val)))

            w(' ( Globals )\n')
            for name, val in globalVars:
                w('  %s : %s\n' % (name, repr(val)))


EXCEPTION_CAUGHT_HERE = '--- <exception caught here> ---'

class NoCurrentExceptionError(Exception):
    pass


class _Traceback(object):

    def __init__(self, frames):
        head, frames = frames[0], frames[1:]
        name, filename, lineno, localz, globalz = head
        self.tb_frame = _Frame(name, filename)
        self.tb_lineno = lineno
        if len(frames) == 0:
            self.tb_next = None
        else:
            self.tb_next = _Traceback(frames)
        return


class _Frame(object):

    def __init__(self, name, filename):
        self.f_code = _Code(name, filename)
        self.f_globals = {}
        self.f_locals = {}


class _Code(object):

    def __init__(self, name, filename):
        self.co_name = name
        self.co_filename = filename


class Failure():
    pickled = 0
    stack = None
    _yieldOpcode = chr(opcode.opmap['YIELD_VALUE'])

    def __init__(self, exc_value=None, exc_type=None, exc_tb=None, captureVars=False):
        global count
        count = count + 1
        self.count = count
        self.type = self.value = tb = None
        self.captureVars = captureVars
        if isinstance(exc_value, str) and exc_type is None:
            raise TypeError('Strings are not supported by Failure')
        stackOffset = 0
        if exc_value is None:
            exc_value = self._findFailure()
        if exc_value is None:
            self.type, self.value, tb = sys.exc_info()
            if self.type is None:
                raise NoCurrentExceptionError()
            stackOffset = 1
        elif exc_type is None:
            if isinstance(exc_value, Exception):
                self.type = exc_value.__class__
            else:
                self.type = type(exc_value)
            self.value = exc_value
        else:
            self.type = exc_type
            self.value = exc_value
        if isinstance(self.value, Failure):
            self.__dict__ = self.value.__dict__
            return
        else:
            if tb is None:
                if exc_tb:
                    tb = exc_tb
                elif _PY3:
                    tb = self.value.__traceback__
            frames = self.frames = []
            stack = self.stack = []
            self.tb = tb
            if tb:
                f = tb.tb_frame
            elif not isinstance(self.value, Failure):
                f = stackOffset = None
            while stackOffset and f:
                f = f.f_back
                stackOffset -= 1

            while f:
                if captureVars:
                    localz = f.f_locals.copy()
                    if f.f_locals is f.f_globals:
                        globalz = {}
                    else:
                        globalz = f.f_globals.copy()
                    for d in (globalz, localz):
                        if '__builtins__' in d:
                            del d['__builtins__']

                    localz = localz.items()
                    globalz = globalz.items()
                else:
                    localz = globalz = ()
                stack.insert(0, (
                 f.f_code.co_name,
                 f.f_code.co_filename,
                 f.f_lineno,
                 localz,
                 globalz))
                f = f.f_back

            while tb is not None:
                f = tb.tb_frame
                if captureVars:
                    localz = f.f_locals.copy()
                    if f.f_locals is f.f_globals:
                        globalz = {}
                    else:
                        globalz = f.f_globals.copy()
                    for d in (globalz, localz):
                        if '__builtins__' in d:
                            del d['__builtins__']

                    localz = list(localz.items())
                    globalz = list(globalz.items())
                else:
                    localz = globalz = ()
                frames.append((
                 f.f_code.co_name,
                 f.f_code.co_filename,
                 tb.tb_lineno,
                 localz,
                 globalz))
                tb = tb.tb_next

            if inspect.isclass(self.type) and issubclass(self.type, Exception):
                parentCs = getmro(self.type)
                self.parents = list(map(reflect.qual, parentCs))
            else:
                self.parents = [
                 self.type]
            return

    def trap(self, *errorTypes):
        error = self.check(*errorTypes)
        if not error:
            if _PY3:
                self.raiseException()
            else:
                raise self
        return error

    def check(self, *errorTypes):
        for error in errorTypes:
            err = error
            if inspect.isclass(error) and issubclass(error, Exception):
                err = reflect.qual(error)
            if err in self.parents:
                return error

        return

    if _PY3:

        def raiseException(self):
            raise self.value.with_traceback(self.tb)

    else:
        exec 'def raiseException(self):\n    raise self.type, self.value, self.tb'
    raiseException.__doc__ = '\n        raise the original exception, preserving traceback\n        information if available.\n        '

    def throwExceptionIntoGenerator(self, g):
        return g.throw(self.type, self.value, self.tb)

    def _findFailure(cls):
        tb = sys.exc_info()[-1]
        if not tb:
            return
        else:
            secondLastTb = None
            lastTb = tb
            while lastTb.tb_next:
                secondLastTb = lastTb
                lastTb = lastTb.tb_next

            lastFrame = lastTb.tb_frame
            if lastFrame.f_code is cls.raiseException.__code__:
                return lastFrame.f_locals.get('self')
            if not lastFrame.f_code.co_code or lastFrame.f_code.co_code[lastTb.tb_lasti] != cls._yieldOpcode:
                return
            if secondLastTb:
                frame = secondLastTb.tb_frame
                if frame.f_code is cls.throwExceptionIntoGenerator.__code__:
                    return frame.f_locals.get('self')
            frame = tb.tb_frame.f_back
            if frame and frame.f_code is cls.throwExceptionIntoGenerator.__code__:
                return frame.f_locals.get('self')
            return

    _findFailure = classmethod(_findFailure)

    def __repr__(self):
        return '<%s %s: %s>' % (reflect.qual(self.__class__),
         reflect.qual(self.type),
         self.getErrorMessage())

    def __str__(self):
        return '[Failure instance: %s]' % self.getBriefTraceback()

    def __getstate__(self):
        if self.pickled:
            return self.__dict__
        else:
            c = self.__dict__.copy()
            c['frames'] = [ [v[0], v[1], v[2], _safeReprVars(v[3]), _safeReprVars(v[4])] for v in self.frames
                          ]
            c['tb'] = None
            if self.stack is not None:
                c['stack'] = [ [v[0], v[1], v[2], _safeReprVars(v[3]), _safeReprVars(v[4])] for v in self.stack
                             ]
            c['pickled'] = 1
            return c

    def cleanFailure(self):
        self.__dict__ = self.__getstate__()
        if _PY3:
            self.value.__traceback__ = None
        return

    def getTracebackObject(self):
        if self.tb is not None:
            return self.tb
        else:
            if len(self.frames) > 0:
                return _Traceback(self.frames)
            else:
                return

            return

    def getErrorMessage(self):
        if isinstance(self.value, Failure):
            return self.value.getErrorMessage()
        return reflect.safe_str(self.value)

    def getBriefTraceback(self):
        io = StringIO()
        self.printBriefTraceback(file=io)
        return io.getvalue()

    def getTraceback(self, elideFrameworkCode=0, detail='default'):
        io = StringIO()
        self.printTraceback(file=io, elideFrameworkCode=elideFrameworkCode, detail=detail)
        return io.getvalue()

    def printTraceback(self, file=None, elideFrameworkCode=False, detail='default'):
        if file is None:
            from twisted.python import log
            file = log.logerr
        w = file.write
        if detail == 'verbose' and not self.captureVars:
            formatDetail = 'verbose-vars-not-captured'
        else:
            formatDetail = detail
        if detail == 'verbose':
            w('*--- Failure #%d%s---\n' % (
             self.count,
             self.pickled and ' (pickled) ' or ' '))
        elif detail == 'brief':
            if self.frames:
                hasFrames = 'Traceback'
            else:
                hasFrames = 'Traceback (failure with no frames)'
            w('%s: %s: %s\n' % (
             hasFrames,
             reflect.safe_str(self.type),
             reflect.safe_str(self.value)))
        else:
            w('Traceback (most recent call last):\n')
        if self.frames:
            if not elideFrameworkCode:
                format_frames(self.stack[-traceupLength:], w, formatDetail)
                w('%s\n' % (EXCEPTION_CAUGHT_HERE,))
            format_frames(self.frames, w, formatDetail)
        elif not detail == 'brief':
            w('Failure: ')
        if not detail == 'brief':
            w('%s: %s\n' % (reflect.qual(self.type),
             reflect.safe_str(self.value)))
        if isinstance(self.value, Failure):
            file.write(' (chained Failure)\n')
            self.value.printTraceback(file, elideFrameworkCode, detail)
        if detail == 'verbose':
            w('*--- End of Failure #%d ---\n' % self.count)
        return

    def printBriefTraceback(self, file=None, elideFrameworkCode=0):
        self.printTraceback(file, elideFrameworkCode, detail='brief')

    def printDetailedTraceback(self, file=None, elideFrameworkCode=0):
        self.printTraceback(file, elideFrameworkCode, detail='verbose')


def _safeReprVars(varsDictItems):
    return [ (name, reflect.safe_repr(obj)) for name, obj in varsDictItems ]


DO_POST_MORTEM = True

def _debuginit(self, exc_value=None, exc_type=None, exc_tb=None, captureVars=False, Failure__init__=Failure.__init__):
    if (
     exc_value, exc_type, exc_tb) == (None, None, None):
        exc = sys.exc_info()
        if not exc[0] == self.__class__ and DO_POST_MORTEM:
            try:
                strrepr = str(exc[1])
            except:
                strrepr = 'broken str'

            print "Jumping into debugger for post-mortem of exception '%s':" % (strrepr,)
            import pdb
            pdb.post_mortem(exc[2])
    Failure__init__(self, exc_value, exc_type, exc_tb, captureVars)
    return


def startDebugMode():
    Failure.__init__ = _debuginit
# okay decompiling out\twisted.python.failure.pyc
