from abc import ABC, abstractmethod

from ..models.ingredient import Ingredient

from typing import List

class IngredientRepository(ABC):
    '''This is an abstraction for ingredient repository. It handles database queries for CRUD operations on ingredients.'''

    @abstractmethod
    def find_by_id(self, id: int) -> Ingredient:
        '''Finds an ingredient given its id. It raises Ingredient.DoesNotExist exception if the food does not exist.'''
        pass

    @abstractmethod
    def find_all(self) -> List[Ingredient]:
        '''Finds all ingredients and returns a list of them.'''
        pass

    @abstractmethod
    def find_all_starting_with(self, name: str) -> List[Ingredient]:
        '''Finds all ingredients which their name starts with the given string and returns a list of them.'''
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> Ingredient:
        '''Finds an ingredient with the given name.'''
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        '''Deletes an ingredient given its id.'''
        pass

    @abstractmethod
    def save(self, ingredient: Ingredient) -> None:
        '''Saves an ingredient to database.'''
        pass
