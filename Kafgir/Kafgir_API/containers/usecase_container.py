from dependency_injector import containers, providers

from ..services.member.shopping_list_services import *
from ..services.auth.authentication_services import *
from ..services.auth.token_generator_service import *

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

    token_generator_usecase = providers.Singleton(
        TokenGeneratorService,
        user_repo= RepoContainer.user_repo
    )


container = UsecaseContainer()
# container.init_resources()
