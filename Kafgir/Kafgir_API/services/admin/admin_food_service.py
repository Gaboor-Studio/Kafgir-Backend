from typing import List

from ...dto.food_dto import FoodOutput, FoodInput, AdminFoodDetailsOutput
from ...usecases.admin.admin_food_usecases import AdminFoodUsecase

from ...repositories.food_repo import FoodRepository
from ...repositories.ingredient_repo import IngredientRepository
from ...repositories.tag_repo import TagRepository
from ...repositories.ingredient_piece_repo import IngredientPieceRepository
from ...repositories.recipe_item_repo import RecipeItemRepository

from ...mappers.food_mapper import AdminFoodDetailsMapper, FoodBriefMapper

from ...models.food import Food
from ...models.tag import Tag
from ...models.ingredient import Ingredient
from ...models.ingredient_piece import IngredientPiece
from ...models.recipe_item import RecipeItem
from ...exceptions.not_found import FoodNotFoundException, TagNotFoundException
from ...exceptions.not_found import FoodNotFoundException,PageNotFoundException

from ...util.paginator import PaginationData,PaginatorUtil,PaginationOutput

from dependency_injector.wiring import inject, Provide

class AdminFoodService(AdminFoodUsecase):

    @inject
    def __init__(self, food_repo: FoodRepository = Provide['food_repo'],
                       admin_food_details_mapper: AdminFoodDetailsMapper = Provide['admin_food_details_mapper'],
                       tag_repo: TagRepository = Provide['tag_repo'],
                       food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper'],
                       ingredient_repo: IngredientRepository = Provide['ingredient_repo'],
                       ingredient_piece_repo: IngredientPieceRepository = Provide['ingredient_piece_repo'],
                       recipe_item_repo: RecipeItemRepository = Provide['recipe_item_repo']
                       ):
        self.food_repo = food_repo
        self.tag_repo = tag_repo
        self.admin_food_details_mapper = admin_food_details_mapper
        self.food_brief_mapper = food_brief_mapper
        self.ingredient_repo = ingredient_repo
        self.ingredient_piece_repo = ingredient_piece_repo
        self.recipe_item_repo = recipe_item_repo
        

    def find_by_id(self, id: int) -> AdminFoodDetailsOutput:
        try:
            food = self.food_repo.find_by_id(id)
            return self.admin_food_details_mapper.from_model(food)
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def load_all(self, pagination_data: PaginationData) -> PaginationOutput:
        foods = self.food_repo.find_all()
        try:
            paginated_foods, pages = PaginatorUtil.paginate_query_set(foods, pagination_data)
            data = list(map(self.food_brief_mapper.from_model, paginated_foods))
            return PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)
        except:
            raise PageNotFoundException(detail= f'Page({pagination_data.page}) not found!')
        
    def delete_by_id(self, id: int) -> None:
        self.food_repo.delete_by_id(id)

    def create_food(self, input: FoodInput) -> AdminFoodDetailsOutput:
        food = Food(title=input.title, level=input.level, cooking_time=input.cooking_time)
        self.food_repo.save(food)

        for ingredient_piece in input.ingredients:
            ingredient = None            
            try:
                ingredient = self.ingredient_repo.find_by_name(ingredient_piece.name)
            except:
                ingredient = Ingredient(name=ingredient_piece.name)
                self.ingredient_repo.save(ingredient)
            
            if not self.ingredient_piece_repo.is_duplicate(food=food,ingredient=ingredient):
                ingredient_piece_obj = IngredientPiece(ingredient=ingredient, food=food, amount=ingredient_piece.amount)
                ingredient_piece_obj.save()
        
        for recipe in input.recipe:
            recipe_item = RecipeItem(food=food, text=recipe.text, step=recipe.step)
            self.recipe_item_repo.save(recipe_item)

        for tag_id in input.tags:
            try:
                tag = self.tag_repo.find_by_id(tag_id)
                food.tags.add(tag)
            except Tag.DoesNotExist:
                raise TagNotFoundException(detail=f'tag(id={id}) not found!') 

        return self.admin_food_details_mapper.from_model(food)