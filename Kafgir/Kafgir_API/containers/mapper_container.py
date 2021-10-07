from dependency_injector import containers, providers

from ..mappers.shopping_list_mapper import *
from ..mappers.food_plan_mapper import *
from ..mappers.food_mappers import *
from ..mappers.ingredient_piece_mappers import *
from ..mappers.ingredient_mappers import *
from ..mappers.recipe_item_mappers import *
from ..mappers.tag_mapper import *
from ..mappers.profile_mapper import *
from ..mappers.comment_mapper import *
from ..mappers.admin_management_mapper import *
from ..mappers.user_management_mapper import *
from ..mappers.history_mappers import *

class MapperContainer(containers.DeclarativeContainer):
     
    shopping_list_output_mapper = providers.Singleton(
        ShoppingListItemOutputMapper
    )

    food_plan_output_mapper = providers.Singleton(
        FoodPlanOutputMapper
    )

    ingredient_piece_mapper = providers.Singleton(
        IngredientPieceMapper
    )

    recipe_item_mapper = providers.Singleton(
        RecipeItemMapper
    )

    food_mapper = providers.Singleton(
        FoodMapper,
        ingredient_piece_mapper=ingredient_piece_mapper,
        recipe_item_mapper=recipe_item_mapper
    )

    food_brief_mapper = providers.Singleton(
        FoodBriefMapper
    )

    food_in_food_plan_mapper = providers.Singleton(
        FoodInFoodPlanMapper
    )

    admin_food_details_mapper = providers.Singleton(
        AdminFoodDetailsMapper,
        ingredient_piece_mapper=ingredient_piece_mapper,
        recipe_item_mapper=recipe_item_mapper
    )

    tag_mapper = providers.Singleton(
        TagMapper
    )

    main_tag_mapper = providers.Singleton(
        MainTagMapper
    )

    profile_output_mapper = providers.Singleton(
        ProfileOutputMapper
    )

    primary_tag_mapper = providers.Singleton(
        PrimaryTagMapper
    )
    
    ingredient_mapper = providers.Singleton(
        IngredientMapper
    )

    comment_mapper = providers.Singleton(
        CommentMapper
    )

    comment_brief_mapper = providers.Singleton(
        CommentBriefMapper
    )

    my_comment_mapper = providers.Singleton(
        MyCommentMapper
    )

    admin_brief_mapper = providers.Singleton(
        AdminBriefMapper
    )

    admin_mapper = providers.Singleton(
        AdminMapper
    )

    user_management_profile_mapper = providers.Singleton(
        UserManagementProfileMapper
    )

    history_mapper = providers.Singleton(
        HistoryMapper,
        primary_tag_mapper= primary_tag_mapper
    )
    

container = MapperContainer()
# container.init_resources()
