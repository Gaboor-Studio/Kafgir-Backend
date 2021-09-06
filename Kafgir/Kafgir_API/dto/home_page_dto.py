import attr

from .tag_dto import TagOutput, MainTagOutput
from .food_plan_dto import FoodPlanOutput

from typing import List

@attr.s
class HomePageOutput:
    food_plan: List[FoodPlanOutput] = attr.ib()
    main_tags: List[MainTagOutput] = attr.ib()
    categories: List[TagOutput] = attr.ib()
    
