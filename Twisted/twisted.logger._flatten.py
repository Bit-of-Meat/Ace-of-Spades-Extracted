# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\twisted.logger._flatten
from string import Formatter
from collections import defaultdict
from twisted.python.compat import unicode
aFormatter = Formatter()

class KeyFlattener(object):

    def __init__(self):
        self.keys = defaultdict((lambda : 0))

    def flatKey(self, fieldName, formatSpec, conversion):
        result = ('{fieldName}!{conversion}:{formatSpec}').format(fieldName=fieldName, formatSpec=formatSpec or '', conversion=conversion or '')
        self.keys[result] += 1
        n = self.keys[result]
        if n != 1:
            result += '/' + str(self.keys[result])
        return result


def flattenEvent(event):
    if 'log_format' not in event:
        return
    else:
        if 'log_flattened' in event:
            fields = event['log_flattened']
        else:
            fields = {}
        keyFlattener = KeyFlattener()
        for literalText, fieldName, formatSpec, conversion in aFormatter.parse(event['log_format']):
            if fieldName is None:
                continue
            if conversion != 'r':
                conversion = 's'
            flattenedKey = keyFlattener.flatKey(fieldName, formatSpec, conversion)
            structuredKey = keyFlattener.flatKey(fieldName, formatSpec, '')
            if flattenedKey in fields:
                continue
            if fieldName.endswith('()'):
                fieldName = fieldName[:-2]
                callit = True
            else:
                callit = False
            field = aFormatter.get_field(fieldName, (), event)
            fieldValue = field[0]
            if conversion == 'r':
                conversionFunction = repr
            else:
                conversionFunction = str
            if callit:
                fieldValue = fieldValue()
            flattenedValue = conversionFunction(fieldValue)
            fields[flattenedKey] = flattenedValue
            fields[structuredKey] = fieldValue

        if fields:
            event['log_flattened'] = fields
        return


def extractField(field, event):
    keyFlattener = KeyFlattener()
    (literalText, fieldName, formatSpec, conversion), = aFormatter.parse('{' + field + '}')
    key = keyFlattener.flatKey(fieldName, formatSpec, conversion)
    if 'log_flattened' not in event:
        flattenEvent(event)
    return event['log_flattened'][key]


def flatFormat(event):
    fieldValues = event['log_flattened']
    s = []
    keyFlattener = KeyFlattener()
    formatFields = aFormatter.parse(event['log_format'])
    for literalText, fieldName, formatSpec, conversion in formatFields:
        s.append(literalText)
        if fieldName is not None:
            key = keyFlattener.flatKey(fieldName, formatSpec, conversion or 's')
            s.append(unicode(fieldValues[key]))

    return ('').join(s)
# okay decompiling out\twisted.logger._flatten.pyc
