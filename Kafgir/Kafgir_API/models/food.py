from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator,MaxValueValidator

class FoodUnit(models.TextChoices):
    KILOGRAM = 'Kg', _('Kilogram')
    GRAM = 'g', _('Gram')
    NUMBER = 'num', _('Number')
    LITER = 'lit', _('Liter')
    
class Food(models.Model):

    title = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    cooking_time = models.IntegerField(validators=[MinValueValidator(1)])
    