from abc import ABC, abstractmethod
from ...models.user import User

class GenerateTokenUsecase(ABC):

    @abstractmethod
    def generate_token(self, user: User) -> str:
        pass
