from dependency_injector.wiring import Provide, inject

from ..models.history import History
from ..dto.history_dto import HistoryOutput
from ..mappers.tag_mapper import PrimaryTagMapper

class HistoryMapper:
    ''' This mapper class has methods for programmer to be able to output a History record in a HistoryOutput DTO. '''

    @inject
    def __init__(self, primary_tag_mapper: PrimaryTagMapper = Provide['primary_tag_mapper']) -> None:
        self.primary_tag_mapper = primary_tag_mapper

    def from_model(self, model: History) -> HistoryOutput:
        ''' This method gets a history record as input and returns it's data containd in a HistoryOutput DTO. '''

        if model is None:
            return None

        return HistoryOutput(
            title= model.title,
            category= self.primary_tag_mapper.from_model(model.category),
            level= model.level,
            cooking_time= model.cooking_time,
            ingredients= model.ingredients.split('_') if model.ingredients is not None else None,
            time= model.time
        )
