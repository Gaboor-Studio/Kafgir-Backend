from dependency_injector import containers, providers

from ..mappers.shopping_list_mapper import *
from ..mappers.food_plan_mapper import *
from ..mappers.food_mapper import *
from ..mappers.ingredient_piece_mapper import *
from ..mappers.recipe_item_mapper import *


class MapperContainer(containers.DeclarativeContainer):
     
    shopping_list_output_mapper = providers.Singleton(
        ShoppingListItemOutputMapper
    )

    food_plan_output_mapper = providers.Singleton(
        FoodPlanOutputMapper
    )

    ingredient_piece_mapper = providers.Singleton(
        IngredientPieceMapper
    )

    recipe_item_mapper = providers.Singleton(
        RecipeItemMapper
    )

    food_mapper = providers.Singleton(
        FoodMapper,
        ingredient_piece_mapper=ingredient_piece_mapper,
        recipe_item_mapper=recipe_item_mapper
    )

    food_brief_mapper = providers.Singleton(
        FoodBriefMapper
    )

    food_in_food_plan_mapper = providers.Singleton(
        FoodInFoodPlanMapper
    )

container = MapperContainer()
# container.init_resources()
