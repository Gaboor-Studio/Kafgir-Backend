from rest_framework.decorators import api_view
from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.response import Response
import cattr

from rest_framework.authtoken.views import ObtainAuthToken

from ...usecases.auth.authentication_usecases import AuthenticationUsecase
from ...serializers.auth_serializers import UserRegisterSerializer
from ...dto.auth_dto import UserRegisterInput
from ...exceptions.common import ValidationError

@api_view(['POST'])
@inject
def register_view(request, authentication_usecase: AuthenticationUsecase = Provide['authentication_usecase']):
    ''' This is a view for registering user '''
    seri = UserRegisterSerializer(data=request.data)

    if seri.is_valid():
        input = cattr.structure(request.data, UserRegisterInput)
        authentication_usecase.register_user(input)
        return Response(data={}, status=status.HTTP_200_OK)
    else:
        return ValidationError()


class LoginApiView(ObtainAuthToken):
    ''' A view for login users.\n
        /api/auth/login (POST)
    '''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
