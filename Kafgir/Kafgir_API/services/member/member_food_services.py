from typing import List

from ...dto.food_dto import FoodOutput, FoodBriefOutput
from ...usecases.member.member_food_usecases import MemberFoodUsecase
from ...models.food import Food
from ...models.shopping_list_item import ShoppingListItem
from ...models.tag import Tag
from ...exceptions.not_found import FoodNotFoundException,TagNotFoundException
from ...repositories.food_repo import FoodRepository
from ...repositories.tag_repo import TagRepository
from ...repositories.shopping_list_repo import ShoppingListRepository
from ...mappers.food_mapper import FoodMapper,FoodBriefMapper

from django.contrib.auth import get_user_model
from dependency_injector.wiring import inject, Provide

class MemberFoodService(MemberFoodUsecase):

    user_model = get_user_model()

    def __init__(self, food_repo: FoodRepository = Provide['food_repo'],
                       tag_repo: TagRepository = Provide['tag_repo'],
                       food_mapper: FoodMapper = Provide['food_mapper'],
                       food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper'],
                       shopping_list_repo: ShoppingListRepository = Provide['shopping_list_repo']):
        self.tag_repo = tag_repo
        self.food_repo = food_repo
        self.food_mapper = food_mapper
        self.food_brief_mapper = food_brief_mapper
        self.shopping_list_repo = shopping_list_repo

    def find_by_id(self, id: int) -> FoodOutput:
        try:
            food = self.food_repo.find_by_id(id)
            return self.food_mapper.from_model(food)
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def add_ingredients_to_list(self, food_id: int, user: user_model) -> None:
        try:
            food = self.food_repo.find_by_id(food_id)
            for ingredient in food.ingredient_pieces.all():
                item = ShoppingListItem(title=ingredient.ingredient.name, amount=ingredient.amount, user=user)
                self.shopping_list_repo.save_item(item)
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def find_all_with_tag(self, tag_id: int) -> List[FoodBriefOutput]:
        try:
            tag = self.tag_repo.find_by_id(tag_id)
            foods = self.food_repo.find_all_by_tag_ordered_by_rating(tag)
            return list(map(self.food_brief_mapper.from_model, foods))
        except Tag.DoesNotExist:
            raise TagNotFoundException(detail=f'Tag(id= {tag_id}) not found!')
    