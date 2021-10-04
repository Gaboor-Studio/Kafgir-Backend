from dependency_injector.wiring import Provide, inject
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ...util.dto_util import create_swagger_output
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import cattr
from typing import Any

from ...usecases.member.search_usecases import SearchUsecase
from ...dto.food_dto import FoodBriefOutput

## to be used in swagger_auto_schema as manual_parameters
test_param=[
    openapi.Parameter('title', openapi.IN_QUERY, 'to look in title of the foods', required=True, type=openapi.TYPE_STRING),
    openapi.Parameter('category', openapi.IN_QUERY, 'id of category we\'re searching in', required=False, type=openapi.TYPE_INTEGER),
    openapi.Parameter('ingredients', openapi.IN_QUERY, 'array of ingredients that should be in the food with "_" between each pair. e.g: karafs_soosis', required=False, type=openapi.TYPE_STRING),
    openapi.Parameter('level', openapi.IN_QUERY, 'level of food. <=3 >0', required=False, type=openapi.TYPE_INTEGER),
    openapi.Parameter('cooking_time', openapi.IN_QUERY, 'expected cooking time', required=False, type=openapi.TYPE_INTEGER),
]

class SearchView(ViewSet):
    ''' This class represents a viewset that member uses to search through app's database'''

    @inject
    def __init__(self, search_usecase: SearchUsecase = Provide['search_usecase'], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.search_usecase = search_usecase

    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=test_param, responses=create_swagger_output(FoodBriefOutput, many=True))
    def search_for_food(self, request):
        ''' This method returns a list of foods which are true in the conditions that user defined in the request '''

        title = request.query_params.get('title')
        category_id = request.query_params.get('category')
        ingredient_string = request.query_params.get('ingredients')
        ingredients = ingredient_string.split('_') if ingredient_string is not None else None
        level = request.query_params.get('level')
        cooking_time = request.query_params.get('cooking_time')

        outputs = self.search_usecase.search_for_food(request.user ,title, category_id, ingredients, level, cooking_time)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)