from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.tag import Tag
from ...models.user import User

from ...usecases.member.member_home_page import MemberHomePageUsecase
from ...dto.tag_dto import MainTagOutput, TagOutput
from ...dto.food_plan_dto import FoodPlanOutput
from ...dto.home_page_dto import HomePageOutput
from ...repositories.tag_repo import TagRepository
from ...repositories.food_planning_repo import FoodPlanningRepository
from ...mappers.food_plan_mapper import FoodPlanOutputMapper
from ...mappers.tag_mapper import MainTagMapper, TagMapper

from typing import List
from datetime import date,timedelta

class MemberHomePageService(MemberHomePageUsecase):

    @inject
    def __init__(self, tag_repo: TagRepository = Provide['tag_repo'],
                       user_repo: UserRepository = Provide['user_repo'],
                       main_tag_mapper: MainTagMapper = Provide['main_tag_mapper'],
                       food_plan_repo: FoodPlanningRepository = Provide['food_plan_repo'],
                       food_plan_output_mapper: FoodPlanOutputMapper = Provide['food_plan_output_mapper'],
                       tag_mapper: TagMapper = Provide['tag_mapper']):

        self.tag_repo = tag_repo
        self.user_repo = user_repo
        self.food_plan_repo = food_plan_repo
        self.food_plan_output_mapper = food_plan_output_mapper
        self.main_tag_mapper = main_tag_mapper
        self.tag_mapper = tag_mapper

    
    def get_some_food_by_tag_id(self, num: int) -> List[MainTagOutput]:
        tags = self.tag_repo.find_main_tag()
        output = []
        for tag in tags:
            foods = self.tag_repo.get_some_food_by_tag_id(id=tag.pk, num=num)
            main_tag_output = self.main_tag_mapper(model=tag, foods=foods)
            output.append(main_tag_output)
        return output
    
    def get_food_plan(self, id: int) -> List[FoodPlanOutput]:
        end = date.today() + timedelta(days=1)
        start = date.today() - timedelta(days=1)
        food_plan = self.food_plan_repo.find_food_plan_by_date(id=id,start_date=start,end_date=end)
        return list(map(self.food_plan_output_mapper.from_model, food_plan))

    def get_categories(self) -> List[TagOutput]:
        return list(map(self.tag_mapper.from_model, self.tag_repo.find_primary_tag()))

    def load_home_page_for_user(self, id: int, num: int) -> HomePageOutput:
        main_tags = self.get_some_food_by_tag_id(num)
        food_plan = self.get_food_plan(id)
        categories = self.get_categories()
        return HomePageOutput(food_plan=food_plan, main_tags=main_tags, categories=categories)

    def load_home_page_for_guest(self, num: int) -> HomePageOutput:
        main_tags = self.get_some_food_by_tag_id(num)
        categories = self.get_categories()
        return HomePageOutput(food_plan=None, main_tags=main_tags, categories=categories)




    