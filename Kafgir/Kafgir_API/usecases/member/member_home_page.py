from abc import ABC, abstractmethod

from ...dto.tag_dto import MainTagOutput
from ...models.user import User

from typing import List

class MemberHomePageUsecase(ABC):
    
    @abstractmethod
    def get_some_food_by_tag_id(self, num: int) -> List[MainTagOutput]:
        pass