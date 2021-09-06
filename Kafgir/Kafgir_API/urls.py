from django.urls import path, include

from .views.auth.authentication_views import register_view, LoginApiView

from .url_patterns.member.member_shopping_list_urls import urlpatterns as member_shopping_list_url_patterns
from .url_patterns.member.member_food_planning_urls import urlpatterns as member_food_planning_url_patterns
from .url_patterns.member.member_home_page_urls import urlpatterns as member_home_page_url_patterns
from .url_patterns.auth.authentication_urls import urlpatterns as auth_url_patterns

urlpatterns = [
    path('auth/', include(auth_url_patterns)),

    path('member/shopping-list/', include(member_shopping_list_url_patterns)),

    path('member/food-planning/', include(member_food_planning_url_patterns)),

    path('member/home-page/', include(member_home_page_url_patterns))
]

