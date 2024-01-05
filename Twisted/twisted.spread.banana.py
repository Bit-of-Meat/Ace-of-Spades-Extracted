# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.spread.banana
import copy, cStringIO, struct
from twisted.internet import protocol
from twisted.persisted import styles
from twisted.python import log
from twisted.python.reflect import fullyQualifiedName

class BananaError(Exception):
    pass


def int2b128(integer, stream):
    if integer == 0:
        stream(chr(0))
        return
    while integer:
        stream(chr(integer & 127))
        integer = integer >> 7


def b1282int(st):
    e = 1
    i = 0
    for char in st:
        n = ord(char)
        i += n * e
        e <<= 7

    return i


LIST = chr(128)
INT = chr(129)
STRING = chr(130)
NEG = chr(131)
FLOAT = chr(132)
LONGINT = chr(133)
LONGNEG = chr(134)
VOCAB = chr(135)
HIGH_BIT_SET = chr(128)

def setPrefixLimit(limit):
    global _PREFIX_LIMIT
    _PREFIX_LIMIT = limit


_PREFIX_LIMIT = None
setPrefixLimit(64)
SIZE_LIMIT = 640 * 1024

class Banana(protocol.Protocol, styles.Ephemeral):
    knownDialects = [
     'pb', 'none']
    prefixLimit = None
    sizeLimit = SIZE_LIMIT

    def setPrefixLimit(self, limit):
        self.prefixLimit = limit
        self._smallestLongInt = -2 ** (limit * 7) + 1
        self._smallestInt = -2147483648
        self._largestInt = 2147483647
        self._largestLongInt = 2 ** (limit * 7) - 1

    def connectionReady(self):
        pass

    def _selectDialect(self, dialect):
        self.currentDialect = dialect
        self.connectionReady()

    def callExpressionReceived(self, obj):
        if self.currentDialect:
            self.expressionReceived(obj)
        elif self.isClient:
            for serverVer in obj:
                if serverVer in self.knownDialects:
                    self.sendEncoded(serverVer)
                    self._selectDialect(serverVer)
                    break
            else:
                log.msg("The client doesn't speak any of the protocols offered by the server: disconnecting.")
                self.transport.loseConnection()

        elif obj in self.knownDialects:
            self._selectDialect(obj)
        else:
            log.msg("The client selected a protocol the server didn't suggest and doesn't know: disconnecting.")
            self.transport.loseConnection()

    def connectionMade(self):
        self.setPrefixLimit(_PREFIX_LIMIT)
        self.currentDialect = None
        if not self.isClient:
            self.sendEncoded(self.knownDialects)
        return

    def gotItem(self, item):
        l = self.listStack
        if l:
            l[-1][1].append(item)
        else:
            self.callExpressionReceived(item)

    buffer = ''

    def dataReceived(self, chunk):
        buffer = self.buffer + chunk
        listStack = self.listStack
        gotItem = self.gotItem
        while buffer:
            self.buffer = buffer
            pos = 0
            for ch in buffer:
                if ch >= HIGH_BIT_SET:
                    break
                pos = pos + 1
            else:
                if pos > self.prefixLimit:
                    raise BananaError('Security precaution: more than %d bytes of prefix' % (self.prefixLimit,))
                return

            num = buffer[:pos]
            typebyte = buffer[pos]
            rest = buffer[pos + 1:]
            if len(num) > self.prefixLimit:
                raise BananaError('Security precaution: longer than %d bytes worth of prefix' % (self.prefixLimit,))
            if typebyte == LIST:
                num = b1282int(num)
                if num > SIZE_LIMIT:
                    raise BananaError('Security precaution: List too long.')
                listStack.append((num, []))
                buffer = rest
            elif typebyte == STRING:
                num = b1282int(num)
                if num > SIZE_LIMIT:
                    raise BananaError('Security precaution: String too long.')
                if len(rest) >= num:
                    buffer = rest[num:]
                    gotItem(rest[:num])
                else:
                    return
            elif typebyte == INT:
                buffer = rest
                num = b1282int(num)
                gotItem(num)
            elif typebyte == LONGINT:
                buffer = rest
                num = b1282int(num)
                gotItem(num)
            elif typebyte == LONGNEG:
                buffer = rest
                num = b1282int(num)
                gotItem(-num)
            elif typebyte == NEG:
                buffer = rest
                num = -b1282int(num)
                gotItem(num)
            elif typebyte == VOCAB:
                buffer = rest
                num = b1282int(num)
                item = self.incomingVocabulary[num]
                if self.currentDialect == 'pb':
                    gotItem(item)
                else:
                    raise NotImplementedError(('Invalid item for pb protocol {0!r}').format(item))
            elif typebyte == FLOAT:
                if len(rest) >= 8:
                    buffer = rest[8:]
                    gotItem(struct.unpack('!d', rest[:8])[0])
                else:
                    return
            else:
                raise NotImplementedError('Invalid Type Byte %r' % (typebyte,))
            while listStack and len(listStack[-1][1]) == listStack[-1][0]:
                item = listStack.pop()[1]
                gotItem(item)

        self.buffer = ''

    def expressionReceived(self, lst):
        raise NotImplementedError()

    outgoingVocabulary = {'None': 1, 
       'class': 2, 
       'dereference': 3, 
       'reference': 4, 
       'dictionary': 5, 
       'function': 6, 
       'instance': 7, 
       'list': 8, 
       'module': 9, 
       'persistent': 10, 
       'tuple': 11, 
       'unpersistable': 12, 
       'copy': 13, 
       'cache': 14, 
       'cached': 15, 
       'remote': 16, 
       'local': 17, 
       'lcache': 18, 
       'version': 19, 
       'login': 20, 
       'password': 21, 
       'challenge': 22, 
       'logged_in': 23, 
       'not_logged_in': 24, 
       'cachemessage': 25, 
       'message': 26, 
       'answer': 27, 
       'error': 28, 
       'decref': 29, 
       'decache': 30, 
       'uncache': 31}
    incomingVocabulary = {}
    for k, v in outgoingVocabulary.items():
        incomingVocabulary[v] = k

    def __init__(self, isClient=1):
        self.listStack = []
        self.outgoingSymbols = copy.copy(self.outgoingVocabulary)
        self.outgoingSymbolCount = 0
        self.isClient = isClient

    def sendEncoded(self, obj):
        io = cStringIO.StringIO()
        self._encode(obj, io.write)
        value = io.getvalue()
        self.transport.write(value)

    def _encode(self, obj, write):
        if isinstance(obj, (list, tuple)):
            if len(obj) > SIZE_LIMIT:
                raise BananaError('list/tuple is too long to send (%d)' % (len(obj),))
            int2b128(len(obj), write)
            write(LIST)
            for elem in obj:
                self._encode(elem, write)

        elif isinstance(obj, (int, long)):
            if obj < self._smallestLongInt or obj > self._largestLongInt:
                raise BananaError('int/long is too large to send (%d)' % (obj,))
            if obj < self._smallestInt:
                int2b128(-obj, write)
                write(LONGNEG)
            elif obj < 0:
                int2b128(-obj, write)
                write(NEG)
            elif obj <= self._largestInt:
                int2b128(obj, write)
                write(INT)
            else:
                int2b128(obj, write)
                write(LONGINT)
        elif isinstance(obj, float):
            write(FLOAT)
            write(struct.pack('!d', obj))
        elif isinstance(obj, str):
            if self.currentDialect == 'pb' and obj in self.outgoingSymbols:
                symbolID = self.outgoingSymbols[obj]
                int2b128(symbolID, write)
                write(VOCAB)
            else:
                if len(obj) > SIZE_LIMIT:
                    raise BananaError('string is too long to send (%d)' % (len(obj),))
                int2b128(len(obj), write)
                write(STRING)
                write(obj)
        else:
            raise BananaError(('Banana cannot send {0} objects: {1!r}').format(fullyQualifiedName(type(obj)), obj))


_i = Banana()
_i.connectionMade()
_i._selectDialect('none')

def encode(lst):
    io = cStringIO.StringIO()
    _i.transport = io
    _i.sendEncoded(lst)
    return io.getvalue()


def decode(st):
    l = []
    _i.expressionReceived = l.append
    try:
        _i.dataReceived(st)
    finally:
        _i.buffer = ''
        del _i.expressionReceived

    return l[0]
# okay decompiling out\twisted.spread.banana.pyc
