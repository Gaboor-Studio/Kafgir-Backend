from abc import ABC, abstractmethod

from typing import List

from ...dto.comment_dto import CommentInput, CommentOutput, CommentBriefInput
from ...models.user import User
from ...dto.food_dto import FoodOutput
from ...dto.food_dto import FoodOutput, FoodBriefOutput

from django.contrib.auth import get_user_model

class MemberFoodUsecase(ABC):
    '''This is an abstraction for member food service.
    
    It provides some functionalities such as finding the food, adding food ingredients to list, posting comments on foods and ...
    '''
    
    user_model = get_user_model()

    @abstractmethod
    def find_by_id(self, user_id: int, food_id: int) -> FoodOutput:
        '''Finds a food given its id and returns a FoodOutput DTO.'''
        pass 
    
    @abstractmethod
    def add_ingredients_to_list(self, food_id: int, user: user_model) -> None:
        '''Adds all food's ingredients to the user's shopping list.'''
        pass

    @abstractmethod
    def get_some_food_comments(self, food_id: int, num: int) -> List[CommentOutput]:
        '''Gets a number of food comments and returns a list of CommentOutput DTO.'''
        pass 

    @abstractmethod
    def get_food_comments(self, food_id: int) -> List[CommentOutput]:
        '''Gets all comments of the food given its id and returns a list of CommentOutput DTO.'''
        pass 

    @abstractmethod
    def find_comment_by_user_id(self, id: int, food_id: int) -> CommentOutput:
        '''Finds the user comment on the post if exists.'''
        pass

    @abstractmethod
    def add_comment(self, input:  CommentInput, user: User) -> None:
        '''Posts a comment on the food with the given user.'''
        pass
    
    @abstractmethod
    def find_all_with_tag(self, tag_id: int) -> List[FoodBriefOutput]:
        '''Finds all foods which have a specific tag and returns a list of FoodBriefOutput.'''
        pass