from django.urls import path
from ...views.member.food_plan_views import MemberFoodPlanView

member_get_food_plan_by_date = MemberFoodPlanView.as_view({
    'get': 'find_food_plan_by_date'
})

member_food_plan_create = MemberFoodPlanView.as_view({
    'post': 'create_new_food_plan'
})

member_food_plan_remove_edit = MemberFoodPlanView.as_view({
    'delete': 'remove_food_plan',
    'put': 'update_food_plan'
})

urlpatterns = [
    path('get-by-date/', member_get_food_plan_by_date),
    path('', member_food_plan_create),
    path('<int:plan_id>/', member_food_plan_remove_edit),
]
