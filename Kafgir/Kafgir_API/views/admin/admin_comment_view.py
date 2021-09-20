from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import cattr
from typing import List

from ...usecases.admin.admin_comment_usecases import AdminCommentUsecase
from ...serializers.comment_serializer import CommentIdListSerializer, UpdateCommentSerializer
from ...dto.comment_dto import CommentBriefInput, CommentOutput, CommentInput, CommentIdListInput

from drf_yasg.utils import swagger_auto_schema
from typing import List
import attr
from ...util.dto_util import dto_to_swagger_json_output

class AdminCommentView(ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    update_comment_serializer = UpdateCommentSerializer
    commentid_list_serializer = CommentIdListSerializer

    @inject
    def __init__(self, admin_comment_usecase: AdminCommentUsecase = Provide['admin_comment_usecase']):
        self.admin_comment_usecase = admin_comment_usecase

    @swagger_auto_schema(responses=dto_to_swagger_json_output(CommentOutput, many=True))
    def get_some_unconfirmed_comments(self, request, num = None):
        ''' receives a number and sends the same number of unconfirmed comments.'''
        
        outputs = self.admin_comment_usecase.get_some_unconfirmed_comments(num=num)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None))    
    def confirm_the_comment(self, request, comment_id = None):
        ''' confirm the comment.'''

        output = self.admin_comment_usecase.confirm_the_comment(comment_id=comment_id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=commentid_list_serializer, responses=dto_to_swagger_json_output(None))    
    def confirm_comments(self, request):
        ''' receives a list of comments id and confirms them.'''

        seri = self.commentid_list_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentIdListInput)
            output = self.admin_comment_usecase.confirm_comments(comments=input)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(CommentOutput, many=True))
    def get_some_food_comments(self, request, food_id = None, num = None):
        ''' receives a number and sends the same number of comments.'''
        
        outputs = self.admin_comment_usecase.get_some_food_comments(food_id=food_id,num=num)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(CommentOutput, many=True))
    def get_food_comments(self, request, food_id = None):
        ''' Gets all comments..'''
        
        outputs = self.admin_comment_usecase.get_food_comments(food_id=food_id)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=update_comment_serializer, responses=dto_to_swagger_json_output(None))    
    def update_comment(self, request, comment_id = None):
        ''' updates comment.'''

        seri = self.update_comment_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentBriefInput)
            output = self.admin_comment_usecase.update_comment(input=input,comment_id=comment_id)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None))
    def remove_comment(self, request, comment_id=None):
        ''' Removes comment.'''

        self.admin_comment_usecase.remove_comment(comment_id=comment_id)
        return Response(data=None, status=status.HTTP_200_OK)
    
