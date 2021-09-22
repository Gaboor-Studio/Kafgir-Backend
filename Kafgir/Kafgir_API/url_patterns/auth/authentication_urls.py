from django.urls import path
from ...views.auth.authentication_views import AuthenticationView
from rest_framework_simplejwt import views as jwt_views

register = AuthenticationView.as_view({
    'post': 'register_view'
})

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
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register),
    path('send-confirmation/', send_email),
    path('confirm-email/', verify_email),
    path('get-reset-token/', get_reset_token),
    path('reset-password/', reset_password)
]
