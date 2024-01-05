# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.python.modules
from __future__ import division, absolute_import
__metaclass__ = type
from os.path import dirname, split as splitpath
import sys, inspect, warnings
from zope.interface import Interface, implementer
from twisted.python.compat import nativeString, _PY3
from twisted.python.components import registerAdapter
from twisted.python.filepath import FilePath, UnlistableError
from twisted.python.reflect import namedAny
if not _PY3:
    from twisted.python.zippath import ZipArchive
    import zipimport
_nothing = object()
PYTHON_EXTENSIONS = [
 '.py']
OPTIMIZED_MODE = __doc__ is None
if OPTIMIZED_MODE:
    PYTHON_EXTENSIONS.append('.pyo')
else:
    PYTHON_EXTENSIONS.append('.pyc')

def _isPythonIdentifier(string):
    textString = nativeString(string)
    return ' ' not in textString and '.' not in textString and '-' not in textString


def _isPackagePath(fpath):
    extless = fpath.splitext()[0]
    basend = splitpath(extless)[1]
    return basend == '__init__'


class _ModuleIteratorHelper:

    def iterModules(self):
        yielded = {}
        if not self.filePath.exists():
            return
        for placeToLook in self._packagePaths():
            try:
                children = sorted(placeToLook.children())
            except UnlistableError:
                continue

            for potentialTopLevel in children:
                ext = potentialTopLevel.splitext()[1]
                potentialBasename = potentialTopLevel.basename()[:-len(ext)]
                if ext in PYTHON_EXTENSIONS:
                    if not _isPythonIdentifier(potentialBasename):
                        continue
                    modname = self._subModuleName(potentialBasename)
                    if modname.split('.')[-1] == '__init__':
                        continue
                    if modname not in yielded:
                        yielded[modname] = True
                        pm = PythonModule(modname, potentialTopLevel, self._getEntry())
                        yield pm
                else:
                    if ext or not _isPythonIdentifier(potentialBasename) or not potentialTopLevel.isdir():
                        continue
                    modname = self._subModuleName(potentialTopLevel.basename())
                    for ext in PYTHON_EXTENSIONS:
                        initpy = potentialTopLevel.child('__init__' + ext)
                        if initpy.exists() and modname not in yielded:
                            yielded[modname] = True
                            pm = PythonModule(modname, initpy, self._getEntry())
                            yield pm
                            break

    def walkModules(self, importPackages=False):
        yield self
        for package in self.iterModules():
            for module in package.walkModules(importPackages=importPackages):
                yield module

    def _subModuleName(self, mn):
        return mn

    def _packagePaths(self):
        raise NotImplementedError()

    def _getEntry(self):
        raise NotImplementedError()

    def __getitem__(self, modname):
        for module in self.iterModules():
            if module.name == self._subModuleName(modname):
                return module

        raise KeyError(modname)

    def __iter__(self):
        raise NotImplementedError()


class PythonAttribute:

    def __init__(self, name, onObject, loaded, pythonValue):
        self.name = name
        self.onObject = onObject
        self._loaded = loaded
        self.pythonValue = pythonValue

    def __repr__(self):
        return 'PythonAttribute<%r>' % (self.name,)

    def isLoaded(self):
        return self._loaded

    def load(self, default=_nothing):
        return self.pythonValue

    def iterAttributes(self):
        for name, val in inspect.getmembers(self.load()):
            yield PythonAttribute(self.name + '.' + name, self, True, val)


class PythonModule(_ModuleIteratorHelper):

    def __init__(self, name, filePath, pathEntry):
        _name = nativeString(name)
        self.name = _name
        self.filePath = filePath
        self.parentPath = filePath.parent()
        self.pathEntry = pathEntry

    def _getEntry(self):
        return self.pathEntry

    def __repr__(self):
        return 'PythonModule<%r>' % (self.name,)

    def isLoaded(self):
        return self.pathEntry.pythonPath.moduleDict.get(self.name) is not None

    def iterAttributes(self):
        if not self.isLoaded():
            raise NotImplementedError("You can't load attributes from non-loaded modules yet.")
        for name, val in inspect.getmembers(self.load()):
            yield PythonAttribute(self.name + '.' + name, self, True, val)

    def isPackage(self):
        return _isPackagePath(self.filePath)

    def load(self, default=_nothing):
        try:
            return self.pathEntry.pythonPath.moduleLoader(self.name)
        except:
            if default is not _nothing:
                return default
            raise

    def __eq__(self, other):
        if not isinstance(other, PythonModule):
            return False
        return other.name == self.name

    def __ne__(self, other):
        if not isinstance(other, PythonModule):
            return True
        return other.name != self.name

    def walkModules(self, importPackages=False):
        if importPackages and self.isPackage():
            self.load()
        return super(PythonModule, self).walkModules(importPackages=importPackages)

    def _subModuleName(self, mn):
        return self.name + '.' + mn

    def _packagePaths(self):
        if not self.isPackage():
            return
        if self.isLoaded():
            load = self.load()
            if hasattr(load, '__path__'):
                for fn in load.__path__:
                    if fn == self.parentPath.path:
                        yield self.parentPath
                    else:
                        smp = self.pathEntry.pythonPath._smartPath(fn)
                        if smp.exists():
                            yield smp

        else:
            yield self.parentPath


class PathEntry(_ModuleIteratorHelper):

    def __init__(self, filePath, pythonPath):
        self.filePath = filePath
        self.pythonPath = pythonPath

    def _getEntry(self):
        return self

    def __repr__(self):
        return 'PathEntry<%r>' % (self.filePath,)

    def _packagePaths(self):
        yield self.filePath


class IPathImportMapper(Interface):

    def mapPath(self, pathLikeString):
        pass


@implementer(IPathImportMapper)
class _DefaultMapImpl:

    def mapPath(self, fsPathString):
        return FilePath(fsPathString)


_theDefaultMapper = _DefaultMapImpl()
if not _PY3:

    @implementer(IPathImportMapper)
    class _ZipMapImpl:

        def __init__(self, importer):
            self.importer = importer

        def mapPath(self, fsPathString):
            za = ZipArchive(self.importer.archive)
            myPath = FilePath(self.importer.archive)
            itsPath = FilePath(fsPathString)
            if myPath == itsPath:
                return za
            segs = itsPath.segmentsFrom(myPath)
            zp = za
            for seg in segs:
                zp = zp.child(seg)

            return zp


    registerAdapter(_ZipMapImpl, zipimport.zipimporter, IPathImportMapper)

def _defaultSysPathFactory():
    return sys.path


class PythonPath:

    def __init__(self, sysPath=None, moduleDict=sys.modules, sysPathHooks=sys.path_hooks, importerCache=sys.path_importer_cache, moduleLoader=namedAny, sysPathFactory=None):
        if sysPath is not None:
            sysPathFactory = lambda : sysPath
        elif sysPathFactory is None:
            sysPathFactory = _defaultSysPathFactory
        self._sysPathFactory = sysPathFactory
        self._sysPath = sysPath
        self.moduleDict = moduleDict
        self.sysPathHooks = sysPathHooks
        self.importerCache = importerCache
        self.moduleLoader = moduleLoader
        return

    def _getSysPath(self):
        return self._sysPathFactory()

    sysPath = property(_getSysPath)

    def _findEntryPathString(self, modobj):
        topPackageObj = modobj
        while '.' in topPackageObj.__name__:
            topPackageObj = self.moduleDict[('.').join(topPackageObj.__name__.split('.')[:-1])]

        if _isPackagePath(FilePath(topPackageObj.__file__)):
            rval = dirname(dirname(topPackageObj.__file__))
        else:
            rval = dirname(topPackageObj.__file__)
        if rval not in self.importerCache:
            warnings.warn('%s (for module %s) not in path importer cache (PEP 302 violation - check your local configuration).' % (
             rval, modobj.__name__), stacklevel=3)
        return rval

    def _smartPath(self, pathName):
        importr = self.importerCache.get(pathName, _nothing)
        if importr is _nothing:
            for hook in self.sysPathHooks:
                try:
                    importr = hook(pathName)
                except ImportError:
                    pass

            if importr is _nothing:
                importr = None
        return IPathImportMapper(importr, _theDefaultMapper).mapPath(pathName)

    def iterEntries(self):
        for pathName in self.sysPath:
            fp = self._smartPath(pathName)
            yield PathEntry(fp, self)

    def __getitem__(self, modname):
        moduleObject = self.moduleDict.get(modname)
        if moduleObject is not None:
            pe = PathEntry(self._smartPath(self._findEntryPathString(moduleObject)), self)
            mp = self._smartPath(moduleObject.__file__)
            return PythonModule(modname, mp, pe)
        else:
            if '.' in modname:
                pkg = self
                for name in modname.split('.'):
                    pkg = pkg[name]

                return pkg
            for module in self.iterModules():
                if module.name == modname:
                    return module

            raise KeyError(modname)
            return

    def __contains__(self, module):
        try:
            self.__getitem__(module)
            return True
        except KeyError:
            return False

    def __repr__(self):
        return 'PythonPath(%r,%r)' % (self.sysPath, self.moduleDict)

    def iterModules(self):
        for entry in self.iterEntries():
            for module in entry.iterModules():
                yield module

    def walkModules(self, importPackages=False):
        for package in self.iterModules():
            for module in package.walkModules(importPackages=False):
                yield module


theSystemPath = PythonPath()

def walkModules(importPackages=False):
    return theSystemPath.walkModules(importPackages=importPackages)


def iterModules():
    return theSystemPath.iterModules()


def getModule(moduleName):
    return theSystemPath[moduleName]
# okay decompiling out\twisted.python.modules.pyc
