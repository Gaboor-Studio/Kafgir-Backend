from django.urls import path

from ...views.member.member_history_view import MemberHistoryView

get_history = MemberHistoryView.as_view({
    'get': 'get_history',
    'delete': 'clear_history'
})

delete_single_history = MemberHistoryView.as_view({
    'delete': 'remove_history'
})

urlpatterns = [
    path('', get_history),
    path('<int:hid>/', delete_single_history)
]