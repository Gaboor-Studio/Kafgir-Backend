from django.db import models

from django.db.models.deletion import SET_NULL
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator

user_model = get_user_model()

class Commentable(models.Model):
    rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)

    class Meta:
        abstract = True

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
    
    user = models.ForeignKey(user_model, on_delete=SET_NULL, null=True, related_name='comments')
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.TextField(null=True)
    confirmed = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()