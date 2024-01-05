# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.greyscale_frag
greyscale_frag = '\n#version 110\n\nvarying vec2 texture_coordinate;\nuniform sampler2D Tex0;\nuniform float coefficient;\n\nvoid main()\n{\n        vec4 col = texture2D(Tex0, texture_coordinate);\n        vec4 new_col = vec4(col);\n        new_col.rgb *= vec3(0.299, 0.587, 0.114);\n        new_col.rgb = vec3(new_col.r+new_col.g+new_col.b);\n        col = mix(col, new_col, coefficient);\n        gl_FragColor = col * gl_Color;\n}\n'
# okay decompiling out\aoslib.shader_source.greyscale_frag.pyc
