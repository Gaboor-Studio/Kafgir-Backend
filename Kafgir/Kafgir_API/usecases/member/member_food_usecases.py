from abc import ABC, abstractmethod

from typing import List

from ...dto.comment_dto import CommentInput, CommentOutput, CommentBriefInput
from ...models.user import User
from ...dto.food_dto import FoodOutput
from ...dto.food_dto import FoodOutput, FoodBriefOutput

from django.contrib.auth import get_user_model

class MemberFoodUsecase(ABC):
    
    user_model = get_user_model()

    @abstractmethod
    def find_by_id(self, user_id: int, food_id: int) -> FoodOutput:
        pass 
    
    @abstractmethod
    def add_ingredients_to_list(self, food_id: int, user: user_model) -> None:
        pass

    @abstractmethod
    def get_some_food_comments(self, food_id: int, num: int) -> List[CommentOutput]:
        pass 

    @abstractmethod
    def get_food_comments(self, food_id: int) -> List[CommentOutput]:
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
    
    @abstractmethod
    def find_all_with_tag(self, tag_id: int) -> List[FoodBriefOutput]:
        pass