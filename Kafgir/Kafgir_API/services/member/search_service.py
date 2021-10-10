from attr import attrs
import attr
import cattr
from dependency_injector.wiring import Provide, inject
from typing import List

from ...dto.food_dto import FoodBriefOutput
from ...dto.history_dto import HistoryInput
from ...dto.search_dto import SearchInput
from ...models.food import Food
from ...models.user import User
from ...usecases.member.search_usecases import SearchUsecase
from ...usecases.member.member_history_usecase import MemberHistoryUsecase
from ...mappers.food_mappers import FoodBriefMapper
from ...exceptions.bad_request import SearchFieldMissing, WrongPairOfBoundsException
from ...exceptions.common import CannotParseToInt


class SearchService(SearchUsecase):
    ''' This class contains all different ways to do a search for any entity in database'''

    @inject
    def __init__(self, food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper']
                     , member_history_usecase: MemberHistoryUsecase = Provide['member_history_usecase']) -> None:
        super().__init__()
        self.food_brief_mapper = food_brief_mapper
        self.member_history_usecase = member_history_usecase

    def search_for_food(self, user: User, input: SearchInput) -> List[FoodBriefOutput]:
        ''' Search for a group of specific foods using their names, category, ingredients, level and cooking time'''

        query_set = Food.objects
        
        ''' title is the only required field '''
        if input.title is None:
            raise SearchFieldMissing(detail="food title you're looking for is being missed")
        else :
            query_set = query_set.filter(title__icontains=input.title)

        ''' rest of attributes are not required so we apply filters if and only if they exist '''
        if input.level is not None:
            try:
                temp_level = int(input.level)
                query_set = query_set.filter(level=temp_level)
            except ValueError:
                raise CannotParseToInt(detail='level needs to be an integer')
        else:
            temp_level= None

        try:
            if input.lct is not None:
                temp_lct = int(input.lct)
                if input.uct is not None:
                    temp_uct = int(input.uct)
                    if temp_lct <= temp_uct:
                        query_set = query_set.filter(cooking_time__tominute__range=(temp_lct, temp_uct))
                    else:
                        raise WrongPairOfBoundsException(detail='lower bound is greater than upper!')
                else:
                    query_set = query_set.filter(cooking_time__tominute__gt=temp_lct)
            else:
                if input.uct is not None:
                    temp_uct = int(input.uct)
                    query_set = query_set.filter(cooking_time__tominute__lt=temp_uct)
                else:
                    pass
        except ValueError:
            raise CannotParseToInt()


        if input.category is not None:
            try:
                temp_id = int(input.category)
                query_set = query_set.filter(tags__id=temp_id, tags__is_primary=True)
            except ValueError:
                raise CannotParseToInt(detail='category needs to be an integer(ID)')
        else:
            temp_id= None

        if input.ingredients is not None:
            ingredients_list = input.ingredients.split('_')
            for ing in ingredients_list:
                query_set = query_set.filter(ingredient_pieces__ingredient__name=ing)

        ''' In this part we create the history record for the search and save it to the database. '''

        filtered = {k: input.__dict__[k] for k in input.__dict__.keys() if input.__dict__[k] is not None}

        input = cattr.structure(filtered, HistoryInput)

        self.member_history_usecase.create_history(user, input)

        return list(map(self.food_brief_mapper.from_model, query_set))