# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.passthrough_frag
passthrough_frag = '\n#version 110\n\n#define saturate(x) clamp(x, 0.0, 1.0)\n\nvoid main() \n{\n    vec4 color = gl_Color;\n\n    // do the final colouring with the fog\n    color.rgb = mix(gl_Fog.color.rgb, color.rgb, saturate((gl_Fog.end - gl_FogFragCoord) * gl_Fog.scale));\n\n    gl_FragColor = vec4(color.rgb, color.a);\n}\n'
# okay decompiling out\aoslib.shader_source.passthrough_frag.pyc
