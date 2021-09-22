import attr

from .ingredient_piece_dto import IngredientPieceOutput,IngredientPieceInput
from .recipe_dto import RecipeItemOutput,RecipeItemInput
from .comment_dto import CommentOutput

from typing import List

@attr.s
class FoodOutput:
    '''This is an output DTO for showing details of a food in client side.'''

    id: int = attr.ib()
    title: str = attr.ib()
    rating: float = attr.ib()
    cooking_time: str = attr.ib()
    level: int = attr.ib()
    ingredients: List[IngredientPieceOutput] = attr.ib()
    recipe: List[RecipeItemOutput] = attr.ib()
    comments: List[CommentOutput] = attr.ib()
    my_comment: CommentOutput = attr.ib()

@attr.s
class AdminFoodDetailsOutput:
    '''This is an output DTO for showing details of a food in admin panel.'''

    id: int = attr.ib()
    title: str = attr.ib()
    rating: float = attr.ib()
    cooking_time: str = attr.ib()
    level: int = attr.ib()
    ingredients: List[IngredientPieceOutput] = attr.ib()
    recipe: List[RecipeItemOutput] = attr.ib()

@attr.s
class FoodBriefOutput:
    '''This is an output DTO for showing a brief details of a food to be placed in a list of foods in admin panel.'''

    id: int = attr.ib()
    title: str = attr.ib()
    rating: float = attr.ib()
    cooking_time: str = attr.ib()
    level: int = attr.ib()

@attr.s
class FoodInFoodPlanOutput:
    '''This is an output DTO for showing details of a food in food planner.'''

    id: int = attr.ib()
    title: str = attr.ib()

@attr.s
class FoodInput:
    '''This is an input DTO for receiving food data in admin panel.'''
    
    title: str = attr.ib()
    cooking_time: str = attr.ib()
    level: int = attr.ib()
    ingredients: List[IngredientPieceInput] = attr.ib()
    recipe: List[RecipeItemInput] = attr.ib()
    tags: List[int] = attr.ib()
