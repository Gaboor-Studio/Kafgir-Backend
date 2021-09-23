from ..models.food_plan import FoodPlan
from ..dto.food_plan_dto import FoodPlanOutput
from ..models.food import Food

from .food_mappers import FoodInFoodPlanMapper

from dependency_injector.wiring import inject, Provide

from typing import List

class FoodPlanOutputMapper:
    
    @inject
    def __init__(self, food_in_food_plan_mapper: FoodInFoodPlanMapper = Provide['food_in_food_plan_mapper']):
        
        self.food_in_food_plan_mapper = food_in_food_plan_mapper

    def from_model(self, model: FoodPlan) -> FoodPlanOutput:
        if model == None:
            return None

        return FoodPlanOutput(  id=model.pk,
                                date_time=model.date_time,
                                breakfast=self.food_in_food_plan_mapper.from_model(model.breakfast),
                                lunch=self.food_in_food_plan_mapper.from_model(model.lunch),
                                dinner=self.food_in_food_plan_mapper.from_model(model.dinner)
                                )               

    