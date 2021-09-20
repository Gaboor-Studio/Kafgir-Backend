from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model

from django.db.models.query import QuerySet

class UserRepository(ABC):

    user_model = get_user_model()

    @abstractmethod
    def exist_user_by_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def exist_user_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> user_model:
        pass

    @abstractmethod
    def save_user(self, user: user_model) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, id: int):
        pass
    
    @abstractmethod
    def get_user_by_id_and_is_staff(self, id: int, is_staff: bool) -> user_model:
        pass

    @abstractmethod
    def get_all_by_is_staff(self, is_staff: bool) -> QuerySet:
        pass

    @abstractmethod
    def delete_by_id(self, id: int):
        pass