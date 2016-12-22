"""
Email Template Definition
"""

from plugs_mail.mail import PlugsMail


class ContactCreated(PlugsMail):
    """
    Email sent to superusers notifying of new contact
    """
    template = 'CONTACT_CREATED'
    context = ('Contact', )
    description = 'Email sent to staff users notifying of new contact'
    subject = 'Recebemos novo contato.'

class ContactReceived(PlugsMail):
    """
    Email sent to user confirming the contact reception
    """
    template = 'CONTACT_RECEIVED'
    context = ('Contact', )
    description = 'Email sent to user confirming the contact reception'
    subject = 'Recebemos o teu pedido de informações'
