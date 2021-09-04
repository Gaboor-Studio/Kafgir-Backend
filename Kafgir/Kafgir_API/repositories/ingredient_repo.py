from abc import ABC, abstractmethod

from ..models.ingredient import Ingredient

from typing import List


class IngredientRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> Ingredient:
        pass

    @abstractmethod
    def find_all_starting_with(self, name: str) -> List[Ingredient]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> Ingredient:
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        pass

    @abstractmethod
    def save(self, ingredient: Ingredient) -> None:
        pass
