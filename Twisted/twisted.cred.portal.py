# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.cred.portal
from __future__ import division, absolute_import
from twisted.internet import defer
from twisted.internet.defer import maybeDeferred
from twisted.python import failure, reflect
from twisted.cred import error
from zope.interface import providedBy, Interface

class IRealm(Interface):

    def requestAvatar(avatarId, mind, *interfaces):
        pass


class Portal(object):

    def __init__(self, realm, checkers=()):
        self.realm = realm
        self.checkers = {}
        for checker in checkers:
            self.registerChecker(checker)

    def listCredentialsInterfaces(self):
        return list(self.checkers.keys())

    def registerChecker(self, checker, *credentialInterfaces):
        if not credentialInterfaces:
            credentialInterfaces = checker.credentialInterfaces
        for credentialInterface in credentialInterfaces:
            self.checkers[credentialInterface] = checker

    def login(self, credentials, mind, *interfaces):
        for i in self.checkers:
            if i.providedBy(credentials):
                return maybeDeferred(self.checkers[i].requestAvatarId, credentials).addCallback(self.realm.requestAvatar, mind, *interfaces)

        ifac = providedBy(credentials)
        return defer.fail(failure.Failure(error.UnhandledCredentials('No checker for %s' % (', ').join(map(reflect.qual, ifac)))))
# okay decompiling out\twisted.cred.portal.pyc
