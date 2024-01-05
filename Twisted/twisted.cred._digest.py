# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.cred._digest
from __future__ import division, absolute_import
from binascii import hexlify
from hashlib import md5, sha1
algorithms = {'md5': md5, 
   'md5-sess': md5, 
   'sha': sha1}

def calcHA1(pszAlg, pszUserName, pszRealm, pszPassword, pszNonce, pszCNonce, preHA1=None):
    if preHA1 and (pszUserName or pszRealm or pszPassword):
        raise TypeError('preHA1 is incompatible with the pszUserName, pszRealm, and pszPassword arguments')
    if preHA1 is None:
        m = algorithms[pszAlg]()
        m.update(pszUserName)
        m.update(':')
        m.update(pszRealm)
        m.update(':')
        m.update(pszPassword)
        HA1 = hexlify(m.digest())
    else:
        HA1 = preHA1
    if pszAlg == 'md5-sess':
        m = algorithms[pszAlg]()
        m.update(HA1)
        m.update(':')
        m.update(pszNonce)
        m.update(':')
        m.update(pszCNonce)
        HA1 = hexlify(m.digest())
    return HA1


def calcHA2(algo, pszMethod, pszDigestUri, pszQop, pszHEntity):
    m = algorithms[algo]()
    m.update(pszMethod)
    m.update(':')
    m.update(pszDigestUri)
    if pszQop == 'auth-int':
        m.update(':')
        m.update(pszHEntity)
    return hexlify(m.digest())


def calcResponse(HA1, HA2, algo, pszNonce, pszNonceCount, pszCNonce, pszQop):
    m = algorithms[algo]()
    m.update(HA1)
    m.update(':')
    m.update(pszNonce)
    m.update(':')
    if pszNonceCount and pszCNonce:
        m.update(pszNonceCount)
        m.update(':')
        m.update(pszCNonce)
        m.update(':')
        m.update(pszQop)
        m.update(':')
    m.update(HA2)
    respHash = hexlify(m.digest())
    return respHash
# okay decompiling out\twisted.cred._digest.pyc
