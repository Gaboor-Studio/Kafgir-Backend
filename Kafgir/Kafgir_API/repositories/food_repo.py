from abc import ABC, abstractmethod

from django.db.models import QuerySet

from ..models.food import Food
from ..models.tag import Tag

class FoodRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> Food:
        pass

    @abstractmethod
    def save(self, food: Food) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        pass

    @abstractmethod
    def find_all(self) -> QuerySet:
        pass

    @abstractmethod
    def find_all_by_tag_ordered_by_rating(self, tag_id: int) -> QuerySet:
        pass