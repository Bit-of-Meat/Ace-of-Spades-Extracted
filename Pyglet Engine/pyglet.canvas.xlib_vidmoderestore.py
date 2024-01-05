# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.canvas.xlib_vidmoderestore
import ctypes, os, signal, struct, threading
from pyglet.libs.x11 import xlib
from pyglet.compat import asbytes
try:
    from pyglet.libs.x11 import xf86vmode
except:
    pass

_restore_mode_child_installed = False
_restorable_screens = set()
_mode_write_pipe = None

class ModePacket(object):
    format = '256siHHI'
    size = struct.calcsize(format)

    def __init__(self, display, screen, width, height, rate):
        self.display = display
        self.screen = screen
        self.width = width
        self.height = height
        self.rate = rate

    def encode(self):
        return struct.pack(self.format, self.display, self.screen, self.width, self.height, self.rate)

    @classmethod
    def decode(cls, data):
        display, screen, width, height, rate = struct.unpack(cls.format, data)
        return cls(display.strip(asbytes('\x00')), screen, width, height, rate)

    def __repr__(self):
        return '%s(%r, %r, %r, %r, %r)' % (
         self.__class__.__name__, self.display, self.screen,
         self.width, self.height, self.rate)

    def set(self):
        display = xlib.XOpenDisplay(self.display)
        modes, n_modes = get_modes_array(display, self.screen)
        mode = get_matching_mode(modes, n_modes, self.width, self.height, self.rate)
        if mode is not None:
            xf86vmode.XF86VidModeSwitchToMode(display, self.screen, mode)
        free_modes_array(modes, n_modes)
        xlib.XCloseDisplay(display)
        return


def get_modes_array(display, screen):
    count = ctypes.c_int()
    modes = ctypes.POINTER(ctypes.POINTER(xf86vmode.XF86VidModeModeInfo))()
    xf86vmode.XF86VidModeGetAllModeLines(display, screen, count, modes)
    return (modes, count.value)


def get_matching_mode(modes, n_modes, width, height, rate):
    for i in range(n_modes):
        mode = modes.contents[i]
        if mode.hdisplay == width and mode.vdisplay == height and mode.dotclock == rate:
            return mode

    return


def free_modes_array(modes, n_modes):
    for i in range(n_modes):
        mode = modes.contents[i]
        if mode.privsize:
            xlib.XFree(mode.private)

    xlib.XFree(modes)


def _install_restore_mode_child():
    global _mode_write_pipe
    global _restore_mode_child_installed
    if _restore_mode_child_installed:
        return
    mode_read_pipe, _mode_write_pipe = os.pipe()
    if os.fork() == 0:
        os.close(_mode_write_pipe)
        PR_SET_PDEATHSIG = 1
        libc = ctypes.cdll.LoadLibrary('libc.so.6')
        libc.prctl.argtypes = (ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong,
         ctypes.c_ulong, ctypes.c_ulong)
        libc.prctl(PR_SET_PDEATHSIG, signal.SIGHUP, 0, 0, 0)

        def _sighup(signum, frame):
            parent_wait_lock.release()

        parent_wait_lock = threading.Lock()
        parent_wait_lock.acquire()
        signal.signal(signal.SIGHUP, _sighup)
        packets = []
        buffer = asbytes('')
        while parent_wait_lock.locked():
            try:
                data = os.read(mode_read_pipe, ModePacket.size)
                buffer += data
                while len(buffer) >= ModePacket.size:
                    packet = ModePacket.decode(buffer[:ModePacket.size])
                    packets.append(packet)
                    buffer = buffer[ModePacket.size:]

            except OSError:
                pass

        for packet in packets:
            packet.set()

        os._exit(0)
    else:
        os.close(mode_read_pipe)
        _restore_mode_child_installed = True


def set_initial_mode(mode):
    _install_restore_mode_child()
    display = xlib.XDisplayString(mode.screen.display._display)
    screen = mode.screen.display.x_screen
    if (
     display, screen) in _restorable_screens:
        return
    packet = ModePacket(display, screen, mode.width, mode.height, mode.rate)
    os.write(_mode_write_pipe, packet.encode())
    _restorable_screens.add((display, screen))
# okay decompiling out\pyglet.canvas.xlib_vidmoderestore.pyc
