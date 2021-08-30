from django.db import models

from django.db.models.deletion import SET_NULL

from .user import User

class ShoppingListItem(models.Model):
    kg = 'kg'
    g = 'g'
    Number = 'Number'
    Liter = 'Liter'

    CHOICES = (
        (kg,'kg'),
        (g,"g"),
        (Number,"Number"),
        (Liter,"Liter")
    )

    title = models.CharField(max_length=255)
    done = models.BooleanField()
    amount = models.IntegerField()
    unit = models.CharField(max_length=255, choices=CHOICES, default=kg)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='shopping_list')
