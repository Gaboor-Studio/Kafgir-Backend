from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import hashlib

from ...usecases.auth.token_generator_usecase import TokenGeneratorUsecase
from ...exceptions.not_found import UserNotFoundException

class TokenGeneratorService(TokenGeneratorUsecase):

    model = get_user_model()

    def generate_auth_token(self, user: model) -> str:
        
        if user is None:
            raise UserNotFoundException('cannot generate token for a user that does not exist!')

        s = user.email + user.username + user.name

        return hashlib.sha1(s.encode("utf-8")).hexdigest()

    def generate_random_str(self, length: int) -> str:
        return get_random_string(length=length)