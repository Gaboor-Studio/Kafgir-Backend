import attr


@attr.s
class RecipeItemOutput:
    '''This is an output DTO for showing recipe of a food.'''

    id: int = attr.ib()
    step: int = attr.ib()
    text: str = attr.ib()

@attr.s
class RecipeItemInput:
    '''This is an input DTO for receiving recipe details in a food in admin panel.'''
    
    step: int = attr.ib()
    text: str = attr.ib()
