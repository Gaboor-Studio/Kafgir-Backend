from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr
from typing import List

from ...usecases.member.food_planning_usecases import MemberFoodPlanUsecase
from ...serializers.food_plan_serializers import FoodPlanInputSerializer
from ...dto.food_plan_dto import FoodPlanOutput, FoodPlanInput


class MemberFoodPlanView(ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    food_plan_serializer = FoodPlanInputSerializer

    @inject
    def __init__(self, member_food_plan_usecase: MemberFoodPlanUsecase = Provide['member_food_plan_usecase']):
        self.member_food_plan_usecase = member_food_plan_usecase

    def find_food_plan_by_date(self, request, start_date=None, end_date=None):
        outputs = self.member_food_plan_usecase.find_food_plan_by_date(id=request.user.id, start_date=start_date, end_date=end_date)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    def create_new_food_plan(self, request):
        seri = self.food_plan_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, FoodPlanInput)
            output = self.member_food_plan_usecase.add_new_food_plan(input=input,user=request.user)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def remove_food_plan(self, request, plan_id=None):
        self.member_food_plan_usecase.remove_food_plan(plan_id)
        return Response(data={}, status=status.HTTP_200_OK)
