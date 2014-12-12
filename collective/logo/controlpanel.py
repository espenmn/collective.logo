from zope.i18nmessageid import MessageFactory
from plone.app.registry.browser import controlpanel
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.logo.interfaces import ILogoSettings
from collective.logo.interfaces import ILogoSettingsProvider

from zope.dottedname.resolve import resolve
from zope.interface import alsoProvides



from z3c.form import interfaces
from zope import schema

from plone.directives import form
from collective.logo.interfaces import ILogoSettingsProvider


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.logo')


class ContextProxy(object):

    def __init__(self, interfaces):
        self.__interfaces = interfaces
        alsoProvides(self, *interfaces)

    def __setattr__(self, name, value):
        if name.startswith('__') or name.startswith('_ContextProxy__'):
            return object.__setattr__(self, name, value)

        registry = getUtility(IRegistry)
        for interface in self.__interfaces:
            proxy = registry.forInterface(interface)
            try:
                getattr(proxy, name)
            except AttributeError:
                pass
            else:
                return setattr(proxy, name, value)
        raise AttributeError(name)

    def __getattr__(self, name):
        if name.startswith('__') or name.startswith('_ContextProxy__'):
            return object.__getattr__(self, name)

        registry = getUtility(IRegistry)
        for interface in self.__interfaces:
            proxy = registry.forInterface(interface)
            try:
                return getattr(proxy, name)
            except AttributeError:
                pass

        raise AttributeError(name)


class LogoSettingsEditForm(controlpanel.RegistryEditForm):
    schema = ILogoSettings
    label = _(u"Logo Controlpanel")
    description = _(u"Change the default Plone logo")

    def getContent(self):
        interfaces = [self.schema]
        interfaces.extend(self.additionalSchemata)
        return ContextProxy(interfaces)

    @property
    def additionalSchemata(self):
        registry = getUtility(IRegistry)
        interface_names = set(record.interfaceName for record
                              in registry.records.values())

        for name in interface_names:
            if not name:
                continue

            interface = resolve(name)
            if ILogoSettingsProvider.providedBy(interface):
                yield interface

    def updateFields(self):
        super(LogoSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(LogoSettingsEditForm, self).updateWidgets()


class LogoControlPanel(controlpanel.ControlPanelFormWrapper):
    form = LogoSettingsEditForm

                        

