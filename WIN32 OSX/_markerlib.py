# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\_markerlib
try:
    import ast
    from _markerlib.markers import default_environment, compile, interpret
except ImportError:
    if 'ast' in globals():
        raise

    def default_environment():
        return {}


    def compile(marker):

        def marker_fn(environment=None, override=None):
            return not marker.strip()

        marker_fn.__doc__ = marker
        return marker_fn


    def interpret(marker, environment=None, override=None):
        return compile(marker)()
# okay decompiling out\_markerlib.pyc
