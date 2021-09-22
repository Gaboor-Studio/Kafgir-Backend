from ..models.recipe_item import RecipeItem
from ..dto.recipe_dto import RecipeItemOutput


class RecipeItemMapper:

    def from_model(self, model: RecipeItem) -> RecipeItemOutput:
        if model == None:
            return None

        return RecipeItemOutput(id=model.pk,
                                step=model.step,
                                text=model.text)