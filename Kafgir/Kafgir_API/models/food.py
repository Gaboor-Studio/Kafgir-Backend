from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Transform, CharField

from django.contrib.auth import get_user_model
from .comment import Commentable, Comment


user_model = get_user_model()

def food_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<filename>
    return f'foods/{filename}'

class Food(Commentable):
    '''This is a model for representing foods.\n

    Fields:\n
    title -- Title of the food.\n
    rating -- Rating of the food which is the average of the ratings sent by users.\n
    rating_count -- Number of the users who rated the food.\n
    level -- The level of the food which is a number between 0 and 2.\n
    cooking_time -- A string containg the time required to cook the food.\n 
    image -- image of the food.
    '''

    title = models.CharField(max_length=255)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    cooking_time = models.CharField(max_length=32)
    image = models.ImageField(upload_to=food_directory_path, null=True)
    comments = GenericRelation(Comment, related_query_name='food')
    users = models.ManyToManyField(user_model, related_name='favorite_of')

    def get_image(self):
        if not self.image:
            return 'no-image'
        return self.image.url


# class CookingTimeToMinutesTransform(Transform):

#     lookup_name = "tominute"

#     def as_sql(self, compiler, connection):
#         lhs, params = compiler.compile(self.lhs)
#         sql ="""
#                 {}
#             """
#         return sql.format(lhs), params

#     @property
#     def output_field(self):
#         return models.IntegerField()
    
# CharField.register_lookup(CookingTimeToMinutesTransform)

# from django.db.models.sql.compiler import SQLCompiler
# from django.db.backends.mysql.base import BaseDatabaseWrapper

# SQLCompiler.