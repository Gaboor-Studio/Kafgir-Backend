from ..models.recipe_item import RecipeItem
from ..repositories.recipe_item_repo import RecipeItemRepository

from typing import List

class RecipeItemRepositoryImpl(RecipeItemRepository):
    '''This is an implementation of the RecipeItemRepository.'''

    def save(self, item: RecipeItem) -> None:
        '''Saves a recipe item in the database.'''
        item.save()
