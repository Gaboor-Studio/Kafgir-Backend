from ..models.food import Food
from ..dto.food_dto import FoodBriefOutput, FoodInFoodPlanOutput, FoodOutput

from .ingredient_piece_mapper import IngredientPieceMapper
from .recipe_item_mapper import RecipeItemMapper

from dependency_injector.wiring import inject, Provide

class FoodMapper:

    @inject
    def __init__(self, ingredient_piece_mapper: IngredientPieceMapper = Provide['ingredient_piece_mapper'],
                       recipe_item_mapper: RecipeItemMapper = Provide['recipe_item_mapper']):
        self.ingredient_piece_mapper = ingredient_piece_mapper
        self.recipe_item_mapper = recipe_item_mapper
                       
    def from_model(self, model: Food) -> FoodOutput:
        if model == None:
            return None

        return FoodOutput(id=model.pk,
                          title=model.title,
                          rating=model.rating,
                          cooking_time=model.cooking_time,
                          level=model.level,
                          ingredients=list(
                              map(self.ingredient_piece_mapper.from_model, list(model.ingredient_pieces.all()))),
                          recipe=list(map(self.recipe_item_mapper.from_model), list(
                              model.recipe_items.all()))
                          )


class FoodBriefMapper:

    def from_model(self, model: Food) -> FoodBriefOutput:
        if model == None:
            return None

        return FoodBriefOutput(id=model.pk,
                          title=model.title,
                          rating=model.rating,
                          cooking_time=model.cooking_time,
                          level=model.level)

class FoodInFoodPlanMapper:

    def from_model(self, model: Food) -> FoodInFoodPlanOutput:
        if model == None:
            return None

        return FoodInFoodPlanOutput(id=model.pk,
                          title=model.title)


