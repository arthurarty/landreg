from django.urls import reverse
from rest_framework import status
from tests.base import BaseTestCase


class AuthTests(BaseTestCase):

    def test_signup(self):
        """
        Ensure user can create account
        """
        url = reverse('signup')
        data = {
            "username": "test_user",
            "password": "thisIS24!#",
            "phone_number": "256787649914"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Ensure user can create account
        """
        url = reverse('signup')
        data = {
            "username": "test_user2",
            "password": "thisIS24!#",
            "phone_number": "25670000000"
        }
        self.client.post(url, data, format='json')
        url = reverse('login')
        data = {
            "password": "thisIS24!#",
            "phone_number": "25670000000",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
