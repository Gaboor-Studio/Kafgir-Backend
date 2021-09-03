from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=4096)


class VerifyEmailSerializer(serializers.Serializer):
    confirm_code = serializers.CharField(max_length=5)
    email = serializers.EmailField()

class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()