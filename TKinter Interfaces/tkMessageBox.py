# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\tkMessageBox
from tkCommonDialog import Dialog
ERROR = 'error'
INFO = 'info'
QUESTION = 'question'
WARNING = 'warning'
ABORTRETRYIGNORE = 'abortretryignore'
OK = 'ok'
OKCANCEL = 'okcancel'
RETRYCANCEL = 'retrycancel'
YESNO = 'yesno'
YESNOCANCEL = 'yesnocancel'
ABORT = 'abort'
RETRY = 'retry'
IGNORE = 'ignore'
OK = 'ok'
CANCEL = 'cancel'
YES = 'yes'
NO = 'no'

class Message(Dialog):
    command = 'tk_messageBox'


def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and 'icon' not in options:
        options['icon'] = _icon
    if _type and 'type' not in options:
        options['type'] = _type
    if title:
        options['title'] = title
    if message:
        options['message'] = message
    res = Message(**options).show()
    if isinstance(res, bool):
        if res:
            return YES
        return NO
    return str(res)


def showinfo(title=None, message=None, **options):
    return _show(title, message, INFO, OK, **options)


def showwarning(title=None, message=None, **options):
    return _show(title, message, WARNING, OK, **options)


def showerror(title=None, message=None, **options):
    return _show(title, message, ERROR, OK, **options)


def askquestion(title=None, message=None, **options):
    return _show(title, message, QUESTION, YESNO, **options)


def askokcancel(title=None, message=None, **options):
    s = _show(title, message, QUESTION, OKCANCEL, **options)
    return s == OK


def askyesno(title=None, message=None, **options):
    s = _show(title, message, QUESTION, YESNO, **options)
    return s == YES


def askyesnocancel(title=None, message=None, **options):
    s = _show(title, message, QUESTION, YESNOCANCEL, **options)
    s = str(s)
    if s == CANCEL:
        return None
    else:
        return s == YES


def askretrycancel(title=None, message=None, **options):
    s = _show(title, message, WARNING, RETRYCANCEL, **options)
    return s == RETRY


if __name__ == '__main__':
    print 'info', showinfo('Spam', 'Egg Information')
    print 'warning', showwarning('Spam', 'Egg Warning')
    print 'error', showerror('Spam', 'Egg Alert')
    print 'question', askquestion('Spam', 'Question?')
    print 'proceed', askokcancel('Spam', 'Proceed?')
    print 'yes/no', askyesno('Spam', 'Got it?')
    print 'yes/no/cancel', askyesnocancel('Spam', 'Want it?')
    print 'try again', askretrycancel('Spam', 'Try again?')
# okay decompiling out\tkMessageBox.pyc
