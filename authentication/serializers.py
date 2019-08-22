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
        user.is_active = False
        user.save()
        return user


class TokenSerializer(serializers.Serializer):
    """
    Serializer that serializes token data
    """
    token = serializers.CharField()


class VerificationSerializer(serializers.Serializer):
    """
    Serializer for phone verification
    """
    code = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def create(self, validated_data):
        """
        Change status of verification to true
        Activate user's account
        """
        user = User.objects.get(
            phone_number=validated_data.get('phone_number')
            )
        verify = user.phone_verification
        if verify.code == validated_data.get('code'):
            verify.status = True
            verify.save()
            user.is_active = True
            user.save()
            return verify
        return None
