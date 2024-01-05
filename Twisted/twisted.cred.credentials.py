# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.cred.credentials
from __future__ import division, absolute_import
from zope.interface import implementer, Interface
import base64, hmac, random, re, time
from binascii import hexlify
from hashlib import md5
from twisted.python.randbytes import secureRandom
from twisted.python.compat import networkString, nativeString
from twisted.python.compat import intToBytes, unicode
from twisted.cred._digest import calcResponse, calcHA1, calcHA2
from twisted.cred import error

class ICredentials(Interface):
    pass


class IUsernameDigestHash(ICredentials):

    def checkHash(digestHash):
        pass


class IUsernameHashedPassword(ICredentials):

    def checkPassword(password):
        pass


class IUsernamePassword(ICredentials):

    def checkPassword(password):
        pass


class IAnonymous(ICredentials):
    pass


@implementer(IUsernameHashedPassword, IUsernameDigestHash)
class DigestedCredentials(object):

    def __init__(self, username, method, realm, fields):
        self.username = username
        self.method = method
        self.realm = realm
        self.fields = fields

    def checkPassword(self, password):
        response = self.fields.get('response')
        uri = self.fields.get('uri')
        nonce = self.fields.get('nonce')
        cnonce = self.fields.get('cnonce')
        nc = self.fields.get('nc')
        algo = self.fields.get('algorithm', 'md5').lower()
        qop = self.fields.get('qop', 'auth')
        expected = calcResponse(calcHA1(algo, self.username, self.realm, password, nonce, cnonce), calcHA2(algo, self.method, uri, qop, None), algo, nonce, nc, cnonce, qop)
        return expected == response

    def checkHash(self, digestHash):
        response = self.fields.get('response')
        uri = self.fields.get('uri')
        nonce = self.fields.get('nonce')
        cnonce = self.fields.get('cnonce')
        nc = self.fields.get('nc')
        algo = self.fields.get('algorithm', 'md5').lower()
        qop = self.fields.get('qop', 'auth')
        expected = calcResponse(calcHA1(algo, None, None, None, nonce, cnonce, preHA1=digestHash), calcHA2(algo, self.method, uri, qop, None), algo, nonce, nc, cnonce, qop)
        return expected == response


class DigestCredentialFactory(object):
    _parseparts = re.compile('([^= ]+)=(?:"([^"]*)"|([^,]+)),?')
    CHALLENGE_LIFETIME_SECS = 900
    scheme = 'digest'

    def __init__(self, algorithm, authenticationRealm):
        self.algorithm = algorithm
        self.authenticationRealm = authenticationRealm
        self.privateKey = secureRandom(12)

    def getChallenge(self, address):
        c = self._generateNonce()
        o = self._generateOpaque(c, address)
        return {'nonce': c, 'opaque': o, 
           'qop': 'auth', 
           'algorithm': self.algorithm, 
           'realm': self.authenticationRealm}

    def _generateNonce(self):
        return hexlify(secureRandom(12))

    def _getTime(self):
        return time.time()

    def _generateOpaque(self, nonce, clientip):
        now = intToBytes(int(self._getTime()))
        if not clientip:
            clientip = ''
        elif isinstance(clientip, unicode):
            clientip = clientip.encode('ascii')
        key = (',').join((nonce, clientip, now))
        digest = hexlify(md5(key + self.privateKey).digest())
        ekey = base64.b64encode(key)
        return ('-').join((digest, ekey.replace('\n', '')))

    def _verifyOpaque(self, opaque, nonce, clientip):
        opaqueParts = opaque.split('-')
        if len(opaqueParts) != 2:
            raise error.LoginFailed('Invalid response, invalid opaque value')
        if not clientip:
            clientip = ''
        else:
            if isinstance(clientip, unicode):
                clientip = clientip.encode('ascii')
            key = base64.b64decode(opaqueParts[1])
            keyParts = key.split(',')
            if len(keyParts) != 3:
                raise error.LoginFailed('Invalid response, invalid opaque value')
            if keyParts[0] != nonce:
                raise error.LoginFailed('Invalid response, incompatible opaque/nonce values')
            if keyParts[1] != clientip:
                raise error.LoginFailed('Invalid response, incompatible opaque/client values')
            try:
                when = int(keyParts[2])
            except ValueError:
                raise error.LoginFailed('Invalid response, invalid opaque/time values')

        if int(self._getTime()) - when > DigestCredentialFactory.CHALLENGE_LIFETIME_SECS:
            raise error.LoginFailed('Invalid response, incompatible opaque/nonce too old')
        digest = hexlify(md5(key + self.privateKey).digest())
        if digest != opaqueParts[0]:
            raise error.LoginFailed('Invalid response, invalid opaque value')
        return True

    def decode(self, response, method, host):
        response = (' ').join(response.splitlines())
        parts = self._parseparts.findall(response)
        auth = {}
        for key, bare, quoted in parts:
            value = (quoted or bare).strip()
            auth[nativeString(key.strip())] = value

        username = auth.get('username')
        if not username:
            raise error.LoginFailed('Invalid response, no username given.')
        if 'opaque' not in auth:
            raise error.LoginFailed('Invalid response, no opaque given.')
        if 'nonce' not in auth:
            raise error.LoginFailed('Invalid response, no nonce given.')
        if self._verifyOpaque(auth.get('opaque'), auth.get('nonce'), host):
            return DigestedCredentials(username, method, self.authenticationRealm, auth)


@implementer(IUsernameHashedPassword)
class CramMD5Credentials(object):
    username = None
    challenge = ''
    response = ''

    def __init__(self, host=None):
        self.host = host

    def getChallenge(self):
        if self.challenge:
            return self.challenge
        else:
            r = random.randrange(2147483647)
            t = time.time()
            self.challenge = networkString('<%d.%d@%s>' % (
             r, t, nativeString(self.host) if self.host else None))
            return self.challenge

    def setResponse(self, response):
        self.username, self.response = response.split(None, 1)
        return

    def moreChallenges(self):
        return False

    def checkPassword(self, password):
        verify = hexlify(hmac.HMAC(password, self.challenge).digest())
        return verify == self.response


@implementer(IUsernameHashedPassword)
class UsernameHashedPassword:

    def __init__(self, username, hashed):
        self.username = username
        self.hashed = hashed

    def checkPassword(self, password):
        return self.hashed == password


@implementer(IUsernamePassword)
class UsernamePassword:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkPassword(self, password):
        return self.password == password


@implementer(IAnonymous)
class Anonymous:
    pass


class ISSHPrivateKey(ICredentials):
    pass


@implementer(ISSHPrivateKey)
class SSHPrivateKey:

    def __init__(self, username, algName, blob, sigData, signature):
        self.username = username
        self.algName = algName
        self.blob = blob
        self.sigData = sigData
        self.signature = signature
# okay decompiling out\twisted.cred.credentials.pyc
