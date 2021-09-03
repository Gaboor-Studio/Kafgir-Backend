from abc import ABC, abstractmethod
from ...models.user import User

class TokenGeneratorUsecase(ABC):

    @abstractmethod
    def generate_auth_token(self, user: User) -> str:
        pass

    @abstractmethod
    def generate_random_str(self, length: int) -> str:
        pass