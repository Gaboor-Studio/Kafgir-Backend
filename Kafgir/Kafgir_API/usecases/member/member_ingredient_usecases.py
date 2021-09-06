from abc import ABC, abstractmethod

from ...dto.ingredient_dto import IngredientOutput
from ...models.user import User

from typing import List

class MemberIngredientUsecase(ABC):

    @abstractmethod 
    def find_all_ingredient(self) -> List[IngredientOutput]:
        pass

    @abstractmethod
    def find_all_ingredients_starting_with_name(self, name: str) -> List[IngredientOutput]:
        pass