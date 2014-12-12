from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from plone.directives import form


_ = MessageFactory('collective.logo')



class ILogoSettingsProvider(Interface):
    """A marker interface for plone.registry configuration interfaces
    """


class ILogoSettings(form.Schema):
    """Logo schema.
    """


    