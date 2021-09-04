from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.food_plan import FoodPlan
from ...models.user import User

from ...usecases.member.food_planning_usecases import MemberFoodPlanUsecase
from ...dto.food_plan_dto import FoodPlanOutput,FoodPlanInput
from ...repositories.food_planning_repo import FoodPlanningRepository
from ...mappers.food_plan_mapper import FoodPlanOutputMapper
from ...exceptions.not_found import FoodPlanNotFoundException

from datetime import date
from typing import List

class MemberFoodPlanService(MemberFoodPlanUsecase):

    @inject
    def __init__(self, food_plan_repo: FoodPlanningRepository = Provide['food_plan_repo'],
                       food_plan_output_mapper: FoodPlanOutputMapper = Provide['food_plan_output_mapper']):

        self.food_plan_repo = food_plan_repo
        self.food_plan_output_mapper = food_plan_output_mapper

    def find_food_plan_by_date(self, id: int, start_date: str, end_date: str) -> List[FoodPlanOutput]:
        inputs1 = start_date.split("-")
        start = date(int(inputs1[0]),int(inputs1[1]),int(inputs1[2]))
        inputs2 = end_date.split("-")
        end = date(int(inputs2[0]),int(inputs2[1]),int(inputs2[2]))
        food_plan = self.food_plan_repo.find_food_plan_by_date(id=id,start_date=start,end_date=end)
        return list(map(self.food_plan_output_mapper.from_model, food_plan))

    def add_new_food_plan(self, input: FoodPlanInput, user: User) -> None:
        inputs = input.date_time.split("-")
        date_time = date(int(inputs[0]),int(inputs[1]),int(inputs[2]))
        food_plan = FoodPlan(date_time=date_time, breakfast=input.breakfast, lunch=input.lunch, dinner=input.dinner, user=user)
        food_plan.save()
    
    def remove_food_plan(self, plan_id: int) -> None:
        self.food_plan_repo.delete_food_plan(plan_id)
