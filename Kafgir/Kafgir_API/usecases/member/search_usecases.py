from abc import ABC, abstractmethod
from typing import List
from ...dto.food_dto import FoodBriefOutput
from ...dto.search_dto import SearchInput
from ...models.user import User

class SearchUsecase(ABC):
    ''' This class contains all different ways to do a search for any entity in database'''

    @abstractmethod
    def search_for_food(self, user: User, input: SearchInput) -> List[FoodBriefOutput]:
        ''' Search for a group of specific foods using their names, category, ingredients, level and cooking time. saves the request as a history record. '''
        pass
    