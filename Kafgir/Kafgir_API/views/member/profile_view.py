from dependency_injector.wiring import Provide, inject
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from ...util.dto_util import create_swagger_output
from drf_yasg.utils import swagger_auto_schema
import cattr
from typing import Any

from ...usecases.member.profile_usecase import ProfileUsecase
from ...dto.profile_dto import ProfileInput, ProfileOutput, ProfileSetPictureInput, ProfilePasswordChangeInput
from ...serializers.profile_serializer import ProfileSerializer, ProfileSetPictureSerializer, ProfilePasswordChangeSerializer

class ProfileView(ViewSet):
    ''' This class is a viewset where user has access to it's own profile APIs'''

    @inject
    def __init__(self, profile_usecase: ProfileUsecase = Provide['profile_usecase'], **kwargs: Any) -> None:
        self.profile_usecase = profile_usecase
        super().__init__(**kwargs)

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    profile_serializer = ProfileSerializer
    profile_set_picture_serializer = ProfileSetPictureSerializer
    profile_password_change_serializer = ProfilePasswordChangeSerializer

    @swagger_auto_schema(responses=create_swagger_output(ProfileOutput), tags=['member','profile'])
    def get_profile(self, request):
        ''' get user profile's details '''
        id = request.user.id
        output = self.profile_usecase.get_profile(id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=profile_password_change_serializer, responses=create_swagger_output(None), tags=['member','profile'])
    def change_password(self, request):
        ''' change user password having the user's old password, new password and it's repeat '''

        seri = self.profile_password_change_serializer(data= request.data)

        if seri.is_valid():
            id = request.user.id
            input = cattr.structure(request.data, ProfilePasswordChangeInput)
            self.profile_usecase.change_password(id, input)
            return Response(data={'message': 'your password has been successfully changed'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=profile_serializer, responses=create_swagger_output(ProfileOutput), tags=['member','profile'])
    def edit_profile(self, request):
        ''' edit user's name and last name (no change of email for now) '''

        seri = self.profile_serializer(data= request.data)

        if seri.is_valid():
            id = request.user.id
            input = cattr.structure(request.data, ProfileInput)
            output = self.profile_usecase.edit_profile(id, input)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=profile_set_picture_serializer, responses=create_swagger_output(None), tags=['member','profile'])
    def set_picture(self, request):
        ''' set user's profile picture '''

        seri = self.profile_set_picture_serializer(data= request.data)

        if seri.is_valid():
            id = request.user.id
            input = cattr.structure(request.data, ProfileSetPictureInput)
            self.profile_usecase.set_photo(id, input)
            return Response(data={'message': 'your profile picture has been set successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member','profile'])
    def log_out(self, request):
        ''' log out of the account '''

        id = request.user.id
        self.profile_usecase.logout(id)
        return Response(data={'message': 'logged out of the account successfully'}, status=status.HTTP_200_OK)

