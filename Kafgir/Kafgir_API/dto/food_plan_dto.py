import attr
from datetime import date

@attr.s
class FoodPlanOutput:
    id: int = attr.ib()
    date_time: date = attr.ib()
    breakfast: int = attr.ib()
    lunch: int = attr.ib()
    dinner: int = attr.ib()

@attr.s
class FoodPlanInput:
    date_time: str = attr.ib()
    breakfast: int = attr.ib()
    lunch: int = attr.ib()
    dinner: int = attr.ib()
