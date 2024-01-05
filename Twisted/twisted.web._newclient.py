# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web._newclient
from __future__ import division, absolute_import
__metaclass__ = type
from zope.interface import implementer
from twisted.python import log
from twisted.python.compat import networkString
from twisted.python.components import proxyForInterface
from twisted.python.reflect import fullyQualifiedName
from twisted.python.failure import Failure
from twisted.internet.interfaces import IConsumer, IPushProducer
from twisted.internet.error import ConnectionDone
from twisted.internet.defer import Deferred, succeed, fail, maybeDeferred
from twisted.internet.defer import CancelledError
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.web.iweb import UNKNOWN_LENGTH, IResponse, IClientRequest
from twisted.web.http_headers import Headers
from twisted.web.http import NO_CONTENT, NOT_MODIFIED
from twisted.web.http import _DataLoss, PotentialDataLoss
from twisted.web.http import _IdentityTransferDecoder, _ChunkedTransferDecoder
STATUS = 'STATUS'
HEADER = 'HEADER'
BODY = 'BODY'
DONE = 'DONE'

class BadHeaders(Exception):
    pass


class ExcessWrite(Exception):
    pass


class ParseError(Exception):

    def __init__(self, reason, data):
        Exception.__init__(self, reason, data)
        self.data = data


class BadResponseVersion(ParseError):
    pass


class _WrapperException(Exception):

    def __init__(self, reasons):
        Exception.__init__(self, reasons)
        self.reasons = reasons


class RequestGenerationFailed(_WrapperException):
    pass


class RequestTransmissionFailed(_WrapperException):
    pass


class ConnectionAborted(Exception):
    pass


class WrongBodyLength(Exception):
    pass


class ResponseDone(Exception):
    pass


class ResponseFailed(_WrapperException):

    def __init__(self, reasons, response=None):
        _WrapperException.__init__(self, reasons)
        self.response = response


class ResponseNeverReceived(ResponseFailed):
    pass


class RequestNotSent(Exception):
    pass


def _callAppFunction(function):
    try:
        function()
    except:
        log.err(None, 'Unexpected exception from %s' % (
         fullyQualifiedName(function),))

    return


class HTTPParser(LineReceiver):
    delimiter = '\n'
    CONNECTION_CONTROL_HEADERS = set([
     'content-length', 'connection', 'keep-alive', 'te', 
     'trailers', 
     'transfer-encoding', 'upgrade', 
     'proxy-connection'])

    def connectionMade(self):
        self.headers = Headers()
        self.connHeaders = Headers()
        self.state = STATUS
        self._partialHeader = None
        return

    def switchToBodyMode(self, decoder):
        if self.state == BODY:
            raise RuntimeError('already in body mode')
        self.bodyDecoder = decoder
        self.state = BODY
        self.setRawMode()

    def lineReceived(self, line):
        if line[-1:] == '\r':
            line = line[:-1]
        if self.state == STATUS:
            self.statusReceived(line)
            self.state = HEADER
        elif self.state == HEADER:
            if not line or line[0] not in ' \t':
                if self._partialHeader is not None:
                    header = ('').join(self._partialHeader)
                    name, value = header.split(':', 1)
                    value = value.strip()
                    self.headerReceived(name, value)
                if not line:
                    self.allHeadersReceived()
                else:
                    self._partialHeader = [
                     line]
            else:
                self._partialHeader.append(line)
        return

    def rawDataReceived(self, data):
        self.bodyDecoder.dataReceived(data)

    def isConnectionControlHeader(self, name):
        return name in self.CONNECTION_CONTROL_HEADERS

    def statusReceived(self, status):
        pass

    def headerReceived(self, name, value):
        name = name.lower()
        if self.isConnectionControlHeader(name):
            headers = self.connHeaders
        else:
            headers = self.headers
        headers.addRawHeader(name, value)

    def allHeadersReceived(self):
        self.switchToBodyMode(None)
        return


class HTTPClientParser(HTTPParser):
    NO_BODY_CODES = set([NO_CONTENT, NOT_MODIFIED])
    _transferDecoders = {'chunked': _ChunkedTransferDecoder}
    bodyDecoder = None

    def __init__(self, request, finisher):
        self.request = request
        self.finisher = finisher
        self._responseDeferred = Deferred()
        self._everReceivedData = False

    def dataReceived(self, data):
        self._everReceivedData = True
        HTTPParser.dataReceived(self, data)

    def parseVersion(self, strversion):
        try:
            proto, strnumber = strversion.split('/')
            major, minor = strnumber.split('.')
            major, minor = int(major), int(minor)
        except ValueError as e:
            raise BadResponseVersion(str(e), strversion)

        if major < 0 or minor < 0:
            raise BadResponseVersion('version may not be negative', strversion)
        return (
         proto, major, minor)

    def statusReceived(self, status):
        parts = status.split(' ', 2)
        if len(parts) != 3:
            raise ParseError('wrong number of parts', status)
        try:
            statusCode = int(parts[1])
        except ValueError:
            raise ParseError('non-integer status code', status)

        self.response = Response._construct(self.parseVersion(parts[0]), statusCode, parts[2], self.headers, self.transport, self.request)

    def _finished(self, rest):
        self.state = DONE
        self.finisher(rest)

    def isConnectionControlHeader(self, name):
        if self.request.method == 'HEAD' and name == 'content-length':
            return False
        return HTTPParser.isConnectionControlHeader(self, name)

    def allHeadersReceived(self):
        if self.response.code in self.NO_BODY_CODES or self.request.method == 'HEAD':
            self.response.length = 0
            self._finished(self.clearLineBuffer())
            self.response._bodyDataFinished()
        else:
            transferEncodingHeaders = self.connHeaders.getRawHeaders('transfer-encoding')
            if transferEncodingHeaders:
                transferDecoder = self._transferDecoders[transferEncodingHeaders[0].lower()]
            else:
                contentLengthHeaders = self.connHeaders.getRawHeaders('content-length')
                if contentLengthHeaders is None:
                    contentLength = None
                elif len(contentLengthHeaders) == 1:
                    contentLength = int(contentLengthHeaders[0])
                    self.response.length = contentLength
                else:
                    raise ValueError('Too many Content-Length headers; response is invalid')
                if contentLength == 0:
                    self._finished(self.clearLineBuffer())
                    transferDecoder = None
                else:
                    transferDecoder = lambda x, y: _IdentityTransferDecoder(contentLength, x, y)
            if transferDecoder is None:
                self.response._bodyDataFinished()
            else:
                self.transport.pauseProducing()
                self.switchToBodyMode(transferDecoder(self.response._bodyDataReceived, self._finished))
        self._responseDeferred.callback(self.response)
        del self._responseDeferred
        return

    def connectionLost(self, reason):
        if self.bodyDecoder is not None:
            try:
                try:
                    self.bodyDecoder.noMoreData()
                except PotentialDataLoss:
                    self.response._bodyDataFinished(Failure())
                except _DataLoss:
                    self.response._bodyDataFinished(Failure(ResponseFailed([reason, Failure()], self.response)))
                else:
                    self.response._bodyDataFinished()

            except:
                log.err()

        elif self.state != DONE:
            if self._everReceivedData:
                exceptionClass = ResponseFailed
            else:
                exceptionClass = ResponseNeverReceived
            self._responseDeferred.errback(Failure(exceptionClass([reason])))
            del self._responseDeferred
        return


@implementer(IClientRequest)
class Request():

    def __init__(self, method, uri, headers, bodyProducer, persistent=False):
        self.method = method
        self.uri = uri
        self.headers = headers
        self.bodyProducer = bodyProducer
        self.persistent = persistent
        self._parsedURI = None
        return

    @classmethod
    def _construct(cls, method, uri, headers, bodyProducer, persistent=False, parsedURI=None):
        request = cls(method, uri, headers, bodyProducer, persistent)
        request._parsedURI = parsedURI
        return request

    @property
    def absoluteURI(self):
        return getattr(self._parsedURI, 'toBytes', (lambda : None))()

    def _writeHeaders(self, transport, TEorCL):
        hosts = self.headers.getRawHeaders('host', ())
        if len(hosts) != 1:
            raise BadHeaders('Exactly one Host header required')
        requestLines = []
        requestLines.append((' ').join([self.method, self.uri,
         'HTTP/1.1\r\n']))
        if not self.persistent:
            requestLines.append('Connection: close\r\n')
        if TEorCL is not None:
            requestLines.append(TEorCL)
        for name, values in self.headers.getAllRawHeaders():
            requestLines.extend([ name + ': ' + v + '\r\n' for v in values ])

        requestLines.append('\r\n')
        transport.writeSequence(requestLines)
        return

    def _writeToChunked(self, transport):
        self._writeHeaders(transport, 'Transfer-Encoding: chunked\r\n')
        encoder = ChunkedEncoder(transport)
        encoder.registerProducer(self.bodyProducer, True)
        d = self.bodyProducer.startProducing(encoder)

        def cbProduced(ignored):
            encoder.unregisterProducer()

        def ebProduced(err):
            encoder._allowNoMoreWrites()
            transport.unregisterProducer()
            return err

        d.addCallbacks(cbProduced, ebProduced)
        return d

    def _writeToContentLength(self, transport):
        self._writeHeaders(transport, networkString('Content-Length: %d\r\n' % (self.bodyProducer.length,)))
        finishedConsuming = Deferred()
        encoder = LengthEnforcingConsumer(self.bodyProducer, transport, finishedConsuming)
        transport.registerProducer(self.bodyProducer, True)
        finishedProducing = self.bodyProducer.startProducing(encoder)

        def combine(consuming, producing):

            def cancelConsuming(ign):
                finishedProducing.cancel()

            ultimate = Deferred(cancelConsuming)
            state = [
             None]

            def ebConsuming(err):
                if state == [None]:
                    state[0] = 1
                    ultimate.errback(err)
                else:
                    log.err(err, 'Buggy state machine in %r/[%d]: ebConsuming called' % (
                     self, state[0]))
                return

            def cbProducing(result):
                if state == [None]:
                    state[0] = 2
                    try:
                        encoder._noMoreWritesExpected()
                    except:
                        ultimate.errback()
                    else:
                        ultimate.callback(None)

                return

            def ebProducing(err):
                if state == [None]:
                    state[0] = 3
                    encoder._allowNoMoreWrites()
                    ultimate.errback(err)
                else:
                    log.err(err, 'Producer is buggy')
                return

            consuming.addErrback(ebConsuming)
            producing.addCallbacks(cbProducing, ebProducing)
            return ultimate

        d = combine(finishedConsuming, finishedProducing)

        def f(passthrough):
            transport.unregisterProducer()
            return passthrough

        d.addBoth(f)
        return d

    def writeTo(self, transport):
        if self.bodyProducer is not None:
            if self.bodyProducer.length is UNKNOWN_LENGTH:
                return self._writeToChunked(transport)
            else:
                return self._writeToContentLength(transport)

        else:
            self._writeHeaders(transport, None)
            return succeed(None)
        return

    def stopWriting(self):
        _callAppFunction(self.bodyProducer.stopProducing)


class LengthEnforcingConsumer():

    def __init__(self, producer, consumer, finished):
        self._length = producer.length
        self._producer = producer
        self._consumer = consumer
        self._finished = finished

    def _allowNoMoreWrites(self):
        self._finished = None
        return

    def write(self, bytes):
        if self._finished is None:
            self._producer.stopProducing()
            raise ExcessWrite()
        if len(bytes) <= self._length:
            self._length -= len(bytes)
            self._consumer.write(bytes)
        else:
            _callAppFunction(self._producer.stopProducing)
            self._finished.errback(WrongBodyLength('too many bytes written'))
            self._allowNoMoreWrites()
        return

    def _noMoreWritesExpected(self):
        if self._finished is not None:
            self._allowNoMoreWrites()
            if self._length:
                raise WrongBodyLength('too few bytes written')
        return


def makeStatefulDispatcher(name, template):

    def dispatcher(self, *args, **kwargs):
        func = getattr(self, '_' + name + '_' + self._state, None)
        if func is None:
            raise RuntimeError('%r has no %s method in state %s' % (self, name, self._state))
        return func(*args, **kwargs)

    dispatcher.__doc__ = template.__doc__
    return dispatcher


@implementer(IResponse)
class Response():
    length = UNKNOWN_LENGTH
    _bodyProtocol = None
    _bodyFinished = False

    def __init__(self, version, code, phrase, headers, _transport):
        self.version = version
        self.code = code
        self.phrase = phrase
        self.headers = headers
        self._transport = _transport
        self._bodyBuffer = []
        self._state = 'INITIAL'
        self.request = None
        self.previousResponse = None
        return

    @classmethod
    def _construct(cls, version, code, phrase, headers, _transport, request):
        response = Response(version, code, phrase, headers, _transport)
        response.request = proxyForInterface(IClientRequest)(request)
        return response

    def setPreviousResponse(self, previousResponse):
        self.previousResponse = previousResponse

    def deliverBody(self, protocol):
        pass

    deliverBody = makeStatefulDispatcher('deliverBody', deliverBody)

    def _deliverBody_INITIAL(self, protocol):
        self._transport.resumeProducing()
        protocol.makeConnection(self._transport)
        self._bodyProtocol = protocol
        for data in self._bodyBuffer:
            self._bodyProtocol.dataReceived(data)

        self._bodyBuffer = None
        self._state = 'CONNECTED'
        return

    def _deliverBody_CONNECTED(self, protocol):
        raise RuntimeError('Response already has protocol %r, cannot deliverBody again' % (
         self._bodyProtocol,))

    def _deliverBody_DEFERRED_CLOSE(self, protocol):
        protocol.makeConnection(self._transport)
        for data in self._bodyBuffer:
            protocol.dataReceived(data)

        self._bodyBuffer = None
        protocol.connectionLost(self._reason)
        self._state = 'FINISHED'
        return

    def _deliverBody_FINISHED(self, protocol):
        raise RuntimeError('Response already finished, cannot deliverBody now.')

    def _bodyDataReceived(self, data):
        pass

    _bodyDataReceived = makeStatefulDispatcher('bodyDataReceived', _bodyDataReceived)

    def _bodyDataReceived_INITIAL(self, data):
        self._bodyBuffer.append(data)

    def _bodyDataReceived_CONNECTED(self, data):
        self._bodyProtocol.dataReceived(data)

    def _bodyDataReceived_DEFERRED_CLOSE(self, data):
        raise RuntimeError('Cannot receive body data after _bodyDataFinished')

    def _bodyDataReceived_FINISHED(self, data):
        raise RuntimeError('Cannot receive body data after protocol disconnected')

    def _bodyDataFinished(self, reason=None):
        pass

    _bodyDataFinished = makeStatefulDispatcher('bodyDataFinished', _bodyDataFinished)

    def _bodyDataFinished_INITIAL(self, reason=None):
        self._state = 'DEFERRED_CLOSE'
        if reason is None:
            reason = Failure(ResponseDone('Response body fully received'))
        self._reason = reason
        return

    def _bodyDataFinished_CONNECTED(self, reason=None):
        if reason is None:
            reason = Failure(ResponseDone('Response body fully received'))
        self._bodyProtocol.connectionLost(reason)
        self._bodyProtocol = None
        self._state = 'FINISHED'
        return

    def _bodyDataFinished_DEFERRED_CLOSE(self):
        raise RuntimeError('Cannot finish body data more than once')

    def _bodyDataFinished_FINISHED(self):
        raise RuntimeError('Cannot finish body data after protocol disconnected')


@implementer(IConsumer)
class ChunkedEncoder():

    def __init__(self, transport):
        self.transport = transport

    def _allowNoMoreWrites(self):
        self.transport = None
        return

    def registerProducer(self, producer, streaming):
        self.transport.registerProducer(producer, streaming)

    def write(self, data):
        if self.transport is None:
            raise ExcessWrite()
        self.transport.writeSequence((networkString('%x\r\n' % len(data)),
         data, '\r\n'))
        return

    def unregisterProducer(self):
        self.write('')
        self.transport.unregisterProducer()
        self._allowNoMoreWrites()


@implementer(IPushProducer)
class TransportProxyProducer():
    disconnecting = False

    def __init__(self, producer):
        self._producer = producer

    def _stopProxying(self):
        self._producer = None
        return

    def stopProducing(self):
        if self._producer is not None:
            self._producer.stopProducing()
        return

    def resumeProducing(self):
        if self._producer is not None:
            self._producer.resumeProducing()
        return

    def pauseProducing(self):
        if self._producer is not None:
            self._producer.pauseProducing()
        return


class HTTP11ClientProtocol(Protocol):
    _state = 'QUIESCENT'
    _parser = None
    _finishedRequest = None
    _currentRequest = None
    _transportProxy = None
    _responseDeferred = None

    def __init__(self, quiescentCallback=(lambda c: None)):
        self._quiescentCallback = quiescentCallback
        self._abortDeferreds = []

    @property
    def state(self):
        return self._state

    def request(self, request):
        if self._state != 'QUIESCENT':
            return fail(RequestNotSent())
        self._state = 'TRANSMITTING'
        _requestDeferred = maybeDeferred(request.writeTo, self.transport)

        def cancelRequest(ign):
            if self._state in ('TRANSMITTING', 'TRANSMITTING_AFTER_RECEIVING_RESPONSE'):
                _requestDeferred.cancel()
            else:
                self.transport.abortConnection()
                self._disconnectParser(Failure(CancelledError()))

        self._finishedRequest = Deferred(cancelRequest)
        self._currentRequest = request
        self._transportProxy = TransportProxyProducer(self.transport)
        self._parser = HTTPClientParser(request, self._finishResponse)
        self._parser.makeConnection(self._transportProxy)
        self._responseDeferred = self._parser._responseDeferred

        def cbRequestWritten(ignored):
            if self._state == 'TRANSMITTING':
                self._state = 'WAITING'
                self._responseDeferred.chainDeferred(self._finishedRequest)

        def ebRequestWriting(err):
            if self._state == 'TRANSMITTING':
                self._state = 'GENERATION_FAILED'
                self.transport.abortConnection()
                self._finishedRequest.errback(Failure(RequestGenerationFailed([err])))
            else:
                log.err(err, 'Error writing request, but not in valid state to finalize request: %s' % self._state)

        _requestDeferred.addCallbacks(cbRequestWritten, ebRequestWriting)
        return self._finishedRequest

    def _finishResponse(self, rest):
        pass

    _finishResponse = makeStatefulDispatcher('finishResponse', _finishResponse)

    def _finishResponse_WAITING(self, rest):
        if self._state == 'WAITING':
            self._state = 'QUIESCENT'
        else:
            self._state = 'TRANSMITTING_AFTER_RECEIVING_RESPONSE'
            self._responseDeferred.chainDeferred(self._finishedRequest)
        if self._parser is None:
            return
        else:
            reason = ConnectionDone('synthetic!')
            connHeaders = self._parser.connHeaders.getRawHeaders('connection', ())
            if 'close' in connHeaders or self._state != 'QUIESCENT' or not self._currentRequest.persistent:
                self._giveUp(Failure(reason))
            else:
                self.transport.resumeProducing()
                try:
                    self._quiescentCallback(self)
                except:
                    log.err()
                    self.transport.loseConnection()

                self._disconnectParser(reason)
            return

    _finishResponse_TRANSMITTING = _finishResponse_WAITING

    def _disconnectParser(self, reason):
        if self._parser is not None:
            parser = self._parser
            self._parser = None
            self._currentRequest = None
            self._finishedRequest = None
            self._responseDeferred = None
            self._transportProxy._stopProxying()
            self._transportProxy = None
            parser.connectionLost(reason)
        return

    def _giveUp(self, reason):
        self.transport.loseConnection()
        self._disconnectParser(reason)

    def dataReceived(self, bytes):
        try:
            self._parser.dataReceived(bytes)
        except:
            self._giveUp(Failure())

    def connectionLost(self, reason):
        pass

    connectionLost = makeStatefulDispatcher('connectionLost', connectionLost)

    def _connectionLost_QUIESCENT(self, reason):
        self._state = 'CONNECTION_LOST'

    def _connectionLost_GENERATION_FAILED(self, reason):
        self._state = 'CONNECTION_LOST'

    def _connectionLost_TRANSMITTING(self, reason):
        self._state = 'CONNECTION_LOST'
        self._finishedRequest.errback(Failure(RequestTransmissionFailed([reason])))
        del self._finishedRequest
        self._currentRequest.stopWriting()

    def _connectionLost_TRANSMITTING_AFTER_RECEIVING_RESPONSE(self, reason):
        self._state = 'CONNECTION_LOST'

    def _connectionLost_WAITING(self, reason):
        self._disconnectParser(reason)
        self._state = 'CONNECTION_LOST'

    def _connectionLost_ABORTING(self, reason):
        self._disconnectParser(Failure(ConnectionAborted()))
        self._state = 'CONNECTION_LOST'
        for d in self._abortDeferreds:
            d.callback(None)

        self._abortDeferreds = []
        return

    def abort(self):
        if self._state == 'CONNECTION_LOST':
            return succeed(None)
        else:
            self.transport.loseConnection()
            self._state = 'ABORTING'
            d = Deferred()
            self._abortDeferreds.append(d)
            return d
# okay decompiling out\twisted.web._newclient.pyc
