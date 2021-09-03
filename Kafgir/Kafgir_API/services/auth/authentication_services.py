from dependency_injector.wiring import inject, Provide
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta
from smtplib import SMTPException

from ...dto.auth_dto import UserRegisterInput, VerifyEmailInput, SendEmailInput, GetResetTokenInput, ResetPasswordInput, PasswordResetTokenOutput
from ...usecases.auth.authentication_usecases import AuthenticationUsecase
from ...usecases.auth.token_generator_usecase import TokenGeneratorUsecase
from ...exceptions.bad_request import UserAlreadyExistsException, OptPasswordIsntSet, UserIsAlreadyActivated, PasscodeIsExpired, WrongPasscode, ResetTokenIsNotSet, ResetTokenIsExpired, WrongResetToken
from ...exceptions.not_found import UserNotFoundException
from ...exceptions.common import CannotGenerateCode, CannotGetCurrentTime, CannotSendEmail, CannotGenerateToken
from ...repositories.user_repo import UserRepository

class AuthenticationService(AuthenticationUsecase):

    model = get_user_model()

    utc=pytz.UTC

    @inject
    def __init__(self, user_repo: UserRepository = Provide['user_repo']
                     , token_generator_usecase: TokenGeneratorUsecase = Provide['token_generator_usecase']):
        self.user_repo = user_repo
        self.token_generator_usecase = token_generator_usecase
    
    def register_user(self, input: UserRegisterInput) -> None:
        
        if self.user_repo.exist_user_by_email(input.email):
            raise UserAlreadyExistsException(detail=f'User(email={input.email}) already exists!')

        user = self.model.objects.create_user(
            username=input.username, email=input.email, name=input.name, last_name=input.last_name, password=input.password)

        self.user_repo.save_user(user)

    def send_email(self, input: SendEmailInput) -> None:
        
        try: 
            user = self.user_repo.get_user_by_email(input.email)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with email={input.email} does not exist!')


        passcode = self.token_generator_usecase.generate_random_str(5)

        if passcode is None:
            raise CannotGenerateCode()

        create_time = datetime.now()

        if create_time is None:
            raise CannotGetCurrentTime()

        user.requested_otp_password = passcode
        user.requested_otp_time = create_time

        try:    
            send_mail(
                'Kafgir Confirmation code',
                f'your confirmation code is: {passcode}. you\'re code expires at {create_time + relativedelta(minutes=5)}.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
        except SMTPException:
            raise CannotSendEmail()
            
        self.user_repo.save_user(user)

    def confirm_email(self, input: VerifyEmailInput) -> None:
        
        try: 
            user = self.user_repo.get_user_by_email(input.email)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with email={input.email} does not exist!')

        if user.requested_otp_password is not None:

            deadline = user.requested_otp_time + relativedelta(minutes=5)

            if input.confirm_code != user.requested_otp_password:
                raise WrongPasscode()

            if datetime.now().replace(tzinfo=self.utc) > deadline.replace(tzinfo=self.utc):
                raise PasscodeIsExpired()

            user.is_active = True
            self.user_repo.save_user(user)
                
        else:
            raise OptPasswordIsntSet()
        
    def get_reset_token(self, input: GetResetTokenInput) -> PasswordResetTokenOutput:
        
        try: 
            user = self.user_repo.get_user_by_email(input.email)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with email={input.email} does not exist!')

        if user.requested_otp_password is not None:

            deadline = user.requested_otp_time + relativedelta(minutes=5)

            if input.confirm_code != user.requested_otp_password:
                raise WrongPasscode()

            if datetime.now().replace(tzinfo=self.utc) > deadline.replace(tzinfo=self.utc):
                raise PasscodeIsExpired()
        
            token = self.token_generator_usecase.generate_auth_token(user)

            if token is None:
                raise CannotGenerateToken()
            
            user.requested_token_time = datetime.now()
            self.user_repo.save_user(user)
            return PasswordResetTokenOutput(token= token)
                
        else:
            raise OptPasswordIsntSet()



    def reset_password(self, input: ResetPasswordInput) -> None:
        
        try: 
            user = self.user_repo.get_user_by_email(input.email)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with email={input.email} does not exist!')

        if user.requested_token_time is None:
            raise ResetTokenIsNotSet()

        deadline = user.requested_token_time + relativedelta(minutes=5)

        if datetime.now().replace(tzinfo=self.utc) > deadline.replace(tzinfo=self.utc):
            raise ResetTokenIsExpired()

        correct_token = self.token_generator_usecase.generate_auth_token(user)

        if correct_token != input.reset_token:
            raise WrongResetToken()

        user.set_password(input.new_password)
        self.user_repo.save_user(user)

        
