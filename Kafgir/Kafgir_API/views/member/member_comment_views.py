from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr
from typing import List

from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...serializers.comment_serializer import CreateCommentSerializer, UpdateCommentSerializer
from ...dto.comment_dto import CommentBriefInput, CommentOutput, CommentInput

from drf_yasg.utils import swagger_auto_schema
from typing import List
import attr
from ...util.dto_util import create_swagger_output

class MemberCommentView(ViewSet):

    authentication_classes = [TokenAuthentication]

    update_comment_serializer = UpdateCommentSerializer
    create_comment_serializer = CreateCommentSerializer

    @inject
    def __init__(self, member_comment_usecase: MemberCommentUsecase = Provide['member_comment_usecase']):
        self.member_comment_usecase = member_comment_usecase

    @swagger_auto_schema(responses=create_swagger_output(CommentOutput, many=True))
    def get_some_food_comments(self, request, food_id = None, num = None):
        ''' receives the number of comments and sends the same number of comments.'''
        
        outputs = self.member_comment_usecase.get_some_food_comments(food_id=food_id,num=num)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(CommentOutput, many=True))
    def get_food_comments(self, request, food_id = None):
        ''' Gets all comments..'''
        
        outputs = self.member_comment_usecase.get_food_comments(food_id=food_id)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)


    @swagger_auto_schema(responses=create_swagger_output(CommentOutput))
    def get_comment_by_user_id(self, request, food_id = None):
        ''' If there is a comment with this userid then it will send it.'''
        if request.user.is_authenticated:
            outputs = self.member_comment_usecase.find_comment_by_user_id(id=request.user.id,food_id=food_id)
            if not outputs==None :
                serialized_outputs = cattr.unstructure(outputs)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            return Response(data={}, status=status.HTTP_200_OK)    

    @swagger_auto_schema(request_body=create_comment_serializer, responses=create_swagger_output(None))    
    def create_new_comment(self, request):
        ''' Creates new comment.'''

        seri = self.create_comment_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentInput)
            output = self.member_comment_usecase.add_comment(input=input,user=request.user)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=update_comment_serializer, responses=create_swagger_output(None))    
    def update_comment(self, request, comment_id = None):
        ''' updates comment.'''

        seri = self.update_comment_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentBriefInput)
            output = self.member_comment_usecase.update_comment(input=input,comment_id=comment_id)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=create_swagger_output(None))
    def remove_comment(self, request, comment_id=None):
        ''' Removes comment.'''

        self.member_comment_usecase.remove_comment(comment_id=comment_id)
        return Response(data=None, status=status.HTTP_200_OK)
    
