from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    # username = serializers.CharField(max_length=64)
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class ProfilePasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    new_password_rep = serializers.CharField(max_length=128)

    def validate(self, attrs):

        if attrs['new_password'] != attrs['new_password_rep']:
            raise serializers.ValidationError(detail='new password and new password\'s repeat does not match')

        return super().validate(attrs)

class ProfileSetEmailSerializer(serializers.Serializer): 
    email = serializers.EmailField(max_length=255)

class ProfileSetPictureSerializer(serializers.Serializer):
    image = serializers.ImageField()

