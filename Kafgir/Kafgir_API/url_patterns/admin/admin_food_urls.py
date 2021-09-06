from django.urls import path
from ...views.admin.admin_food_view import AdminFoodView

root = AdminFoodView.as_view({
    'get': 'get_all_food',
    'post': 'create_food'
})

with_id = AdminFoodView.as_view({
    'get': 'get_one_food',
    'delete': 'delete_food'
})

urlpatterns = [
    path('', root),
    path('<int:food_id>/',with_id)
]