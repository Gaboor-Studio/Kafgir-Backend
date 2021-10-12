from attr import attr
from dependency_injector.wiring import inject, Provide

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...usecases.member.member_food_usecase import MemberFoodUsecase
from ...serializers.food_serializers import FoodSerializer
from ...dto.food_dto import FoodOutput
from ...usecases.member.member_food_usecase import MemberFoodUsecase
from ...serializers.comment_serializer import CreateCommentSerializer, UpdateCommentSerializer
from ...dto.comment_dto import CommentOutput, CommentInput
from ...dto.food_dto import FoodOutput, FoodBriefOutput
from ...exceptions.bad_request import TagIdMissingException
from ...util.view_util import validate
from ...util.paginator import PaginationData

from ...models.food import Food

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import attr , cattr
from typing import List

from ...util.dto_util import create_swagger_output

## to be used in swagger_auto_schema as manual_parameters
test_param=[
    openapi.Parameter('tagId', openapi.IN_QUERY, 'The tag id which the foods are in it.', required=True, type=openapi.TYPE_INTEGER),
]

class MemberFoodView(ViewSet):
    '''This is a view for foods in client side.'''

    authentication_classes = [TokenAuthentication]
    permission_classes = []

    food_serializer = FoodSerializer
    update_comment_serializer = UpdateCommentSerializer
    create_comment_serializer = CreateCommentSerializer

    @inject
    def __init__(self, member_food_usecase: MemberFoodUsecase = Provide['member_food_usecase'], member_comment_usecase: MemberCommentUsecase = Provide['member_comment_usecase']):
        self.member_food_usecase = member_food_usecase
        self.member_comment_usecase = member_comment_usecase

    @swagger_auto_schema(responses=create_swagger_output(FoodOutput), tags=['member','food'])
    def get_one_food(self, request, food_id=None):
        ''' Gets informations of a food.'''
        # Finding user id if exists
        user_id = request.user.id if request.user.is_authenticated else None

        #Get pagination data of comments from the request
        pagination_data = PaginationData(request)

        # Finding the food
        output = self.member_food_usecase.find_by_id(user_id=user_id,food_id=food_id,pagination_data=pagination_data)
        
        # Converting to JSON. here we used attr.asdict because the comment field of the food can be null.
        serialized_output = attr.asdict(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member','food'])
    def add_ingredients_to_list(self, request, food_id=None):
        ''' add ingredients to list.'''
        self.member_food_usecase.add_ingredients_to_list(food_id=food_id, user=request.user)
        return Response(data=None, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(CommentOutput, many=True, paginated=True), tags=['member','food'])
    def get_food_comments(self, request, food_id = None):
        ''' Gets all comments paginated.'''
        # Get pagination data from request
        pagination_data = PaginationData(request)

        outputs = self.member_comment_usecase.get_all_comments_of_model(Food, food_id, pagination_data)
        serialized_outputs = list(map(cattr.unstructure, outputs.data))
        return Response(data=cattr.unstructure(serialized_outputs), status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=create_comment_serializer, responses=create_swagger_output(None), tags=['member','food'])    
    @validate(CreateCommentSerializer)
    def create_new_comment(self, request, food_id=None):
        ''' Creates new comment.'''
        input = cattr.structure(request.data, CommentInput)
        output = self.member_comment_usecase.add_comment(Food, food_id, request.user, input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=test_param, responses=create_swagger_output(FoodBriefOutput, many=True, paginated=True), tags=['member','food'])
    def get_all_foods_with_tag(self, request):
        ''' Gets all foods in a tag. Receives in paginated form .'''
        # Checking if tagId is in query params
        tag_id = request.GET.get('tagId')        
        if tag_id is None:
            raise TagIdMissingException()
        
        # Get pagination data from request
        pagination_data = PaginationData(request)

        outputs = self.member_food_usecase.find_all_with_tag(tag_id, pagination_data)
        serialized_outputs = list(map(cattr.unstructure, outputs.data))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema( responses=create_swagger_output(FoodBriefOutput, many=True, paginated=True), tags=['member','food'])
    def get_favorite_foods(self, request):
        ''' Gets all favorite foods paginated .'''

        # Get pagination data from request
        pagination_data = PaginationData(request)
        
        if request.user.is_authenticated:
            # Finding user
            user_id = request.user.id

            outputs = self.member_food_usecase.find_favorite_foods(user_id, pagination_data)
            serialized_outputs = list(map(cattr.unstructure, outputs.data))
            return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member','food'])
    def add_favorite_food(self, request, food_id=None):
        '''Adds a favorite food to user'''

        if request.user.is_authenticated:
            # Finding user
            user_id = request.user.id

            self.member_food_usecase.add_favorite_food(food_id=food_id, user_id=user_id)
            return Response(data=None, status=status.HTTP_200_OK)