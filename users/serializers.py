from rest_framework import serializers

from users.models import Person


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "username", "email", "password")


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("username", "email", "first_name", "last_name", "about", "image")


class EmptySerializer(serializers.Serializer):
    pass


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
