import attr

@attr.s
class IngredientOutput:
    '''This is an output dto for showing an ingredient.'''

    id: int = attr.ib()
    name: str = attr.ib()

@attr.s
class IngredientInput:
    '''This is an input DTO for receiving ingredient datails.'''

    name: str = attr.ib()
