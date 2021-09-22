from rest_framework import serializers

class UserManagementCreateProfileSerializer(serializers.Serializer):
    ''' This serializer manages validation over create profile api in admin-management'''

    username= serializers.CharField(max_length=64)
    email= serializers.EmailField(max_length=255)
    password= serializers.CharField(max_length=4096)
    is_active= serializers.NullBooleanField()
    name= serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name= serializers.CharField(max_length=255, required=False, allow_blank=True)

class UserManagementEditProfileSerializer(serializers.Serializer):
    ''' This serializer manages validation over edit profile api'''

    username= serializers.CharField(max_length=64, required=False, allow_blank=True)
    is_active= serializers.NullBooleanField(required=False)
    name= serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name= serializers.CharField(max_length=255, required=False, allow_blank=True)

class UserManagementSetPasswordSerializer(serializers.Serializer):
    ''' This serializer manages validation over set password api'''

    new_password= serializers.CharField(max_length=4096)

class UserManagementSetPfpSerializer(serializers.Serializer):
    ''' This serializer manages validation over set profile picture api'''

    image= serializers.ImageField()
