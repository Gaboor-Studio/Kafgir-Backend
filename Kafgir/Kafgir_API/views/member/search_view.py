from dependency_injector.wiring import Provide, inject
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ...util.dto_util import dto_to_swagger_json_output
from drf_yasg.utils import swagger_auto_schema
import cattr
from typing import Any

from ...usecases.member.search_usecases import SearchUsecase

class SearchView(ViewSet):

    @inject
    def __init__(self, search_usecase: SearchUsecase = Provide['search_usecase'], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.search_usecase = search_usecase

    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def search_for_food(self, request):
        title = request.query_params.get('title')
        category_id = request.query_params.get('category')
        ingredient_string = request.query_params.get('ingredients')
        ingredients = ingredient_string.split('_') if ingredient_string is not None else None
        level = request.query_params.get('level')
        cooking_time = request.query_params.get('cooking_time')

        outputs = self.search_usecase.search_for_food(title, category_id, ingredients, level, cooking_time)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)