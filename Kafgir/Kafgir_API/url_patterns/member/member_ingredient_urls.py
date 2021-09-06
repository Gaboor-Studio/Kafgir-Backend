from django.urls import path
from ...views.member.member_ingredient_view import MemberIngredientView

member_ingredinet_list = MemberIngredientView.as_view({
    'get': 'get_ingredient_list',
})


urlpatterns = [
    path('', member_ingredinet_list)
]
