from django.urls import path
from ...views.auth.authentication_views import LoginApiView,register_view

urlpatterns = [
    path('register/', register_view),
    path('login/', LoginApiView.as_view()),
]
