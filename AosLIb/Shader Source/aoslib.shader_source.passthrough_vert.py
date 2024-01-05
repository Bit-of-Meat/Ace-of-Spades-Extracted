# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.passthrough_vert
passthrough_vert = '\n#version 110\n\nfloat FogEyeRadial(vec4 Rh)\n{\n    vec4 Re = Rh / Rh.w;\n    return length(Re);\n}\n\nvoid main() \n{\n    gl_FrontColor = gl_Color;\n    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;\n\n    gl_FogFragCoord = FogEyeRadial(gl_ModelViewMatrix * gl_Vertex);\n}\n'
# okay decompiling out\aoslib.shader_source.passthrough_vert.pyc
