from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator
    
class Food(models.Model):
    '''This is a model for representing foods.\n

    Fields:\n
    title -- Title of the food.\n
    rating -- Rating of the food which is the average of the ratings sent by users.\n
    rating_count -- Number of the users who rated the food.\n
    level -- The level of the food which is a number between 0 and 2.\n
    cooking_time -- A string containg the time required to cook the food. 
    '''
    
    #TODO: add image

    title = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    cooking_time = models.CharField(max_length=32)
    