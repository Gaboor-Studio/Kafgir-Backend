from dependency_injector import containers, providers

from ..services.member.shopping_list_services import *
from ..services.auth.authentication_service import *
from ..services.auth.sha1_generate_token_service import *
from ..services.member.food_planning_services import *
from ..services.member.member_home_page_service import *

from .repo_container import RepoContainer
from .mapper_container import MapperContainer

class UsecaseContainer(containers.DeclarativeContainer):

    member_shopping_list_usecase = providers.Singleton(
        MemberShoppingListService,
        user_repo=RepoContainer.user_repo,
        shopping_list_repo=RepoContainer.shopping_list_repo,
        shopping_list_output_mapper=MapperContainer.shopping_list_output_mapper
    )

    authentication_usecase = providers.Singleton(
        AuthenticationService,
        user_repo=RepoContainer.user_repo
    )

    generate_token_usecase = providers.Singleton(
        SHA1GenerateTokenService,
    )
    
    member_food_plan_usecase = providers.Singleton(
        MemberFoodPlanService,
        food_plan_repo = RepoContainer.food_plan_repo,
        food_plan_output_mapper = MapperContainer.food_plan_output_mapper
    )

    member_home_page_usecase = providers.Singleton(
        MemberHomePageService,
        user_repo=RepoContainer.user_repo,
        tag_repo=RepoContainer.tag_repo,
        food_plan_repo=RepoContainer.food_plan_repo,
        food_plan_output_mapper=MapperContainer.food_plan_output_mapper,
        main_tag_mapper=MapperContainer.main_tag_mapper,
        tag_mapper=MapperContainer.tag_mapper,        
    )

container = UsecaseContainer()
# container.init_resources()
