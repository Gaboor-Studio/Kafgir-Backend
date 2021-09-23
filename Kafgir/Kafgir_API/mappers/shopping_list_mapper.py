from ..models.shopping_list_item import ShoppingListItem
from ..dto.shopping_list_dto import ShoppingListItemOutput

class ShoppingListItemOutputMapper:
    ''' This is a mapper for converting shopping list item default model to ShoppingListItemOutput DTO'''

    def from_model(self, model: ShoppingListItem) -> ShoppingListItemOutput:
        '''Takes a model of shopping list item and converts it to ShoppingListItemOutput DTO'''

        if model == None:
            return None

        return ShoppingListItemOutput(  id=model.pk,
                                        title=model.title,
                                        done=model.done,
                                        amount=model.amount)

