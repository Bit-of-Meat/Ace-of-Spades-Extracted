# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.web.iweb
from zope.interface import Interface, Attribute
from twisted.internet.interfaces import IPushProducer
from twisted.cred.credentials import IUsernameDigestHash

class IRequest(Interface):
    method = Attribute('A C{str} giving the HTTP method that was used.')
    uri = Attribute('A C{str} giving the full encoded URI which was requested (including query arguments).')
    path = Attribute('A C{str} giving the encoded query path of the request URI.')
    args = Attribute("A mapping of decoded query argument names as C{str} to corresponding query argument values as C{list}s of C{str}.  For example, for a URI with C{'foo=bar&foo=baz&quux=spam'} for its query part, C{args} will be C{{'foo': ['bar', 'baz'], 'quux': ['spam']}}.")
    received_headers = Attribute('Backwards-compatibility access to C{requestHeaders}, deprecated in Twisted 13.2.0.  Use C{requestHeaders} instead.  C{received_headers} behaves mostly like a C{dict} and does not provide access to all header values.')
    requestHeaders = Attribute('A L{http_headers.Headers} instance giving all received HTTP request headers.')
    content = Attribute('A file-like object giving the request body.  This may be a file on disk, a C{StringIO}, or some other type.  The implementation is free to decide on a per-request basis.')
    headers = Attribute('Backwards-compatibility access to C{responseHeaders}, deprecated in Twisted 13.2.0.  Use C{responseHeaders} instead.  C{headers} behaves mostly like a C{dict} and does not provide access to all header values nor does it allow multiple values for one header to be set.')
    responseHeaders = Attribute('A L{http_headers.Headers} instance holding all HTTP response headers to be sent.')

    def getHeader(key):
        pass

    def getCookie(key):
        pass

    def getAllHeaders():
        pass

    def getRequestHostname():
        pass

    def getHost():
        pass

    def getClientIP():
        pass

    def getClient():
        pass

    def getUser():
        pass

    def getPassword():
        pass

    def isSecure():
        pass

    def getSession(sessionInterface=None):
        pass

    def URLPath():
        pass

    def prePathURL():
        pass

    def rememberRootURL():
        pass

    def getRootURL():
        pass

    def finish():
        pass

    def write(data):
        pass

    def addCookie(k, v, expires=None, domain=None, path=None, max_age=None, comment=None, secure=None):
        pass

    def setResponseCode(code, message=None):
        pass

    def setHeader(k, v):
        pass

    def redirect(url):
        pass

    def setLastModified(when):
        pass

    def setETag(etag):
        pass

    def setHost(host, port, ssl=0):
        pass


class IAccessLogFormatter(Interface):

    def __call__(timestamp, request):
        pass


class ICredentialFactory(Interface):
    scheme = Attribute("A C{str} giving the name of the authentication scheme with which this factory is associated.  For example, C{'basic'} or C{'digest'}.")

    def getChallenge(request):
        pass

    def decode(response, request):
        pass


class IBodyProducer(IPushProducer):
    length = Attribute('\n        C{length} is a C{int} indicating how many bytes in total this\n        L{IBodyProducer} will write to the consumer or L{UNKNOWN_LENGTH}\n        if this is not known in advance.\n        ')

    def startProducing(consumer):
        pass

    def stopProducing():
        pass


class IRenderable(Interface):

    def lookupRenderMethod(name):
        pass

    def render(request):
        pass


class ITemplateLoader(Interface):

    def load():
        pass


class IResponse(Interface):
    version = Attribute("A three-tuple describing the protocol and protocol version of the response.  The first element is of type C{str}, the second and third are of type C{int}.  For example, C{('HTTP', 1, 1)}.")
    code = Attribute('The HTTP status code of this response, as a C{int}.')
    phrase = Attribute('The HTTP reason phrase of this response, as a C{str}.')
    headers = Attribute('The HTTP response L{Headers} of this response.')
    length = Attribute('The C{int} number of bytes expected to be in the body of this response or L{UNKNOWN_LENGTH} if the server did not indicate how many bytes to expect.  For I{HEAD} responses, this will be 0; if the response includes a I{Content-Length} header, it will be available in C{headers}.')
    request = Attribute('The L{IClientRequest} that resulted in this response.')
    previousResponse = Attribute('The previous L{IResponse} from a redirect, or C{None} if there was no previous response. This can be used to walk the response or request history for redirections.')

    def deliverBody(protocol):
        pass

    def setPreviousResponse(response):
        pass


class _IRequestEncoder(Interface):

    def encode(data):
        pass

    def finish():
        pass


class _IRequestEncoderFactory(Interface):

    def encoderForRequest(request):
        pass


class IClientRequest(Interface):
    method = Attribute("The HTTP method for this request, as L{bytes}. For example: C{b'GET'}, C{b'HEAD'}, C{b'POST'}, etc.")
    absoluteURI = Attribute('The absolute URI of the requested resource, as L{bytes}; or C{None} if the absolute URI cannot be determined.')
    headers = Attribute('Headers to be sent to the server, as a L{twisted.web.http_headers.Headers} instance.')


class IAgent(Interface):

    def request(method, uri, headers=None, bodyProducer=None):
        pass


class IPolicyForHTTPS(Interface):

    def creatorForNetloc(hostname, port):
        pass


class IAgentEndpointFactory(Interface):

    def endpointForURI(uri):
        pass


UNKNOWN_LENGTH = 'twisted.web.iweb.UNKNOWN_LENGTH'
__all__ = [
 'IUsernameDigestHash', 'ICredentialFactory', 'IRequest', 
 'IBodyProducer', 
 'IRenderable', 'IResponse', '_IRequestEncoder', 
 '_IRequestEncoderFactory', 
 'IClientRequest', 
 'UNKNOWN_LENGTH']
# okay decompiling out\twisted.web.iweb.pyc
