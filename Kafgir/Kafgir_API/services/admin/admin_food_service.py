from typing import List

from ...dto.food_dto import FoodOutput, FoodInput, FoodBriefOutput
from ...usecases.admin.admin_food_usecases import AdminFoodUsecase

from ...repositories.food_repo import FoodRepository
from ...repositories.ingredient_repo import IngredientRepository
from ...repositories.ingredient_piece_repo import IngredientPieceRepository
from ...repositories.recipe_item_repo import RecipeItemRepository

from ...mappers.food_mapper import FoodMapper, FoodBriefMapper

from ...models.food import Food
from ...models.ingredient import Ingredient
from ...models.ingredient_piece import IngredientPiece
from ...models.recipe_item import RecipeItem

from ...exceptions.not_found import FoodNotFoundException

from dependency_injector.wiring import inject, Provide

class AdminFoodUsecase(AdminFoodUsecase):

    @inject
    def __init__(self, food_repo: FoodRepository = Provide['food_repo'],
                       food_mapper: FoodMapper = Provide['food_mapper'],
                       food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper'],
                       ingredient_repo: IngredientRepository = Provide['ingredient_repo'],
                       ingredient_piece_repo: IngredientPieceRepository = Provide['ingredient_piece_repo'],
                       recipe_item_repo: RecipeItemRepository = Provide['recipe_item_repo']
                       ):
        self.food_repo = food_repo
        self.food_mapper = food_mapper
        self.food_brief_mapper = food_brief_mapper
        self.ingredient_repo = ingredient_repo
        self.ingredient_piece_repo = ingredient_piece_repo
        self.recipe_item_repo = recipe_item_repo

    def find_by_id(self, id: int) -> FoodOutput:
        try:
            food = self.food_repo.find_by_id(id)
            return self.food_mapper.from_model(food)
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def load_all(self) -> List[FoodBriefOutput]:
        foods = self.food_repo.find_all()
        return list(map(self.food_brief_mapper.from_model, foods))

    def delete_by_id(self, id: int) -> None:
        self.food_repo.delete_by_id(id)

    def create_food(self, input: FoodInput) -> FoodOutput:
        food = Food(title=input.title, level=input.level, cooking_time=input.cooking_time)
        self.food_repo.save(food)

        for ingredient_piece in input.ingredients:
            ingredient = None            
            try:
                ingredient = self.ingredient_repo.find_by_name(ingredient_piece.name)
            except:
                ingredient = Ingredient(name=ingredient_piece.name)
                self.ingredient_repo.save(ingredient)
            
            ingredient_piece_obj = IngredientPiece(ingredient=ingredient, food=food, amount=ingredient_piece.amount)
            ingredient_piece_obj.save()
        
        for recipe in input.recipe:
            recipe_item = RecipeItem(food=food, text=recipe.text, step=recipe.step)
            self.recipe_item_repo.save(recipe_item)
        
        return self.food_mapper.from_model(food)