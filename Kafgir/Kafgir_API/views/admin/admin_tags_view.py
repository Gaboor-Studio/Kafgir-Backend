from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import cattr
from typing import List

from ...usecases.admin.admin_tag_usecases import AdminTagUsecase
from ...serializers.tag_serializers import TagInputSerializer 
from ...dto.tag_dto import TagInput,TagOutput

from drf_yasg.utils import swagger_auto_schema
import attr
from ...util.dto_util import create_swagger_output

class AdminTagView(ViewSet):
    '''This is a view for tag in admin side.'''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    tag_serializer = TagInputSerializer

    @inject
    def __init__(self, admin_tag_usecase: AdminTagUsecase = Provide['admin_tag_usecase']):
        self.admin_tag_usecase = admin_tag_usecase

    @swagger_auto_schema(responses=create_swagger_output(TagOutput, many=True), tags=['admin','tag'])
    def get_tags(self, request):
        ''' Gets all tags..'''

        outputs = self.admin_tag_usecase.find_all()
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=tag_serializer, responses=create_swagger_output(None), tags=['admin','tag','x'])    
    def create_new_tag(self, request):
        ''' Creates new tag.'''

        seri = self.tag_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, TagInput)
            output = self.admin_tag_usecase.create_new_tag(input=input)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=tag_serializer, responses=create_swagger_output(None), tags=['admin','tag'])
    def update_tag(self, request, tag_id=None):
        ''' updates tag.'''

        seri = self.tag_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, TagInput)
            self.admin_tag_usecase.update_tag(id=tag_id, input=input)
            return Response(status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(responses=create_swagger_output(None), tags=['admin','tag'])
    def remove_tag(self, request, tag_id=None):
        ''' Removes a tag.'''

        self.admin_tag_usecase.remove_tag(tag_id)
        return Response(data={}, status=status.HTTP_200_OK)
