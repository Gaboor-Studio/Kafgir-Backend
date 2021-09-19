from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from ..repositories.user_repo import UserRepository

from typing import List

class UserRepositoryImpl(UserRepository):

    user_model = get_user_model()

    def exist_user_by_username(self, username: str) -> bool:
        return self.user_model.objects.filter(username=username).exists()

    def exist_user_by_email(self, email: str) -> bool:
        return self.user_model.objects.filter(email=email).exists()

    def get_user_by_email(self, email: str) -> user_model:
        return self.user_model.objects.get(email=email)

    def save_user(self, user: user_model) -> None:
        user.save()

    def get_user_by_id(self, id):
        return self.user_model.objects.get(id=id)
    
    def get_user_by_id_and_is_staff(self, id: int, is_staff: bool) -> user_model:
        return self.user_model.objects.get(id=id, is_staff=is_staff)

    def get_all_by_is_staff(self, is_staff: bool) -> QuerySet:
        return self.user_model.objects.filter(is_staff=is_staff)
    
    def delete_by_id(self, id: int):
        self.user_model.objects.filter(id=id).delete()
