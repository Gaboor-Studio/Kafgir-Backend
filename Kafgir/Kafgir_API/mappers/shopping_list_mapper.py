from ..models.shopping_list_item import ShoppingListItem
from ..dto.shopping_list_dto import ShoppingListItemOutput

class ShoppingListItemOutputMapper:

    def from_model(self, model: ShoppingListItem) -> ShoppingListItemOutput:
        if model == None:
            return None

        return ShoppingListItemOutput(  id=model.pk,
                                        title=model.title,
                                        done=model.done,
                                        amount=model.amount,
                                        unit=model.unit)

