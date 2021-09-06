from django.urls import path
from ...views.member.member_food_view import MemberFoodView

with_id = MemberFoodView.as_view({
    'get': 'get_one_food'
})

add_ingredients = MemberFoodView.as_view({
    'post': 'add_ingredients_to_list'
})
urlpatterns = [
    path('<int:food_id>/', with_id),
    path('<int:food_id>/add-to-shopping-list',add_ingredients)
]
