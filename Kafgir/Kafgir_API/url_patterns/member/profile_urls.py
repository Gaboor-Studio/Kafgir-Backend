from django.urls import path

from ...views.member.profile_view import ProfileView

get_profile = ProfileView.as_view({
    'get': 'get_profile'
})

set_password = ProfileView.as_view({
    'post': 'change_password'
})

picture = ProfileView.as_view({
    'post': 'set_picture',
    'delete': 'delete_picture'
})

edit_profile = ProfileView.as_view({
    'put': 'edit_profile'
})

log_out = ProfileView.as_view({
    'get': 'log_out'
})

urlpatterns = [
    path('', get_profile),
    path('set-password/', set_password),
    path('picture/', picture),
    path('edit-profile/', edit_profile),
    path('log-out/', log_out)
]