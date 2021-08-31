from dependency_injector.wiring import inject, Provide
from django.contrib.auth import get_user_model

from ...dto.auth_dto import UserRegisterInput
from ...usecases.auth.authentication_usecases import AuthenticationUsecase
from ...exceptions.bad_request import UserAlreadyExistsException
from ...repositories.user_repo import UserRepository

class AuthenticationService(AuthenticationUsecase):

    model = get_user_model()

    @inject
    def __init__(self, user_repo: UserRepository = Provide['user_repo']):
        self.user_repo = user_repo
    
    def register_user(self, input: UserRegisterInput) -> None:
        
        if self.user_repo.exist_user_by_email(input.email):
            raise UserAlreadyExistsException(detail=f'User(email={input.email}) already exists!')

        user = self.model.objects.create_user(
            username=input.username, email=input.email, name=input.name, last_name=input.last_name, password=input.password)

        self.user_repo.save_user(user)
