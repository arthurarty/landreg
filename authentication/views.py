from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import UserSerializer


@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
