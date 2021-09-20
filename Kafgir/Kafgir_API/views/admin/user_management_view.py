import cattr
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ...usecases.admin.user_management_usecases import UserManagementUsecase 
from ...serializers.user_management_serializer import UserManagementCreateProfileSerializer, UserManagementEditProfileSerializer \
                                                    , UserManagementSetPasswordSerializer, UserManagementSetPfpSerializer
from ...dto.user_management_dto import UserManagementCreateProfileInput, UserManagementEditProfileInput \
                                        , UserManagementSetPasswordInput, UserManagementSetPfpInput, UserManagementProfileOutput
from ...util.dto_util import dto_to_swagger_json_output
from ...util.view_util import validate

from drf_yasg.utils import swagger_auto_schema

from typing import List, Any

from dependency_injector.wiring import inject, Provide

class UserManagementView(ViewSet):
    ''' this view creates user management APIs for admins to use'''

    @inject
    def __init__(self, user_management_usecase: UserManagementUsecase = Provide['user_management_usecase'], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user_management_usecase= user_management_usecase

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(responses=dto_to_swagger_json_output(UserManagementProfileOutput, many=True), tags=['admin', 'user-management'])
    def get_users(self, request):
        '''GET: get list of all non-admin users'''
        output = self.user_management_usecase.get_users_list()
        serializer_output = cattr.unstructure(output)
        return Response(data=serializer_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserManagementCreateProfileSerializer, responses=dto_to_swagger_json_output(UserManagementProfileOutput), tags=['admin', 'user-management'])
    @validate(UserManagementCreateProfileSerializer)
    def create_user(self, request):
        '''POST: creates a new non-admin user'''
        input= cattr.structure(request.data, UserManagementCreateProfileInput)
        output= self.user_management_usecase.create_user(input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserManagementEditProfileSerializer, responses=dto_to_swagger_json_output(UserManagementProfileOutput), tags=['admin', 'user-management'])
    @validate(UserManagementEditProfileSerializer)
    def edit_user(self, request, id=None):
        '''PUT: edits the user with the given id'''
        input= cattr.structure(request.data, UserManagementEditProfileInput)
        output= self.user_management_usecase.edit_user(id, input)
        serialized_output= cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None), tags=['admin', 'user-management'])
    def delete_user(self, request, id=None):
        '''DELETE: deletes the user with the given id'''
        self.user_management_usecase.delete_user(id)
        return Response(data={'message': 'user has been successfully deleted!'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserManagementSetPasswordSerializer, responses=dto_to_swagger_json_output(None), tags=['admin', 'user-management'])
    @validate(UserManagementSetPasswordSerializer)
    def set_user_password(self, request, id=None):
        '''POST: sets password for the user with the given id'''
        input= cattr.structure(request.data, UserManagementSetPasswordInput)
        self.user_management_usecase.set_user_password(id, input)
        return Response(data={'message': 'user\'s password has been successfully changed!'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserManagementSetPfpSerializer, responses=dto_to_swagger_json_output(None), tags=['admin', 'user-management'])
    @validate(UserManagementSetPfpSerializer)
    def set_user_picture(self, request, id=None):
        '''POST: sets profile picture of the user with the given id'''
        input= cattr.structure(request.data, UserManagementSetPfpInput)
        self.user_management_usecase.set_user_pfp(id, input)
        return Response(data={'message': 'user\'s profile picture has been successfully changed!'})
