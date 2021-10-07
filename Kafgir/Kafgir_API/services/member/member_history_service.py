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
from ...exceptions.common import CannotParseToInt

DEFAULT_HISTORY_COUNT = 5

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

        history = History(user= user, title= input.title, category= category_obj, level= input.level, lct= input.lct, uct= input.uct, ingredients= input.ingredients)
        self.history_repo.save_history(history)
        return self.history_mapper.from_model(history)

    def get_history(self, uid: int, cnt: int) -> List[HistoryOutput]:
        ''' This method returns a user's search history. '''

        if cnt is not None:
            try:
                count = int(cnt)
            except ValueError:
                raise CannotParseToInt(detail='count needs to be an integer(ID)')
        else:
            count= DEFAULT_HISTORY_COUNT

        return list(map(self.history_mapper.from_model, self.history_repo.get_user_history(uid, count)))

    def remove_history(self, hid: int) -> None:
        ''' This method deletes a history record. '''

        try:
            history = self.history_repo.get_history_by_id(hid)
            self.history_repo.delete_history(history)
        except History.DoesNotExist:
            raise HistoryNotFoundException(detail=f'history with id (id={hid}) does not exist.')

    def remove_all_history(self, uid: int) -> None:
        ''' This method deletes all history records that belong to the user with the id of (uid). '''

        self.history_repo.remove_all_history(uid)
    