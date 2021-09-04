from ..models.ingredient_piece import IngredientPiece
from ..dto.ingredient_piece_dto import IngredientPieceOutput


class IngredientPieceMapper:

    def from_model(self, model: IngredientPiece) -> IngredientPieceOutput:
        if model == None:
            return None

        return IngredientPieceOutput(id=model.pk,
                                    name=model.ingredient.name,
                                    amount=model.amount)