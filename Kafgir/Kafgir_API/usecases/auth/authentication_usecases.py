from abc import ABC, abstractmethod

from ...dto.auth_dto import UserRegisterInput

class AuthenticationUsecase(ABC):

    @abstractmethod
    def register_user(self, input: UserRegisterInput) -> None:
        pass
