from ..models.food import Food
from ..dto.food_dto import FoodBriefOutput, FoodInFoodPlanOutput, FoodOutput, AdminFoodDetailsOutput
from .ingredient_piece_mappers import IngredientPieceMapper
from .recipe_item_mappers import RecipeItemMapper
from .comment_mapper import CommentMapper

from dependency_injector.wiring import inject, Provide

class FoodMapper:
    '''A mapper for converting a food to the FoodOutput DTO.'''

    @inject
    def __init__(self, ingredient_piece_mapper: IngredientPieceMapper = Provide['ingredient_piece_mapper'],
                       comment_mapper: CommentMapper = Provide['comment_mapper'],
                       recipe_item_mapper: RecipeItemMapper = Provide['recipe_item_mapper']):
        '''Constructor with 4 arguments that will be injected automatically by the freamwork.
        It uses those 4 mappers to make a FoodOutput DTO.
        '''
        self.ingredient_piece_mapper = ingredient_piece_mapper
        self.recipe_item_mapper = recipe_item_mapper
        self.comment_mapper = comment_mapper
                       
    def from_model(self, model: Food) -> FoodOutput:
        '''A methods that converts a given food model to a FoodOutput DTO'''
        # If the model is none it must return None
        if model == None:
            return None

        # Creating FoodOutput DTO
        return FoodOutput(id=model.pk,
                          title=model.title,
                          rating=model.rating,
                          cooking_time=model.cooking_time,
                          level=model.level,
                          ingredients=list(
                              map(self.ingredient_piece_mapper.from_model, list(model.ingredient_pieces.all()))),
                          recipe=list(map(self.recipe_item_mapper.from_model, list(model.recipe_items.all()))),
                          comments=[],
                          my_comment=None,
                          tags=[tag.title for tag in model.tags.all()])



class FoodBriefMapper:
    '''A mapper for converting a food model to the FoodBriefOutput DTO.'''

    def from_model(self, model: Food) -> FoodBriefOutput:
        '''A method that converts a given food model to a FoodBriefOutput DTO.'''
        # If the model is none it must return None
        if model == None:
            return None

        # Creating FoodBriefOutput DTO
        return FoodBriefOutput(id=model.pk,
                          title=model.title,
                          rating=model.rating,
                          cooking_time=model.cooking_time,
                          level=model.level)

class FoodInFoodPlanMapper:
    '''A mapper for converting a food model to the FoodInFoodPlanOutput DTO.'''

    def from_model(self, model: Food) -> FoodInFoodPlanOutput:
        '''A method that converts a given food model to a FoodInFoodPlanOutput DTO.'''
        # If the model is none it must return None
        if model == None:
            return None

        # Creating FoodInFoodPlanOutput DTO
        return FoodInFoodPlanOutput(id=model.pk,
                          title=model.title)


class AdminFoodDetailsMapper:
    '''A mapper for converting a food model to the AdminFoodDetailsOutput DTO.'''

    @inject
    def __init__(self, ingredient_piece_mapper: IngredientPieceMapper = Provide['ingredient_piece_mapper'],
                       recipe_item_mapper: RecipeItemMapper = Provide['recipe_item_mapper']):
        '''Constructor with w arguments that will be injected automatically by the freamwork.
        It uses those w mappers to make a AdminFoodDetailsOutput DTO.
        '''
        self.ingredient_piece_mapper = ingredient_piece_mapper
        self.recipe_item_mapper = recipe_item_mapper

    def from_model(self, model: Food) -> AdminFoodDetailsOutput:
        '''A method that converts a given food model to a AdminFoodDetailsOutput DTO.'''
        # If the model is none it must return None
        if model == None:
            return None

        # Creating AdminFoodDetailsOutput DTO
        return AdminFoodDetailsOutput(id=model.pk,
                          title=model.title,
                          rating=model.rating,
                          cooking_time=model.cooking_time,
                          level=model.level,
                          ingredients=list(
                              map(self.ingredient_piece_mapper.from_model, list(model.ingredient_pieces.all()))),
                          recipe=list(map(self.recipe_item_mapper.from_model, list(model.recipe_items.all()))),
                          tags=[tag.title for tag in model.tags.all()])