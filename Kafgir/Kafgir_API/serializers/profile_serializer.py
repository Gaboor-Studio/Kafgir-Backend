from rest_framework import serializers

class ProfileInput(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class ProfileOutput(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    image = serializers.ImageField()

class ProfilePasswordChangeInput(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    new_password_rep = serializers.CharField(max_length=128)

    def validate(self, attrs):

        if attrs['new_password'] != attrs['new_password_rep']:
            raise serializers.ValidationError(detail='new password and new password\'s repeat does not match')

        return super().validate(attrs)

class ProfileSetEmailInput(serializers.Serializer): 
    email = serializers.EmailField(max_length=255)

class ProfileSetPictureInput(serializers.Serializer):
    image = serializers.ImageField()

