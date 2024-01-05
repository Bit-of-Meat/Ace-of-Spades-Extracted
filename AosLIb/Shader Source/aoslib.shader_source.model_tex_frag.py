# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.shader_source.model_tex_frag
model_tex_frag = '\n#version 110\n\n#define DETAIL_LEVEL 3\n\n#define saturate(x) clamp(x, 0.0, 1.0)\n\n#if DETAIL_LEVEL > 0\n\nvarying vec3 normal;\nvarying vec3 worldPos;\n\n#endif\n\nuniform sampler2D model_texture;\nvarying vec2 tex_coord;\n\nvoid main() \n{\n    vec4 tex_col = texture2D(model_texture, tex_coord);\n    vec4 color = gl_Color * tex_col;\n\n#if DETAIL_LEVEL > 0\n    // find our diffuse contribution\n    vec3 L = normalize(gl_LightSource[0].position.xyz);\n    vec3 N = normalize(normal);\n\n    // bring the -1 -> 1 range into 0 - 1\n    float fresnel = (0.5 + 0.5*dot(N, L)) * 0.5 + 0.5;\n\n    color.rgb *= (fresnel * gl_LightSource[0].diffuse.rgb);\n\n    // now find our specular contribution\n    vec3 H = normalize(gl_LightSource[0].halfVector.xyz);\n\n    float specular = max(0.0, dot(N, H));\n\n    // 0.2 & 5 would be used with the material properties for the surface\n    vec3 specularResult = (pow(specular,5.0) * gl_LightSource[0].specular.rgb * 0.2);\n    color.rgb += specularResult;\n#endif\n\n    // do the final colouring with the fog\n    color.rgb = mix(gl_Fog.color.rgb, color.rgb, saturate((gl_Fog.end - gl_FogFragCoord) * gl_Fog.scale));\n\n    gl_FragColor = vec4(color.rgb, color.a);\n}\n'
# okay decompiling out\aoslib.shader_source.model_tex_frag.pyc
