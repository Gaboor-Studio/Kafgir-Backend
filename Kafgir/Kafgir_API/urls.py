from django.urls import path, include

from .views.member.shopping_list_views import MemberShoppingListView
from .views.member.food_plan_views import MemberFoodPlanView
from .views.auth.authentication_views import register_view, LoginApiView

member_shopping_list_create_get = MemberShoppingListView.as_view({
    'get': 'get_shopping_list',
    'post': 'create_new_shopping_list'
})

member_shopping_list_item_create = MemberShoppingListView.as_view({
    'post': 'create_new_shopping_list_item'
})

member_shopping_list_item_edit_remove = MemberShoppingListView.as_view({
    'put': 'update_shopping_list_item',
    'delete': 'remove_shopping_list_item'
})

member_shopping_list_item_done = MemberShoppingListView.as_view({
    'put': 'done'
})

member_shopping_list_item_undone = MemberShoppingListView.as_view({
    'put': 'undone'
})

member_get_food_plan_by_date = MemberFoodPlanView.as_view({
    'get': 'find_food_plan_by_date'
})

member_food_plan_create = MemberFoodPlanView.as_view({
    'post': 'create_new_food_plan'
})

member_food_plan_remove = MemberFoodPlanView.as_view({
    'delete': 'remove_food_plan'
})


urlpatterns = [
    path('auth/register/', register_view),
    path('auth/login/', LoginApiView.as_view()),
    path('member/shopping-list/', member_shopping_list_create_get),
    path('member/shopping-list-item/', member_shopping_list_item_create),
    path('member/shopping-list-item/<int:item_id>/', member_shopping_list_item_edit_remove),
    path('member/shopping-list-item/done/<int:item_id>/', member_shopping_list_item_done),
    path('member/shopping-list-item/undone/<int:item_id>/', member_shopping_list_item_undone),
    path('member/food-planning/<str:start_date>/<str:end_date>/', member_get_food_plan_by_date),
    path('member/food-planning/', member_food_plan_create),
    path('member/food-planning/<int:plan_id>/', member_food_plan_remove),
]

