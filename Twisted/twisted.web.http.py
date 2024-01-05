# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.http
from __future__ import division, absolute_import
__all__ = [
 'SWITCHING', 'OK', 'CREATED', 'ACCEPTED', 'NON_AUTHORITATIVE_INFORMATION', 
 'NO_CONTENT', 
 'RESET_CONTENT', 'PARTIAL_CONTENT', 'MULTI_STATUS', 
 'MULTIPLE_CHOICE', 
 'MOVED_PERMANENTLY', 'FOUND', 'SEE_OTHER', 
 'NOT_MODIFIED', 'USE_PROXY', 
 'TEMPORARY_REDIRECT', 
 'BAD_REQUEST', 'UNAUTHORIZED', 'PAYMENT_REQUIRED', 
 'FORBIDDEN', 'NOT_FOUND', 
 'NOT_ALLOWED', 'NOT_ACCEPTABLE', 'PROXY_AUTH_REQUIRED', 
 'REQUEST_TIMEOUT', 
 'CONFLICT', 'GONE', 'LENGTH_REQUIRED', 'PRECONDITION_FAILED', 
 'REQUEST_ENTITY_TOO_LARGE', 
 'REQUEST_URI_TOO_LONG', 
 'UNSUPPORTED_MEDIA_TYPE', 'REQUESTED_RANGE_NOT_SATISFIABLE', 
 'EXPECTATION_FAILED', 
 'INTERNAL_SERVER_ERROR', 
 'NOT_IMPLEMENTED', 'BAD_GATEWAY', 
 'SERVICE_UNAVAILABLE', 'GATEWAY_TIMEOUT', 
 'HTTP_VERSION_NOT_SUPPORTED', 
 'INSUFFICIENT_STORAGE_SPACE', 'NOT_EXTENDED', 
 'RESPONSES', 
 'CACHED', 
 'urlparse', 'parse_qs', 'datetimeToString', 'datetimeToLogString', 
 'timegm', 
 'stringToDatetime', 'toChunk', 'fromChunk', 'parseContentRange', 
 'StringTransport', 
 'HTTPClient', 'NO_BODY_CODES', 'Request', 
 'PotentialDataLoss', 'HTTPChannel', 
 'HTTPFactory']
import tempfile, base64, binascii, cgi, math, time, calendar, warnings, os
from io import BytesIO as StringIO
try:
    from urlparse import ParseResult as ParseResultBytes, urlparse as _urlparse
    from urllib import unquote
    from cgi import parse_header as _parseHeader
except ImportError:
    from urllib.parse import ParseResultBytes, urlparse as _urlparse, unquote_to_bytes as unquote

    def _parseHeader(line):
        key, pdict = cgi.parse_header(line.decode('charmap'))
        return (key.encode('charmap'), pdict)


from zope.interface import implementer, provider
from twisted.python.compat import _PY3, unicode, intToBytes, networkString, nativeString
from twisted.python.deprecate import deprecated
from twisted.python import log
from twisted.python.versions import Version
from twisted.python.components import proxyForInterface
from twisted.internet import interfaces, reactor, protocol, address
from twisted.internet.defer import Deferred
from twisted.protocols import policies, basic
from twisted.web.iweb import IRequest, IAccessLogFormatter
from twisted.web.http_headers import _DictHeaders, Headers
from twisted.web._responses import SWITCHING, OK, CREATED, ACCEPTED, NON_AUTHORITATIVE_INFORMATION, NO_CONTENT, RESET_CONTENT, PARTIAL_CONTENT, MULTI_STATUS, MULTIPLE_CHOICE, MOVED_PERMANENTLY, FOUND, SEE_OTHER, NOT_MODIFIED, USE_PROXY, TEMPORARY_REDIRECT, BAD_REQUEST, UNAUTHORIZED, PAYMENT_REQUIRED, FORBIDDEN, NOT_FOUND, NOT_ALLOWED, NOT_ACCEPTABLE, PROXY_AUTH_REQUIRED, REQUEST_TIMEOUT, CONFLICT, GONE, LENGTH_REQUIRED, PRECONDITION_FAILED, REQUEST_ENTITY_TOO_LARGE, REQUEST_URI_TOO_LONG, UNSUPPORTED_MEDIA_TYPE, REQUESTED_RANGE_NOT_SATISFIABLE, EXPECTATION_FAILED, INTERNAL_SERVER_ERROR, NOT_IMPLEMENTED, BAD_GATEWAY, SERVICE_UNAVAILABLE, GATEWAY_TIMEOUT, HTTP_VERSION_NOT_SUPPORTED, INSUFFICIENT_STORAGE_SPACE, NOT_EXTENDED, RESPONSES
if _PY3:
    _intTypes = int
else:
    _intTypes = (
     int, long)
protocol_version = 'HTTP/1.1'
CACHED = 'Magic constant returned by http.Request methods to set cache\nvalidation headers when the request is conditional and the value fails\nthe condition.'
responses = RESPONSES
weekdayname = [
 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
monthname = ['None', 
 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
 'Jul', 'Aug', 'Sep', 
 'Oct', 'Nov', 'Dec']
weekdayname_lower = [ name.lower() for name in weekdayname ]
monthname_lower = [ name and name.lower() for name in monthname ]

def urlparse(url):
    if isinstance(url, unicode):
        raise TypeError('url must be bytes, not unicode')
    scheme, netloc, path, params, query, fragment = _urlparse(url)
    if isinstance(scheme, unicode):
        scheme = scheme.encode('ascii')
        netloc = netloc.encode('ascii')
        path = path.encode('ascii')
        query = query.encode('ascii')
        fragment = fragment.encode('ascii')
    return ParseResultBytes(scheme, netloc, path, params, query, fragment)


def parse_qs(qs, keep_blank_values=0, strict_parsing=0):
    d = {}
    items = [ s2 for s1 in qs.split('&') for s2 in s1.split(';') ]
    for item in items:
        try:
            k, v = item.split('=', 1)
        except ValueError:
            if strict_parsing:
                raise
            continue

        if v or keep_blank_values:
            k = unquote(k.replace('+', ' '))
            v = unquote(v.replace('+', ' '))
            if k in d:
                d[k].append(v)
            else:
                d[k] = [
                 v]

    return d


def datetimeToString(msSinceEpoch=None):
    if msSinceEpoch == None:
        msSinceEpoch = time.time()
    year, month, day, hh, mm, ss, wd, y, z = time.gmtime(msSinceEpoch)
    s = networkString('%s, %02d %3s %4d %02d:%02d:%02d GMT' % (
     weekdayname[wd],
     day, monthname[month], year,
     hh, mm, ss))
    return s


def datetimeToLogString(msSinceEpoch=None):
    if msSinceEpoch == None:
        msSinceEpoch = time.time()
    year, month, day, hh, mm, ss, wd, y, z = time.gmtime(msSinceEpoch)
    s = '[%02d/%3s/%4d:%02d:%02d:%02d +0000]' % (
     day, monthname[month], year,
     hh, mm, ss)
    return s


def timegm(year, month, day, hour, minute, second):
    EPOCH = 1970
    if year < EPOCH:
        raise ValueError('Years prior to %d not supported' % (EPOCH,))
    days = 365 * (year - EPOCH) + calendar.leapdays(EPOCH, year)
    for i in range(1, month):
        days = days + calendar.mdays[i]

    if month > 2 and calendar.isleap(year):
        days = days + 1
    days = days + day - 1
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    seconds = minutes * 60 + second
    return seconds


def stringToDatetime(dateString):
    parts = nativeString(dateString).split()
    if parts[0][0:3].lower() not in weekdayname_lower:
        try:
            return stringToDatetime('Sun, ' + dateString)
        except ValueError:
            pass

    partlen = len(parts)
    if (partlen == 5 or partlen == 6) and parts[1].isdigit():
        day = parts[1]
        month = parts[2]
        year = parts[3]
        time = parts[4]
    elif (partlen == 3 or partlen == 4) and parts[1].find('-') != -1:
        day, month, year = parts[1].split('-')
        time = parts[2]
        year = int(year)
        if year < 69:
            year = year + 2000
        elif year < 100:
            year = year + 1900
    elif len(parts) == 5:
        day = parts[2]
        month = parts[1]
        year = parts[4]
        time = parts[3]
    else:
        raise ValueError('Unknown datetime format %r' % dateString)
    day = int(day)
    month = int(monthname_lower.index(month.lower()))
    year = int(year)
    hour, min, sec = map(int, time.split(':'))
    return int(timegm(year, month, day, hour, min, sec))


def toChunk(data):
    return (
     networkString('%x' % (len(data),)), '\r\n', data, '\r\n')


def fromChunk(data):
    prefix, rest = data.split('\r\n', 1)
    length = int(prefix, 16)
    if length < 0:
        raise ValueError('Chunk length must be >= 0, not %d' % (length,))
    if rest[length:length + 2] != '\r\n':
        raise ValueError('chunk must end with CRLF')
    return (
     rest[:length], rest[length + 2:])


def parseContentRange(header):
    kind, other = header.strip().split()
    if kind.lower() != 'bytes':
        raise ValueError('a range of type %r is not supported')
    startend, realLength = other.split('/')
    start, end = map(int, startend.split('-'))
    if realLength == '*':
        realLength = None
    else:
        realLength = int(realLength)
    return (
     start, end, realLength)


class StringTransport():

    def __init__(self):
        self.s = StringIO()

    def writeSequence(self, seq):
        self.s.write(('').join(seq))

    def __getattr__(self, attr):
        return getattr(self.__dict__['s'], attr)


class HTTPClient(basic.LineReceiver):
    length = None
    firstLine = True
    __buffer = None
    _header = ''

    def sendCommand(self, command, path):
        self.transport.writeSequence([command, ' ', path, ' HTTP/1.0\r\n'])

    def sendHeader(self, name, value):
        if not isinstance(value, bytes):
            value = networkString(str(value))
        self.transport.writeSequence([name, ': ', value, '\r\n'])

    def endHeaders(self):
        self.transport.write('\r\n')

    def extractHeader(self, header):
        key, val = header.split(':', 1)
        val = val.lstrip()
        self.handleHeader(key, val)
        if key.lower() == 'content-length':
            self.length = int(val)

    def lineReceived(self, line):
        if self.firstLine:
            self.firstLine = False
            l = line.split(None, 2)
            version = l[0]
            status = l[1]
            try:
                message = l[2]
            except IndexError:
                message = ''

            self.handleStatus(version, status, message)
            return
        else:
            if not line:
                if self._header != '':
                    self.extractHeader(self._header)
                self.__buffer = StringIO()
                self.handleEndHeaders()
                self.setRawMode()
                return
            if line.startswith('\t') or line.startswith(' '):
                self._header = self._header + line
            elif self._header:
                self.extractHeader(self._header)
                self._header = line
            else:
                self._header = line
            return

    def connectionLost(self, reason):
        self.handleResponseEnd()

    def handleResponseEnd(self):
        if self.__buffer is not None:
            b = self.__buffer.getvalue()
            self.__buffer = None
            self.handleResponse(b)
        return

    def handleResponsePart(self, data):
        self.__buffer.write(data)

    def connectionMade(self):
        pass

    def handleStatus(self, version, status, message):
        pass

    def handleHeader(self, key, val):
        pass

    def handleEndHeaders(self):
        pass

    def rawDataReceived(self, data):
        if self.length is not None:
            data, rest = data[:self.length], data[self.length:]
            self.length -= len(data)
        else:
            rest = ''
        self.handleResponsePart(data)
        if self.length == 0:
            self.handleResponseEnd()
            self.setLineMode(rest)
        return


NO_BODY_CODES = (
 204, 304)

@implementer(interfaces.IConsumer)
class Request():
    producer = None
    finished = 0
    code = OK
    code_message = RESPONSES[OK]
    method = '(no method yet)'
    clientproto = '(no clientproto yet)'
    uri = '(no uri yet)'
    startedWriting = 0
    chunked = 0
    sentLength = 0
    etag = None
    lastModified = None
    args = None
    path = None
    content = None
    _forceSSL = 0
    _disconnected = False

    def __init__(self, channel, queued):
        self.notifications = []
        self.channel = channel
        self.queued = queued
        self.requestHeaders = Headers()
        self.received_cookies = {}
        self.responseHeaders = Headers()
        self.cookies = []
        if queued:
            self.transport = StringTransport()
        else:
            self.transport = self.channel.transport

    def _warnHeaders(self, old, new):
        warnings.warn(category=DeprecationWarning, message='twisted.web.http.Request.%(old)s was deprecated in Twisted 13.2.0: Please use twisted.web.http.Request.%(new)s instead.' % dict(old=old, new=new), stacklevel=3)

    @property
    def headers(self):
        self._warnHeaders('headers', 'responseHeaders')
        return _DictHeaders(self.responseHeaders)

    @property
    def received_headers(self):
        self._warnHeaders('received_headers', 'requestHeaders')
        return _DictHeaders(self.requestHeaders)

    def __setattr__(self, name, value):
        if name == 'received_headers':
            self.requestHeaders = headers = Headers()
            for k, v in value.items():
                headers.setRawHeaders(k, [v])

            self._warnHeaders('received_headers', 'requestHeaders')
        elif name == 'headers':
            self.responseHeaders = headers = Headers()
            for k, v in value.items():
                headers.setRawHeaders(k, [v])

            self._warnHeaders('headers', 'responseHeaders')
        else:
            self.__dict__[name] = value

    def _cleanup(self):
        if self.producer:
            log.err(RuntimeError('Producer was not unregistered for %s' % self.uri))
            self.unregisterProducer()
        self.channel.requestDone(self)
        del self.channel
        try:
            self.content.close()
        except OSError:
            pass

        del self.content
        for d in self.notifications:
            d.callback(None)

        self.notifications = []
        return

    def noLongerQueued(self):
        if not self.queued:
            raise RuntimeError('noLongerQueued() got called unnecessarily.')
        self.queued = 0
        data = self.transport.getvalue()
        self.transport = self.channel.transport
        if data:
            self.transport.write(data)
        if self.producer is not None and not self.finished:
            self.transport.registerProducer(self.producer, self.streamingProducer)
        if self.finished:
            self._cleanup()
        return

    def gotLength(self, length):
        if length is not None and length < 100000:
            self.content = StringIO()
        else:
            self.content = tempfile.TemporaryFile()
        return

    def parseCookies(self):
        cookieheaders = self.requestHeaders.getRawHeaders('cookie')
        if cookieheaders is None:
            return
        else:
            for cookietxt in cookieheaders:
                if cookietxt:
                    for cook in cookietxt.split(';'):
                        cook = cook.lstrip()
                        try:
                            k, v = cook.split('=', 1)
                            self.received_cookies[k] = v
                        except ValueError:
                            pass

            return

    def handleContentChunk(self, data):
        self.content.write(data)

    def requestReceived(self, command, path, version):
        self.content.seek(0, 0)
        self.args = {}
        self.method, self.uri = command, path
        self.clientproto = version
        x = self.uri.split('?', 1)
        if len(x) == 1:
            self.path = self.uri
        else:
            self.path, argstring = x
            self.args = parse_qs(argstring, 1)
        self.client = self.channel.transport.getPeer()
        self.host = self.channel.transport.getHost()
        args = self.args
        ctype = self.requestHeaders.getRawHeaders('content-type')
        if ctype is not None:
            ctype = ctype[0]
        if self.method == 'POST' and ctype:
            mfd = 'multipart/form-data'
            key, pdict = _parseHeader(ctype)
            if key == 'application/x-www-form-urlencoded':
                args.update(parse_qs(self.content.read(), 1))
            elif key == mfd:
                try:
                    args.update(cgi.parse_multipart(self.content, pdict))
                except KeyError as e:
                    if e.args[0] == 'content-disposition':
                        _respondToBadRequestAndDisconnect(self.channel.transport)
                        return
                    raise

            self.content.seek(0, 0)
        self.process()
        return

    def __repr__(self):
        return '<%s at 0x%x method=%s uri=%s clientproto=%s>' % (
         self.__class__.__name__,
         id(self),
         nativeString(self.method),
         nativeString(self.uri),
         nativeString(self.clientproto))

    def process(self):
        pass

    def registerProducer(self, producer, streaming):
        if self.producer:
            raise ValueError('registering producer %s before previous one (%s) was unregistered' % (
             producer, self.producer))
        self.streamingProducer = streaming
        self.producer = producer
        if self.queued:
            if streaming:
                producer.pauseProducing()
        else:
            self.transport.registerProducer(producer, streaming)

    def unregisterProducer(self):
        if not self.queued:
            self.transport.unregisterProducer()
        self.producer = None
        return

    def getHeader(self, key):
        value = self.requestHeaders.getRawHeaders(key)
        if value is not None:
            return value[-1]
        else:
            return

    def getCookie(self, key):
        return self.received_cookies.get(key)

    def notifyFinish(self):
        self.notifications.append(Deferred())
        return self.notifications[-1]

    def finish(self):
        if self._disconnected:
            raise RuntimeError('Request.finish called on a request after its connection was lost; use Request.notifyFinish to keep track of this.')
        if self.finished:
            warnings.warn('Warning! request.finish called twice.', stacklevel=2)
            return
        if not self.startedWriting:
            self.write('')
        if self.chunked:
            self.transport.write('0\r\n\r\n')
        if hasattr(self.channel, 'factory'):
            self.channel.factory.log(self)
        self.finished = 1
        if not self.queued:
            self._cleanup()

    def write(self, data):
        if self.finished:
            raise RuntimeError('Request.write called on a request after Request.finish was called.')
        if not self.startedWriting:
            self.startedWriting = 1
            version = self.clientproto
            l = []
            l.append(version + ' ' + intToBytes(self.code) + ' ' + self.code_message + '\r\n')
            if version == 'HTTP/1.1' and self.responseHeaders.getRawHeaders('content-length') is None and self.method != 'HEAD' and self.code not in NO_BODY_CODES:
                l.append('Transfer-Encoding: chunked\r\n')
                self.chunked = 1
            if self.lastModified is not None:
                if self.responseHeaders.hasHeader('last-modified'):
                    log.msg('Warning: last-modified specified both in header list and lastModified attribute.')
                else:
                    self.responseHeaders.setRawHeaders('last-modified', [
                     datetimeToString(self.lastModified)])
            if self.etag is not None:
                self.responseHeaders.setRawHeaders('ETag', [self.etag])
            for name, values in self.responseHeaders.getAllRawHeaders():
                for value in values:
                    if not isinstance(value, bytes):
                        warnings.warn('Passing non-bytes header values is deprecated since Twisted 12.3. Pass only bytes instead.', category=DeprecationWarning, stacklevel=2)
                        value = networkString('%s' % (value,))
                    l.extend([name, ': ', value, '\r\n'])

            for cookie in self.cookies:
                l.append(networkString('Set-Cookie: %s\r\n' % (cookie,)))

            l.append('\r\n')
            self.transport.writeSequence(l)
            if self.method == 'HEAD':
                self.write = lambda data: None
                return
            if self.code in NO_BODY_CODES:
                self.write = lambda data: None
                return
        self.sentLength = self.sentLength + len(data)
        if data:
            if self.chunked:
                self.transport.writeSequence(toChunk(data))
            else:
                self.transport.write(data)
        return

    def addCookie(self, k, v, expires=None, domain=None, path=None, max_age=None, comment=None, secure=None):
        cookie = '%s=%s' % (k, v)
        if expires is not None:
            cookie = cookie + '; Expires=%s' % expires
        if domain is not None:
            cookie = cookie + '; Domain=%s' % domain
        if path is not None:
            cookie = cookie + '; Path=%s' % path
        if max_age is not None:
            cookie = cookie + '; Max-Age=%s' % max_age
        if comment is not None:
            cookie = cookie + '; Comment=%s' % comment
        if secure:
            cookie = cookie + '; Secure'
        self.cookies.append(cookie)
        return

    def setResponseCode(self, code, message=None):
        if not isinstance(code, _intTypes):
            raise TypeError('HTTP response code must be int or long')
        self.code = code
        if message:
            if not isinstance(message, bytes):
                raise TypeError('HTTP response status message must be bytes')
            self.code_message = message
        else:
            self.code_message = RESPONSES.get(code, 'Unknown Status')

    def setHeader(self, name, value):
        self.responseHeaders.setRawHeaders(name, [value])

    def redirect(self, url):
        self.setResponseCode(FOUND)
        self.setHeader('location', url)

    def setLastModified(self, when):
        when = int(math.ceil(when))
        if not self.lastModified or self.lastModified < when:
            self.lastModified = when
        modifiedSince = self.getHeader('if-modified-since')
        if modifiedSince:
            firstPart = modifiedSince.split(';', 1)[0]
            try:
                modifiedSince = stringToDatetime(firstPart)
            except ValueError:
                return

            if modifiedSince >= when:
                self.setResponseCode(NOT_MODIFIED)
                return CACHED
        return

    def setETag(self, etag):
        if etag:
            self.etag = etag
        tags = self.getHeader('if-none-match')
        if tags:
            tags = tags.split()
            if etag in tags or '*' in tags:
                self.setResponseCode(self.method in ('HEAD', 'GET') and NOT_MODIFIED or PRECONDITION_FAILED)
                return CACHED
        return

    def getAllHeaders(self):
        headers = {}
        for k, v in self.requestHeaders.getAllRawHeaders():
            headers[k.lower()] = v[-1]

        return headers

    def getRequestHostname(self):
        host = self.getHeader('host')
        if host:
            return host.split(':', 1)[0]
        return networkString(self.getHost().host)

    def getHost(self):
        return self.host

    def setHost(self, host, port, ssl=0):
        self._forceSSL = ssl
        if self.isSecure():
            default = 443
        else:
            default = 80
        if port == default:
            hostHeader = host
        else:
            hostHeader = host + ':' + intToBytes(port)
        self.requestHeaders.setRawHeaders('host', [hostHeader])
        self.host = address.IPv4Address('TCP', host, port)

    def getClientIP(self):
        if isinstance(self.client, address.IPv4Address):
            return self.client.host
        else:
            return
            return

    def isSecure(self):
        if self._forceSSL:
            return True
        else:
            transport = getattr(getattr(self, 'channel', None), 'transport', None)
            if interfaces.ISSLTransport(transport, None) is not None:
                return True
            return False

    def _authorize(self):
        try:
            authh = self.getHeader('Authorization')
            if not authh:
                self.user = self.password = ''
                return
            bas, upw = authh.split()
            if bas.lower() != 'basic':
                raise ValueError()
            upw = base64.decodestring(upw)
            self.user, self.password = upw.split(':', 1)
        except (binascii.Error, ValueError):
            self.user = self.password = ''
        except:
            log.err()
            self.user = self.password = ''

    def getUser(self):
        try:
            return self.user
        except:
            pass

        self._authorize()
        return self.user

    def getPassword(self):
        try:
            return self.password
        except:
            pass

        self._authorize()
        return self.password

    def getClient(self):
        return self.getClientIP()

    def connectionLost(self, reason):
        self._disconnected = True
        self.channel = None
        if self.content is not None:
            self.content.close()
        for d in self.notifications:
            d.errback(reason)

        self.notifications = []
        return


Request.getClient = deprecated(Version('Twisted', 15, 0, 0), 'Twisted Names to resolve hostnames')(Request.getClient)

class _DataLoss(Exception):
    pass


class PotentialDataLoss(Exception):
    pass


class _MalformedChunkedDataError(Exception):
    pass


class _IdentityTransferDecoder(object):

    def __init__(self, contentLength, dataCallback, finishCallback):
        self.contentLength = contentLength
        self.dataCallback = dataCallback
        self.finishCallback = finishCallback

    def dataReceived(self, data):
        if self.dataCallback is None:
            raise RuntimeError('_IdentityTransferDecoder cannot decode data after finishing')
        if self.contentLength is None:
            self.dataCallback(data)
        elif len(data) < self.contentLength:
            self.contentLength -= len(data)
            self.dataCallback(data)
        else:
            contentLength = self.contentLength
            dataCallback = self.dataCallback
            finishCallback = self.finishCallback
            self.dataCallback = self.finishCallback = None
            self.contentLength = 0
            dataCallback(data[:contentLength])
            finishCallback(data[contentLength:])
        return

    def noMoreData(self):
        finishCallback = self.finishCallback
        self.dataCallback = self.finishCallback = None
        if self.contentLength is None:
            finishCallback('')
            raise PotentialDataLoss()
        elif self.contentLength != 0:
            raise _DataLoss()
        return


class _ChunkedTransferDecoder(object):
    state = 'CHUNK_LENGTH'

    def __init__(self, dataCallback, finishCallback):
        self.dataCallback = dataCallback
        self.finishCallback = finishCallback
        self._buffer = ''

    def _dataReceived_CHUNK_LENGTH(self, data):
        if '\r\n' in data:
            line, rest = data.split('\r\n', 1)
            parts = line.split(';')
            try:
                self.length = int(parts[0], 16)
            except ValueError:
                raise _MalformedChunkedDataError('Chunk-size must be an integer.')

            if self.length == 0:
                self.state = 'TRAILER'
            else:
                self.state = 'BODY'
            return rest
        self._buffer = data
        return ''

    def _dataReceived_CRLF(self, data):
        if data.startswith('\r\n'):
            self.state = 'CHUNK_LENGTH'
            return data[2:]
        else:
            self._buffer = data
            return ''

    def _dataReceived_TRAILER(self, data):
        if data.startswith('\r\n'):
            data = data[2:]
            self.state = 'FINISHED'
            self.finishCallback(data)
        else:
            self._buffer = data
        return ''

    def _dataReceived_BODY(self, data):
        if len(data) >= self.length:
            chunk, data = data[:self.length], data[self.length:]
            self.dataCallback(chunk)
            self.state = 'CRLF'
            return data
        if len(data) < self.length:
            self.length -= len(data)
            self.dataCallback(data)
            return ''

    def _dataReceived_FINISHED(self, data):
        raise RuntimeError('_ChunkedTransferDecoder.dataReceived called after last chunk was processed')

    def dataReceived(self, data):
        data = self._buffer + data
        self._buffer = ''
        while data:
            data = getattr(self, '_dataReceived_%s' % (self.state,))(data)

    def noMoreData(self):
        if self.state != 'FINISHED':
            raise _DataLoss("Chunked decoder in %r state, still expecting more data to get to 'FINISHED' state." % (
             self.state,))


class HTTPChannel(basic.LineReceiver, policies.TimeoutMixin):
    maxHeaders = 500
    totalHeadersSize = 16384
    length = 0
    persistent = 1
    __header = ''
    __first_line = 1
    __content = None
    requestFactory = Request
    _savedTimeOut = None
    _receivedHeaderCount = 0
    _receivedHeaderSize = 0

    def __init__(self):
        self.requests = []
        self._transferDecoder = None
        return

    def connectionMade(self):
        self.setTimeout(self.timeOut)

    def lineReceived(self, line):
        self.resetTimeout()
        self._receivedHeaderSize += len(line)
        if self._receivedHeaderSize > self.totalHeadersSize:
            _respondToBadRequestAndDisconnect(self.transport)
            return
        if self.__first_line:
            if not self.persistent:
                self.dataReceived = self.lineReceived = lambda *args: None
                return
            if not line and self.__first_line == 1:
                self.__first_line = 2
                return
            request = self.requestFactory(self, len(self.requests))
            self.requests.append(request)
            self.__first_line = 0
            parts = line.split()
            if len(parts) != 3:
                _respondToBadRequestAndDisconnect(self.transport)
                return
            command, request, version = parts
            self._command = command
            self._path = request
            self._version = version
        elif line == '':
            if self.__header:
                self.headerReceived(self.__header)
            self.__header = ''
            self.allHeadersReceived()
            if self.length == 0:
                self.allContentReceived()
            else:
                self.setRawMode()
        elif line[0] in ' \t':
            self.__header = self.__header + '\n' + line
        else:
            if self.__header:
                self.headerReceived(self.__header)
            self.__header = line

    def _finishRequestBody(self, data):
        self.allContentReceived()
        self.setLineMode(data)

    def headerReceived(self, line):
        header, data = line.split(':', 1)
        header = header.lower()
        data = data.strip()
        if header == 'content-length':
            try:
                self.length = int(data)
            except ValueError:
                _respondToBadRequestAndDisconnect(self.transport)
                self.length = None
                return

            self._transferDecoder = _IdentityTransferDecoder(self.length, self.requests[-1].handleContentChunk, self._finishRequestBody)
        elif header == 'transfer-encoding' and data.lower() == 'chunked':
            self.length = None
            self._transferDecoder = _ChunkedTransferDecoder(self.requests[-1].handleContentChunk, self._finishRequestBody)
        reqHeaders = self.requests[-1].requestHeaders
        values = reqHeaders.getRawHeaders(header)
        if values is not None:
            values.append(data)
        else:
            reqHeaders.setRawHeaders(header, [data])
        self._receivedHeaderCount += 1
        if self._receivedHeaderCount > self.maxHeaders:
            _respondToBadRequestAndDisconnect(self.transport)
            return
        else:
            return

    def allContentReceived(self):
        command = self._command
        path = self._path
        version = self._version
        self.length = 0
        self._receivedHeaderCount = 0
        self._receivedHeaderSize = 0
        self.__first_line = 1
        self._transferDecoder = None
        del self._command
        del self._path
        del self._version
        if self.timeOut:
            self._savedTimeOut = self.setTimeout(None)
        req = self.requests[-1]
        req.requestReceived(command, path, version)
        return

    def rawDataReceived(self, data):
        self.resetTimeout()
        try:
            self._transferDecoder.dataReceived(data)
        except _MalformedChunkedDataError:
            _respondToBadRequestAndDisconnect(self.transport)

    def allHeadersReceived(self):
        req = self.requests[-1]
        req.parseCookies()
        self.persistent = self.checkPersistence(req, self._version)
        req.gotLength(self.length)
        expectContinue = req.requestHeaders.getRawHeaders('expect')
        if expectContinue and expectContinue[0].lower() == '100-continue' and self._version == 'HTTP/1.1':
            req.transport.write('HTTP/1.1 100 Continue\r\n\r\n')

    def checkPersistence(self, request, version):
        connection = request.requestHeaders.getRawHeaders('connection')
        if connection:
            tokens = [ t.lower() for t in connection[0].split(' ') ]
        else:
            tokens = []
        if version == 'HTTP/1.1':
            if 'close' in tokens:
                request.responseHeaders.setRawHeaders('connection', ['close'])
                return False
            else:
                return True

        else:
            return False

    def requestDone(self, request):
        if request != self.requests[0]:
            raise TypeError
        del self.requests[0]
        if self.persistent:
            if self.requests:
                self.requests[0].noLongerQueued()
            elif self._savedTimeOut:
                self.setTimeout(self._savedTimeOut)
        else:
            self.transport.loseConnection()

    def timeoutConnection(self):
        log.msg('Timing out client: %s' % str(self.transport.getPeer()))
        policies.TimeoutMixin.timeoutConnection(self)

    def connectionLost(self, reason):
        self.setTimeout(None)
        for request in self.requests:
            request.connectionLost(reason)

        return


def _respondToBadRequestAndDisconnect(transport):
    transport.write('HTTP/1.1 400 Bad Request\r\n\r\n')
    transport.loseConnection()


def _escape(s):
    if not isinstance(s, bytes):
        s = s.encode('ascii')
    r = repr(s)
    if not isinstance(r, unicode):
        r = r.decode('ascii')
    if r.startswith('b'):
        r = r[1:]
    if r.startswith("'"):
        return r[1:-1].replace('"', '\\"').replace("\\'", "'")
    return r[1:-1]


@provider(IAccessLogFormatter)
def combinedLogFormatter(timestamp, request):
    referrer = _escape(request.getHeader('referer') or '-')
    agent = _escape(request.getHeader('user-agent') or '-')
    line = '"%(ip)s" - - %(timestamp)s "%(method)s %(uri)s %(protocol)s" %(code)d %(length)s "%(referrer)s" "%(agent)s"' % dict(ip=_escape(request.getClientIP() or '-'), timestamp=timestamp, method=_escape(request.method), uri=_escape(request.uri), protocol=_escape(request.clientproto), code=request.code, length=request.sentLength or '-', referrer=referrer, agent=agent)
    return line


class _XForwardedForRequest(proxyForInterface(IRequest, '_request')):

    def getClientIP(self):
        return self._request.requestHeaders.getRawHeaders('x-forwarded-for', ['-'])[0].split(',')[0].strip()

    @property
    def clientproto(self):
        return self._request.clientproto

    @property
    def code(self):
        return self._request.code

    @property
    def sentLength(self):
        return self._request.sentLength


@provider(IAccessLogFormatter)
def proxiedLogFormatter(timestamp, request):
    return combinedLogFormatter(timestamp, _XForwardedForRequest(request))


class HTTPFactory(protocol.ServerFactory):
    protocol = HTTPChannel
    logPath = None
    timeOut = 43200
    _reactor = reactor

    def __init__(self, logPath=None, timeout=43200, logFormatter=None):
        if logPath is not None:
            logPath = os.path.abspath(logPath)
        self.logPath = logPath
        self.timeOut = timeout
        if logFormatter is None:
            logFormatter = combinedLogFormatter
        self._logFormatter = logFormatter
        self._logDateTime = None
        self._logDateTimeCall = None
        return

    def _updateLogDateTime(self):
        self._logDateTime = datetimeToLogString(self._reactor.seconds())
        self._logDateTimeCall = self._reactor.callLater(1, self._updateLogDateTime)

    def buildProtocol(self, addr):
        p = protocol.ServerFactory.buildProtocol(self, addr)
        p.timeOut = self.timeOut
        return p

    def startFactory(self):
        if self._logDateTimeCall is None:
            self._updateLogDateTime()
        if self.logPath:
            self._nativeize = False
            self.logFile = self._openLogFile(self.logPath)
        else:
            self._nativeize = True
            self.logFile = log.logfile
        return

    def stopFactory(self):
        if hasattr(self, 'logFile'):
            if self.logFile != log.logfile:
                self.logFile.close()
            del self.logFile
        if self._logDateTimeCall is not None and self._logDateTimeCall.active():
            self._logDateTimeCall.cancel()
            self._logDateTimeCall = None
        return

    def _openLogFile(self, path):
        f = open(path, 'ab', 1)
        return f

    def log(self, request):
        try:
            logFile = self.logFile
        except AttributeError:
            pass
        else:
            line = self._logFormatter(self._logDateTime, request) + '\n'
            if self._nativeize:
                line = nativeString(line)
            else:
                line = line.encode('utf-8')
            logFile.write(line)
# okay decompiling out\twisted.web.http.pyc
