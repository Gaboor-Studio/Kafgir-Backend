from abc import ABC, abstractmethod

from ...dto.food_plan_dto import FoodPlanInput,FoodPlanOutput,FoodPlanBriefInput
from ...models.user import User

from typing import List

class MemberFoodPlanUsecase(ABC):
    
    @abstractmethod
    def find_food_plan_by_date(self, id: int, start_date: str, end_date: str) -> List[FoodPlanOutput]:
        pass 

    @abstractmethod
    def add_new_food_plan(self, input: FoodPlanInput, user: User) -> None:
        pass

    @abstractmethod
    def remove_food_plan(self, plan_id: int) -> None:
        pass

    @abstractmethod
    def update_food_plan(self, plan_id: int, input:  FoodPlanBriefInput) -> None:
        pass