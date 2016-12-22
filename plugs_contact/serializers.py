"""
Plugs Contact Serializers
"""

from rest_framework import serializers

from plugs_contact import models

class ContactSerializer(serializers.ModelSerializer):
    """
    Contact Serializer
    """
    # pylint: disable=R0903
    class Meta:
        """
        Metaclass definition
        """
        model = models.Contact
        fields = ('id', 'email', 'subject', 'message', 'created', 'updated')
