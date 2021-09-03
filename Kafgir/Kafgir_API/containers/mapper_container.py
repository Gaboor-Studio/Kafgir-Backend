from dependency_injector import containers, providers

from ..mappers.shopping_list_mapper import *

class MapperContainer(containers.DeclarativeContainer):
     
    shopping_list_output_mapper = providers.Singleton(
        ShoppingListItemOutputMapper
    )

container = MapperContainer()
# container.init_resources()
