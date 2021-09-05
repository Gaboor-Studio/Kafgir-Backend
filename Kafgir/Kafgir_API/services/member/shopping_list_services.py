from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.shopping_list_item import ShoppingListItem
from ...models.user import User

from ...usecases.member.shopping_list_usecases import MemberShoppingListUsecase
from ...dto.shopping_list_dto import ShoppingListItemInput,ShoppingListItemOutput
from ...repositories.shopping_list_repo import ShoppingListRepository
from ...mappers.shopping_list_mapper import ShoppingListItemOutputMapper
from ...exceptions.not_found import ShoppingListItemNotFoundException

from typing import List

class MemberShoppingListService(MemberShoppingListUsecase):

    @inject
    def __init__(self, shopping_list_repo: ShoppingListRepository = Provide['shopping_list_repo'],
                       user_repo: UserRepository = Provide['user_repo'],
                       shopping_list_output_mapper: ShoppingListItemOutputMapper = Provide['shopping_list_output_mapper']):

        self.shopping_list_repo = shopping_list_repo
        self.user_repo = user_repo
        self.shopping_list_output_mapper = shopping_list_output_mapper

    def find_shopping_list(self, id: int) -> List[ShoppingListItemOutput]:
        return list(map(self.shopping_list_output_mapper.from_model, self.shopping_list_repo.find_all_items(id=id)))

    def add_new_shopping_list_item(self, input:  ShoppingListItemInput, user: User) -> None: 
        shopping_list_item = ShoppingListItem(title=input.title, amount=input.amount, user=user)
        shopping_list_item.save()

    def add_new_shopping_list(self, inputs:  List[ShoppingListItemInput], user: User) -> None:
        for input in inputs:
            shopping_list_item = ShoppingListItem(title=input.title, amount=input.amount, user=user)
            shopping_list_item.save()

    def update_shopping_list_item(self, item_id: int, input:  ShoppingListItemInput) -> None:
        try:
            shopping_list_item = self.shopping_list_repo.find_item_by_id(item_id)
            
            shopping_list_item.title = input.title
            shopping_list_item.amount = input.amount

            shopping_list_item.save()
        
        except ShoppingListItem.DoesNotExist:
            raise ShoppingListItemNotFoundException(
                detail=f'shopping list item with item_id={item_id} does not exist!')


    def done(self, item_id: int) -> None:
        try:
            shopping_list_item = self.shopping_list_repo.find_item_by_id(item_id)
            
            shopping_list_item.done = True

            shopping_list_item.save()
        
        except ShoppingListItem.DoesNotExist:
            raise ShoppingListItemNotFoundException(
                detail=f'shopping list item with item_id={item_id} does not exist!')

    def undone(self, item_id: int) -> None:
        try:
            shopping_list_item = self.shopping_list_repo.find_item_by_id(item_id)
            
            shopping_list_item.done = False

            shopping_list_item.save()
        
        except ShoppingListItem.DoesNotExist:
            raise ShoppingListItemNotFoundException(
                detail=f'shopping list item with item_id={item_id} does not exist!')

    def remove_shopping_list_item(self, item_id: int) -> None:
        self.shopping_list_repo.delete_item(item_id)
    
