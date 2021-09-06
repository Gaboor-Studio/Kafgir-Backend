from abc import ABC, abstractmethod

from ..models.tag import Tag
from ..models.food import Food

from typing import List


class TagRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> Tag:
        pass

    @abstractmethod
    def find_all(self) -> List[Tag]:
        pass

    @abstractmethod
    def save(self, tag: Tag) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        pass

    @abstractmethod
    def find_main_tag(self) -> List[Tag]:
        pass

    @abstractmethod
    def find_primary_tag(self) -> List[Tag]:
        pass

    @abstractmethod
    def get_some_food_by_tag_id(self, id: int, num: int) -> List[Food]:
        pass