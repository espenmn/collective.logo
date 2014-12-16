from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from plone.directives import form

from plone.namedfile.field import NamedBlobImage
						

_ = MessageFactory('collective.logo')



class ILogoSettingsProvider(Interface):
    """A marker interface for plone.registry configuration interfaces
    """


class ILogoSettings(form.Schema):
    """Logo schema.
    """


    logo = NamedBlobImage (
        title=_(u"label_logo", default=u"Logo"),
        description=_(u"help_logo",
                      default=u"Change the logo")
        )
