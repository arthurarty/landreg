from django.urls import reverse
from rest_framework import status

from authentication.models import User
from tests.base import BaseTestCase
from tests.sample_data.authentication import user, user_1


class AuthTests(BaseTestCase):
    def setUp(self):
        self.signup_user(user_1)

    def test_sign_up(self):
        """
        Ensure user can create account
        """
        response = self.signup_user(user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Ensure user can login using existing account
        """
        self.activate_user(user_1['phone_number'])
        url = reverse('authentication:login')
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
        response = self.signup_user(user_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_verification(self):
        """
        Ensure user can verify account
        """
        user = User.objects.get(phone_number=user_1['phone_number'])
        url = reverse('authentication:verify')
        data = {
            "phone_number": user_1['phone_number'],
            "code": user.phone_verification.code
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
