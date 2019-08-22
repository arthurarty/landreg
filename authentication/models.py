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

    @property
    def phone_verification(self):
        """return the phone_verification object"""
        return PhoneVerification.objects.get(user=self.id)


class PhoneVerification(models.Model):
    """Phone verification table"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
