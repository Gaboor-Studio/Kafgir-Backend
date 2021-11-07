from abc import ABC, abstractmethod
from typing import List
from ...dto.history_dto import HistoryInput, HistoryOutput
from ...models.user import User

class MemberHistoryUsecase(ABC):
    ''' This is an interface for what a history servce should look like, defining it's more importatnt methods to be implemented. '''

    @abstractmethod
    def create_history(self, user: User, input: HistoryInput) -> HistoryOutput:
        ''' This method saves a search request as a history. '''
        pass

    @abstractmethod
    def get_history(self, uid: int, cnt: int) -> List[HistoryOutput]:
        ''' This method returns a user's search history or a part of it. '''
        pass

    @abstractmethod
    def remove_history(self, uid: int, hid: int) -> None:
        ''' This method deletes a history record. '''
        pass

    @abstractmethod
    def remove_all_history(self, uid: int) -> None:
        ''' This method deletes all history records that belong to the user with the id of (uid). '''
        pass
    