import attr

@attr.s
class ShoppingListItemOutput:
    '''This is a DTO for showing a shopping list.'''

    id: int = attr.ib()
    title: str = attr.ib()
    done: bool = attr.ib()
    amount: str = attr.ib()

@attr.s
class ShoppingListItemInput:
    '''This is a DTO for updating shopping list items .'''

    title: str = attr.ib()
    done: bool = attr.ib()
    amount: str = attr.ib()

@attr.s
class ShoppingListItemBriefInput:
    '''This is a DTO for creating shopping list items . It does not take done as parameters.'''
    
    title: str = attr.ib()
    amount: str = attr.ib()
