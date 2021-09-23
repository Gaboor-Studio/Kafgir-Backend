from django.db import models

from .food import Food

class RecipeItem(models.Model):
    '''This is a model to represent a recipe item in a food.
    
    Fields:\n
    food -- The food of the recipe.\n
    text -- content of the recipe.\n
    step -- step of the recipe item.
    '''

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='recipe_items')
    text = models.TextField(null=False)
    step = models.IntegerField(null=False)