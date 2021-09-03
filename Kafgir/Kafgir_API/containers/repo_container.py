from dependency_injector import containers, providers

from ..repositories_impl.shopping_list_repo import *
from ..repositories_impl.user_repo import *

class RepoContainer(containers.DeclarativeContainer):
     
    # Repositories 

    shopping_list_repo = providers.Singleton(
        SoppingListRepositoryImpl
    )

    user_repo = providers.Singleton(
        UserRepositoryImpl
    )


container = RepoContainer()
# container.init_resources()
