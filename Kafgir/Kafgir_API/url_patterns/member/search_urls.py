from django.urls import path

from ...views.member.search_view import SearchView

search_for_food = SearchView.as_view({
    'get': 'search_for_food'
})

urlpatterns = [
    path('', search_for_food)
]