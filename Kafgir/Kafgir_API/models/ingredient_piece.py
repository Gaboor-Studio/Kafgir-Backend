from django.db import models

from .ingredient import Ingredient
from .food import Food, FoodUnit

class IngredientPiece(models.Model):

    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='pieces')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='ingredient_pieces')
    amount = models.CharField(max_length=255, null=False)
