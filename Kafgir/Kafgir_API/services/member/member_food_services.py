from typing import List

from ...dto.food_dto import FoodOutput
from ...usecases.member.member_food_usecases import MemberFoodUsecase
from ...models.food import Food
from ...exceptions.not_found import FoodNotFoundException
from ...repositories.food_repo import FoodRepository
from ...mappers.food_mapper import FoodMapper

from dependency_injector.wiring import inject, Provide

class MemberFoodService(MemberFoodUsecase):

    def __init__(self, food_repo: FoodRepository = Provide['food_repo'],
                       food_mapper: FoodMapper = Provide['food_mapper']):
        self.food_repo = food_repo
        self.food_mapper = food_mapper
        
    def find_by_id(self, id: int) -> FoodOutput:
        try:
            food = self.food_repo.find_by_id(id)
            return self.food_mapper.from_model(food)
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def add_ingredients_to_list(self, food_id: int) -> None:
        pass
