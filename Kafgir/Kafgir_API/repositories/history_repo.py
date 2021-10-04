from django.db.models import QuerySet
from abc import ABC, abstractmethod

from ..models.history import History

class HistoryRepository(ABC):
    ''' This repository holds on to all the calls to database relating search history. except for creating history!'''

    @abstractmethod
    def get_user_history(self, id: int, cnt: int) -> QuerySet:
        ''' This is a method for user to get all ( or a part of ) it's search history. '''
        pass

    @abstractmethod
    def get_history_by_id(self, hid: int) -> History:
        ''' This is a method for user to get a history using it's id. '''
        pass

    @abstractmethod
    def remove_all_history(self, uid: int) -> None:
        ''' This is a method for user to delete all it's search history. '''
        pass

    @abstractmethod 
    def save_history(self, history: History) -> None:
        ''' This is a method for saving a history object. '''
        pass

    @abstractmethod
    def delete_history(self, history: History) -> None:
        ''' This method deletes a history record. '''
        pass