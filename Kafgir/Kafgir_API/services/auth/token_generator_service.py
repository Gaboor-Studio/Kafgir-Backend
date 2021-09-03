from dependency_injector.wiring import inject, Provide
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import hashlib

from ...usecases.auth.token_generator_usecase import TokenGeneratorUsecase
from ...repositories.user_repo import UserRepository
from ...exceptions.not_found import UserNotFoundException

class TokenGeneratorService(TokenGeneratorUsecase):

    @inject
    def __init__(self, user_repo: UserRepository = Provide['user_repo']) -> None:
        self.user_repo = user_repo
        super().__init__()

    model = get_user_model()

    def generate_auth_token(self, id: int) -> str:
        
        try: 
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with id={id} does not exist!')

        s = user.email + user.username + user.name

        return hashlib.sha1(s.encode("utf-8")).hexdigest()

    def generate_random_str(self, length: int) -> str:
        return get_random_string(length=length)