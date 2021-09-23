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
from drf_yasg import openapi
import attr
from ...util.dto_util import create_swagger_output

## to be used in swagger_auto_schema as manual_parameters
test_param=[
    openapi.Parameter('number_of_foods', openapi.IN_QUERY, 'the number of food we need in the main tag.', type=openapi.TYPE_INTEGER),
]

class MemberHomePageView(ViewSet):

    authentication_classes = [TokenAuthentication]

    @inject
    def __init__(self, member_home_page_usecase: MemberHomePageUsecase = Provide['member_home_page_usecase']):
        self.member_home_page_usecase = member_home_page_usecase

    @swagger_auto_schema(manual_parameters=test_param, responses=create_swagger_output(HomePageOutput), tags=['member','home-page'])
    def load_home_page(self, request):
        ''' Gets food plan, main tags and categories.'''
        
        number_of_foods = request.GET.get('number_of_foods')        

        if number_of_foods is not None:
            if request.user.is_authenticated:
                output = self.member_home_page_usecase.load_home_page(id=request.user.id,num=number_of_foods)
                serialized_outputs = attr.asdict(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            else:
                output = self.member_home_page_usecase.load_home_page(id=None,num=number_of_foods)
                serialized_outputs = attr.asdict(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
        else:
            if request.user.is_authenticated:
                output = self.member_home_page_usecase.load_home_page(id=request.user.id,num=6)
                serialized_outputs = attr.asdict(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)
            else:
                output = self.member_home_page_usecase.load_home_page(id=None,num=6)
                serialized_outputs = attr.asdict(output)
                return Response(data=serialized_outputs, status=status.HTTP_200_OK)