from django.db import models

from django.db.models.deletion import SET_NULL

from .food import Food
from .user import User

class Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='comments')
    food = models.ForeignKey(Food, on_delete=SET_NULL, null=True,related_name='comments') 
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)
    text = models.TextField(null=True)
    confirmed = models.BooleanField(default=False)