from abc import ABC, abstractmethod

from typing import List

from ...dto.food_dto import FoodOutput

class MemberFoodUsecase(ABC):
    
    @abstractmethod
    def find_by_id(self, id: int) -> FoodOutput:
        pass 
    
    @abstractmethod
    def add_ingredients_to_list(self, food_id: int) -> None:
        pass