from abc import ABC, abstractmethod

from ..models.ingredient_piece import IngredientPiece

from typing import List


class IngredientPieceRepository(ABC):

    @abstractmethod
    def save(self, ingredient: IngredientPiece) -> None:
        pass
