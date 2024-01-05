# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.protocols.basic
from __future__ import absolute_import, division
import re
from struct import pack, unpack, calcsize
from io import BytesIO
import math
from zope.interface import implementer
from twisted.python.compat import _PY3
from twisted.internet import protocol, defer, interfaces, error
from twisted.python import log
if _PY3:

    def _formatNetstring(data):
        return ('').join([str(len(data)).encode('ascii'), ':', data, ','])


else:

    def _formatNetstring(data):
        return '%d:%s,' % (len(data), data)


_formatNetstring.__doc__ = '\nConvert some C{bytes} into netstring format.\n\n@param data: C{bytes} that will be reformatted.\n'
DEBUG = 0

class NetstringParseError(ValueError):
    pass


class IncompleteNetstring(Exception):
    pass


class NetstringReceiver(protocol.Protocol):
    MAX_LENGTH = 99999
    _LENGTH = re.compile('(0|[1-9]\\d*)(:)')
    _LENGTH_PREFIX = re.compile('(0|[1-9]\\d*)$')
    _MISSING_LENGTH = 'The received netstring does not start with a length specification.'
    _OVERFLOW = 'The length specification of the received netstring cannot be represented in Python - it causes an OverflowError!'
    _TOO_LONG = 'The received netstring is longer than the maximum %s specified by self.MAX_LENGTH'
    _MISSING_COMMA = 'The received netstring is not terminated by a comma.'
    _PARSING_LENGTH, _PARSING_PAYLOAD = range(2)

    def makeConnection(self, transport):
        protocol.Protocol.makeConnection(self, transport)
        self._remainingData = ''
        self._currentPayloadSize = 0
        self._payload = BytesIO()
        self._state = self._PARSING_LENGTH
        self._expectedPayloadSize = 0
        self.brokenPeer = 0

    def sendString(self, string):
        self.transport.write(_formatNetstring(string))

    def dataReceived(self, data):
        self._remainingData += data
        while self._remainingData:
            try:
                self._consumeData()
            except IncompleteNetstring:
                break
            except NetstringParseError:
                self._handleParseError()
                break

    def stringReceived(self, string):
        raise NotImplementedError()

    def _maxLengthSize(self):
        return math.ceil(math.log10(self.MAX_LENGTH)) + 1

    def _consumeData(self):
        if self._state == self._PARSING_LENGTH:
            self._consumeLength()
            self._prepareForPayloadConsumption()
        if self._state == self._PARSING_PAYLOAD:
            self._consumePayload()

    def _consumeLength(self):
        lengthMatch = self._LENGTH.match(self._remainingData)
        if not lengthMatch:
            self._checkPartialLengthSpecification()
            raise IncompleteNetstring()
        self._processLength(lengthMatch)

    def _checkPartialLengthSpecification(self):
        partialLengthMatch = self._LENGTH_PREFIX.match(self._remainingData)
        if not partialLengthMatch:
            raise NetstringParseError(self._MISSING_LENGTH)
        lengthSpecification = partialLengthMatch.group(1)
        self._extractLength(lengthSpecification)

    def _processLength(self, lengthMatch):
        endOfNumber = lengthMatch.end(1)
        startOfData = lengthMatch.end(2)
        lengthString = self._remainingData[:endOfNumber]
        self._expectedPayloadSize = self._extractLength(lengthString) + 1
        self._remainingData = self._remainingData[startOfData:]

    def _extractLength(self, lengthAsString):
        self._checkStringSize(lengthAsString)
        length = int(lengthAsString)
        if length > self.MAX_LENGTH:
            raise NetstringParseError(self._TOO_LONG % (self.MAX_LENGTH,))
        return length

    def _checkStringSize(self, lengthAsString):
        if len(lengthAsString) > self._maxLengthSize():
            raise NetstringParseError(self._TOO_LONG % (self.MAX_LENGTH,))

    def _prepareForPayloadConsumption(self):
        self._state = self._PARSING_PAYLOAD
        self._currentPayloadSize = 0
        self._payload.seek(0)
        self._payload.truncate()

    def _consumePayload(self):
        self._extractPayload()
        if self._currentPayloadSize < self._expectedPayloadSize:
            raise IncompleteNetstring()
        self._checkForTrailingComma()
        self._state = self._PARSING_LENGTH
        self._processPayload()

    def _extractPayload(self):
        if self._payloadComplete():
            remainingPayloadSize = self._expectedPayloadSize - self._currentPayloadSize
            self._payload.write(self._remainingData[:remainingPayloadSize])
            self._remainingData = self._remainingData[remainingPayloadSize:]
            self._currentPayloadSize = self._expectedPayloadSize
        else:
            self._payload.write(self._remainingData)
            self._currentPayloadSize += len(self._remainingData)
            self._remainingData = ''

    def _payloadComplete(self):
        return len(self._remainingData) + self._currentPayloadSize >= self._expectedPayloadSize

    def _processPayload(self):
        self.stringReceived(self._payload.getvalue()[:-1])

    def _checkForTrailingComma(self):
        if self._payload.getvalue()[-1:] != ',':
            raise NetstringParseError(self._MISSING_COMMA)

    def _handleParseError(self):
        self.transport.loseConnection()
        self.brokenPeer = 1


class LineOnlyReceiver(protocol.Protocol):
    _buffer = ''
    delimiter = '\r\n'
    MAX_LENGTH = 16384

    def dataReceived(self, data):
        lines = (self._buffer + data).split(self.delimiter)
        self._buffer = lines.pop(-1)
        for line in lines:
            if self.transport.disconnecting:
                return
            if len(line) > self.MAX_LENGTH:
                return self.lineLengthExceeded(line)
            self.lineReceived(line)

        if len(self._buffer) > self.MAX_LENGTH:
            return self.lineLengthExceeded(self._buffer)

    def lineReceived(self, line):
        raise NotImplementedError

    def sendLine(self, line):
        return self.transport.writeSequence((line, self.delimiter))

    def lineLengthExceeded(self, line):
        return error.ConnectionLost('Line length exceeded')


class _PauseableMixin():
    paused = False

    def pauseProducing(self):
        self.paused = True
        self.transport.pauseProducing()

    def resumeProducing(self):
        self.paused = False
        self.transport.resumeProducing()
        self.dataReceived('')

    def stopProducing(self):
        self.paused = True
        self.transport.stopProducing()


class LineReceiver(protocol.Protocol, _PauseableMixin):
    line_mode = 1
    _buffer = ''
    _busyReceiving = False
    delimiter = '\r\n'
    MAX_LENGTH = 16384

    def clearLineBuffer(self):
        b, self._buffer = self._buffer, ''
        return b

    def dataReceived(self, data):
        if self._busyReceiving:
            self._buffer += data
            return
        try:
            self._busyReceiving = True
            self._buffer += data
            while self._buffer and not self.paused:
                if self.line_mode:
                    try:
                        line, self._buffer = self._buffer.split(self.delimiter, 1)
                    except ValueError:
                        if len(self._buffer) > self.MAX_LENGTH:
                            line, self._buffer = self._buffer, ''
                            return self.lineLengthExceeded(line)
                        return

                    lineLength = len(line)
                    if lineLength > self.MAX_LENGTH:
                        exceeded = line + self.delimiter + self._buffer
                        self._buffer = ''
                        return self.lineLengthExceeded(exceeded)
                    why = self.lineReceived(line)
                    if why or self.transport and self.transport.disconnecting:
                        return why
                else:
                    data = self._buffer
                    self._buffer = ''
                    why = self.rawDataReceived(data)
                    if why:
                        return why

        finally:
            self._busyReceiving = False

    def setLineMode(self, extra=''):
        self.line_mode = 1
        if extra:
            return self.dataReceived(extra)

    def setRawMode(self):
        self.line_mode = 0

    def rawDataReceived(self, data):
        raise NotImplementedError

    def lineReceived(self, line):
        raise NotImplementedError

    def sendLine(self, line):
        return self.transport.write(line + self.delimiter)

    def lineLengthExceeded(self, line):
        return self.transport.loseConnection()


class StringTooLongError(AssertionError):
    pass


class _RecvdCompatHack(object):

    def __get__(self, oself, type=None):
        return oself._unprocessed[oself._compatibilityOffset:]


class IntNStringReceiver(protocol.Protocol, _PauseableMixin):
    MAX_LENGTH = 99999
    _unprocessed = ''
    _compatibilityOffset = 0
    recvd = _RecvdCompatHack()

    def stringReceived(self, string):
        raise NotImplementedError

    def lengthLimitExceeded(self, length):
        self.transport.loseConnection()

    def dataReceived(self, data):
        alldata = self._unprocessed + data
        currentOffset = 0
        prefixLength = self.prefixLength
        fmt = self.structFormat
        self._unprocessed = alldata
        while len(alldata) >= currentOffset + prefixLength and not self.paused:
            messageStart = currentOffset + prefixLength
            length, = unpack(fmt, alldata[currentOffset:messageStart])
            if length > self.MAX_LENGTH:
                self._unprocessed = alldata
                self._compatibilityOffset = currentOffset
                self.lengthLimitExceeded(length)
                return
            messageEnd = messageStart + length
            if len(alldata) < messageEnd:
                break
            packet = alldata[messageStart:messageEnd]
            currentOffset = messageEnd
            self._compatibilityOffset = currentOffset
            self.stringReceived(packet)
            if 'recvd' in self.__dict__:
                alldata = self.__dict__.pop('recvd')
                self._unprocessed = alldata
                self._compatibilityOffset = currentOffset = 0
                if alldata:
                    continue
                return

        self._unprocessed = alldata[currentOffset:]
        self._compatibilityOffset = 0

    def sendString(self, string):
        if len(string) >= 2 ** (8 * self.prefixLength):
            raise StringTooLongError('Try to send %s bytes whereas maximum is %s' % (
             len(string), 2 ** (8 * self.prefixLength)))
        self.transport.write(pack(self.structFormat, len(string)) + string)


class Int32StringReceiver(IntNStringReceiver):
    structFormat = '!I'
    prefixLength = calcsize(structFormat)


class Int16StringReceiver(IntNStringReceiver):
    structFormat = '!H'
    prefixLength = calcsize(structFormat)


class Int8StringReceiver(IntNStringReceiver):
    structFormat = '!B'
    prefixLength = calcsize(structFormat)


class StatefulStringProtocol():
    state = 'init'

    def stringReceived(self, string):
        try:
            pto = 'proto_' + self.state
            statehandler = getattr(self, pto)
        except AttributeError:
            log.msg('callback', self.state, 'not found')

        self.state = statehandler(string)
        if self.state == 'done':
            self.transport.loseConnection()


@implementer(interfaces.IProducer)
class FileSender():
    CHUNK_SIZE = 16384
    lastSent = ''
    deferred = None

    def beginFileTransfer(self, file, consumer, transform=None):
        self.file = file
        self.consumer = consumer
        self.transform = transform
        self.deferred = deferred = defer.Deferred()
        self.consumer.registerProducer(self, False)
        return deferred

    def resumeProducing(self):
        chunk = ''
        if self.file:
            chunk = self.file.read(self.CHUNK_SIZE)
        if not chunk:
            self.file = None
            self.consumer.unregisterProducer()
            if self.deferred:
                self.deferred.callback(self.lastSent)
                self.deferred = None
            return
        if self.transform:
            chunk = self.transform(chunk)
        self.consumer.write(chunk)
        self.lastSent = chunk[-1:]
        return

    def pauseProducing(self):
        pass

    def stopProducing(self):
        if self.deferred:
            self.deferred.errback(Exception('Consumer asked us to stop producing'))
            self.deferred = None
        return
# okay decompiling out\twisted.protocols.basic.pyc
