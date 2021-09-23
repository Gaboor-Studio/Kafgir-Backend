from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    ''' This serializer manages validation over editing profile api'''
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class ProfilePasswordChangeSerializer(serializers.Serializer):
    ''' This serializer manages validation over change profile password api'''
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    new_password_rep = serializers.CharField(max_length=128)

    def validate(self, attrs):

        if attrs['new_password'] != attrs['new_password_rep']:
            raise serializers.ValidationError(detail='new password and new password\'s repeat does not match')

        return super().validate(attrs)

class ProfileSetEmailSerializer(serializers.Serializer): 
    ''' This serializer manages validation over set profile email api'''
    email = serializers.EmailField(max_length=255)

class ProfileSetPictureSerializer(serializers.Serializer):
    ''' This serializer manages validation over set profile picture api'''
    image = serializers.ImageField()

