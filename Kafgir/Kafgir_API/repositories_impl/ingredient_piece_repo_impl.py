from ..models.ingredient import Ingredient
from ..models.food import Food
from ..models.ingredient_piece import IngredientPiece
from ..models.ingredient import Ingredient
from ..models.food import Food
from ..repositories.ingredient_piece_repo import IngredientPieceRepository

from typing import List

class IngredientPieceRepositoryImpl(IngredientPieceRepository):
    '''This is an implementation of the IngredientPieceRepository.'''

    def save(self, ingredient_piece: IngredientPiece) -> None:
        '''Saves an ingredient piece to database.'''
        ingredient_piece.save()

    def is_duplicate(self,food: Food, ingredient: Ingredient) -> bool:
        '''Checks if an ingredient is already exists in the food and returns a boolean result.'''
        return IngredientPiece.objects.filter(food=food,ingredient=ingredient).exists()
