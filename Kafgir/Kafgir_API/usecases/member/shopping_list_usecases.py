from abc import ABC, abstractmethod

from ...dto.shopping_list_dto import ShoppingListItemInput,ShoppingListItemOutput,ShoppingListItemBriefInput
from ...models.user import User

from typing import List

class MemberShoppingListUsecase(ABC):
    
    @abstractmethod
    def find_shopping_list(self, id: int) -> List[ShoppingListItemOutput]:
        pass 

    @abstractmethod
    def add_new_shopping_list_item(self, input:  ShoppingListItemBriefInput, user: User) -> None:
        pass

    @abstractmethod
    def add_new_shopping_list(self, inputs:  List[ShoppingListItemBriefInput], user: User) -> None:
        pass

    @abstractmethod
    def update_shopping_list_item(self, item_id: int, input:  ShoppingListItemInput) -> None:
        pass

    @abstractmethod
    def done(self, item_id: int) -> None:
        pass

    @abstractmethod
    def undone(self, item_id: int) -> None:
        pass

    @abstractmethod
    def remove_shopping_list_item(self, item_id: int) -> None:
        pass