from abc import ABC, abstractmethod

from ..models.comment import Comment
from django.db.models import QuerySet
from django.contrib.contenttypes.models import ContentType

from typing import List

class CommentRepository(ABC):
    '''This is an abstraction for comment repository. it handels database operations for comments.'''

    @abstractmethod
    def find_all_by_confirmed_and_model_order_by_datetime_desc(self, obj_id: int, content_type: ContentType, confirmed: bool) -> QuerySet:
        '''Finds all comments by confirmed ordered by datetime. It finds the comments using commentable object_id and content_type.'''
        pass

    @abstractmethod
    def find_by_user_id_and_model(self, user_id: int, obj_id: int, content_type: ContentType) -> Comment:
        '''Finds the comment by user if exists. It finds the comment using commentable object_id and content_type.'''
        pass

    @abstractmethod
    def exist_by_user_id_and_model(self, user_id: int, obj_id: int, content_type: ContentType) -> bool:
        '''Checks if a comment exists by user. It finds the cooments using commentable object_id and content_type.'''
        pass
    
    @abstractmethod
    def find_all_by_confirmed_ordered_by_datetime_desc(self, confirmed: bool) -> QuerySet:
        '''Finds all comments by confirmed ordered by datetime.'''
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Comment:
        '''Finds a comment by its id.'''
        return Comment.objects.get(pk=id)

    @abstractmethod
    def save(self, comment: Comment) -> None:
        '''Saves a comment given its object.'''
        pass

    @abstractmethod
    def create(self, content_object, user, text, rating, confirmed=False) -> None:
        '''Saves a comment given its data.'''
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        '''Deletes a comment by its id.'''
        pass