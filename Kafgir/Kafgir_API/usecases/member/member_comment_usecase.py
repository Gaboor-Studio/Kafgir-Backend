from abc import ABC, abstractmethod

from ...dto.comment_dto import CommentOutput,CommentInput
from ...util.paginator import PaginationData,PaginationOutput

from django.contrib.auth import get_user_model

user_model = get_user_model()

class MemberCommentUsecase(ABC):
    '''This is an abstraction for member comment service.
    
    It provides some functionalities such as updating comments and removing comments ...
    '''
    
    @abstractmethod
    def update_comment(self, comment_id: int, input:  CommentInput) -> None:
        '''Updates the comment of the user.'''
        pass

    @abstractmethod
    def remove_comment(self, comment_id: int) -> None:
        '''Removes the comment of the user.'''
        pass

    @abstractmethod
    def get_all_comments_of_model(self, model_class, model_id: int, pagination_data: PaginationData, confirmed = True) -> PaginationOutput:
        pass

    @abstractmethod
    def find_comment_by_user_id(self, user_id: int, model_class, model_id: int) -> CommentOutput:
        '''Finds the user comment on the post if exists.'''
        pass

    @abstractmethod
    def add_comment(self, model_class, model_id: int, user: user_model, input:  CommentInput) -> None:
        '''Posts a comment on the model with the given user.'''
        pass