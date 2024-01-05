# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.app
__docformat__ = 'restructuredtext'
__version__ = '$Id$'
import sys, weakref
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

class AppException(Exception):
    pass


class WeakSet(object):

    def __init__(self):
        self._dict = weakref.WeakKeyDictionary()

    def add(self, value):
        self._dict[value] = True

    def remove(self, value):
        del self._dict[value]

    def __iter__(self):
        for key in self._dict.keys():
            yield key

    def __contains__(self, other):
        return other in self._dict

    def __len__(self):
        return len(self._dict)


displays = WeakSet()
windows = WeakSet()

def run():
    event_loop.run()


def exit():
    event_loop.exit()


from pyglet.app.base import EventLoop
if _is_epydoc:
    from pyglet.app.base import PlatformEventLoop
elif sys.platform == 'darwin':
    from pyglet import options as pyglet_options
    if pyglet_options['darwin_cocoa']:
        from pyglet.app.cocoa import CocoaEventLoop as PlatformEventLoop
    else:
        from pyglet.app.carbon import CarbonEventLoop as PlatformEventLoop
elif sys.platform in ('win32', 'cygwin'):
    from pyglet.app.win32 import Win32EventLoop as PlatformEventLoop
else:
    from pyglet.app.xlib import XlibEventLoop as PlatformEventLoop
event_loop = EventLoop()
platform_event_loop = PlatformEventLoop()
# okay decompiling out\pyglet.app.pyc
