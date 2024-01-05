# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.web
from twisted.web.client import getPage
from twisted.internet.defer import Deferred
from collections import namedtuple
from aoslib.tools import get_server_details
import json
SERVER_LIST = 'http://staging.ace-spades.com/serverlist.json'

class ServerEntry(object):

    def __init__(self, value):
        for k, v in value.iteritems():
            setattr(self, k, v)


def got_servers(data, defer):
    data = json.loads(data)
    entries = []
    for entry in data:
        ip, port = get_server_details(entry['identifier'])
        entry['ip'] = ip
        entry['port'] = port
        entries.append(ServerEntry(entry))

    defer.callback(entries)


def err(e):
    print e


def get_servers():
    defer = Deferred()
    getPage(SERVER_LIST).addCallback(got_servers, defer).addErrback(err)
    return defer
# okay decompiling out\aoslib.web.pyc
