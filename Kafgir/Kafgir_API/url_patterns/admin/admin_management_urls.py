from django.urls import path
from ...views.admin.admin_management_view import AdminManagementView

root = AdminManagementView.as_view({
    'get': 'get_all_admins',
    'post': 'create_admin'
})

with_id = AdminManagementView.as_view({
    'delete': 'delete_admin',
    'get': 'get_admin',
    'put': 'update_admin'
})

set_password = AdminManagementView.as_view({
    'put': 'update_admin_passsword'
})

urlpatterns = [
    path('', root),
    path('<int:admin_id>/', with_id),
    path('<int:admin_id>/set-password', set_password)
]
