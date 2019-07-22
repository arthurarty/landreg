from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=True, max_length=50)
    last_name = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def create(self, validated_data):
        """
        Create and return user instance, given validate data
        """
        user = User()
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.email = validated_data.get('email')
        user.set_password(validated_data.get('password'))
        user.phone_number = validated_data.get('phone_number')
        user.username = validated_data.get('phone_number')
        user.save()
        return user
