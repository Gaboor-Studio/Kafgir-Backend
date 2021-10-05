from ..repositories.comment_repo import CommentRepository

from ..models.comment import Comment,Commentable
from ..models.food import Food
from django.contrib.contenttypes.models import ContentType

from typing import List
from django.db.models import Q,QuerySet

class CommentRepositoryImpl(CommentRepository):
    
    def find_all_by_confirmed_and_model_order_by_datetime_desc(self, obj_id: int, content_type: ContentType, confirmed: bool = True) -> QuerySet:
        '''Finds all comments by confirmed ordered by datetime. It finds the comments using commentable object_id and content_type.'''
        return Comment.objects.filter(Q(content_type=content_type), Q(object_id=obj_id) , Q(confirmed=confirmed) , ~Q(text='')).order_by('-date_time')

    def find_by_user_id_and_model(self, user_id: int, obj_id: int, content_type: ContentType) -> Comment:
        '''Finds the comment by user if exists. It finds the comment using commentable object_id and content_type.'''
        return Comment.objects.get(user=user_id, object_id=obj_id, content_type=content_type)

    def exist_by_user_id_and_model(self, user_id: int, obj_id: int, content_type: ContentType) -> bool:
        '''Checks if a comment exists by user. It finds the cooments using commentable object_id and content_type.'''
        return Comment.objects.filter(user=user_id, object_id=obj_id, content_type=content_type).exists()

    def find_all_by_confirmed_ordered_by_datetime_desc(self, confirmed: bool) -> QuerySet:
        '''Finds all comments by confirmed ordered by datetime.'''
        return Comment.objects.filter(confirmed=confirmed)

    def find_by_id(self, id: int) -> Comment:
        return Comment.objects.get(pk=id)

    def save(self, comment: Comment) -> None:
        comment.save()

    def create(self, content_object, user, text, rating, confirmed=False) -> None:
        '''Saves a comment given its data.'''
        Comment.objects.create(content_object=content_object,user=user,confirmed=False,text=text,rating=rating)

    def delete_by_id(self, id: int) -> None:
        Comment.objects.filter(id=id).delete()