from django.db import models
from django.db.models.deletion import SET_NULL;
from django.core.validators import MinValueValidator, MaxValueValidator
from .user import User;
from .tag import Tag;

class History(models.Model):
    '''This is a model for representing search histories.\n

    Fields:\n
    user -- The user who requested for the search.\n
    title -- Title of the food.\n
    category -- Category in which we're searching for foods. \n
    level -- The level of the food which is a number between 0 and 2.\n
    cooking_time -- A string containg the time required to cook the food.\n 
    ingredients -- ingredient titles seperated by underscores (_).\n
    time -- The time on which the search request has been made.
    '''    

    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='search_history')
    title = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Tag, on_delete=SET_NULL, null=True)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], null=True)
    cooking_time = models.CharField(max_length=32, null=True)
    ingredients = models.CharField(max_length=1023, null=True)    
    time = models.DateTimeField(auto_now_add=True)