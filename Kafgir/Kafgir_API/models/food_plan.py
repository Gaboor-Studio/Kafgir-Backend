from django.db import models

from django.db.models.deletion import SET_NULL

from .food import Food
from .user import User

class FoodPlan(models.Model):
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    breakfast = models.ForeignKey(Food, on_delete=SET_NULL, null=True,related_name='breakfast')
    lunch = models.ForeignKey(Food, on_delete=SET_NULL, null=True ,related_name='lunch')
    dinner = models.ForeignKey(Food, on_delete=SET_NULL, null=True,related_name='dinner')
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='food_plan')