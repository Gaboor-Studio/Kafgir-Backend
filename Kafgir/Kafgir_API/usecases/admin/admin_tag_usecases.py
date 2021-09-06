from abc import ABC, abstractmethod

from ...dto.tag_dto import TagInput,TagOutput

from typing import List

class AdminTagUsecase(ABC):
    
    @abstractmethod
    def find_all(self) -> List[TagOutput]:
        pass 

    @abstractmethod
    def find_by_id(self, id: int) -> TagOutput:
        pass 

    @abstractmethod
    def create_new_tag(self, input:  TagInput) -> None:
        pass

    @abstractmethod
    def update_tag(self, id: int, input:  TagInput) -> None:
        pass

    @abstractmethod
    def remove_tag(self, id: int) -> None:
        pass