from django.db import models

from django.db.models.deletion import SET_NULL

from .comment import Comment
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Report(models.Model):
    
    user = models.ForeignKey(user_model, on_delete=SET_NULL, null=True, related_name='reports')
    Comment = models.ForeignKey(Comment, on_delete=SET_NULL, null=True,related_name='reports') 
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(null=True)
