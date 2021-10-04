from dependency_injector.wiring import Provide, inject
from typing import List

from ...dto.food_dto import FoodBriefOutput
from ...dto.history_dto import HistoryInput
from ...models.food import Food
from ...models.user import User
from ...usecases.member.search_usecases import SearchUsecase
from ...usecases.member.member_history_usecase import MemberHistoryUsecase
from ...mappers.food_mappers import FoodBriefMapper
from ...exceptions.bad_request import SearchFieldMissing
from ...exceptions.common import CannotParseToInt


class SearchService(SearchUsecase):
    ''' This class contains all different ways to do a search for any entity in database'''

    @inject
    def __init__(self, food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper']
                     , member_history_usecase: MemberHistoryUsecase = Provide['member_history_usecase']) -> None:
        super().__init__()
        self.food_brief_mapper = food_brief_mapper
        self.member_history_usecase = member_history_usecase

    def search_for_food(self, user: User, title: str, category: int, ingredients: str, level: int, cooking_time: int) -> List[FoodBriefOutput]:
        ''' Search for a group of specific foods using their names, category, ingredients, level and cooking time'''

        query_set = Food.objects
        
        ''' title is the only required field '''
        if title is None:
            raise SearchFieldMissing(detail="food title you're looking for is being missed")
        else :
            query_set = query_set.filter(title__icontains=title)

        ''' rest of attributes are not required so we apply filters if and only if they exist '''
        if level is not None:
            try:
                temp_level = int(level)
                query_set = query_set.filter(level=temp_level)
            except ValueError:
                raise CannotParseToInt(detail='level needs to be an integer')
        else:
            temp_level= None

        if cooking_time is not None:
            try:
                temp_time = int(cooking_time)
                query_set = query_set.filter(cooking_time__range=(temp_time-15, temp_time+15))
            except ValueError:
                raise CannotParseToInt(detail='cooking time needs to be an integer')
        else: 
            temp_time = None

        if category is not None:
            try:
                temp_id = int(category)
                query_set = query_set.filter(tags__id=temp_id, tags__is_primary=True)
            except ValueError:
                raise CannotParseToInt(detail='category needs to be an integer(ID)')
        else:
            temp_id= None

        if ingredients is not None:
            ingredients_list = ingredients.split('_')
            for ing in ingredients_list:
                query_set = query_set.filter(ingredient_pieces__ingredient__name=ing)

        ''' In this part we create the history record for the search and save it to the database. '''

        input = HistoryInput(title= title, category= temp_id, level= temp_level, cooking_time= cooking_time, ingredients= ingredients)

        self.member_history_usecase.create_history(user, input)

        return list(map(self.food_brief_mapper.from_model, query_set))