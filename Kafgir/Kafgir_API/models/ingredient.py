from django.db import models

class Ingredient(models.Model):
    '''This is a model for ingredients.\n
    
    Fields:\n
    name: The name of the ingredient.
    '''

    #TODO: add image to ingredient
    #TODO: Decide about colories
    name = models.CharField(max_length=255, null=False, unique=True)
    