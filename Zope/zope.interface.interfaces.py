# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\zope.interface.interfaces
__docformat__ = 'restructuredtext'
from zope.interface.interface import Attribute
from zope.interface.interface import Interface
from zope.interface.declarations import implementer
from zope.interface._compat import _u
_BLANK = _u('')

class IElement(Interface):
    __name__ = Attribute('__name__', 'The object name')
    __doc__ = Attribute('__doc__', 'The object doc string')

    def getTaggedValue(tag):
        pass

    def queryTaggedValue(tag, default=None):
        pass

    def getTaggedValueTags():
        pass

    def setTaggedValue(tag, value):
        pass


class IAttribute(IElement):
    interface = Attribute('interface', 'Stores the interface instance in which the attribute is located.')


class IMethod(IAttribute):

    def getSignatureInfo():
        pass

    def getSignatureString():
        pass


class ISpecification(Interface):

    def providedBy(object):
        pass

    def implementedBy(class_):
        pass

    def isOrExtends(other):
        pass

    def extends(other, strict=True):
        pass

    def weakref(callback=None):
        pass

    __bases__ = Attribute('Base specifications\n\n    A tuple if specifications from which this specification is\n    directly derived.\n\n    ')
    __sro__ = Attribute("Specification-resolution order\n\n    A tuple of the specification and all of it's ancestor\n    specifications from most specific to least specific.\n\n    (This is similar to the method-resolution order for new-style classes.)\n    ")
    __iro__ = Attribute("Interface-resolution order\n\n    A tuple of the of the specification's ancestor interfaces from\n    most specific to least specific.  The specification itself is\n    included if it is an interface.\n\n    (This is similar to the method-resolution order for new-style classes.)\n    ")

    def get(name, default=None):
        pass


class IInterface(ISpecification, IElement):

    def names(all=False):
        pass

    def namesAndDescriptions(all=False):
        pass

    def __getitem__(name):
        pass

    def direct(name):
        pass

    def validateInvariants(obj, errors=None):
        pass

    def __contains__(name):
        pass

    def __iter__():
        pass

    __module__ = Attribute('The name of the module defining the interface')


class IDeclaration(ISpecification):

    def __contains__(interface):
        pass

    def __iter__():
        pass

    def flattened():
        pass

    def __sub__(interfaces):
        pass

    def __add__(interfaces):
        pass

    def __nonzero__():
        pass


class IInterfaceDeclaration(Interface):

    def providedBy(ob):
        pass

    def implementedBy(class_):
        pass

    def classImplements(class_, *interfaces):
        pass

    def implementer(*interfaces):
        pass

    def classImplementsOnly(class_, *interfaces):
        pass

    def implementer_only(*interfaces):
        pass

    def directlyProvidedBy(object):
        pass

    def directlyProvides(object, *interfaces):
        pass

    def alsoProvides(object, *interfaces):
        pass

    def noLongerProvides(object, interface):
        pass

    def implements(*interfaces):
        pass

    def implementsOnly(*interfaces):
        pass

    def classProvides(*interfaces):
        pass

    def provider(*interfaces):
        pass

    def moduleProvides(*interfaces):
        pass

    def Declaration(*interfaces):
        pass


class IAdapterRegistry(Interface):

    def register(required, provided, name, value):
        pass

    def registered(required, provided, name=_BLANK):
        pass

    def lookup(required, provided, name='', default=None):
        pass

    def queryMultiAdapter(objects, provided, name=_BLANK, default=None):
        pass

    def lookup1(required, provided, name=_BLANK, default=None):
        pass

    def queryAdapter(object, provided, name=_BLANK, default=None):
        pass

    def adapter_hook(provided, object, name=_BLANK, default=None):
        pass

    def lookupAll(required, provided):
        pass

    def names(required, provided):
        pass

    def subscribe(required, provided, subscriber, name=_BLANK):
        pass

    def subscriptions(required, provided, name=_BLANK):
        pass

    def subscribers(objects, provided, name=_BLANK):
        pass


class ComponentLookupError(LookupError):
    pass


class Invalid(Exception):
    pass


class IObjectEvent(Interface):
    object = Attribute('The subject of the event.')


@implementer(IObjectEvent)
class ObjectEvent(object):

    def __init__(self, object):
        self.object = object


class IComponentLookup(Interface):
    adapters = Attribute('Adapter Registry to manage all registered adapters.')
    utilities = Attribute('Adapter Registry to manage all registered utilities.')

    def queryAdapter(object, interface, name=_BLANK, default=None):
        pass

    def getAdapter(object, interface, name=_BLANK):
        pass

    def queryMultiAdapter(objects, interface, name=_BLANK, default=None):
        pass

    def getMultiAdapter(objects, interface, name=_BLANK):
        pass

    def getAdapters(objects, provided):
        pass

    def subscribers(objects, provided):
        pass

    def handle(*objects):
        pass

    def queryUtility(interface, name='', default=None):
        pass

    def getUtilitiesFor(interface):
        pass

    def getAllUtilitiesRegisteredFor(interface):
        pass


class IRegistration(Interface):
    registry = Attribute('The registry having the registration')
    name = Attribute('The registration name')
    info = Attribute('Information about the registration\n\n    This is information deemed useful to people browsing the\n    configuration of a system. It could, for example, include\n    commentary or information about the source of the configuration.\n    ')


class IUtilityRegistration(IRegistration):
    factory = Attribute('The factory used to create the utility. Optional.')
    component = Attribute('The object registered')
    provided = Attribute('The interface provided by the component')


class _IBaseAdapterRegistration(IRegistration):
    factory = Attribute('The factory used to create adapters')
    required = Attribute('The adapted interfaces\n\n    This is a sequence of interfaces adapters by the registered\n    factory.  The factory will be caled with a sequence of objects, as\n    positional arguments, that provide these interfaces.\n    ')
    provided = Attribute('The interface provided by the adapters.\n\n    This interface is implemented by the factory\n    ')


class IAdapterRegistration(_IBaseAdapterRegistration):
    pass


class ISubscriptionAdapterRegistration(_IBaseAdapterRegistration):
    pass


class IHandlerRegistration(IRegistration):
    handler = Attribute('An object called used to handle an event')
    required = Attribute('The handled interfaces\n\n    This is a sequence of interfaces handled by the registered\n    handler.  The handler will be caled with a sequence of objects, as\n    positional arguments, that provide these interfaces.\n    ')


class IRegistrationEvent(IObjectEvent):
    pass


@implementer(IRegistrationEvent)
class RegistrationEvent(ObjectEvent):

    def __repr__(self):
        return '%s event:\n%r' % (self.__class__.__name__, self.object)


class IRegistered(IRegistrationEvent):
    pass


@implementer(IRegistered)
class Registered(RegistrationEvent):
    pass


class IUnregistered(IRegistrationEvent):
    pass


@implementer(IUnregistered)
class Unregistered(RegistrationEvent):
    pass


class IComponentRegistry(Interface):

    def registerUtility(component=None, provided=None, name=_BLANK, info=_BLANK, factory=None):
        pass

    def unregisterUtility(component=None, provided=None, name=_BLANK, factory=None):
        pass

    def registeredUtilities():
        pass

    def registerAdapter(factory, required=None, provided=None, name=_BLANK, info=_BLANK):
        pass

    def unregisterAdapter(factory=None, required=None, provided=None, name=_BLANK):
        pass

    def registeredAdapters():
        pass

    def registerSubscriptionAdapter(factory, required=None, provides=None, name=_BLANK, info=''):
        pass

    def unregisterSubscriptionAdapter(factory=None, required=None, provides=None, name=_BLANK):
        pass

    def registeredSubscriptionAdapters():
        pass

    def registerHandler(handler, required=None, name=_BLANK, info=''):
        pass

    def unregisterHandler(handler=None, required=None, name=_BLANK):
        pass

    def registeredHandlers():
        pass


class IComponents(IComponentLookup, IComponentRegistry):
    pass
# okay decompiling out\zope.interface.interfaces.pyc
