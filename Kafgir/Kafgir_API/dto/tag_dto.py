import attr
from .food_dto import FoodInFoodPlanOutput

from typing import List

@attr.s
class TagOutput:
    '''This is a DTO for showing tag details.'''

    id: int = attr.ib()
    title: str = attr.ib()
    is_main: bool = attr.ib()
    is_primary: bool = attr.ib()
    display_order: int = attr.ib()

@attr.s
class PrimaryTagOutput:
    '''This is a DTO for showing a list of categories in home page.'''

    id: int = attr.ib()
    title: str = attr.ib()

@attr.s
class TagInput:
    '''This is a DTO for creating and updating tags.'''

    title: str = attr.ib()
    is_main: bool = attr.ib()
    is_primary: bool = attr.ib()
    display_order: int = attr.ib()

@attr.s
class MainTagOutput:
    '''This is a DTO for showing a list of main tag in home page.'''

    id: int = attr.ib()
    title: str = attr.ib()
    foods: List[FoodInFoodPlanOutput] = attr.ib()
