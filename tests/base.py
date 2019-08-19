from django.urls import reverse
from rest_framework.test import APITestCase
from authentication.models import User


class BaseTestCase(APITestCase):
    """
    All helper methods
    """

    def signup_user(self, user):
        """
        Method signups user it is given
        by sending post request to signup
        endpoint
        """
        url = reverse('signup')
        return self.client.post(url, user, format='json')
