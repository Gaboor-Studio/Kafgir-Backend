from django.urls import path
from ...views.member.member_food_view import MemberFoodView

with_id = MemberFoodView.as_view({
    'get': 'get_one_food'
})

add_ingredients = MemberFoodView.as_view({
    'post': 'add_ingredients_to_list'
})

comments = MemberFoodView.as_view({
    'get': 'get_food_comments',
    'post': 'create_new_comment'
})

with_nothing = MemberFoodView.as_view({
    'get': 'get_all_foods_with_tag'
})

favorite_foods = MemberFoodView.as_view({
    'get': 'get_favorite_foods'
})

add_to_favorite = MemberFoodView.as_view({
    'post': 'add_favorite_food'
})

urlpatterns = [
    path('<int:food_id>/comments/', comments),
    path('', with_nothing),
    path('<int:food_id>/', with_id),
    path('get-favorites/', favorite_foods),
    path('<int:food_id>/add-to-favorite/', add_to_favorite),
    path('<int:food_id>/add-to-shopping-list/',add_ingredients)
]
