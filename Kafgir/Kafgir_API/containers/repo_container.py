from dependency_injector import containers, providers

from ..repositories_impl.shopping_list_repo import *
from ..repositories_impl.user_repo import *
from ..repositories_impl.food_planning_repo import *
from ..repositories_impl.food_repo_impl import *
from ..repositories_impl.ingredient_repo_impl import *
from ..repositories_impl.ingredient_piece_repo_impl import *
from ..repositories_impl.recipe_item_repo_impl import *
from ..repositories_impl.tag_repo import *

class RepoContainer(containers.DeclarativeContainer):
     
    # Repositories 

    shopping_list_repo = providers.Singleton(
        ShoppingListRepositoryImpl
    )

    user_repo = providers.Singleton(
        UserRepositoryImpl
    )

    food_plan_repo = providers.Singleton(
        FoodPlanningRepositoryImpl
    )

    food_repo = providers.Singleton(
        FoodRepositoryImpl
    )

    ingredient_repo = providers.Singleton(
        IngredientRepositoryImpl
    )

    ingredient_piece_repo = providers.Singleton(
        IngredientPieceRepositoryImpl
    )

    reciple_item_repo = providers.Singleton(
        RecipeItemRepositoryImpl
    )

    tag_repo = providers.Singleton(
        TagRepositoryImpl
    )


container = RepoContainer()
# container.init_resources()
