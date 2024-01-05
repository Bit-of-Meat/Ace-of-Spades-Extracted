# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.strings
from shared.steam import SteamGetCurrentGameLanguage
from shared.constants import *
from aoslib import text
import sys, english, german, french, spanish, italian, portuguese_brazil, russian, polish, turkish, spanish_mexico
LANG_ENGLISH, LANG_GERMAN, LANG_FRENCH, LANG_SPANISH, LANG_ITALIAN, LANG_BRAZILIAN, LANG_RUSSIAN, LANG_POLISH, LANG_TURKISH, LANG_MEXICAN = xrange(10)
language_ids = {'english': LANG_ENGLISH, 
   'german': LANG_GERMAN, 
   'french': LANG_FRENCH, 
   'spanish': LANG_SPANISH, 
   'italian': LANG_ITALIAN, 
   'brazilian': LANG_BRAZILIAN, 
   'portuguese_brazil': LANG_BRAZILIAN, 
   'russian': LANG_RUSSIAN, 
   'polish': LANG_POLISH, 
   'turkish': LANG_TURKISH, 
   'mexican': LANG_MEXICAN, 
   'spanish_mexico': LANG_MEXICAN}
try:
    language_arg = sys.argv.index('+language')
    language = sys.argv[language_arg + 1]
except:
    language = SteamGetCurrentGameLanguage()

print 'Language detected: ', language
if language == '':
    language = 'english'
local_language_id = language_ids[language]
if language == 'brazilian':
    language = 'portuguese_brazil'
else:
    if language == 'mexican':
        language = 'spanish_mexico'
    if language == 'russian' or language == 'polish':
        text.EDO_FONT = 'Spades'
        text.STANDARD_FONT = 'Tuffy_Bold'
        text.ALDO_FONT = 'Spades'
    if language == 'turkish':
        text.EDO_FONT = 'Edo'
        text.STANDARD_FONT = 'Tuffy_Bold'
        text.ALDO_FONT = 'Edo'
    text.set_fonts()
    try:
        language_strings = __import__(language, globals())
    except:
        language_strings = __import__('english', globals())

    for key, value in language_strings.__dict__.iteritems():
        globals()[key] = value

def language_requires_tuffy(language):
    return language == LANG_POLISH or language == LANG_TURKISH or language == LANG_RUSSIAN


def get_by_id(id):
    try:
        return globals()[id]
    except:
        if A2298:
            return 'Missing string ' + id
        else:
            return id


def get_by_id_or_except(id):
    return globals()[id]
# okay decompiling out\aoslib.strings.pyc
