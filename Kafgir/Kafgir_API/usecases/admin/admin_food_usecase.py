from abc import ABC, abstractmethod

from typing import List

from ...dto.food_dto import FoodInput,AdminFoodDetailsOutput
from ...util.paginator import PaginationData,PaginationOutput

class AdminFoodUsecase(ABC):
    '''This an abstraction of AdminFoodService. It handles food use cases in admin side.'''

    @abstractmethod
    def find_by_id(self, id: int) -> AdminFoodDetailsOutput:
        '''Finds a food by its id.'''
        pass

    @abstractmethod
    def load_all(self, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds a paginated list of foods given pagination data which are the page size and number.'''
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        '''Deletes a food by its id.'''
        pass

    @abstractmethod
    def create_food(self, input: FoodInput) -> AdminFoodDetailsOutput:
        '''Creates a new food.'''
        pass
    

    