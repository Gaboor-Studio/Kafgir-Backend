from ..repositories.shopping_list_repo import ShoppingListRepository

from ..models.shopping_list_item import ShoppingListItem

from typing import List

class ShoppingListRepositoryImpl(ShoppingListRepository):

    def find_item_by_id(self, id: int) -> ShoppingListItem:
        return ShoppingListItem.objects.get(pk=id)

    def find_all_items(self, id: int) -> List[ShoppingListItem]:
        return list(ShoppingListItem.objects.filter(user=id))

    def save_item(self, shopping_list_item: ShoppingListItem) -> None:
        shopping_list_item.save()

    def delete_item(self, item_id: int) -> None:
        ShoppingListItem.objects.filter(id=item_id).delete()