from rest_framework import serializers

class AdminProfileUpdateSerializer(serializers.Serializer):
    '''This is a serializer for AdminProfileUpdateInput DTO'''
    
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    is_superuser = serializers.BooleanField(default=False)
    
class AdminRegisterSerializer(serializers.Serializer):
    '''This is a serializer for AdminRegisterInput DTO'''
    
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=4096)
    password_repeat = serializers.CharField(max_length=4096)
    is_superuser = serializers.BooleanField(default=False)

    def validate(self, data):
        '''Check that password and it's repetation are equal.'''

        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("password repeat must be the same as the password")
        return data

class AdminResetPasswordSerializer(serializers.Serializer):
    '''This is a serializer for AdminSetPasswordInput DTO'''
    
    new_password = serializers.CharField(max_length=4096)
    new_password_repeat = serializers.CharField(max_length=4096)

    def validate(self, data):
        """Check that password and it's repetation are equal."""

        if data['new_password'] != data['new_password_repeat']:
            raise serializers.ValidationError("new password repeat must be the same as new password")
        return data
