# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.internet._sslverify
from __future__ import division, absolute_import
import itertools, warnings
from binascii import a2b_base64
from hashlib import md5
import OpenSSL
from OpenSSL import SSL, crypto
try:
    from OpenSSL.SSL import SSL_CB_HANDSHAKE_DONE, SSL_CB_HANDSHAKE_START
except ImportError:
    SSL_CB_HANDSHAKE_START = 16
    SSL_CB_HANDSHAKE_DONE = 32

from twisted.python import log

def _cantSetHostnameIndication(connection, hostname):
    pass


def _setHostNameIndication(connection, hostname):
    connection.set_tlsext_host_name(hostname)


if getattr(SSL.Connection, 'set_tlsext_host_name', None) is None:
    _maybeSetHostNameIndication = _cantSetHostnameIndication
else:
    _maybeSetHostNameIndication = _setHostNameIndication

class SimpleVerificationError(Exception):
    pass


def _idnaBytes(text):
    try:
        import idna
    except ImportError:
        return text.encode('idna')

    return idna.encode(text)


def _idnaText(octets):
    try:
        import idna
    except ImportError:
        return octets.decode('idna')

    return idna.decode(octets)


def simpleVerifyHostname(connection, hostname):
    commonName = connection.get_peer_certificate().get_subject().commonName
    if commonName != hostname:
        raise SimpleVerificationError(repr(commonName) + '!=' + repr(hostname))


def _selectVerifyImplementation(lib):
    whatsWrong = 'Without the service_identity module and a recent enough pyOpenSSL to support it, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.'
    major, minor = list(int(part) for part in lib.__version__.split('.'))[:2]
    if (
     major, minor) >= (0, 12):
        try:
            from service_identity import VerificationError
            from service_identity.pyopenssl import verify_hostname
            return (
             verify_hostname, VerificationError)
        except ImportError as e:
            warnings.warn_explicit("You do not have a working installation of the service_identity module: '" + str(e) + "'.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  " + whatsWrong, category=UserWarning, filename='', lineno=0)

    else:
        warnings.warn_explicit(('Your version of pyOpenSSL, {0}, is out of date.  Please upgrade to at least 0.12 and install service_identity from <https://pypi.python.org/pypi/service_identity>.  ').format(lib.__version__) + whatsWrong, category=UserWarning, filename='', lineno=0)
    return (simpleVerifyHostname, SimpleVerificationError)


verifyHostname, VerificationError = _selectVerifyImplementation(OpenSSL)
from zope.interface import Interface, implementer
from twisted.internet.defer import Deferred
from twisted.internet.error import VerifyError, CertificateError
from twisted.internet.interfaces import IAcceptableCiphers, ICipher, IOpenSSLClientConnectionCreator
from twisted.python import reflect, util
from twisted.python.deprecate import _mutuallyExclusiveArguments
from twisted.python.compat import nativeString, networkString, unicode
from twisted.python.failure import Failure
from twisted.python.util import FancyEqMixin
from twisted.python.deprecate import deprecated
from twisted.python.versions import Version

def _sessionCounter(counter=itertools.count()):
    return next(counter)


_x509names = {'CN': 'commonName', 
   'commonName': 'commonName', 
   'O': 'organizationName', 
   'organizationName': 'organizationName', 
   'OU': 'organizationalUnitName', 
   'organizationalUnitName': 'organizationalUnitName', 
   'L': 'localityName', 
   'localityName': 'localityName', 
   'ST': 'stateOrProvinceName', 
   'stateOrProvinceName': 'stateOrProvinceName', 
   'C': 'countryName', 
   'countryName': 'countryName', 
   'emailAddress': 'emailAddress'}

class DistinguishedName(dict):
    __slots__ = ()

    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

    def _copyFrom(self, x509name):
        for name in _x509names:
            value = getattr(x509name, name, None)
            if value is not None:
                setattr(self, name, value)

        return

    def _copyInto(self, x509name):
        for k, v in self.items():
            setattr(x509name, k, nativeString(v))

    def __repr__(self):
        return '<DN %s>' % dict.__repr__(self)[1:-1]

    def __getattr__(self, attr):
        try:
            return self[_x509names[attr]]
        except KeyError:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr not in _x509names:
            raise AttributeError('%s is not a valid OpenSSL X509 name field' % (attr,))
        realAttr = _x509names[attr]
        if not isinstance(value, bytes):
            value = value.encode('ascii')
        self[realAttr] = value

    def inspect(self):
        l = []
        lablen = 0

        def uniqueValues(mapping):
            return set(mapping.values())

        for k in sorted(uniqueValues(_x509names)):
            label = util.nameToLabel(k)
            lablen = max(len(label), lablen)
            v = getattr(self, k, None)
            if v is not None:
                l.append((label, nativeString(v)))

        lablen += 2
        for n, (label, attr) in enumerate(l):
            l[n] = label.rjust(lablen) + ': ' + attr

        return ('\n').join(l)


DN = DistinguishedName

class CertBase():

    def __init__(self, original):
        self.original = original

    def _copyName(self, suffix):
        dn = DistinguishedName()
        dn._copyFrom(getattr(self.original, 'get_' + suffix)())
        return dn

    def getSubject(self):
        return self._copyName('subject')

    def __conform__(self, interface):
        if interface is IOpenSSLTrustRoot:
            return OpenSSLCertificateAuthorities([self.original])
        return NotImplemented


def _handleattrhelper(Class, transport, methodName):
    method = getattr(transport.getHandle(), 'get_%s_certificate' % (methodName,), None)
    if method is None:
        raise CertificateError('non-TLS transport %r did not have %s certificate' % (transport, methodName))
    cert = method()
    if cert is None:
        raise CertificateError('TLS transport %r did not have %s certificate' % (transport, methodName))
    return Class(cert)


class Certificate(CertBase):

    def __repr__(self):
        return '<%s Subject=%s Issuer=%s>' % (self.__class__.__name__,
         self.getSubject().commonName,
         self.getIssuer().commonName)

    def __eq__(self, other):
        if isinstance(other, Certificate):
            return self.dump() == other.dump()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def load(Class, requestData, format=crypto.FILETYPE_ASN1, args=()):
        return Class(crypto.load_certificate(format, requestData), *args)

    load = classmethod(load)
    _load = load

    def dumpPEM(self):
        return self.dump(crypto.FILETYPE_PEM)

    def loadPEM(Class, data):
        return Class.load(data, crypto.FILETYPE_PEM)

    loadPEM = classmethod(loadPEM)

    def peerFromTransport(Class, transport):
        return _handleattrhelper(Class, transport, 'peer')

    peerFromTransport = classmethod(peerFromTransport)

    def hostFromTransport(Class, transport):
        return _handleattrhelper(Class, transport, 'host')

    hostFromTransport = classmethod(hostFromTransport)

    def getPublicKey(self):
        return PublicKey(self.original.get_pubkey())

    def dump(self, format=crypto.FILETYPE_ASN1):
        return crypto.dump_certificate(format, self.original)

    def serialNumber(self):
        return self.original.get_serial_number()

    def digest(self, method='md5'):
        return self.original.digest(method)

    def _inspect(self):
        return ('\n').join(['Certificate For Subject:',
         self.getSubject().inspect(),
         '\nIssuer:',
         self.getIssuer().inspect(),
         '\nSerial Number: %d' % self.serialNumber(),
         'Digest: %s' % nativeString(self.digest())])

    def inspect(self):
        return ('\n').join((self._inspect(), self.getPublicKey().inspect()))

    def getIssuer(self):
        return self._copyName('issuer')

    def options(self, *authorities):
        raise NotImplementedError('Possible, but doubtful we need this yet')


class CertificateRequest(CertBase):

    def load(Class, requestData, requestFormat=crypto.FILETYPE_ASN1):
        req = crypto.load_certificate_request(requestFormat, requestData)
        dn = DistinguishedName()
        dn._copyFrom(req.get_subject())
        if not req.verify(req.get_pubkey()):
            raise VerifyError("Can't verify that request for %r is self-signed." % (dn,))
        return Class(req)

    load = classmethod(load)

    def dump(self, format=crypto.FILETYPE_ASN1):
        return crypto.dump_certificate_request(format, self.original)


class PrivateCertificate(Certificate):

    def __repr__(self):
        return Certificate.__repr__(self) + ' with ' + repr(self.privateKey)

    def _setPrivateKey(self, privateKey):
        if not privateKey.matches(self.getPublicKey()):
            raise VerifyError('Certificate public and private keys do not match.')
        self.privateKey = privateKey
        return self

    def newCertificate(self, newCertData, format=crypto.FILETYPE_ASN1):
        return self.load(newCertData, self.privateKey, format)

    def load(Class, data, privateKey, format=crypto.FILETYPE_ASN1):
        return Class._load(data, format)._setPrivateKey(privateKey)

    load = classmethod(load)

    def inspect(self):
        return ('\n').join([Certificate._inspect(self),
         self.privateKey.inspect()])

    def dumpPEM(self):
        return self.dump(crypto.FILETYPE_PEM) + self.privateKey.dump(crypto.FILETYPE_PEM)

    def loadPEM(Class, data):
        return Class.load(data, KeyPair.load(data, crypto.FILETYPE_PEM), crypto.FILETYPE_PEM)

    loadPEM = classmethod(loadPEM)

    def fromCertificateAndKeyPair(Class, certificateInstance, privateKey):
        privcert = Class(certificateInstance.original)
        return privcert._setPrivateKey(privateKey)

    fromCertificateAndKeyPair = classmethod(fromCertificateAndKeyPair)

    def options(self, *authorities):
        options = dict(privateKey=self.privateKey.original, certificate=self.original)
        if authorities:
            options.update(dict(trustRoot=OpenSSLCertificateAuthorities([ auth.original for auth in authorities ])))
        return OpenSSLCertificateOptions(**options)

    def certificateRequest(self, format=crypto.FILETYPE_ASN1, digestAlgorithm='sha256'):
        return self.privateKey.certificateRequest(self.getSubject(), format, digestAlgorithm)

    def signCertificateRequest(self, requestData, verifyDNCallback, serialNumber, requestFormat=crypto.FILETYPE_ASN1, certificateFormat=crypto.FILETYPE_ASN1):
        issuer = self.getSubject()
        return self.privateKey.signCertificateRequest(issuer, requestData, verifyDNCallback, serialNumber, requestFormat, certificateFormat)

    def signRequestObject(self, certificateRequest, serialNumber, secondsToExpiry=31536000, digestAlgorithm='sha256'):
        return self.privateKey.signRequestObject(self.getSubject(), certificateRequest, serialNumber, secondsToExpiry, digestAlgorithm)


class PublicKey():

    def __init__(self, osslpkey):
        self.original = osslpkey

    def matches(self, otherKey):
        return self.keyHash() == otherKey.keyHash()

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.keyHash())

    def keyHash(self):
        nsspki = crypto.NetscapeSPKI()
        nsspki.set_pubkey(self.original)
        encoded = nsspki.b64_encode()
        raw = a2b_base64(encoded)
        h = md5()
        h.update(raw)
        return h.hexdigest()

    def inspect(self):
        return 'Public Key with Hash: %s' % (self.keyHash(),)


class KeyPair(PublicKey):

    def load(Class, data, format=crypto.FILETYPE_ASN1):
        return Class(crypto.load_privatekey(format, data))

    load = classmethod(load)

    def dump(self, format=crypto.FILETYPE_ASN1):
        return crypto.dump_privatekey(format, self.original)

    def __getstate__(self):
        return self.dump()

    def __setstate__(self, state):
        self.__init__(crypto.load_privatekey(crypto.FILETYPE_ASN1, state))

    def inspect(self):
        t = self.original.type()
        if t == crypto.TYPE_RSA:
            ts = 'RSA'
        elif t == crypto.TYPE_DSA:
            ts = 'DSA'
        else:
            ts = '(Unknown Type!)'
        L = (
         self.original.bits(), ts, self.keyHash())
        return '%s-bit %s Key Pair with Hash: %s' % L

    def generate(Class, kind=crypto.TYPE_RSA, size=1024):
        pkey = crypto.PKey()
        pkey.generate_key(kind, size)
        return Class(pkey)

    def newCertificate(self, newCertData, format=crypto.FILETYPE_ASN1):
        return PrivateCertificate.load(newCertData, self, format)

    generate = classmethod(generate)

    def requestObject(self, distinguishedName, digestAlgorithm='sha256'):
        req = crypto.X509Req()
        req.set_pubkey(self.original)
        distinguishedName._copyInto(req.get_subject())
        req.sign(self.original, digestAlgorithm)
        return CertificateRequest(req)

    def certificateRequest(self, distinguishedName, format=crypto.FILETYPE_ASN1, digestAlgorithm='sha256'):
        return self.requestObject(distinguishedName, digestAlgorithm).dump(format)

    def signCertificateRequest(self, issuerDistinguishedName, requestData, verifyDNCallback, serialNumber, requestFormat=crypto.FILETYPE_ASN1, certificateFormat=crypto.FILETYPE_ASN1, secondsToExpiry=31536000, digestAlgorithm='sha256'):
        hlreq = CertificateRequest.load(requestData, requestFormat)
        dn = hlreq.getSubject()
        vval = verifyDNCallback(dn)

        def verified(value):
            if not value:
                raise VerifyError('DN callback %r rejected request DN %r' % (verifyDNCallback, dn))
            return self.signRequestObject(issuerDistinguishedName, hlreq, serialNumber, secondsToExpiry, digestAlgorithm).dump(certificateFormat)

        if isinstance(vval, Deferred):
            return vval.addCallback(verified)
        else:
            return verified(vval)

    def signRequestObject(self, issuerDistinguishedName, requestObject, serialNumber, secondsToExpiry=31536000, digestAlgorithm='sha256'):
        req = requestObject.original
        cert = crypto.X509()
        issuerDistinguishedName._copyInto(cert.get_issuer())
        cert.set_subject(req.get_subject())
        cert.set_pubkey(req.get_pubkey())
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(secondsToExpiry)
        cert.set_serial_number(serialNumber)
        cert.sign(self.original, digestAlgorithm)
        return Certificate(cert)

    def selfSignedCert(self, serialNumber, **kw):
        dn = DN(**kw)
        return PrivateCertificate.fromCertificateAndKeyPair(self.signRequestObject(dn, self.requestObject(dn), serialNumber), self)


KeyPair.__getstate__ = deprecated(Version('Twisted', 15, 0, 0), 'a real persistence system')(KeyPair.__getstate__)
KeyPair.__setstate__ = deprecated(Version('Twisted', 15, 0, 0), 'a real persistence system')(KeyPair.__setstate__)

class IOpenSSLTrustRoot(Interface):

    def _addCACertsToContext(context):
        pass


@implementer(IOpenSSLTrustRoot)
class OpenSSLCertificateAuthorities(object):

    def __init__(self, caCerts):
        self._caCerts = caCerts

    def _addCACertsToContext(self, context):
        store = context.get_cert_store()
        for cert in self._caCerts:
            store.add_cert(cert)


@implementer(IOpenSSLTrustRoot)
class OpenSSLDefaultPaths(object):

    def _addCACertsToContext(self, context):
        context.set_default_verify_paths()


def platformTrust():
    return OpenSSLDefaultPaths()


def _tolerateErrors(wrapped):

    def infoCallback(connection, where, ret):
        try:
            return wrapped(connection, where, ret)
        except:
            f = Failure()
            log.err(f, 'Error during info_callback')
            connection.get_app_data().failVerification(f)

    return infoCallback


@implementer(IOpenSSLClientConnectionCreator)
class ClientTLSOptions(object):

    def __init__(self, hostname, ctx):
        self._ctx = ctx
        self._hostname = hostname
        self._hostnameBytes = _idnaBytes(hostname)
        self._hostnameASCII = self._hostnameBytes.decode('ascii')
        ctx.set_info_callback(_tolerateErrors(self._identityVerifyingInfoCallback))

    def clientConnectionForTLS(self, tlsProtocol):
        context = self._ctx
        connection = SSL.Connection(context, None)
        connection.set_app_data(tlsProtocol)
        return connection

    def _identityVerifyingInfoCallback(self, connection, where, ret):
        if where & SSL_CB_HANDSHAKE_START:
            _maybeSetHostNameIndication(connection, self._hostnameBytes)
        elif where & SSL_CB_HANDSHAKE_DONE:
            try:
                verifyHostname(connection, self._hostnameASCII)
            except VerificationError:
                f = Failure()
                transport = connection.get_app_data()
                transport.failVerification(f)


def optionsForClientTLS(hostname, trustRoot=None, clientCertificate=None, **kw):
    extraCertificateOptions = kw.pop('extraCertificateOptions', None) or {}
    if trustRoot is None:
        trustRoot = platformTrust()
    if kw:
        raise TypeError(("optionsForClientTLS() got an unexpected keyword argument '{arg}'").format(arg=kw.popitem()[0]))
    if not isinstance(hostname, unicode):
        raise TypeError('optionsForClientTLS requires text for host names, not ' + hostname.__class__.__name__)
    if clientCertificate:
        extraCertificateOptions.update(privateKey=clientCertificate.privateKey.original, certificate=clientCertificate.original)
    certificateOptions = OpenSSLCertificateOptions(trustRoot=trustRoot, **extraCertificateOptions)
    return ClientTLSOptions(hostname, certificateOptions.getContext())


class OpenSSLCertificateOptions(object):
    _contextFactory = SSL.Context
    _context = None
    _OP_ALL = getattr(SSL, 'OP_ALL', 65535)
    _OP_NO_TICKET = getattr(SSL, 'OP_NO_TICKET', 16384)
    _OP_NO_COMPRESSION = getattr(SSL, 'OP_NO_COMPRESSION', 131072)
    _OP_CIPHER_SERVER_PREFERENCE = getattr(SSL, 'OP_CIPHER_SERVER_PREFERENCE ', 4194304)
    _OP_SINGLE_ECDH_USE = getattr(SSL, 'OP_SINGLE_ECDH_USE ', 524288)

    @_mutuallyExclusiveArguments([
     [
      'trustRoot', 'requireCertificate'],
     [
      'trustRoot', 'verify'],
     [
      'trustRoot', 'caCerts']])
    def __init__(self, privateKey=None, certificate=None, method=None, verify=False, caCerts=None, verifyDepth=9, requireCertificate=True, verifyOnce=True, enableSingleUseKeys=True, enableSessions=True, fixBrokenPeers=False, enableSessionTickets=False, extraCertChain=None, acceptableCiphers=None, dhParameters=None, trustRoot=None):
        if (privateKey is None) != (certificate is None):
            raise ValueError('Specify neither or both of privateKey and certificate')
        self.privateKey = privateKey
        self.certificate = certificate
        self._options = SSL.OP_NO_SSLv2 | self._OP_NO_COMPRESSION | self._OP_CIPHER_SERVER_PREFERENCE
        if method is None:
            self.method = SSL.SSLv23_METHOD
            self._options |= SSL.OP_NO_SSLv3
        else:
            self.method = method
        if verify and not caCerts:
            raise ValueError('Specify client CA certificate information if and only if enabling certificate verification')
        self.verify = verify
        if extraCertChain is not None and None in (privateKey, certificate):
            raise ValueError('A private key and a certificate are required when adding a supplemental certificate chain.')
        if extraCertChain is not None:
            self.extraCertChain = extraCertChain
        else:
            self.extraCertChain = []
        self.caCerts = caCerts
        self.verifyDepth = verifyDepth
        self.requireCertificate = requireCertificate
        self.verifyOnce = verifyOnce
        self.enableSingleUseKeys = enableSingleUseKeys
        if enableSingleUseKeys:
            self._options |= SSL.OP_SINGLE_DH_USE | self._OP_SINGLE_ECDH_USE
        self.enableSessions = enableSessions
        self.fixBrokenPeers = fixBrokenPeers
        if fixBrokenPeers:
            self._options |= self._OP_ALL
        self.enableSessionTickets = enableSessionTickets
        if not enableSessionTickets:
            self._options |= self._OP_NO_TICKET
        self.dhParameters = dhParameters
        try:
            self._ecCurve = _OpenSSLECCurve(_defaultCurveName)
        except NotImplementedError:
            self._ecCurve = None

        if acceptableCiphers is None:
            acceptableCiphers = defaultCiphers
        self._cipherString = (':').join(c.fullName for c in acceptableCiphers.selectCiphers(_expandCipherString('ALL', self.method, self._options)))
        if self._cipherString == '':
            raise ValueError('Supplied IAcceptableCiphers yielded no usable ciphers on this platform.')
        if trustRoot is None:
            if self.verify:
                trustRoot = OpenSSLCertificateAuthorities(caCerts)
        else:
            self.verify = True
            self.requireCertificate = True
            trustRoot = IOpenSSLTrustRoot(trustRoot)
        self.trustRoot = trustRoot
        return

    def __getstate__(self):
        d = self.__dict__.copy()
        try:
            del d['_context']
        except KeyError:
            pass

        return d

    def __setstate__(self, state):
        self.__dict__ = state

    def getContext(self):
        if self._context is None:
            self._context = self._makeContext()
        return self._context

    def _makeContext(self):
        ctx = self._contextFactory(self.method)
        ctx.set_options(self._options)
        if self.certificate is not None and self.privateKey is not None:
            ctx.use_certificate(self.certificate)
            ctx.use_privatekey(self.privateKey)
            for extraCert in self.extraCertChain:
                ctx.add_extra_chain_cert(extraCert)

            ctx.check_privatekey()
        verifyFlags = SSL.VERIFY_NONE
        if self.verify:
            verifyFlags = SSL.VERIFY_PEER
            if self.requireCertificate:
                verifyFlags |= SSL.VERIFY_FAIL_IF_NO_PEER_CERT
            if self.verifyOnce:
                verifyFlags |= SSL.VERIFY_CLIENT_ONCE
            self.trustRoot._addCACertsToContext(ctx)

        def _verifyCallback(conn, cert, errno, depth, preverify_ok):
            return preverify_ok

        ctx.set_verify(verifyFlags, _verifyCallback)
        if self.verifyDepth is not None:
            ctx.set_verify_depth(self.verifyDepth)
        if self.enableSessions:
            name = '%s-%d' % (reflect.qual(self.__class__), _sessionCounter())
            sessionName = md5(networkString(name)).hexdigest()
            ctx.set_session_id(sessionName)
        if self.dhParameters:
            ctx.load_tmp_dh(self.dhParameters._dhFile.path)
        ctx.set_cipher_list(nativeString(self._cipherString))
        if self._ecCurve is not None:
            try:
                self._ecCurve.addECKeyToContext(ctx)
            except BaseException:
                pass

        return ctx


OpenSSLCertificateOptions.__getstate__ = deprecated(Version('Twisted', 15, 0, 0), 'a real persistence system')(OpenSSLCertificateOptions.__getstate__)
OpenSSLCertificateOptions.__setstate__ = deprecated(Version('Twisted', 15, 0, 0), 'a real persistence system')(OpenSSLCertificateOptions.__setstate__)

class _OpenSSLECCurve(FancyEqMixin, object):
    compareAttributes = ('snName', )

    def __init__(self, snName):
        self.snName = nativeString(snName)
        try:
            binding = self._getBinding()
            self._lib = binding.lib
            self._ffi = binding.ffi
            self._nid = self._lib.OBJ_sn2nid(self.snName.encode('ascii'))
            if self._nid == self._lib.NID_undef:
                raise ValueError('Unknown ECC curve.')
        except AttributeError:
            raise NotImplementedError('This version of pyOpenSSL does not support ECC.')

    def _getBinding(self):
        try:
            from OpenSSL._util import binding
            return binding
        except ImportError:
            raise NotImplementedError('This version of pyOpenSSL does not support ECC.')

    def addECKeyToContext(self, context):
        ecKey = self._lib.EC_KEY_new_by_curve_name(self._nid)
        if ecKey == self._ffi.NULL:
            raise EnvironmentError('EC key creation failed.')
        self._lib.SSL_CTX_set_tmp_ecdh(context._context, ecKey)
        self._lib.EC_KEY_free(ecKey)


@implementer(ICipher)
class OpenSSLCipher(FancyEqMixin, object):
    compareAttributes = ('fullName', )

    def __init__(self, fullName):
        self.fullName = fullName

    def __repr__(self):
        return ('OpenSSLCipher({0!r})').format(self.fullName)


def _expandCipherString(cipherString, method, options):
    ctx = SSL.Context(method)
    ctx.set_options(options)
    try:
        ctx.set_cipher_list(nativeString(cipherString))
    except SSL.Error as e:
        if e.args[0][0][2] == 'no cipher match':
            return []
        raise

    conn = SSL.Connection(ctx, None)
    ciphers = conn.get_cipher_list()
    if isinstance(ciphers[0], unicode):
        return [ OpenSSLCipher(cipher) for cipher in ciphers ]
    else:
        return [ OpenSSLCipher(cipher.decode('ascii')) for cipher in ciphers ]
        return


@implementer(IAcceptableCiphers)
class OpenSSLAcceptableCiphers(object):

    def __init__(self, ciphers):
        self._ciphers = ciphers

    def selectCiphers(self, availableCiphers):
        return [ cipher for cipher in self._ciphers if cipher in availableCiphers
               ]

    @classmethod
    def fromOpenSSLCipherString(cls, cipherString):
        return cls(_expandCipherString(nativeString(cipherString), SSL.SSLv23_METHOD, SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3))


defaultCiphers = OpenSSLAcceptableCiphers.fromOpenSSLCipherString('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS')
_defaultCurveName = 'prime256v1'

class OpenSSLDiffieHellmanParameters(object):

    def __init__(self, parameters):
        self._dhFile = parameters

    @classmethod
    def fromFile(cls, filePath):
        return cls(filePath)
# okay decompiling out\twisted.internet._sslverify.pyc
