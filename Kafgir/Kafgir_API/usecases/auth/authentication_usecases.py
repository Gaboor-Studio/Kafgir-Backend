from abc import ABC, abstractmethod

from ...dto.auth_dto import UserRegisterInput, VerifyEmailInput, SendEmailInput

class AuthenticationUsecase(ABC):

    @abstractmethod
    def register_user(self, input: UserRegisterInput) -> None:
        pass

    @abstractmethod
    def send_email(self, input: SendEmailInput) -> None:
        pass

    @abstractmethod
    def confirm_email(self, input: VerifyEmailInput) -> None:
        pass