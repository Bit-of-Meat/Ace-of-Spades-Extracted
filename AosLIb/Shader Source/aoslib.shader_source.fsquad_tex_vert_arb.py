# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.fsquad_tex_vert_arb
fsquad_tex_vert_arb = '!!ARBvp1.0\n# cgc version 3.1.0013, build date Apr 18 2012\n# command line args: -oglsl -profile arbvp1\n# source file: ./shader_temp/fsquad_tex_vert\n#vendor NVIDIA Corporation\n#version 3.1.0.13\n#profile arbvp1\n#program main\n#var float4 gl_Position : $vout.POSITION : HPOS : -1 : 1\n#var float4 gl_Vertex : $vin.POSITION : POSITION : -1 : 1\n#var float4 gl_FrontColor : $vout.COLOR0 : COL0 : -1 : 1\n#var float4 gl_Color : $vin.COLOR0 : COLOR0 : -1 : 1\n#var float2 texCoord : $vout.TEX0 : TEX0 : -1 : 1\n#const c[0] = -1 1 2\nPARAM c[1] = { { -1, 1, 2 } };\nMOV result.color, vertex.color;\nMOV result.position.zw, c[0].xyxy;\nMAD result.position.xy, vertex.position, c[0].z, -c[0].y;\nMOV result.texcoord[0].xy, vertex.position;\nEND\n# 4 instructions, 0 R-regs\n'
# okay decompiling out\aoslib.shader_source.fsquad_tex_vert_arb.pyc
