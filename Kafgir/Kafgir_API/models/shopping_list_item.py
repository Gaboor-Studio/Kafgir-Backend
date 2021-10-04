from django.db import models

from django.db.models.deletion import SET_NULL

from django.contrib.auth import get_user_model

user_model = get_user_model()

class ShoppingListItem(models.Model):

    title = models.CharField(default='' ,max_length=255)
    done = models.BooleanField(default=False)
    amount = models.CharField(max_length=255, default='')
    user = models.ForeignKey(user_model, on_delete=SET_NULL, null=True, related_name='shopping_list')
