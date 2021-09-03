from abc import ABC, abstractmethod

class TokenGeneratorUsecase(ABC):

    @abstractmethod
    def generate_auth_token(self, id: int) -> str:
        pass

    @abstractmethod
    def generate_random_str(self, length: int) -> str:
        pass