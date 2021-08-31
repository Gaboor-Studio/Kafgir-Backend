from abc import ABC, abstractmethod

from ..models.shopping_list_item import ShoppingListItem

from typing import List


class ShoppingListRepository(ABC):

    @abstractmethod
    def find_item_by_id(self, id: int) -> ShoppingListItem:
        pass

    @abstractmethod
    def find_all_items(self, id: int) -> List[ShoppingListItem]:
        pass

    @abstractmethod
    def save_item(self, shopping_list_item: ShoppingListItem) -> None:
        pass

    @abstractmethod
    def delete_item(self, item_id: int) -> None:
        pass
