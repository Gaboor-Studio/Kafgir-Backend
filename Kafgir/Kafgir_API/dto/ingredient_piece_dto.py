import attr

@attr.s
class IngredientPieceOutput:
    '''This is an output DTO for showing ingredient piece details.'''

    id: int = attr.ib()
    name: str = attr.ib()
    amount: str = attr.ib()

@attr.s
class IngredientPieceInput:
    '''This is an input DTO for receiving ingredient piece details.'''
    
    name: str = attr.ib()
    amount: str = attr.ib()
