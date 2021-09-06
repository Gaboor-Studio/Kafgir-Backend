from django.urls import path
from ...views.member.home_page_view import MemberHomePageView

load_home_page = MemberHomePageView.as_view({
    'get': 'load_home_page'
})

urlpatterns = [
    path('', load_home_page)
]
