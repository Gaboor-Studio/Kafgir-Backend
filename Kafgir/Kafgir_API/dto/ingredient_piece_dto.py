import attr

@attr.s
class IngredientPieceOutput:
    '''This is an output DTO for showing an ingredient and its amount in a food.'''

    id: int = attr.ib()
    name: str = attr.ib()
    amount: str = attr.ib()

@attr.s
class IngredientPieceInput:
    '''This is an input DTO for receiving a ingredient piece in a food in admin panel.'''
    
    name: str = attr.ib()
    amount: str = attr.ib()
