# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.billboard_vert
billboard_vert = '\n#version 110\n\nuniform float scale;\nuniform float rotate;\n\nfloat FogEyeRadial(vec4 Rh)\n{\n    vec4 Re = Rh / Rh.w;\n    return length(Re);\n}\n\nvoid main() {\n    gl_FrontColor = gl_Color;\n    vec3 right_vec = vec3(gl_ModelViewMatrix[0][0], gl_ModelViewMatrix[1][0],\n                          gl_ModelViewMatrix[2][0]);\n    vec3 up_vec = vec3(gl_ModelViewMatrix[0][1], gl_ModelViewMatrix[1][1],\n                       gl_ModelViewMatrix[2][1]);\n    vec2 texCoord = gl_MultiTexCoord0.xy;\n    float pos_x = ((texCoord.x - 0.5) * 2.0) * scale;\n    float pos_y = ((texCoord.y - 0.5) * 2.0) * scale;\n    float co = cos(radians(rotate));\n    float si = sin(radians(rotate));\n    float new_x = pos_x * co - pos_y * si;\n    float new_y = pos_x * si + pos_y * co;\n    vec4 corner = vec4(gl_Vertex.xyz + (new_x * right_vec) + (new_y * up_vec),\n                       gl_Vertex.w);\n    gl_Position = gl_ModelViewProjectionMatrix * corner;\n    gl_FogFragCoord = FogEyeRadial(gl_ModelViewMatrix * gl_Vertex);\n}\n'
# okay decompiling out\aoslib.shader_source.billboard_vert.pyc