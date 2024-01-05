# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.event
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import inspect
EVENT_HANDLED = True
EVENT_UNHANDLED = None

class EventException(Exception):
    pass


class EventDispatcher(object):
    _event_stack = ()

    @classmethod
    def register_event_type(cls, name):
        if not hasattr(cls, 'event_types'):
            cls.event_types = []
        cls.event_types.append(name)
        return name

    def push_handlers(self, *args, **kwargs):
        if type(self._event_stack) is tuple:
            self._event_stack = []
        self._event_stack.insert(0, {})
        self.set_handlers(*args, **kwargs)

    def _get_handlers(self, args, kwargs):
        for object in args:
            if inspect.isroutine(object):
                name = object.__name__
                if name not in self.event_types:
                    raise EventException('Unknown event "%s"' % name)
                yield (
                 name, object)
            else:
                for name in dir(object):
                    if name in self.event_types:
                        yield (
                         name, getattr(object, name))

        for name, handler in kwargs.items():
            if name not in self.event_types:
                raise EventException('Unknown event "%s"' % name)
            yield (
             name, handler)

    def set_handlers(self, *args, **kwargs):
        if type(self._event_stack) is tuple:
            self._event_stack = [{}]
        for name, handler in self._get_handlers(args, kwargs):
            self.set_handler(name, handler)

    def set_handler(self, name, handler):
        if type(self._event_stack) is tuple:
            self._event_stack = [{}]
        self._event_stack[0][name] = handler

    def pop_handlers(self):
        del self._event_stack[0]

    def remove_handlers(self, *args, **kwargs):
        handlers = list(self._get_handlers(args, kwargs))

        def find_frame():
            for frame in self._event_stack:
                for name, handler in handlers:
                    try:
                        if frame[name] == handler:
                            return frame
                    except KeyError:
                        pass

        frame = find_frame()
        if not frame:
            return
        for name, handler in handlers:
            try:
                if frame[name] == handler:
                    del frame[name]
            except KeyError:
                pass

        if not frame:
            self._event_stack.remove(frame)

    def remove_handler(self, name, handler):
        for frame in self._event_stack:
            try:
                if frame[name] is handler:
                    del frame[name]
                    break
            except KeyError:
                pass

    def dispatch_event(self, event_type, *args):
        invoked = False
        for frame in list(self._event_stack):
            handler = frame.get(event_type, None)
            if handler:
                try:
                    invoked = True
                    if handler(*args):
                        return EVENT_HANDLED
                except TypeError:
                    self._raise_dispatch_exception(event_type, args, handler)

        if hasattr(self, event_type):
            try:
                invoked = True
                if getattr(self, event_type)(*args):
                    return EVENT_HANDLED
            except TypeError:
                self._raise_dispatch_exception(event_type, args, getattr(self, event_type))

        if invoked:
            return EVENT_UNHANDLED
        else:
            return False

    def _raise_dispatch_exception(self, event_type, args, handler):
        n_args = len(args)
        handler_args, handler_varargs, _, handler_defaults = inspect.getargspec(handler)
        n_handler_args = len(handler_args)
        if inspect.ismethod(handler) and handler.im_self:
            n_handler_args -= 1
        if handler_varargs:
            n_handler_args = max(n_handler_args, n_args)
        if n_handler_args > n_args and handler_defaults and n_handler_args - len(handler_defaults) <= n_args:
            n_handler_args = n_args
        if n_handler_args != n_args:
            if inspect.isfunction(handler) or inspect.ismethod(handler):
                descr = '%s at %s:%d' % (
                 handler.func_name,
                 handler.func_code.co_filename,
                 handler.func_code.co_firstlineno)
            else:
                descr = repr(handler)
            raise TypeError('%s event was dispatched with %d arguments, but handler %s has an incompatible function signature' % (
             event_type, len(args), descr))
        else:
            raise

    def event(self, *args):
        if len(args) == 0:

            def decorator(func):
                name = func.__name__
                self.set_handler(name, func)
                return func

            return decorator
        if inspect.isroutine(args[0]):
            func = args[0]
            name = func.__name__
            self.set_handler(name, func)
            return args[0]
        if type(args[0]) in (str, unicode):
            name = args[0]

            def decorator(func):
                self.set_handler(name, func)
                return func

            return decorator
# okay decompiling out\pyglet.event.pyc
