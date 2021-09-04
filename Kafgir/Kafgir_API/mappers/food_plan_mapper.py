from ..models.food_plan import FoodPlan
from ..dto.food_plan_dto import FoodPlanOutput

class FoodPlanOutputMapper:

    def from_model(self, model: FoodPlan) -> FoodPlanOutput:
        if model == None:
            return None

        return FoodPlanOutput(  id=model.pk,
                                date_time=model.date_time,
                                breakfast=model.breakfast.pk,
                                lunch=model.lunch.pk,
                                dinner=model.dinner.pk)

    