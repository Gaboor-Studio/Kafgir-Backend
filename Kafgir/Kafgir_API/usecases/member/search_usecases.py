from abc import ABC, abstractmethod
from typing import List
from ...dto.food_dto import FoodBriefOutput

class SearchUsecase(ABC):

    @abstractmethod
    def search_for_food(self, name: str, category: int, ingredients: List[str], level: int, cooking_time: int) -> List[FoodBriefOutput]:
        pass
    