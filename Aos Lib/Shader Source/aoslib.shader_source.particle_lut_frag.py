# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.particle_lut_frag
particle_lut_frag = '\n#version 110\n\nuniform sampler2D particle_tex;\nuniform sampler2D particle_lut;\n\nvarying float time;\n\nvarying vec2 tex_coord;\n\nvoid main()\n{\n    vec4 tex_col = texture2D(particle_tex, tex_coord);\n\n    vec2 lut_tex_coord = vec2(tex_col.x, 0.0);\n    lut_tex_coord.y += time;\n\n    vec4 tex_lut = texture2D(particle_lut, lut_tex_coord);\n\n    gl_FragColor = vec4(tex_lut.rgb, tex_col.a * tex_lut.a);\n}\n'
# okay decompiling out\aoslib.shader_source.particle_lut_frag.pyc
