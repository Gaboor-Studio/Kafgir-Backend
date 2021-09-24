from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr
from typing import List

from ...usecases.member.food_planning_usecases import MemberFoodPlanUsecase
from ...serializers.food_plan_serializers import FoodPlanInputSerializer , CreateFoodPlanInputSerializer
from ...dto.food_plan_dto import FoodPlanOutput, FoodPlanInput, FoodPlanBriefInput
from ...exceptions.bad_request import StartDateMissingException, EndtDateMissingException

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import attr
from ...util.dto_util import create_swagger_output

## to be used in swagger_auto_schema as manual_parameters
test_param=[
    openapi.Parameter('start_date', openapi.IN_QUERY, 'the start date of the meal plan.', required=True, type=openapi.TYPE_INTEGER),
    openapi.Parameter('end_date', openapi.IN_QUERY, 'the end date of the meal plan.', required=True, type=openapi.TYPE_INTEGER),
]


class MemberFoodPlanView(ViewSet):
    '''This is a view for food plan in client side.'''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    food_plan_serializer = FoodPlanInputSerializer
    create_food_plan_serializer = CreateFoodPlanInputSerializer

    @inject
    def __init__(self, member_food_plan_usecase: MemberFoodPlanUsecase = Provide['member_food_plan_usecase']):
        self.member_food_plan_usecase = member_food_plan_usecase

    @swagger_auto_schema(manual_parameters=test_param, responses=create_swagger_output(FoodPlanOutput, many=True), tags=['member','food-plan'])
    def find_food_plan_by_date(self, request): 
        '''This method returns the meal plan by getting the start and end dates .'''
       
        start_date = request.GET.get('start_date')        
        if start_date is None:
            raise StartDateMissingException()
        
        end_date = request.GET.get('end_date')        
        if end_date is None:
            raise EndtDateMissingException()

        outputs = self.member_food_plan_usecase.find_food_plan_by_date(id=request.user.id, start_date=start_date, end_date=end_date)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=create_food_plan_serializer, responses=create_swagger_output(None), tags=['member','food-plan'])    
    def create_new_food_plan(self, request):
        '''Creates food plan .'''

        seri = self.create_food_plan_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, FoodPlanInput)
            output = self.member_food_plan_usecase.add_new_food_plan(input=input,user=request.user)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=food_plan_serializer, responses=create_swagger_output(None), tags=['member','food-plan'])
    def update_food_plan(self, request, plan_id=None):
        ''' Updates a food plan .'''

        seri = self.food_plan_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, FoodPlanBriefInput)
            self.member_food_plan_usecase.update_food_plan(plan_id=plan_id, input=input)
            return Response(status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member','food-plan'])
    def remove_food_plan(self, request, plan_id=None):
        '''removes a food plan .'''

        self.member_food_plan_usecase.remove_food_plan(plan_id)
        return Response(data={}, status=status.HTTP_200_OK)
