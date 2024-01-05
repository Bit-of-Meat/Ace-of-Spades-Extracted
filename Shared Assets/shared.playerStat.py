# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\shared.playerStat
import math
LEVEL_EASE_FACTOR = [
 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 
 1.0, 0.9792, 0.9779, 0.9766, 0.9753, 0.974, 0.9727, 0.9714, 0.9701, 0.9688, 
 0.9675, 0.9662, 0.9649, 0.9636, 0.9623, 0.961, 0.9597, 0.9584, 0.9571, 
 0.9558, 0.9545, 0.9532, 0.9519, 0.9506, 0.9493, 0.948, 0.9467, 0.9454, 
 0.9441, 0.9428, 0.9415, 0.9402, 0.9389, 0.9376, 0.9363, 0.935, 0.9337, 
 0.9324, 0.9311, 0.9298, 0.9285, 0.9272, 0.9259, 0.9246, 0.9233, 0.922, 
 0.9207, 0.9194, 0.9181, 0.9168, 0.9155, 0.9142, 0.9129, 0.9116, 0.9103, 
 0.909, 0.9077, 0.9064, 0.9051, 0.9038, 0.9025, 0.9012, 0.8999, 0.8986, 
 0.8973, 0.896, 0.8947, 0.8934, 0.8921, 0.8908, 0.8895, 0.8882, 0.8869, 
 0.8856, 0.8843, 0.883, 0.8817, 0.8804, 0.8791, 0.8778, 0.8765, 0.8752, 
 0.8739, 0.8726, 0.8713, 0.87]

class PlayerStat(object):

    def __init__(self, code=0, category='NONE', show_bar=False, show_score=False, level1_requirement=10, multiplier=1.15, value_modifier=None):
        self.code = code
        self.category = category
        self.count = 0
        self.score = 0
        self.value_modifier = value_modifier
        self.multiplier = multiplier
        self.show_bar = show_bar
        self.show_score = show_score
        self.level1_requirement = level1_requirement
        self.level = 1
        self.percentage = 0.0
        self.next_level_min = 0.0
        self.next_level_max = 0.0

    def calculate_level(self):
        res = self.__calculate_level(self.count, self.level1_requirement, self.multiplier)
        self.level = res['level']
        self.percentage = res['percentage']
        self.next_level_min = res['next_level_min']
        self.next_level_max = res['next_level_max']

    @staticmethod
    def __calculate_level(score, level1_requirement, multiplier):
        level = 1
        percentage = 0
        next_level_min = 0
        next_level_max = level1_requirement * LEVEL_EASE_FACTOR[0]
        for i in range(score):
            if i >= next_level_max:
                level = level + 1
                next_level_min = next_level_max
                next_level_max = next_level_max + level1_requirement * ((level - 1) * multiplier)
                if level in range(0, len(LEVEL_EASE_FACTOR)):
                    next_level_max = next_level_max * LEVEL_EASE_FACTOR[level]
                next_level_max = round(next_level_max)

        percentage = 100.0 / max(0.001, next_level_max - next_level_min) * (score - next_level_min)
        return {'level': level, 'percentage': percentage, 'next_level_min': next_level_min, 'next_level_max': next_level_max}

    @staticmethod
    def value_modifier_mins_to_hours(value):
        if value == 0:
            return 0
        return '%.2f' % (value / 60.0)

    @staticmethod
    def value_modifier_percentage(value):
        return str(int(value * 100)) + '%'
# okay decompiling out\shared.playerStat.pyc
