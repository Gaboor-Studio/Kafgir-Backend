from dependency_injector.wiring import inject, Provide
from django.core import paginator
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import cattr
from typing import List

from ...usecases.admin.admin_comment_usecases import AdminCommentUsecase
from ...serializers.comment_serializer import CommentIdListSerializer, UpdateCommentSerializer
from ...dto.comment_dto import CommentInput, CommentOutput, CommentIdListInput, CommentBriefOutput

from drf_yasg.utils import swagger_auto_schema
from typing import List
from ...util.dto_util import create_swagger_output
from ...util.paginator import PaginationData
from ...util.view_util import validate

from drf_yasg import openapi

## to be used in swagger_auto_schema as manual_parameters
confirmed_param=[
    openapi.Parameter('confirmed', openapi.IN_QUERY, 'is comment confirmed or not.', required=False, type=openapi.TYPE_BOOLEAN, default=False)
]


class AdminCommentView(ViewSet):
    '''This is a view for comment in admin side.'''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    update_comment_serializer = UpdateCommentSerializer
    commentid_list_serializer = CommentIdListSerializer

    @inject
    def __init__(self, admin_comment_usecase: AdminCommentUsecase = Provide['admin_comment_usecase']):
        self.admin_comment_usecase = admin_comment_usecase

    @swagger_auto_schema(manual_parameters=confirmed_param,responses=create_swagger_output(CommentBriefOutput, many=True, paginated=True), tags=['admin','comment'])
    def get_comments(self, request):
        ''' receives a number and sends the same number of unconfirmed comments.'''
        # Get confirmed query params. default = false
        confirmed = request.GET.get('confirmed', False)

        # Get pagination data
        pagination_data = PaginationData(request)

        outputs = self.admin_comment_usecase.get_comments_by_confirmed(confirmed, pagination_data)
        outputs.data = list(map(cattr.unstructure, outputs.data))
        
        return Response(data=cattr.unstructure(outputs), status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['admin','comment'])    
    def confirm_the_comment(self, request, comment_id = None):
        ''' confirm the comment.'''
        output = self.admin_comment_usecase.confirm_the_comment(comment_id=comment_id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=commentid_list_serializer, responses=create_swagger_output(None), tags=['admin','comment'])    
    @validate(CommentIdListSerializer)
    def confirm_comments(self, request):
        ''' receives a list of comments id and confirms them.'''
        input = cattr.structure(request.data, CommentIdListInput)
        output = self.admin_comment_usecase.confirm_comments(comments=input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=update_comment_serializer, responses=create_swagger_output(None), tags=['admin','comment'])    
    @validate(UpdateCommentSerializer)
    def update_comment(self, request, comment_id = None):
        ''' updates comment.'''
        input = cattr.structure(request.data, CommentInput)
        output = self.admin_comment_usecase.update_comment(input=input,comment_id=comment_id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)
        
    @swagger_auto_schema(responses=create_swagger_output(None), tags=['admin','comment'])
    def remove_comment(self, request, comment_id=None):
        ''' Removes comment.'''
        self.admin_comment_usecase.remove_comment(comment_id=comment_id)
        return Response(data=None, status=status.HTTP_200_OK)
    
