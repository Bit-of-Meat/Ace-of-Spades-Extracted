# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\shared.constants
from constants_gamemode import *
from constants_shop import *
A0 = 224540
A1 = 200
import json, sys
from shared.constants_audio import *

def A2():
    constants_file = 'constants.txt'
    import os
    if os.path.exists(constants_file):
        print 'Loading overrides from', constants_file
        f = open(constants_file)
        for line in f:
            try:
                attribute_to_override, override_value = line.split('=', 1)
                attribute_to_override = attribute_to_override.strip()
                override_value = override_value.split('#')[0]
                override_value = override_value.strip()
                try:
                    existing_value = globals()[attribute_to_override]
                except KeyError:
                    print 'Constant', attribute_to_override, 'does not exist'

                if isinstance(existing_value, bool):
                    globals()[attribute_to_override] = override_value in ('True', 'true',
                                                                          '1')
                elif isinstance(existing_value, float):
                    globals()[attribute_to_override] = float(override_value)
                elif isinstance(existing_value, int):
                    globals()[attribute_to_override] = int(override_value)
                elif isinstance(existing_value, basestring):
                    globals()[attribute_to_override] = override_value.strip('"')
                else:
                    override_value = override_value.replace("'", '"')
                    override_value = override_value.replace('+', '')
                    globals()[attribute_to_override] = json.loads(override_value)
                print 'Override applied: %s = %s (default %s)' % (attribute_to_override, override_value, str(existing_value))
            except:
                if len(line) > 2:
                    print 'Skipped line:', line


A3 = 32
A4, A5, A6, A7 = xrange(4)
A8 = {A4: 'us_west', 
   A5: 'us_east', 
   A6: 'europe', 
   A7: 'australia'}
A9 = 60
A10 = 30
A11 = 800
A12 = 600
A13, A14, A15 = xrange(3)
A16 = 4
A17 = 4
A18 = 0
A19, A20, A21, A22, A23, A24 = xrange(6)
A25 = '/bot qadd'
A26 = '/bot add 1 g'
A27 = '/bot add 1 b'
A28 = '/bot wake toggle'
A29 = '/bot shoot toggle'
A30 = '/bot tool'
A31 = '/airstrike'
A32 = '/'
A33 = '/'
A34 = '/'
A35, A36 = xrange(2)
A37 = 1
A38 = 1000000
A39, A40 = xrange(2)
A41, A42 = xrange(2)
A43 = 0.25
A44 = 1.0 / A43
A45 = 128.0
A46 = 192.0
A47 = (
 255, 228, 0, 255)
A48 = (204, 28, 24, 255)
A49 = (
 255, 0, 0, 255)
A50 = (255, 0, 0, 255)
A51 = (
 255, 194, 81, 255)
A52 = (
 194, 194, 194, 255)
A53, TEAM_NEUTRAL, A55, A56 = xrange(4)
A57 = {A53: 'SPECTATOR', 
   TEAM_NEUTRAL: 'NEUTRAL', 
   A55: 'TEAM1_COLOR', 
   A56: 'TEAM2_COLOR'}
A58 = {A53: (
       255, 255, 255), 
   TEAM_NEUTRAL: (
                128, 128, 128), 
   A55: (
       44, 117, 179), 
   A56: (
       137, 179, 44)}
A59 = {A55: (
       44, 117, 179), 
   A56: (
       137, 179, 44)}
A60 = (
 255, 100, 0)
A61, A62, A63, A64 = xrange(4)
A65, A66, A67, A68, A69, A70, A71, A72 = xrange(8)
A73 = [A68, A69, A71, A72]
A74, A75, A76, A77, A78, A79, A80, A81, A82, A83, A84, A85, A86, A87, A88, A89, A90, A91, A92 = xrange(19)
A93 = [A74, A75, A86, A77, A90, A91]
A94 = [A79]
A95 = [A80, A81, A82, A83]
A96 = [A87]
A97 = [A78, A88, A89]
A98 = {A74: 'SOLDIER', 
   A75: 'SCOUT', 
   A76: 'ENGINEER', 
   A86: 'ENGINEER2', 
   A77: 'MINER', 
   A78: 'ZOMBIE', 
   A79: 'CLASSIC_SOLDIER', 
   A80: 'GANGSTER_1_NAME', 
   A81: 'GANGSTER_2_NAME', 
   A82: 'GANGSTER_3_NAME', 
   A83: 'GANGSTER_4_NAME', 
   A84: 'GANGSTER_VIP_1_NAME', 
   A85: 'GANGSTER_VIP_2_NAME', 
   A87: 'UGCBUILDER', 
   A88: 'FAST_ZOMBIE', 
   A89: 'JUMP_ZOMBIE', 
   A90: 'SPECIALIST', 
   A91: 'MEDIC'}
A99 = {A55: A84, 
   A56: A85}
A100 = 5.0
A101 = 0.5
A102 = 1.0
A103 = 1.5
A104 = 1.5
A105 = 1.5
A106 = 0.5
A107 = 1.0
A108 = 1.0
A109 = 1.2
A110 = 0
A111 = 2.5
A112 = 1.5
A113 = 1.5
A114 = 1.0
A115 = 1.0
A116 = 1.43
A117 = 1.43
A118 = 1.1765
A119 = 1.1765
A120 = 0.6
A121 = 1.0
A122 = 1.0
A123 = 0
A124 = 0.5
A125 = 0.5
A126 = 1.1765
A127 = 1.0
A128 = 0.7
A129 = 0.7
A130 = 0.7
A131 = 0.7
A132 = 0.7
A133 = 0.5
A134 = 1.0
A135 = 0.7
A136 = 1.0
A137 = 1.1
A138 = 0.5
A139 = 0.85
A140 = 0.6
A141 = 1.4
A142 = 1.45
A143 = 1.1
A144 = 1.25
A145 = 1.4
A146 = 1.65
A147 = 1.33
A148 = 1.5
A149 = 3.0
A150 = 3.0
A151 = 1.0
A152 = 1.55
A153 = 1.35
A154 = 0.5
A155 = 0.5
A156 = 0.5
A157 = 0.5
A158 = 0.5
A159 = 0.5
A160 = 0.5
A161 = 0.5
A162 = 0.5
A163 = 0.25
A164 = 0.5
A165 = 0.5
A166 = 0.5
A167 = 0.5
A168 = 0.5
A169 = 0.5
A170 = 0.5
A171 = 0.5
A172 = 0.25
A173 = 1.0
A174 = 0.5
A175 = 1.0
A176 = 2.0
A177 = 0.5
A178 = 0.5
A179 = 0.5
A180 = 1.2
A181 = 1.5
A182 = 1.0
A183 = 1.0
A184 = 1.2
A185 = 1.5
A186 = 1.0
A187 = 1.2
A188 = 1.0
A189 = 2.5
A190 = 3.0
A191 = 1.5
A192 = 1.2
A193 = 8
A194 = 8
A195 = 12.0
A196 = 8
A197 = 8
A198 = 4.0
A199 = 8
A200 = 8
A201 = 1.0
A202 = 12.0
A203 = 8
A204 = 8
A205 = 8
A206 = 10
A207 = 10
A208 = 10
A209 = 10
A210 = 10
A211 = 10
A212 = 6
A213 = 10
A214 = 255
A215 = 6
A216 = 15
A217 = 10
A218 = 10
A219 = 40
A220 = 30
A221 = 10
A222 = 40
A223 = 40
A224 = 60
A225 = 26
A226 = 40
A227 = 255
A228 = 20
A229 = 25
A230 = 40
A231 = 40
A232 = 100
A233 = 100
A234 = 10
A235 = 100
A236 = 100
A237 = 100
A238 = 100
A239 = 100
A240 = 0
A241 = 500
A242 = 100
A243 = 100
A244 = 100
A245 = 0.45
A246 = 3
A247 = 1.5 / 2
A248 = 2.5 / 2
A249, A250, A251 = xrange(3)
A252 = {A249: 0.5, 
   A250: 0.3, 
   A251: 0.2}
A253 = 2.25
A254 = 1.35
A255 = A253 + A245
A256 = A254 + A245
A257 = 2
A258, A259, A260, A261, A262, A263, A264, A265, A266 = xrange(9)
A267 = {A258: 'head', 
   A259: 'torso', 
   A260: 'arms', 
   A261: 'left leg', 
   A262: 'right leg', 
   A263: 'torso crouch', 
   A264: 'leg crouch', 
   A265: 'entity 1', 
   A266: 'entity 2'}
A268 = {A74: [
       'HEAD_MODEL_SOLDIER', 'TORSO_MODEL_SOLDIER', 'ARMS_MODEL_SOLDIER', 
       'LEG_MODEL_SOLDIER', 'LEG_MODEL_SOLDIER', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A75: [
       'HEAD_MODEL_SCOUT', 'TORSO_MODEL_SCOUT', 'ARMS_MODEL_SCOUT', 
       'LEG_MODEL_SCOUT', 'LEG_MODEL_SCOUT', 'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A76: [
       'HEAD_MODEL_ROCKETEER', 'TORSO_MODEL_ROCKETEER', 'ARMS_MODEL_ROCKETEER', 
       'LEG_MODEL_ROCKETEER', 'LEG_MODEL_ROCKETEER', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A86: [
       'HEAD_MODEL_ENGINEER', 'TORSO_MODEL_ENGINEER', 'ARMS_MODEL_ENGINEER', 
       'LEG_MODEL_ENGINEER', 'LEG_MODEL_ENGINEER', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A77: [
       'HEAD_MODEL_MINER', 'TORSO_MODEL_MINER', 'ARMS_MODEL_MINER', 
       'LEG_MODEL_MINER', 'LEG_MODEL_MINER', 'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A78: [
       'HEAD_MODEL_ZOMBIE', 'TORSO_MODEL_ZOMBIE', 'ARMS_MODEL_SOLDIER', 
       'LEG_MODEL_ZOMBIE', 'LEG_MODEL_ZOMBIE', 'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A79: [
       'HEAD_MODEL_DEUCE', 'TORSO_MODEL_DEUCE', 'ARMS_MODEL_DEUCE', 
       'LEG_MODEL_DEUCE', 'LEG_MODEL_DEUCE', 'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A80: [
       'HEAD_MODEL_GANGSTER_1', 'TORSO_MODEL_GANGSTER_1', 'ARMS_MODEL_GANGSTER_1', 
       'LEG_MODEL_GANGSTER_1', 'LEG_MODEL_GANGSTER_1', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A81: [
       'HEAD_MODEL_GANGSTER_2', 'TORSO_MODEL_GANGSTER_2', 'ARMS_MODEL_GANGSTER_2', 
       'LEG_MODEL_GANGSTER_2', 'LEG_MODEL_GANGSTER_2', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A82: [
       'HEAD_MODEL_GANGSTER_3', 'TORSO_MODEL_GANGSTER_3', 'ARMS_MODEL_GANGSTER_3', 
       'LEG_MODEL_GANGSTER_3', 'LEG_MODEL_GANGSTER_3', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A83: [
       'HEAD_MODEL_GANGSTER_4', 'TORSO_MODEL_GANGSTER_4', 'ARMS_MODEL_GANGSTER_4', 
       'LEG_MODEL_GANGSTER_4', 'LEG_MODEL_GANGSTER_4', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A84: [
       'HEAD_MODEL_GANGSTER_VIP_1', 'TORSO_MODEL_GANGSTER_VIP_1', 
       'ARMS_MODEL_GANGSTER_VIP_1', 'LEG_MODEL_GANGSTER_VIP_1', 'LEG_MODEL_GANGSTER_VIP_1', 
       'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A85: [
       'HEAD_MODEL_GANGSTER_VIP_2', 'TORSO_MODEL_GANGSTER_VIP_2', 
       'ARMS_MODEL_GANGSTER_VIP_2', 'LEG_MODEL_GANGSTER_VIP_2', 'LEG_MODEL_GANGSTER_VIP_2', 
       'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A87: [
       'HEAD_MODEL_UGCBUILDER', 'TORSO_MODEL_UGCBUILDER', 'ARMS_MODEL_UGCBUILDER', 
       'LEG_MODEL_UGCBUILDER', 'LEG_MODEL_UGCBUILDER', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A88: [
       'HEAD_MODEL_ZOMBIE', 'TORSO_MODEL_ZOMBIE', 'ARMS_MODEL_SOLDIER', 
       'LEG_MODEL_ZOMBIE', 'LEG_MODEL_ZOMBIE', 'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A89: [
       'HEAD_MODEL_ZOMBIE', 'TORSO_MODEL_ZOMBIE', 'ARMS_MODEL_SOLDIER', 
       'LEG_MODEL_ZOMBIE', 'LEG_MODEL_ZOMBIE', 'TORSO_CROUCH_MODEL', 'LEG_CROUCH_MODEL'], 
   A90: [
       'HEAD_MODEL_SPECIALIST', 'TORSO_MODEL_SPECIALIST', 'ARMS_MODEL_SPECIALIST', 
       'LEG_MODEL_LEFT_SPECIALIST', 'LEG_MODEL_RIGHT_SPECIALIST', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL'], 
   A91: [
       'HEAD_MODEL_MEDIC', 'TORSO_MODEL_MEDIC', 'ARMS_MODEL_MEDIC', 
       'LEG_MODEL_LEFT_MEDIC', 'LEG_MODEL_RIGHT_MEDIC', 'TORSO_CROUCH_MODEL', 
       'LEG_CROUCH_MODEL']}
A269 = {A74: [
       'Character_Soldier_Head', 'Character_Soldier_Body', 'Character_Arms_Collision', 
       'Character_Soldier_Leg', 'Character_Soldier_Leg', 'playertorsoc', 
       'playerlegc'], 
   A75: [
       'Character_Scout_Head', 'Character_Scout_Body', 'Character_Arms_Collision', 
       'Character_Scout_Leg', 'Character_Scout_Leg', 'playertorsoc', 'playerlegc'], 
   A76: [
       'Character_Rocketeer_Head', 'Character_Rocketeer_Body', 'Character_Arms_Collision', 
       'Character_Rocketeer_Leg', 'Character_Rocketeer_Leg', 'playertorsoc', 
       'playerlegc'], 
   A86: [
       'Character_Engineer_Head', 'Character_Engineer_Body', 'Character_Arms_Collision', 
       'Character_Engineer_Leg', 'Character_Engineer_Leg', 'playertorsoc', 
       'playerlegc'], 
   A77: [
       'Character_Miner_Head', 'Character_Miner_Body', 'Character_Arms_Collision', 
       'Character_Miner_Leg', 'Character_Miner_Leg', 'playertorsoc', 'playerlegc'], 
   A78: [
       'Character_Zombie_Head', 'Character_Zombie_Body', 'Character_Arms_Collision', 
       'Character_Zombie_Leg', 'Character_Zombie_Leg', 'playertorsoc', 
       'playerlegc'], 
   A79: [
       'Character_Deuce_Head', 'Character_Deuce_Body', 'Character_Arms_Collision', 
       'Character_Deuce_Leg', 'Character_Deuce_Leg', 'playertorsoc', 'playerlegc'], 
   A80: [
       'Character_Gangster1_Head', 'Character_Gangster1_Body', 'Character_Arms_Collision', 
       'Character_Gangster1_Leg', 'Character_Gangster1_Leg', 'playertorsoc', 
       'playerlegc'], 
   A81: [
       'Character_Gangster2_Head', 'Character_Gangster2_Body', 'Character_Arms_Collision', 
       'Character_Gangster2_Leg', 'Character_Gangster2_Leg', 'playertorsoc', 
       'playerlegc'], 
   A82: [
       'Character_Gangster3_Head', 'Character_Gangster3_Body', 'Character_Arms_Collision', 
       'Character_Gangster3_Leg', 'Character_Gangster3_Leg', 'playertorsoc', 
       'playerlegc'], 
   A83: [
       'Character_Gangster4_Head', 'Character_Gangster4_Body', 'Character_Arms_Collision', 
       'Character_Gangster4_Leg', 'Character_Gangster4_Leg', 'playertorsoc', 
       'playerlegc'], 
   A84: [
       'Character_GangsterVIP1_Head', 'Character_GangsterVIP1_Body', 
       'Character_Arms_Collision', 'Character_GangsterVIP1_Leg', 'Character_GangsterVIP1_Leg', 
       'playertorsoc', 'playerlegc'], 
   A85: [
       'Character_GangsterVIP2_Head', 'Character_GangsterVIP2_Body', 
       'Character_Arms_Collision', 'Character_GangsterVIP2_Leg', 'Character_GangsterVIP2_Leg', 
       'playertorsoc', 'playerlegc'], 
   A87: [
       'Character_UGCBuilder_Head', 'Character_UGCBuilder_Body', 'Character_Arms_Collision', 
       'Character_UGCBuilder_Leg', 'Character_UGCBuilder_Leg', 'playertorsoc', 
       'playerlegc'], 
   A88: [
       'Character_Zombie_Head', 'Character_Zombie_Body', 'Character_Arms_Collision', 
       'Character_Zombie_Leg', 'Character_Zombie_Leg', 'playertorsoc', 
       'playerlegc'], 
   A89: [
       'Character_Zombie_Head', 'Character_Zombie_Body', 'Character_Arms_Collision', 
       'Character_Zombie_Leg', 'Character_Zombie_Leg', 'playertorsoc', 
       'playerlegc'], 
   A90: [
       'Character_Specialist_Head', 'Character_Specialist_Body', 'Character_Arms_Collision', 
       'Character_Specialist_Leg_L', 'Character_Specialist_Leg_R', 'playertorsoc', 
       'playerlegc'], 
   A91: [
       'Character_Medic_Head', 'Character_Medic_Body', 'Character_Arms_Collision', 
       'Character_Medic_Leg_L', 'Character_Medic_Leg_R', 'playertorsoc', 
       'playerlegc']}
A270 = {A74: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A75: [
       (
        0.0, 0.0, 5.5), (0.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A76: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A86: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A77: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A78: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, 0.0, 0.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A79: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A80: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A81: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A82: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A83: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A84: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A85: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A87: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A88: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, 0.0, 0.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A89: [
       (
        0.0, 0.0, 5.5), (0.0, 0.0, -9.0), (0.0, 0.0, 0.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A90: [
       (
        0.0, 0.0, 5.5), (0.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (0.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)], 
   A91: [
       (
        0.0, 0.0, 5.5), (-1.0, 1.5, -9.0), (0.0, -8.0, -5.0), (0.0, 0.0, -12.0), (-2.0, 0.0, -12.0), (0.0, 6.0, -5.0), (0.0, 0.0, -5.0)]}
A271 = [
 0.0, 0.0, 0.0, 0.25, -0.25, 0.0, 0.0]
A272 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
A273 = [0.3, 0.3, 0.5, 1.1, 1.1, 0.0, 0.7]
A274 = 0.05
A275 = -0.3
A276 = 0.4
A277, A278 = xrange(2)
A279 = {A74: [
       'UPPER_ARM_MODEL_SOLDIER', 'LOWER_ARM_MODEL_SOLDIER'], 
   A75: [
       'UPPER_ARM_MODEL_SCOUT', 'LOWER_ARM_MODEL_SCOUT'], 
   A76: [
       'UPPER_ARM_MODEL_ROCKETEER', 'LOWER_ARM_MODEL_ROCKETEER'], 
   A86: [
       'UPPER_ARM_MODEL_ENGINEER', 'LOWER_ARM_MODEL_ENGINEER'], 
   A77: [
       'UPPER_ARM_MODEL_MINER', 'LOWER_ARM_MODEL_MINER'], 
   A78: [
       '', ''], 
   A79: [
       'UPPER_ARM_MODEL_DEUCE', 'LOWER_ARM_MODEL_DEUCE'], 
   A80: [
       'UPPER_ARM_MODEL_GANGSTER_1', 'LOWER_ARM_MODEL_GANGSTER_1'], 
   A81: [
       'UPPER_ARM_MODEL_GANGSTER_2', 'LOWER_ARM_MODEL_GANGSTER_2'], 
   A82: [
       'UPPER_ARM_MODEL_GANGSTER_3', 'LOWER_ARM_MODEL_GANGSTER_3'], 
   A83: [
       'UPPER_ARM_MODEL_GANGSTER_4', 'LOWER_ARM_MODEL_GANGSTER_4'], 
   A84: [
       'UPPER_ARM_MODEL_GANGSTER_VIP_1', 'LOWER_ARM_MODEL_GANGSTER_VIP_1'], 
   A85: [
       'UPPER_ARM_MODEL_GANGSTER_VIP_2', 'LOWER_ARM_MODEL_GANGSTER_VIP_2'], 
   A87: [
       'UPPER_ARM_MODEL_UGCBUILDER', 'LOWER_ARM_MODEL_UGCBUILDER'], 
   A88: [
       '', ''], 
   A89: [
       '', ''], 
   A90: [
       'UPPER_ARM_MODEL_SPECIALIST', 'LOWER_ARM_MODEL_SPECIALIST'], 
   A91: [
       'UPPER_ARM_MODEL_MEDIC', 'LOWER_ARM_MODEL_MEDIC']}
A280 = {A74: [
       'Character_Soldier_Arms_Upper', 'Character_Soldier_Arms_Lower'], 
   A75: [
       'Character_Scout_Arms_Upper', 'Character_Scout_Arms_Lower'], 
   A76: [
       'Character_Rocketeer_Arms_Upper', 'Character_Rocketeer_Arms_Lower'], 
   A86: [
       'Character_Engineer_Arms_Upper', 'Character_Engineer_Arms_Lower'], 
   A77: [
       'Character_Miner_Arms_Upper', 'Character_Miner_Arms_Lower'], 
   A78: [
       '', ''], 
   A79: [
       'Character_Deuce_Arms_Upper', 'Character_Deuce_Arms_Lower'], 
   A80: [
       'Character_Gangster1_Arms_Upper', 'Character_Gangster1_Arms_Lower'], 
   A81: [
       'Character_Gangster2_Arms_Upper', 'Character_Gangster2_Arms_Lower'], 
   A82: [
       'Character_Gangster3_Arms_Upper', 'Character_Gangster3_Arms_Lower'], 
   A83: [
       'Character_Gangster4_Arms_Upper', 'Character_Gangster4_Arms_Lower'], 
   A84: [
       'Character_GangsterVIP1_Arms_Upper', 'Character_GangsterVIP1_Arms_Lower'], 
   A85: [
       'Character_GangsterVIP2_Arms_Upper', 'Character_GangsterVIP2_Arms_Lower'], 
   A87: [
       'Character_UGCBuilder_Arms_Upper', 'Character_UGCBuilder_Arms_Lower'], 
   A88: [
       '', ''], 
   A89: [
       '', ''], 
   A90: [
       'Character_Specialist_Arms_Upper', 'Character_Specialist_Arms_Lower'], 
   A91: [
       'Character_Medic_Arms_Upper', 'Character_Medic_Arms_Lower']}
A281, A282, A283 = xrange(3)
A284, A285, A286 = xrange(3)
A287 = (
 255, 255, 255)
A288 = (230, 40, 79)
A289 = 0.25
A290, A291, A292, A293, A294 = xrange(5)
A295 = 66
A296, A297, A298, A299, A300, A301, A302, A303, A304, A305, A306, A307, A308, A309, A310, A311, A312, A313, A314, A315, A316, A317, A318, A319, A320, A321, A322, A323, A324, A325, A326, A327, A328, A329, A330, A331, A332, A333, A334, A335, A336, A337, A338, A339, A340, A341, A342, A343, A344, A345, A346, A347, A348, A349, A350, A351, A352, A353, A354, A355, A356, A357, A358, A359, A360, A361 = xrange(A295)
A362 = 5
A363, A364, A365, A366, A367 = xrange(A361, A361 + A362)
A368 = 2
A369, A370 = xrange(A363 + A362 + 1, A363 + A362 + 1 + A368)
A371 = (
 A296, A297, A298, A299, A300, A320, A330, A340, A341, A345, A346, A348)
A372 = (
 A307, A327, A328, A308, A309, A342, A325, A344, A310, A343, A329, A350, A351, A353, A355, A354)
A373 = (
 A316, A317, A307, A327, A328,
 A319, A312, A301, A318, A324, A329, A350, A353, A360)
A374, A375, A376, A377, A378, A379, A380, A381, A382, A383, A384, A385, A386, A387, A388, A389, A390, A391, A392, A393, A394, A395, A396, A397, A398, A399, A400, A401, A402, A403, A404, A405, A406, A407, A408, A409, A410, A411, A412, A413, A414, A415, A416, A417 = xrange(44)
A418 = {A296: A374, 
   A340: A402, 
   A297: A375, 
   A298: A376, 
   A299: A377, 
   A341: A403, 
   A300: A378, 
   A301: None, 
   A302: A380, 
   A303: A380, 
   A349: A380, 
   A304: A380, 
   A305: A380, 
   A306: A380, 
   A307: A381, 
   A327: A396, 
   A328: A397, 
   A308: A382, 
   A309: A383, 
   A342: A404, 
   A310: A384, 
   A343: A407, 
   A311: A380, 
   A312: None, 
   A313: A380, 
   A314: A380, 
   A315: A380, 
   A316: A389, 
   A317: A390, 
   A318: None, 
   A319: None, 
   A320: A391, 
   A321: A393, 
   A322: None, 
   A323: A380, 
   A324: None, 
   A325: A394, 
   A344: A406, 
   A326: None, 
   A329: A398, 
   A330: A400, 
   A331: A380, 
   A332: A380, 
   A333: A380, 
   A334: A380, 
   A335: None, 
   A337: None, 
   A336: None, 
   A338: None, 
   A339: None, 
   A345: A408, 
   A346: A409, 
   A347: None, 
   A348: A410, 
   A350: A380, 
   A351: A411, 
   A352: None, 
   A353: A413, 
   A354: A414, 
   A355: A415, 
   A356: A380, 
   A357: A380, 
   A358: A380, 
   A359: A416, 
   A360: None}
A419 = {A296: A374, 
   A296: A402, 
   A297: A375, 
   A298: A376, 
   A299: A377, 
   A341: A405, 
   A300: A379, 
   A301: None, 
   A302: A380, 
   A303: A380, 
   A349: A380, 
   A304: A380, 
   A305: A380, 
   A306: A380, 
   A307: A381, 
   A327: A396, 
   A328: A397, 
   A308: A382, 
   A309: A383, 
   A342: A404, 
   A310: A384, 
   A343: A407, 
   A311: A380, 
   A312: None, 
   A313: A380, 
   A314: A380, 
   A315: A380, 
   A316: A389, 
   A317: A390, 
   A318: None, 
   A319: None, 
   A320: A391, 
   A321: A393, 
   A322: None, 
   A323: A380, 
   A324: None, 
   A325: A394, 
   A344: A406, 
   A326: None, 
   A329: A398, 
   A330: A400, 
   A331: A380, 
   A332: A380, 
   A333: A380, 
   A334: A380, 
   A335: None, 
   A337: None, 
   A336: None, 
   A338: None, 
   A339: None, 
   A345: A408, 
   A346: A409, 
   A347: None, 
   A348: A410, 
   A350: A380, 
   A351: A411, 
   A352: None, 
   A353: A413, 
   A354: A414, 
   A355: A415, 
   A356: A380, 
   A357: A380, 
   A358: A380, 
   A359: A416, 
   A360: None}
A420 = (
 A376,
 A378,
 A377,
 A374,
 A375,
 A391,
 A400,
 A402,
 A403,
 A408,
 A409,
 A410,
 A416)
A421, A422, A423, A424, A425, A426, A427, A428, A429, A430, A431, A432, A433, A434, A435, A436, A437, A438, A439, A440, A441, A442, A443, A444, A445, A446, A447, A448, A449, A450, A451, A452, A453, A454, A455, A456, A457 = xrange(37)
A458 = {A296: A421, 
   A340: A421, 
   A297: A421, 
   A298: A421, 
   A299: A421, 
   A341: A421, 
   A300: A421, 
   A301: A421, 
   A302: A421, 
   A303: A421, 
   A349: A421, 
   A304: A421, 
   A305: A421, 
   A306: A421, 
   A307: A421, 
   A327: A421, 
   A328: A421, 
   A308: A425, 
   A342: A448, 
   A310: A427, 
   A343: A449, 
   A311: A421, 
   A312: A425, 
   A313: A421, 
   A314: A421, 
   A315: A421, 
   A316: A421, 
   A317: A421, 
   A318: A421, 
   A319: A421, 
   A320: A421, 
   A321: A438, 
   A322: A421, 
   A323: A440, 
   A324: A421, 
   A325: A442, 
   A344: A450, 
   A326: A421, 
   A329: A421, 
   A330: A421, 
   A331: A421, 
   A332: A421, 
   A333: A421, 
   A334: A421, 
   A335: A421, 
   A337: A421, 
   A336: A421, 
   A338: A421, 
   A339: A421, 
   A345: A421, 
   A346: A421, 
   A348: A421, 
   A350: A452, 
   A351: A453, 
   A352: A454, 
   A353: A455, 
   A354: A456, 
   A355: A457, 
   A356: A421, 
   A357: A421, 
   A358: A421, 
   A359: A421, 
   A360: A421}
A459 = {A302: (
        2.5, 6.0), 
   A314: (
        7.5, 6.0), 
   A315: (
        2.5, 6.0), 
   A361: (
        5.0, 5.0)}
A460, A461, A462, A463 = xrange(4)
A464 = {A460: 'EXTRA_HEALTH', 
   A461: 'SPEED', 
   A462: 'DIGGING_SPEED'}
A465 = []
A466, A467, A468, A469, A470, A471, A472, A473, A474, A475, A476, A477, A478, A479, A480 = xrange(15)
A481 = {A466: [
        'prefab_ultrabarrier', 'prefab_superbarrier', 'prefab_supersmallwall', 'prefab_fort_wall'], 
   A467: [
        'prefab_supertower', 'prefab_superbridge', 'prefab_superminibunker', 'prefab_caltrop'], 
   A468: [
        'prefab_caltrop', 'prefab_superminibunker', 'prefab_safety_tube'], 
   A475: [
        'prefab_caltrop', 'prefab_supertower', 'prefab_ultrabarrier', 
        'prefab_platform', 'prefab_superminibunker', 'prefab_superdome', 
        'prefab_fort_wall', 'prefab_superbridge', 'prefab_superpole'], 
   A469: [
        'prefab_superdome', 'prefab_superpole', 'prefab_safety_corridor'], 
   A470: [
        'prefab_zombiehand', 'prefab_zombiebone', 'prefab_zombiehead'], 
   A471: [], A472: [
        'prefab_small_platform', 'prefab_ladder', 'prefab_square_bunker'], 
   A476: [], A477: [
        'prefab_zombiehand', 'prefab_zombiebone', 'prefab_zombiehead'], 
   A478: [
        'prefab_zombiehand', 'prefab_zombiebone', 'prefab_zombiehead'], 
   A479: [
        'prefab_caltrop', 'prefab_superpole', 'prefab_fort_wall', 'prefab_safety_corridor'], 
   A480: [
        'prefab_supersmallwall', 'prefab_ultrabarrier', 'prefab_fort_wall', 'prefab_superbridge'], 
   A473: [], A474: []}
A482, A483, A484, A485, A486, A487, A488, A489, A490, A491, A492, A493, A494, A495, A496, A497, A498, A499, A500 = xrange(19)
A501, A502, A503, A504, A505, A506 = xrange(6)
A507 = {A501: [
        A482, A483, A484], 
   A502: [
        A486, A487, A488], 
   A503: [
        A489, A490, A491], 
   A504: [
        A492, A493, A494], 
   A505: [
        A495, A496, A497], 
   A506: [
        A498, A499, A500]}
A508 = xrange(1)
A509 = {A508: [
        A482, A483, A484, A485, 
        A486, A487, 
        A488, 
        A489, A490, A491, 
        A492, 
        A493, A494, 
        A495, A496, A497, 
        A498, 
        A499, A500]}
A510 = {'UGC_TOOL_CAT_SPAWNS': [
                         A486, 
                         A487, A488, 
                         A489, 
                         A490, A491], 
   'UGC_TOOL_CAT_BASES': [
                        A492, A493, 
                        A494, 
                        A495, 
                        A496, A497, 
                        A498, 
                        A499, A500, 
                        A485], 
   'UGC_TOOL_CAT_CRATE_DROPS': [
                              A482, A483, A484]}
A511 = {A482: 'A482', 
   A483: 'A483', 
   A484: 'A484', 
   A485: 'A485', 
   A486: 'A486', 
   A487: 'A487', 
   A488: 'A488', 
   A489: 'A489', 
   A490: 'A490', 
   A491: 'A491', 
   A492: 'A492', 
   A493: 'A493', 
   A494: 'A494', 
   A495: 'A495', 
   A496: 'A496', 
   A497: 'A497', 
   A498: 'A498', 
   A499: 'A499', 
   A500: 'A500'}
A512 = [
 A321, A322, A326]
A513 = [A301, A319, A318, A326] + A512
A514 = [A301] + A512
A515, A516, A517, A518, A519, A520, A521, A522 = xrange(8)
A523 = A520
A524 = [
 A516,
 A517,
 A515]
A525 = []
A526 = {A516: 'PRIMARY_WEAPONS', 
   A517: 'SECONDARY_WEAPONS', 
   A518: 'EQUIPMENT', 
   A515: 'MELEE', 
   A519: 'PREFABS', 
   A521: 'UGC_TOOLS'}
A527 = 200
A528 = 1000
A529 = 400
A530 = 1000
A531 = 500
A532 = 1500
A533 = 2000
A534 = 3000
A535 = 0
A536 = 1000
A537 = 1000
A538 = 2000
A539 = 25
A540 = 100
A541 = 500
A542 = 1200
A543 = 1
A544 = 1
A545 = 500
A546 = 1000
A547 = 500
A548 = 1000
A549 = 400
A550 = 1000
A551 = 900
A552 = 2000
A553 = A79
A554 = {A74: {A516: [
              A304, A356], 
         A517: [
              A308, A309], 
         A518: [
              A307, A328, A370], 
         A515: [
              A298, A297], 
         A519: [
              A466, A474, A473], 
         A520: A513, 
         A521: []}, 
   A75: {A516: [
              A314, A315], 
         A517: [
              A313, A349], 
         A518: [
              A316, A352], 
         A515: [
              A296, A297], 
         A519: [
              A467, A474, A473], 
         A520: A513, 
         A521: []}, 
   A76: {A516: [
              A303], 
         A517: [
              A312, A307], 
         A518: [
              A365, A364], 
         A515: [
              A298, A296], 
         A519: [
              A468, A474, A473], 
         A520: A513, 
         A521: []}, 
   A86: {A516: [
              A303], 
         A517: [
              A312, A325, A354], 
         A518: [
              A366, A360], 
         A515: [
              A296], 
         A519: [
              A475, A474, A473], 
         A520: A513, 
         A521: []}, 
   A77: {A516: [
              A305, A306], 
         A517: [
              A310, A359], 
         A518: [
              A317, A355], 
         A515: [
              A299], 
         A519: [
              A469, A474, A473], 
         A520: A513, 
         A521: []}, 
   A78: {A516: [
              A320], 
         A517: [], A518: [], A515: [], A519: [
              A470], 
         A520: [
              A324], 
         A521: []}, 
   A79: {A516: [
              A302, A334, A333], 
         A517: [], A518: [
              A327], 
         A515: [
              A300], 
         A519: [], A520: A514, 
         A521: []}, 
   A80: {A516: [
              A331], 
         A517: [
              A332], 
         A518: [
              A329], 
         A515: [
              A330], 
         A519: [
              A472, A474, A473], 
         A520: A513, 
         A521: []}, 
   A81: {A516: [
              A331], 
         A517: [
              A332], 
         A518: [
              A329], 
         A515: [
              A330], 
         A519: [
              A472, A474, A473], 
         A520: A513, 
         A521: []}, 
   A82: {A516: [
              A331], 
         A517: [
              A332], 
         A518: [
              A329], 
         A515: [
              A330], 
         A519: [
              A472, A474, A473], 
         A520: A513, 
         A521: []}, 
   A83: {A516: [
              A331], 
         A517: [
              A332], 
         A518: [
              A329], 
         A515: [
              A330], 
         A519: [
              A472, A474, A473], 
         A520: A513, 
         A521: []}, 
   A84: {A516: [
              A331], 
         A517: [
              A332], 
         A518: [
              A329], 
         A515: [
              A330], 
         A519: [
              A472, A474, A473], 
         A520: A513, 
         A521: []}, 
   A85: {A516: [
              A331], 
         A517: [
              A332], 
         A518: [
              A329], 
         A515: [
              A330], 
         A519: [
              A472, A474, A473], 
         A520: A513, 
         A521: []}, 
   A87: {A516: [
              A343], 
         A517: [
              A344], 
         A518: [
              A367], 
         A515: [
              A341], 
         A519: [
              A476, A474, A473], 
         A520: [
              A301, A339, A318, A326, A338, A337] + A512, 
         A521: [
              A508]}, 
   A88: {A516: [
              A320], 
         A517: [], A518: [], A515: [], A519: [
              A470], 
         A520: [
              A324], 
         A521: []}, 
   A89: {A516: [
              A320], 
         A517: [], A518: [], A515: [], A519: [
              A470], 
         A520: [
              A324], 
         A521: []}, 
   A90: {A516: [
              A358, A303], 
         A517: [
              A349, A351], 
         A518: [
              A350, A353], 
         A515: [
              A298, A346], 
         A519: [
              A479, A474, A473], 
         A520: A513, 
         A521: []}, 
   A91: {A516: [
              A357, A306], 
         A517: [
              A348], 
         A518: [
              A347], 
         A515: [
              A296, A345], 
         A519: [
              A480, A474, A473], 
         A520: A513, 
         A521: []}}
A555 = {'Hiesville': 'Hiesville_TagLine', 
   'Trenches': 'Trenches_TagLine'}
A556 = {A74: 'SOLDIER_DESCRIPTION', 
   A75: 'SCOUT_DESCRIPTION', 
   A76: 'ROCKETEER_DESCRIPTION', 
   A86: 'ENGINEER_DESCRIPTION', 
   A77: 'MINER_DESCRIPTION', 
   A78: 'ZOMBIE_DESCRIPTION', 
   A79: 'SOLDIER_DESCRIPTION', 
   A80: 'GANGSTER_DESCRIPTION', 
   A81: 'GANGSTER_DESCRIPTION', 
   A82: 'GANGSTER_DESCRIPTION', 
   A83: 'GANGSTER_DESCRIPTION', 
   A84: 'GANGSTER_DESCRIPTION', 
   A85: 'GANGSTER_DESCRIPTION', 
   A87: 'UGCBUILDER_DESCRIPTION', 
   A88: 'ZOMBIE_DESCRIPTION', 
   A89: 'ZOMBIE_DESCRIPTION', 
   A90: 'SPECIALIST_DESCRIPTION', 
   A91: 'MEDIC_DESCRIPTION'}
A557 = {A304: 'minigun', 
   A308: 'rpg', 
   A309: 'rpg2', 
   A342: 'ugc_rpg2', 
   A325: 'snowblower', 
   A344: 'snowblower', 
   A314: 'sniper', 
   A315: 'sniper2', 
   A303: 'smg', 
   A349: 'autoPistol', 
   A305: 'shotgun', 
   A306: 'shotgun2', 
   A313: 'pistol', 
   A307: 'grenade', 
   A327: 'grenade', 
   A328: 'antipersonnel_grenade', 
   A316: 'land_mine', 
   A310: 'drillgun', 
   A343: 'drillgun', 
   A317: 'dynamite', 
   A364: 'jetpack', 
   A365: 'jetpack2', 
   A366: 'jetpack_engineer', 
   A367: 'jetpack_ugcbuilder', 
   A320: 'zombie_hands', 
   A296: 'pickaxe', 
   A340: 'ugc_pickaxe', 
   A297: 'knife', 
   A299: 'superspade', 
   A341: 'ugc_superspade', 
   A298: 'spade', 
   A300: 'spade', 
   A301: 'block', 
   A302: 'semi', 
   A311: 'mg', 
   A312: 'rocket_turret', 
   A319: 'prefab', 
   A318: 'glowblock', 
   A321: 'bomb', 
   A322: 'diamond', 
   A323: 'shrapnel', 
   A324: 'prefab', 
   A326: 'intel', 
   A329: 'Weapon_Molotov', 
   A330: 'Weapon_Crowbar', 
   A331: 'Weapon_TommyGun', 
   A332: 'Weapon_SnubNosePistol', 
   A333: 'classic_shotgun', 
   A334: 'classic_smg', 
   A335: 'null_tool', 
   A337: 'ugc_tool', 
   A336: 'pistol', 
   A338: 'ugc_prefab', 
   A339: 'paintbrush', 
   A345: 'riotstick', 
   A346: 'machete', 
   A347: 'medpack', 
   A348: 'riotshield', 
   A350: 'chemicalbomb', 
   A351: 'grenadelauncher', 
   A352: 'radar_station', 
   A370: 'parachute', 
   A353: 'stickygrenade', 
   A354: 'minelauncher', 
   A355: 'c4', 
   A356: 'assaultRifle', 
   A357: 'lightMachineGun', 
   A358: 'autoShotgun', 
   A359: 'blocksucker', 
   A360: 'disguise'}
A558 = {A304: 'MINIGUN', 
   A308: 'ROCKET_PROPELLED_GRENADE', 
   A309: 'ROCKET_PROPELLED_GRENADE2', 
   A342: 'UGC_RPG2', 
   A325: 'SNOWBLOWER', 
   A344: 'SNOWBLOWER', 
   A314: 'SNIPER_RIFLE', 
   A315: 'SNIPER2_RIFLE', 
   A303: 'SUB_MACHINE_GUN', 
   A349: 'AUTOMATIC_PISTOL', 
   A305: 'SHOTGUN', 
   A306: 'SHOTGUN2', 
   A313: 'PISTOL', 
   A307: 'A307', 
   A327: 'CLASSIC_GRENADE', 
   A328: 'A328', 
   A316: 'A316', 
   A310: 'DRILL_TOOL', 
   A343: 'DRILL_TOOL', 
   A317: 'A317', 
   A364: 'A364', 
   A365: 'JETPACK_2', 
   A366: 'A366', 
   A367: 'A367', 
   A320: 'ZOMBIE_HANDS', 
   A296: 'PICKAXE', 
   A340: 'UGC_PICKAXE', 
   A297: 'KNIFE', 
   A299: 'SUPER_SPADE', 
   A341: 'UGC_SUPERSPADE', 
   A298: 'SPADE', 
   A300: 'SPADE', 
   A301: 'A301', 
   A302: 'RIFLE', 
   A311: 'MOUNTED_GUN', 
   A312: 'ROCKET_TURRET', 
   A319: 'A319', 
   A318: 'FLARE_BLOCK_TOOL', 
   A321: 'A321', 
   A322: 'A322', 
   A323: 'A323', 
   A324: 'ZOMBIE_PREFAB_TOOL', 
   A326: 'A326', 
   A329: 'A329', 
   A330: 'A330', 
   A331: 'A331', 
   A332: 'A332', 
   A333: 'CLASSIC_SHOTGUN', 
   A334: 'CLASSIC_SUB_MACHINE_GUN', 
   A335: 'NULL_TOOL', 
   A337: 'A337', 
   A336: 'FAKE_PISTOL_TOOL', 
   A338: 'UGC_PREFAB_TOOL', 
   A339: 'PAINTBRUSH_TOOL', 
   A345: 'RIOTSTICK', 
   A346: 'MACHETE', 
   A347: 'MEDPACK_WEAPON', 
   A348: 'RIOTSHIELD', 
   A350: 'CHEMICALBOMB', 
   A351: 'GRENADE_LAUNCHER_WEAPON', 
   A352: 'RADAR_STATION', 
   A370: 'A370', 
   A353: 'STICKY_GRENADE', 
   A354: 'MINE_LAUNCHER', 
   A355: 'C4', 
   A356: 'ASSAULT_RIFLE', 
   A357: 'LIGHT_MACHINE_GUN', 
   A358: 'AUTO_SHOTGUN', 
   A359: 'BLOCK_SUCKER', 
   A360: 'DISGUISE'}
A559 = {A304: 'MINIGUN_TOOL_DESCRIPTION', 
   A308: 'RPG_TOOL_DESCRIPTION', 
   A309: 'RPG2_TOOL_DESCRIPTION', 
   A342: 'UGC_RPG2_TOOL_DESCRIPTION', 
   A325: 'SNOWBLOWER_DESCRIPTION', 
   A344: 'SNOWBLOWER_DESCRIPTION', 
   A313: 'PISTOL_TOOL_DESCRIPTION', 
   A307: 'GRENADE_TOOL_DESCRIPTION', 
   A327: 'CLASSIC_GRENADE_TOOL_DESCRIPTION', 
   A328: 'ANTIPERSONNEL_GRENADE_TOOL_DESCRIPTION', 
   A298: 'SPADE_TOOL_DESCRIPTION', 
   A300: 'CLASSIC_SPADE_TOOL_DESCRIPTION', 
   A314: 'SNIPER_TOOL_DESCRIPTION', 
   A315: 'SNIPER2_TOOL_DESCRIPTION', 
   A316: 'LANDMINE_TOOL_DESCRIPTION', 
   A296: 'PICKAXE_TOOL_DESCRIPTION', 
   A340: 'UGC_PICKAXE_TOOL_DESCRIPTION', 
   A297: 'KNIFE_TOOL_DESCRIPTION', 
   A364: 'JETPACK_NORMAL_DESCRIPTION', 
   A365: 'JETPACK_2_DESCRIPTION', 
   A366: 'JETPACK_ENGINEER_DESCRIPTION', 
   A367: 'JETPACK_UGCBUILDER_DESCRIPTION', 
   A303: 'SMG_TOOL_DESCRIPTION', 
   A349: 'AUTOPISTOL_TOOL_DESCRIPTION', 
   A312: 'ROCKET_TURRET_TOOL_DESCRIPTION', 
   A305: 'SHOTGUN_TOOL_DESCRIPTION', 
   A306: 'SHOTGUN2_TOOL_DESCRIPTION', 
   A310: 'DRILLGUN_TOOL_DESCRIPTION', 
   A343: 'DRILLGUN_TOOL_DESCRIPTION', 
   A317: 'DYNAMITE_TOOL_DESCRIPTION', 
   A299: 'SUPERSPADE_TOOL_DESCRIPTION', 
   A341: 'UGC_SUPERSPADE_TOOL_DESCRIPTION', 
   A320: 'ZOMBIEHAND_TOOL_DESCRIPTION', 
   A302: 'RIFLE_TOOL_DESCRIPTION', 
   A329: 'MOLOTOV_TOOL_DESCRIPTION', 
   A330: 'CROWBAR_TOOL_DESCRIPTION', 
   A331: 'TOMMYGUN_TOOL_DESCRIPTION', 
   A332: 'SNUB_PISTOL_TOOL_DESCRIPTION', 
   A311: 'MG_TOOL_DESCRIPTION', 
   A333: 'CLASSIC_SHOTGUN_TOOL_DESCRIPTION', 
   A334: 'CLASSIC_SMG_TOOL_DESCRIPTION', 
   A335: 'NULL_TOOL_DESCRIPTION', 
   A337: 'UGC_TOOL_DESCRIPTION', 
   A336: 'FAKE_PISTOL_TOOL_DESCRIPTION', 
   A339: 'PAINTBRUSH_TOOL_DESCRIPTION', 
   A345: 'RIOTSTICK_TOOL_DESCRIPTION', 
   A346: 'MACHETE_TOOL_DESCRIPTION', 
   A347: 'MEDPACK_TOOL_DESCRIPTION', 
   A348: 'RIOTSHIELD_TOOL_DESCRIPTION', 
   A350: 'CHEMICALBOMB_TOOL_DESCRIPTION', 
   A351: 'GRENADE_LAUNCHER_TOOL_DESCRIPTION', 
   A352: 'RADAR_STATION_TOOL_DESCRIPTION', 
   A370: 'PARACHUTE_NORMAL_DESCRIPTION', 
   A353: 'STICKY_GRENADE_TOOL_DESCRIPTION', 
   A354: 'MINE_LAUNCHER_TOOL_DESCRIPTION', 
   A355: 'C4_TOOL_DESCRIPTION', 
   A356: 'ASSAULTRIFLE_TOOL_DESCRIPTION', 
   A357: 'LIGHTMACHINEGUN_TOOL_DESCRIPTION', 
   A358: 'AUTOSHOTGUN_TOOL_DESCRIPTION', 
   A359: 'BLOCKSUCKER_TOOL_DESCRIPTION', 
   A360: 'DISGUISE_TOOL_DESCRIPTION'}
A560 = {A304: True, 
   A308: True, 
   A309: True, 
   A342: True, 
   A325: True, 
   A344: True, 
   A314: 2, 
   A315: True, 
   A303: True, 
   A305: True, 
   A306: True, 
   A313: True, 
   A307: True, 
   A327: True, 
   A328: True, 
   A316: True, 
   A310: True, 
   A343: True, 
   A317: True, 
   A364: True, 
   A365: True, 
   A366: True, 
   A367: True, 
   A320: True, 
   A296: True, 
   A340: True, 
   A297: True, 
   A299: True, 
   A341: True, 
   A298: True, 
   A300: True, 
   A301: True, 
   A302: True, 
   A311: False, 
   A312: True, 
   A319: True, 
   A318: True, 
   A321: True, 
   A322: True, 
   A323: False, 
   A324: True, 
   A326: True, 
   A329: True, 
   A330: True, 
   A331: True, 
   A332: True, 
   A333: True, 
   A334: True, 
   A335: False, 
   A337: True, 
   A336: False, 
   A338: False, 
   A339: True, 
   A345: True, 
   A346: True, 
   A347: True, 
   A348: True, 
   A350: True, 
   A349: True, 
   A351: True, 
   A352: True, 
   A370: True, 
   A353: True, 
   A354: True, 
   A355: True, 
   A356: True, 
   A357: True, 
   A358: True, 
   A359: True, 
   A360: True}
A561 = 3
A562, A563, A564, A565, A566, A567, A568, A569, A570, A571, A572, A573, A574, A575, A576, A577, A578, A579, A580, A581, A582, A583, A584, A585, A586, A587, A588, A589, A590, A591 = xrange(30)
A592 = {A562: 'MOST_DistanceTravelled', 
   A563: 'MOST_TimeInAir', 
   A564: 'MOST_HealthCratesCollected', 
   A565: 'MOST_AmmoCratesCollected', 
   A566: 'MOST_BlockCratesCollected', 
   A567: 'MOST_Kills', 
   A568: 'MOST_KillsAtLowHealth', 
   A569: 'MOST_Teabags', 
   A570: 'MOST_Headshots', 
   A571: 'MOST_BlocksPlaced', 
   A572: 'MOST_BlocksDestroyed', 
   A573: 'BIGGEST_KillStreak', 
   A574: 'BIGGEST_CollapsingObject', 
   A575: 'BIGGEST_RangedKill', 
   A576: 'MOST_MeleeKills', 
   A577: 'MOST_BrainsEaten', 
   A578: 'MOST_Distractions', 
   A579: 'MOST_Defends', 
   A580: 'MOST_Assists', 
   A581: 'MOST_AirStrikesSurvived', 
   A582: 'MOST_DamageTaken', 
   A583: 'HIGHEST_Block', 
   A584: 'MOST_HeadshotsReceived', 
   A585: 'MOST_SnipersKilled', 
   A586: 'FEWEST_ShotsFired', 
   A587: 'MOST_Suicides', 
   A588: 'MOST_KillSteals', 
   A589: 'MOST_TimeOnFire', 
   A590: 'MOST_Dominated', 
   A591: 'MOST_Dominations'}
A593, A594 = xrange(2)
A595 = 251
A596, A597, A598, A599, A600, A601, A602, A603, A604, A605, A606, A607, A608, A609, A610, A611, A612, A613, A614, A615, A616, A617, A618, A619, A620, A621, A622, A623, A624, A625, A626, A627, A628, A629, A630, A631, A632, A633, A634, A635, A636, A637, A638, A639, A640, A641, A642, A643, A644, A645, A646, A647, A648, A649, A650, A651, A652, A653, A654, A655, A656, A657, A658, A659, A660, A661, A662, A663, A664, A665, A666, A667, A668, A669, A670, A671, A672, A673, A674, A675, A676, A677, A678, A679, A680, A681, A682, A683, A684, A685, A686, A687, A688, A689, A690, A691, A692, A693, A694, A695, A696, A697, A698, A699, A700, A701, A702, A703, A704, A705, A706, A707, A708, A709, A710, A711, A712, A713, A714, A715, A716, A717, A718, A719, A720, A721, A722, A723, A724, A725, A726, A727, A728, A729, A730, A731, A732, A733, A734, A735, A736, A737, A738, A739, A740, A741, A742, A743, A744, A745, A746, A747, A748, A749, A750, A751, A752, A753, A754, A755, A756, A757, A758, A759, A760, A761, A762, A763, A764, A765, A766, A767, A768, A769, A770, A771, A772, A773, A774, A775, A776, A777, A778, A779, A780, A781, A782, A783, A784, A785, A786, A787, A788, A789, A790, A791, A792, A793, A794, A795, A796, A797, A798, A799, A800, A801, A802, A803, A804, A805, A806, A807, A808, A809, A810, A811, A812, A813, A814, A815, A816, A817, A818, A819, A820, A821, A822, A823, A824, A825, A826, A827, A828, A829, A830, A831, A832, A833, A834, A835, A836, A837, A838, A839, A840, A841, A842, A843, A844, A845, A846 = xrange(A595)
A847 = A295
A848 = xrange(1000, 1000 + A847)
A849 = xrange(2000, 2000 + A847)
A850 = xrange(3000, 3000 + A847)
A851 = {A596: '', 
   A597: 'TDM_Kill', 
   A598: 'TDM_Suicide', 
   A599: 'TDM_Headshot', 
   A600: 'TDM_Melee', 
   A601: 'TDM_Assist', 
   A602: 'TDM_TeamKill', 
   A603: 'TDM_Revenge', 
   A604: 'TDM_Distract', 
   A605: 'TDM_Payback', 
   A606: 'TDM_Reload', 
   A607: 'TDM_Defend', 
   A608: 'VIP_Survive', 
   A609: 'VIP_Escort', 
   A610: 'VIP_KillEnemyVIP', 
   A611: 'VIP_Distract', 
   A612: 'VIP_Kill', 
   A613: 'VIP_Assault', 
   A614: 'VIP_Assault_Enemy', 
   A615: 'VIP_Defend', 
   A616: 'TC_Occupy', 
   A617: 'TC_Claim', 
   A618: 'TC_Control', 
   A619: 'TC_Defend', 
   A620: 'TC_Assault', 
   A621: 'TC_Contend', 
   A622: 'OCC_Occupy', 
   A623: 'OCC_Carry', 
   A624: 'OCC_Boom', 
   A625: 'OCC_Distract', 
   A626: 'OCC_Carrier_Defend', 
   A627: 'OCC_Defend', 
   A628: 'OCC_Assault', 
   A629: 'OCC_Survive', 
   A630: 'OCC_Intercept', 
   A631: 'OCC_LastMan_Total', 
   A632: 'Occ_Disposal', 
   A633: 'Occ_Intercept_Disposal', 
   A634: 'DIA_Capture', 
   A635: 'DIA_Uncover', 
   A636: 'DIA_Carry', 
   A637: 'DIA_Escort', 
   A638: 'DIA_Distract', 
   A639: 'DIA_Carrier_Defend', 
   A640: 'DIA_Defend', 
   A641: 'DIA_Assault', 
   A642: 'DIA_Intercept', 
   A643: 'DIA_Steal_Total', 
   A644: 'DIA_FindAndCashIn_Total', 
   A645: 'CTF_Capture', 
   A646: 'CTF_Carry', 
   A647: 'CTF_Escort', 
   A648: 'CTF_Claim', 
   A649: 'CTF_Distract', 
   A650: 'CTF_Defend', 
   A651: 'CTF_Assault', 
   A652: 'CTF_Assault_Enemy', 
   A653: 'CTF_Carrier_Defend', 
   A654: 'CTF_Intercept', 
   A655: 'ZOM_Survive', 
   A656: 'ZOM_LastMan', 
   A657: 'ZOM_KillSurvivor', 
   A658: 'ZOM_LastManZombieKill', 
   A659: 'ZOM_Zombies_Killed_Total', 
   A660: 'ZOM_Time_Survived_Total', 
   A661: 'ZOM_LastMan_Time_Total', 
   A662: 'ZOM_Pistol_ZombieKill_Total', 
   A663: 'ZOM_LastMan_Kills_Total', 
   A664: 'ZOM_LastManStanding_Total', 
   A665: 'DEM_Destroy', 
   A666: 'DEM_Repair', 
   A667: 'DEM_Defend', 
   A668: 'DEM_Assault', 
   A669: 'DEM_Repair_Total', 
   A670: 'DEM_DestroyOverMultiple_Total', 
   A671: 'DEM_FinalDamageToBase_Total', 
   A672: 'MH_Occupy', 
   A673: 'MH_First', 
   A674: 'MH_Claim', 
   A675: 'MH_Control', 
   A676: 'MH_Defend', 
   A677: 'MH_Assault', 
   A678: 'MH_Contest', 
   A679: 'MH_Survive_Airstrike_Total', 
   A680: 'MH_Trigger_Airstrike_Total', 
   A681: 'ZOMBIE_HumansKilled_Total', 
   A682: 'ZOMBIE_HumansKilled_InWater_Total', 
   A683: 'ZOMBIE_HumansKilled_AsPatientZero_Total', 
   A684: 'ZOMBIE_Blocks_Destroyed_Total', 
   A685: 'ZOMBIE_Hands_Kills', 
   A686: 'SOLDIER_Minigun_Kills', 
   A687: 'SOLDIER_RPG_Kills', 
   A688: 'SOLDIER_RPG2_Kills', 
   A689: 'SOLDIER_Pistol_Kills', 
   A690: 'SOLDIER_Grenade_Kills', 
   A691: 'SOLDIER_APG_Kills', 
   A692: 'SOLDIER_Snowblower_Kills', 
   A693: 'SOLDIER_Spade_Kills', 
   A694: 'SOLDIER_Knife_Kills', 
   A695: 'SOLDIER_Minigun_Demolish_Total', 
   A696: 'SOLDIER_RPG_Fall_Total', 
   A697: 'SOLDIER_Airborne_Rocket_Kills', 
   A698: 'SCOUT_Sniper_Kills', 
   A699: 'SCOUT_Sniper2_Kills', 
   A700: 'SCOUT_Landmine_Kills', 
   A701: 'SCOUT_Snowblower_Kills', 
   A702: 'SCOUT_Pickaxe_Kills', 
   A703: 'SCOUT_Knife_Kills', 
   A704: 'SCOUT_Sniper_Streak3_Total', 
   A705: 'SCOUT_Sniper_Streak6_Total', 
   A707: 'SCOUT_Sniper2_Speed_Total', 
   A706: 'SCOUT_Sniper_Headshot_Total', 
   A708: 'ROCKETEER_SMG_Kills', 
   A709: 'ROCKETEER_Turret_Kills', 
   A710: 'ROCKETEER_Grenade_Kills', 
   A711: 'ROCKETEER_Spade_Kills', 
   A712: 'ROCKETEER_Pickaxe_Kills', 
   A713: 'ROCKETEER_Jetpack_Kills', 
   A714: 'ROCKETEER_Jetpack_Grenade_Kills', 
   A715: 'ROCKETEER_Jetpack_SMG_Kills', 
   A821: 'ENGINEER_SMG_Kills', 
   A829: 'ENGINEER_Snowblower_Kills', 
   A822: 'ENGINEER_Turret_Kills', 
   A825: 'ENGINEER_Pickaxe_Kills', 
   A826: 'ENGINEER_Jetpack_Kills', 
   A828: 'ENGINEER_Jetpack_SMG_Kills', 
   A716: 'MINER_Shotgun_Kills', 
   A717: 'MINER_Shotgun2_Kills', 
   A718: 'MINER_Dynamite_Kills', 
   A719: 'MINER_Snowblower_Kills', 
   A720: 'MINER_Superspade_Kills', 
   A721: 'MINER_Pickaxe_Kills', 
   A722: 'MINER_Drill_Demolish_Total', 
   A723: 'MINER_Dynamite_Below_Kills', 
   A724: 'MINER_Shotgun_Headshot_Total', 
   A725: 'MINER_Shotgun_Zombie_Kills', 
   A726: 'GANGSTER_Tommygun_Kills', 
   A727: 'GANGSTER_Pistol_Kills', 
   A728: 'GANGSTER_Molotov_Kills', 
   A729: 'GANGSTER_Crowbar_Kills', 
   A730: 'CLASSIC_SOLDIER_Rifle_Kills', 
   A731: 'CLASSIC_SOLDIER_Grenade_Kills', 
   A732: 'CLASSIC_SOLDIER_Spade_Kills', 
   A733: 'CLASSIC_SOLDIER_Rifle_Headshot_Total', 
   A734: 'CLASSIC_SOLDIER_Intel_Kills', 
   A735: 'COMBAT_5InARow_Total', 
   A736: 'COMBAT_10InARow_Total', 
   A737: 'COMBAT_15InARow_Total', 
   A738: 'COMBAT_DistanceRan_Total', 
   A739: 'COMBAT_AmmoDrop_Total', 
   A740: 'COMBAT_HealthDrop_Total', 
   A741: 'COMBAT_BlockDrop_Total', 
   A742: 'COMBAT_GrenadeDemolish_Total', 
   A743: 'COMBAT_KillJetpack_Total', 
   A744: 'COMBAT_Pickaxe_Kills', 
   A745: 'COMBAT_Pistol_Kills', 
   A746: 'COMBAT_Spade_Kills', 
   A747: 'COMBAT_TurretEvasion_Total', 
   A748: 'COMBAT_Teabag_Total', 
   A749: 'COMBAT_TeabagClassic_Total', 
   A750: 'COMBAT_KillsAtLowHealth_Total', 
   A751: 'COMBAT_TimeInAir_Total', 
   A752: 'MAP_SingleBlocksAdded_Total', 
   A753: 'MAP_PrefabAdded_Total', 
   A754: 'MAP_BlocksDestroyed_Total', 
   A755: 'GAME_Wins_Total', 
   A756: 'GAME_Losses_Total', 
   A757: 'GAME_Draws_Total', 
   A758: 'Ancient_Egypt_time_score', 
   A759: 'Arctic_Base_time_score', 
   A760: 'Bran_Castle_time_score', 
   A761: 'Dragon_Island_time_score', 
   A762: 'London_time_score', 
   A763: 'Lunar_Base_time_score', 
   A764: 'Mayan_Jungle_time_score', 
   A765: 'Spooky_Mansion_time_score', 
   A766: 'Tokyo_Neon_time_score', 
   A767: 'Hiesville_time_score', 
   A768: 'Block_Ness_time_score', 
   A769: 'Castle_Wars_time_score', 
   A770: 'Double_Dragon_time_score', 
   A771: 'WW1_time_score', 
   A772: 'To_The_Bridge_time_score', 
   A773: 'Crossroads_time_score', 
   A774: 'Winter_Valley_time_score', 
   A775: 'Trenches_time_score', 
   A776: 'City_Of_Chicago_time_score', 
   A777: 'Alcatraz_time_score', 
   A778: 'Zombie_mode_score', 
   A779: 'TDM_mode_score', 
   A780: 'Diamond_mine_mode_score', 
   A781: 'Occupation_mode_score', 
   A782: 'Demolition_mode_score', 
   A783: 'Multihill_mode_score', 
   A784: 'VIP_mode_score', 
   A785: 'Capture_the_flag_mode_score', 
   A786: 'Territory_control_mode_score', 
   A787: 'Classic_CTF_mode_score', 
   A788: 'TDM_total_score', 
   A789: 'VIP_total_score', 
   A790: 'TC_total_score', 
   A791: 'OCC_total_score', 
   A792: 'DIA_total_score', 
   A793: 'CTF_total_score', 
   A794: 'ZOM_total_score', 
   A795: 'DEM_total_score', 
   A796: 'MH_total_score', 
   A797: 'Complete_total_score', 
   A798: 'COM_TDM_ASSIST', 
   A799: 'COM_TDM_RETRIBUTION', 
   A800: 'COM_VIP_SURVIVE', 
   A801: 'COM_VIP_ASSAULT', 
   A802: 'COM_VIP_DEFEND', 
   A803: 'COM_VIP_ESCORT', 
   A804: 'COM_TC_CONTEND', 
   A805: 'COM_OCC_CARRY', 
   A806: 'COM_OCC_ASSIST', 
   A807: 'COM_OCC_DEFEND', 
   A808: 'COM_OCC_SURVIVAL', 
   A809: 'COM_DIA_ASSIST', 
   A810: 'COM_DIA_ASSAULT', 
   A811: 'COM_DIA_STEAL', 
   A812: 'COM_CTF_ASSIST', 
   A813: 'COM_CTF_DEFEND', 
   A814: 'COM_CTF_ASSAULT', 
   A815: 'COM_MH_CONTROL', 
   A816: 'DEATH_SCORE_REASON', 
   A817: '', 
   A818: 'SUPER_MARKSMAN_SCORE_REASON', 
   A819: 'SUPER_SPRINTER_SCORE_REASON', 
   A820: 'KICKED_SCORE_REASON', 
   A830: 'MEDIC_RiotStick_Kills', 
   A831: 'MEDIC_RiotShield_Kills', 
   A832: 'MEDIC_LightMachineGun_Kills', 
   A841: 'MEDIC_Pickaxe_Kills', 
   A842: 'MEDIC_Shotgun2_Kills', 
   A833: 'SPECIALIST_Machete_Kills', 
   A834: 'SPECIALIST_AutoPistol_Kills', 
   A835: 'SPECIALIST_ChemicalBomb_Kills', 
   A836: 'SPECIALIST_GrenadeLauncher_Kills', 
   A837: 'SPECIALIST_StickyGrenade_Kills', 
   A838: 'SPECIALIST_AutoShotgun_Kills', 
   A839: 'SPECIALIST_Spade_Kills', 
   A840: 'SPECIALIST_Smg_Kills', 
   A843: 'MINER_C4_Kills', 
   A844: 'ENGINEER_MineLauncher_Kills', 
   A845: 'SOLDIER_AssaultRifle_Kills', 
   A846: 'SPECIALIST_AutoPistol_Kills'}
A852 = {'Ancient Egypt': A758, 
   'Arctic Base': A759, 
   'Bran Castle': A760, 
   'Dragon Island': A761, 
   'London': A762, 
   'Lunar Base': A763, 
   'Mayan Jungle': A764, 
   'Spooky Mansion': A765, 
   'Tokyo Neon': A766, 
   'Hiesville': A767, 
   'Block Ness': A768, 
   'Castle Wars': A769, 
   'Double Dragon': A770, 
   'WW1': A771, 
   'To The Bridge': A772, 
   'Crossroads': A773, 
   'Winter Valley': A774, 
   'Trenches': A775, 
   'City Of Chicago': A776, 
   'Alcatraz': A777}
A853 = {'zom': A778, 
   'tdm': A779, 
   'dia': A780, 
   'oc': A781, 
   'dem': A782, 
   'mh': A783, 
   'vip': A784, 
   'ctf': A785, 
   'tc': A786, 
   'cctf': A787}
A854 = {A798: [
        A601, A604, A606], 
   A799: [
        A603, A605], 
   A800: [
        A608, A612], 
   A801: [
        A610, A613, A614], 
   A802: [
        A615, A611], 
   A804: [
        A620, A621], 
   A805: [
        A623, A625], 
   A806: [
        A627, A626, A628], 
   A807: [
        A630, A632, A633], 
   A808: [
        A631, A629], 
   A809: [
        A637, A638, A639], 
   A810: [
        A640, A641, A642], 
   A811: [
        A643, A644], 
   A812: [
        A647, A649], 
   A813: [
        A650, A653], 
   A814: [
        A651, A652, A654], 
   A815: [
        A674, A675], 
   A788: [
        A599, A600, A597, A798, A799, A607], 
   A789: [
        A609, A800, A801, A802], 
   A790: [
        A616, A617, A618, A619, A804], 
   A791: [
        A622, A624, A805, A806, A807, A808], 
   A792: [
        A634, A635, A636, A809, A810, A811], 
   A793: [
        A645, A646, A648, A812, A813, A814], 
   A794: [
        A655, A656, A657, A658], 
   A795: [
        A665, A666, A667, A668], 
   A796: [
        A672, A673, A815, A676, A677, A678]}
A855, A856, A857, A858, A859, A860, A861, A862, A863, A864, A865 = xrange(11)
A866, A867, A868, A869, A870 = xrange(5)
A871 = {A855: [
        'GENERAL', 'General Global', 'General Local', A797,
        [
         A597, A816, A597, A755, A756]], 
   A856: [
        'TDM_TITLE', A851[A788] + ' global', A851[A788] + ' local', A788,
        A854[A788]], 
   A857: [
        'VIP_MODE_TITLE', A851[A789] + ' global', A851[A789] + ' local', A789,
        A854[A789]], 
   A858: [
        'TC_TITLE', A851[A790] + ' global', A851[A790] + ' local', A790,
        A854[A790]], 
   A859: [
        'OCCUPATION_MODE_TITLE', A851[A791] + ' global', A851[A791] + ' local', A791,
        A854[A791]], 
   A860: [
        'DIAMOND_MINE_TITLE', A851[A792] + ' global', A851[A792] + ' local', A792,
        A854[A792]], 
   A861: [
        'CTF_TITLE', A851[A793] + ' global', A851[A793] + ' local', A793,
        A854[A793]], 
   A862: [
        'ZOMBIE_MODE_TITLE', A851[A794] + ' global', A851[A794] + ' local', A794,
        A854[A794]], 
   A863: [
        'DEMOLITION_TITLE', A851[A795] + ' global', A851[A795] + ' local', A795,
        A854[A795]], 
   A864: [
        'MULTIHILL_TITLE', A851[A796] + ' global', A851[A796] + ' local', A796,
        A854[A796]]}
A872, A873, A874, A875 = xrange(4)
A876 = {A872: 'KICK_REASON_GRIEFING', A873: 'KICK_REASON_HACKING', 
   A874: 'KICK_REASON_ABUSE'}
A877, A878, A879 = xrange(3)
A880 = 1
A881 = 2
A882 = 3
A883 = 4
A884 = {A880: 'Success', 
   A881: 'Failed', 
   A882: 'Invalid parameter', 
   A883: 'Internal error'}
A885 = 6.0
A886, A887, A888, A889 = xrange(4)
A890, A891, A892, A893, A894 = xrange(5)
A895, A896, A897, A898 = xrange(4)
A899, A900, A901, A902, A903, A904, A905, A906, A907, A908, A909, A910, A911, A912, A913, A914, A915, A916, A917, A918, A919, A920, A921, A922, A923, A924, A925, A926, A927, A928, A929, A930, A931, A932, A933, A934, A935, A936, A937, A938 = xrange(40)
A939, A940, A941, A942, A943, A944, A945, A946, A947, A948, A949, A950, A951, A952, A953, A954, A955, A956, A957, A958, A959, A960, A961, A962, A963, A964, A965, A966, A967, A968, A969, A970 = xrange(32)
A971, A972, A973, A974, A975, A976, A977, A978, A979, A980 = xrange(10)
A981, A982, A983, A984, A985 = xrange(5)
A986, A987, A988, A989, A990, A991, A992 = xrange(7)
A993 = 1.0
A994 = 90
A995 = 99999
A996 = 2000
A997 = 40
A998 = 60
A999 = 10
A1000 = 3.0
A1001 = 100.0
A1002 = 30.0
A1003 = 60.0
A1004 = 1.0 / A1003
A1005 = 5
A1006 = 1.0 / A1005
A1007 = 20
A1008 = 1.0 / A1007
A1009 = 4
A1010, A1011 = xrange(2)
A1012 = 5
A1013 = 60
A1014 = 10
A1015 = 10
A1016 = 0.1
A1017 = 10
A1018 = 5.0
A1019 = 2.5
A1020 = 3.0
A1021 = 3.0
A1022 = 10.0
A1023 = 2.5
A1024 = 10
A1025 = 50
A1026 = 1 / 30.0
A1027 = 2
A1028 = 1.2
A1029 = 1.2
A1030 = 1.2
A1031 = 5
A1032 = 9
A1033 = 3
A1034 = 2
A1035 = 8
A1036 = 5
A1037 = 60
A1038 = 0.3
A1039 = 25
A1040 = 10
A1041 = 2
A1042 = 0.75
A1043 = False
A1044 = True
A1045 = (0, 0.707, -0.707)
A1046 = (0, 0.707, 0.707)
A1047 = (1.0, 1.0, 1.0, 1.0)
A1048 = (1.0, 1.0, 0.0, 0.0)
A1049 = (255, 255, 255, 255)
A1050 = 0.0075
A1051 = (255, 255, 255, 200)
A1052 = (255, 0, 0, 200)
A1053 = (20, 20, 20, 255)
A1054 = (244, 236, 187, 255)
A1055 = (122, 118, 94, 255)
A1056 = (232, 207, 78, 255)
A1057 = (244, 236, 187, 255)
A1058 = (255, 255, 255, 255)
A1059 = (0, 0, 0, 255)
A1060 = (255, 255, 255, 255)
A1061 = (0, 0, 0, 255)
A1062 = (255, 255, 255, 255)
A1063 = (243, 237, 179)
A1064 = (86, 100, 21, 255)
A1065 = (137, 179, 45, 255)
A1066 = (255, 0, 0, 255)
A1067 = 10
A1068 = 5.5
A1069 = 0.75
A1070 = 1.5
A1071 = 2.0
A1072 = A1069 + A1070 + A1071
A1073 = 0.5
A1074 = 0.5
A1075 = 0.3
A1076 = 3
A1077 = 0.0
A1078 = 0.4
A1079 = 0.3
A1080 = 0.3
A1081 = (104, 173, 87, 255)
A1082 = (192, 255, 132)
A1083 = 2.0
A1084 = 3
A1085 = 4
A1086 = 10000
A1087 = 10000
A1088 = 1.0
A1089 = 0.5
A1090 = 0.5
A1091 = 200
A1092 = 200
A1093 = 0.8
A1094 = 5
A1095 = 35
A1096 = 0.6
A1097 = 7.5
A1098 = 50
A1099 = 0.2
A1100 = 7.5
A1101 = 7.5
A1102 = 0
A1103 = 0.6
A1104 = 7
A1105 = 40
A1106 = 0.2
A1107 = 9
A1108 = 0
A1109 = 0.5
A1110 = 1.0
A1111 = 80
A1112 = 0.5
A1113 = 5
A1114 = 80
A1115 = 0.4
A1116 = 2
A1117 = 70
A1118 = 550
A1119 = 0.6
A1120 = 0.4
A1121 = 0.015
A1122 = -0.05
A1123 = 0
A1124 = 20
A1125 = 45
A1126 = 20
A1127 = 20
A1128 = 20
A1129 = 3
A1130 = 30
A1131 = A1130
A1132 = A1130
A1133 = 6
A1134 = 500
A1135 = 0.75
A1136 = 1.0
A1137 = 0.5
A1138 = 0.01
A1139 = -0.05
A1140 = 0
A1141 = 40
A1142 = 70
A1143 = 30
A1144 = 30
A1145 = 20
A1146 = 1
A1147 = 30
A1148 = A1147
A1149 = A1147
A1150 = 6
A1151 = 350
A1152 = 1.25
A1153 = 0.11
A1154 = 0.1
A1155 = 0.02
A1156 = 0.02
A1157 = 1
A1158 = 5
A1159 = 0.2
A1160 = 1
A1161 = -0.01
A1162 = 2e-05
A1163 = 10
A1164 = 15
A1165 = 10
A1166 = 10
A1167 = 15
A1168 = 1
A1169 = 100
A1170 = A1169
A1171 = A1169
A1172 = 25
A1173 = 100
A1174 = 1.25
A1175 = 0.11
A1176 = 0.1
A1177 = 0.01
A1178 = 0.05
A1179 = 1
A1180 = 5
A1181 = 0.2
A1182 = 0.6
A1183 = -0.007
A1184 = 0
A1185 = 20
A1186 = 20
A1187 = 20
A1188 = 20
A1189 = 20
A1190 = 2
A1191 = 100
A1192 = A1169
A1193 = A1169
A1194 = 25
A1195 = 300
A1196 = 1
A1197 = 0.11
A1198 = 0.175
A1199 = 0.02
A1200 = 0.02
A1201 = 1.5
A1202 = 5
A1203 = 0.3
A1204 = 2
A1205 = -0.0175
A1206 = 0.0001
A1207 = 15
A1208 = 30
A1209 = 15
A1210 = 15
A1211 = 15
A1212 = 2.5
A1213 = 50
A1214 = A1213
A1215 = A1213
A1216 = 15
A1217 = 500
A1218 = 2.0
A1219 = 0.11
A1220 = 0.12
A1221 = 0.01
A1222 = 0.04
A1223 = 1
A1224 = 4
A1225 = 0.1
A1226 = 0.5
A1227 = -0.01
A1228 = 0
A1229 = 30
A1230 = 35
A1231 = 30
A1232 = 30
A1233 = 30
A1234 = 1
A1235 = 120
A1236 = A1235
A1237 = A1235
A1238 = 30
A1239 = 100
A1240 = 2
A1241 = 0.11
A1242 = 0.3
A1243 = -0.15
A1244 = 0.075
A1245 = -0.2
A1246 = 0.1
A1247 = 5
A1248 = 0.5
A1249 = 0.03
A1250 = 0.015
A1251 = 0.015
A1252 = 2
A1253 = 5
A1254 = 0.3
A1255 = 2
A1256 = -0.003
A1257 = 2e-05
A1258 = 15
A1259 = 30
A1260 = 15
A1261 = 15
A1262 = 20
A1263 = 2.5
A1264 = 300
A1265 = A1264
A1266 = A1264
A1267 = 100
A1268 = 60
A1269 = 0.5
A1270 = 1.0
A1271 = 1
A1272 = 0.04
A1273 = 0.04
A1274 = 4.0
A1275 = 3.0
A1276 = 0.5
A1277 = 1.0
A1278 = -0.1
A1279 = 0.0002
A1280 = 20
A1281 = 30
A1282 = 12
A1283 = 12
A1284 = 25
A1285 = 1
A1286 = 20
A1287 = A1286
A1288 = A1286
A1289 = 5
A1290 = 10
A1291 = 75
A1292 = 0.5
A1293 = 1.0
A1294 = 1
A1295 = 0.04
A1296 = 0.04
A1297 = 4.0
A1298 = 3.0
A1299 = 0.5
A1300 = 1.0
A1301 = -0.1
A1302 = 0.0002
A1303 = 20
A1304 = 30
A1305 = 12
A1306 = 12
A1307 = 25
A1308 = 1
A1309 = 45.0
A1310 = A1286
A1311 = A1286
A1312 = 5
A1313 = 12
A1314 = 20
A1315 = 1.0
A1316 = 1.0
A1317 = 1.0
A1318 = 0.05
A1319 = 0.05
A1320 = 4.0
A1321 = 3.0
A1322 = 0.5
A1323 = 1.0
A1324 = -0.25
A1325 = 0.001
A1326 = 40
A1327 = 50
A1328 = 50
A1329 = 50
A1330 = 25
A1331 = 2.5
A1332 = 14
A1333 = A1332
A1334 = A1332
A1335 = 2
A1336 = 10
A1337 = 10000
A1338 = 2.0
A1339 = 1.0
A1340 = 1.0
A1341 = 0.025
A1342 = 0.0
A1343 = -0.06
A1344 = 0.0
A1345 = 50
A1346 = 175
A1347 = 50.0
A1348 = 50.0
A1349 = 100.0
A1350 = 5
A1351 = 7
A1352 = A1351
A1353 = A1351
A1354 = 1
A1355 = 1.5
A1356 = 0.4
A1357 = 2.5
A1358 = 1.5
A1359 = 3.0
A1360 = (0.08, 0.08)
A1361 = 2.0
A1362 = 0.015
A1363 = 0.01
A1364 = 0.07
A1365 = A245
A1366 = 12
A1367 = 10000
A1368 = 3.0
A1369 = 1.0
A1370 = 1.1
A1371 = 0.025
A1372 = 0.0
A1373 = -0.03
A1374 = 0.0
A1375 = 34
A1376 = 85
A1377 = 34
A1378 = 34
A1379 = 100.0
A1380 = 3
A1381 = 15
A1382 = A1381
A1383 = A1381
A1384 = 5
A1385 = 1.2
A1386 = 0.5
A1387 = 1.5
A1388 = 1.0
A1389 = 0.01
A1390 = -0.1
A1391 = 0.0001
A1392 = 0.7
A1393 = 3
A1394 = A1393
A1395 = A1393
A1396 = 1
A1397 = 75
A1398 = 0.05
A1399 = 0.5
A1400 = 1.2
A1401 = 4.0
A1402 = 6.0
A1403 = 140
A1404 = 3
A1405 = 0.25
A1406 = 0
A1407 = 0.06
A1408 = 0.0
A1409 = 1
A1410 = 1.0
A1411 = 0.75
A1412 = 0.02
A1413 = -0.05
A1414 = 0
A1415 = 0.75
A1416 = 3
A1417 = A1416
A1418 = A1416
A1419 = 3
A1420 = 150
A1421 = 0.025
A1422 = 0.5
A1400 = 1.2
A1423 = 6.0
A1424 = 6.0
A1425 = 40
A1426 = 6
A1427 = 0.25
A1428 = 0
A1429 = 1.5
A1430 = 1.0
A1431 = 0.06
A1432 = 0.0
A1433 = 1
A1434 = 1.0
A1435 = 1
A1436 = 0.02
A1437 = 0
A1438 = 0
A1439 = 0.5
A1440 = 1
A1441 = A1416
A1442 = A1416
A1443 = 1
A1444 = 150
A1445 = 4.0
A1446 = 4.0
A1447 = 50
A1448 = 2
A1449 = 0.25
A1450 = 0
A1451 = 1.5
A1452 = 1.0
A1453 = 3.0
A1454 = 1.0
A1455 = 0.02
A1456 = 0.0
A1457 = 0
A1458 = 0.2
A1459 = 9
A1460 = 3.0
A1461 = 50
A1462 = 0.5
A1463 = 5.0
A1464 = 10
A1465 = 0
A1466 = 0.3
A1467 = 0.3
A1468 = 3.0
A1469 = 1.0
A1470 = 0.02
A1471 = 0.0
A1472 = 0
A1473 = 0.2
A1474 = 9
A1475 = 3.0
A1476 = 50
A1477 = 0.5
A1478 = 5.0
A1479 = 10
A1480 = 0
A1481 = 0.3
A1482 = 0.3
A1483 = 4.0
A1484 = 1.0
A1485 = 0.04
A1486 = -0.1
A1487 = 0.0002
A1488 = 0.2
A1489 = 3.0
A1490 = 1
A1491 = 2
A1492 = 1.0
A1493 = 20.0
A1494 = 1.5
A1495 = 0.5
A1496 = 1
A1497 = 3.0
A1498 = 50
A1499 = 5.0
A1500 = 0.1
A1501 = 0.01
A1502 = 3.5
A1503 = 95
A1504 = 10.0
A1505 = 0.2
A1506 = 0.1
A1507 = 3.0
A1508 = 20.0
A1509 = 0.5
A1510 = 40.0
A1511 = 0.06
A1512 = 0.0
A1513 = 10
A1514 = 1.0
A1515 = 4.0
A1516 = 1.0
A1517 = 0.04
A1518 = -1e-05
A1519 = 0
A1520 = 0.2
A1521 = 1.0
A1522 = 1
A1523 = 1
A1524 = 1.0
A1525 = 20.0
A1526 = 1.5
A1527 = 0.5
A1528 = 1
A1529 = 3.0
A1530 = 50
A1531 = 5.0
A1532 = 0.1
A1533 = 0.01
A1534 = 3.5
A1535 = 95
A1536 = 10.0
A1537 = 0.2
A1538 = 0.1
A1539 = 3.0
A1540 = 20.0
A1541 = 0.5
A1542 = 40.0
A1543 = 0.06
A1544 = 0.0
A1545 = 10
A1546 = 3.0
A1547 = 0.75
A1548 = 300
A1549 = 300
A1550 = 4.0
A1551 = 4.0
A1552 = 0.11
A1553 = 0.5
A1554 = 0.1
A1555 = 0.01
A1556 = 0.01
A1557 = 0.05
A1558 = 0.005
A1559 = 1
A1560 = 1
A1561 = 5
A1562 = 5
A1563 = 0.2
A1564 = 0.2
A1565 = 0.6
A1566 = 0.6
A1567 = -0.007
A1568 = -0.007
A1569 = 0
A1570 = 0
A1571 = 30
A1572 = 30
A1573 = 20
A1574 = 20
A1575 = 20
A1576 = 20
A1577 = 20
A1578 = 20
A1579 = 20
A1580 = 20
A1581 = 2
A1582 = 2
A1583 = 400
A1584 = A1583
A1585 = A1583
A1586 = 100
A1587 = 45
A1588 = 45
A1589 = 0.06
A1590 = -25.0 * A1589
A1591 = -25.0 * A1589
A1592 = 5.0
A1593 = 3.0
A1594 = 100
A1595 = 5
A1596 = 1.0
A1597 = 0.2
A1598 = 100
A1599 = 999
A1600 = 4
A1601 = 2
A1602 = 2
A1603 = 10
A1604 = 1.5
A1605 = 50.0
A1606 = 30.0
A1607 = 0.1
A1608 = 180
A1609 = 30
A1610 = 0.06
A1611 = 100
A1612 = -3.0 * A1610
A1613 = -17.0 * A1610
A1614 = -11.0 * A1610
A1615 = 10
A1616 = 3.0
A1617 = 100
A1618 = 15
A1619 = 1.0
A1620 = 0.2
A1621 = 3
A1622 = 50
A1623 = 10
A1624 = 0.3
A1625 = 0.1
A1626 = 20
A1627 = 1
A1628 = A1627
A1629 = A1627
A1630 = 1.0
A1631 = 7
A1632 = 8
A1633 = 300.0
A1634 = 7
A1635 = 0.15
A1636 = 0.1
A1637 = 5.0
A1638 = 0.06
A1639 = 1
A1640 = -0.2
A1641 = 3
A1642 = 3
A1643 = A1641
A1644 = 1.0
A1645 = 3
A1646 = 40.0
A1647 = 35.0
A1648 = 1.0
A1649 = 4
A1650 = 50
A1651 = 3
A1652 = 0.1
A1653 = 0.0
A1654 = 6.0
A1655 = 0.0
A1656 = 0.0
A1657 = 0.0
A1658 = 4
A1659 = 2
A1660 = 2
A1661 = 1.0
A1662 = 1
A1663 = 50
A1664 = 25
A1665 = 1.0
A1666 = 3
A1667 = 50
A1668 = 3
A1669 = 0.1
A1670 = 0.0
A1671 = 6.0
A1672 = 0.0
A1673 = 0.0
A1674 = 0.0
A1675 = 0.06
A1676 = 0.0
A1677 = 4
A1678 = 2
A1679 = 2
A1680 = 1.0
A1681 = 1
A1682 = 50
A1683 = 25
A1684 = 1.0
A1685 = 5
A1686 = 200
A1687 = 6
A1688 = 0.1
A1689 = 0.75
A1690 = 6.0
A1691 = 0.0
A1692 = 0.0
A1693 = 0.0
A1694 = 5.0
A1695 = 2.0
A1696 = 1.0
A1697 = 0.01
A1698 = -0.15
A1699 = 0
A1700 = 0.35
A1701 = 5
A1702 = 3
A1703 = 5
A1704 = 1
A1705 = 75
A1706 = 0.025
A1707 = 0.5
A1708 = 1.2
A1709 = 4
A1710 = 100
A1711 = 6.0
A1712 = 0.25
A1713 = 0.0
A1714 = 0.06
A1715 = 0.0
A1716 = 1
A1717 = 3.0
A1718 = 2.0
A1719 = 1.0
A1720 = 0.01
A1721 = -0.15
A1722 = 0
A1723 = 0.35
A1724 = 5
A1725 = 3
A1726 = 5
A1727 = 1
A1728 = 75
A1729 = 3.0
A1730 = 6.0
A1731 = 4
A1732 = 2.5
A1733 = 3
A1734 = -0.5
A1735 = 100
A1736 = 15
A1737 = 0.75
A1738 = 0.75
A1739 = 5.0
A1740 = 0.05
A1741 = 1
A1742 = 0.0
A1743 = True
A1744 = 1.0
A1745 = 2
A1746 = 2
A1747 = 1
A1748 = 1.0
A1749 = 8
A1750 = 300.0
A1751 = 7
A1752 = 0.15
A1753 = 0.1
A1754 = 5.0
A1755 = 0.06
A1756 = 1
A1757 = -0.2
A1758 = 2.5
A1759 = 0.3
A1760 = 3
A1761 = 10
A1762 = 0.7
A1763 = 0.4
A1764 = 4.0
A1765 = 5
A1766 = 0.5
A1767 = 2.0
A1768 = 0.3
A1769 = -1
A1770 = 1.0
A1771 = 2
A1772 = (
 255, 255, 255)
A1773 = (255, 255, 0)
A1774 = (255, 0, 0)
A1775 = 5
A1776 = 0.5
A1777 = 3
A1778 = 5
A1779 = 0.8
A1780 = 0.2
A1781 = 6.0
A1782 = 5
A1783 = 0.5
A1784 = 2.0
A1785 = 0.3
A1786 = -1
A1787 = 1.0
A1788 = 2
A1789 = (
 255, 255, 255)
A1790 = (255, 255, 0)
A1791 = (255, 0, 0)
A1792 = 5
A1793 = 3
A1794 = A1792
A1795 = 1.0
A1796 = 3.0
A1797 = 6.0
A1798 = 4
A1799 = 2.5
A1800 = 3
A1801 = -0.5
A1802 = 100
A1803 = 15
A1804 = 0.75
A1805 = 0.75
A1806 = 5.0
A1807 = 0.05
A1808 = 1
A1809 = 0.0
A1810 = True
A1811 = 4
A1812 = 2
A1813 = A1811
A1814 = 0.5
A1815 = 50.0
A1816 = 25
A1817 = 2.5
A1818 = 4
A1819 = 230.0
A1820 = 6.0
A1821 = 1.0
A1822 = 0.5
A1823 = 50
A1824 = 50
A1825 = 50
A1826 = 50
A1827 = 50
A1828 = 6.0
A1829 = 0.0
A1830 = 0.0
A1831 = 0.0
A1832 = 4
A1833 = 2
A1834 = A1832
A1835 = 0.5
A1836 = 50.0
A1837 = 25
A1838 = 2.5
A1839 = 2.0
A1840 = 6.0
A1841 = 500.0
A1842 = 0.5
A1843 = 0.5
A1844 = 0.25
A1845 = 6.0
A1846 = 0.0
A1847 = 0.0
A1848 = 0.0
A1849 = 15
A1850 = 0.03
A1851 = 3
A1852 = 0.5
A1853 = 0.5
A1854 = 0.5
A1855 = 1.75
A1856 = 85
A1857 = 0.7
A1858 = 2.0
A1859 = 100
A1860 = 1.5
A1861 = 1.0
A1862 = 0.02
A1863 = 0.0
A1864 = 0
A1865 = 0.2
A1866 = 2
A1867 = 2
A1868 = 2
A1869 = 2
A1870 = 1
A1865 = 1.0
A1871 = 25
A1872 = 3
A1873 = 0.06
A1874 = 1
A1875 = -0.5
A1876 = 3
A1877 = -0.5
A1878 = 5
A1879 = 300
A1880 = 5.0
A1881 = 1
A1882 = 2
A1883 = 50
A1884 = 0.5
A1885 = 0.06
A1886 = -80
A1887 = 0
A1888 = 0.8
A1889 = -0.1
A1890 = -0.6
A1891 = 1.9
A1892 = 1.4
A1893 = 1
A1894 = 1
A1895 = 1
A1896 = 10
A1897 = 1.5
A1898 = 0.03
A1899 = 45
A1900 = 250
A1901 = 45
A1902 = -0.55
A1903 = 180
A1904 = 3.0
A1905 = 7
A1906 = 2
A1907 = 0.1
A1908 = 0.0
A1909 = 0.5
A1910 = 6
A1911 = 1.5
A1912 = 400
A1913 = 0.9
A1914 = 0.11
A1915 = 0.5
A1916 = 0.01
A1917 = 0.01
A1918 = 0.5
A1919 = 0.5
A1920 = 0.5
A1921 = 0.7
A1922 = -0.0075
A1923 = 1e-05
A1924 = 20
A1925 = 40
A1926 = 20
A1927 = 20
A1928 = 20
A1929 = 2.5
A1930 = 60
A1931 = A1930
A1932 = A1930
A1933 = 15
A1934 = 3
A1935 = 0.1
A1936 = 175
A1937 = 2
A1938 = 0.11
A1939 = 0.15
A1940 = 0.02
A1941 = 0.02
A1942 = 2
A1943 = 4
A1944 = 0.5
A1945 = 1.4
A1946 = -0.02
A1947 = 2e-05
A1948 = 20
A1949 = 37
A1950 = 20
A1951 = 20
A1952 = 20
A1953 = 2.5
A1954 = 250
A1955 = A1954
A1956 = A1954
A1957 = 50
A1958 = 60
A1959 = 2.5
A1960 = 0.3
A1961 = 0.35
A1962 = 0.05
A1963 = 0.05
A1964 = 4.0
A1965 = 3.0
A1966 = 0.5
A1967 = 1.0
A1968 = -0.05
A1969 = 0.0005
A1970 = 20
A1971 = 25
A1972 = 10
A1973 = 10
A1974 = 20
A1975 = 2
A1976 = 40
A1977 = A1976
A1978 = A1976
A1979 = 8
A1980 = 10
A1981 = 0.03
A1982 = 0.0
A1983 = 0
A1984 = 0.2
A1985 = 9
A1986 = 3.0
A1987 = 5
A1988 = 10
A1989 = 2
A1990 = 4
A1991 = 1
A1992 = 0.5
A1993 = 4
A1994 = 3
A1995 = 0.5
A1996 = 0.035
A1997 = 0.05
A1998, A1999, A2000 = xrange(3)
A2001 = 3
A2002 = 2
A2003 = A2001
A2004 = 0.5
A2005 = 0.5
A2006 = 10.0
A2007 = 18446744073709551615
A2008 = {A482: 'ugc_health_drop', 
   A483: 'ugc_ammo_drop', 
   A484: 'ugc_block_drop', 
   A485: 'ugc_bomb_drop', 
   A486: 'ugc_spawngreen_small', 
   A489: 'ugc_spawnblue_small', 
   A492: 'ugc_basegreen_small', 
   A495: 'ugc_baseblue_small', 
   A498: 'ugc_base_small', 
   A487: 'ugc_spawngreen_med', 
   A490: 'ugc_spawnblue_med', 
   A493: 'ugc_basegreen_med', 
   A496: 'ugc_baseblue_med', 
   A499: 'ugc_base_med', 
   A488: 'ugc_spawngreen_large', 
   A491: 'ugc_spawnblue_large', 
   A494: 'ugc_basegreen_large', 
   A497: 'ugc_baseblue_large', 
   A500: 'ugc_base_large'}
A2009 = {A486: (
        -5, 5, -5, 5, -8, 2), 
   A489: (
        -5, 5, -5, 5, -8, 2), 
   A492: (
        -5, 5, -5, 5, -8, 2), 
   A495: (
        -5, 5, -5, 5, -8, 2), 
   A498: (
        -5, 5, -5, 5, -8, 2), 
   A487: (
        -12, 12, -12, 12, -21, 3), 
   A490: (
        -12, 12, -12, 12, -21, 3), 
   A493: (
        -12, 12, -12, 12, -21, 3), 
   A496: (
        -12, 12, -12, 12, -21, 3), 
   A499: (
        -12, 12, -12, 12, -21, 3), 
   A488: (
        -20, 20, -20, 20, -36, 4), 
   A491: (
        -20, 20, -20, 20, -36, 4), 
   A494: (
        -20, 20, -20, 20, -36, 4), 
   A497: (
        -20, 20, -20, 20, -36, 4), 
   A500: (
        -20, 20, -20, 20, -36, 4)}
A2010, A2011, A2012, A2013, A2014 = xrange(5)
A2015, A2016, A2017 = xrange(3)
for ugc_zone_key, ugc_zone_size in A2009.iteritems():
    A2018, A2019, A2020, A2021, A2022, A2023 = ugc_zone_size
    A2024 = A2018 + (A2019 - A2018 & ~1)
    A2025 = A2020 + (A2021 - A2020 & ~1)
    A2026 = A2022 + (A2023 - A2022 & ~1)
    if A2024 != A2019 or A2025 != A2021 or A2026 != A2023:
        print 'zone size', ugc_zone_size, 'adjusted to be of even dimensions',
        A2009[ugc_zone_key] = (A2018, A2024, A2020, A2025, A2022, A2026)
        print A2009[ugc_zone_key]

A2027 = {A486: A56, 
   A489: A55, 
   A492: A56, 
   A495: A55, 
   A498: TEAM_NEUTRAL, 
   A487: A56, 
   A490: A55, 
   A493: A56, 
   A496: A55, 
   A499: TEAM_NEUTRAL, 
   A488: A56, 
   A491: A55, 
   A494: A56, 
   A497: A55, 
   A500: TEAM_NEUTRAL}
A2028, A2029, A2030, A2031, A2032 = xrange(5)
A2033 = {A486: A2029, 
   A489: A2028, 
   A492: A2031, 
   A495: A2030, 
   A498: A2032, 
   A487: A2029, 
   A490: A2028, 
   A493: A2031, 
   A496: A2030, 
   A499: A2032, 
   A488: A2029, 
   A491: A2028, 
   A494: A2031, 
   A497: A2030, 
   A500: A2032}
A2034 = {A482: 'minimap_healthcrate', 
   A483: 'minimap_ammocrate', 
   A484: 'minimap_blockcrate', 
   A485: 'minimap_bomb'}
A2035 = 8
A2036 = {A339: [
        'UGC_HELP_PAINTBRUSH'], 
   A338: [
        'UGC_HELP_CONSTRUCTTOOL_STEP1', 'UGC_HELP_CONSTRUCTTOOL_STEP2'], 
   A340: [
        'UGC_HELP_PICKAXE'], 
   A341: [
        'UGC_HELP_SPADEDUELUSE'], 
   A342: [
        'UGC_HELP_ROCKETLAUNCHER'], 
   A301: [
        'UGC_HELP_BLOCKTOOL'], 
   A337: [
        'UGC_HELP_GAMEDATATOOL'], 
   A343: [
        'UGC_HELP_DRILLGUN'], 
   A344: [
        'UGC_HELP_BLOCKCANNON']}
A2037 = 0.3
A2038 = 3
A2039 = 5
A2040 = 50
A2041 = 10000
A2042 = 2.5
A2043 = 0.5
A2044 = 0.5
A2045 = 0.003
A2046 = -0.05
A2047 = 0.0001
A2048 = 70.0
A2049 = 150
A2050 = 35
A2051 = 35
A2052 = 25.0
A2053 = 2
A2054 = 50.0
A2055 = 30.0
A2056 = A2054
A2057 = 10.0
A2058 = 4
A2059 = 2
A2060 = A2058
A2061 = 0.5
A2062 = 35.0
A2063 = 3.0
A2064 = 2.0
A2065 = 9.0
A2066 = 130.0
A2067 = 15
A2068 = 0.1
A2069 = 0.1
A2070 = 6.0
A2071 = 0.0
A2072 = 0.0
A2073 = 0.0
A2074 = 0
A2075 = 1.0
A2076 = 3
A2077 = 0
A2078 = 1
A2079 = 0.1
A2080 = 0.05
A2081 = 10
A2082 = 75.0
A2083 = 20
A2084 = 3
A2085 = 2
A2086 = 7
A2087 = 3
A2088 = 25
A2089 = 3
A2090 = 1.0
A2091 = 0.5
A2092 = 10.0
A2093 = 7
A2092 = 7.0
A2093 = 8.0
A2092 = 10
A2093 = 7
A2094 = 500
A2095 = 20
A2096 = 3.0
A2097 = 2.0
A2098 = 10
A2099 = 15
A2100 = 15
A2101 = 30
A2102 = 6
A2103 = 400.0
A2104 = 15
A2105 = 2.0
A2106 = 1.0
A2107 = 100
A2108 = 100
A2109 = 1.0
A2110 = 100.0
A2111 = 50.0
A2112 = 1.0
A2113 = 1.0
A2114 = 5.0
A2115 = 12.0
A2116 = 4
A2117 = 3.0
A2118 = 3.0
A2119, A2120, A2121, A2122, A2123, A2124, A2125, A2126, A2127 = xrange(9)
A2128 = {A364: {A2119: 0.25, 
          A2120: 100, 
          A2121: 10, 
          A2122: 10, 
          A2123: 75, 
          A2124: 0.5, 
          A2125: 2.0, 
          A2126: 2.0, 
          A2127: 3}, 
   A365: {A2119: 0.25, 
          A2120: 100, 
          A2121: 10, 
          A2122: 9, 
          A2123: 17, 
          A2124: 0.5, 
          A2125: 2.0, 
          A2126: 2.0, 
          A2127: 0.25}, 
   A366: {A2119: 0.25, 
          A2120: 100, 
          A2121: 10, 
          A2122: 3, 
          A2123: 18, 
          A2124: 0.5, 
          A2125: 0.5, 
          A2126: 1.0, 
          A2127: 0.25}, 
   A367: {A2119: 0.1, 
          A2120: 100, 
          A2121: 0, 
          A2122: 100, 
          A2123: 0, 
          A2124: 0.5, 
          A2125: 0.1, 
          A2126: 1.0, 
          A2127: 0.25}}
A2129 = 1.0
A2130 = 2.0
A2131 = -1
A2132 = 3
A2133 = 4
A2134 = 8
A2135 = 0.0
A2136 = 0.1
A2137 = 0.02
A2138 = -1
A2139 = 1
A2140 = 2
A2141 = 5
A2142 = 0.0
A2143 = 0.1
A2144 = -1
A2145 = 2
A2146 = 3
A2147 = 5
A2148 = 25.0
A2149 = -1
A2150 = 1
A2151 = 0.5
A2152 = 1.0
A2153 = 0.05
A2154 = 0.05
A2155 = 0
A2156 = 0
A2157 = 0.45
A2158 = 0.82
A2159 = 0.37
A2160 = 0.45
A2161 = -0.05
A2162 = -0.05
A2163 = -1.2
A2164 = 0.02
A2165 = 2
A2166 = 0.01
A2167 = 5
A2168 = -1
A2169 = 2
A2170 = 0.01
A2171 = 2
A2172 = 0.01
A2173 = 2
A2174 = -1
A2175 = 160
A2176 = 200
A2177 = 2
A2178 = 4
A2179 = 0.7
A2180 = 0.0
A2181 = 0.05
A2182 = 3
A2183 = 6
A2184 = 160
A2185 = 200
A2186 = 2.5
A2187 = 1
A2188 = 1
A2189 = -1
A2190 = 0.7
A2191 = 0.0
A2192 = 0.05
A2193 = 0.2
A2194 = 0.5
A2195 = 160
A2196 = 200
A2197 = 0.5
A2198 = 1
A2199 = 1
A2200 = -1
A2201 = A2182
A2202 = A2183
A2203 = A2184
A2204 = A2185
A2205 = 1.0
A2206 = 100.0
A2207 = 0.5
A2208 = 2.0
A2209 = 0.5
A2210 = 0.5
A2211 = -2.4
A2212 = 512
A2213 = 512
A2214 = 240
A2215 = A2214 - 2
A2216 = 9
A2217 = 18
A2218 = 511
A2219 = 261632
A2220 = 133955584
A2221 = (
 (
  80, 96, 80, 0), (96, 88, 72, int(0.58 * A2214)), (112, 80, 64, int(0.94 * A2214)), (128, 72, 56, int(0.66 * A2214)), (112, 64, 58, int(0.78 * A2214)), (96, 56, 40, int(0.86 * A2214)), (80, 48, 32, int(0.94 * A2214)), (64, 40, 24, A2214 - 2), (5, 85, 156, A2214 - 1))
A2222 = (59, 58, 55, A2214 - 2)
A2223, A2224, A2225, A2226, A2227 = xrange(5)
A2228, A2229, A2230, A2231, A2232 = xrange(5)
A2233, A2234, A2235, A2236, A2237 = xrange(5)
A2238 = [
 A321, A322, A319, A324, A318, A326, A337, A338]
A2239 = [A319, A324, A318, A337, A338]
A2240, A2241, A2242, A2243, A2244, A2245, A2246, A2247, A2248 = xrange(9)
A2249, A2250, A2251, A2252 = xrange(4)
A2253 = {0: {A2249: 1.0, A2250: 1.2, 
       A2251: 7.0, 
       A2252: 12.0}, 
   10: {A2249: 1.0, A2250: 1.2, 
        A2251: 7.0, 
        A2252: 999999.0}, 
   20: {A2249: 1.0, A2250: 1.15, 
        A2251: 7.0, 
        A2252: 999999.0}, 
   70: {A2249: 1.0, A2250: 1.1, 
        A2251: 7.0, 
        A2252: 999999.0}, 
   120: {A2249: 1.0, A2250: 1.05, 
         A2251: 7.0, 
         A2252: 999999.0}, 
   1000: {A2249: 1.0, A2250: 1.0, 
          A2251: 7.0, 
          A2252: 999999.0}}
A2254 = 10
A2255 = -0.8
A2256 = 20.0
A2257 = 5.0
A2258 = 10
A2259 = 5
A2260 = 5.0
A2261 = 5.0
A2262 = 3.0
A2263 = False
A2264 = 100.0 / 1000.0 / 2.0
A2265 = False
A2266 = False
A2267, A2268 = xrange(2)
A2269 = 31
A2270 = 20
A2271 = 7
A2272 = 10
A2273 = 255
A2274 = True
A2275 = False
A2276 = False
A2277 = False
A2278 = 5
A2279 = 15
A2280 = 8000
A2281 = (
 0.1, 0.5, 1.0)
A2282, A2283, A2284 = xrange(3)
A2285 = {A2282: 90, 
   A2283: 128, 
   A2284: 192}
A2286 = 150
A2287 = 0.5
A2288 = 0.3
A2289 = 0.0
A2290 = -0.1
A2291 = 0.1
A2292 = 2
A2293 = 0.5
A2294 = 0.5
A2295 = 3
A2296 = 1.75
A2297 = 0.15
A2298 = False
A2299 = 1.0
A2300 = 0.0
A2301 = 0.5
A2302 = 1.0
A2303 = 0.5
A2304 = 3.0
A2305 = 10
A2306 = 8
A2307, A2308 = xrange(2)
A2309, A2310, A2311, A2312, A2313, A2314, A2315, A2316 = xrange(8)
A2317 = 1
A2318 = 2
A2319 = 3
A2320 = 30.0
A2321 = 20.0
A2322 = 3
A2323, A2324, A2325, A2326 = xrange(4)
A2327 = 25
A2328 = 0.05
A2329 = 0.05
A2330 = 4
A2331 = 0
A2332 = 180
A2333 = 1
A2334 = 2
A2335 = 0
A2336 = 4
A2337 = 4
A2338 = 0
A2339 = 30
A2340 = False
A2341 = False
A2342 = A2325
A2343 = 50
A2344 = 0.08
A2345 = 0.07
A2346 = 5
A2347 = 0
A2348 = 180
A2349 = 1
A2350 = 2
A2351 = 0
A2352 = 4
A2353 = 4
A2354 = 0
A2355 = 30
A2356 = False
A2357 = False
A2358 = A2325
A2359, A2360 = xrange(2)
A2361, A2362 = xrange(2)
A2363, A2364 = xrange(2)
A2365, A2366 = xrange(2)
A2367, A2368 = xrange(2)
A2369, A2370 = xrange(2)
A2371 = 4
A2372 = [
 A924,
 A915]
A2373 = 2
A2374 = 10.0
A2375 = 3
A2376 = 0.25
A2377 = 20.0
A2378 = 5.0
A2379 = 1.5
A2380 = 5.0
A2381 = [
 A421, A422, A423, A424, A425, A426, 
 A427, A442, A443, A444, A445]
A2382 = [
 A421, A422, A423, A424, A425, A426, 
 A427, A442, A443, A444, A445, 
 A439, 
 A434, A435, A436, A437, A438, A440]
A2383 = 80.0
A2384 = True
A2385 = 5 * 60
A2386 = 45
A2387 = 1 << 0
A2388 = 1 << 1
A2389 = 1 << 2
A2390 = 1 << 3
A2391 = 1 << 4
A2392 = 5
A2393 = A2387 | A2388 | A2389 | A2390
import sys
if 'blitzdev' in sys.argv and 'enzymebeta' in sys.argv:
    A2()
A2394 = 1.0
A2395 = 0.92
A2396 = 0.2
A2397 = A1004
A2398 = A1004 * 4
A2399 = {A74: (
       A527, A528), 
   A75: (
       A529, A530), 
   A76: (
       A531, A532), 
   A86: (
       A533, A534), 
   A77: (
       A535, A536), 
   A78: (
       A537, A538), 
   A79: (
       A539, A540), 
   A80: (
       A541, A542), 
   A81: (
       A541, A542), 
   A82: (
       A541, A542), 
   A83: (
       A541, A542), 
   A84: (
       A541, A542), 
   A85: (
       A541, A542), 
   A87: (
       A543, A544), 
   A88: (
       A545, A546), 
   A89: (
       A547, A548), 
   A90: (
       A549, A550), 
   A91: (
       A551, A552)}
A2400 = {A74: A102, 
   A75: A103, 
   A76: A104, 
   A86: A105, 
   A77: A106, 
   A78: A107, 
   A79: A108, 
   A80: A109, 
   A81: A109, 
   A82: A109, 
   A83: A109, 
   A84: A109, 
   A85: A109, 
   A87: A110, 
   A88: A111, 
   A89: A112, 
   A90: A113, 
   A91: A114}
A2401 = {A74: A115, 
   A75: A116, 
   A76: A117, 
   A86: A118, 
   A77: A119, 
   A78: A120, 
   A79: A121, 
   A80: A122, 
   A81: A122, 
   A82: A122, 
   A83: A122, 
   A84: A122, 
   A85: A122, 
   A87: A123, 
   A88: A124, 
   A89: A125, 
   A90: A126, 
   A91: A127}
A2402 = {A74: A128, 
   A75: A129, 
   A76: A130, 
   A86: A131, 
   A77: A132, 
   A78: A133, 
   A79: A134, 
   A80: A135, 
   A81: A135, 
   A82: A135, 
   A83: A135, 
   A84: A135, 
   A85: A135, 
   A87: A136, 
   A88: A137, 
   A89: A138, 
   A90: A139, 
   A91: A140}
A2403 = {A74: A141, 
   A75: A142, 
   A76: A143, 
   A86: A144, 
   A77: A145, 
   A78: A146, 
   A79: A147, 
   A80: A148, 
   A81: A148, 
   A82: A148, 
   A83: A148, 
   A84: A148, 
   A85: A148, 
   A87: A149, 
   A88: A150, 
   A89: A151, 
   A90: A152, 
   A91: A153}
A2404 = {A74: A154, 
   A75: A155, 
   A76: A156, 
   A86: A157, 
   A77: A158, 
   A78: A159, 
   A79: A160, 
   A80: A161, 
   A81: A161, 
   A82: A161, 
   A83: A161, 
   A84: A161, 
   A85: A161, 
   A87: A162, 
   A88: A163, 
   A89: A164, 
   A90: A165, 
   A91: A166}
A2405 = {A74: A167, 
   A75: A168, 
   A76: A169, 
   A86: A170, 
   A77: A171, 
   A78: A172, 
   A79: A173, 
   A80: A174, 
   A81: A174, 
   A82: A174, 
   A83: A174, 
   A84: A174, 
   A85: A174, 
   A87: A175, 
   A88: A176, 
   A89: A177, 
   A90: A178, 
   A91: A179}
A2406 = {A74: A180, 
   A75: A181, 
   A76: A182, 
   A86: A183, 
   A77: A184, 
   A78: A185, 
   A79: A186, 
   A80: A187, 
   A81: A187, 
   A82: A187, 
   A83: A187, 
   A84: A187, 
   A85: A187, 
   A87: A188, 
   A88: A189, 
   A89: A190, 
   A90: A191, 
   A91: A192}
A2407 = {A74: True, 
   A75: True, 
   A76: True, 
   A86: True, 
   A77: True, 
   A78: True, 
   A79: False, 
   A80: True, 
   A81: True, 
   A82: True, 
   A83: True, 
   A84: True, 
   A85: True, 
   A87: True, 
   A88: True, 
   A89: False, 
   A90: True, 
   A91: True}
A2408 = {A74: A193, 
   A75: A194, 
   A76: A195, 
   A86: A196, 
   A77: A197, 
   A78: A198, 
   A79: A199, 
   A80: A200, 
   A81: A200, 
   A82: A200, 
   A83: A200, 
   A84: A200, 
   A85: A200, 
   A87: A201, 
   A88: A202, 
   A89: A203, 
   A90: A204, 
   A91: A205}
A2409 = {A74: A206, 
   A75: A207, 
   A76: A208, 
   A86: A209, 
   A77: A210, 
   A78: A211, 
   A79: A212, 
   A80: A213, 
   A81: A213, 
   A82: A213, 
   A83: A213, 
   A84: A213, 
   A85: A213, 
   A87: A214, 
   A88: A215, 
   A89: A216, 
   A90: A217, 
   A91: A218}
A2410 = {A74: A219, 
   A75: A220, 
   A76: A221, 
   A86: A222, 
   A77: A223, 
   A78: A224, 
   A79: A225, 
   A80: A226, 
   A81: A226, 
   A82: A226, 
   A83: A226, 
   A84: A226, 
   A85: A226, 
   A87: A227, 
   A88: A228, 
   A89: A229, 
   A90: A230, 
   A91: A231}
A2411 = {A74: A232, 
   A75: A233, 
   A76: A234, 
   A86: A235, 
   A77: A236, 
   A78: A237, 
   A79: A238, 
   A80: A239, 
   A81: A239, 
   A82: A239, 
   A83: A239, 
   A84: A239, 
   A85: A239, 
   A87: A240, 
   A88: A241, 
   A89: A242, 
   A90: A243, 
   A91: A244}
A2412 = {A74: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'sol_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'sol_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'sol_jump_vo_001-008', -1, A2790], 
         A2738: [
               'sol_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'sol_land_vo_001-008', -1, A2792], 
         A2740: [
               'sol_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'sol_water_land_vo_001-008', -1, A2794]}, 
   A75: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'sco_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'sco_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'sco_jump_vo_001-008', -1, A2790], 
         A2738: [
               'sco_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'sco_land_vo_001-008', -1, A2792], 
         A2740: [
               'sco_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'sco_water_land_vo_001-008', -1, A2794]}, 
   A76: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'roc_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'roc_spawn_vo_001-005', -1, A2789], 
         A2737: [
               'roc_jump_vo_001-008', -1, A2790], 
         A2738: [
               'roc_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'roc_land_vo_001-008', -1, A2792], 
         A2740: [
               'roc_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'roc_water_land_vo_001-008', -1, A2794]}, 
   A86: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'eng_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'eng_spawn_vo_001-005', -1, A2789], 
         A2737: [
               'eng_jump_vo_001-008', -1, A2790], 
         A2738: [
               'eng_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'eng_land_vo_001-008', -1, A2792], 
         A2740: [
               'eng_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'eng_water_land_vo_001-008', -1, A2794]}, 
   A77: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'min_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'min_spawn_vo_001-004', -1, A2789], 
         A2737: [
               'min_jump_vo_001-008', -1, A2790], 
         A2738: [
               'min_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'min_land_vo_001-008', -1, A2792], 
         A2740: [
               'min_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'min_water_land_vo_001-008', -1, A2794]}, 
   A78: {A2726: A2750, A2727: A2751, 
         A2728: A2744, 
         A2729: A2752, 
         A2730: A2753, 
         A2731: 'zombie_fallhurt', 
         A2732: A2755, 
         A2733: A2754, 
         A2734: [
               'vo_zombiedeath_001-010', -1, 100], 
         A2735: (
               [
                'vo_zombiegroan_001-016', -1, 100], 3.0, 6.0), 
         A2736: A2788, 
         A2737: A2788, 
         A2738: A2788, 
         A2739: A2788, 
         A2740: A2788, 
         A2741: A2788}, 
   A79: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'classic_death_vo', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: A2788, 
         A2737: A2788, 
         A2738: A2788, 
         A2739: A2788, 
         A2740: A2788, 
         A2741: [
               'classic_fallhurt_vo', -1, A2794]}, 
   A80: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'gang_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'gang_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'gang_jump_vo_001-008', -1, A2790], 
         A2738: [
               'gang_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'gang_land_vo_001-008', -1, A2792], 
         A2740: [
               'gang_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'gang_water_land_vo_001-008', -1, A2794]}, 
   A81: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'gang_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'gang_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'gang_jump_vo_001-008', -1, A2790], 
         A2738: [
               'gang_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'gang_land_vo_001-008', -1, A2792], 
         A2740: [
               'gang_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'gang_water_land_vo_001-008', -1, A2794]}, 
   A82: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'gang_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'gang_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'gang_jump_vo_001-008', -1, A2790], 
         A2738: [
               'gang_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'gang_land_vo_001-008', -1, A2792], 
         A2740: [
               'gang_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'gang_water_land_vo_001-008', -1, A2794]}, 
   A83: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'gang_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'gang_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'gang_jump_vo_001-008', -1, A2790], 
         A2738: [
               'gang_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'gang_land_vo_001-008', -1, A2792], 
         A2740: [
               'gang_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'gang_water_land_vo_001-008', -1, A2794]}, 
   A84: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'gang_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'gang_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'gang_jump_vo_001-008', -1, A2790], 
         A2738: [
               'gang_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'gang_land_vo_001-008', -1, A2792], 
         A2740: [
               'gang_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'gang_water_land_vo_001-008', -1, A2794]}, 
   A85: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'gang_death_vo_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'gang_spawn_vo_001-006', -1, A2789], 
         A2737: [
               'gang_jump_vo_001-008', -1, A2790], 
         A2738: [
               'gang_water_jump_vo_001-008', -1, A2791], 
         A2739: [
               'gang_land_vo_001-008', -1, A2792], 
         A2740: [
               'gang_water_land_vo_001-008', -1, A2793], 
         A2741: [
               'gang_water_land_vo_001-008', -1, A2794]}, 
   A87: {A2726: A2742, A2727: A2743, 
         A2728: A2788, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: A2788, 
         A2735: (
               A2788, 0, 0), 
         A2736: A2788, 
         A2737: A2788, 
         A2738: A2788, 
         A2739: A2788, 
         A2740: A2788, 
         A2741: A2788}, 
   A88: {A2726: A2750, A2727: A2751, 
         A2728: A2744, 
         A2729: A2752, 
         A2730: A2753, 
         A2731: 'zombie_fallhurt', 
         A2732: A2755, 
         A2733: A2754, 
         A2734: [
               'vo_zombiedeath_001-010', -1, 100], 
         A2735: (
               [
                'vo_zombiegroan_001-016', -1, 100], 3.0, 6.0), 
         A2736: A2788, 
         A2737: A2788, 
         A2738: A2788, 
         A2739: A2788, 
         A2740: A2788, 
         A2741: A2788}, 
   A89: {A2726: A2750, A2727: A2751, 
         A2728: A2744, 
         A2729: A2752, 
         A2730: A2753, 
         A2731: 'zombie_fallhurt', 
         A2732: A2755, 
         A2733: A2754, 
         A2734: [
               'vo_zombiedeath_001-010', -1, 100], 
         A2735: (
               [
                'vo_zombiegroan_001-016', -1, 100], 3.0, 6.0), 
         A2736: A2788, 
         A2737: A2788, 
         A2738: A2788, 
         A2739: A2788, 
         A2740: A2788, 
         A2741: A2788}, 
   A90: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'AoS_vox_SPECIALIST_emote_death_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'AoS_vox_SPECIALIST_spawn_001-005', -1, A2789], 
         A2737: [
               'AoS_vox_SPECIALIST_emote_jump_001-008', -1, A2790], 
         A2738: [
               'AoS_vox_SPECIALIST_emote_jump_001-008', -1, A2791], 
         A2739: [
               'AoS_vox_SPECIALIST_emote_land_001-008', -1, A2792], 
         A2740: [
               'AoS_vox_SPECIALIST_emote_land_001-008', -1, A2793], 
         A2741: [
               'AoS_vox_SPECIALIST_emote_impact_fallen_001-008', -1, A2794]}, 
   A91: {A2726: A2742, A2727: A2743, 
         A2728: A2744, 
         A2729: A2745, 
         A2730: A2746, 
         A2731: A2747, 
         A2732: A2748, 
         A2733: A2749, 
         A2734: [
               'AoS_vox_MEDIC_emote_death_001-008', -1, 100], 
         A2735: (
               A2788, 0, 0), 
         A2736: [
               'AoS_vox_MEDIC_spawn_001-005', -1, A2789], 
         A2737: [
               'AoS_vox_MEDIC_emote_jump_001-008', -1, A2790], 
         A2738: [
               'AoS_vox_MEDIC_emote_jump_001-008', -1, A2791], 
         A2739: [
               'AoS_vox_MEDIC_emote_land_001-008', -1, A2792], 
         A2740: [
               'AoS_vox_MEDIC_emote_land_001-008', -1, A2793], 
         A2741: [
               'AoS_vox_MEDIC_emote_impact_fallen_001-008', -1, A2794]}}
A2413 = {'Alcatraz.txt': (77, 68, 66), 'ArcticBase.txt': (
                    114, 174, 175), 
   'Atlantis.txt': (
                  61, 100, 214), 
   'BranCastle.txt': (
                    30, 30, 30), 
   'Chicago.txt': (
                 0, 0, 0), 
   'Classic.txt': (
                 30, 30, 30), 
   'Classic_B.txt': (
                   111, 215, 223), 
   'Colosseum.txt': (
                   162, 110, 64), 
   'Egypt.txt': (
               195, 116, 77), 
   'Frontier.txt': (
                  163, 111, 65), 
   'GreatWall.txt': (
                   163, 153, 138), 
   'Invasion.txt': (
                  61, 61, 53), 
   'London.txt': (
                33, 32, 27), 
   'LunarBase.txt': (
                   62, 59, 57), 
   'MayanJungle.txt': (
                     69, 76, 39), 
   'SecretBase.txt': (
                    69, 92, 100), 
   'SecretBase_Night.txt': (
                          0, 0, 0), 
   'Tokyo.txt': (
               0, 0, 0), 
   'User_Desert.txt': (
                     195, 116, 77), 
   'User_Grassland.txt': (
                        111, 215, 223), 
   'User_Lunar.txt': (
                    62, 59, 57), 
   'User_Mountain.txt': (
                       50, 59, 61), 
   'User_Temple.txt': (
                     61, 61, 53), 
   'User_Urban.txt': (
                    128, 128, 127), 
   'WW1.txt': (
             168, 134, 109), 
   'WW2.txt': (
             168, 134, 109), 
   'WW2_DockLands.txt': (
                       168, 134, 109)}
A2414 = 30.0
A2415 = 60.0
A2416 = 20.0
A2417 = 30.0
A2418 = {A1010: [
         A1032], 
   A1011: [
         A1033]}
A2419 = -90
A2420 = 70
A2421 = 9999999
A2422 = 9
A2423 = False
A2424 = True
A2425 = 3
A2426 = 5
A2427 = 0.001
from constants_gamemode import *
from constants_shop import *
A0 = 224540
A1 = 200
A2428 = (48, 68, 38)
A2429 = 4.0
A2430 = 4.0
A2431 = 0.15
A2432 = (
 255, 255, 255)
A2433 = (20, 255, 50)
A2434 = (0, 255, 0)
# okay decompiling out\shared.constants.pyc
