import attr

from .tag_dto import TagOutput, MainTagOutput, PrimaryTagOutput
from .food_plan_dto import FoodPlanOutput

from typing import List

@attr.s
class HomePageBriefOutput:
    main_tags: List[MainTagOutput] = attr.ib()
    categories: List[PrimaryTagOutput] = attr.ib()
    

@attr.s
class HomePageOutput(HomePageBriefOutput):
    food_plan: List[FoodPlanOutput] = attr.ib()
    
    

    
