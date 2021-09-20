from abc import ABC, abstractmethod
from typing import List
from ...dto.food_dto import FoodBriefOutput

class SearchUsecase(ABC):
    ''' This class contains all different ways to do a search for any entity in database'''

    @abstractmethod
    def search_for_food(self, name: str, category: int, ingredients: List[str], level: int, cooking_time: int) -> List[FoodBriefOutput]:
        ''' Search for a group of specific foods using their names, category, ingredients, level and cooking time'''
        pass
    