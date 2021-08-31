from django.urls import path, include

from .views.member.shopping_list_views import MemberShoppingListView
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

urlpatterns = [
    path('auth/register/', register_view),
    path('auth/login/', LoginApiView.as_view()),
    path('member/shopping-list/', member_shopping_list_create_get),
    path('member/shopping-list-item/', member_shopping_list_item_create),
    path('member/shopping-list-item/<int:item_id>/', member_shopping_list_item_edit_remove),
    path('member/shopping-list-item/done/<int:item_id>/', member_shopping_list_item_done),
    path('member/shopping-list-item/undone/<int:item_id>/', member_shopping_list_item_undone),
]

