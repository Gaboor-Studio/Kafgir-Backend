from django.db.models import QuerySet

from abc import ABC, abstractmethod

class HistoryRepository(ABC):
    ''' This repository holds on to all the calls to database relating search history. except for creating history!'''

    @abstractmethod
    def get_user_history(self, id: int) -> QuerySet:
        ''' This is a method for user to get all it's search history. '''
        pass

    @abstractmethod
    def remove_history(self, uid: int, hid: int) -> None:
        ''' This is a method for user to get rid of a single search history. '''
        pass