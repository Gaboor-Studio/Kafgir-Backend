from abc import ABC, abstractmethod

from ...dto.comment_dto import CommentInput, CommentOutput, CommentIdListInput
from ...models.user import User
from ...util.paginator import PaginationData,PaginationOutput
from typing import List

class AdminCommentUsecase(ABC):

    @abstractmethod
    def get_comment(self, comment_id: int) -> CommentOutput:
        '''This method returns a comment given its id.'''
        pass

    @abstractmethod
    def get_comments_by_confirmed(self, confirmed: bool, pagination_data: PaginationData) -> PaginationOutput:
        '''This method returns a list of paginated comments with respect to confirmed field.'''
        pass 
    
    @abstractmethod
    def confirm_the_comment(self, comment_id: int) -> None:
        '''This method receives a comment ID to confirm user comment .'''
        pass 

    @abstractmethod
    def confirm_comments(self, comments: CommentIdListInput) -> None:
        '''This method receives a list of comment IDs for confirming user comments .'''
        pass 

    @abstractmethod
    def update_comment(self, comment_id: int, input:  CommentInput) -> None:
        '''updates a comment .'''
        pass

    @abstractmethod
    def remove_comment(self, comment_id: int) -> None:
        '''deletes a comment by ID.'''
        pass