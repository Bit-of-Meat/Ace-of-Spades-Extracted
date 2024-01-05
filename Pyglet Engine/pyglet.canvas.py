# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.canvas
import sys
_is_epydoc = hasattr(sys, 'is_epydoc') and sys.is_epydoc

def get_display():
    from pyglet.app import displays
    for display in displays:
        return display

    return Display()


if _is_epydoc:
    from pyglet.canvas.base import Display, Screen, Canvas
elif sys.platform == 'darwin':
    from pyglet import options as pyglet_options
    if pyglet_options['darwin_cocoa']:
        from pyglet.canvas.cocoa import CocoaDisplay as Display
        from pyglet.canvas.cocoa import CocoaScreen as Screen
        from pyglet.canvas.cocoa import CocoaCanvas as Canvas
    else:
        from pyglet.canvas.carbon import CarbonDisplay as Display
        from pyglet.canvas.carbon import CarbonScreen as Screen
        from pyglet.canvas.carbon import CarbonCanvas as Canvas
elif sys.platform in ('win32', 'cygwin'):
    from pyglet.canvas.win32 import Win32Display as Display
    from pyglet.canvas.win32 import Win32Screen as Screen
    from pyglet.canvas.win32 import Win32Canvas as Canvas
else:
    from pyglet.canvas.xlib import XlibDisplay as Display
    from pyglet.canvas.xlib import XlibScreen as Screen
    from pyglet.canvas.xlib import XlibCanvas as Canvas
# okay decompiling out\pyglet.canvas.pyc
