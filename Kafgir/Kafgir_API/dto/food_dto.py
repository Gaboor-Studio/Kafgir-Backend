import attr

from .ingredient_piece_dto import IngredientPieceOutput,IngredientPieceInput
from .recipe_dto import RecipeItemOutput,RecipeItemInput

from typing import List

@attr.s
class FoodOutput:
    id: int = attr.ib()
    title: str = attr.ib()
    rating: float = attr.ib()
    cooking_time: int = attr.ib()
    level: int = attr.ib()
    ingredients: List[IngredientPieceOutput] = attr.ib()
    recipe: List[RecipeItemOutput] = attr.ib()

@attr.s
class FoodBriefOutput:
    id: int = attr.ib()
    title: str = attr.ib()
    rating: float = attr.ib()
    cooking_time: int = attr.ib()
    level: int = attr.ib()

@attr.s
class FoodInFoodPlanOutput:
    id: int = attr.ib()
    title: str = attr.ib()

@attr.s
class FoodInput:
    title: str = attr.ib()
    cooking_time: int = attr.ib()
    level: int = attr.ib()
    ingredients: List[IngredientPieceInput] = attr.ib()
    recipe: List[RecipeItemInput] = attr.ib()