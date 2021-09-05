from django.db import models

class Ingredient(models.Model):

    #TODO: add image to ingredient
    #TODO: Decide about colories
    name = models.CharField(max_length=255, null=False, unique=True)
    