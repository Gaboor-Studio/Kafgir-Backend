from django.urls import path
from ...views.member.shopping_list_views import MemberShoppingListView

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
    path('', member_shopping_list_create_get),
    path('item/', member_shopping_list_item_create),
    path('item/<int:item_id>/',
         member_shopping_list_item_edit_remove),
    path('item/done/<int:item_id>/',
         member_shopping_list_item_done),
    path('item/undone/<int:item_id>/',
         member_shopping_list_item_undone),
]
