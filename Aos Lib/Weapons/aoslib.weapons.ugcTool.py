# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.ugcTool
from tool import Tool
from . import TOOL_IMAGES
from aoslib.models import *
from aoslib.models import UGC_ENTITY_MODELS
from aoslib.shaders import *
from aoslib.draw import DisplayList
from pyglet.gl import *
from shared.constants import *
from aoslib import strings
from aoslib.animations.animPlaceBlock import *

class UGCTool(Tool):
    name = strings.A337
    damage = None
    sight = None
    shoot_sound = None
    model = [UGC_TOOL_MODEL]
    view_model = [UGC_TOOL_VIEW_MODEL]
    tracer = None
    shoot_interval = A2005
    secondary_shoot_interval = A2005
    ghost_position = None
    can_place_spawnpoint = False
    image = TOOL_IMAGES[A337]
    ugc_loadout_index = 0
    ugc_item_id = A482
    ghost_display = []
    models = {A482: [
            UGC_TOOL_MODEL], 
       A483: [
            UGC_TOOL_MODEL], 
       A484: [
            UGC_TOOL_MODEL], 
       A485: [
            UGC_TOOL_MODEL], 
       A486: [
            UGC_TOOL_MODEL], 
       A489: [
            UGC_TOOL_MODEL], 
       A492: [
            UGC_TOOL_MODEL], 
       A495: [
            UGC_TOOL_MODEL], 
       A498: [
            UGC_TOOL_MODEL], 
       A487: [
            UGC_TOOL_MODEL], 
       A490: [
            UGC_TOOL_MODEL], 
       A493: [
            UGC_TOOL_MODEL], 
       A496: [
            UGC_TOOL_MODEL], 
       A499: [
            UGC_TOOL_MODEL], 
       A488: [
            UGC_TOOL_MODEL], 
       A491: [
            UGC_TOOL_MODEL], 
       A494: [
            UGC_TOOL_MODEL], 
       A497: [
            UGC_TOOL_MODEL], 
       A500: [
            UGC_TOOL_MODEL]}
    view_models = {A482: [
            UGC_TOOL_VIEW_MODEL], 
       A483: [
            UGC_TOOL_VIEW_MODEL], 
       A484: [
            UGC_TOOL_VIEW_MODEL], 
       A485: [
            UGC_TOOL_VIEW_MODEL], 
       A486: [
            UGC_TOOL_VIEW_MODEL], 
       A489: [
            UGC_TOOL_VIEW_MODEL], 
       A492: [
            UGC_TOOL_VIEW_MODEL], 
       A495: [
            UGC_TOOL_VIEW_MODEL], 
       A498: [
            UGC_TOOL_VIEW_MODEL], 
       A487: [
            UGC_TOOL_VIEW_MODEL], 
       A490: [
            UGC_TOOL_VIEW_MODEL], 
       A493: [
            UGC_TOOL_VIEW_MODEL], 
       A496: [
            UGC_TOOL_VIEW_MODEL], 
       A499: [
            UGC_TOOL_VIEW_MODEL], 
       A488: [
            UGC_TOOL_VIEW_MODEL], 
       A491: [
            UGC_TOOL_VIEW_MODEL], 
       A494: [
            UGC_TOOL_VIEW_MODEL], 
       A497: [
            UGC_TOOL_VIEW_MODEL], 
       A500: [
            UGC_TOOL_VIEW_MODEL]}
    model_offsets = {A482: (0.0, 0.0, 0.0), 
       A483: (0.0, 0.0, 0.0), 
       A484: (0.0, 0.0, 0.0), 
       A485: (0.0, 0.0, 0.0), 
       A486: (0.0, 0.0, 0.0), 
       A489: (0.0, 0.0, 0.0), 
       A492: (0.0, 0.0, 0.0), 
       A495: (0.0, 0.0, 0.0), 
       A498: (0.0, 0.0, 0.0), 
       A487: (0.0, 0.0, 0.0), 
       A490: (0.0, 0.0, 0.0), 
       A493: (0.0, 0.0, 0.0), 
       A496: (0.0, 0.0, 0.0), 
       A499: (0.0, 0.0, 0.0), 
       A488: (0.0, 0.0, 0.0), 
       A491: (0.0, 0.0, 0.0), 
       A494: (0.0, 0.0, 0.0), 
       A497: (0.0, 0.0, 0.0), 
       A500: (0.0, 0.0, 0.0)}

    def __init__(self, character):
        super(UGCTool, self).__init__(character)
        self.animations['place_block'] = AnimPlaceBlock(self.shoot_interval)
        self.item_groups = {}
        self.group_indices = {}

    def reset_item_groups_and_indices(self):
        self.item_groups.clear()
        self.group_indices.clear()

    def set_ugc_tool_id(self, ugc_loadout_index, ugc_item_id):
        self.ugc_loadout_index = ugc_loadout_index
        if ugc_loadout_index not in self.item_groups:
            self.update_item_groups_and_indices = False
            self.original_ugc_tool_id = ugc_item_id
            for click_group, item_ids in A507.iteritems():
                if ugc_item_id in item_ids:
                    self.item_groups[self.ugc_loadout_index] = click_group
                    self.group_indices[self.ugc_loadout_index] = item_ids.index(ugc_item_id)
                    break
            else:
                self.item_groups[self.ugc_loadout_index] = None
                self.group_indices[self.ugc_loadout_index] = None

        if self.item_groups[self.ugc_loadout_index] is None:
            self.select_ugc_item(ugc_item_id)
        else:
            self.select_ugc_item_index(self.group_indices[self.ugc_loadout_index])
        return

    def get_ugc_tool_id(self, ugc_loadout_index):
        if ugc_loadout_index in self.item_groups:
            if ugc_loadout_index in self.item_groups:
                group = self.item_groups[ugc_loadout_index]
                if group is not None:
                    ugc_items = A507[self.item_groups[ugc_loadout_index]]
                    index = self.group_indices[ugc_loadout_index]
                    return ugc_items[index]
            return
        return

    def select_ugc_item_index(self, index):
        self.group_indices[self.ugc_loadout_index] = index
        if self.item_groups[self.ugc_loadout_index] == None:
            return
        else:
            ugc_item_ids = A507[self.item_groups[self.ugc_loadout_index]]
            self.select_ugc_item(ugc_item_ids[index])
            return

    def select_ugc_item(self, ugc_item_id):
        self.ugc_item_id = ugc_item_id
        self.model = self.models[self.ugc_item_id]
        self.view_model = self.view_models[self.ugc_item_id]
        model_offset = self.model_offsets[self.ugc_item_id]
        for model_index in range(len(self.view_model)):
            self.initial_position[model_index] = Vector3(model_offset[0], model_offset[1], model_offset[2])
            self.reset_position(model_index)
            self.reset_orientation(model_index)

        self.arms_position_offset = Vector3(-model_offset[0], -model_offset[1], -model_offset[2])
        self.ghost_display = self.create_ugc_entity_display(self.ugc_item_id)

    def create_ugc_entity_display(self, ugc_item_id):
        model, size, offset = UGC_ENTITY_MODELS[ugc_item_id]
        display = []
        for model_index in range(len(model)):
            display.append(DisplayList(model[model_index]))
            display[model_index].size = 0.06

        display[1].size = display[1].size * size
        display[1].z = offset
        return display

    def on_start_primary(self):
        super(UGCTool, self).on_start_primary()
        if not self.character.main:
            return False
        else:
            if not self.ghost_position:
                self.play_sound(A2827)
                return False
            entity = self.is_pointing_at_ugc()
            if entity is None:
                if self.can_place_spawnpoint:
                    self.character.scene.send_place_ugc(self.ugc_item_id, self.ghost_position, True)
                    self.animations['place_block'].start()
            else:
                self.character.scene.send_place_ugc(entity.ugc_item_id, self.ghost_position, False)
                self.animations['place_block'].start()
            return True

    def use_secondary(self):
        super(UGCTool, self).use_secondary()
        return True

    def on_start_secondary(self):
        super(UGCTool, self).on_start_secondary()
        if not self.character.main:
            return False
        else:
            entity = self.is_pointing_at_ugc()
            if entity is None:
                if self.item_groups[self.ugc_loadout_index] is None:
                    return False
                if self.group_indices[self.ugc_loadout_index] is None:
                    return False
                ugc_items = A507[self.item_groups[self.ugc_loadout_index]]
                index = self.group_indices[self.ugc_loadout_index]
                index = (index + 1) % len(ugc_items)
                self.select_ugc_item_index(index)
            else:
                item_id = entity.ugc_item_id
                for click_group, item_ids in A507.iteritems():
                    if item_id in item_ids:
                        self.character.scene.send_place_ugc(item_id, self.ghost_position, False)
                        index = item_ids.index(item_id)
                        index = (index + 1) % len(item_ids)
                        self.character.scene.send_place_ugc(item_ids[index], self.ghost_position, True)
                        break
                else:
                    return False

            return True

    def is_pointing_at_ugc(self):
        if self.ghost_position is None:
            return
        else:
            pointed_at = self.character.scene.is_object_on_entity_of_class(self.ghost_position[0], self.ghost_position[1], self.ghost_position[2], 1.0, [A928])
            return pointed_at

    def draw_ghosting(self):
        self.ghost_position = None
        self.can_place_spawnpoint, ret = self.character.scene.can_place_object(self.character, A2006, player_min_radius=0, entity_min_radius=1, others_min_radius=0, can_place_vertical=False)
        if ret is None:
            self.can_place_spawnpoint = False
            return
        else:
            position, face = ret
            self.ghost_position = position.get()
            if self.can_place_spawnpoint:
                glPushMatrix()
                glTranslatef(position.x + 0.5, -position.z, position.y + 0.5)
                MODEL_SHADER.bind()
                MODEL_SHADER.uniformf_loc(MODEL_SHADER_BLEND_COLOR_LOC, 1.0, 1.0, 1.0, 0.3)
                for model_index in range(len(self.ghost_display)):
                    self.ghost_display[model_index].draw(frustum_check=False)

                MODEL_SHADER.uniformf_loc(MODEL_SHADER_BLEND_COLOR_LOC, 1.0, 1.0, 1.0, 1.0)
                MODEL_SHADER.unbind()
                glPopMatrix()
            return

    def is_available(self):
        return True
# okay decompiling out\aoslib.weapons.ugcTool.pyc
