from Kafgir_API.models.ingredient import Ingredient
from Kafgir_API.models.food import Food
from abc import ABC, abstractmethod

from ..models.ingredient_piece import IngredientPiece
from ..models.ingredient import Ingredient
from ..models.food import Food
from ..repositories.ingredient_piece_repo import IngredientPieceRepository

from typing import List


class IngredientPieceRepositoryImpl(IngredientPieceRepository):

    def save(self, ingredient_piece: IngredientPiece) -> None:
        ingredient_piece.save()

    def is_duplicate(self,food: Food, ingredient: Ingredient) -> bool:
        return IngredientPiece.objects.filter(food=food,ingredient=ingredient).exists()
