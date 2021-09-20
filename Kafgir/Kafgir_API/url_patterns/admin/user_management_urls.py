from django.urls import path

from ...views.admin.user_management_view import UserManagementView

root = UserManagementView.as_view({
    'get': 'get_users',
    'post': 'create_user'
})

change_user = UserManagementView.as_view({
    'put': 'edit_user',
    'delete': 'delete_user'
})

set_password = UserManagementView.as_view({
    'post': 'set_user_password'
})

set_pfp = UserManagementView.as_view({
    'post': 'set_user_picture'
})

urlpatterns = [
    path('', root),
    path('<int:id>/', change_user),
    path('<int:id>/set-password/', set_password),
    path('<int:id>/set-picture/', set_pfp)
]