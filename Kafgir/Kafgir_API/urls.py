from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .url_patterns.member.member_shopping_list_urls import urlpatterns as member_shopping_list_url_patterns
from .url_patterns.member.member_food_planning_urls import urlpatterns as member_food_planning_url_patterns
from .url_patterns.member.member_home_page_urls import urlpatterns as member_home_page_url_patterns
from .url_patterns.member.profile_urls import urlpatterns as profile_url_patterns
from .url_patterns.auth.authentication_urls import urlpatterns as auth_url_patterns
from .url_patterns.admin.admin_food_urls import urlpatterns as admin_food_url_patterns
from .url_patterns.member.member_food_urls import urlpatterns as member_food_url_patterns
from .url_patterns.admin.admin_tag_urls import urlpatterns as admin_tag_url_patterns
from .url_patterns.admin.admin_comment_urls import urlpatterns as admin_comment_url_patterns
from .url_patterns.member.member_ingredient_urls import urlpatterns as member_ingredient_url_patterns
from .url_patterns.member.search_urls import urlpatterns as member_search_url_patterns
from .url_patterns.admin.admin_management_urls import urlpatterns as admin_management_url_patterns
from .url_patterns.admin.user_management_urls import urlpatterns as user_management_url_patterns

urlpatterns = [
    path('auth/', include(auth_url_patterns)),

    path('member/shopping-list/', include(member_shopping_list_url_patterns)),

    path('member/food-planning/', include(member_food_planning_url_patterns)),

    path('member/home-page/', include(member_home_page_url_patterns)),

    path('member/food/', include(member_food_url_patterns)),

    path('member/ingredient/', include(member_ingredient_url_patterns)),

    path('admin/food/', include(admin_food_url_patterns)),

    path('admin/tag/', include(admin_tag_url_patterns)),

    path('member/profile/', include(profile_url_patterns)),

    path('member/search/', include(member_search_url_patterns)),
    
    path('admin/comment/', include(admin_comment_url_patterns)),

    path('admin/admin-management/', include(admin_management_url_patterns)),

    path('admin/admin-management/', include(admin_management_url_patterns)),

    path('admin/user-management/', include(user_management_url_patterns))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

