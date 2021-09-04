from abc import ABC, abstractmethod

from ..models.food import Food

from typing import List

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
    def find_all(self) -> List[Food]:
        pass