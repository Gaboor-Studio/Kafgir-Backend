from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr
from typing import List

from ...usecases.member.member_ingredient_usecases import MemberIngredientUsecase
from ...dto.ingredient_dto import IngredientOutput

from drf_yasg.utils import swagger_auto_schema
from typing import List
import attr
from ...util.dto_util import dto_to_swagger_json_output

class MemberIngredientView(ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @inject
    def __init__(self, member_ingredient_usecase: MemberIngredientUsecase = Provide['member_ingredient_usecase']):
        self.member_ingredient_usecase = member_ingredient_usecase

    @swagger_auto_schema(responses=dto_to_swagger_json_output(IngredientOutput, many=True), tags=['member','ingredient'])
    def get_ingredient_list(self, request):
        ''' Find all ingredients starting with name or gets all ingredient.'''
        
        name = request.query_params.get('name')

        if name is not None:
            outputs = self.member_ingredient_usecase.find_all_ingredients_starting_with_name(name=name)
            serialized_outputs = list(map(cattr.unstructure, outputs))
            return Response(data=serialized_outputs, status=status.HTTP_200_OK)

        outputs = self.member_ingredient_usecase.find_all_ingredient()
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

