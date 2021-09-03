from abc import ABC, abstractmethod

from ..models.user import User

class UserRepository(ABC):

    @abstractmethod
    def exist_user_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, id):
        pass