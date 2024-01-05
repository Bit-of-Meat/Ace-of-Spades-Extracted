# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.sea_frag_arb
sea_frag_arb = '!!ARBfp1.0\n# cgc version 3.1.0013, build date Apr 18 2012\n# command line args: -oglsl -profile arbfp1\n# source file: ./shader_temp/sea_frag\n#vendor NVIDIA Corporation\n#version 3.1.0.13\n#profile arbfp1\n#program main\n#semantic aotexture\n#var float4 gl_Color : $vin.COLOR0 : COL0 : -1 : 1\n#var float4 gl_FragColor : $vout.COLOR : COL : -1 : 1\n#var float3 normal :  :  : -1 : 0\n#var float4 posView :  :  : -1 : 0\n#var float2 noiseTexCoord :  :  : -1 : 0\n#var float2 aoTexCoord :  :  : -1 : 0\n#var sampler2D aotexture :  :  : -1 : 0\n#const c[0] = 1\nPARAM c[1] = { { 1 } };\nMOV result.color.xyz, fragment.color.primary;\nMOV result.color.w, c[0].x;\nEND\n# 2 instructions, 0 R-regs\n'
# okay decompiling out\aoslib.shader_source.sea_frag_arb.pyc
