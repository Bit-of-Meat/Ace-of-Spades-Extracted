# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.billboard_frag
billboard_frag = '\n#version 110\n\nvarying float diffuse_value;\n\n#define saturate(x) clamp(x, 0.0, 1.0)\n\nvoid main() {\n    vec4 color = gl_Color;\n    color.rgb = mix(gl_Fog.color.rgb, color.rgb, \n        saturate((gl_Fog.end - gl_FogFragCoord) * gl_Fog.scale));\n    gl_FragColor = color;\n}\n'
# okay decompiling out\aoslib.shader_source.billboard_frag.pyc
