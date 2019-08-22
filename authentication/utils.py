import os
import random

import africastalking
from dotenv import load_dotenv

from authentication.models import PhoneVerification, User

load_dotenv()


# Initialize SDK
username = os.environ.get('USERNAME')
api_key = os.environ.get('API_KEY')
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def random_code():
    """
    genatea random number
    """
    return random.randrange(000000, 999999)


def send_sms(number):
    """
    Send sms to number provided
    """
    user = User.objects.get(phone_number=number)
    phone_verify = PhoneVerification.objects.create(
        user=user, code=random_code())
    response = sms.send(
        f"Your code is {phone_verify.code}", [f"+{number}"])
    print(response)
