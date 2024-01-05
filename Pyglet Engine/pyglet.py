# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import os, sys
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc
version = '1.2dev'

def _require_ctypes_version(version):
    import ctypes
    req = [ int(i) for i in version.split('.') ]
    have = [ int(i) for i in ctypes.__version__.split('.') ]
    if not tuple(have) >= tuple(req):
        raise ImportError('pyglet requires ctypes %s or later.' % version)


_require_ctypes_version('1.0.0')
_enable_optimisations = not __debug__
if getattr(sys, 'frozen', None):
    _enable_optimisations = True
options = {'audio': ('directsound', 'pulse', 'openal', 'silent'), 
   'font': ('gdiplus', 'win32'), 
   'debug_font': False, 
   'debug_gl': not _enable_optimisations, 
   'debug_gl_trace': False, 
   'debug_gl_trace_args': False, 
   'debug_graphics_batch': False, 
   'debug_lib': False, 
   'debug_media': False, 
   'debug_texture': False, 
   'debug_trace': False, 
   'debug_trace_args': False, 
   'debug_trace_depth': 1, 
   'debug_trace_flush': True, 
   'debug_win32': False, 
   'debug_x11': False, 
   'graphics_vbo': False, 
   'shadow_window': True, 
   'vsync': None, 
   'xsync': True, 
   'xlib_fullscreen_override_redirect': False, 
   'darwin_cocoa': False}
_option_types = {'audio': tuple, 
   'font': tuple, 
   'debug_font': bool, 
   'debug_gl': bool, 
   'debug_gl_trace': bool, 
   'debug_gl_trace_args': bool, 
   'debug_graphics_batch': bool, 
   'debug_lib': bool, 
   'debug_media': bool, 
   'debug_texture': bool, 
   'debug_trace': bool, 
   'debug_trace_args': bool, 
   'debug_trace_depth': int, 
   'debug_trace_flush': bool, 
   'debug_win32': bool, 
   'debug_x11': bool, 
   'graphics_vbo': bool, 
   'shadow_window': bool, 
   'vsync': bool, 
   'xsync': bool, 
   'xlib_fullscreen_override_redirect': bool, 
   'darwin_cocoa': bool}

def _choose_darwin_platform():
    if sys.platform != 'darwin':
        return
    else:
        options['darwin_cocoa'] = False
        return

    is_64bits = sys.maxint > 4294967296
    import platform
    osx_version = platform.mac_ver()[0]
    from objc import __version__ as pyobjc_version
    if is_64bits:
        if osx_version < '10.6':
            raise Exception('pyglet is not compatible with 64-bit Python for versions of Mac OS X prior to 10.6.')
        if pyobjc_version < '2.2':
            raise Exception('pyglet is not compatible with 64-bit Python for versions of PyObjC prior to 2.2')
        options['darwin_cocoa'] = True
    else:
        options['darwin_cocoa'] = False


_choose_darwin_platform()

def _read_environment():
    for key in options:
        env = 'PYGLET_%s' % key.upper()
        try:
            value = os.environ[env]
            if _option_types[key] is tuple:
                options[key] = value.split(',')
            elif _option_types[key] is bool:
                options[key] = value in ('true', 'TRUE', 'True', '1')
            elif _option_types[key] is int:
                options[key] = int(value)
        except KeyError:
            pass


_read_environment()
if sys.platform == 'cygwin':
    import ctypes
    ctypes.windll = ctypes.cdll
    ctypes.oledll = ctypes.cdll
    ctypes.WINFUNCTYPE = ctypes.CFUNCTYPE
    ctypes.HRESULT = ctypes.c_long
_trace_filename_abbreviations = {}

def _trace_repr(value, size=40):
    value = repr(value)
    if len(value) > size:
        value = value[:size // 2 - 2] + '...' + value[-size // 2 - 1:]
    return value


def _trace_frame(thread, frame, indent):
    from pyglet import lib
    if frame.f_code is lib._TraceFunction.__call__.func_code:
        is_ctypes = True
        func = frame.f_locals['self']._func
        name = func.__name__
        location = '[ctypes]'
    else:
        is_ctypes = False
        code = frame.f_code
        name = code.co_name
        path = code.co_filename
        line = code.co_firstlineno
        try:
            filename = _trace_filename_abbreviations[path]
        except KeyError:
            dir = ''
            path, filename = os.path.split(path)
            while len(dir + filename) < 30:
                filename = os.path.join(dir, filename)
                path, dir = os.path.split(path)
                if not dir:
                    filename = os.path.join('', filename)
                    break
            else:
                filename = os.path.join('...', filename)

            _trace_filename_abbreviations[path] = filename

        location = '(%s:%d)' % (filename, line)
    if indent:
        name = 'Called from %s' % name
    print '[%d] %s%s %s' % (thread, indent, name, location)
    if _trace_args:
        if is_ctypes:
            args = [ _trace_repr(arg) for arg in frame.f_locals['args'] ]
            print '  %sargs=(%s)' % (indent, (', ').join(args))
        else:
            for argname in code.co_varnames[:code.co_argcount]:
                try:
                    argvalue = _trace_repr(frame.f_locals[argname])
                    print '  %s%s=%s' % (indent, argname, argvalue)
                except:
                    pass

    if _trace_flush:
        sys.stdout.flush()


def _thread_trace_func(thread):

    def _trace_func(frame, event, arg):
        if event == 'call':
            indent = ''
            for i in range(_trace_depth):
                _trace_frame(thread, frame, indent)
                indent += '  '
                frame = frame.f_back
                if not frame:
                    break

        elif event == 'exception':
            exception, value, traceback = arg
            print 'First chance exception raised:', repr(exception)

    return _trace_func


def _install_trace():
    global _trace_thread_count
    sys.setprofile(_thread_trace_func(_trace_thread_count))
    _trace_thread_count += 1


_trace_thread_count = 0
_trace_args = options['debug_trace_args']
_trace_depth = options['debug_trace_depth']
_trace_flush = options['debug_trace_flush']
if options['debug_trace']:
    _install_trace()

class _ModuleProxy(object):
    _module = None

    def __init__(self, name):
        self.__dict__['_module_name'] = name

    def __getattr__(self, name):
        try:
            return getattr(self._module, name)
        except AttributeError:
            if self._module is not None:
                raise
            import_name = 'pyglet.%s' % self._module_name
            __import__(import_name)
            module = sys.modules[import_name]
            object.__setattr__(self, '_module', module)
            globals()[self._module_name] = module
            return getattr(module, name)

        return

    def __setattr__(self, name, value):
        try:
            setattr(self._module, name, value)
        except AttributeError:
            if self._module is not None:
                raise
            import_name = 'pyglet.%s' % self._module_name
            __import__(import_name)
            module = sys.modules[import_name]
            object.__setattr__(self, '_module', module)
            globals()[self._module_name] = module
            setattr(module, name, value)

        return


if not _is_epydoc:
    app = _ModuleProxy('app')
    canvas = _ModuleProxy('canvas')
    clock = _ModuleProxy('clock')
    com = _ModuleProxy('com')
    event = _ModuleProxy('event')
    font = _ModuleProxy('font')
    gl = _ModuleProxy('gl')
    graphics = _ModuleProxy('graphics')
    image = _ModuleProxy('image')
    input = _ModuleProxy('input')
    lib = _ModuleProxy('lib')
    media = _ModuleProxy('media')
    resource = _ModuleProxy('resource')
    sprite = _ModuleProxy('sprite')
    text = _ModuleProxy('text')
    window = _ModuleProxy('window')
if False:
    import app, canvas, clock, com, event, font, gl, graphics, input, image, lib, media, resource, sprite, text, window
if _is_epydoc:
    import window
# okay decompiling out\pyglet.pyc
