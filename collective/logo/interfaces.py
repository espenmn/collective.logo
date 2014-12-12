from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from plone.directives import form

#from plone.namedfile.field import NamedImage
						

_ = MessageFactory('collective.logo')



class ILogoSettingsProvider(Interface):
    """A marker interface for plone.registry configuration interfaces
    """


class ILogoSettings(form.Schema):
    """Logo schema.
    """

    form.fieldset(
        'logo',
        label=_(u'Logo Settings'),
        fields=[
            'logo',
            ],
        )

    logo = schema.TextLine (
        title=_(u"label_logo", default=u"Logo"),
        description=_(u"help_logo",
                      default=u"Change the logo")
        )

    form.fieldset(
        'footer',
        label=_(u'footer Settings'),
        fields=[
            'footer',
            ],
        )
    footer = schema.TextLine (
        title=_(u"label_footer", default=u"Footer"),
        description=_(u"help_footer",
                      default=u"Change the footer text")
        )
