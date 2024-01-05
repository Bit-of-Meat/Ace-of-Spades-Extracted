# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.window.cocoa
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
from ..ctypes import *
import unicodedata, pyglet
from pyglet.window import BaseWindow, WindowException
from pyglet.window import MouseCursor, DefaultMouseCursor
from pyglet.window import key, mouse
from pyglet.event import EventDispatcher
from pyglet.canvas.cocoa import CocoaCanvas
from ..pyglet.libs.darwin import *
from pyglet.libs.darwin.quartzkey import keymap, charmap

class SystemCursor():
    cursor_is_hidden = False

    @classmethod
    def hide(cls):
        if not cls.cursor_is_hidden:
            NSCursor.hide()
            cls.cursor_is_hidden = True

    @classmethod
    def unhide(cls):
        if cls.cursor_is_hidden:
            NSCursor.unhide()
            cls.cursor_is_hidden = False


class CocoaMouseCursor(MouseCursor):
    drawable = False

    def __init__(self, constructor):
        self.constructor = constructor

    def set(self):
        self.constructor().set()


class PygletDelegate(NSObject):
    _window = None

    def initWithWindow_(self, window):
        self = super(PygletDelegate, self).init()
        if self is not None:
            self._window = window
            window._nswindow.setDelegate_(self)
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self, 'applicationDidHide:', NSApplicationDidHideNotification, None)
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self, 'applicationDidUnhide:', NSApplicationDidUnhideNotification, None)
        self.did_pause_exclusive_mouse = False
        return self

    def dealloc(self):
        NSNotificationCenter.defaultCenter().removeObserver_(self)
        super(PygletDelegate, self).dealloc()

    def applicationDidHide_(self, notification):
        self._window.dispatch_event('on_hide')

    def applicationDidUnhide_(self, notification):
        if self._window._is_mouse_exclusive and CGCursorIsVisible():
            SystemCursor.unhide()
            SystemCursor.hide()
        self._window.dispatch_event('on_show')

    def windowShouldClose_(self, notification):
        self._window.dispatch_event('on_close')
        return False

    def windowDidMove_(self, notification):
        x, y = self._window.get_location()
        self._window.dispatch_event('on_move', x, y)

    def windowDidResize_(self, notification):
        pass

    def windowDidBecomeKey_(self, notification):
        if self.did_pause_exclusive_mouse:
            self._window.set_exclusive_mouse(True)
            self.did_pause_exclusive_mouse = False
            self._window._nswindow.setMovable_(True)
        self._window.set_mouse_platform_visible()
        self._window.dispatch_event('on_activate')

    def windowDidResignKey_(self, notification):
        if self._window._is_mouse_exclusive:
            self._window.set_exclusive_mouse(False)
            self.did_pause_exclusive_mouse = True
            self._window._nswindow.setMovable_(False)
        self._window.set_mouse_platform_visible(True)
        self._window.dispatch_event('on_deactivate')

    def windowDidMiniaturize_(self, notification):
        self._window.dispatch_event('on_hide')

    def windowDidDeminiaturize_(self, notification):
        if self._window._is_mouse_exclusive and CGCursorIsVisible():
            SystemCursor.unhide()
            SystemCursor.hide()
        self._window.dispatch_event('on_show')

    def windowDidExpose_(self, notification):
        self._window.dispatch_event('on_expose')

    def terminate_(self, sender):
        NSApp().terminate_(self)

    def validateMenuItem_(self, menuitem):
        if menuitem.action() == 'terminate:':
            return not self._window._is_keyboard_exclusive
        return True


class PygletTextView(NSTextView):

    def keyDown_(self, nsevent):
        self.interpretKeyEvents_([nsevent])

    def initWithCocoaWindow_(self, window):
        self = super(PygletTextView, self).init()
        if self is not None:
            self._window = window
            self.setFieldEditor_(False)
        return self

    def insertText_(self, text):
        self.setString_('')
        if unicodedata.category(text[0]) != 'Cc':
            self._window.dispatch_event('on_text', text)

    def insertNewline_(self, sender):
        if NSApp().currentEvent().charactersIgnoringModifiers()[0] == '\r':
            self._window.dispatch_event('on_text', '\r')

    def moveUp_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_UP)

    def moveDown_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_DOWN)

    def moveLeft_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_LEFT)

    def moveRight_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_RIGHT)

    def moveWordLeft_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_PREVIOUS_WORD)

    def moveWordRight_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_NEXT_WORD)

    def moveToBeginningOfLine_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_BEGINNING_OF_LINE)

    def moveToEndOfLine_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_END_OF_LINE)

    def scrollPageUp_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_PREVIOUS_PAGE)

    def scrollPageDown_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_NEXT_PAGE)

    def scrollToBeginningOfDocument_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_BEGINNING_OF_FILE)

    def scrollToEndOfDocument_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_END_OF_FILE)

    def deleteBackward_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_BACKSPACE)

    def deleteForward_(self, sender):
        self._window.dispatch_event('on_text_motion', key.MOTION_DELETE)

    def moveUpAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_UP)

    def moveDownAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_DOWN)

    def moveLeftAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_LEFT)

    def moveRightAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_RIGHT)

    def moveWordLeftAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_PREVIOUS_WORD)

    def moveWordRightAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_NEXT_WORD)

    def moveToBeginningOfLineAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_BEGINNING_OF_LINE)

    def moveToEndOfLineAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_END_OF_LINE)

    def pageUpAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_PREVIOUS_PAGE)

    def pageDownAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_NEXT_PAGE)

    def moveToBeginningOfDocumentAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_BEGINNING_OF_FILE)

    def moveToEndOfDocumentAndModifySelection_(self, sender):
        self._window.dispatch_event('on_text_motion_select', key.MOTION_END_OF_FILE)


class PygletWindow(NSWindow):

    def canBecomeKeyWindow(self):
        return True

    def nextEventMatchingMask_untilDate_inMode_dequeue_(self, mask, date, mode, dequeue):
        if self.inLiveResize():
            from pyglet import app
            if app.event_loop is not None:
                app.event_loop.idle()
        return super(PygletWindow, self).nextEventMatchingMask_untilDate_inMode_dequeue_(mask, date, mode, dequeue)

    def animationResizeTime_(self, newFrame):
        return 0.0


class PygletToolWindow(NSPanel):

    def nextEventMatchingMask_untilDate_inMode_dequeue_(self, mask, date, mode, dequeue):
        if self.inLiveResize():
            from pyglet import app
            if app.event_loop is not None:
                app.event_loop.idle()
        return super(PygletToolWindow, self).nextEventMatchingMask_untilDate_inMode_dequeue_(mask, date, mode, dequeue)


class PygletView(NSView):
    _window = None
    _tracking_area = None

    def initWithFrame_cocoaWindow_(self, frame, window):
        self = super(PygletView, self).initWithFrame_(frame)
        if self is not None:
            self._window = window
            self.updateTrackingAreas()
        self._textview = PygletTextView.alloc().initWithCocoaWindow_(window)
        self.addSubview_(self._textview)
        return self

    def updateTrackingAreas(self):
        if self._tracking_area:
            self.removeTrackingArea_(self._tracking_area)
            del self._tracking_area
        tracking_options = NSTrackingMouseEnteredAndExited | NSTrackingActiveInActiveApp | NSTrackingCursorUpdate
        self._tracking_area = NSTrackingArea.alloc().initWithRect_options_owner_userInfo_(self.frame(), tracking_options, self, None)
        self.addTrackingArea_(self._tracking_area)
        return

    def canBecomeKeyView(self):
        return True

    def isOpaque(self):
        return True

    def destroy(self):
        if self._tracking_area:
            self.removeTrackingArea_(self._tracking_area)
            self._tracking_area = None
        self._textview._window = None
        self._textview.removeFromSuperviewWithoutNeedingDisplay()
        self._textview = None
        self._window = None
        self.removeFromSuperviewWithoutNeedingDisplay()
        return

    def getMouseDelta_(self, nsevent):
        dx = nsevent.deltaX()
        dy = -nsevent.deltaY()
        return (int(dx), int(dy))

    def getMousePosition_(self, nsevent):
        in_window = nsevent.locationInWindow()
        x, y = map(int, self.convertPoint_fromView_(in_window, None))
        self._window._mouse_x = x
        self._window._mouse_y = y
        return (x, y)

    def getModifiers_(self, nsevent):
        modifiers = 0
        modifierFlags = nsevent.modifierFlags()
        if modifierFlags & NSAlphaShiftKeyMask:
            modifiers |= key.MOD_CAPSLOCK
        if modifierFlags & NSShiftKeyMask:
            modifiers |= key.MOD_SHIFT
        if modifierFlags & NSControlKeyMask:
            modifiers |= key.MOD_CTRL
        if modifierFlags & NSAlternateKeyMask:
            modifiers |= key.MOD_ALT
            modifiers |= key.MOD_OPTION
        if modifierFlags & NSCommandKeyMask:
            modifiers |= key.MOD_COMMAND
        return modifiers

    def getSymbol_(self, nsevent):
        return keymap[nsevent.keyCode()]

    def setFrameSize_(self, size):
        super(PygletView, self).setFrameSize_(size)
        if not self._window.context.canvas:
            return
        else:
            width, height = map(int, size)
            self._window.switch_to()
            self._window.context.update_geometry()
            self._window.dispatch_event('on_resize', width, height)
            self._window.dispatch_event('on_expose')
            if self.inLiveResize():
                from pyglet import app
                if app.event_loop is not None:
                    app.event_loop.idle()
            return

    def pygletKeyDown_(self, nsevent):
        symbol = self.getSymbol_(nsevent)
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_key_press', symbol, modifiers)

    def pygletKeyUp_(self, nsevent):
        symbol = self.getSymbol_(nsevent)
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_key_release', symbol, modifiers)

    def pygletFlagsChanged_(self, nsevent):
        NSLeftShiftKeyMask = 2
        NSRightShiftKeyMask = 4
        NSLeftControlKeyMask = 1
        NSRightControlKeyMask = 8192
        NSLeftAlternateKeyMask = 32
        NSRightAlternateKeyMask = 64
        NSLeftCommandKeyMask = 8
        NSRightCommandKeyMask = 16
        maskForKey = {key.LSHIFT: NSLeftShiftKeyMask, key.RSHIFT: NSRightShiftKeyMask, 
           key.LCTRL: NSLeftControlKeyMask, 
           key.RCTRL: NSRightControlKeyMask, 
           key.LOPTION: NSLeftAlternateKeyMask, 
           key.ROPTION: NSRightAlternateKeyMask, 
           key.LCOMMAND: NSLeftCommandKeyMask, 
           key.RCOMMAND: NSRightCommandKeyMask, 
           key.CAPSLOCK: NSAlphaShiftKeyMask}
        symbol = self.getSymbol_(nsevent)
        if symbol not in maskForKey:
            return
        modifiers = self.getModifiers_(nsevent)
        modifierFlags = nsevent.modifierFlags()
        if symbol and modifierFlags & maskForKey[symbol]:
            self._window.dispatch_event('on_key_press', symbol, modifiers)
        else:
            self._window.dispatch_event('on_key_release', symbol, modifiers)

    def performKeyEquivalent_(self, nsevent):
        modifierFlags = nsevent.modifierFlags()
        if modifierFlags & NSNumericPadKeyMask:
            return False
        if modifierFlags & NSFunctionKeyMask:
            ch = nsevent.charactersIgnoringModifiers()
            if ch in (NSHomeFunctionKey, NSEndFunctionKey,
             NSPageUpFunctionKey, NSPageDownFunctionKey):
                return False
        NSApp().mainMenu().performKeyEquivalent_(nsevent)
        return True

    def mouseMoved_(self, nsevent):
        if self._window._mouse_ignore_motion:
            self._window._mouse_ignore_motion = False
            return
        if not self._window._mouse_in_window:
            return
        x, y = self.getMousePosition_(nsevent)
        dx, dy = self.getMouseDelta_(nsevent)
        self._window.dispatch_event('on_mouse_motion', x, y, dx, dy)

    def scrollWheel_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        scroll_x, scroll_y = self.getMouseDelta_(nsevent)
        self._window.dispatch_event('on_mouse_scroll', x, y, scroll_x, -scroll_y)

    def mouseDown_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        buttons = mouse.LEFT
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_press', x, y, buttons, modifiers)

    def mouseDragged_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        dx, dy = self.getMouseDelta_(nsevent)
        buttons = mouse.LEFT
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_drag', x, y, dx, dy, buttons, modifiers)

    def mouseUp_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        buttons = mouse.LEFT
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_release', x, y, buttons, modifiers)

    def rightMouseDown_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        buttons = mouse.RIGHT
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_press', x, y, buttons, modifiers)

    def rightMouseDragged_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        dx, dy = self.getMouseDelta_(nsevent)
        buttons = mouse.RIGHT
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_drag', x, y, dx, dy, buttons, modifiers)

    def rightMouseUp_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        buttons = mouse.RIGHT
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_release', x, y, buttons, modifiers)

    def otherMouseDown_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        buttons = mouse.MIDDLE
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_press', x, y, buttons, modifiers)

    def otherMouseDragged_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        dx, dy = self.getMouseDelta_(nsevent)
        buttons = mouse.MIDDLE
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_drag', x, y, dx, dy, buttons, modifiers)

    def otherMouseUp_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        buttons = mouse.MIDDLE
        modifiers = self.getModifiers_(nsevent)
        self._window.dispatch_event('on_mouse_release', x, y, buttons, modifiers)

    def mouseEntered_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        self._window._mouse_in_window = True
        self._window.dispatch_event('on_mouse_enter', x, y)

    def mouseExited_(self, nsevent):
        x, y = self.getMousePosition_(nsevent)
        self._window._mouse_in_window = False
        if not self._window._is_mouse_exclusive:
            self._window.set_mouse_platform_visible()
        self._window.dispatch_event('on_mouse_leave', x, y)

    def cursorUpdate_(self, nsevent):
        if not self._window._is_mouse_exclusive:
            self._window.set_mouse_platform_visible()


class CocoaWindow(BaseWindow):
    _nswindow = None
    _delegate = None
    _minimum_size = None
    _maximum_size = None
    _is_mouse_exclusive = False
    _mouse_platform_visible = True
    _mouse_ignore_motion = False
    _is_keyboard_exclusive = False
    _was_closed = False
    _style_masks = {BaseWindow.WINDOW_STYLE_DEFAULT: NSTitledWindowMask | NSClosableWindowMask | NSMiniaturizableWindowMask, 
       BaseWindow.WINDOW_STYLE_DIALOG: NSTitledWindowMask | NSClosableWindowMask, 
       BaseWindow.WINDOW_STYLE_TOOL: NSTitledWindowMask | NSClosableWindowMask | NSUtilityWindowMask, 
       BaseWindow.WINDOW_STYLE_BORDERLESS: NSBorderlessWindowMask}

    def _recreate(self, changes):
        if 'context' in changes:
            self.context.set_current()
        if 'fullscreen' in changes:
            if not self._fullscreen:
                self.screen.release_display()
        self._create()

    def _create(self):
        pool = NSAutoreleasePool.alloc().init()
        if self._nswindow:
            self.canvas = None
            self._nswindow.orderOut_(None)
            self._nswindow.close()
            self.context.detach()
            self._nswindow = None
        content_rect = NSMakeRect(0, 0, self._width, self._height)
        WindowClass = PygletWindow
        if self._fullscreen:
            style_mask = NSBorderlessWindowMask
        else:
            if self._style not in self._style_masks:
                self._style = self.WINDOW_STYLE_DEFAULT
            style_mask = self._style_masks[self._style]
            if self._resizable:
                style_mask |= NSResizableWindowMask
            if self._style == BaseWindow.WINDOW_STYLE_TOOL:
                WindowClass = PygletToolWindow
        self._nswindow = WindowClass.alloc().initWithContentRect_styleMask_backing_defer_(content_rect, style_mask, NSBackingStoreBuffered, False)
        if self._fullscreen:
            self._nswindow.setBackgroundColor_(NSColor.blackColor())
            self._nswindow.setOpaque_(True)
            self.screen.capture_display()
            self._nswindow.setLevel_(CGShieldingWindowLevel())
            self.context.set_full_screen()
            self._center_fullscreen_window()
        else:
            self._set_nice_window_location()
        nsview = PygletView.alloc().initWithFrame_cocoaWindow_(content_rect, self)
        self._nswindow.setContentView_(nsview)
        self._nswindow.makeFirstResponder_(nsview)
        self.canvas = CocoaCanvas(self.display, self.screen, nsview)
        self.context.attach(self.canvas)
        self._nswindow.setAcceptsMouseMovedEvents_(True)
        self._nswindow.setReleasedWhenClosed_(False)
        self._nswindow.useOptimizedDrawing_(True)
        self._nswindow.setPreservesContentDuringLiveResize_(False)
        self._delegate = PygletDelegate.alloc().initWithWindow_(self)
        self.set_caption(self._caption)
        if self._minimum_size is not None:
            self.set_minimum_size(*self._minimum_size)
        if self._maximum_size is not None:
            self.set_maximum_size(*self._maximum_size)
        self.context.update_geometry()
        self.switch_to()
        self.set_vsync(self._vsync)
        self.set_visible(self._visible)
        del pool
        return

    def _set_nice_window_location(self):
        visible_windows = [ win for win in pyglet.app.windows if win is not self and win._nswindow and win._nswindow.isVisible()
                          ]
        if not visible_windows:
            self._nswindow.center()
        else:
            point = visible_windows[-1]._nswindow.cascadeTopLeftFromPoint_(NSZeroPoint)
            self._nswindow.cascadeTopLeftFromPoint_(point)

    def _center_fullscreen_window(self):
        x = int((self.screen.width - self._width) / 2)
        y = int((self.screen.height - self._height) / 2)
        self._nswindow.setFrameOrigin_((x, y))

    def close(self):
        if self._was_closed:
            return
        else:
            pool = NSAutoreleasePool.alloc().init()
            self.set_mouse_platform_visible(True)
            self.set_exclusive_mouse(False)
            self.set_exclusive_keyboard(False)
            if self._delegate:
                self._nswindow.setDelegate_(None)
                self._delegate._window = None
                self._delegate = None
            if self._nswindow:
                self._nswindow.orderOut_(None)
                self._nswindow.setContentView_(None)
                self._nswindow.close()
            self.screen.restore_mode()
            if self.canvas:
                self.canvas.nsview.destroy()
                self.canvas.nsview = None
                self.canvas = None
            super(CocoaWindow, self).close()
            self._was_closed = True
            del pool
            return

    def switch_to(self):
        if self.context:
            self.context.set_current()

    def flip(self):
        self.draw_mouse_cursor()
        if self.context:
            self.context.flip()

    def dispatch_events(self):
        self._allow_dispatch_event = True
        self.dispatch_pending_events()
        event = True
        pool = NSAutoreleasePool.alloc().init()
        while event and self._nswindow and self._context:
            event = NSApp().nextEventMatchingMask_untilDate_inMode_dequeue_(NSAnyEventMask, None, NSEventTrackingRunLoopMode, True)
            if event is not None:
                event_type = event.type()
                NSApp().sendEvent_(event)
                if event_type == NSKeyDown and not event.isARepeat():
                    NSApp().sendAction_to_from_('pygletKeyDown:', None, event)
                elif event_type == NSKeyUp:
                    NSApp().sendAction_to_from_('pygletKeyUp:', None, event)
                elif event_type == NSFlagsChanged:
                    NSApp().sendAction_to_from_('pygletFlagsChanged:', None, event)
                NSApp().updateWindows()

        del pool
        self._allow_dispatch_event = False
        return

    def dispatch_pending_events(self):
        while self._event_queue:
            event = self._event_queue.pop(0)
            EventDispatcher.dispatch_event(self, *event)

    def set_caption(self, caption):
        self._caption = caption
        if self._nswindow is not None:
            self._nswindow.setTitle_(caption)
        return

    def set_icon(self, *images):
        max_image = images[0]
        for img in images:
            if img.width > max_image.width and img.height > max_image.height:
                max_image = img

        image = max_image.get_image_data()
        format = 'ARGB'
        bytesPerRow = len(format) * image.width
        data = image.get_data(format, -bytesPerRow)
        cfdata = CoreFoundation.CFDataCreate(None, data, len(data))
        provider = CGDataProviderCreateWithCFData(cfdata)
        cgimage = CGImageCreate(image.width, image.height, 8, 32, bytesPerRow, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaFirst, provider, None, True, kCGRenderingIntentDefault)
        if not cgimage:
            return
        else:
            size = NSMakeSize(image.width, image.height)
            nsimage = NSImage.alloc().initWithCGImage_size_(cgimage, size)
            if not nsimage:
                return
            NSApp().setApplicationIconImage_(nsimage)
            return

    def get_location(self):
        rect = self._nswindow.contentRectForFrameRect_(self._nswindow.frame())
        screen_width, screen_height = self._nswindow.screen().frame().size
        return (int(rect.origin.x), int(screen_height - rect.origin.y - rect.size.height))

    def set_location(self, x, y):
        rect = self._nswindow.contentRectForFrameRect_(self._nswindow.frame())
        screen_width, screen_height = self._nswindow.screen().frame().size
        self._nswindow.setFrameOrigin_(NSPoint(x, screen_height - y - rect.size.height))

    def get_size(self):
        rect = self._nswindow.contentRectForFrameRect_(self._nswindow.frame())
        return (int(rect.size.width), int(rect.size.height))

    def set_size(self, width, height):
        if self._fullscreen:
            raise WindowException('Cannot set size of fullscreen window.')
        self._width = max(1, int(width))
        self._height = max(1, int(height))
        rect = self._nswindow.contentRectForFrameRect_(self._nswindow.frame())
        rect.origin.y += rect.size.height - self._height
        rect.size.width = self._width
        rect.size.height = self._height
        frame = self._nswindow.frameRectForContentRect_(rect)
        self._nswindow.setFrame_display_animate_(frame, True, self._nswindow.isVisible())

    def set_minimum_size(self, width, height):
        self._minimum_size = NSSize(width, height)
        if self._nswindow is not None:
            self._nswindow.setContentMinSize_(self._minimum_size)
        return

    def set_maximum_size(self, width, height):
        self._maximum_size = NSSize(width, height)
        if self._nswindow is not None:
            self._nswindow.setContentMaxSize_(self._maximum_size)
        return

    def activate(self):
        if self._nswindow is not None:
            NSApp().activateIgnoringOtherApps_(True)
            self._nswindow.makeKeyAndOrderFront_(None)
        return

    def set_visible(self, visible=True):
        self._visible = visible
        if self._nswindow is not None:
            if visible:
                self.dispatch_event('on_resize', self._width, self._height)
                self.dispatch_event('on_show')
                self.dispatch_event('on_expose')
                self._nswindow.makeKeyAndOrderFront_(None)
            else:
                self._nswindow.orderOut_(None)
        return

    def minimize(self):
        self._mouse_in_window = False
        if self._nswindow is not None:
            self._nswindow.miniaturize_(None)
        return

    def maximize(self):
        if self._nswindow is not None:
            self._nswindow.zoom_(None)
        return

    def set_vsync(self, vsync):
        if pyglet.options['vsync'] is not None:
            vsync = pyglet.options['vsync']
        self._vsync = vsync
        if self.context:
            self.context.set_vsync(vsync)
        return

    def _mouse_in_content_rect(self):
        point = NSEvent.mouseLocation()
        rect = self._nswindow.contentRectForFrameRect_(self._nswindow.frame())
        return NSMouseInRect(point, rect, False)

    def set_mouse_platform_visible(self, platform_visible=None):
        if platform_visible is not None:
            if platform_visible:
                SystemCursor.unhide()
            else:
                SystemCursor.hide()
        elif self._is_mouse_exclusive:
            SystemCursor.hide()
        elif not self._mouse_in_content_rect():
            NSCursor.arrowCursor().set()
            SystemCursor.unhide()
        elif not self._mouse_visible:
            SystemCursor.hide()
        elif isinstance(self._mouse_cursor, CocoaMouseCursor):
            self._mouse_cursor.set()
            SystemCursor.unhide()
        elif self._mouse_cursor.drawable:
            SystemCursor.hide()
        else:
            NSCursor.arrowCursor().set()
            SystemCursor.unhide()
        return

    def get_system_mouse_cursor(self, name):
        if name == self.CURSOR_DEFAULT:
            return DefaultMouseCursor()
        cursors = {self.CURSOR_CROSSHAIR: NSCursor.crosshairCursor, self.CURSOR_HAND: NSCursor.pointingHandCursor, 
           self.CURSOR_HELP: NSCursor.arrowCursor, 
           self.CURSOR_NO: NSCursor.operationNotAllowedCursor, 
           self.CURSOR_SIZE: NSCursor.arrowCursor, 
           self.CURSOR_SIZE_UP: NSCursor.resizeUpCursor, 
           self.CURSOR_SIZE_UP_RIGHT: NSCursor.arrowCursor, 
           self.CURSOR_SIZE_RIGHT: NSCursor.resizeRightCursor, 
           self.CURSOR_SIZE_DOWN_RIGHT: NSCursor.arrowCursor, 
           self.CURSOR_SIZE_DOWN: NSCursor.resizeDownCursor, 
           self.CURSOR_SIZE_DOWN_LEFT: NSCursor.arrowCursor, 
           self.CURSOR_SIZE_LEFT: NSCursor.resizeLeftCursor, 
           self.CURSOR_SIZE_UP_LEFT: NSCursor.arrowCursor, 
           self.CURSOR_SIZE_UP_DOWN: NSCursor.resizeUpDownCursor, 
           self.CURSOR_SIZE_LEFT_RIGHT: NSCursor.resizeLeftRightCursor, 
           self.CURSOR_TEXT: NSCursor.IBeamCursor, 
           self.CURSOR_WAIT: NSCursor.arrowCursor, 
           self.CURSOR_WAIT_ARROW: NSCursor.arrowCursor}
        if name not in cursors:
            raise RuntimeError('Unknown cursor name "%s"' % name)
        return CocoaMouseCursor(cursors[name])

    def set_mouse_position(self, x, y, absolute=False):
        if absolute:
            CGWarpMouseCursorPosition((x, y))
        else:
            screenInfo = self._nswindow.screen().deviceDescription()
            displayID = screenInfo.objectForKey_('NSScreenNumber')
            displayBounds = CGDisplayBounds(displayID)
            windowOrigin = self._nswindow.frame().origin
            x += windowOrigin.x
            y = displayBounds.size.height - windowOrigin.y - y
            CGDisplayMoveCursorToPoint(displayID, (x, y))

    def set_exclusive_mouse(self, exclusive=True):
        self._is_mouse_exclusive = exclusive
        if exclusive:
            self._mouse_ignore_motion = True
            width, height = self._nswindow.frame().size
            self.set_mouse_position(width / 2, height / 2)
            CGAssociateMouseAndMouseCursorPosition(False)
        else:
            CGAssociateMouseAndMouseCursorPosition(True)
        self.set_mouse_platform_visible()

    def set_exclusive_keyboard(self, exclusive=True):
        NSApplicationPresentationDefault = 0
        NSApplicationPresentationHideDock = 2
        NSApplicationPresentationHideMenuBar = 8
        NSApplicationPresentationDisableProcessSwitching = 32
        NSApplicationPresentationDisableHideApplication = 256
        self._is_keyboard_exclusive = exclusive
        if exclusive:
            options = NSApplicationPresentationHideDock | NSApplicationPresentationHideMenuBar | NSApplicationPresentationDisableProcessSwitching | NSApplicationPresentationDisableHideApplication
        else:
            options = NSApplicationPresentationDefault
        NSApp().setPresentationOptions_(options)
# okay decompiling out\pyglet.window.cocoa.pyc
