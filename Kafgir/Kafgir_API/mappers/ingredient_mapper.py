from ..models.ingredient import Ingredient
from ..dto.ingredient_dto import IngredientOutput

class IngredientMapper:

    def from_model(self, model: Ingredient) -> IngredientOutput:
        if model == None:
            return None

        return IngredientOutput(  id=model.pk,
                                        name=model.name)