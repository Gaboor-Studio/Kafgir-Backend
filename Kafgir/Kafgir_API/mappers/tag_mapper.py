from ..models.tag import Tag
from ..models.food import Food
from ..dto.tag_dto import TagOutput, MainTagOutput, PrimaryTagOutput

from .food_mappers import FoodInFoodPlanMapper

from dependency_injector.wiring import inject, Provide

from typing import List

class TagMapper:

    def from_model(self, model: Tag) -> TagOutput:
        if model == None:
            return None

        return TagOutput(   id=model.pk,
                            title=model.title,
                            is_main=model.is_main,
                            is_primary=model.is_primary,
                            display_order=model.display_order)

class PrimaryTagMapper:

    def from_model(self, model: Tag) -> PrimaryTagOutput:
        if model == None:
            return None

        return PrimaryTagOutput(   id=model.pk,
                                    title=model.title
                                    )

class MainTagMapper:

    @inject
    def __init__(self, food_in_food_plan_mapper: FoodInFoodPlanMapper = Provide['food_in_food_plan_mapper']):
        
        self.food_in_food_plan_mapper = food_in_food_plan_mapper
                       
    def from_model(self, model: Tag, foods:List[Food]) -> MainTagOutput:
        if model == None:
            return None

        return MainTagOutput(   id=model.pk,
                                title=model.title,
                                foods=list(map(self.food_in_food_plan_mapper.from_model, foods))
                                )               
