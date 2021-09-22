from django.contrib.auth import get_user_model
import hashlib

from ...usecases.auth.generate_token_usecase import GenerateTokenUsecase
from ...exceptions.not_found import UserNotFoundException

class SHA1GenerateTokenService(GenerateTokenUsecase):

    model = get_user_model()

    def generate_token(self, user: model) -> str:
        ''' Generete token for the given user that is unique using sha1 algorithm'''
        
        if user is None:
            raise UserNotFoundException('cannot generate token for a user that does not exist!')

        s = user.email + user.username

        return hashlib.sha1(s.encode("utf-8")).hexdigest()