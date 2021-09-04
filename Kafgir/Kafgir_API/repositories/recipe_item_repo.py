from abc import ABC, abstractmethod

from ..models.recipe_item import RecipeItem

from typing import List


class RecipeItemRepository(ABC):

    @abstractmethod
    def save(self, item: RecipeItem) -> None:
        pass
