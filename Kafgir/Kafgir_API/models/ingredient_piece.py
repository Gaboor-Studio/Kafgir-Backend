from django.db import models

from .ingredient import Ingredient
from .food import Food

class IngredientPiece(models.Model):
    '''This is a model for representing needed ingredients for each food and their amount.\n

    Fields:\n
    ingredient -- The ingredient object\n
    food -- The food object which the ingredient piece is belong to.\n
    amount -- The amount of the ingredient in the food.
    '''

    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='pieces')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='ingredient_pieces')
    amount = models.CharField(max_length=255, null=False)
