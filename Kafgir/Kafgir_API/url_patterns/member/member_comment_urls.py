from django.urls import path
from ...views.member.member_comment_view import MemberCommentView

member_comment_remove_edit = MemberCommentView.as_view({
    'delete': 'remove_comment',
    'put': 'update_comment'
})


urlpatterns = [
    path('<int:comment_id>/', member_comment_remove_edit)
]
