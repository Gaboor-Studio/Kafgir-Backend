from dependency_injector.wiring import Provide, inject
from typing import List

from ...dto.food_dto import FoodBriefOutput
from ...models.food import Food
from ...usecases.member.search_usecases import SearchUsecase
from ...mappers.food_mapper import FoodBriefMapper
from ...exceptions.bad_request import SearchFieldMissing
from ...exceptions.common import CannotParseToInt


class SearchService(SearchUsecase):
    ''' This class contains all different ways to do a search for any entity in database'''


    @inject
    def __init__(self, food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper']) -> None:
        super().__init__()
        self.food_brief_mapper = food_brief_mapper

    def search_for_food(self, title: str, category: int, ingredients: List[str], level: int, cooking_time: int) -> List[FoodBriefOutput]:
        ''' Search for a group of specific foods using their names, category, ingredients, level and cooking time'''

        query_set = Food.objects
        
        ''' title is the only required field '''
        if title is None:
            raise SearchFieldMissing(detail="food title you're looking for is being missed")
        else :
            query_set = query_set.filter(title__icontains=title)\

        ''' rest of attributes are not required so we apply filters if and only if they exist '''
        if level is not None:
            try:
                temp_level = int(level)
                query_set = query_set.filter(level=temp_level)
            except ValueError:
                raise CannotParseToInt(detail='level needs to be an integer')

        if cooking_time is not None:
            try:
                temp_time = int(cooking_time)
                query_set = query_set.filter(cooking_time__range=(temp_time-15, temp_time+15))
            except ValueError:
                raise CannotParseToInt(detail='cooking time needs to be an integer')

        if category is not None:
            query_set = query_set.filter(tags__id=category, tags__is_primary=True)

        if ingredients is not None:
            for ing in ingredients:
                query_set = query_set.filter(ingredient_pieces__ingredient__name=ing)

        return list(map(self.food_brief_mapper.from_model, query_set))