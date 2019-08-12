from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user class to include phone number
    and change username field to email
    """
    email = models.EmailField(null=True, blank=True, default='')
    phone_number = models.CharField(unique=True, max_length=12)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'password']
