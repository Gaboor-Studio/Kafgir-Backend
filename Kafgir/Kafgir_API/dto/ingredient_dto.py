import attr

@attr.s
class IngredientOutput:
    '''This is an output DTO for showing details of an ingredient.'''

    id: int = attr.ib()
    name: str = attr.ib()

@attr.s
class IngredientInput:
    '''This is an input DTO for receiving ingredient details.'''
    name: str = attr.ib()
