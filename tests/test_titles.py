from django.urls import reverse
from rest_framework import status

from tests.base import BaseTestCase
from tests.sample_data.authentication import user_1
from tests.sample_data.titles import title


class TitleTestCase(BaseTestCase):
    """
    tests on the title application
    """

    def setUp(self):
        self.signup_user(user_1)
        self.token = self.login_user(user_1)

    def test_create_title(self):
        url = reverse('title:create')
        self.add_token(self.token)
        response = self.client.post(url, title, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
