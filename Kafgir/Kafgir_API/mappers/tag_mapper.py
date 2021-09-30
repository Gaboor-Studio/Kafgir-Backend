from ..models.tag import Tag
from ..models.food import Food
from ..dto.tag_dto import TagOutput, MainTagOutput, PrimaryTagOutput

from .food_mappers import FoodInFoodPlanMapper

from dependency_injector.wiring import inject, Provide

from typing import List

class TagMapper:
    ''' This is a mapper for converting tag default model to TagOutput DTO'''

    def from_model(self, model: Tag) -> TagOutput:
        '''Takes a model of tag and converts it to TagOutput DTO'''

        if model == None:
            return None

        return TagOutput(   id=model.pk,
                            title=model.title,
                            is_main=model.is_main,
                            is_primary=model.is_primary,
                            image=model.get_image(),
                            display_order=model.display_order)

class PrimaryTagMapper:
    ''' This is a mapper for converting tag default model to PrimaryTagOutput DTO'''

    def from_model(self, model: Tag) -> PrimaryTagOutput:
        '''Takes a model of tag and converts it to PrimaryTagOutput DTO'''

        if model == None:
            return None

        return PrimaryTagOutput(    id=model.pk,
                                    image=model.get_image(),
                                    title=model.title
                                    )

class MainTagMapper:
    '''This class uses the FoodInFoodPlanMapper class to convert the default tag model to MainTagOutput DTO.'''

    @inject
    def __init__(self, food_in_food_plan_mapper: FoodInFoodPlanMapper = Provide['food_in_food_plan_mapper']):
        
        self.food_in_food_plan_mapper = food_in_food_plan_mapper
                       
    def from_model(self, model: Tag, foods:List[Food]) -> MainTagOutput:
        '''Takes a model of tag and converts it to MainTagOutput DTO'''

        if model == None:
            return None

        return MainTagOutput(   id=model.pk,
                                title=model.title,
                                foods=list(map(self.food_in_food_plan_mapper.from_model, foods))
                                )               
