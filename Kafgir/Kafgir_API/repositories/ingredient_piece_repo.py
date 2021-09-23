from abc import ABC, abstractmethod

from ..models.ingredient_piece import IngredientPiece
from ..models.ingredient import Ingredient
from ..models.food import Food

from typing import List


class IngredientPieceRepository(ABC):
    '''This is an abstraction for ingredient piece repository.It handles database queries for CRUD operations on ingredient pieces.'''

    @abstractmethod
    def save(self, ingredient: IngredientPiece) -> None:
        '''Saves an ingredient piece to database.'''
        pass

    @abstractmethod
    def is_duplicate(self,food: Food, ingredient: Ingredient) -> bool:
        '''Checks if an ingredient is already exists in the food and returns a boolean result.'''
        pass
    