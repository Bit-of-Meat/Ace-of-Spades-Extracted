# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.client
from __future__ import division, absolute_import
import os, types, warnings
try:
    from urlparse import urlunparse, urljoin, urldefrag
    from urllib import splithost, splittype
except ImportError:
    from urllib.parse import splithost, splittype, urljoin, urldefrag
    from urllib.parse import urlunparse as _urlunparse

    def urlunparse(parts):
        result = _urlunparse(tuple([ p.decode('charmap') for p in parts ]))
        return result.encode('charmap')


import zlib
from functools import wraps
from zope.interface import implementer
from twisted.python.compat import nativeString, intToBytes
from twisted.python import log
from twisted.python.failure import Failure
from twisted.python.deprecate import deprecatedModuleAttribute
from twisted.python.versions import Version
from twisted.web.iweb import IPolicyForHTTPS, IAgentEndpointFactory
from twisted.python.deprecate import getDeprecationWarningString
from twisted.web import http
from twisted.internet import defer, protocol, task, reactor
from twisted.internet.interfaces import IProtocol
from twisted.internet.endpoints import TCP4ClientEndpoint, SSL4ClientEndpoint
from twisted.python.util import InsensitiveDict
from twisted.python.components import proxyForInterface
from twisted.web import error
from twisted.web.iweb import UNKNOWN_LENGTH, IAgent, IBodyProducer, IResponse
from twisted.web.http_headers import Headers

class PartialDownloadError(error.Error):
    pass


class HTTPPageGetter(http.HTTPClient):
    quietLoss = 0
    followRedirect = True
    failed = 0
    _completelyDone = True
    _specialHeaders = set(('host', 'user-agent', 'cookie', 'content-length'))

    def connectionMade(self):
        method = getattr(self.factory, 'method', 'GET')
        self.sendCommand(method, self.factory.path)
        if self.factory.scheme == 'http' and self.factory.port != 80:
            host = self.factory.host + ':' + intToBytes(self.factory.port)
        else:
            if self.factory.scheme == 'https' and self.factory.port != 443:
                host = self.factory.host + ':' + intToBytes(self.factory.port)
            else:
                host = self.factory.host
            self.sendHeader('Host', self.factory.headers.get('host', host))
            self.sendHeader('User-Agent', self.factory.agent)
            data = getattr(self.factory, 'postdata', None)
            if data is not None:
                self.sendHeader('Content-Length', intToBytes(len(data)))
            cookieData = []
            for key, value in self.factory.headers.items():
                if key.lower() not in self._specialHeaders:
                    self.sendHeader(key, value)
                if key.lower() == 'cookie':
                    cookieData.append(value)

            for cookie, cookval in self.factory.cookies.items():
                cookieData.append(cookie + '=' + cookval)

        if cookieData:
            self.sendHeader('Cookie', ('; ').join(cookieData))
        self.endHeaders()
        self.headers = {}
        if data is not None:
            self.transport.write(data)
        return

    def handleHeader(self, key, value):
        key = key.lower()
        l = self.headers.setdefault(key, [])
        l.append(value)

    def handleStatus(self, version, status, message):
        self.version, self.status, self.message = version, status, message
        self.factory.gotStatus(version, status, message)

    def handleEndHeaders(self):
        self.factory.gotHeaders(self.headers)
        m = getattr(self, 'handleStatus_' + nativeString(self.status), self.handleStatusDefault)
        m()

    def handleStatus_200(self):
        pass

    handleStatus_201 = lambda self: self.handleStatus_200()
    handleStatus_202 = lambda self: self.handleStatus_200()

    def handleStatusDefault(self):
        self.failed = 1

    def handleStatus_301(self):
        l = self.headers.get('location')
        if not l:
            self.handleStatusDefault()
            return
        url = l[0]
        if self.followRedirect:
            self.factory._redirectCount += 1
            if self.factory._redirectCount >= self.factory.redirectLimit:
                err = error.InfiniteRedirection(self.status, 'Infinite redirection detected', location=url)
                self.factory.noPage(Failure(err))
                self.quietLoss = True
                self.transport.loseConnection()
                return
            self._completelyDone = False
            self.factory.setURL(url)
            if self.factory.scheme == 'https':
                from twisted.internet import ssl
                contextFactory = ssl.ClientContextFactory()
                reactor.connectSSL(nativeString(self.factory.host), self.factory.port, self.factory, contextFactory)
            else:
                reactor.connectTCP(nativeString(self.factory.host), self.factory.port, self.factory)
        else:
            self.handleStatusDefault()
            self.factory.noPage(Failure(error.PageRedirect(self.status, self.message, location=url)))
        self.quietLoss = True
        self.transport.loseConnection()

    def handleStatus_302(self):
        if self.afterFoundGet:
            self.handleStatus_303()
        else:
            self.handleStatus_301()

    def handleStatus_303(self):
        self.factory.method = 'GET'
        self.handleStatus_301()

    def connectionLost(self, reason):
        if not self.quietLoss:
            http.HTTPClient.connectionLost(self, reason)
            self.factory.noPage(reason)
        if self._completelyDone:
            self.factory._disconnectedDeferred.callback(None)
        return

    def handleResponse(self, response):
        if self.quietLoss:
            return
        else:
            if self.failed:
                self.factory.noPage(Failure(error.Error(self.status, self.message, response)))
            if self.factory.method == 'HEAD':
                self.factory.page('')
            elif self.length != None and self.length != 0:
                self.factory.noPage(Failure(PartialDownloadError(self.status, self.message, response)))
            else:
                self.factory.page(response)
            self.transport.loseConnection()
            return

    def timeout(self):
        self.quietLoss = True
        self.transport.loseConnection()
        self.factory.noPage(defer.TimeoutError('Getting %s took longer than %s seconds.' % (self.factory.url, self.factory.timeout)))


class HTTPPageDownloader(HTTPPageGetter):
    transmittingPage = 0

    def handleStatus_200(self, partialContent=0):
        HTTPPageGetter.handleStatus_200(self)
        self.transmittingPage = 1
        self.factory.pageStart(partialContent)

    def handleStatus_206(self):
        self.handleStatus_200(partialContent=1)

    def handleResponsePart(self, data):
        if self.transmittingPage:
            self.factory.pagePart(data)

    def handleResponseEnd(self):
        if self.length:
            self.transmittingPage = 0
            self.factory.noPage(Failure(PartialDownloadError(self.status)))
        if self.transmittingPage:
            self.factory.pageEnd()
            self.transmittingPage = 0
        if self.failed:
            self.factory.noPage(Failure(error.Error(self.status, self.message, None)))
            self.transport.loseConnection()
        return


class HTTPClientFactory(protocol.ClientFactory):
    protocol = HTTPPageGetter
    url = None
    scheme = None
    host = ''
    port = None
    path = None

    def __init__(self, url, method='GET', postdata=None, headers=None, agent='Twisted PageGetter', timeout=0, cookies=None, followRedirect=True, redirectLimit=20, afterFoundGet=False):
        self.followRedirect = followRedirect
        self.redirectLimit = redirectLimit
        self._redirectCount = 0
        self.timeout = timeout
        self.agent = agent
        self.afterFoundGet = afterFoundGet
        if cookies is None:
            cookies = {}
        self.cookies = cookies
        if headers is not None:
            self.headers = InsensitiveDict(headers)
        else:
            self.headers = InsensitiveDict()
        if postdata is not None:
            self.headers.setdefault('Content-Length', intToBytes(len(postdata)))
            self.headers.setdefault('connection', 'close')
        self.postdata = postdata
        self.method = method
        self.setURL(url)
        self.waiting = 1
        self._disconnectedDeferred = defer.Deferred()
        self.deferred = defer.Deferred()
        self.deferred.addBoth(self._waitForDisconnect)
        self.response_headers = None
        return

    def _waitForDisconnect(self, passthrough):
        self._disconnectedDeferred.addCallback((lambda ignored: passthrough))
        return self._disconnectedDeferred

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.url)

    def setURL(self, url):
        self.url = url
        uri = URI.fromBytes(url)
        if uri.scheme and uri.host:
            self.scheme = uri.scheme
            self.host = uri.host
            self.port = uri.port
        self.path = uri.originForm

    def buildProtocol(self, addr):
        p = protocol.ClientFactory.buildProtocol(self, addr)
        p.followRedirect = self.followRedirect
        p.afterFoundGet = self.afterFoundGet
        if self.timeout:
            timeoutCall = reactor.callLater(self.timeout, p.timeout)
            self.deferred.addBoth(self._cancelTimeout, timeoutCall)
        return p

    def _cancelTimeout(self, result, timeoutCall):
        if timeoutCall.active():
            timeoutCall.cancel()
        return result

    def gotHeaders(self, headers):
        self.response_headers = headers
        if 'set-cookie' in headers:
            for cookie in headers['set-cookie']:
                cookparts = cookie.split(';')
                cook = cookparts[0]
                cook.lstrip()
                k, v = cook.split('=', 1)
                self.cookies[k.lstrip()] = v.lstrip()

    def gotStatus(self, version, status, message):
        self.version, self.status, self.message = version, status, message

    def page(self, page):
        if self.waiting:
            self.waiting = 0
            self.deferred.callback(page)

    def noPage(self, reason):
        if self.waiting:
            self.waiting = 0
            self.deferred.errback(reason)

    def clientConnectionFailed(self, _, reason):
        if self.waiting:
            self.waiting = 0
            self._disconnectedDeferred.callback(None)
            self.deferred.errback(reason)
        return


class HTTPDownloader(HTTPClientFactory):
    protocol = HTTPPageDownloader
    value = None

    def __init__(self, url, fileOrName, method='GET', postdata=None, headers=None, agent='Twisted client', supportPartial=0, timeout=0, cookies=None, followRedirect=1, redirectLimit=20, afterFoundGet=False):
        self.requestedPartial = 0
        if isinstance(fileOrName, types.StringTypes):
            self.fileName = fileOrName
            self.file = None
            if supportPartial and os.path.exists(self.fileName):
                fileLength = os.path.getsize(self.fileName)
                if fileLength:
                    self.requestedPartial = fileLength
                    if headers == None:
                        headers = {}
                    headers['range'] = 'bytes=%d-' % fileLength
        else:
            self.file = fileOrName
        HTTPClientFactory.__init__(self, url, method=method, postdata=postdata, headers=headers, agent=agent, timeout=timeout, cookies=cookies, followRedirect=followRedirect, redirectLimit=redirectLimit, afterFoundGet=afterFoundGet)
        return

    def gotHeaders(self, headers):
        HTTPClientFactory.gotHeaders(self, headers)
        if self.requestedPartial:
            contentRange = headers.get('content-range', None)
            if not contentRange:
                self.requestedPartial = 0
                return
            start, end, realLength = http.parseContentRange(contentRange[0])
            if start != self.requestedPartial:
                self.requestedPartial = 0
        return

    def openFile(self, partialContent):
        if partialContent:
            file = open(self.fileName, 'rb+')
            file.seek(0, 2)
        else:
            file = open(self.fileName, 'wb')
        return file

    def pageStart(self, partialContent):
        if partialContent and not self.requestedPartial:
            raise ValueError("we shouldn't get partial content response if we didn't want it!")
        if self.waiting:
            try:
                if not self.file:
                    self.file = self.openFile(partialContent)
            except IOError:
                self.deferred.errback(Failure())

    def pagePart(self, data):
        if not self.file:
            return
        else:
            try:
                self.file.write(data)
            except IOError:
                self.file = None
                self.deferred.errback(Failure())

            return

    def noPage(self, reason):
        if self.waiting:
            self.waiting = 0
            if self.file:
                try:
                    self.file.close()
                except:
                    log.err(None, 'Error closing HTTPDownloader file')

            self.deferred.errback(reason)
        return

    def pageEnd(self):
        self.waiting = 0
        if not self.file:
            return
        try:
            self.file.close()
        except IOError:
            self.deferred.errback(Failure())
            return

        self.deferred.callback(self.value)


class URI(object):

    def __init__(self, scheme, netloc, host, port, path, params, query, fragment):
        self.scheme = scheme
        self.netloc = netloc
        self.host = host
        self.port = port
        self.path = path
        self.params = params
        self.query = query
        self.fragment = fragment

    @classmethod
    def fromBytes(cls, uri, defaultPort=None):
        uri = uri.strip()
        scheme, netloc, path, params, query, fragment = http.urlparse(uri)
        if defaultPort is None:
            if scheme == 'https':
                defaultPort = 443
            else:
                defaultPort = 80
        host, port = netloc, defaultPort
        if ':' in host:
            host, port = host.split(':')
            try:
                port = int(port)
            except ValueError:
                port = defaultPort

        return cls(scheme, netloc, host, port, path, params, query, fragment)

    def toBytes(self):
        return urlunparse((
         self.scheme, self.netloc, self.path, self.params, self.query,
         self.fragment))

    @property
    def originForm(self):
        path = urlunparse((
         '', '', self.path, self.params, self.query, ''))
        if path == '':
            path = '/'
        return path


def _urljoin(base, url):
    base, baseFrag = urldefrag(base)
    url, urlFrag = urldefrag(urljoin(base, url))
    return urljoin(url, '#' + (urlFrag or baseFrag))


def _makeGetterFactory(url, factoryFactory, contextFactory=None, *args, **kwargs):
    uri = URI.fromBytes(url)
    factory = factoryFactory(url, *args, **kwargs)
    if uri.scheme == 'https':
        from twisted.internet import ssl
        if contextFactory is None:
            contextFactory = ssl.ClientContextFactory()
        reactor.connectSSL(nativeString(uri.host), uri.port, factory, contextFactory)
    else:
        reactor.connectTCP(nativeString(uri.host), uri.port, factory)
    return factory


def getPage(url, contextFactory=None, *args, **kwargs):
    return _makeGetterFactory(url, HTTPClientFactory, contextFactory=contextFactory, *args, **kwargs).deferred


def downloadPage(url, file, contextFactory=None, *args, **kwargs):
    factoryFactory = lambda url, *a, **kw: HTTPDownloader(url, file, *a, **kw)
    return _makeGetterFactory(url, factoryFactory, contextFactory=contextFactory, *args, **kwargs).deferred


from twisted.web.error import SchemeNotSupported
from twisted.web._newclient import Request, Response, HTTP11ClientProtocol
from twisted.web._newclient import ResponseDone, ResponseFailed
from twisted.web._newclient import RequestNotSent, RequestTransmissionFailed
from twisted.web._newclient import ResponseNeverReceived, PotentialDataLoss, _WrapperException
try:
    from OpenSSL import SSL
except ImportError:
    SSL = None
else:
    from twisted.internet.ssl import CertificateOptions, platformTrust, optionsForClientTLS

def _requireSSL(decoratee):
    if SSL is None:

        @wraps(decoratee)
        def raiseNotImplemented(*a, **kw):
            raise NotImplementedError('SSL support unavailable')

        return raiseNotImplemented
    else:
        return decoratee


class WebClientContextFactory(object):

    def _getCertificateOptions(self, hostname, port):
        return CertificateOptions(method=SSL.SSLv23_METHOD, trustRoot=platformTrust())

    @_requireSSL
    def getContext(self, hostname, port):
        return self._getCertificateOptions(hostname, port).getContext()


@implementer(IPolicyForHTTPS)
class BrowserLikePolicyForHTTPS(object):

    def __init__(self, trustRoot=None):
        self._trustRoot = trustRoot

    @_requireSSL
    def creatorForNetloc(self, hostname, port):
        return optionsForClientTLS(hostname.decode('ascii'), trustRoot=self._trustRoot)


deprecatedModuleAttribute(Version('Twisted', 14, 0, 0), getDeprecationWarningString(WebClientContextFactory, Version('Twisted', 14, 0, 0), replacement=BrowserLikePolicyForHTTPS).split('; ')[1], WebClientContextFactory.__module__, WebClientContextFactory.__name__)

class _ContextFactoryWithContext(object):

    def __init__(self, context):
        self._context = context

    def getContext(self):
        return self._context


@implementer(IPolicyForHTTPS)
class _DeprecatedToCurrentPolicyForHTTPS(object):

    def __init__(self, webContextFactory):
        self._webContextFactory = webContextFactory

    def creatorForNetloc(self, hostname, port):
        context = self._webContextFactory.getContext(hostname, port)
        return _ContextFactoryWithContext(context)


@implementer(IBodyProducer)
class FileBodyProducer(object):

    def __init__(self, inputFile, cooperator=task, readSize=65536):
        self._inputFile = inputFile
        self._cooperate = cooperator.cooperate
        self._readSize = readSize
        self.length = self._determineLength(inputFile)

    def _determineLength(self, fObj):
        try:
            seek = fObj.seek
            tell = fObj.tell
        except AttributeError:
            return UNKNOWN_LENGTH

        originalPosition = tell()
        seek(0, os.SEEK_END)
        end = tell()
        seek(originalPosition, os.SEEK_SET)
        return end - originalPosition

    def stopProducing(self):
        self._inputFile.close()
        self._task.stop()

    def startProducing(self, consumer):
        self._task = self._cooperate(self._writeloop(consumer))
        d = self._task.whenDone()

        def maybeStopped(reason):
            reason.trap(task.TaskStopped)
            return defer.Deferred()

        d.addCallbacks((lambda ignored: None), maybeStopped)
        return d

    def _writeloop(self, consumer):
        while True:
            bytes = self._inputFile.read(self._readSize)
            if not bytes:
                self._inputFile.close()
                break
            consumer.write(bytes)
            yield

        return

    def pauseProducing(self):
        self._task.pause()

    def resumeProducing(self):
        self._task.resume()


class _HTTP11ClientFactory(protocol.Factory):

    def __init__(self, quiescentCallback):
        self._quiescentCallback = quiescentCallback

    def buildProtocol(self, addr):
        return HTTP11ClientProtocol(self._quiescentCallback)


class _RetryingHTTP11ClientProtocol(object):

    def __init__(self, clientProtocol, newConnection):
        self._clientProtocol = clientProtocol
        self._newConnection = newConnection

    def _shouldRetry(self, method, exception, bodyProducer):
        if method not in ('GET', 'HEAD', 'OPTIONS', 'DELETE', 'TRACE'):
            return False
        else:
            if not isinstance(exception, (RequestNotSent, RequestTransmissionFailed,
             ResponseNeverReceived)):
                return False
            if isinstance(exception, _WrapperException):
                for aFailure in exception.reasons:
                    if aFailure.check(defer.CancelledError):
                        return False

            if bodyProducer is not None:
                return False
            return True

    def request(self, request):
        d = self._clientProtocol.request(request)

        def failed(reason):
            if self._shouldRetry(request.method, reason.value, request.bodyProducer):
                return self._newConnection().addCallback((lambda connection: connection.request(request)))
            else:
                return reason

        d.addErrback(failed)
        return d


class HTTPConnectionPool(object):
    _factory = _HTTP11ClientFactory
    maxPersistentPerHost = 2
    cachedConnectionTimeout = 240
    retryAutomatically = True

    def __init__(self, reactor, persistent=True):
        self._reactor = reactor
        self.persistent = persistent
        self._connections = {}
        self._timeouts = {}

    def getConnection(self, key, endpoint):
        connections = self._connections.get(key)
        while connections:
            connection = connections.pop(0)
            self._timeouts[connection].cancel()
            del self._timeouts[connection]
            if connection.state == 'QUIESCENT':
                if self.retryAutomatically:
                    newConnection = lambda : self._newConnection(key, endpoint)
                    connection = _RetryingHTTP11ClientProtocol(connection, newConnection)
                return defer.succeed(connection)

        return self._newConnection(key, endpoint)

    def _newConnection(self, key, endpoint):

        def quiescentCallback(protocol):
            self._putConnection(key, protocol)

        factory = self._factory(quiescentCallback)
        return endpoint.connect(factory)

    def _removeConnection(self, key, connection):
        connection.transport.loseConnection()
        self._connections[key].remove(connection)
        del self._timeouts[connection]

    def _putConnection(self, key, connection):
        if connection.state != 'QUIESCENT':
            try:
                raise RuntimeError('BUG: Non-quiescent protocol added to connection pool.')
            except:
                log.err()

            return
        connections = self._connections.setdefault(key, [])
        if len(connections) == self.maxPersistentPerHost:
            dropped = connections.pop(0)
            dropped.transport.loseConnection()
            self._timeouts[dropped].cancel()
            del self._timeouts[dropped]
        connections.append(connection)
        cid = self._reactor.callLater(self.cachedConnectionTimeout, self._removeConnection, key, connection)
        self._timeouts[connection] = cid

    def closeCachedConnections(self):
        results = []
        for protocols in self._connections.itervalues():
            for p in protocols:
                results.append(p.abort())

        self._connections = {}
        for dc in self._timeouts.values():
            dc.cancel()

        self._timeouts = {}
        return defer.gatherResults(results).addCallback((lambda ign: None))


class _AgentBase(object):

    def __init__(self, reactor, pool):
        if pool is None:
            pool = HTTPConnectionPool(reactor, False)
        self._reactor = reactor
        self._pool = pool
        return

    def _computeHostValue(self, scheme, host, port):
        if (
         scheme, port) in (('http', 80), ('https', 443)):
            return host
        return '%s:%d' % (host, port)

    def _requestWithEndpoint(self, key, endpoint, method, parsedURI, headers, bodyProducer, requestPath):
        if headers is None:
            headers = Headers()
        if not headers.hasHeader('host'):
            headers = headers.copy()
            headers.addRawHeader('host', self._computeHostValue(parsedURI.scheme, parsedURI.host, parsedURI.port))
        d = self._pool.getConnection(key, endpoint)

        def cbConnected(proto):
            return proto.request(Request._construct(method, requestPath, headers, bodyProducer, persistent=self._pool.persistent, parsedURI=parsedURI))

        d.addCallback(cbConnected)
        return d


@implementer(IAgentEndpointFactory)
class _StandardEndpointFactory(object):

    def __init__(self, reactor, contextFactory, connectTimeout, bindAddress):
        self._reactor = reactor
        self._policyForHTTPS = contextFactory
        self._connectTimeout = connectTimeout
        self._bindAddress = bindAddress

    def endpointForURI(self, uri):
        kwargs = {}
        if self._connectTimeout is not None:
            kwargs['timeout'] = self._connectTimeout
        kwargs['bindAddress'] = self._bindAddress
        if uri.scheme == 'http':
            return TCP4ClientEndpoint(self._reactor, uri.host, uri.port, **kwargs)
        else:
            if uri.scheme == 'https':
                tlsPolicy = self._policyForHTTPS.creatorForNetloc(uri.host, uri.port)
                return SSL4ClientEndpoint(self._reactor, uri.host, uri.port, tlsPolicy, **kwargs)
            raise SchemeNotSupported('Unsupported scheme: %r' % (uri.scheme,))
            return


@implementer(IAgent)
class Agent(_AgentBase):

    def __init__(self, reactor, contextFactory=BrowserLikePolicyForHTTPS(), connectTimeout=None, bindAddress=None, pool=None):
        if not IPolicyForHTTPS.providedBy(contextFactory):
            warnings.warn(repr(contextFactory) + ' was passed as the HTTPS policy for an Agent, but it does not provide IPolicyForHTTPS.  Since Twisted 14.0, you must pass a provider of IPolicyForHTTPS.', stacklevel=2, category=DeprecationWarning)
            contextFactory = _DeprecatedToCurrentPolicyForHTTPS(contextFactory)
        endpointFactory = _StandardEndpointFactory(reactor, contextFactory, connectTimeout, bindAddress)
        self._init(reactor, endpointFactory, pool)

    @classmethod
    def usingEndpointFactory(cls, reactor, endpointFactory, pool=None):
        agent = cls.__new__(cls)
        agent._init(reactor, endpointFactory, pool)
        return agent

    def _init(self, reactor, endpointFactory, pool):
        _AgentBase.__init__(self, reactor, pool)
        self._endpointFactory = endpointFactory

    def _getEndpoint(self, uri):
        return self._endpointFactory.endpointForURI(uri)

    def request(self, method, uri, headers=None, bodyProducer=None):
        parsedURI = URI.fromBytes(uri)
        try:
            endpoint = self._getEndpoint(parsedURI)
        except SchemeNotSupported:
            return defer.fail(Failure())

        key = (
         parsedURI.scheme, parsedURI.host, parsedURI.port)
        return self._requestWithEndpoint(key, endpoint, method, parsedURI, headers, bodyProducer, parsedURI.originForm)


@implementer(IAgent)
class ProxyAgent(_AgentBase):

    def __init__(self, endpoint, reactor=None, pool=None):
        if reactor is None:
            from twisted.internet import reactor
        _AgentBase.__init__(self, reactor, pool)
        self._proxyEndpoint = endpoint
        return

    def request(self, method, uri, headers=None, bodyProducer=None):
        key = (
         'http-proxy', self._proxyEndpoint)
        return self._requestWithEndpoint(key, self._proxyEndpoint, method, URI.fromBytes(uri), headers, bodyProducer, uri)


class _FakeUrllib2Request(object):

    def __init__(self, uri):
        self.uri = uri
        self.headers = Headers()
        self.type, rest = splittype(self.uri)
        self.host, rest = splithost(rest)

    def has_header(self, header):
        return self.headers.hasHeader(header)

    def add_unredirected_header(self, name, value):
        self.headers.addRawHeader(name, value)

    def get_full_url(self):
        return self.uri

    def get_header(self, name, default=None):
        headers = self.headers.getRawHeaders(name, default)
        if headers is not None:
            return headers[0]
        else:
            return

    def get_host(self):
        return self.host

    def get_type(self):
        return self.type

    def is_unverifiable(self):
        return False


class _FakeUrllib2Response(object):

    def __init__(self, response):
        self.response = response

    def info(self):

        class _Meta(object):

            def getheaders(zelf, name):
                return self.response.headers.getRawHeaders(name, [])

        return _Meta()


@implementer(IAgent)
class CookieAgent(object):

    def __init__(self, agent, cookieJar):
        self._agent = agent
        self.cookieJar = cookieJar

    def request(self, method, uri, headers=None, bodyProducer=None):
        if headers is None:
            headers = Headers()
        lastRequest = _FakeUrllib2Request(uri)
        if not headers.hasHeader('cookie'):
            self.cookieJar.add_cookie_header(lastRequest)
            cookieHeader = lastRequest.get_header('Cookie', None)
            if cookieHeader is not None:
                headers = headers.copy()
                headers.addRawHeader('cookie', cookieHeader)
        d = self._agent.request(method, uri, headers, bodyProducer)
        d.addCallback(self._extractCookies, lastRequest)
        return d

    def _extractCookies(self, response, request):
        resp = _FakeUrllib2Response(response)
        self.cookieJar.extract_cookies(resp, request)
        return response


class GzipDecoder(proxyForInterface(IResponse)):

    def __init__(self, response):
        self.original = response
        self.length = UNKNOWN_LENGTH

    def deliverBody(self, protocol):
        self.original.deliverBody(_GzipProtocol(protocol, self.original))


class _GzipProtocol(proxyForInterface(IProtocol)):

    def __init__(self, protocol, response):
        self.original = protocol
        self._response = response
        self._zlibDecompress = zlib.decompressobj(16 + zlib.MAX_WBITS)

    def dataReceived(self, data):
        try:
            rawData = self._zlibDecompress.decompress(data)
        except zlib.error:
            raise ResponseFailed([Failure()], self._response)

        if rawData:
            self.original.dataReceived(rawData)

    def connectionLost(self, reason):
        try:
            rawData = self._zlibDecompress.flush()
        except zlib.error:
            raise ResponseFailed([reason, Failure()], self._response)

        if rawData:
            self.original.dataReceived(rawData)
        self.original.connectionLost(reason)


@implementer(IAgent)
class ContentDecoderAgent(object):

    def __init__(self, agent, decoders):
        self._agent = agent
        self._decoders = dict(decoders)
        self._supported = (',').join([ decoder[0] for decoder in decoders ])

    def request(self, method, uri, headers=None, bodyProducer=None):
        if headers is None:
            headers = Headers()
        else:
            headers = headers.copy()
        headers.addRawHeader('accept-encoding', self._supported)
        deferred = self._agent.request(method, uri, headers, bodyProducer)
        return deferred.addCallback(self._handleResponse)

    def _handleResponse(self, response):
        contentEncodingHeaders = response.headers.getRawHeaders('content-encoding', [])
        contentEncodingHeaders = (',').join(contentEncodingHeaders).split(',')
        while contentEncodingHeaders:
            name = contentEncodingHeaders.pop().strip()
            decoder = self._decoders.get(name)
            if decoder is not None:
                response = decoder(response)
            else:
                contentEncodingHeaders.append(name)
                break

        if contentEncodingHeaders:
            response.headers.setRawHeaders('content-encoding', [(',').join(contentEncodingHeaders)])
        else:
            response.headers.removeHeader('content-encoding')
        return response


@implementer(IAgent)
class RedirectAgent(object):
    _redirectResponses = [
     http.MOVED_PERMANENTLY, http.FOUND,
     http.TEMPORARY_REDIRECT]
    _seeOtherResponses = [http.SEE_OTHER]

    def __init__(self, agent, redirectLimit=20):
        self._agent = agent
        self._redirectLimit = redirectLimit

    def request(self, method, uri, headers=None, bodyProducer=None):
        deferred = self._agent.request(method, uri, headers, bodyProducer)
        return deferred.addCallback(self._handleResponse, method, uri, headers, 0)

    def _resolveLocation(self, requestURI, location):
        return _urljoin(requestURI, location)

    def _handleRedirect(self, response, method, uri, headers, redirectCount):
        if redirectCount >= self._redirectLimit:
            err = error.InfiniteRedirection(response.code, 'Infinite redirection detected', location=uri)
            raise ResponseFailed([Failure(err)], response)
        locationHeaders = response.headers.getRawHeaders('location', [])
        if not locationHeaders:
            err = error.RedirectWithNoLocation(response.code, 'No location header field', uri)
            raise ResponseFailed([Failure(err)], response)
        location = self._resolveLocation(uri, locationHeaders[0])
        deferred = self._agent.request(method, location, headers)

        def _chainResponse(newResponse):
            newResponse.setPreviousResponse(response)
            return newResponse

        deferred.addCallback(_chainResponse)
        return deferred.addCallback(self._handleResponse, method, uri, headers, redirectCount + 1)

    def _handleResponse(self, response, method, uri, headers, redirectCount):
        if response.code in self._redirectResponses:
            if method not in ('GET', 'HEAD'):
                err = error.PageRedirect(response.code, location=uri)
                raise ResponseFailed([Failure(err)], response)
            return self._handleRedirect(response, method, uri, headers, redirectCount)
        if response.code in self._seeOtherResponses:
            return self._handleRedirect(response, 'GET', uri, headers, redirectCount)
        return response


class BrowserLikeRedirectAgent(RedirectAgent):
    _redirectResponses = [
     http.TEMPORARY_REDIRECT]
    _seeOtherResponses = [http.MOVED_PERMANENTLY, http.FOUND, http.SEE_OTHER]


class _ReadBodyProtocol(protocol.Protocol):

    def __init__(self, status, message, deferred):
        self.deferred = deferred
        self.status = status
        self.message = message
        self.dataBuffer = []

    def dataReceived(self, data):
        self.dataBuffer.append(data)

    def connectionLost(self, reason):
        if reason.check(ResponseDone):
            self.deferred.callback(('').join(self.dataBuffer))
        elif reason.check(PotentialDataLoss):
            self.deferred.errback(PartialDownloadError(self.status, self.message, ('').join(self.dataBuffer)))
        else:
            self.deferred.errback(reason)


def readBody(response):

    def cancel(deferred):
        abort = getAbort()
        if abort is not None:
            abort()
        return

    d = defer.Deferred(cancel)
    protocol = _ReadBodyProtocol(response.code, response.phrase, d)

    def getAbort():
        return getattr(protocol.transport, 'abortConnection', None)

    response.deliverBody(protocol)
    if protocol.transport is not None and getAbort() is None:
        warnings.warn('Using readBody with a transport that does not have an abortConnection method', category=DeprecationWarning, stacklevel=2)
    return d


__all__ = [
 'PartialDownloadError', 'HTTPPageGetter', 'HTTPPageDownloader', 
 'HTTPClientFactory', 
 'HTTPDownloader', 'getPage', 'downloadPage', 
 'ResponseDone', 'Response', 
 'ResponseFailed', 'Agent', 'CookieAgent', 
 'ProxyAgent', 'ContentDecoderAgent', 
 'GzipDecoder', 'RedirectAgent', 
 'HTTPConnectionPool', 'readBody', 'BrowserLikeRedirectAgent', 
 'URI']
# okay decompiling out\twisted.web.client.pyc
