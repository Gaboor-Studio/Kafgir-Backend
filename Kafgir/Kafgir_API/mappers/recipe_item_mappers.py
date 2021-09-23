from ..models.recipe_item import RecipeItem
from ..dto.recipe_dto import RecipeItemOutput


class RecipeItemMapper:
    '''A mapper for converting a recipe item model to the RecipeItemOutput DTO.'''

    def from_model(self, model: RecipeItem) -> RecipeItemOutput:
        '''A method that converts the given recipe item model to a RecipeItemOutput DTO.'''
        # Returns None if the model is None
        if model == None:
            return None

        # Creating the RecipeItemOutput
        return RecipeItemOutput(id=model.pk,
                                step=model.step,
                                text=model.text)