from django.db.models import QuerySet

from abc import ABC, abstractmethod

from ..models.food import Food
from ..models.tag import Tag

class FoodRepository(ABC):
    '''This is an abstraction for food repository.It handles database queries for CRUD operations on some foods.'''

    @abstractmethod
    def find_by_id(self, id: int) -> Food:
        '''Finds a food given its id. It raises Food.DoesNotExist exception if the food does not exist.'''
        pass

    @abstractmethod
    def save(self, food: Food) -> None:
        '''Saves or updates the given food in database.'''
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        '''Deletes a food given its id.'''
        pass

    @abstractmethod
    def find_all(self) -> QuerySet:
        '''Finds all foods and returns a QuerySet of them.'''
        pass

    @abstractmethod
    def find_all_by_tag_ordered_by_rating(self, tag_id: int) -> QuerySet:
        '''Finds all food in a specific tag given the tag id and orders them by food rating and returns a QuerySet.'''
        pass