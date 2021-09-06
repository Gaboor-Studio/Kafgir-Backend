from django.db import models
from .food import Food

class Tag(models.Model):

    #TODO: add image

    title = models.CharField(max_length=255, default='')
    is_main = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    food = models.ManyToManyField(Food, related_name="tags")
