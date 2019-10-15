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
        url = reverse('authentication:signup')
        httpretty.register_uri(
            httpretty.POST, "https://api.sandbox.africastalking.com/version1/messaging",
            body=json.dumps({"hello": "world"}))
        return self.client.post(url, user, format='json')

    def activate_user(self, phone_number):
        """Activate a user so they can login"""
        user = User.objects.get(phone_number=phone_number)
        user.is_active = True
        user.save()

    def add_token(self, token):
        """adds authentication credentials in the request header"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def login_user(self, user):
        """
        logs in activated user and returns token
        """
        self.activate_user(user['phone_number'])
        url = reverse('authentication:login')
        data = {
            "password": "thisIS24!#",
            "phone_number": "25670000000",
        }
        response = self.client.post(url, data, format='json')
        return response.data['access']
