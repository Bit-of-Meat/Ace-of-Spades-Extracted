# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.app.cocoa
from __future__ import with_statement
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from pyglet.app.base import PlatformEventLoop
from pyglet.libs.darwin import *

class CocoaEventLoop(PlatformEventLoop):

    def __init__(self):
        super(CocoaEventLoop, self).__init__()
        NSApplication.sharedApplication()
        pool = NSAutoreleasePool.alloc().init()
        self._create_application_menu()
        NSApp().finishLaunching()
        NSApp().activateIgnoringOtherApps_(True)
        del pool

    def _create_application_menu(self):
        menubar = NSMenu.alloc().init()
        appMenuItem = NSMenuItem.alloc().init()
        menubar.addItem_(appMenuItem)
        NSApp().setMainMenu_(menubar)
        appMenu = NSMenu.alloc().init()
        processName = NSProcessInfo.processInfo().processName()
        hideItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Hide ' + processName, 'hide:', 'h')
        appMenu.addItem_(hideItem)
        appMenu.addItem_(NSMenuItem.separatorItem())
        quitItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit ' + processName, 'terminate:', 'q')
        appMenu.addItem_(quitItem)
        appMenuItem.setSubmenu_(appMenu)

    def start(self):
        pass

    def step(self, timeout=None):
        pool = NSAutoreleasePool.alloc().init()
        if timeout is None:
            timeout_date = NSDate.distantFuture()
        else:
            timeout_date = NSDate.dateWithTimeIntervalSinceNow_(timeout)
        self._is_running.set()
        event = NSApp().nextEventMatchingMask_untilDate_inMode_dequeue_(NSAnyEventMask, timeout_date, NSDefaultRunLoopMode, True)
        if event is not None:
            event_type = event.type()
            if event_type != NSApplicationDefined:
                NSApp().sendEvent_(event)
                if event_type == NSKeyDown and not event.isARepeat():
                    NSApp().sendAction_to_from_('pygletKeyDown:', None, event)
                else:
                    if event_type == NSKeyUp:
                        NSApp().sendAction_to_from_('pygletKeyUp:', None, event)
                    elif event_type == NSFlagsChanged:
                        NSApp().sendAction_to_from_('pygletFlagsChanged:', None, event)
            NSApp().updateWindows()
            did_time_out = False
        else:
            did_time_out = True
        self._is_running.clear()
        del pool
        return did_time_out

    def stop(self):
        pass

    def notify(self):
        pool = NSAutoreleasePool.alloc().init()
        notifyEvent = NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(NSApplicationDefined, NSPoint(0.0, 0.0), 0, 0, 0, None, 0, 0, 0)
        NSApp().postEvent_atStart_(notifyEvent, False)
        del pool
        return
# okay decompiling out\pyglet.app.cocoa.pyc
