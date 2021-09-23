from ..models.ingredient import Ingredient
from ..dto.ingredient_dto import IngredientOutput

class IngredientMapper:
    '''A mapper for converting an ingredient model to the IngredientOutput DTO.'''

    def from_model(self, model: Ingredient) -> IngredientOutput:
        '''A method that converts the given ingredient model to a IngredientOutput DTO.'''    
        # Return None if the model is None
        if model == None:
            return None

        # Create the IngredientOutput
        return IngredientOutput(id=model.pk, name=model.name)