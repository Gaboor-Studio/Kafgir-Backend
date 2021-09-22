from abc import ABC, abstractmethod
from ...models.user import User

class GenerateTokenUsecase(ABC):
    ''' This class contains different usecases of generating tokens for different uses'''

    @abstractmethod
    def generate_token(self, user: User) -> str:
        ''' Generete token for the given user that is unique using sha1 algorithm'''
        pass
