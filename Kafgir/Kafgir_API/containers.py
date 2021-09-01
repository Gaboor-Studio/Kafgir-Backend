from dependency_injector import containers, providers

from .repositories_impl.shopping_list_repo import *
from .repositories_impl.user_repo import *
from .repositories_impl.food_planning_repo import *

from .usecases.member.shopping_list_usecases import *

from .services.member.shopping_list_services import *
from .services.member.food_planning_services import *
from .services.auth.authentication_services import *

from .mappers.shopping_list_mapper import *
from .mappers.food_plan_mapper import *

class Container(containers.DeclarativeContainer):
     
    # Repositories 

    shopping_list_repo = providers.Singleton(
        SoppingListRepositoryImpl
    )

    user_repo = providers.Singleton(
        UserRepositoryImpl
    )

    food_plan_repo = providers.Singleton(
        FoodPlanningRepositoryImpl
    )
    
    
    # Mappers

    shopping_list_output_mapper = providers.Singleton(
        ShoppingListItemOutputMapper
    )

    food_plan_output_mapper = providers.Singleton(
        FoodPlanOutputMapper
    )

    # Usecases

    member_shopping_list_usecase = providers.Singleton(
        MemberShoppingListService,
        user_repo = user_repo,
        shopping_list_repo = shopping_list_repo,
        shopping_list_output_mapper = shopping_list_output_mapper
    )

    member_food_plan_usecase = providers.Singleton(
        MemberFoodPlanService,
        food_plan_repo = food_plan_repo,
        food_plan_output_mapper = food_plan_output_mapper
    )

    authentication_usecase = providers.Singleton(
        AuthenticationService,
        user_repo = user_repo
    )


container = Container()
# container.init_resources()
