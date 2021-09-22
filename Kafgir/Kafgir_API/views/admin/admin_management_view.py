from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ...usecases.admin.admin_management_usecases import AdminManagementUsecase 
from ...serializers.admin_management_serializer import AdminRegisterSerializer,AdminResetPasswordSerializer, AdminProfileUpdateSerializer
from ...dto.admin_management_dto import AdminBriefOutput,AdminOutput, AdminRegisterInput, AdminRegisterInput, AdminUpdateProfileInput, AdminSetPasswordInput
from ...util.dto_util import create_swagger_output
from ...util.view_util import validate
from ...util.paginator import PaginationData, PaginatorUtil

from drf_yasg.utils import swagger_auto_schema

from typing import List
import attr
import cattr

from dependency_injector.wiring import inject, Provide

class AdminManagementView(ViewSet):
    '''This is a view for managing admins in admin panel.'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @inject
    def __init__(self, admin_management_usecase: AdminManagementUsecase = Provide['admin_management_usecase']):
        self.admin_management_usecase = admin_management_usecase

    @swagger_auto_schema(responses=create_swagger_output(AdminOutput), tags=['admin', 'admin-management'])
    def get_admin(self, request, admin_id=None):
        '''GET: Gets informations of an admin.'''

        output = self.admin_management_usecase.find_admin(admin_id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(AdminBriefOutput, many=True, paginated=True), tags=['admin', 'admin-management'])
    def get_all_admins(self, request):
        '''GET: Gets list of all admins.'''

        pagination_data = PaginationData(request)
        outputs = self.admin_management_usecase.load_all_admins(pagination_data)
        outputs.data = list(map(cattr.unstructure, outputs.data))
        return Response(data=cattr.unstructure(outputs), status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AdminRegisterSerializer ,responses=create_swagger_output(AdminOutput), tags=['admin', 'admin-management'])
    @validate(AdminRegisterSerializer)
    def create_admin(self, request):
        '''POST: Gets a brief list of foods.'''

        input = cattr.structure(request.data, AdminRegisterInput)
        output = self.admin_management_usecase.create_admin(input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AdminProfileUpdateSerializer ,responses=create_swagger_output(AdminOutput), tags=['admin', 'admin-management'])
    @validate(AdminProfileUpdateSerializer)
    def update_admin(self, request, admin_id=None):
        '''PUT: Updates details of an admin'''

        input = cattr.structure(request.data, AdminUpdateProfileInput)
        output = self.admin_management_usecase.update_admin(admin_id, input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AdminResetPasswordSerializer ,responses=create_swagger_output(AdminOutput), tags=['admin', 'admin-management'])
    @validate(AdminResetPasswordSerializer)
    def update_admin_passsword(self, request, admin_id=None):
        '''PUT: Updates password of an admin'''

        input = cattr.structure(request.data, AdminSetPasswordInput)
        output = self.admin_management_usecase.set_password(admin_id, input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)


    @swagger_auto_schema(responses=create_swagger_output(None), tags=['admin', 'admin-management'])
    def delete_admin(self, request, admin_id=None):
        '''DELETE: Deletes a admin.'''

        self.admin_management_usecase.delete_admin(admin_id)
        return Response(data=None, status=status.HTTP_200_OK)
