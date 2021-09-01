from ..repositories.food_planning_repo import FoodPlanningRepository

from ..models.food_plan import FoodPlan

from typing import List
from datetime import date, timedelta
from django.db.models import Q

class FoodPlanningRepositoryImpl(FoodPlanningRepository):

    def find_food_plan_by_id(self, id: int) -> FoodPlan:
        return FoodPlan.objects.get(pk=id)

    def find_food_plan_by_date(self, id: int, start_date: date, end_date: date) -> List[FoodPlan]:
        return FoodPlan.objects.filter(date_time__lte = end_date, date_time__gte = start_date, user=id)

    def save_food_plan(self, food_plan: FoodPlan) -> None:
        food_plan.save()

    def delete_food_plan(self, plan_id: int) -> None:
        FoodPlan.objects.filter(id=plan_id).delete()