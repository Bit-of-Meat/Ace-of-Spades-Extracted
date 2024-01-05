# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.util
from __future__ import division, absolute_import, print_function
import os, sys, errno, warnings
try:
    import pwd, grp
except ImportError:
    pwd = grp = None

try:
    from os import setgroups, getgroups
except ImportError:
    setgroups = getgroups = None

from twisted.python.compat import _PY3, unicode
if _PY3:
    UserDict = object
else:
    from UserDict import UserDict

class InsensitiveDict:

    def __init__(self, dict=None, preserve=1):
        self.data = {}
        self.preserve = preserve
        if dict:
            self.update(dict)

    def __delitem__(self, key):
        k = self._lowerOrReturn(key)
        del self.data[k]

    def _lowerOrReturn(self, key):
        if isinstance(key, bytes) or isinstance(key, unicode):
            return key.lower()
        else:
            return key

    def __getitem__(self, key):
        k = self._lowerOrReturn(key)
        return self.data[k][1]

    def __setitem__(self, key, value):
        k = self._lowerOrReturn(key)
        self.data[k] = (key, value)

    def has_key(self, key):
        k = self._lowerOrReturn(key)
        return k in self.data

    __contains__ = has_key

    def _doPreserve(self, key):
        if not self.preserve and (isinstance(key, bytes) or isinstance(key, unicode)):
            return key.lower()
        else:
            return key

    def keys(self):
        return list(self.iterkeys())

    def values(self):
        return list(self.itervalues())

    def items(self):
        return list(self.iteritems())

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def setdefault(self, key, default):
        if not self.has_key(key):
            self[key] = default
        return self[key]

    def update(self, dict):
        for k, v in dict.items():
            self[k] = v

    def __repr__(self):
        items = (', ').join([ '%r: %r' % (k, v) for k, v in self.items() ])
        return 'InsensitiveDict({%s})' % items

    def iterkeys(self):
        for v in self.data.values():
            yield self._doPreserve(v[0])

    def itervalues(self):
        for v in self.data.values():
            yield v[1]

    def iteritems(self):
        for k, v in self.data.values():
            yield (
             self._doPreserve(k), v)

    def popitem(self):
        i = self.items()[0]
        del self[i[0]]
        return i

    def clear(self):
        for k in self.keys():
            del self[k]

    def copy(self):
        return InsensitiveDict(self, self.preserve)

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        for k, v in self.items():
            if k not in other or not other[k] == v:
                return 0

        return len(self) == len(other)


class OrderedDict(UserDict):

    def __init__(self, dict=None, **kwargs):
        self._order = []
        self.data = {}
        if dict is not None:
            if hasattr(dict, 'keys'):
                self.update(dict)
            else:
                for k, v in dict:
                    self[k] = v

        if len(kwargs):
            self.update(kwargs)
        return

    def __repr__(self):
        return '{' + (', ').join([ '%r: %r' % item for item in self.items() ]) + '}'

    def __setitem__(self, key, value):
        if not self.has_key(key):
            self._order.append(key)
        UserDict.__setitem__(self, key, value)

    def copy(self):
        return self.__class__(self)

    def __delitem__(self, key):
        UserDict.__delitem__(self, key)
        self._order.remove(key)

    def iteritems(self):
        for item in self._order:
            yield (item, self[item])

    def items(self):
        return list(self.iteritems())

    def itervalues(self):
        for item in self._order:
            yield self[item]

    def values(self):
        return list(self.itervalues())

    def iterkeys(self):
        return iter(self._order)

    def keys(self):
        return list(self._order)

    def popitem(self):
        key = self._order[-1]
        value = self[key]
        del self[key]
        return (key, value)

    def setdefault(self, item, default):
        if self.has_key(item):
            return self[item]
        self[item] = default
        return default

    def update(self, d):
        for k, v in d.items():
            self[k] = v


if _PY3:
    del OrderedDict
    from collections import OrderedDict

def uniquify(lst):
    dct = {}
    result = []
    for k in lst:
        if k not in dct:
            result.append(k)
        dct[k] = 1

    return result


def padTo(n, seq, default=None):
    if len(seq) > n:
        raise ValueError('%d elements is more than %d.' % (len(seq), n))
    blank = [default] * n
    blank[:(len(seq))] = list(seq)
    return blank


def getPluginDirs():
    warnings.warn('twisted.python.util.getPluginDirs is deprecated since Twisted 12.2.', DeprecationWarning, stacklevel=2)
    import twisted
    systemPlugins = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(twisted.__file__))), 'plugins')
    userPlugins = os.path.expanduser('~/TwistedPlugins')
    confPlugins = os.path.expanduser('~/.twisted')
    allPlugins = filter(os.path.isdir, [systemPlugins, userPlugins, confPlugins])
    return allPlugins


def addPluginDir():
    warnings.warn('twisted.python.util.addPluginDir is deprecated since Twisted 12.2.', DeprecationWarning, stacklevel=2)
    sys.path.extend(getPluginDirs())


def sibpath(path, sibling):
    return os.path.join(os.path.dirname(os.path.abspath(path)), sibling)


def _getpass(prompt):
    import getpass
    try:
        return getpass.getpass(prompt)
    except IOError as e:
        if e.errno == errno.EINTR:
            raise KeyboardInterrupt
        raise
    except EOFError:
        raise KeyboardInterrupt


def getPassword(prompt='Password: ', confirm=0, forceTTY=0, confirmPrompt='Confirm password: ', mismatchMessage="Passwords don't match."):
    isaTTY = hasattr(sys.stdin, 'isatty') and sys.stdin.isatty()
    old = None
    try:
        if not isaTTY:
            if forceTTY:
                try:
                    old = (
                     sys.stdin, sys.stdout)
                    sys.stdin = sys.stdout = open('/dev/tty', 'r+')
                except:
                    raise RuntimeError('Cannot obtain a TTY')

            else:
                password = sys.stdin.readline()
                if password[-1] == '\n':
                    password = password[:-1]
                return password
        while 1:
            try1 = _getpass(prompt)
            if not confirm:
                return try1
            try2 = _getpass(confirmPrompt)
            if try1 == try2:
                return try1
            sys.stderr.write(mismatchMessage + '\n')

    finally:
        if old:
            sys.stdin.close()
            sys.stdin, sys.stdout = old

    return


def println(*a):
    sys.stdout.write((' ').join(map(str, a)) + '\n')


def str_xor(s, b):
    return ('').join([ chr(ord(c) ^ b) for c in s ])


def makeStatBar(width, maxPosition, doneChar='=', undoneChar='-', currentChar='>'):
    aValue = width / float(maxPosition)

    def statBar(position, force=0, last=['']):
        done = int(aValue * position)
        toDo = width - done - 2
        result = '[%s%s%s]' % (doneChar * done, currentChar, undoneChar * toDo)
        if force:
            last[0] = result
            return result
        if result == last[0]:
            return ''
        last[0] = result
        return result

    statBar.__doc__ = "statBar(position, force = 0) -> '[%s%s%s]'-style progress bar\n\n    returned string is %d characters long, and the range goes from 0..%d.\n    The 'position' argument is where the '%s' will be drawn.  If force is false,\n    '' will be returned instead if the resulting progress bar is identical to the\n    previously returned progress bar.\n" % (doneChar * 3, currentChar, undoneChar * 3, width, maxPosition, currentChar)
    return statBar


def spewer(frame, s, ignored):
    from twisted.python import reflect
    if 'self' in frame.f_locals:
        se = frame.f_locals['self']
        if hasattr(se, '__class__'):
            k = reflect.qual(se.__class__)
        else:
            k = reflect.qual(type(se))
        print('method %s of %s at %s' % (
         frame.f_code.co_name, k, id(se)))
    else:
        print('function %s in %s, line %s' % (
         frame.f_code.co_name,
         frame.f_code.co_filename,
         frame.f_lineno))


def searchupwards(start, files=[], dirs=[]):
    start = os.path.abspath(start)
    parents = start.split(os.sep)
    exists = os.path.exists
    join = os.sep.join
    isdir = os.path.isdir
    while len(parents):
        candidate = join(parents) + os.sep
        allpresent = 1
        for f in files:
            if not exists('%s%s' % (candidate, f)):
                allpresent = 0
                break

        if allpresent:
            for d in dirs:
                if not isdir('%s%s' % (candidate, d)):
                    allpresent = 0
                    break

        if allpresent:
            return candidate
        parents.pop(-1)

    return


class LineLog:

    def __init__(self, size=10):
        if size < 0:
            size = 0
        self.log = [
         None] * size
        self.size = size
        return

    def append(self, line):
        if self.size:
            self.log[:(-1)] = self.log[1:]
            self.log[-1] = line
        else:
            self.log.append(line)

    def str(self):
        return ('\n').join(filter(None, self.log))

    def __getitem__(self, item):
        return filter(None, self.log)[item]

    def clear(self):
        self.log = [
         None] * self.size
        return


def raises(exception, f, *args, **kwargs):
    try:
        f(*args, **kwargs)
    except exception:
        return 1

    return 0


class IntervalDifferential(object):

    def __init__(self, intervals, default=60):
        self.intervals = intervals[:]
        self.default = default

    def __iter__(self):
        return _IntervalDifferentialIterator(self.intervals, self.default)


class _IntervalDifferentialIterator(object):

    def __init__(self, i, d):
        self.intervals = [ [e, e, n] for e, n in zip(i, range(len(i))) ]
        self.default = d
        self.last = 0

    def __next__(self):
        if not self.intervals:
            return (self.default, None)
        else:
            last, index = self.intervals[0][0], self.intervals[0][2]
            self.intervals[0][0] += self.intervals[0][1]
            self.intervals.sort()
            result = last - self.last
            self.last = last
            return (result, index)

    next = __next__

    def addInterval(self, i):
        if self.intervals:
            delay = self.intervals[0][0] - self.intervals[0][1]
            self.intervals.append([delay + i, i, len(self.intervals)])
            self.intervals.sort()
        else:
            self.intervals.append([i, i, 0])

    def removeInterval(self, interval):
        for i in range(len(self.intervals)):
            if self.intervals[i][1] == interval:
                index = self.intervals[i][2]
                del self.intervals[i]
                for i in self.intervals:
                    if i[2] > index:
                        i[2] -= 1

                return

        raise ValueError('Specified interval not in IntervalDifferential')


class FancyStrMixin:
    showAttributes = ()

    def __str__(self):
        r = [
         '<',
         hasattr(self, 'fancybasename') and self.fancybasename or self.__class__.__name__]
        for attr in self.showAttributes:
            if isinstance(attr, str):
                r.append(' %s=%r' % (attr, getattr(self, attr)))
            elif len(attr) == 2:
                r.append(' %s=' % (attr[0],) + attr[1](getattr(self, attr[0])))
            else:
                r.append((' %s=' + attr[2]) % (attr[1], getattr(self, attr[0])))

        r.append('>')
        return ('').join(r)

    __repr__ = __str__


class FancyEqMixin:
    compareAttributes = ()

    def __eq__(self, other):
        if not self.compareAttributes:
            return self is other
        if isinstance(self, other.__class__):
            return [ getattr(self, name) for name in self.compareAttributes ] == [ getattr(other, name) for name in self.compareAttributes ]
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result


try:
    from os import initgroups as _c_initgroups
except ImportError:
    try:
        from twisted.python._initgroups import initgroups as _c_initgroups
    except ImportError:
        _c_initgroups = None

if pwd is None or grp is None or setgroups is None or getgroups is None:

    def initgroups(uid, primaryGid):
        pass


else:

    def _setgroups_until_success(l):
        while 1:
            try:
                setgroups(l)
            except ValueError:
                if len(l) > 1:
                    del l[-1]
                else:
                    raise
            except OSError as e:
                if e.errno == errno.EINVAL and len(l) > 1:
                    del l[-1]
                else:
                    raise
            else:
                return


    def initgroups(uid, primaryGid):
        if _c_initgroups is not None:
            return _c_initgroups(pwd.getpwuid(uid)[0], primaryGid)
        else:
            try:
                max_groups = os.sysconf('SC_NGROUPS_MAX')
            except:
                max_groups = 0

            username = pwd.getpwuid(uid)[0]
            l = []
            if primaryGid is not None:
                l.append(primaryGid)
            for groupname, password, gid, userlist in grp.getgrall():
                if username in userlist:
                    l.append(gid)
                    if len(l) == max_groups:
                        break

            try:
                _setgroups_until_success(l)
            except OSError as e:
                if e.errno == errno.EPERM:
                    for g in getgroups():
                        if g not in l:
                            raise

                else:
                    raise

            return


def switchUID(uid, gid, euid=False):
    if euid:
        setuid = os.seteuid
        setgid = os.setegid
        getuid = os.geteuid
    else:
        setuid = os.setuid
        setgid = os.setgid
        getuid = os.getuid
    if gid is not None:
        setgid(gid)
    if uid is not None:
        if uid == getuid():
            uidText = euid and 'euid' or 'uid'
            actionText = 'tried to drop privileges and set%s %s' % (uidText, uid)
            problemText = '%s is already %s' % (uidText, getuid())
            warnings.warn('%s but %s; should we be root? Continuing.' % (
             actionText, problemText))
        else:
            initgroups(uid, gid)
            setuid(uid)
    return


class SubclassableCStringIO(object):
    __csio = None

    def __init__(self, *a, **kw):
        from cStringIO import StringIO
        self.__csio = StringIO(*a, **kw)

    def __iter__(self):
        return self.__csio.__iter__()

    def next(self):
        return self.__csio.next()

    def close(self):
        return self.__csio.close()

    def isatty(self):
        return self.__csio.isatty()

    def seek(self, pos, mode=0):
        return self.__csio.seek(pos, mode)

    def tell(self):
        return self.__csio.tell()

    def read(self, n=-1):
        return self.__csio.read(n)

    def readline(self, length=None):
        return self.__csio.readline(length)

    def readlines(self, sizehint=0):
        return self.__csio.readlines(sizehint)

    def truncate(self, size=None):
        return self.__csio.truncate(size)

    def write(self, s):
        return self.__csio.write(s)

    def writelines(self, list):
        return self.__csio.writelines(list)

    def flush(self):
        return self.__csio.flush()

    def getvalue(self):
        return self.__csio.getvalue()


def untilConcludes(f, *a, **kw):
    while True:
        try:
            return f(*a, **kw)
        except (IOError, OSError) as e:
            if e.args[0] == errno.EINTR:
                continue
            raise


def mergeFunctionMetadata(f, g):
    try:
        g.__name__ = f.__name__
    except TypeError:
        pass

    try:
        g.__doc__ = f.__doc__
    except (TypeError, AttributeError):
        pass

    try:
        g.__dict__.update(f.__dict__)
    except (TypeError, AttributeError):
        pass

    try:
        g.__module__ = f.__module__
    except TypeError:
        pass

    return g


def nameToLabel(mname):
    labelList = []
    word = ''
    lastWasUpper = False
    for letter in mname:
        if letter.isupper() == lastWasUpper:
            word += letter
        elif lastWasUpper:
            if len(word) == 1:
                word += letter
            else:
                lastWord = word[:-1]
                firstLetter = word[-1]
                labelList.append(lastWord)
                word = firstLetter + letter
        else:
            labelList.append(word)
            word = letter
        lastWasUpper = letter.isupper()

    if labelList:
        labelList[0] = labelList[0].capitalize()
    else:
        return mname.capitalize()
    labelList.append(word)
    return (' ').join(labelList)


def uidFromString(uidString):
    try:
        return int(uidString)
    except ValueError:
        if pwd is None:
            raise
        return pwd.getpwnam(uidString)[2]

    return


def gidFromString(gidString):
    try:
        return int(gidString)
    except ValueError:
        if grp is None:
            raise
        return grp.getgrnam(gidString)[2]

    return


def runAsEffectiveUser(euid, egid, function, *args, **kwargs):
    uid, gid = os.geteuid(), os.getegid()
    if uid == euid and gid == egid:
        return function(*args, **kwargs)
    if uid != 0 and (uid != euid or gid != egid):
        os.seteuid(0)
    if gid != egid:
        os.setegid(egid)
    if euid != 0 and (euid != uid or gid != egid):
        os.seteuid(euid)
    try:
        return function(*args, **kwargs)
    finally:
        if euid != 0 and (uid != euid or gid != egid):
            os.seteuid(0)
        if gid != egid:
            os.setegid(gid)
        if uid != 0 and (uid != euid or gid != egid):
            os.seteuid(uid)


def runWithWarningsSuppressed(suppressedWarnings, f, *args, **kwargs):
    with warnings.catch_warnings():
        for a, kw in suppressedWarnings:
            warnings.filterwarnings(*a, **kw)

        return f(*args, **kwargs)


__all__ = [
 'uniquify', 'padTo', 'getPluginDirs', 'addPluginDir', 'sibpath', 
 'getPassword', 
 'println', 'makeStatBar', 'OrderedDict', 
 'InsensitiveDict', 'spewer', 
 'searchupwards', 'LineLog', 
 'raises', 'IntervalDifferential', 'FancyStrMixin', 
 'FancyEqMixin', 
 'switchUID', 'SubclassableCStringIO', 'mergeFunctionMetadata', 
 'nameToLabel', 
 'uidFromString', 'gidFromString', 'runAsEffectiveUser', 
 'untilConcludes', 
 'runWithWarningsSuppressed']
if _PY3:
    __notported__ = [
     'SubclassableCStringIO', 'LineLog', 'makeStatBar']
    for name in __all__[:]:
        if name in __notported__:
            __all__.remove(name)
            del globals()[name]

    del name
    del __notported__
# okay decompiling out\twisted.python.util.pyc
