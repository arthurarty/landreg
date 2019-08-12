from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    def create(self, validated_data):
        """
        Create and return user instance, given validate data
        """
        user = User()
        user.email = validated_data.get('email')
        user.set_password(validated_data.get('password'))
        user.phone_number = validated_data.get('phone_number')
        user.username = validated_data.get('username')
        user.save()
        return user


class TokenSerializer(serializers.Serializer):
    """
    Serializer that serializes token data
    """
    token = serializers.CharField()
