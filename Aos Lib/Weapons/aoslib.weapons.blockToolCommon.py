# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.blockToolCommon
from tool import Tool
from aoslib.world import get_next_cube, cube_line
from aoslib import strings
from aoslib.draw import draw_cube
from pyglet.gl import glLineWidth
from shared.glm import IntVector3
from shared.constants import A1017, A1012, A2215
from shared.hud_constants import BIG_TEXT_TIME_1FRAME

class BlockToolCommon(Tool):
    hit_cube = old_hit_cube = None
    old_hit_cube_adjacent = False
    valid_placement = False

    def __init__(self, character):
        super(BlockToolCommon, self).__init__(character)
        self.block_cost = 1

    def draw_ghosting(self):
        character = self.character
        player = character.world_object
        self.valid_placement = True
        position = None
        check_bridge_placement = False
        if not character.scene.manager.classic:
            max_block_distance = A1017 if 1 else A1012
            big_message_this_frame = False
            ret = character.scene.world.hitscan(player.position, player.orientation)
            if ret is None:
                self.hit_cube = None
                check_bridge_placement = True
                self.valid_placement = False
            else:
                position = get_next_cube(*ret)
                can_place_block = self.character.scene.can_place_block_on_player(position)
                if can_place_block == False:
                    if not big_message_this_frame:
                        big_message_this_frame = True
                        self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_FAIL_SOMETHING_IN_THE_WAY, duration=BIG_TEXT_TIME_1FRAME)
                    self.valid_placement = False
                elif not player.check_cube_placement(position, max_block_distance):
                    check_bridge_placement = True
                    cube_sq_distance = player.get_cube_sq_distance()
                    if cube_sq_distance < max_block_distance * max_block_distance:
                        max_block_distance = math.sqrt(cube_sq_distance)
            if check_bridge_placement:
                bridge_position, bridge_valid, floating_blocks = self.character.scan_bridge_placement(player.position, player.orientation, max_block_distance)
                if not bridge_valid and bridge_position != None and not big_message_this_frame:
                    big_message_this_frame = True
                    if floating_blocks:
                        self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_FAIL_NOT_ATTACHED, duration=BIG_TEXT_TIME_1FRAME)
                    else:
                        self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_FAIL_TOO_FAR, duration=BIG_TEXT_TIME_1FRAME)
                if bridge_position is not None:
                    position = bridge_position
                    self.valid_placement = bridge_valid
                else:
                    self.valid_placement = False
            self.hit_cube = position
            if position:
                block_line = self.get_block_line(include_solids=False)
                if len(block_line) > 0:
                    first_block = block_line[0]
                    map = self.character.scene.map
                    self.old_hit_cube_adjacent = False
                    if map.has_neighbors(first_block[0], first_block[1], first_block[2], False):
                        self.old_hit_cube_adjacent = True
                    if not self.character.scene.block_manager.is_space_to_add_blocks():
                        big_message_this_frame = big_message_this_frame or True
                        self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_UGC_CAPACITY, duration=BIG_TEXT_TIME_1FRAME)
                    self.valid_placement = False
                else:
                    for x, y, z, sufficient_ammo, unobstructed in block_line:
                        if not unobstructed or not self.character.scene.block_manager.valid_to_add(x, y, z):
                            if not big_message_this_frame:
                                big_message_this_frame = True
                                if z > self.character.scene.block_manager.max_modifiable_z:
                                    self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_FAIL_WATER, duration=BIG_TEXT_TIME_1FRAME)
                                else:
                                    self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_FAIL_SOMETHING_IN_THE_WAY, duration=BIG_TEXT_TIME_1FRAME)
                            self.valid_placement = False
                            break
                        elif not sufficient_ammo:
                            if not big_message_this_frame:
                                big_message_this_frame = True
                                self.character.scene.hud.add_big_messageBackGround(strings.BLOCK_PLACE_FAIL_NOT_ENOUGH_BLOCKS, duration=BIG_TEXT_TIME_1FRAME)
                            self.valid_placement = False
                            break

                color = (character.block_color if self.valid_placement and self.old_hit_cube_adjacent else (255,
                                                                                                            0,
                                                                                                            0)) + (80, )
                for x, y, z, _, _ in reversed(block_line):
                    draw_cube(x, y, z, color, textured_wireframe=self.character.scene.manager.classic)

        return

    def get_block_line(self, with_state=True, include_solids=True):
        if not self.hit_cube:
            return []
        x, y, z = self.hit_cube.get()
        old_cube = self.old_hit_cube
        if old_cube:
            x2, y2, z2 = old_cube.get()
            cubes = cube_line(x2, y2, z2, x, y, z)
        else:
            cubes = [
             (
              x, y, z)]
        if not include_solids:
            map = self.character.scene.map
            if not map:
                return []
            cubes = [ cube for cube in cubes if not map.get_solid(cube[0], cube[1], cube[2]) ]
        if not with_state:
            return cubes
        new_cubes = []
        current_ammo = self.get_ammo()[0]
        infinite_blocks = False
        player = self.character.parent
        if player and player.team and player.team.infinite_blocks:
            infinite_blocks = True
        for i, (x, y, z) in enumerate(cubes):
            has_enough_ammo = infinite_blocks or (i + 1) * self.block_cost <= current_ammo
            int_block_position = IntVector3(x, y, z)
            can_place_block = self.character.scene.can_place_block_on_player(int_block_position)
            new_cubes.append((x, y, z, has_enough_ammo, can_place_block))

        return new_cubes

    def get_ammo(self):
        return (
         self.character.block_count, None)

    def use_secondary(self):
        super(BlockToolCommon, self).use_secondary()

    def can_shoot_secondary(self):
        return self.character.scene.manager.enable_colour_picker

    def use_custom(self):
        character = self.character
        if not character.scene.manager.enable_colour_picker:
            return False
        else:
            character.fire_secondary = False
            player = character.world_object
            max_block_distance = A1017 if not character.scene.manager.classic else A1012
            hit_scenery = character.scene.world.hitscan_accurate(player.position, player.orientation, max_block_distance)
            if hit_scenery == None:
                return False
            position, hit_block, face = hit_scenery
            if hit_block.z > A2215:
                return False
            solid, color = character.scene.map.get_point(hit_block.x, hit_block.y, hit_block.z)
            r, g, b, a = color
            self.set_block_color((r, g, b))
            character.pullout = 0.5
            palette = character.scene.hud.palette
            if palette is not None:
                palette.hide_selection()
            return

    def set_block_color(self, color):
        self.character.set_block_color(color)
# okay decompiling out\aoslib.weapons.blockToolCommon.pyc
