from dependency_injector.wiring import Provide, inject
from typing import List

from ...usecases.member.member_history_usecase import MemberHistoryUsecase
from ...dto.history_dto import HistoryInput, HistoryOutput
from ...repositories.tag_repo import TagRepository
from ...repositories.history_repo import HistoryRepository
from ...mappers.history_mappers import HistoryMapper
from ...models.history import History
from ...models.user import User
from ...models.tag import Tag
from ...exceptions.not_found import UserNotFoundException, TagNotFoundException, HistoryNotFoundException

class MemberHistoryService(MemberHistoryUsecase):
    ''' This is an implementation to MemberHistoryUsecase for user to be able to play with history and stuff. '''

    @inject
    def __init__(self, history_repo: HistoryRepository = Provide['history_repo'], 
                       history_mapper: HistoryMapper = Provide['history_mapper'],
                       tag_repo: TagRepository = Provide['tag_repo']) -> None:
        super().__init__()
        self.history_repo = history_repo
        self.history_mapper = history_mapper
        self.tag_repo = tag_repo

    def create_history(self, user: User, input: HistoryInput) -> HistoryOutput:
        ''' This method saves a search request as a history. '''
        if user is None:
            raise UserNotFoundException()

        try:
            if input.category is not None:
                category_obj = self.tag_repo.find_by_id(input.category)
            else:
                category_obj = None
        except Tag.DoesNotExist:
            raise TagNotFoundException()

        history = History(user= user, title= input.title, category= category_obj, level= input.level, cooking_time= input.cooking_time, ingredients= input.ingredients)
        self.history_repo.save_history(history)
        return self.history_mapper.from_model(history)

    def get_history(self, uid: int) -> List[HistoryOutput]:
        ''' This method returns a user's search history. '''
        return list(map(self.history_mapper.from_model, self.history_repo.get_user_history(uid)))

    def remove_history(self, hid: int) -> None:
        ''' This method deletes a history record. '''
        try:
            self.history_repo.remove_history(hid)
        except History.DoesNotExist:
            raise HistoryNotFoundException()
    