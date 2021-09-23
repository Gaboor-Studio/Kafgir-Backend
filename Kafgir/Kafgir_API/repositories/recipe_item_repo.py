from abc import ABC, abstractmethod

from ..models.recipe_item import RecipeItem

from typing import List

class RecipeItemRepository(ABC):
    '''This is an abstraction for recipe item repository. It handles database queries for CRUD operations on recipe items.'''

    @abstractmethod
    def save(self, item: RecipeItem) -> None:
        '''Saves a recipe item in the database.'''
        pass
