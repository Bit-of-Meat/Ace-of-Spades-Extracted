# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.resource
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import os, weakref, sys, zipfile, StringIO, pyglet

class ResourceNotFoundException(Exception):

    def __init__(self, name):
        message = 'Resource "%s" was not found on the path.  Ensure that the filename has the correct captialisation.' % name
        Exception.__init__(self, message)


def get_script_home():
    frozen = getattr(sys, 'frozen', None)
    if frozen in ('windows_exe', 'console_exe'):
        return os.path.dirname(sys.executable)
    else:
        if frozen == 'macosx_app':
            return os.environ['RESOURCEPATH']
        main = sys.modules['__main__']
        if hasattr(main, '__file__'):
            return os.path.dirname(main.__file__)
        return ''


def get_settings_path(name):
    if sys.platform in ('cygwin', 'win32'):
        if 'APPDATA' in os.environ:
            return os.path.join(os.environ['APPDATA'], name)
        else:
            return os.path.expanduser('~/%s' % name)

    else:
        if sys.platform == 'darwin':
            return os.path.expanduser('~/Library/Application Support/%s' % name)
        else:
            return os.path.expanduser('~/.%s' % name)


class Location(object):

    def open(self, filename, mode='rb'):
        raise NotImplementedError('abstract')


class FileLocation(Location):

    def __init__(self, path):
        self.path = path

    def open(self, filename, mode='rb'):
        return open(os.path.join(self.path, filename), mode)


class ZIPLocation(Location):

    def __init__(self, zip, dir):
        self.zip = zip
        self.dir = dir

    def open(self, filename, mode='rb'):
        if self.dir:
            path = self.dir + '/' + filename
        else:
            path = filename
        text = self.zip.read(path)
        return StringIO.StringIO(text)


class URLLocation(Location):

    def __init__(self, base_url):
        self.base = base_url

    def open(self, filename, mode='rb'):
        import urlparse, urllib2
        url = urlparse.urljoin(self.base, filename)
        return urllib2.urlopen(url)


class Loader(object):

    def __init__(self, path=None, script_home=None):
        if path is None:
            path = [
             '.']
        if type(path) in (str, unicode):
            path = [
             path]
        self.path = list(path)
        if script_home is None:
            script_home = get_script_home()
        self._script_home = script_home
        self._index = None
        self._cached_textures = weakref.WeakValueDictionary()
        self._cached_images = weakref.WeakValueDictionary()
        self._cached_animations = weakref.WeakValueDictionary()
        self._texture_atlas_bins = {}
        return

    def _require_index(self):
        if self._index is None:
            self.reindex()
        return

    def reindex(self):
        self._cached_textures = weakref.WeakValueDictionary()
        self._cached_images = weakref.WeakValueDictionary()
        self._cached_animations = weakref.WeakValueDictionary()
        self._index = {}
        for path in self.path:
            if path.startswith('@'):
                name = path[1:]
                try:
                    module = __import__(name)
                except:
                    continue

                for component in name.split('.')[1:]:
                    module = getattr(module, component)

                if hasattr(module, '__file__'):
                    path = os.path.dirname(module.__file__)
                else:
                    path = ''
            elif not os.path.isabs(path):
                path = os.path.join(self._script_home, path)
            if os.path.isdir(path):
                path = path.rstrip(os.path.sep)
                location = FileLocation(path)
                for dirpath, dirnames, filenames in os.walk(path):
                    dirpath = dirpath[len(path) + 1:]
                    if dirpath:
                        parts = filter(None, dirpath.split(os.sep))
                        dirpath = ('/').join(parts)
                    for filename in filenames:
                        if dirpath:
                            index_name = dirpath + '/' + filename
                        else:
                            index_name = filename
                        self._index_file(index_name, location)

            else:
                dir = ''
                old_path = None
                while path and not os.path.isfile(path):
                    old_path = path
                    path, tail_dir = os.path.split(path)
                    if path == old_path:
                        break
                    dir = ('/').join((tail_dir, dir))

                if path == old_path:
                    continue
                dir = dir.rstrip('/')
                if path and zipfile.is_zipfile(path):
                    zip = zipfile.ZipFile(path, 'r')
                    location = ZIPLocation(zip, dir)
                    for zip_name in zip.namelist():
                        if zip_name.startswith(dir):
                            if dir:
                                zip_name = zip_name[len(dir) + 1:]
                            self._index_file(zip_name, location)

        return

    def _index_file(self, name, location):
        if name not in self._index:
            self._index[name] = location

    def file(self, name, mode='rb'):
        self._require_index()
        try:
            location = self._index[name]
            return location.open(name, mode)
        except KeyError:
            raise ResourceNotFoundException(name)

    def location(self, name):
        self._require_index()
        try:
            return self._index[name]
        except KeyError:
            raise ResourceNotFoundException(name)

    def add_font(self, name):
        self._require_index()
        from pyglet import font
        file = self.file(name)
        font.add_file(file)

    def _alloc_image(self, name):
        file = self.file(name)
        img = pyglet.image.load(name, file=file)
        bin = self._get_texture_atlas_bin(img.width, img.height)
        if bin is None:
            return img.get_texture(True)
        else:
            return bin.add(img)

    def _get_texture_atlas_bin(self, width, height):
        if width > 128 or height > 128:
            return None
        bin_size = 1
        if height > 32:
            bin_size = 2
        try:
            bin = self._texture_atlas_bins[bin_size]
        except KeyError:
            bin = self._texture_atlas_bins[bin_size] = pyglet.image.atlas.TextureBin()

        return bin

    def image(self, name, flip_x=False, flip_y=False, rotate=0):
        self._require_index()
        if name in self._cached_images:
            identity = self._cached_images[name]
        else:
            identity = self._cached_images[name] = self._alloc_image(name)
        if not rotate and not flip_x and not flip_y:
            return identity
        return identity.get_transform(flip_x, flip_y, rotate)

    def animation(self, name, flip_x=False, flip_y=False, rotate=0):
        self._require_index()
        try:
            identity = self._cached_animations[name]
        except KeyError:
            animation = pyglet.image.load_animation(name, self.file(name))
            bin = self._get_texture_atlas_bin(animation.get_max_width(), animation.get_max_height())
            if bin:
                animation.add_to_texture_bin(bin)
            identity = self._cached_animations[name] = animation

        if not rotate and not flip_x and not flip_y:
            return identity
        return identity.get_transform(flip_x, flip_y, rotate)

    def get_cached_image_names(self):
        self._require_index()
        return self._cached_images.keys()

    def get_cached_animation_names(self):
        self._require_index()
        return self._cached_animations.keys()

    def get_texture_bins(self):
        self._require_index()
        return self._texture_atlas_bins.values()

    def media(self, name, streaming=True):
        self._require_index()
        from pyglet import media
        try:
            location = self._index[name]
            if isinstance(location, FileLocation):
                path = os.path.join(location.path, name)
                return media.load(path, streaming=streaming)
            file = location.open(name)
            return media.load(name, file=file, streaming=streaming)
        except KeyError:
            raise ResourceNotFoundException(name)

    def texture(self, name):
        self._require_index()
        if name in self._cached_textures:
            return self._cached_textures[name]
        file = self.file(name)
        texture = pyglet.image.load(name, file=file).get_texture()
        self._cached_textures[name] = texture
        return texture

    def html(self, name):
        self._require_index()
        file = self.file(name)
        return pyglet.text.decode_html(file.read(), self.location(name))

    def attributed(self, name):
        self._require_index()
        file = self.file(name)
        return pyglet.text.load(name, file, 'text/vnd.pyglet-attributed')

    def text(self, name):
        self._require_index()
        file = self.file(name)
        return pyglet.text.load(name, file, 'text/plain')

    def get_cached_texture_names(self):
        self._require_index()
        return self._cached_textures.keys()


path = []

class _DefaultLoader(Loader):

    def _get_path(self):
        global path
        return path

    def _set_path(self, value):
        global path
        path = value

    path = property(_get_path, _set_path)


_default_loader = _DefaultLoader()
reindex = _default_loader.reindex
file = _default_loader.file
location = _default_loader.location
add_font = _default_loader.add_font
image = _default_loader.image
animation = _default_loader.animation
get_cached_image_names = _default_loader.get_cached_image_names
get_cached_animation_names = _default_loader.get_cached_animation_names
get_texture_bins = _default_loader.get_texture_bins
media = _default_loader.media
texture = _default_loader.texture
html = _default_loader.html
attributed = _default_loader.attributed
text = _default_loader.text
get_cached_texture_names = _default_loader.get_cached_texture_names
# okay decompiling out\pyglet.resource.pyc
