from django.db import models

from django.db.models.deletion import SET_NULL

from .user import User
from .food import FoodUnit

class ShoppingListItem(models.Model):

    title = models.CharField(default='' ,max_length=255)
    done = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
    unit = models.CharField(max_length=255, choices=FoodUnit.choices, default=FoodUnit.KILOGRAM)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='shopping_list')
