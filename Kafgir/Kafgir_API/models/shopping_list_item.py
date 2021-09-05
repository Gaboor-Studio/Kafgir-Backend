from django.db import models

from django.db.models.deletion import SET_NULL

from .user import User

class ShoppingListItem(models.Model):

    title = models.CharField(default='' ,max_length=255)
    done = models.BooleanField(default=False)
    amount = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='shopping_list')
