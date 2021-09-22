from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import cattr
from typing import List

from ...usecases.member.member_food_usecases import MemberFoodUsecase
from ...serializers.food_serializers import FoodSerializer
from ...dto.food_dto import FoodOutput
from ...usecases.member.member_food_usecases import MemberFoodUsecase
from ...serializers.comment_serializer import CreateCommentSerializer, UpdateCommentSerializer
from ...dto.comment_dto import CommentBriefInput, CommentOutput, CommentInput


from drf_yasg.utils import swagger_auto_schema
from typing import List
import attr
from ...util.dto_util import dto_to_swagger_json_output


class MemberFoodView(ViewSet):


    authentication_classes = [TokenAuthentication]
    permission_classes = []

    food_serializer = FoodSerializer
    update_comment_serializer = UpdateCommentSerializer
    create_comment_serializer = CreateCommentSerializer

    @inject
    def __init__(self, member_food_usecase: MemberFoodUsecase = Provide['member_food_usecase']):
        self.member_food_usecase = member_food_usecase

    @swagger_auto_schema(responses=dto_to_swagger_json_output(FoodOutput))
    def get_one_food(self, request, food_id=None):
        ''' Gets informations of a food.'''
        if request.user.is_authenticated:
            outputs = self.member_food_usecase.find_by_id(user_id=request.user.id,food_id=food_id)
            serialized_outputs = cattr.unstructure(outputs)
            return Response(data=serialized_outputs, status=status.HTTP_200_OK)
 

        output = self.member_food_usecase.find_by_id(user_id=None,food_id=food_id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None))
    def add_ingredients_to_list(self, request, food_id=None):
        ''' add ingredients to list.'''

        self.member_food_usecase.add_ingredients_to_list(food_id=food_id, user=request.user)
        return Response(data=None, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(CommentOutput, many=True))
    def get_some_food_comments(self, request, food_id = None, number_of_comments = None):
        ''' receives the number of comments and sends the same number of comments.'''
        
        outputs = self.member_food_usecase.get_some_food_comments(food_id=food_id,num=number_of_comments)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(CommentOutput, many=True))
    def get_food_comments(self, request, food_id = None):
        ''' Gets all comments..'''
        
        outputs = self.member_food_usecase.get_food_comments(food_id=food_id)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=create_comment_serializer, responses=dto_to_swagger_json_output(None))    
    def create_new_comment(self, request):
        ''' Creates new comment.'''

        seri = self.create_comment_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentInput)
            output = self.member_food_usecase.add_comment(input=input,user=request.user)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=update_comment_serializer, responses=dto_to_swagger_json_output(None))    
    def update_comment(self, request, comment_id = None):
        ''' updates comment.'''

        seri = self.update_comment_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, CommentBriefInput)
            output = self.member_food_usecase.update_comment(input=input,comment_id=comment_id)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None))
    def remove_comment(self, request, comment_id=None):
        ''' Removes comment.'''

        self.member_food_usecase.remove_comment(comment_id=comment_id)
        return Response(data=None, status=status.HTTP_200_OK)