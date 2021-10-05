import attr
from datetime import datetime
from .food_dto import FoodInFoodPlanOutput

from typing import List


@attr.s
class FoodPlanOutput:
    '''This is a DTO for showing food plan details.'''

    id: int = attr.ib()
    date_time: datetime = attr.ib()
    breakfast: FoodInFoodPlanOutput = attr.ib()
    lunch: FoodInFoodPlanOutput = attr.ib()
    dinner: FoodInFoodPlanOutput = attr.ib()

@attr.s
class FoodPlanInput:
    '''This is a DTO for creating food plan .'''

    date_time: str = attr.ib()
    breakfast: int = attr.ib()
    lunch: int = attr.ib()
    dinner: int = attr.ib()

@attr.s
class FoodPlanBriefInput:
    '''This is a DTO for updating food plan . It does not take date time as parameters.'''

    breakfast: int = attr.ib()
    lunch: int = attr.ib()
    dinner: int = attr.ib()
