from abc import ABC, abstractmethod

from typing import List

from ...dto.food_dto import FoodOutput,FoodInput, FoodBriefOutput

from ...util.paginator import PaginationData,PaginationOutput

class AdminFoodUsecase(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> FoodOutput:
        pass

    @abstractmethod
    def load_all(self, pagination_data: PaginationData) -> PaginationOutput:
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        pass

    @abstractmethod
    def create_food(self, input: FoodInput) -> FoodOutput:
        pass
    

    