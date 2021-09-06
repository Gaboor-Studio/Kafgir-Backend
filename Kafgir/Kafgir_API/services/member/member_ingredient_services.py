from dependency_injector.wiring import inject, Provide

from ...models.ingredient import Ingredient

from ...usecases.member.member_ingredient_usecases import MemberIngredientUsecase
from ...dto.ingredient_dto import IngredientOutput
from ...repositories.ingredient_repo import IngredientRepository
from ...mappers.ingredient_mapper import IngredientMapper
from ...exceptions.not_found import IngredientNotFoundException

from datetime import date
from typing import List

class MemberIngredientService(MemberIngredientUsecase):

    @inject
    def __init__(self, ingredient_repo: IngredientRepository = Provide['ingredient_repo'],
                       ingredient_mapper: IngredientMapper = Provide['ingredient_mapper']):

        self.ingredient_repo = ingredient_repo
        self.ingredient_mapper = ingredient_mapper

    def find_all_ingredient(self) -> List[IngredientOutput]:
        return list(map(self.ingredient_mapper.from_model, self.ingredient_repo.find_all()))

    
    def find_all_ingredients_starting_with_name(self, name: str) -> List[IngredientOutput]:
        return list(map(self.ingredient_mapper.from_model, self.ingredient_repo.find_all_starting_with(name)))

