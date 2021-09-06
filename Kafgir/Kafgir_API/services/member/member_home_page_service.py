from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.tag import Tag
from ...models.user import User

from ...usecases.member.member_home_page import MemberHomePageUsecase
from ...dto.tag_dto import MainTagOutput
from ...repositories.tag_repo import TagRepository
from ...mappers.tag_mapper import MainTagMapper

from typing import List

class MemberHomePageService(MemberHomePageUsecase):

    @inject
    def __init__(self, tag_repo: TagRepository = Provide['tag_repo'],
                       user_repo: UserRepository = Provide['user_repo'],
                       main_tag_mapper: MainTagMapper = Provide['main_tag_mapper']):

        self.tag_repo = tag_repo
        self.user_repo = user_repo
        self.main_tag_mapper = main_tag_mapper

    
    def get_some_food_by_tag_id(self, num: int) -> List[MainTagOutput]:
        tags = self.tag_repo.find_main_tag()
        output = []
        for tag in tags:
            foods = self.tag_repo.get_some_food_by_tag_id(id=tag.pk, num=num)
            main_tag_output = self.main_tag_mapper(model=tag, foods=foods)
            output.append(main_tag_output)
        return output
        