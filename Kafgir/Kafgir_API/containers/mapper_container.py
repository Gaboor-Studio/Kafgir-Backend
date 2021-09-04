from dependency_injector import containers, providers

from ..mappers.shopping_list_mapper import *
from ..mappers.food_plan_mapper import *

class MapperContainer(containers.DeclarativeContainer):
     
    shopping_list_output_mapper = providers.Singleton(
        ShoppingListItemOutputMapper
    )

    food_plan_output_mapper = providers.Singleton(
        FoodPlanOutputMapper
    )

container = MapperContainer()
# container.init_resources()
