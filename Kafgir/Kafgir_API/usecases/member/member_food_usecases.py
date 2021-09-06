from abc import ABC, abstractmethod

from typing import List

from ...dto.food_dto import FoodOutput
from django.contrib.auth import get_user_model
class MemberFoodUsecase(ABC):
    
    user_model = get_user_model()

    @abstractmethod
    def find_by_id(self, id: int) -> FoodOutput:
        pass 
    
    @abstractmethod
    def add_ingredients_to_list(self, food_id: int, user: user_model) -> None:
        pass