from django.urls import path
from ...views.auth.authentication_views import LoginApiView,register_view, AuthenticationView

send_email = AuthenticationView.as_view({
    'post': 'send_email'
})

verify_email = AuthenticationView.as_view({
    'post': 'verify_email'
})

urlpatterns = [
    path('register/', register_view),
    path('login/', LoginApiView.as_view()),
    path('send-confirmation/', send_email),
    path('confirm-email/', verify_email)
]
