# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\os2emxpath
import os, stat
from genericpath import *
from genericpath import _unicode
from ntpath import expanduser, expandvars, isabs, islink, splitdrive, splitext, split, walk
__all__ = [
 'normcase', 'isabs', 'join', 'splitdrive', 'split', 'splitext', 
 'basename', 
 'dirname', 'commonprefix', 'getsize', 'getmtime', 
 'getatime', 'getctime', 
 'islink', 'exists', 'lexists', 'isdir', 'isfile', 
 'ismount', 'walk', 
 'expanduser', 'expandvars', 'normpath', 'abspath', 
 'splitunc', 'curdir', 
 'pardir', 'sep', 'pathsep', 'defpath', 'altsep', 
 'extsep', 'devnull', 
 'realpath', 'supports_unicode_filenames']
curdir = '.'
pardir = '..'
extsep = '.'
sep = '/'
altsep = '\\'
pathsep = ';'
defpath = '.;C:\\bin'
devnull = 'nul'

def normcase(s):
    return s.replace('\\', '/').lower()


def join(a, *p):
    path = a
    for b in p:
        if isabs(b):
            path = b
        elif path == '' or path[-1:] in '/\\:':
            path = path + b
        else:
            path = path + '/' + b

    return path


def splitunc(p):
    if p[1:2] == ':':
        return ('', p)
    firstTwo = p[0:2]
    if firstTwo == '//' or firstTwo == '\\\\':
        normp = normcase(p)
        index = normp.find('/', 2)
        if index == -1:
            return (
             '', p)
        index = normp.find('/', index + 1)
        if index == -1:
            index = len(p)
        return (p[:index], p[index:])
    return (
     '', p)


def basename(p):
    return split(p)[1]


def dirname(p):
    return split(p)[0]


lexists = exists

def ismount(path):
    unc, rest = splitunc(path)
    if unc:
        return rest in ('', '/', '\\')
    p = splitdrive(path)[1]
    return len(p) == 1 and p[0] in '/\\'


def normpath(path):
    path = path.replace('\\', '/')
    prefix, path = splitdrive(path)
    while path[:1] == '/':
        prefix = prefix + '/'
        path = path[1:]

    comps = path.split('/')
    i = 0
    while i < len(comps):
        if comps[i] == '.':
            del comps[i]
        elif comps[i] == '..' and i > 0 and comps[i - 1] not in ('', '..'):
            del comps[i - 1:i + 1]
            i = i - 1
        elif comps[i] == '' and i > 0 and comps[i - 1] != '':
            del comps[i]
        else:
            i = i + 1

    if not prefix and not comps:
        comps.append('.')
    return prefix + ('/').join(comps)


def abspath(path):
    if not isabs(path):
        if isinstance(path, _unicode):
            cwd = os.getcwdu()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


realpath = abspath
supports_unicode_filenames = False
# okay decompiling out\os2emxpath.pyc
