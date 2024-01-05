# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.weapons.list
from shared.constants import *
from grenadeTool import GrenadeTool
from classicGrenadeTool import ClassicGrenadeTool
from antipersonnelGrenadeTool import AntipersonnelGrenadeTool
from classicRifleWeapon import ClassicRifleWeapon
from smgWeapon import SMGWeapon
from minigunWeapon import MinigunWeapon
from shotgunWeapon import ShotgunWeapon
from shotgun2Weapon import Shotgun2Weapon
from blockTool import BlockTool
from pickAxeTool import PickAxeTool
from ugcPickAxeTool import UGCPickAxeTool
from knifeTool import KnifeTool
from spadeTool import SpadeTool
from superSpadeTool import SuperSpadeTool
from ugcSuperSpadeTool import UGCSuperSpadeTool
from classicSpadeTool import ClassicSpadeTool
from prefabTool import PrefabTool
from rpgWeapon import RPGWeapon
from rpg2Weapon import RPG2Weapon
from ugcRPG2Weapon import UGCRPG2Weapon
from drillgunWeapon import DrillgunWeapon
from ugcDrillgunWeapon import UGCDrillgunWeapon
from mgWeapon import MGWeapon
from rocketTurretWeapon import RocketTurretWeapon
from pistolWeapon import PistolWeapon
from sniperWeapon import SniperWeapon
from sniper2Weapon import Sniper2Weapon
from landmineWeapon import LandmineWeapon
from dynamiteWeapon import DynamiteWeapon
from flareBlockTool import FlareBlockTool
from zombieHandTool import ZombieHandTool
from bombTool import BombTool
from diamondTool import DiamondTool
from intelTool import IntelTool
from zombiePrefabTool import ZombiePrefabTool
from snowBlowerWeapon import SnowBlowerWeapon
from ugcSnowBlowerWeapon import UGCSnowBlowerWeapon
from molotovWeapon import MolotovWeapon
from crowbarTool import CrowbarTool
from tommyGunWeapon import TommyGunWeapon
from snubPistolWeapon import SnubPistolWeapon
from classicShotgunWeapon import ClassicShotgunWeapon
from classicSmgWeapon import ClassicSmgWeapon
from nullTool import NullTool
from ugcTool import UGCTool
from fakePistolTool import FakePistolTool
from ugcPrefabTool import UGCPrefabTool
from paintbrushTool import PaintbrushTool
from riotStickTool import RiotStickTool
from macheteTool import MacheteTool
from medPackWeapon import MedPackWeapon
from riotShieldTool import RiotShieldTool
from autoPistolWeapon import AutoPistolWeapon
from chemicalbombWeapon import ChemicalBombWeapon
from grenadeLauncherWeapon import GrenadeLauncherWeapon
from stickygrenadeWeapon import StickyGrenadeWeapon
from radarStationWeapon import RadarStationWeapon
from c4Weapon import C4Weapon
from assaultRifleWeapon import AssaultRifleWeapon
from lightMachineGunWeapon import LightMachineGunWeapon
from autoShotgunWeapon import AutoShotgunWeapon
from blockSuckerWeapon import BlockSuckerWeapon
from disguiseTool import DisguiseTool
from mineLauncherWeapon import MineLauncherWeapon
WEAPONS = {A307: GrenadeTool, 
   A327: ClassicGrenadeTool, 
   A328: AntipersonnelGrenadeTool, 
   A302: ClassicRifleWeapon, 
   A303: SMGWeapon, 
   A304: MinigunWeapon, 
   A305: ShotgunWeapon, 
   A306: Shotgun2Weapon, 
   A308: RPGWeapon, 
   A309: RPG2Weapon, 
   A342: UGCRPG2Weapon, 
   A325: SnowBlowerWeapon, 
   A344: UGCSnowBlowerWeapon, 
   A310: DrillgunWeapon, 
   A343: UGCDrillgunWeapon, 
   A311: MGWeapon, 
   A312: RocketTurretWeapon, 
   A313: PistolWeapon, 
   A314: SniperWeapon, 
   A315: Sniper2Weapon, 
   A316: LandmineWeapon, 
   A317: DynamiteWeapon, 
   A318: FlareBlockTool, 
   A319: PrefabTool, 
   A296: PickAxeTool, 
   A340: UGCPickAxeTool, 
   A297: KnifeTool, 
   A298: SpadeTool, 
   A299: SuperSpadeTool, 
   A341: UGCSuperSpadeTool, 
   A300: ClassicSpadeTool, 
   A301: BlockTool, 
   A320: ZombieHandTool, 
   A321: BombTool, 
   A322: DiamondTool, 
   A323: BlockTool, 
   A324: ZombiePrefabTool, 
   A326: IntelTool, 
   A329: MolotovWeapon, 
   A330: CrowbarTool, 
   A331: TommyGunWeapon, 
   A332: SnubPistolWeapon, 
   A333: ClassicShotgunWeapon, 
   A334: ClassicSmgWeapon, 
   A335: NullTool, 
   A337: UGCTool, 
   A336: FakePistolTool, 
   A338: UGCPrefabTool, 
   A339: PaintbrushTool, 
   A345: RiotStickTool, 
   A346: MacheteTool, 
   A347: MedPackWeapon, 
   A348: RiotShieldTool, 
   A350: ChemicalBombWeapon, 
   A349: AutoPistolWeapon, 
   A351: GrenadeLauncherWeapon, 
   A353: StickyGrenadeWeapon, 
   A352: RadarStationWeapon, 
   A354: MineLauncherWeapon, 
   A355: C4Weapon, 
   A356: AssaultRifleWeapon, 
   A357: LightMachineGunWeapon, 
   A358: AutoShotgunWeapon, 
   A359: BlockSuckerWeapon, 
   A360: DisguiseTool}
for id, weapon in WEAPONS.iteritems():
    if len(weapon.model) != len(weapon.view_model):
        if id != A324:
            raise Exception('Weapon/Tools - model list for ', weapon.name, 'should have same length as view_model list.')

PICKUPS = {A913: A321, A914: A322, 
   A915: A326}
# okay decompiling out\aoslib.weapons.list.pyc
