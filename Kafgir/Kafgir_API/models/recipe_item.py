from django.db import models

from .ingredient import Ingredient
from .food import Food


class RecipeItem(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='recipe_items')
    text = models.TextField(null=False)
    step = models.IntegerField(null=False)