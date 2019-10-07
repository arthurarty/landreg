import json

import httpretty
from django.urls import reverse
from rest_framework.test import APITestCase

from authentication.models import User


class BaseTestCase(APITestCase):
    """
    All helper methods
    """

    @httpretty.activate
    def signup_user(self, user):
        """
        Method signups user it is given
        by sending post request to signup
        endpoint
        """
        url = reverse('signup')
        httpretty.register_uri(
            httpretty.POST, "https://api.sandbox.africastalking.com/version1/messaging",
            body=json.dumps({"hello": "world"}))
        return self.client.post(url, user, format='json')

    def activate_user(self, phone_number):
        """Activate a user so they can login"""
        user = User.objects.get(phone_number=phone_number)
        user.is_active = True
        user.save()
