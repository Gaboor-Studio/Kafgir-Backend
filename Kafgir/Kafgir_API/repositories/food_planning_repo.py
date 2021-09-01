from abc import ABC, abstractmethod

from ..models.food_plan import FoodPlan

from datetime import date
from typing import List


class FoodPlanningRepository(ABC):

    @abstractmethod
    def find_food_plan_by_id(self, id: int) -> FoodPlan:
        pass

    @abstractmethod
    def find_food_plan_by_date(self, id: int, start_date: date, end_date: date) -> List[FoodPlan]:
        pass

    @abstractmethod
    def save_food_plan(self, food_plan: FoodPlan) -> None:
        pass

    @abstractmethod
    def delete_food_plan(self, plan_id: int) -> None:
        pass
