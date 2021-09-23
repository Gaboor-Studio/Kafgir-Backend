from rest_framework.decorators import api_view
from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
from ...util.dto_util import create_swagger_output
from drf_yasg.utils import swagger_auto_schema
import cattr

from rest_framework.authtoken.views import ObtainAuthToken

from ...usecases.auth.authentication_usecase import AuthenticationUsecase
from ...serializers.auth_serializers import UserRegisterSerializer, SendEmailSerializer, VerifyEmailSerializer, GetResetTokenSerializer, ResetPasswordSerializer
from ...dto.auth_dto import UserRegisterInput, SendEmailInput, VerifyEmailInput, GetResetTokenInput, ResetPasswordInput, PasswordResetTokenOutput

class LoginApiView(ObtainAuthToken):
    ''' A view for login users.\n
        /api/auth/login (POST)
    '''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class AuthenticationView(viewsets.ViewSet):
    ''' This class is a view where user has access to sign up an other authentication APIs'''

    @inject
    def __init__(self, authentication_usecase: AuthenticationUsecase = Provide['authentication_usecase'], **kwargs) -> None:
        self.authentication_usecase = authentication_usecase
        super().__init__(**kwargs)

    send_email_serializer = SendEmailSerializer
    verify_email_serializer = VerifyEmailSerializer
    get_reset_token_serializer = GetResetTokenSerializer
    reset_password_serializer = ResetPasswordSerializer

    @swagger_auto_schema(request_body=UserRegisterSerializer, responses=create_swagger_output(None), tags=['auth','authentication']) 
    def register_view(self, request):
        ''' This is a view for registering user '''
        seri = UserRegisterSerializer(data=request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, UserRegisterInput)
            self.authentication_usecase.register_user(input)
            return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=send_email_serializer, responses=create_swagger_output(None), tags=['auth','authentication'])  
    def send_email(self, request):
        ''' sends an email to the user's email that contains a 5 digit code that could be used for resetting the password or activating the account'''

        seri = self.send_email_serializer(data=request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, SendEmailInput)
            self.authentication_usecase.send_email(input)
            return Response(data={'message': 'email was successfully sent!'}, status=status.HTTP_200_OK)

        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=verify_email_serializer, responses=create_swagger_output(None), tags=['auth','authentication'])  
    def verify_email(self, request):
        ''' given the 5 digit code as input, it activates the user's account '''

        seri = self.verify_email_serializer(data=request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, VerifyEmailInput)
            self.authentication_usecase.confirm_email(input)
            return Response(data={'message': 'your account was successfully activated!'}, status=status.HTTP_200_OK)

        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=get_reset_token_serializer, responses=create_swagger_output(PasswordResetTokenOutput), tags=['auth','authentication'])
    def get_reset_token(self, request):
        ''' given the 5 digit code as input, responses with the user's token that could be used to resetting the password '''

        seri = self.get_reset_token_serializer(data= request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, GetResetTokenInput)
            output = self.authentication_usecase.get_reset_token(input)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=reset_password_serializer, responses=create_swagger_output(None), tags=['auth','authentication'])
    def reset_password(self, request):
        ''' given the user's token as input, resets user's password to the given new password '''

        seri = self.reset_password_serializer(data= request.data)

        if seri.is_valid():
            input = cattr.structure(request.data, ResetPasswordInput)
            self.authentication_usecase.reset_password(input)
            return Response(data={'message': 'your password has been successfully changed'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)