"""
Plugs Contact Models
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from plugs_core import mixins

class Contact(mixins.Timestampable, models.Model):
    """
    Contact Model
    """
    email = models.EmailField()
    subject = models.CharField(max_length=75, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        """
        Return subject or call method on super is
        subject is null
        """
        return self.subject or super(Contact, self).__str__()

    
    # pylint: disable=R0903
    class Meta:
        """
        Providing verbose names is recommended if
        we want to use i18n in admin site
        """
        ordering = ('created', )
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
