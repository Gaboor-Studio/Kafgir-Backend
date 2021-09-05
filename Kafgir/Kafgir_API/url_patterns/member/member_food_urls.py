from django.urls import path
from ...views.member.member_food_view import MemberFoodView

with_id = MemberFoodView.as_view({
    'get': 'get_one_food'
})

urlpatterns = [
    path('<int:food_id>/', with_id)
]
