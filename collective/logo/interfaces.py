from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
from plone.directives import form


_ = MessageFactory('collective.logo')

from zope.interface import Interface
from plone.namedfile import field

 
class ILogoSettingsProvider(Interface):
    """A marker interface for plone.registry configuration interfaces
    """


class ILogoSettings(form.Schema):
    """Logo schema.
    """
    
    
    logo = field.NamedBlobImage(
        title=_(u"label_logo", default=u"Logo"),
        description=_(u"help_logo",
                      default=u"Change the logo")
        )
