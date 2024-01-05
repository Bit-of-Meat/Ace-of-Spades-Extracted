# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\shared.constants_DLC
from constants_shop import *
from constants import *

class constants_DLC(object):
    pass


DLC_TOOLS = {DLC_AppName01: [], DLC_AppName02: [
                 A345, A346, A347, A348, A349, 
                 A350, A351, 
                 A353, 
                 A354, A356, A357, A358, A359]}
DLC_CHARACTERS = {DLC_AppName01: [], DLC_AppName02: [
                 A90, A91]}

def get_tool_dlc_Name(tool_id):
    dlc_AppName = None
    for k, v in DLC_TOOLS.iteritems():
        if tool_id in v:
            dlc_AppName = k
            break

    return dlc_AppName


def get_character_dlc_Name(character_id):
    dlc_AppName = None
    for k, v in DLC_CHARACTERS.iteritems():
        if character_id in v:
            dlc_AppName = k
            break

    return dlc_AppName


def is_tool_selectable(tool_id, dlc_manager):
    selectable = True
    dlcName = get_tool_dlc_Name(tool_id)
    if dlcName != None:
        if not dlc_manager.is_installed_dlc(dlcName):
            selectable = False
    return selectable


def is_character_selectable(character_id, dlc_manager):
    selectable = True
    dlcName = get_character_dlc_Name(character_id)
    if dlcName != None:
        if not dlc_manager.is_installed_dlc(dlcName):
            selectable = False
    return selectable
# okay decompiling out\shared.constants_DLC.pyc
