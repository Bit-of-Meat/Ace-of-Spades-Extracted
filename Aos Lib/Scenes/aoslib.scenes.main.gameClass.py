# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.gameClass
from shared.constants import *
import aoslib.config
from aoslib import strings
from shared.constants_gamemode import A2447
from shared.constants_DLC import get_character_dlc_Name

class GameClass(object):

    def __init__(self, manager, id, disabled_tools, speed_multiplier, config=None, enable_fall_on_water_damage=True):
        self.id = id
        self.manager = manager
        self.disabled_tools = [] if disabled_tools is None else disabled_tools
        self.name = strings.get_by_id(A98[self.id])
        self.has_jetpack = False
        self.loadout = self.build_class_loadout(config)
        self.gun = self.loadout[0]
        self.damage_multiplier = A2401[self.id]
        self.accel_multiplier = A2402[self.id] * speed_multiplier
        self.sprint_multiplier = A2403[self.id] * speed_multiplier
        self.crouch_sneak_multiplier = A2404[self.id] * speed_multiplier
        if enable_fall_on_water_damage:
            self.fall_on_water_damage_multiplier = A2405[self.id]
        else:
            self.fall_on_water_damage_multiplier = 0.0
        self.jump_multiplier = A2406[self.id]
        self.can_sprint_uphill = A2407[self.id]
        self.water_friction = A2408[self.id]
        self.falling_damage_min_distance = A2409[self.id]
        self.falling_damage_max_distance = A2410[self.id]
        self.falling_damage_max_damage = A2411[self.id]
        self.body_parts = A268[self.id]
        self.prefabs = []
        self.ugc_tools = []
        if self.manager.game_mode == A2447 or A319 in self.disabled_tools or self.manager.is_in_mafia_mode():
            self.get_prefabs(config, 0)
        else:
            self.get_prefabs(config, 3)
        self.get_ugc_tools(config, 0)
        return

    def get_prefabs(self, config, noof_selected_prefabs):
        class_id = self.id
        if config and not self.manager.game_mode != A2447:
            saved_prefabs = getattr(config, aoslib.config.prefab_name(class_id))
        else:
            saved_prefabs = []
        available_prefabs = []
        for prefab_list_index in A554[class_id][A519]:
            prefab_list = A481[prefab_list_index]
            for prefab in prefab_list:
                available_prefabs.append(prefab)

        self.prefabs = []
        for saved_prefab in saved_prefabs:
            if saved_prefab in available_prefabs:
                self.prefabs.append(saved_prefab)

        prefab_index = 0
        while len(self.prefabs) < noof_selected_prefabs and len(available_prefabs) >= noof_selected_prefabs:
            if available_prefabs[prefab_index] not in self.prefabs:
                self.prefabs.append(available_prefabs[prefab_index])
            prefab_index += 1

    def get_ugc_tools(self, config, noof_selected_tools):
        class_id = self.id
        available_tools = []
        for tool_list_index in A554[class_id][A521]:
            tool_list = A509[tool_list_index]
            for tool in tool_list:
                available_tools.append(tool)

        tool_index = 0
        while len(self.ugc_tools) < noof_selected_tools and len(available_tools) >= noof_selected_tools:
            if available_tools[tool_index] not in self.ugc_tools:
                self.ugc_tools.append(available_tools[tool_index])
            tool_index += 1

    def get_valid_items(self, items, saved_items, noof_selected_items=1):
        valid_items = []
        if len(items):
            valid_item = -1
            for item in items:
                if item in saved_items and item not in self.disabled_tools:
                    valid_items.append(item)
                    if len(valid_items) == noof_selected_items:
                        break

            if len(valid_items) == 0:
                for item in items:
                    if len(valid_items) < noof_selected_items and item not in self.disabled_tools:
                        valid_items.append(item)

        return valid_items

    def set_common_loadout_items(self, loadout, add_flareblock=False):
        class_items = A554[self.id]
        for item in class_items[A520]:
            if item in self.disabled_tools:
                continue
            if item == A318 and add_flareblock == False:
                continue
            if item == A301:
                loadout.insert(0, item)
                continue
            loadout.append(item)

    def build_class_loadout(self, config):
        class_id = self.id
        if config:
            saved_loadout = getattr(config, aoslib.config.loadout_name(class_id))
        else:
            saved_loadout = []
        loadout = []
        class_items = A554[class_id]
        for index in xrange(A523):
            if index == A519:
                continue
            items = self.get_valid_items(class_items[index], saved_loadout)
            for valid_item in items:
                loadout.append(valid_item)
                if valid_item == A364:
                    self.has_jetpack = True
                elif valid_item == A370:
                    self.has_parachute = True

        self.set_common_loadout_items(loadout)
        if not self.manager.is_in_mafia_mode():
            if A318 not in self.disabled_tools:
                loadout.append(A318)
            if A319 not in self.disabled_tools:
                loadout.append(A319)
        return loadout

    def is_selectable(self):
        selectable = True
        dlcName = get_character_dlc_Name(self.id)
        if dlcName != None:
            if not self.manager.dlc_manager.is_installed_dlc(dlcName):
                selectable = False
        return selectable
# okay decompiling out\aoslib.scenes.main.gameClass.pyc
