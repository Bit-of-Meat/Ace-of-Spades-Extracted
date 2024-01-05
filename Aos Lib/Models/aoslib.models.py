# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.models
import os
from aoslib.kv6 import KV6
from aoslib.physfs import join
from shared.constants import *
import os, glob
from shared.common import *
import json
__all__ = []
__modeldetail = 2
__detaillevel = 2
KV6_PATH = 'kv6'
JETPACK_MODELS = {}
PARACHUTE_MODELS = {}
PARACHUTE_FPS_MODELS = {}
UGC_ENTITY_MODELS = {}
import model_crcs
from aoslib import loadingscreen

def get_kv6_model(name):
    if name in globals():
        return globals()[name]
    else:
        return


def check_model(name, crc, instance):
    valid_crc = False
    try:
        actual_crc = model_crcs.model_crcs[name.lower()]
        if actual_crc == crc:
            valid_crc = True
    except:
        pass

    if not valid_crc:
        if check_model_size(A2428, name, instance) == False:
            from aoslib.gamemanager import GameManager
            GameManager.invalid_data_error = True
            model_bounding_box = KV6.get_bounding_box_sizes(instance)
            print 'Asset Size Invalid Report (%s): Actual %s - Maximum: %s' % (repr(name), model_bounding_box, A2428)
        else:
            print 'Asset Warning - file has been altered (%s)' % name


def load_model(global_name, name, offset=None, prefab=False, ugc=False, min_model_detail=0):
    global __detaillevel
    global __modeldetail
    loadingscreen.update_progress()
    path = join(KV6_PATH, name + '.kv6')
    if ugc:
        path = join('ugc', path)
    detail_level = 2
    invscale = 1
    if not prefab:
        invscale = 3 - max(min_model_detail, __modeldetail)
        detail_level = __detaillevel
    display = KV6(path, A1043, offset, invscale=invscale, detail_level=detail_level)
    if global_name in __all__:
        globals()[global_name].replace(display)
    elif not ugc:
        globals()[global_name] = display
        __all__.append(global_name)
    check_model(name, display.get_crc(), display)
    if not ugc:
        return globals()[global_name]
    else:
        return display


def unload_model(model):
    model.destroy_kv6()


def create_adjacent_points_file(model, path):
    output_file = None
    adjacent_points = None
    try:
        output_file = open(path, 'w')
        adjacent_points = model.get_adjacent_points()
        adjacent_points_data = (model.get_crc(), adjacent_points)
        try:
            json.dump(adjacent_points_data, output_file)
        except:
            print 'create_adjacent_points_file: json failed to write to file: ', path

    except IOError as e:
        print 'create_adjacent_points_file: failed to create file: ', path

    if output_file != None:
        output_file.close()
    return


def load_adjacent_points(model, global_name, name, ugc=False):
    path = join(name + '_ap.txt')
    crc = None
    kv6_path = os.path.abspath(os.path.join(os.getcwd(), get_relative_path(['../../common', '../common', './common'], 'kv6')))
    ugc_kv6_path = os.path.abspath(os.path.join(os.getcwd(), get_relative_path(['./ugc', '../../common/ugc', '../common/ugc', './common/ugc'], 'kv6')))
    if ugc:
        path = join(ugc_kv6_path, path)
    else:
        path = join(kv6_path, path)
    if os.path.exists(path):
        try:
            file = open(path, 'r')
            try:
                adjacent_points_data = json.load(file)
                crc, adjacent_points = adjacent_points_data
            except:
                print 'load_adjacent_points: json failed to retrieve data from file: ', path

            if file:
                file.close()
        except IOError as e:
            print 'load_adjacent_points: Failed to open file: ', path

    if crc == None or crc <= 0 or crc != model.get_crc():
        print 'load_adjacent_points: crc mismatch for kv6 model ', name, '. - creating cache file'
    else:
        model.set_adjacent_points(adjacent_points)
        print 'loaded adjacent points for kv6 model', name
    return


def load_prefab(name, ugc=False):
    model = load_model(name.upper(), name, prefab=True, ugc=ugc)
    model.reset_prefab_pivots()
    return model


def load_weapon(name, sight_extra=(), extra_offset=(0, 0, 0), sight_offset=(0, 0, 0), sight_extra_offset=(0, 0, 0)):
    upper = name.upper()
    load_model('%s_TRACER' % upper, '%stracer' % name)
    load_model('%s_CASING' % upper, '%scasing' % name)
    load_model('%s_VIEW_MODEL' % upper, name)
    load_model('%s_MODEL' % upper, name, (6 + extra_offset[0], -18 + extra_offset[1], 0.0 + extra_offset[2]))
    load_model('%s_SIGHT' % upper, '%s_sight' % name, (sight_offset[0], sight_offset[1], sight_offset[2]), min_model_detail=2)
    for value in sight_extra:
        load_model('%s_%s' % (upper, value.upper()), '%s_sight_%s' % (name, value), (sight_extra_offset[0], sight_extra_offset[1], sight_extra_offset[2]), min_model_detail=2)


def load_models(detail_level, model_detail):
    global JETPACK_MODELS
    global PARACHUTE_FPS_MODELS
    global PARACHUTE_MODELS
    global UGC_ENTITY_MODELS
    global __detaillevel
    global __modeldetail
    __detaillevel = detail_level
    __modeldetail = model_detail
    load_model(A268[A76][A258], A269[A76][A258], A270[A76][A258])
    load_model(A268[A86][A258], A269[A86][A258], A270[A86][A258])
    load_model(A268[A77][A258], A269[A77][A258], A270[A77][A258])
    load_model(A268[A75][A258], A269[A75][A258], A270[A75][A258])
    load_model(A268[A74][A258], A269[A74][A258], A270[A74][A258])
    load_model(A268[A78][A258], A269[A78][A258], A270[A78][A258])
    load_model(A268[A79][A258], A269[A79][A258], A270[A79][A258])
    load_model(A268[A87][A258], A269[A87][A258], A270[A87][A258])
    load_model(A268[A76][A259], A269[A76][A259], A270[A76][A259])
    load_model(A268[A86][A259], A269[A86][A259], A270[A86][A259])
    load_model(A268[A77][A259], A269[A77][A259], A270[A77][A259])
    load_model(A268[A75][A259], A269[A75][A259], A270[A75][A259])
    load_model(A268[A74][A259], A269[A74][A259], A270[A74][A259])
    load_model(A268[A78][A259], A269[A78][A259], A270[A78][A259])
    load_model(A268[A79][A259], A269[A79][A259], A270[A79][A259])
    load_model(A268[A87][A259], A269[A87][A259], A270[A87][A259])
    load_model(A268[A76][A260], A269[A76][A260], A270[A76][A260])
    load_model(A268[A86][A260], A269[A86][A260], A270[A86][A260])
    load_model(A268[A77][A260], A269[A77][A260], A270[A77][A260])
    load_model(A268[A75][A260], A269[A75][A260], A270[A75][A260])
    load_model(A268[A74][A260], A269[A74][A260], A270[A74][A260])
    load_model(A268[A79][A260], A269[A79][A260], A270[A79][A260])
    load_model(A268[A87][A260], A269[A87][A260], A270[A87][A260])
    load_model(A268[A76][A261], A269[A76][A261], A270[A76][A261])
    load_model(A268[A86][A261], A269[A86][A261], A270[A86][A261])
    load_model(A268[A77][A261], A269[A77][A261], A270[A77][A261])
    load_model(A268[A75][A261], A269[A75][A261], A270[A75][A261])
    load_model(A268[A74][A261], A269[A74][A261], A270[A74][A261])
    load_model(A268[A78][A261], A269[A78][A261], A270[A78][A261])
    load_model(A268[A79][A261], A269[A79][A261], A270[A79][A261])
    load_model(A268[A87][A261], A269[A87][A261], A270[A87][A261])
    load_model(A268[A80][A258], A269[A80][A258], A270[A80][A258])
    load_model(A268[A80][A259], A269[A80][A259], A270[A80][A259])
    load_model(A268[A80][A260], A269[A80][A260], A270[A80][A260])
    load_model(A268[A80][A261], A269[A80][A261], A270[A80][A261])
    load_model(A268[A81][A258], A269[A81][A258], A270[A81][A258])
    load_model(A268[A81][A259], A269[A81][A259], A270[A81][A259])
    load_model(A268[A81][A260], A269[A81][A260], A270[A81][A260])
    load_model(A268[A81][A261], A269[A81][A261], A270[A81][A261])
    load_model(A268[A82][A258], A269[A82][A258], A270[A82][A258])
    load_model(A268[A82][A259], A269[A82][A259], A270[A82][A259])
    load_model(A268[A82][A260], A269[A82][A260], A270[A82][A260])
    load_model(A268[A82][A261], A269[A82][A261], A270[A82][A261])
    load_model(A268[A83][A258], A269[A83][A258], A270[A83][A258])
    load_model(A268[A83][A259], A269[A83][A259], A270[A83][A259])
    load_model(A268[A83][A260], A269[A83][A260], A270[A83][A260])
    load_model(A268[A83][A261], A269[A83][A261], A270[A83][A261])
    load_model(A268[A84][A258], A269[A84][A258], A270[A84][A258])
    load_model(A268[A84][A259], A269[A84][A259], A270[A84][A259])
    load_model(A268[A84][A260], A269[A84][A260], A270[A84][A260])
    load_model(A268[A84][A261], A269[A84][A261], A270[A84][A261])
    load_model(A268[A85][A258], A269[A85][A258], A270[A85][A258])
    load_model(A268[A85][A259], A269[A85][A259], A270[A85][A259])
    load_model(A268[A85][A260], A269[A85][A260], A270[A85][A260])
    load_model(A268[A85][A261], A269[A85][A261], A270[A85][A261])
    load_model(A268[A90][A258], A269[A90][A258], A270[A90][A258])
    load_model(A268[A90][A259], A269[A90][A259], A270[A90][A259])
    load_model(A268[A90][A260], A269[A90][A260], A270[A90][A260])
    load_model(A268[A90][A261], A269[A90][A261], A270[A90][A261])
    load_model(A268[A90][A262], A269[A90][A262], A270[A90][A262])
    load_model(A268[A91][A258], A269[A91][A258], A270[A91][A258])
    load_model(A268[A91][A259], A269[A91][A259], A270[A91][A259])
    load_model(A268[A91][A260], A269[A91][A260], A270[A91][A260])
    load_model(A268[A91][A261], A269[A91][A261], A270[A91][A261])
    load_model(A268[A91][A262], A269[A91][A262], A270[A91][A262])
    load_model('TORSO_CROUCH_MODEL', 'playertorsoc', (0.0, 6.0, -5.0))
    load_model('LEG_CROUCH_MODEL', 'playerlegc', (0.0, 0.0, -5.0))
    for value in (
     (
      'shotgun', ('pin', 'ring')),
     (
      'shotgun2', ('pin', 'ring')),
     (
      'smg', ('ring', )),
     (
      'semi', ('pin', ), (0, 0, 0), (0, 0, -0.0), (0, 0, -0.5)),
     ('minigun', ),
     ('pistol', ),
     ('sniper', ),
     ('sniper2', ),
     (
      'Weapon_SnubNosePistol', '', (3, -2, 2)),
     (
      'Weapon_TommyGun', '', (3, -3, 2)),
     (
      'classic_shotgun', ('pin', 'ring')),
     (
      'classic_smg', ('ring', )),
     (
      'autoPistol', '', (3, -5, -1)),
     (
      'assaultRifle', '', (4, -8, 4)),
     (
      'lightMachineGun', '', (0, -4, 1)),
     (
      'autoShotgun', '', (2, -3, 2))):
        load_weapon(*value)

    load_model(A279[A74][A277], A280[A74][A277])
    load_model(A279[A74][A278], A280[A74][A278])
    load_model(A279[A75][A277], A280[A75][A277])
    load_model(A279[A75][A278], A280[A75][A278])
    load_model(A279[A76][A277], A280[A76][A277])
    load_model(A279[A76][A278], A280[A76][A278])
    load_model(A279[A86][A277], A280[A86][A277])
    load_model(A279[A86][A278], A280[A86][A278])
    load_model(A279[A77][A277], A280[A77][A277])
    load_model(A279[A77][A278], A280[A77][A278])
    load_model(A279[A79][A277], A280[A79][A277])
    load_model(A279[A79][A278], A280[A79][A278])
    load_model(A279[A80][A277], A280[A80][A277])
    load_model(A279[A80][A278], A280[A80][A278])
    load_model(A279[A81][A277], A280[A81][A277])
    load_model(A279[A81][A278], A280[A81][A278])
    load_model(A279[A82][A277], A280[A82][A277])
    load_model(A279[A82][A278], A280[A82][A278])
    load_model(A279[A83][A277], A280[A83][A277])
    load_model(A279[A83][A278], A280[A83][A278])
    load_model(A279[A84][A277], A280[A84][A277])
    load_model(A279[A84][A278], A280[A84][A278])
    load_model(A279[A85][A277], A280[A85][A277])
    load_model(A279[A85][A278], A280[A85][A278])
    load_model(A279[A87][A277], A280[A87][A277])
    load_model(A279[A87][A278], A280[A87][A278])
    load_model(A279[A90][A277], A280[A90][A277])
    load_model(A279[A90][A278], A280[A90][A278])
    load_model(A279[A91][A277], A280[A91][A277])
    load_model(A279[A91][A278], A280[A91][A278])
    load_model('MINIGUN_BODY_MODEL', 'Minigun_Body', (6, -9, -7.0))
    load_model('MINIGUN_BARREL_MODEL', 'Minigun_Barrel')
    load_model('MINIGUN_BODY_VIEW_MODEL', 'Minigun_Body', (0, 0, -6))
    load_model('MINIGUN_BARREL_VIEW_MODEL', 'Minigun_Barrel')
    load_model('BOMB_MODEL', 'Bomb', (5.0, -13.0, 2.0))
    load_model('BOMB_VIEW_MODEL', 'Bomb')
    load_model('BOMB_ENTITY_MODEL', 'Bomb', (0.0, 0.0, 7.0))
    load_model('BOMB_VIEW_MODEL', 'Bomb')
    load_model('DIAMOND_MODEL', 'diamond', (5.0, -13.0, 2.0))
    load_model('DIAMOND_VIEW_MODEL', 'diamond')
    load_model('DIAMOND_ENTITY_MODEL', 'diamond', (0.0, 0.0, 7.0))
    load_model('PICKUP_MODEL', 'pickup')
    load_model('PICKUP_VIEW_MODEL', 'pickup')
    load_model('RPG_MODEL', 'rpg', (6, -9, 0.0))
    load_model('RPG_VIEW_MODEL', 'rpg')
    load_model('RPG_SIGHT', 'rpg_sight', min_model_detail=2)
    load_model('RPG2_MODEL', 'RPG2', (6, -9, 0.0))
    load_model('RPG2_VIEW_MODEL', 'RPG2')
    load_model('RPG2_SIGHT', 'RPG2_sight', min_model_detail=2)
    load_model('UGC_RPG2_MODEL', 'ugc_RPG2', (6, -9, 0.0))
    load_model('UGC_RPG2_VIEW_MODEL', 'ugc_RPG2')
    load_model('UGC_RPG2_SIGHT', 'ugc_RPG2_sight', min_model_detail=2)
    load_model('ROCKET_MODEL', 'rocket')
    load_model('ROCKET2_MODEL', 'rocket2')
    load_model('SNOWBLOWER_MODEL', 'snowblower', (6, -9, 0.0))
    load_model('SNOWBLOWER_VIEW_MODEL', 'snowblower', (6, -9, 0.0))
    load_model('SNOWBLOWER_SIGHT', 'snowblower_sight', min_model_detail=2)
    load_model('SNOWBALL_MODEL', 'snowball')
    load_model('DRILLGUN_MODEL', 'drillgun', (6, -9, 0.0))
    load_model('DRILLGUN_SIGHT', 'drillgun_sight', min_model_detail=2)
    load_model('DRILL_MODEL', 'drill')
    load_model('DRILLGUN_VIEW_MODEL', 'drillgun')
    load_model('LANDMINE_MODEL', 'landmine', (5, -13, 0.0))
    load_model('LANDMINE_VIEW_MODEL', 'landmine')
    load_model('DYNAMITE_MODEL', 'dynamite', (5, -13, 0.0))
    load_model('DYNAMITE_VIEW_MODEL', 'dynamite')
    load_model('BLOCK_MODEL', 'block', (5, -13, 0.0))
    load_model('BLOCK_VIEW_MODEL', 'block')
    load_model('GRENADE_MODEL', 'grenade', (5, -13, 0.0))
    load_model('GRENADE_VIEW_MODEL', 'grenade')
    load_model('ANTIPERSONNEL_GRENADE_MODEL', 'grenade2', (5, -13, 2.0))
    load_model('ANTIPERSONNEL_GRENADE_VIEW_MODEL', 'grenade2')
    load_model('SPADE_MODEL', 'spade', (6, -12, 2.0))
    load_model('SPADE_VIEW_MODEL', 'spade')
    load_model('SUPERSPADE_MODEL', 'SuperSpade', (6, -12, 2.0))
    load_model('SUPERSPADE_VIEW_MODEL', 'SuperSpade')
    load_model('UGC_SUPERSPADE_MODEL', 'ugc_superspade', (6, -12, 2.0))
    load_model('UGC_SUPERSPADE_VIEW_MODEL', 'ugc_superspade')
    load_model('PICKAXE_MODEL', 'Pickaxe', (6, -12, 2.0))
    load_model('PICKAXE_VIEW_MODEL', 'Pickaxe')
    load_model('UGC_PICKAXE_MODEL', 'ugc_pickaxe', (6, -12, 2.0))
    load_model('UGC_PICKAXE_VIEW_MODEL', 'ugc_pickaxe')
    load_model('KNIFE_MODEL', 'Knife', (17.0, -25.0, 2.0))
    load_model('KNIFE_VIEW_MODEL', 'Knife')
    load_model('CROWBAR_MODEL', 'Weapon_Crowbar', (9, -19, 2.0))
    load_model('CROWBAR_VIEW_MODEL', 'Weapon_Crowbar')
    load_model('CP_MODEL', 'cp')
    load_model('INTEL_MODEL', 'intel', (6, -12, -8.0))
    load_model('INTEL_VIEW_MODEL', 'intel', (0, 0, -6.8))
    load_model('INTEL_ENTITY_MODEL', 'intel')
    load_model('HEALTH_MODEL', 'healthcrate')
    load_model('AMMO_MODEL', 'ammocrate')
    load_model('BLOCK_CRATE_MODEL', 'block_crate')
    load_model('HEALTH_DROP_POINT_MODEL', 'Crate_Target', (0.0, 0.0, 1.0))
    load_model('AMMO_DROP_POINT_MODEL', 'Crate_Target', (0.0, 0.0, 1.0))
    load_model('BLOCK_CRATE_DROP_POINT_MODEL', 'Crate_Target', (0.0, 0.0, 1.0))
    load_model('GRAVE_MODEL', 'grave', (0.0, 0.0, 11.0))
    load_model('JETPACK_MODEL', 'jetpack')
    load_model('JETPACK2_MODEL', 'Jetpack2')
    load_model('JETPACK_ENGINEER_MODEL', 'JetpackEngineer')
    load_model('JETPACK_UGCBUILDER_MODEL', 'JetpackUGCBuilder')
    load_model('ZOMBIE_HAND_MODEL', 'ZombieHand', (12.5, -15.0, -7.0))
    load_model('ZOMBIE_HAND_LEFT_MODEL', 'ZombieHandLeft', (-12.5, -15.0, -7.0))
    load_model('ZOMBIE_HAND_VIEW_MODEL', 'ZombieHand')
    load_model('ZOMBIE_HAND_VIEW_LEFT_MODEL', 'ZombieHandLeft', (-17.25, 0.0, 0.0))
    load_model('AIRSTRIKE_BOMB_VIEW_MODEL', 'airstrike_bomb')
    load_model('MUZZLE_FLASH_PISTOL', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_PISTOL_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SMG', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SMG_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_AUTOPISTOL', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_AUTOPISTOL_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SHOTGUN', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SHOTGUN_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SNIPER', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SNIPER_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_MINIGUN', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_MINIGUN_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_RIFLE', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_TOMMYGUN', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_TOMMYGUN_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SNUB_PISTOL', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_SNUB_PISTOL_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_MG', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_MG_VIEW', 'muzzleflash_default')
    load_model('TURRET_BASE_ENTITY_MODEL', 'Turret_base')
    load_model('TURRET_BALL_ENTITY_MODEL', 'Turret_ball')
    load_model('TURRET_GUN_ENTITY_MODEL', 'Turret_gun')
    load_model('TURRET_BASE_VIEW_MODEL', 'Turret_base')
    load_model('TURRET_BALL_VIEW_MODEL', 'Turret_ball')
    load_model('TURRET_GUN_VIEW_MODEL', 'Turret_gun')
    load_model('TURRET_BASE_TOOL_MODEL', 'Turret_base', (0.0, -18.0, 3.0))
    load_model('TURRET_BALL_TOOL_MODEL', 'Turret_ball', (0.0, -18.0, 17.0))
    load_model('TURRET_GUN_TOOL_MODEL', 'Turret_gun', (0.0, -18.0, 11.0))
    load_model('CRATE_PARACHUTE_MODEL', 'Crate_Parachute')
    load_model('CLASSIC_CORPSE_MODEL', 'ClassicCorpse')
    load_model('REF_POINT_MODEL', 'refPoint')
    load_model('MOLOTOV_MODEL', 'Weapon_Molotov', (10, -20, 5.0))
    load_model('MOLOTOV_VIEW_MODEL', 'Weapon_Molotov')
    load_model('CHEMICALBOMB_MODEL', 'chemicalbomb', (20, -40, 14.0))
    load_model('CHEMICALBOMB_VIEW_MODEL', 'chemicalbomb')
    load_model('UGC_ENTITY_BASEPLATE_MODEL', 'ugc_baseplate', (0.0, 0.0, 1.0))
    load_model('UGC_SPAWN_ZONE_MODEL', 'ugc_spawn_zone', (0.0, 0.0, 1.0))
    load_model('UGC_BASE_ZONE_MODEL', 'ugc_base_zone', (0.0, 0.0, 1.0))
    load_model('UGC_TOOL_MODEL', 'place_ent', (6, -9, 0.0))
    load_model('UGC_TOOL_VIEW_MODEL', 'place_ent', (6, -9, 0.0))
    load_model('UGCPREFAB_TOOL_MODEL', 'place_pf', (4, -13, 5))
    load_model('UGCPREFAB_TOOL_VIEW_MODEL', 'place_pf', (0, 0, 0))
    load_model('PAINTBRUSH_TOOL_MODEL', 'place_painbrush', (7, -12, 0))
    load_model('PAINTBRUSH_TOOL_VIEW_MODEL', 'place_painbrush', (0, 0, 0))
    load_model('RIOTSTICK_MODEL', 'riotstick', (13.0, -25.0, 17.0))
    load_model('RIOTSTICK_VIEW_MODEL', 'riotstick', (0, 3, 17))
    load_model('MACHETE_MODEL', 'Machete', (13.0, -25.0, 15.0))
    load_model('MACHETE_VIEW_MODEL', 'Machete', (0, 3, 15))
    load_model('MEDPACK_MODEL', 'MedPack', (8, -21, 0.0))
    load_model('MEDPACK_VIEW_MODEL', 'MedPack', (0.0, 0.0, -3.0))
    load_model('RIOTSHIELD_MODEL', 'riotshield', (0.5, -11.5, -4.0))
    load_model('RIOTSHIELD_VIEW_MODEL', 'riotshield')
    load_model('GRENADE_LAUNCHER_MODEL', 'grenadelauncher', (14, -32, 6.5))
    load_model('GRENADE_LAUNCHER_VIEW_MODEL', 'grenadelauncher')
    load_model('STICKY_GRENADE_MODEL', 'stickygrenade', (10, -20, 5))
    load_model('STICKY_GRENADE_VIEW_MODEL', 'stickygrenade')
    load_model('MINE_LAUNCHER_MODEL', 'minelauncher', (10.0, -10.0, 5.0))
    load_model('MINE_LAUNCHER_VIEW_MODEL', 'minelauncher')
    load_model('PROJECTILE_MINE_MODEL', 'projectilemine', (6, -9, 0.0))
    load_model('PROJECTILE_MINE_VIEW_MODEL', 'projectilemine')
    load_model('RADAR_STATION_BASE_ENTITY_MODEL', 'radar_station')
    load_model('RADAR_STATION_BASE_VIEW_MODEL', 'radar_station')
    load_model('RADAR_STATION_BASE_TOOL_MODEL', 'radar_station', (20.0, -40.0, 28.0))
    load_model('PARACHUTE_MODEL', 'parachute')
    load_model('PARACHUTE_FPS_MODEL', 'parachute_firstperson')
    load_model('C4_MODEL', 'c4_detonator', (8, -21, 2.0))
    load_model('C4_VIEW_MODEL', 'c4')
    load_model('C4_DETONATOR_VIEW_MODEL', 'c4_detonator')
    load_model('MUZZLE_FLASH_ASSAULTRIFLE', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_ASSAULTRIFLE_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_LIGHTMACHINEGUN', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_LIGHTMACHINEGUN_VIEW', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_AUTOSHOTGUN', 'muzzleflash_default')
    load_model('MUZZLE_FLASH_AUTOSHOTGUN_VIEW', 'muzzleflash_default')
    load_model('BLOCKSUCKER_MODEL', 'blocksucker', (8.0, -12.0, 2.0))
    load_model('BLOCKSUCKER_VIEW_MODEL', 'blocksucker')
    load_model('DISGUISE_MODEL', 'disguise', (15.0, -40.0, 0.0))
    load_model('DISGUISE_VIEW_MODEL', 'disguise')
    load_model('CHARACTER_DISGUISE_STANDING', 'Character_Disguise_Blocks_Standing')
    load_model('CHARACTER_DISGUISE_CROUCHED', 'Character_Disguise_Blocks_Crouched')
    JETPACK_MODELS = {A363: JETPACK_MODEL, 
       A364: JETPACK_MODEL, 
       A365: JETPACK2_MODEL, 
       A366: JETPACK_ENGINEER_MODEL, 
       A367: JETPACK_UGCBUILDER_MODEL}
    PARACHUTE_MODELS = {A369: None, 
       A370: PARACHUTE_MODEL}
    PARACHUTE_FPS_MODELS = {A369: None, 
       A370: PARACHUTE_FPS_MODEL}
    UGC_ENTITY_MODELS = {A482: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, HEALTH_MODEL], 0.25, -0.5), 
       A483: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, AMMO_MODEL], 0.25, -0.5), 
       A484: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, BLOCK_CRATE_MODEL], 0.25, -0.5), 
       A485: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, BOMB_ENTITY_MODEL], 1.0, -0.5), 
       A486: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_SPAWN_ZONE_MODEL], 0.25, -0.5), 
       A489: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_SPAWN_ZONE_MODEL], 0.25, -0.5), 
       A492: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 0.5, -0.5), 
       A495: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 0.5, -0.5), 
       A498: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 0.5, -0.5), 
       A487: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_SPAWN_ZONE_MODEL], 1.0, -0.5), 
       A490: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_SPAWN_ZONE_MODEL], 1.0, -0.5), 
       A493: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 1.0, -0.5), 
       A496: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 1.0, -0.5), 
       A499: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 1.0, -0.5), 
       A488: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_SPAWN_ZONE_MODEL], 1.5, -0.5), 
       A491: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_SPAWN_ZONE_MODEL], 1.5, -0.5), 
       A494: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 1.75, -0.5), 
       A497: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 1.75, -0.5), 
       A500: (
            [
             UGC_ENTITY_BASEPLATE_MODEL, UGC_BASE_ZONE_MODEL], 1.75, -0.5)}
    return


def check_model_size(largest_bounding_box, name, instance):
    path = join(KV6_PATH, name + '.kv6')
    model_bounding_box = KV6.get_bounding_box_sizes(instance)
    print 'Model Bounding Box : ' + str(model_bounding_box)
    bounding_boxes = zip(*(largest_bounding_box, model_bounding_box))
    print bounding_boxes
    x1, x2 = bounding_boxes[0]
    y1, y2 = bounding_boxes[1]
    z1, z2 = bounding_boxes[2]
    if x1 >= x2 and y1 >= y2 and z1 >= z2:
        print 'True'
        return True
    else:
        print 'False'
        return False
# okay decompiling out\aoslib.models.pyc
