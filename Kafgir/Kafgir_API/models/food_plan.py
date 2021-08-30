from django.db import models

from django.db.models.deletion import SET_NULL

from .food import Food
from .user import User

class FoodPlan(models.Model):
    date_time = models.DateTimeField()
    breakfast = models.ForeignKey(Food, on_delete=SET_NULL, null=True)
    lunch = models.ForeignKey(Food, on_delete=SET_NULL, null=True)
    dinner = models.ForeignKey(Food, on_delete=SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='food_plan')