from abc import ABC, abstractmethod

from ..models.ingredient_piece import IngredientPiece
from ..models.ingredient import Ingredient
from ..models.food import Food
from typing import List


class IngredientPieceRepository(ABC):

    @abstractmethod
    def save(self, ingredient: IngredientPiece) -> None:
        pass

    @abstractmethod
    def is_duplicate(self,food: Food, ingredient: Ingredient) -> bool:
        pass
    