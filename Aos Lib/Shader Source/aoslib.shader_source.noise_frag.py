# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.noise_frag
noise_frag = '\n#version 110\n\nuniform sampler2D texture;\nuniform float random_value;\nuniform float alpha;\nvarying vec2 vertex_position;\nconst float size = 5.0;\n\nfloat rnd(vec2 n)\n{\n  return 0.5 + 0.5 * \n     fract(sin(dot(n.xy, vec2(12.9898, 78.233)))* 43758.5453);\n}\n\nvoid main()\n{\n    // cool\n    vec4 input_color = gl_Color;\n    vec2 posd = vertex_position / size;\n    posd = vec2(float(int(posd.x)), float(int(posd.y)));\n    vec2 pos = posd * size;\n    pos.y *= 2.0;\n    vec2 x = pos + random_value;\n    float value = rnd(x);\n    input_color.rgb = mix(input_color.rgb, vec3(value, value, value), alpha);\n    gl_FragColor = input_color;\n}\n'
# okay decompiling out\aoslib.shader_source.noise_frag.pyc
