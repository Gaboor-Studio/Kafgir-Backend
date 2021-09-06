from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr

from ...usecases.member.member_home_page import MemberHomePageUsecase
from ...dto.home_page_dto import HomePageOutput

from drf_yasg.utils import swagger_auto_schema
import attr
from ...util.dto_util import dto_to_swagger_json_output

class MemberHomePageView(ViewSet):

    @inject
    def __init__(self, member_home_page_usecase: MemberHomePageUsecase = Provide['member_home_page_usecase']):
        self.member_home_page_usecase = member_home_page_usecase

    @swagger_auto_schema(responses=dto_to_swagger_json_output(HomePageOutput))
    def load_home_page(self, request):
        ''' Gets food plan, main tags and categories.'''
        number_of_foods = request.query_params.get('number_of_foods')
    
        if number_of_foods is not None:
            if request.user.is_authenticated:
                outputs = self.member_home_page_usecase.load_home_page_for_user(id=request.user.id,num=number_of_foods)
                serialized_outputs = list(map(cattr.unstructure, outputs))
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            else:
                outputs = self.member_home_page_usecase.load_home_page_for_guest(num=number_of_foods)
                serialized_outputs = list(map(cattr.unstructure, outputs))
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
        else:
            if request.user.is_authenticated:
                outputs = self.member_home_page_usecase.load_home_page_for_user(id=request.user.id,num=6)
                serialized_outputs = list(map(cattr.unstructure, outputs))
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            else:
                outputs = self.member_home_page_usecase.load_home_page_for_guest(num=6)
                serialized_outputs = list(map(cattr.unstructure, outputs))
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)