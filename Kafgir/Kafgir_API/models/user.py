from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from .food import Food


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user.username/<filename>
    return 'profiles/user_{0}/{1}'.format(instance.username, filename)


class UserProfileManager(BaseUserManager):

    def create_user(self, username, email, name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          name=name, last_name=last_name)

        user.set_password(password)

        return user

    def create_superuser(self, username, email, name, last_name, password, is_superuser=True):
        user = self.create_user(username, email, name, last_name, password)

        user.is_active = True
        user.is_superuser = is_superuser
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path)
    favorite_foods = models.ManyToManyField(Food, related_name="favorite_of")
    requested_otp_password = models.CharField(max_length=5, null=True)
    requested_otp_time = models.DateTimeField(null=True)
    requested_token_time = models.DateTimeField(null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'last_name', 'email']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email

    def get_image(self):
        if not self.image:
            return 'no-image'
        return self.image.url
