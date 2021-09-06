import attr
from .food_dto import FoodInFoodPlanOutput

from typing import List

@attr.s
class TagOutput:
    id: int = attr.ib()
    title: str = attr.ib()
    is_main: bool = attr.ib()
    is_primary: bool = attr.ib()
    display_order: int = attr.ib()

@attr.s
class PrimaryTagOutput:
    id: int = attr.ib()
    title: str = attr.ib()
    display_order: int = attr.ib()

@attr.s
class TagInput:
    title: str = attr.ib()
    is_main: bool = attr.ib()
    is_primary: bool = attr.ib()
    display_order: int = attr.ib()

@attr.s
class MainTagOutput:
    id: int = attr.ib()
    title: str = attr.ib()
    foods: List[FoodInFoodPlanOutput] = attr.ib()
    display_order: int = attr.ib()
