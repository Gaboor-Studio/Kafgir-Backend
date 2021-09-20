from abc import ABC, abstractmethod

from ...dto.tag_dto import MainTagOutput, TagOutput
from ...dto.food_plan_dto import FoodPlanInput,FoodPlanOutput
from ...dto.home_page_dto import HomePageBriefOutput
from ...models.user import User

from typing import List

class MemberHomePageUsecase(ABC):

    @abstractmethod
    def load_home_page(self, id: int, num: int) -> HomePageBriefOutput:
        pass