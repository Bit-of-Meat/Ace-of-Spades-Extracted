# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.fsquad_tex_frag_arb
fsquad_tex_frag_arb = '!!ARBfp1.0\n# cgc version 3.1.0013, build date Apr 18 2012\n# command line args: -oglsl -profile arbfp1\n# source file: ./shader_temp/fsquad_tex_frag\n#vendor NVIDIA Corporation\n#version 3.1.0.13\n#profile arbfp1\n#program main\n#semantic texture\n#var float4 gl_FragColor : $vout.COLOR : COL : -1 : 1\n#var float4 gl_Color : $vin.COLOR0 : COL0 : -1 : 1\n#var float2 texCoord : $vin.TEX0 : TEX0 : -1 : 1\n#var sampler2D texture :  : texunit 0 : -1 : 1\nTEMP R0;\nTEX R0, fragment.texcoord[0], texture[0], 2D;\nMUL result.color, R0, fragment.color.primary;\nEND\n# 2 instructions, 1 R-regs\n'
# okay decompiling out\aoslib.shader_source.fsquad_tex_frag_arb.pyc
