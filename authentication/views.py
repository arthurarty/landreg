from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers import UserSerializer, VerificationSerializer
from authentication.utils import send_sms


@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except IntegrityError as e:
            return Response(
                "Number or Username already exists",
                status=status.HTTP_400_BAD_REQUEST)
        send_sms(request.data['phone_number'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_number(request):
    serializer = VerificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Account verified", status=status.HTTP_200_OK)
    return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
