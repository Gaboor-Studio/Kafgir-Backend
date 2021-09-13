from abc import ABC, abstractmethod

from ...dto.comment_dto import CommentInput, CommentOutput, CommentBriefInput
from ...models.user import User

from typing import List

class MemberCommentUsecase(ABC):

    @abstractmethod
    def get_some_food_comments(self, food_id: int, num: int) -> List[CommentOutput]:
        pass 

    @abstractmethod
    def get_food_comments(self, food_id: int) -> List[CommentOutput]:
        pass 

    @abstractmethod
    def find_comment_by_user_id(self, id: int, food_id: int) -> CommentOutput:
        pass

    @abstractmethod
    def add_comment(self, input:  CommentInput, user: User) -> None:
        pass

    @abstractmethod
    def update_comment(self, comment_id: int, input:  CommentBriefInput) -> None:
        pass

    @abstractmethod
    def remove_comment(self, comment_id: int) -> None:
        pass