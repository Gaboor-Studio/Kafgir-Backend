from rest_framework.decorators import api_view
from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
import cattr

from rest_framework.authtoken.views import ObtainAuthToken

from ...usecases.auth.authentication_usecase import AuthenticationUsecase
from ...serializers.auth_serializers import UserRegisterSerializer, SendEmailSerializer, VerifyEmailSerializer, GetResetTokenSerializer, ResetPasswordSerializer
from ...dto.auth_dto import UserRegisterInput, SendEmailInput, VerifyEmailInput, GetResetTokenInput, ResetPasswordInput

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
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(ObtainAuthToken):
    ''' A view for login users.\n
        /api/auth/login (POST)
    '''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class AuthenticationView(viewsets.ViewSet):

    @inject
    def __init__(self, authentication_usecase: AuthenticationUsecase = Provide['authentication_usecase'], **kwargs) -> None:
        self.authentication_usecase = authentication_usecase
        super().__init__(**kwargs)

    send_email_serializer = SendEmailSerializer
    verify_email_serializer = VerifyEmailSerializer
    get_reset_token_serializer = GetResetTokenSerializer
    reset_password_serializer = ResetPasswordSerializer


    def send_email(self, request):
        seri = self.send_email_serializer(data=request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, SendEmailInput)
            self.authentication_usecase.send_email(input)
            return Response(data={'message': 'email was successfully sent!'}, status=status.HTTP_200_OK)

        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def verify_email(self, request):
        seri = self.verify_email_serializer(data=request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, VerifyEmailInput)
            self.authentication_usecase.confirm_email(input)
            return Response(data={'message': 'your account was successfully activated!'}, status=status.HTTP_200_OK)

        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_reset_token(self, request):
        seri = self.get_reset_token_serializer(data= request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, GetResetTokenInput)
            output = self.authentication_usecase.get_reset_token(input)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def reset_password(self, request):
        seri = self.reset_password_serializer(data= request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, ResetPasswordInput)
            self.authentication_usecase.reset_password(input)
            return Response(data={'message': 'your password has been successfully changed'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)