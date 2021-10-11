from abc import ABC, abstractmethod

from typing import List

from ...util.paginator import PaginationData,PaginationOutput

from django.contrib.auth import get_user_model

class MemberFoodUsecase(ABC):
    '''This is an abstraction for member food service.
    
    It provides some functionalities such as finding the food, adding food ingredients to list, posting comments on foods and ...
    '''
    
    user_model = get_user_model()

    @abstractmethod
    def find_by_id(self, user_id: int, food_id: int, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds a food given its id and returns a PaginationOutput containing paginated comments.'''
        pass 
    
    @abstractmethod
    def add_ingredients_to_list(self, food_id: int, user: user_model) -> None:
        '''Adds all food's ingredients to the user's shopping list.'''
        pass
    
    @abstractmethod
    def find_all_with_tag(self, tag_id: int, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds all foods which have a specific tag and returns a PaginationOutput.'''
        pass 

    @abstractmethod
    def get_favorite_foods(self, user_id: int, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds the user favourite foods and returns a list of FoodBriefOutput.'''
        pass