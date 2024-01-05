# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.server
from __future__ import division, absolute_import
import copy, os
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote as _quote

    def quote(string, *args, **kwargs):
        return _quote(string.decode('charmap'), *args, **kwargs).encode('charmap')


import zlib
from zope.interface import implementer
from twisted.python.compat import _PY3, networkString, nativeString, intToBytes
if _PY3:

    class Copyable():
        pass


else:
    from twisted.spread.pb import Copyable, ViewPoint
from twisted.internet import address
from twisted.web import iweb, http, util
from twisted.web.http import unquote
from twisted.python import log, reflect, failure, components
from twisted import copyright
from twisted.web import resource
from twisted.web.error import UnsupportedMethod
from twisted.python.versions import Version
from twisted.python.deprecate import deprecatedModuleAttribute
from twisted.python.compat import escape
NOT_DONE_YET = 1
__all__ = [
 'supportedMethods', 
 'Request', 
 'Session', 
 'Site', 
 'version', 
 'NOT_DONE_YET', 
 'GzipEncoderFactory']
deprecatedModuleAttribute(Version('Twisted', 12, 1, 0), 'Please use twisted.web.http.datetimeToString instead', 'twisted.web.server', 'date_time_string')
deprecatedModuleAttribute(Version('Twisted', 12, 1, 0), 'Please use twisted.web.http.stringToDatetime instead', 'twisted.web.server', 'string_date_time')
date_time_string = http.datetimeToString
string_date_time = http.stringToDatetime
supportedMethods = (
 'GET', 'HEAD', 'POST')

def _addressToTuple(addr):
    if isinstance(addr, address.IPv4Address):
        return ('INET', addr.host, addr.port)
    else:
        if isinstance(addr, address.UNIXAddress):
            return ('UNIX', addr.name)
        return tuple(addr)


@implementer(iweb.IRequest)
class Request(Copyable, http.Request, components.Componentized):
    defaultContentType = 'text/html'
    site = None
    appRootURL = None
    __pychecker__ = 'unusednames=issuer'
    _inFakeHead = False
    _encoder = None

    def __init__(self, *args, **kw):
        http.Request.__init__(self, *args, **kw)
        components.Componentized.__init__(self)

    def getStateToCopyFor(self, issuer):
        x = self.__dict__.copy()
        del x['transport']
        del x['channel']
        del x['content']
        del x['site']
        self.content.seek(0, 0)
        x['content_data'] = self.content.read()
        x['remote'] = ViewPoint(issuer, self)
        x['host'] = _addressToTuple(x['host'])
        x['client'] = _addressToTuple(x['client'])
        x['requestHeaders'] = list(x['requestHeaders'].getAllRawHeaders())
        return x

    def sibLink(self, name):
        if self.postpath:
            return len(self.postpath) * '../' + name
        else:
            return name

    def childLink(self, name):
        lpp = len(self.postpath)
        if lpp > 1:
            return (lpp - 1) * '../' + name
        else:
            if lpp == 1:
                return name
            if len(self.prepath) and self.prepath[-1]:
                return self.prepath[-1] + '/' + name
            return name

    def process(self):
        self.site = self.channel.site
        self.setHeader('server', version)
        self.setHeader('date', http.datetimeToString())
        self.prepath = []
        self.postpath = list(map(unquote, self.path[1:].split('/')))
        try:
            resrc = self.site.getResourceFor(self)
            if resource._IEncodingResource.providedBy(resrc):
                encoder = resrc.getEncoder(self)
                if encoder is not None:
                    self._encoder = encoder
            self.render(resrc)
        except:
            self.processingFailed(failure.Failure())

        return

    def write(self, data):
        if not self.startedWriting:
            modified = self.code != http.NOT_MODIFIED
            contentType = self.responseHeaders.getRawHeaders('content-type')
            if modified and contentType is None and self.defaultContentType is not None:
                self.responseHeaders.setRawHeaders('content-type', [self.defaultContentType])
        if not self._inFakeHead:
            if self._encoder:
                data = self._encoder.encode(data)
            http.Request.write(self, data)
        return

    def finish(self):
        if self._encoder:
            data = self._encoder.finish()
            if data:
                http.Request.write(self, data)
        return http.Request.finish(self)

    def render(self, resrc):
        try:
            body = resrc.render(self)
        except UnsupportedMethod as e:
            allowedMethods = e.allowedMethods
            if self.method == 'HEAD' and 'GET' in allowedMethods:
                log.msg('Using GET to fake a HEAD request for %s' % (
                 resrc,))
                self.method = 'GET'
                self._inFakeHead = True
                body = resrc.render(self)
                if body is NOT_DONE_YET:
                    log.msg('Tried to fake a HEAD request for %s, but it got away from me.' % resrc)
                else:
                    self.setHeader('content-length', intToBytes(len(body)))
                self._inFakeHead = False
                self.method = 'HEAD'
                self.write('')
                self.finish()
                return
            if self.method in supportedMethods:
                self.setHeader('Allow', (', ').join(allowedMethods))
                s = 'Your browser approached me (at %(URI)s) with the method "%(method)s".  I only allow the method%(plural)s %(allowed)s here.' % {'URI': escape(nativeString(self.uri)), 
                   'method': nativeString(self.method), 
                   'plural': len(allowedMethods) > 1 and 's' or '', 
                   'allowed': (', ').join([ nativeString(x) for x in allowedMethods ])}
                epage = resource.ErrorPage(http.NOT_ALLOWED, 'Method Not Allowed', s)
                body = epage.render(self)
            else:
                epage = resource.ErrorPage(http.NOT_IMPLEMENTED, 'Huh?', "I don't know how to treat a %s request." % (
                 escape(self.method.decode('charmap')),))
                body = epage.render(self)

        if body == NOT_DONE_YET:
            return
        if not isinstance(body, bytes):
            body = resource.ErrorPage(http.INTERNAL_SERVER_ERROR, 'Request did not return bytes', 'Request: ' + util._PRE(reflect.safe_repr(self)) + '<br />' + 'Resource: ' + util._PRE(reflect.safe_repr(resrc)) + '<br />' + 'Value: ' + util._PRE(reflect.safe_repr(body))).render(self)
        if self.method == 'HEAD':
            if len(body) > 0:
                log.msg("Warning: HEAD request %s for resource %s is returning a message body.  I think I'll eat it." % (
                 self, resrc))
                self.setHeader('content-length', intToBytes(len(body)))
            self.write('')
        else:
            self.setHeader('content-length', intToBytes(len(body)))
            self.write(body)
        self.finish()

    def processingFailed(self, reason):
        log.err(reason)
        if self.site.displayTracebacks:
            body = '<html><head><title>web.Server Traceback (most recent call last)</title></head><body><b>web.Server Traceback (most recent call last):</b>\n\n' + util.formatFailure(reason) + '\n\n</body></html>\n'
        else:
            body = '<html><head><title>Processing Failed</title></head><body><b>Processing Failed</b></body></html>'
        self.setResponseCode(http.INTERNAL_SERVER_ERROR)
        self.setHeader('content-type', 'text/html')
        self.setHeader('content-length', intToBytes(len(body)))
        self.write(body)
        self.finish()
        return reason

    def view_write(self, issuer, data):
        self.write(data)

    def view_finish(self, issuer):
        self.finish()

    def view_addCookie(self, issuer, k, v, **kwargs):
        self.addCookie(k, v, **kwargs)

    def view_setHeader(self, issuer, k, v):
        self.setHeader(k, v)

    def view_setLastModified(self, issuer, when):
        self.setLastModified(when)

    def view_setETag(self, issuer, tag):
        self.setETag(tag)

    def view_setResponseCode(self, issuer, code, message=None):
        self.setResponseCode(code, message)

    def view_registerProducer(self, issuer, producer, streaming):
        self.registerProducer(_RemoteProducerWrapper(producer), streaming)

    def view_unregisterProducer(self, issuer):
        self.unregisterProducer()

    session = None

    def getSession(self, sessionInterface=None):
        if not self.session:
            cookiename = ('_').join(['TWISTED_SESSION'] + self.sitepath)
            sessionCookie = self.getCookie(cookiename)
            if sessionCookie:
                try:
                    self.session = self.site.getSession(sessionCookie)
                except KeyError:
                    pass

            if not self.session:
                self.session = self.site.makeSession()
                self.addCookie(cookiename, self.session.uid, path='/')
        self.session.touch()
        if sessionInterface:
            return self.session.getComponent(sessionInterface)
        return self.session

    def _prePathURL(self, prepath):
        port = self.getHost().port
        if self.isSecure():
            default = 443
        else:
            default = 80
        if port == default:
            hostport = ''
        else:
            hostport = ':%d' % port
        prefix = networkString('http%s://%s%s/' % (
         self.isSecure() and 's' or '',
         nativeString(self.getRequestHostname()),
         hostport))
        path = ('/').join([ quote(segment, safe='') for segment in prepath ])
        return prefix + path

    def prePathURL(self):
        return self._prePathURL(self.prepath)

    def URLPath(self):
        from twisted.python import urlpath
        return urlpath.URLPath.fromRequest(self)

    def rememberRootURL(self):
        url = self._prePathURL(self.prepath[:-1])
        self.appRootURL = url

    def getRootURL(self):
        return self.appRootURL


@implementer(iweb._IRequestEncoderFactory)
class GzipEncoderFactory(object):
    compressLevel = 9

    def encoderForRequest(self, request):
        acceptHeaders = request.requestHeaders.getRawHeaders('accept-encoding', [])
        supported = (',').join(acceptHeaders).split(',')
        if 'gzip' in supported:
            encoding = request.responseHeaders.getRawHeaders('content-encoding')
            if encoding:
                encoding = '%s,gzip' % (',').join(encoding)
            else:
                encoding = 'gzip'
            request.responseHeaders.setRawHeaders('content-encoding', [
             encoding])
            return _GzipEncoder(self.compressLevel, request)


@implementer(iweb._IRequestEncoder)
class _GzipEncoder(object):
    _zlibCompressor = None

    def __init__(self, compressLevel, request):
        self._zlibCompressor = zlib.compressobj(compressLevel, zlib.DEFLATED, 16 + zlib.MAX_WBITS)
        self._request = request

    def encode(self, data):
        if not self._request.startedWriting:
            self._request.responseHeaders.removeHeader('content-length')
        return self._zlibCompressor.compress(data)

    def finish(self):
        remain = self._zlibCompressor.flush()
        self._zlibCompressor = None
        return remain


class _RemoteProducerWrapper():

    def __init__(self, remote):
        self.resumeProducing = remote.remoteMethod('resumeProducing')
        self.pauseProducing = remote.remoteMethod('pauseProducing')
        self.stopProducing = remote.remoteMethod('stopProducing')


class Session(components.Componentized):
    sessionTimeout = 900
    _expireCall = None

    def __init__(self, site, uid, reactor=None):
        components.Componentized.__init__(self)
        if reactor is None:
            from twisted.internet import reactor
        self._reactor = reactor
        self.site = site
        self.uid = uid
        self.expireCallbacks = []
        self.touch()
        self.sessionNamespaces = {}
        return

    def startCheckingExpiration(self):
        self._expireCall = self._reactor.callLater(self.sessionTimeout, self.expire)

    def notifyOnExpire(self, callback):
        self.expireCallbacks.append(callback)

    def expire(self):
        del self.site.sessions[self.uid]
        for c in self.expireCallbacks:
            c()

        self.expireCallbacks = []
        if self._expireCall and self._expireCall.active():
            self._expireCall.cancel()
            self._expireCall = None
        return

    def touch(self):
        self.lastModified = self._reactor.seconds()
        if self._expireCall is not None:
            self._expireCall.reset(self.sessionTimeout)
        return


version = networkString('TwistedWeb/%s' % (copyright.version,))

class Site(http.HTTPFactory):
    counter = 0
    requestFactory = Request
    displayTracebacks = True
    sessionFactory = Session
    sessionCheckTime = 1800

    def __init__(self, resource, requestFactory=None, *args, **kwargs):
        http.HTTPFactory.__init__(self, *args, **kwargs)
        self.sessions = {}
        self.resource = resource
        if requestFactory is not None:
            self.requestFactory = requestFactory
        return

    def _openLogFile(self, path):
        from twisted.python import logfile
        return logfile.LogFile(os.path.basename(path), os.path.dirname(path))

    def __getstate__(self):
        d = self.__dict__.copy()
        d['sessions'] = {}
        return d

    def _mkuid(self):
        from hashlib import md5
        import random
        self.counter = self.counter + 1
        return md5(networkString('%s_%s' % (str(random.random()), str(self.counter)))).hexdigest()

    def makeSession(self):
        uid = self._mkuid()
        session = self.sessions[uid] = self.sessionFactory(self, uid)
        session.startCheckingExpiration()
        return session

    def getSession(self, uid):
        return self.sessions[uid]

    def buildProtocol(self, addr):
        channel = http.HTTPFactory.buildProtocol(self, addr)
        channel.requestFactory = self.requestFactory
        channel.site = self
        return channel

    isLeaf = 0

    def render(self, request):
        request.redirect(request.prePathURL() + '/')
        request.finish()

    def getChildWithDefault(self, pathEl, request):
        request.site = self
        return self.resource.getChildWithDefault(pathEl, request)

    def getResourceFor(self, request):
        request.site = self
        request.sitepath = copy.copy(request.prepath)
        return resource.getChildForRequest(self.resource, request)
# okay decompiling out\twisted.web.server.pyc
