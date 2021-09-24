from attr import attr
from dependency_injector.wiring import inject, Provide

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...serializers.comment_serializer import UpdateCommentSerializer
from ...dto.comment_dto import CommentBriefInput


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import attr , cattr

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
    #TODO: use @validate here
    def update_comment(self, request, comment_id = None):
        ''' updates comment.'''

        seri = self.update_comment_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentBriefInput)
            output = self.member_comment_usecase.update_comment(input=input,comment_id=comment_id)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member','food'])
    def remove_comment(self, request, comment_id=None):
        ''' Removes comment.'''

        self.member_comment_usecase.remove_comment(comment_id=comment_id)
        return Response(data=None, status=status.HTTP_200_OK)