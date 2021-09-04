from django.urls import path
from ...views.auth.authentication_views import LoginApiView,register_view, AuthenticationView

send_email = AuthenticationView.as_view({
    'post': 'send_email'
})

verify_email = AuthenticationView.as_view({
    'post': 'verify_email'
})

get_reset_token = AuthenticationView.as_view({
    'post': 'get_reset_token'
})

reset_password = AuthenticationView.as_view({
    'post': 'reset_password'
})

urlpatterns = [
    path('register/', register_view),
    path('login/', LoginApiView.as_view()),
    path('send-confirmation/', send_email),
    path('confirm-email/', verify_email),
    path('get-reset-token/', get_reset_token),
    path('reset-password/', reset_password)
]
