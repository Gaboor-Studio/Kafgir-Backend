from django.db.models import QuerySet
from ..repositories.history_repo import HistoryRepository
from ..models.history import History

class HistoryRepositoryImpl(HistoryRepository):
    ''' This repository implementation holds implementation to all the calls to database relating search history. except for creating history!'''
    model = History

    def get_user_history(self, id: int) -> QuerySet:
        ''' This is a method for user to get all it's search history. '''
        return self.model.objects.filter(user__id=id).order_by('-time')

    def remove_history(self, hid: int) -> None:
        ''' This is a method for user to get rid of a single search history. '''
        self.model.objects.filter(id=hid).delete()
    
    def remove_all_history(self, id: int) -> None:
        ''' This is a method for user to delete all it's search history. '''
        self.model.objects.filter(user__id=id).delete()
    
    def save_history(self, history: History) -> None:
        ''' This is a method for saving a history object. '''
        history.save()