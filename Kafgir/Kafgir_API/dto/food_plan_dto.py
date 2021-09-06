import attr
from datetime import date
from .food_dto import FoodInFoodPlanOutput

from typing import List


@attr.s
class FoodPlanOutput:
    id: int = attr.ib()
    date_time: date = attr.ib()
    breakfast: FoodInFoodPlanOutput = attr.ib()
    lunch: FoodInFoodPlanOutput = attr.ib()
    dinner: FoodInFoodPlanOutput = attr.ib()

@attr.s
class FoodPlanInput:
    date_time: str = attr.ib()
    breakfast: int = attr.ib()
    lunch: int = attr.ib()
    dinner: int = attr.ib()

@attr.s
class FoodPlanBriefInput:
    breakfast: int = attr.ib()
    lunch: int = attr.ib()
    dinner: int = attr.ib()
