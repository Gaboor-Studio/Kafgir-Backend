from abc import ABC, abstractmethod

from ...dto.auth_dto import UserRegisterInput, VerifyEmailInput, SendEmailInput, ResetPasswordInput, GetResetTokenInput, PasswordResetTokenOutput

class AuthenticationUsecase(ABC):
    ''' This class is an abstract class to define usecases of APIs users need to authenticate'''

    @abstractmethod
    def register_user(self, input: UserRegisterInput) -> None:
        ''' creates a row in user table if and only if no user with the given username and email exists already '''
        pass

    @abstractmethod
    def send_email(self, input: SendEmailInput) -> None:
        ''' sends a 5 digit code to the user's email (could be used in account activation or setting the password) '''
        pass

    @abstractmethod
    def confirm_email(self, input: VerifyEmailInput) -> None:
        ''' given the 5 digit code, activates the account if the email matches with the code and the code is still valid'''
        pass

    @abstractmethod
    def get_reset_token(self, input: GetResetTokenInput) -> PasswordResetTokenOutput:
        ''' given the 5 digit code, generates a token to be used for password reset operation if the code is still valid'''
        pass

    @abstractmethod
    def reset_password(self, input: ResetPasswordInput) -> None:
        ''' given the reset_token, allows the user to set a new password if the token is valid '''
        pass