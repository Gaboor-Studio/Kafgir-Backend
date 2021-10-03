from django.db.models import QuerySet
from ..repositories.history_repo import HistoryRepository
from ..models.history import History

class HistoryRepositorImpl(HistoryRepository):
    ''' This repository implementation holds implementation to all the calls to database relating search history. except for creating history!'''
    model = History

    def get_user_history(self, id: int) -> QuerySet:
        ''' This is a method for user to get all it's search history. '''
        return self.model.objects.filter(user=id).order_by('-time')

    def remove_history(self, hid: int) -> None:
        ''' This is a method for user to get rid of a single search history. '''
        self.model.objects.filter(id=hid).delete()