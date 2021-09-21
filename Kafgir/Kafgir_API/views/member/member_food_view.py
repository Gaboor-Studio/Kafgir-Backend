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
from ...dto.food_dto import FoodOutput, FoodBriefOutput

from drf_yasg.utils import swagger_auto_schema
from typing import List
import attr
from ...util.dto_util import dto_to_swagger_json_output


class MemberFoodView(ViewSet):


    authentication_classes = [TokenAuthentication]
    permission_classes = []

    food_serializer = FoodSerializer

    @inject
    def __init__(self, member_food_usecase: MemberFoodUsecase = Provide['member_food_usecase']):
        self.member_food_usecase = member_food_usecase

    @swagger_auto_schema(responses=dto_to_swagger_json_output(FoodOutput), tags=['member','food'])
    def get_one_food(self, request, food_id=None):
        ''' Gets informations of a food.'''

        output = self.member_food_usecase.find_by_id(food_id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None), tags=['member','food'])
    def add_ingredients_to_list(self, request, food_id=None):
        ''' Gets informations of a food.'''

        self.member_food_usecase.add_ingredients_to_list(food_id=food_id, user=request.user)
        return Response(data=None, status=status.HTTP_200_OK)


