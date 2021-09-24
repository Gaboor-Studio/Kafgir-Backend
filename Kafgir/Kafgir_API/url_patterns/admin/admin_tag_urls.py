from django.urls import path
from ...views.admin.admin_tags_view import AdminTagView

admin_get_tags = AdminTagView.as_view({
    'get': 'get_tags'
})

admin_create_tag = AdminTagView.as_view({
    'post': 'create_new_tag'
})

member_tag_remove_edit = AdminTagView.as_view({
    'delete': 'remove_tag',
    'put': 'update_tag'
})

urlpatterns = [
    path('', admin_get_tags),
    path('', admin_create_tag),
    path('<int:tag_id>/', member_tag_remove_edit),
]
