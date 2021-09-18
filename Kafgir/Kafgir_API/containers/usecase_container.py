from dependency_injector import containers, providers

from ..services.member.shopping_list_services import *
from ..services.auth.authentication_service import *
from ..services.auth.sha1_generate_token_service import *
from ..services.member.food_planning_services import *
from ..services.member.member_home_page_service import *
from ..services.member.member_ingredient_services import *
from ..services.member.member_food_services import MemberFoodService
from ..services.admin.admin_food_service import AdminFoodService
from ..services.admin.admin_tag_service import AdminTagServices
from ..services.member.profile_service import *
from ..services.admin.admin_management_service import AdminManagementService


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
        food_plan_output_mapper = MapperContainer.food_plan_output_mapper,
        food_repo = RepoContainer.food_repo
    )

    member_home_page_usecase = providers.Singleton(
        MemberHomePageService,
        user_repo=RepoContainer.user_repo,
        tag_repo=RepoContainer.tag_repo,
        food_plan_repo=RepoContainer.food_plan_repo,
        food_plan_output_mapper=MapperContainer.food_plan_output_mapper,
        main_tag_mapper=MapperContainer.main_tag_mapper,
        tag_mapper=MapperContainer.tag_mapper, 
        primary_tag_mapper= MapperContainer.primary_tag_mapper      
    )

    member_food_usecase = providers.Singleton(
        MemberFoodService,
        food_repo = RepoContainer.food_repo,
        food_mapper = MapperContainer.food_mapper
    )

    admin_food_usecase = providers.Singleton(
        AdminFoodService,
        food_repo = RepoContainer.food_repo,
        food_mapper= MapperContainer.food_mapper,
        food_brief_mapper = MapperContainer.food_brief_mapper,
        ingredient_repo= RepoContainer.ingredient_repo,
        ingredient_piece_repo=RepoContainer.ingredient_piece_repo,
        recipe_item_repo=RepoContainer.reciple_item_repo
    )
    
    profile_usecase = providers.Singleton(
        ProfileService,
        user_repo = RepoContainer.user_repo,
        profile_output_mapper = MapperContainer.profile_output_mapper
    )

    admin_tag_usecase = providers.Singleton(
        AdminTagServices,
        tag_repo = RepoContainer.tag_repo,
        tag_mapper= MapperContainer.tag_mapper
    )

    member_ingredient_usecase = providers.Singleton(
        MemberIngredientService,
        ingredient_repo = RepoContainer.ingredient_repo,
        ingredient_mapper= MapperContainer.ingredient_mapper
    )

    admin_management_usecase = providers.Singleton(
        AdminManagementService,
        user_repo = RepoContainer.user_repo,
        admin_mapper = MapperContainer.admin_mapper,
        admin_brief_mapper = MapperContainer.admin_brief_mapper 
    )

container = UsecaseContainer()
# container.init_resources()
