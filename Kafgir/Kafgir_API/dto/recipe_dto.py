import attr

@attr.s
class RecipeItemOutput:
    '''This is an output DTO for showing recipe item details.'''

    id: int = attr.ib()
    step: int = attr.ib()
    text: str = attr.ib()

@attr.s
class RecipeItemInput:
    '''This is an input DTO for receiving recipe item details.'''
    
    step: int = attr.ib()
    text: str = attr.ib()
