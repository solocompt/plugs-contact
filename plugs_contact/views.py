"""
Plugs Contact Views
"""
from django.conf import settings

from rest_framework import permissions

from plugs_core.viewsets import CreateViewSet

from plugs_mail import utils

from plugs_contact import serializers, models, emails

from plugs_auth.utils import language_from_header

# pylint: disable=R0901
class ContactViewSet(CreateViewSet):
    """
    Contact Viewset
    """
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.AllowAny]

    def get_language(self):
        try:
            accept_language_header = self.request.META['HTTP_ACCEPT_LANGUAGE']
            return language_from_header(accept_language_header)
        except KeyError:
            return settings.LANGUAGE_CODE

    def perform_create(self, serializer):
        try:
            language = self.request.user.language
        except AttributeError:
            language = self.get_language()
        contact = serializer.save()
        data = {'contact': contact}
        payload = {'head': serializer.data.get('email'), 'body': serializer.data.get('message')}
        utils.to_staff(emails.ContactCreated, language, **data)
        utils.to_email(emails.ContactReceived, contact.email, language, **data)
