from ..models.ingredient import Ingredient
from ..repositories.ingredient_repo import IngredientRepository

from typing import List

class IngredientRepositoryImpl(IngredientRepository):
    '''This is an implementation of the IngredientRepository.'''

    def find_by_id(self, id: int) -> Ingredient:
        '''Finds an ingredient given its id. It raises Ingredient.DoesNotExist exception if the food does not exist.'''
        return Ingredient.objects.get(pk=id)

    def find_all(self) -> None:
        '''Finds all ingredients and returns a list of them.'''
        return Ingredient.objects.all()

    def find_all_starting_with(self, name: str) -> None:
        '''Finds all ingredients which their name starts with the given string and returns a list of them.'''
        return Ingredient.objects.filter(name__istartswith=name)

    def find_by_name(self, name: str) -> Ingredient:
        '''Finds an ingredient with the given name.'''
        return Ingredient.objects.get(name__exact=name)

    def delete_by_id(self, id: int) -> None:
        '''Deletes an ingredient given its id.'''
        Ingredient.objects.filter(pk=id).delete()

    def save(self, ingredient: Ingredient) -> None:
        '''Saves an ingredient to database.'''
        ingredient.save()
