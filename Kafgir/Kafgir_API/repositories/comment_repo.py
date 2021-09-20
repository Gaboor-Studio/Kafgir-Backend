from abc import ABC, abstractmethod

from ..models.comment import Comment
from ..models.food import Food

from typing import List

class CommentRepository(ABC):
    
    @abstractmethod
    def get_some_food_comments(self, food: Food, num: int) -> List[Comment]:
        pass

    @abstractmethod
    def get_food_comments(self, food: Food) -> List[Comment]:
        pass

    @abstractmethod
    def find_comment_by_user_id(self, id: int, food: Food) -> Comment:
        pass

    @abstractmethod
    def are_there_any_user_comment(self, id: int, food: Food) -> bool:
        pass

    @abstractmethod
    def get_some_unconfirmed_comments(self, num: int) -> List[Comment]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Comment:
        pass

    @abstractmethod
    def save(self, comment: Comment) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        pass