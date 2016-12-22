"""
Plugs Contact Views
"""
from rest_framework import permissions

from plugs_core.viewsets import CreateViewSet

from plugs_mail import utils

from plugs_contact import serializers, models, emails

# pylint: disable=R0901
class ContactViewSet(CreateViewSet):
    """
    Contact Viewset
    """
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        contact = serializer.save()
        data = {'contact': contact}
        payload = {'head': serializer.data.get('email'), 'body': serializer.data.get('message')}
        utils.to_staff(emails.ContactCreated, **data)
        utils.to_email(emails.ContactReceived, contact.email, **data)
