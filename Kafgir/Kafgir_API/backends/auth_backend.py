import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

user_model = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    """
    Custom Email Backend to perform authentication via email or username
    """

    EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if re.fullmatch(self.EMAIL_REGEX, username):
            try:
                user =  user_model.objects.get(email=username)
                print(user.check_password(password))
                return user if user.check_password(password) else None
            except:
                return None
        try:
            user = user_model.objects.get(username=username)
            print(user.check_password(password))
            return user if user.check_password(password) else None
        except:
            print('here')
            return None

    def get_user(self, user_id):
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None