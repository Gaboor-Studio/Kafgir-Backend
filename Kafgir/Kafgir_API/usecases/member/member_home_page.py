from abc import ABC, abstractmethod

from ...dto.tag_dto import MainTagOutput, TagOutput
from ...dto.food_plan_dto import FoodPlanInput,FoodPlanOutput
from ...dto.home_page_dto import HomePageOutput
from ...models.user import User

from typing import List

class MemberHomePageUsecase(ABC):
    
    @abstractmethod
    def get_some_food_by_tag_id(self, num: int) -> List[MainTagOutput]:
        pass

    @abstractmethod
    def get_food_plan(self, id: int) -> List[FoodPlanOutput]:
        pass 

    @abstractmethod
    def get_categories(self) -> List[TagOutput]:
        pass

    @abstractmethod
    def load_home_page_for_user(self, id: int, num: int) -> HomePageOutput:
        pass

    @abstractmethod
    def load_home_page_for_guest(self, num: int) -> HomePageOutput:
        pass
