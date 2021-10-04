from django.db.models import QuerySet
from ..repositories.history_repo import HistoryRepository
from ..models.history import History

class HistoryRepositoryImpl(HistoryRepository):
    ''' This repository implementation holds implementation to all the calls to database relating search history. except for creating history!'''
    model = History

    def get_user_history(self, id: int, cnt: int) -> QuerySet:
        ''' This is a method for user to get all ( or a part of ) it's search history. '''
        return self.model.objects.filter(user__id=id).order_by('-time')[:cnt]

    def get_history_by_id(self, hid: int) -> History:
        ''' This is a method for user to get a history using it's id. '''
        return self.model.objects.get(id=hid)
    
    def remove_all_history(self, id: int) -> None:
        ''' This is a method for user to delete all it's search history. '''
        self.model.objects.filter(user__id=id).delete()
    
    def save_history(self, history: History) -> None:
        ''' This is a method for saving a history object. '''
        history.save()

    def delete_history(self, history: History) -> None:
        ''' This method deletes a history record. '''
        history.delete()