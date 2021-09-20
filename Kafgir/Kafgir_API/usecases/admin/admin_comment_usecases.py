from abc import ABC, abstractmethod

from ...dto.comment_dto import CommentInput, CommentOutput, CommentBriefInput, CommentIdListInput
from ...models.user import User

from typing import List

class AdminCommentUsecase(ABC):

    @abstractmethod
    def get_some_unconfirmed_comments(self, num: int) -> List[CommentOutput]:
        pass 
    
    @abstractmethod
    def confirm_the_comment(self, comment_id: int) -> None:
        pass 

    @abstractmethod
    def confirm_comments(self, comments: CommentIdListInput) -> None:
        pass 

    @abstractmethod
    def get_some_food_comments(self, food_id: int, num: int) -> List[CommentOutput]:
        pass 

    @abstractmethod
    def get_food_comments(self, food_id: int) -> List[CommentOutput]:
        pass 

    @abstractmethod
    def update_comment(self, comment_id: int, input:  CommentBriefInput) -> None:
        pass

    @abstractmethod
    def remove_comment(self, comment_id: int) -> None:
        pass