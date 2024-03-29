# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface.adapter
import weakref
from zope.interface import providedBy
from zope.interface import Interface
from zope.interface import ro
from zope.interface._compat import _u
from zope.interface._compat import _normalize_name
_BLANK = _u('')

class BaseAdapterRegistry(object):
    _delegated = ('lookup', 'queryMultiAdapter', 'lookup1', 'queryAdapter', 'adapter_hook',
                  'lookupAll', 'names', 'subscriptions', 'subscribers')
    _generation = 0

    def __init__(self, bases=()):
        self._adapters = []
        self._subscribers = []
        self._provided = {}
        self._createLookup()
        self.__bases__ = bases

    def _setBases(self, bases):
        self.__dict__['__bases__'] = bases
        self.ro = ro.ro(self)
        self.changed(self)

    __bases__ = property((lambda self: self.__dict__['__bases__']), (lambda self, bases: self._setBases(bases)))

    def _createLookup(self):
        self._v_lookup = self.LookupClass(self)
        for name in self._delegated:
            self.__dict__[name] = getattr(self._v_lookup, name)

    def changed(self, originally_changed):
        self._generation += 1
        self._v_lookup.changed(originally_changed)

    def register(self, required, provided, name, value):
        if value is None:
            self.unregister(required, provided, name, value)
            return
        else:
            required = tuple(map(_convert_None_to_Interface, required))
            name = _normalize_name(name)
            order = len(required)
            byorder = self._adapters
            while len(byorder) <= order:
                byorder.append({})

            components = byorder[order]
            key = required + (provided,)
            for k in key:
                d = components.get(k)
                if d is None:
                    d = {}
                    components[k] = d
                components = d

            if components.get(name) is value:
                return
            components[name] = value
            n = self._provided.get(provided, 0) + 1
            self._provided[provided] = n
            if n == 1:
                self._v_lookup.add_extendor(provided)
            self.changed(self)
            return

    def registered(self, required, provided, name=_BLANK):
        required = tuple(map(_convert_None_to_Interface, required))
        name = _normalize_name(name)
        order = len(required)
        byorder = self._adapters
        if len(byorder) <= order:
            return
        else:
            components = byorder[order]
            key = required + (provided,)
            for k in key:
                d = components.get(k)
                if d is None:
                    return
                components = d

            return components.get(name)

    def unregister(self, required, provided, name, value=None):
        required = tuple(map(_convert_None_to_Interface, required))
        order = len(required)
        byorder = self._adapters
        if order >= len(byorder):
            return False
        else:
            components = byorder[order]
            key = required + (provided,)
            lookups = []
            for k in key:
                d = components.get(k)
                if d is None:
                    return
                lookups.append((components, k))
                components = d

            old = components.get(name)
            if old is None:
                return
            if value is not None and old is not value:
                return
            del components[name]
            if not components:
                for comp, k in reversed(lookups):
                    d = comp[k]
                    if d:
                        break
                    else:
                        del comp[k]

                while byorder and not byorder[-1]:
                    del byorder[-1]

            n = self._provided[provided] - 1
            if n == 0:
                del self._provided[provided]
                self._v_lookup.remove_extendor(provided)
            else:
                self._provided[provided] = n
            self.changed(self)
            return

    def subscribe(self, required, provided, value):
        required = tuple(map(_convert_None_to_Interface, required))
        name = _BLANK
        order = len(required)
        byorder = self._subscribers
        while len(byorder) <= order:
            byorder.append({})

        components = byorder[order]
        key = required + (provided,)
        for k in key:
            d = components.get(k)
            if d is None:
                d = {}
                components[k] = d
            components = d

        components[name] = components.get(name, ()) + (value,)
        if provided is not None:
            n = self._provided.get(provided, 0) + 1
            self._provided[provided] = n
            if n == 1:
                self._v_lookup.add_extendor(provided)
        self.changed(self)
        return

    def unsubscribe(self, required, provided, value=None):
        required = tuple(map(_convert_None_to_Interface, required))
        order = len(required)
        byorder = self._subscribers
        if order >= len(byorder):
            return
        else:
            components = byorder[order]
            key = required + (provided,)
            lookups = []
            for k in key:
                d = components.get(k)
                if d is None:
                    return
                lookups.append((components, k))
                components = d

            old = components.get(_BLANK)
            if not old:
                return
            if value is None:
                new = ()
            else:
                new = tuple([ v for v in old if v is not value ])
            if new == old:
                return
            if new:
                components[_BLANK] = new
            else:
                del components[_BLANK]
                for comp, k in reversed(lookups):
                    d = comp[k]
                    if d:
                        break
                    else:
                        del comp[k]

                while byorder and not byorder[-1]:
                    del byorder[-1]

            if provided is not None:
                n = self._provided[provided] + len(new) - len(old)
                if n == 0:
                    del self._provided[provided]
                    self._v_lookup.remove_extendor(provided)
            self.changed(self)
            return

    def get(self, _):

        class XXXTwistedFakeOut:
            selfImplied = {}

        return XXXTwistedFakeOut


_not_in_mapping = object()

class LookupBaseFallback(object):

    def __init__(self):
        self._cache = {}
        self._mcache = {}
        self._scache = {}

    def changed(self, ignored=None):
        self._cache.clear()
        self._mcache.clear()
        self._scache.clear()

    def _getcache(self, provided, name):
        cache = self._cache.get(provided)
        if cache is None:
            cache = {}
            self._cache[provided] = cache
        if name:
            c = cache.get(name)
            if c is None:
                c = {}
                cache[name] = c
            cache = c
        return cache

    def lookup(self, required, provided, name=_BLANK, default=None):
        cache = self._getcache(provided, name)
        required = tuple(required)
        if len(required) == 1:
            result = cache.get(required[0], _not_in_mapping)
        else:
            result = cache.get(tuple(required), _not_in_mapping)
        if result is _not_in_mapping:
            result = self._uncached_lookup(required, provided, name)
            if len(required) == 1:
                cache[required[0]] = result
            else:
                cache[tuple(required)] = result
        if result is None:
            return default
        else:
            return result

    def lookup1(self, required, provided, name=_BLANK, default=None):
        cache = self._getcache(provided, name)
        result = cache.get(required, _not_in_mapping)
        if result is _not_in_mapping:
            return self.lookup((required,), provided, name, default)
        else:
            if result is None:
                return default
            return result

    def queryAdapter(self, object, provided, name=_BLANK, default=None):
        return self.adapter_hook(provided, object, name, default)

    def adapter_hook(self, provided, object, name=_BLANK, default=None):
        required = providedBy(object)
        cache = self._getcache(provided, name)
        factory = cache.get(required, _not_in_mapping)
        if factory is _not_in_mapping:
            factory = self.lookup((required,), provided, name)
        if factory is not None:
            result = factory(object)
            if result is not None:
                return result
        return default

    def lookupAll(self, required, provided):
        cache = self._mcache.get(provided)
        if cache is None:
            cache = {}
            self._mcache[provided] = cache
        required = tuple(required)
        result = cache.get(required, _not_in_mapping)
        if result is _not_in_mapping:
            result = self._uncached_lookupAll(required, provided)
            cache[required] = result
        return result

    def subscriptions(self, required, provided):
        cache = self._scache.get(provided)
        if cache is None:
            cache = {}
            self._scache[provided] = cache
        required = tuple(required)
        result = cache.get(required, _not_in_mapping)
        if result is _not_in_mapping:
            result = self._uncached_subscriptions(required, provided)
            cache[required] = result
        return result


LookupBasePy = LookupBaseFallback
try:
    from _zope_interface_coptimizations import LookupBase
except ImportError:
    LookupBase = LookupBaseFallback

class VerifyingBaseFallback(LookupBaseFallback):

    def changed(self, originally_changed):
        LookupBaseFallback.changed(self, originally_changed)
        self._verify_ro = self._registry.ro[1:]
        self._verify_generations = [ r._generation for r in self._verify_ro ]

    def _verify(self):
        if [ r._generation for r in self._verify_ro ] != self._verify_generations:
            self.changed(None)
        return

    def _getcache(self, provided, name):
        self._verify()
        return LookupBaseFallback._getcache(self, provided, name)

    def lookupAll(self, required, provided):
        self._verify()
        return LookupBaseFallback.lookupAll(self, required, provided)

    def subscriptions(self, required, provided):
        self._verify()
        return LookupBaseFallback.subscriptions(self, required, provided)


VerifyingBasePy = VerifyingBaseFallback
try:
    from _zope_interface_coptimizations import VerifyingBase
except ImportError:
    VerifyingBase = VerifyingBaseFallback

class AdapterLookupBase(object):

    def __init__(self, registry):
        self._registry = registry
        self._required = {}
        self.init_extendors()
        super(AdapterLookupBase, self).__init__()

    def changed(self, ignored=None):
        super(AdapterLookupBase, self).changed(None)
        for r in self._required.keys():
            r = r()
            if r is not None:
                r.unsubscribe(self)

        self._required.clear()
        return

    def init_extendors(self):
        self._extendors = {}
        for p in self._registry._provided:
            self.add_extendor(p)

    def add_extendor(self, provided):
        _extendors = self._extendors
        for i in provided.__iro__:
            extendors = _extendors.get(i, ())
            _extendors[i] = [ e for e in extendors if provided.isOrExtends(e) ] + [provided] + [ e for e in extendors if not provided.isOrExtends(e) ]

    def remove_extendor(self, provided):
        _extendors = self._extendors
        for i in provided.__iro__:
            _extendors[i] = [ e for e in _extendors.get(i, ()) if e != provided ]

    def _subscribe(self, *required):
        _refs = self._required
        for r in required:
            ref = r.weakref()
            if ref not in _refs:
                r.subscribe(self)
                _refs[ref] = 1

    def _uncached_lookup(self, required, provided, name=_BLANK):
        required = tuple(required)
        result = None
        order = len(required)
        for registry in self._registry.ro:
            byorder = registry._adapters
            if order >= len(byorder):
                continue
            extendors = registry._v_lookup._extendors.get(provided)
            if not extendors:
                continue
            components = byorder[order]
            result = _lookup(components, required, extendors, name, 0, order)
            if result is not None:
                break

        self._subscribe(*required)
        return result

    def queryMultiAdapter(self, objects, provided, name=_BLANK, default=None):
        factory = self.lookup(map(providedBy, objects), provided, name)
        if factory is None:
            return default
        else:
            result = factory(*objects)
            if result is None:
                return default
            return result

    def _uncached_lookupAll(self, required, provided):
        required = tuple(required)
        order = len(required)
        result = {}
        for registry in reversed(self._registry.ro):
            byorder = registry._adapters
            if order >= len(byorder):
                continue
            extendors = registry._v_lookup._extendors.get(provided)
            if not extendors:
                continue
            components = byorder[order]
            _lookupAll(components, required, extendors, result, 0, order)

        self._subscribe(*required)
        return tuple(result.items())

    def names(self, required, provided):
        return [ c[0] for c in self.lookupAll(required, provided) ]

    def _uncached_subscriptions(self, required, provided):
        required = tuple(required)
        order = len(required)
        result = []
        for registry in reversed(self._registry.ro):
            byorder = registry._subscribers
            if order >= len(byorder):
                continue
            if provided is None:
                extendors = (
                 provided,)
            else:
                extendors = registry._v_lookup._extendors.get(provided)
                if extendors is None:
                    continue
            _subscriptions(byorder[order], required, extendors, _BLANK, result, 0, order)

        self._subscribe(*required)
        return result

    def subscribers(self, objects, provided):
        subscriptions = self.subscriptions(map(providedBy, objects), provided)
        if provided is None:
            result = ()
            for subscription in subscriptions:
                subscription(*objects)

        else:
            result = []
            for subscription in subscriptions:
                subscriber = subscription(*objects)
                if subscriber is not None:
                    result.append(subscriber)

        return result


class AdapterLookup(AdapterLookupBase, LookupBase):
    pass


class AdapterRegistry(BaseAdapterRegistry):
    LookupClass = AdapterLookup

    def __init__(self, bases=()):
        self._v_subregistries = weakref.WeakKeyDictionary()
        super(AdapterRegistry, self).__init__(bases)

    def _addSubregistry(self, r):
        self._v_subregistries[r] = 1

    def _removeSubregistry(self, r):
        if r in self._v_subregistries:
            del self._v_subregistries[r]

    def _setBases(self, bases):
        old = self.__dict__.get('__bases__', ())
        for r in old:
            if r not in bases:
                r._removeSubregistry(self)

        for r in bases:
            if r not in old:
                r._addSubregistry(self)

        super(AdapterRegistry, self)._setBases(bases)

    def changed(self, originally_changed):
        super(AdapterRegistry, self).changed(originally_changed)
        for sub in self._v_subregistries.keys():
            sub.changed(originally_changed)


class VerifyingAdapterLookup(AdapterLookupBase, VerifyingBase):
    pass


class VerifyingAdapterRegistry(BaseAdapterRegistry):
    LookupClass = VerifyingAdapterLookup


def _convert_None_to_Interface(x):
    if x is None:
        return Interface
    else:
        return x
        return


def _lookup(components, specs, provided, name, i, l):
    if i < l:
        for spec in specs[i].__sro__:
            comps = components.get(spec)
            if comps:
                r = _lookup(comps, specs, provided, name, i + 1, l)
                if r is not None:
                    return r

    else:
        for iface in provided:
            comps = components.get(iface)
            if comps:
                r = comps.get(name)
                if r is not None:
                    return r

    return


def _lookupAll(components, specs, provided, result, i, l):
    if i < l:
        for spec in reversed(specs[i].__sro__):
            comps = components.get(spec)
            if comps:
                _lookupAll(comps, specs, provided, result, i + 1, l)

    else:
        for iface in reversed(provided):
            comps = components.get(iface)
            if comps:
                result.update(comps)


def _subscriptions(components, specs, provided, name, result, i, l):
    if i < l:
        for spec in reversed(specs[i].__sro__):
            comps = components.get(spec)
            if comps:
                _subscriptions(comps, specs, provided, name, result, i + 1, l)

    else:
        for iface in reversed(provided):
            comps = components.get(iface)
            if comps:
                comps = comps.get(name)
                if comps:
                    result.extend(comps)
# okay decompiling out\zope.interface.adapter.pyc
