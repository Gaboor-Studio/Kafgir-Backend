from django.urls import path

from ...views.member.member_history_view import MemberHistoryView

get_history = MemberHistoryView.as_view({
    'GET': 'get_history'
})

delete_single_history = MemberHistoryView.as_view({
    'DELETE': 'remove_history'
})

urlpatterns = [
    path('', get_history),
    path('<int:uid>/', delete_single_history)
]