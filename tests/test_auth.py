from django.urls import reverse
from rest_framework import status
from tests.base import BaseTestCase


class AuthTests(BaseTestCase):

    def test_signup(self):
        """
        Ensure user can create account
        """
        user = {
            "username": "test_user",
            "password": "thisIS24!#",
            "phone_number": "256787649914"
        }
        response = self.signup_user(user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Ensure user can login using existing account
        """
        user_1 = {
            "username": "test_user2",
            "password": "thisIS24!#",
            "phone_number": "25670000000"
        }
        self.signup_user(user_1)
        url = reverse('login')
        data = {
            "password": "thisIS24!#",
            "phone_number": "25670000000",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_duplicate_account(self):
        """
        Ensure duplicate accounts are handled
        """
        user_1 = {
            "username": "test_user2",
            "password": "thisIS24!#",
            "phone_number": "25670000000"
        }
        self.signup_user(user_1)
        response = self.signup_user(user_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
