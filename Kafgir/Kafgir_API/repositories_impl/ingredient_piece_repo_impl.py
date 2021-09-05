from abc import ABC, abstractmethod

from ..models.ingredient_piece import IngredientPiece
from ..repositories.ingredient_piece_repo import IngredientPieceRepository

from typing import List


class IngredientPieceRepositoryImpl(IngredientPieceRepository):

    def save(self, ingredient_piece: IngredientPiece) -> None:
        ingredient_piece.save()
