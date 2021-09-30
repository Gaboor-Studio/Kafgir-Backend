from django.db import models

from django.db.models.deletion import SET_NULL

from .food import Food
from .user import User

from django.core.validators import MinValueValidator,MaxValueValidator

class Comment(models.Model):
    '''This is a model for comments.\n

    Fields:\n
    user -- The user object.\n
    food -- The food object.\n
    date_time -- Message time.\n
    rating -- The score of the food which is a number between 0 and 10.\n
    text -- Comment content.\n
    confirmed -- This field specifies whether this comment is allowed to be displayed. 
    '''
    
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='comments')
    food = models.ForeignKey(Food, on_delete=SET_NULL, null=True,related_name='comments') 
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.TextField(null=True)
    confirmed = models.BooleanField(default=False)