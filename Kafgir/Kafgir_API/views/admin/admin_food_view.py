from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from ...usecases.admin.admin_food_usecase import AdminFoodUsecase
from ...serializers.food_serializers import FoodSerializer
from ...dto.food_dto import FoodOutput,FoodBriefOutput,FoodInput
from ...util.paginator import PaginationData
from ...util.dto_util import create_swagger_output
from ...util.view_util import validate

from drf_yasg.utils import swagger_auto_schema

from typing import List

import cattr
import attr


class AdminFoodView(ViewSet):
    '''This is a view for food in admin side.'''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    @inject
    def __init__(self, admin_food_usecase: AdminFoodUsecase = Provide['admin_food_usecase']):
        self.admin_food_usecase = admin_food_usecase

    @swagger_auto_schema(responses=create_swagger_output(FoodOutput), tags=['admin','food'])
    def get_one_food(self, request, food_id=None):
        ''' Gets informations of a food.'''
        # Finding the food
        output = self.admin_food_usecase.find_by_id(food_id)

        # converting the output to json
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    
    @swagger_auto_schema(responses=create_swagger_output(FoodBriefOutput,many=True,paginated=True), tags=['admin','food'])
    def get_all_food(self, request):
        ''' Gets a brief list of foods.'''
        # Get pagination data from request
        pagination_data = PaginationData(request)
        
        # Load paginated list from the service
        outputs = self.admin_food_usecase.load_all(pagination_data)

        # Convert the data to Json
        outputs.data = list(map(cattr.unstructure,outputs.data))
        serialized_output = cattr.unstructure(outputs)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['admin','food'])
    def delete_food(self, request, food_id=None):
        ''' Deletes a food.'''
        self.admin_food_usecase.delete_by_id(food_id)
        return Response(data=None, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=FoodSerializer ,responses=create_swagger_output(FoodOutput), tags=['admin','food'])
    @validate(FoodSerializer)
    def create_food(self, request):
        ''' Creats a new food. Food ingredients will automatically be added to app ingredients. '''
        input = cattr.structure(request.data, FoodInput)
        output = self.admin_food_usecase.create_food(input)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)

