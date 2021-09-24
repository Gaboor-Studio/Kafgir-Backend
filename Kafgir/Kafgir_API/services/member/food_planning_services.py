from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.food_plan import FoodPlan
from ...models.user import User

from ...usecases.member.food_planning_usecases import MemberFoodPlanUsecase
from ...dto.food_plan_dto import FoodPlanInput,FoodPlanOutput,FoodPlanBriefInput
from ...repositories.food_planning_repo import FoodPlanningRepository
from ...repositories.food_repo import FoodRepository
from ...mappers.food_plan_mapper import FoodPlanOutputMapper
from ...exceptions.not_found import FoodPlanNotFoundException

from datetime import date
from typing import List

class MemberFoodPlanService(MemberFoodPlanUsecase):
    ''' This class is an abstract class for usecases of member_food_plan api '''

    @inject
    def __init__(self, food_plan_repo: FoodPlanningRepository = Provide['food_plan_repo'],
                       food_repo: FoodRepository = Provide['food_repo'],
                       food_plan_output_mapper: FoodPlanOutputMapper = Provide['food_plan_output_mapper']):

        self.food_plan_repo = food_plan_repo
        self.food_plan_output_mapper = food_plan_output_mapper
        self.food_repo = food_repo

    def find_food_plan_by_date(self, id: int, start_date: str, end_date: str) -> List[FoodPlanOutput]:
        '''This method returns the meal plan by getting the start and end dates .'''

        inputs1 = start_date.split("-")
        start = date(int(inputs1[0]),int(inputs1[1]),int(inputs1[2]))
        inputs2 = end_date.split("-")
        end = date(int(inputs2[0]),int(inputs2[1]),int(inputs2[2]))
        food_plan = self.food_plan_repo.find_food_plan_by_date(id=id,start_date=start,end_date=end)
        return list(map(self.food_plan_output_mapper.from_model, food_plan))

    def add_new_food_plan(self, input: FoodPlanInput, user: User) -> None:
        '''Creates a food plan .'''

        inputs = input.date_time.split("-")
        date_time = date(int(inputs[0]),int(inputs[1]),int(inputs[2]))
        breakfast = self.food_repo.find_by_id(input.breakfast)
        lunch = self.food_repo.find_by_id(input.lunch)
        dinner = self.food_repo.find_by_id(input.dinner)
        food_plan = FoodPlan(date_time=date_time, breakfast=breakfast, lunch=lunch, dinner=dinner, user=user)
        food_plan.save()
    

    def update_food_plan(self, plan_id: int, input:  FoodPlanBriefInput) -> None:
        ''' Updates a food plan .'''

        try:
            food_plan = self.food_plan_repo.find_food_plan_by_id(plan_id)
            breakfast = self.food_repo.find_by_id(input.breakfast)
            lunch = self.food_repo.find_by_id(input.lunch)
            dinner = self.food_repo.find_by_id(input.dinner)

            food_plan.breakfast = breakfast
            food_plan.lunch = lunch
            food_plan.dinner = dinner
            food_plan.save()
        
        except FoodPlan.DoesNotExist:
            raise FoodPlanNotFoundException(
                detail=f'food plan with plan_id={plan_id} does not exist!')


    def remove_food_plan(self, plan_id: int) -> None:
        '''Deletes a food plan by ID .'''

        self.food_plan_repo.delete_food_plan(plan_id)
