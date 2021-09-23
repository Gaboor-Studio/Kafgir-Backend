from ..models.ingredient_piece import IngredientPiece
from ..dto.ingredient_piece_dto import IngredientPieceOutput


class IngredientPieceMapper:
    '''A mapper for converting an ingredient piece model to the IngredientPieceOutput DTO.'''

    def from_model(self, model: IngredientPiece) -> IngredientPieceOutput:
        '''A method that converts the given ingredient piece model to a IngredientPieceOutput DTO.'''
        # Return None if the model is None
        if model == None:
            return None
        
        # Creating the IngredientPieceOutput
        return IngredientPieceOutput(id=model.pk,
                                    name=model.ingredient.name,
                                    amount=model.amount)