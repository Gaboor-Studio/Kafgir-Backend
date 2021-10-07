from attr import attr
from dependency_injector.wiring import inject, Provide

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...serializers.comment_serializer import UpdateCommentSerializer
from ...dto.comment_dto import CommentInput
from ...util.view_util import validate

from drf_yasg.utils import swagger_auto_schema

import cattr

from ...util.dto_util import create_swagger_output

class MemberCommentView(ViewSet):
    '''This is a view for comments in client side.'''

    authentication_classes = [TokenAuthentication]
    permission_classes = []

    update_comment_serializer = UpdateCommentSerializer

    @inject
    def __init__(self, member_comment_usecase: MemberCommentUsecase = Provide['member_comment_usecase']):
        self.member_comment_usecase = member_comment_usecase

    @swagger_auto_schema(request_body=update_comment_serializer, responses=create_swagger_output(None), tags=['member','food'])    
    @validate(UpdateCommentSerializer)
    def update_comment(self, request, comment_id = None):
        ''' updates comment.'''
        input = cattr.structure(request.data, CommentInput)
        output = self.member_comment_usecase.update_comment(comment_id, input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)
        

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member','food'])
    def remove_comment(self, request, comment_id=None):
        ''' Removes comment.'''
        self.member_comment_usecase.remove_comment(comment_id)
        return Response(data=None, status=status.HTTP_200_OK)