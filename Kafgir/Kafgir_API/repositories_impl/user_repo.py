from django.contrib.auth import get_user_model
from django.db.models import Q

from ..repositories.user_repo import UserRepository

from typing import List

class UserRepositoryImpl(UserRepository):

    model = get_user_model()

    def exist_user_by_email(self, email: str) -> bool:
        return self.model.objects.filter(email=email).exists()

    def get_user_by_email(self, email: str) -> model:
        return self.model.objects.get(email=email)

    def save_user(self, user: model) -> None:
        user.save()

    def get_user_by_id(self, id):
        return self.model.objects.get(id=id)