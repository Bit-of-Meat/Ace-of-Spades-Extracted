# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.skydome_vert
skydome_vert = '\n#version 110\n\nvarying vec2 tex_coord;\n\nuniform float time;\nuniform vec2 uv_speed;\n\nvoid main()\n{\n    gl_Position = gl_ModelViewProjectionMatrix * vec4(gl_Vertex.xyz, 1.0);\n    gl_FrontColor = gl_Color;\n\n    tex_coord = gl_MultiTexCoord0.xy;\n\n    //tex_coord += (time * 0.1);\n    tex_coord.x += (time * uv_speed.x);\n    tex_coord.y += (time * uv_speed.y);\n}\n'
# okay decompiling out\aoslib.shader_source.skydome_vert.pyc
