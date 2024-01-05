# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.model_tex_vert
model_tex_vert = '\n#version 110\n\n#define DETAIL_LEVEL 3\n\n// #define CELSHADING\n// #define FACE_NORMAL\n #define KV6_NORMAL\n\nuniform vec4 blend_color;\n\n#if DETAIL_LEVEL > 0\nattribute vec3 face_normal;\nvarying vec3 normal;\nvarying vec3 worldPos;\n\n#endif\n\nvarying vec2 tex_coord;\n\nfloat FogEyeRadial(vec4 Rh)\n{\n    vec4 Re = Rh / Rh.w;\n    return length(Re);\n}\n\nvoid main() \n{\n\n#if DETAIL_LEVEL > 0\n\n#ifdef KV6_NORMAL\n    normal = (gl_NormalMatrix * gl_Normal);\n#endif\n\n#ifdef FACE_NORMAL\n    normal = (gl_NormalMatrix * face_normal);\n#endif\n\n#endif\n\n    vec4 color = gl_Color;\n\n    gl_FrontColor = color * blend_color;\n    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;\n    gl_FogFragCoord = FogEyeRadial(gl_ModelViewMatrix * gl_Vertex);\n\n#if DETAIL_LEVEL > 0\n\n    worldPos = gl_Position.xyz;\n\n#endif\n\n    tex_coord = gl_MultiTexCoord0.xy;\n\n\n    \n}\n'
# okay decompiling out\aoslib.shader_source.model_tex_vert.pyc
