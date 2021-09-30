from django.urls import path
from ...views.admin.admin_tags_view import AdminTagView

admin_get_post_tags = AdminTagView.as_view({
    'get': 'get_tags',
    'post': 'create_new_tag'
})

member_tag_remove_edit = AdminTagView.as_view({
    'delete': 'remove_tag',
    'put': 'update_tag'
})

set_tp = AdminTagView.as_view({
    'post': 'set_tag_picture'
})

urlpatterns = [
    path('', admin_get_post_tags),
    path('<int:tag_id>/', member_tag_remove_edit),
    path('<int:tag_id>/set-picture/', set_tp)
]
