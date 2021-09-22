from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
import cattr

from ...usecases.member.member_home_page import MemberHomePageUsecase
from ...dto.home_page_dto import HomePageOutput

from drf_yasg.utils import swagger_auto_schema
import attr
from ...util.dto_util import create_swagger_output

class MemberHomePageView(ViewSet):

    authentication_classes = [JWTAuthentication]

    @inject
    def __init__(self, member_home_page_usecase: MemberHomePageUsecase = Provide['member_home_page_usecase']):
        self.member_home_page_usecase = member_home_page_usecase

    @swagger_auto_schema(responses=create_swagger_output(HomePageOutput), tags=['member','home-page'])
    def load_home_page(self, request):
        ''' Gets food plan, main tags and categories.'''
        number_of_foods = request.query_params.get('number_of_foods')
    
        if number_of_foods is not None:
            if request.user.is_authenticated:
                output = self.member_home_page_usecase.load_home_page(id=request.user.id,num=number_of_foods)
                serialized_outputs = cattr.unstructure(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            else:
                output = self.member_home_page_usecase.load_home_page(id=None,num=number_of_foods)
                serialized_outputs = cattr.unstructure(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
        else:
            if request.user.is_authenticated:
                output = self.member_home_page_usecase.load_home_page(id=request.user.id,num=6)
                serialized_outputs = cattr.unstructure(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            else:
                output = self.member_home_page_usecase.load_home_page(id=None,num=6)
                serialized_outputs = cattr.unstructure(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)