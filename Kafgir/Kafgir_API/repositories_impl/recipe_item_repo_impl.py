from ..models.recipe_item import RecipeItem
from ..repositories.recipe_item_repo import RecipeItemRepository

from typing import List


class RecipeItemRepositoryImpl(RecipeItemRepository):

    def save(self, item: RecipeItem) -> None:
        item.save()
