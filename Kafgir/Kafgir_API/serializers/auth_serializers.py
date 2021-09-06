from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    password = serializers.CharField(max_length=4096)


class VerifyEmailSerializer(serializers.Serializer):
    confirm_code = serializers.CharField(max_length=5)
    email = serializers.EmailField()

class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class GetResetTokenSerializer(serializers.Serializer):
    confirm_code = serializers.CharField(max_length=5)
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    reset_token = serializers.CharField(max_length=127)
    new_password = serializers.CharField(max_length=4096)
    new_password_rep = serializers.CharField(max_length=4096)

    def validate(self, data):
        """
        Check that password and it's repetation are equal.
        """
        if data['new_password'] != data['new_password_rep']:
            raise serializers.ValidationError("new password repeat must be the same as new password")
        return data