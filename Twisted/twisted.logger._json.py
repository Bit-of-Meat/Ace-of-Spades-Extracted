# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._json
import types
from json import dumps, loads
from uuid import UUID
from ._flatten import flattenEvent
from ._file import FileLogObserver
from ._levels import LogLevel
from ._logger import Logger
from twisted.python.constants import NamedConstant
from twisted.python.compat import unicode
from twisted.python.failure import Failure
log = Logger()

def failureAsJSON(failure):
    return dict(failure.__getstate__(), type=dict(__module__=failure.type.__module__, __name__=failure.type.__name__))


def asBytes(obj):
    if isinstance(obj, list):
        return map(asBytes, obj)
    else:
        if isinstance(obj, dict):
            return dict((asBytes(k), asBytes(v)) for k, v in obj.items())
        if isinstance(obj, unicode):
            return obj.encode('utf-8')
        return obj


def failureFromJSON(failureDict):
    newFailure = getattr(Failure, '__new__', None)
    if newFailure is None:
        failureDict = asBytes(failureDict)
        f = types.InstanceType(Failure)
    else:
        f = newFailure(Failure)
    typeInfo = failureDict['type']
    failureDict['type'] = type(typeInfo['__name__'], (), typeInfo)
    f.__dict__ = failureDict
    return f


classInfo = [
 (
  (lambda level: isinstance(level, NamedConstant) and getattr(LogLevel, level.name, None) is level),
  UUID('02E59486-F24D-46AD-8224-3ACDF2A5732A'),
  (lambda level: dict(name=level.name)),
  (lambda level: getattr(LogLevel, level['name'], None))),
 (
  (lambda o: isinstance(o, Failure)),
  UUID('E76887E2-20ED-49BF-A8F8-BA25CC586F2D'),
  failureAsJSON, failureFromJSON)]
uuidToLoader = dict([ (uuid, loader) for predicate, uuid, saver, loader in classInfo ])

def objectLoadHook(aDict):
    if '__class_uuid__' in aDict:
        return uuidToLoader[UUID(aDict['__class_uuid__'])](aDict)
    return aDict


def objectSaveHook(pythonObject):
    for predicate, uuid, saver, loader in classInfo:
        if predicate(pythonObject):
            result = saver(pythonObject)
            result['__class_uuid__'] = str(uuid)
            return result

    return {'unpersistable': True}


def eventAsJSON(event):
    if bytes is str:
        kw = dict(default=objectSaveHook, encoding='charmap', skipkeys=True)
    else:

        def default(unencodable):
            if isinstance(unencodable, bytes):
                return unencodable.decode('charmap')
            return objectSaveHook(unencodable)

        kw = dict(default=default, skipkeys=True)
    flattenEvent(event)
    result = dumps(event, **kw)
    if not isinstance(result, unicode):
        return unicode(result, 'utf-8', 'replace')
    return result


def eventFromJSON(eventText):
    loaded = loads(eventText, object_hook=objectLoadHook)
    return loaded


def jsonFileLogObserver(outFile, recordSeparator='\x1e'):
    return FileLogObserver(outFile, (lambda event: ('{0}{1}\n').format(recordSeparator, eventAsJSON(event))))


def eventsFromJSONLogFile(inFile, recordSeparator=None, bufferSize=4096):

    def asBytes(s):
        if type(s) is bytes:
            return s
        else:
            return s.encode('utf-8')

    def eventFromBytearray(record):
        try:
            text = bytes(record).decode('utf-8')
        except UnicodeDecodeError:
            log.error('Unable to decode UTF-8 for JSON record: {record!r}', record=bytes(record))
            return

        try:
            return eventFromJSON(text)
        except ValueError:
            log.error('Unable to read JSON record: {record!r}', record=bytes(record))
            return

        return

    if recordSeparator is None:
        first = asBytes(inFile.read(1))
        if first == '\x1e':
            recordSeparator = first
        else:
            recordSeparator = ''
    else:
        recordSeparator = asBytes(recordSeparator)
        first = ''
    if recordSeparator == '':
        recordSeparator = '\n'
        eventFromRecord = eventFromBytearray
    else:

        def eventFromRecord(record):
            if record[-1] == ord('\n'):
                return eventFromBytearray(record)
            else:
                log.error('Unable to read truncated JSON record: {record!r}', record=bytes(record))
                return

    buffer = bytearray(first)
    while True:
        newData = inFile.read(bufferSize)
        if not newData:
            if len(buffer) > 0:
                event = eventFromRecord(buffer)
                if event is not None:
                    yield event
            break
        buffer += asBytes(newData)
        records = buffer.split(recordSeparator)
        for record in records[:-1]:
            if len(record) > 0:
                event = eventFromRecord(record)
                if event is not None:
                    yield event

        buffer = records[-1]

    return
# okay decompiling out\twisted.logger._json.pyc
