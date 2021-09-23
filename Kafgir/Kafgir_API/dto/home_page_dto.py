import attr

from .tag_dto import TagOutput, MainTagOutput, PrimaryTagOutput
from .food_plan_dto import FoodPlanOutput

from typing import List

@attr.s
class HomePageOutput:
    '''This is a DTO for displaying categories, main tags and meal plans on the Home page.'''

    main_tags: List[MainTagOutput] = attr.ib()
    categories: List[PrimaryTagOutput] = attr.ib()
    food_plan: List[FoodPlanOutput] = attr.ib()
    
    

    
