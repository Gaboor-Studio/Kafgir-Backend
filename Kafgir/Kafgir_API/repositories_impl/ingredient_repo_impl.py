from abc import ABC, abstractmethod

from ..models.ingredient import Ingredient
from ..repositories.ingredient_repo import IngredientRepository

from typing import List

class IngredientRepositoryImpl(IngredientRepository):

    def find_by_id(self, id: int) -> Ingredient:
        return Ingredient.objects.get(pk=id)

    def find_all_starting_with(self, name: str) -> None:
        return Ingredient.objects.filter(name__istartingwith=name)

    def find_by_name(self, name: str) -> Ingredient:
        return Ingredient.objects.get(name__exact=name)

    def delete_by_id(self, id: int) -> None:
        Ingredient.objects.filter(pk=id).delete()

    def save(self, ingredient: Ingredient) -> None:
        ingredient.save()
