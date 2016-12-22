"""
Testing Views
"""

from django.core.urlresolvers import reverse

from plugs_core.testcases import PlugsAPITestCase


class TestsViews(PlugsAPITestCase):
    """
    Testing Views
    """
    
    def test_guest_can_create_contact(self):
        """
        Ensures guest can create contact
        """
        data = {'email': 'janedoe@example.com', 'subject': 'test 123', 'message': 'testing'}
        response = self.client.post(reverse('contact-list'), data)
        self.assert201(response)

    def test_methods_not_allowed(self):
        """
        Ensures methods not allowed for contacts endpoint
        """
        response = self.client.get(reverse('contact-list'))
        self.assert405(response)                
