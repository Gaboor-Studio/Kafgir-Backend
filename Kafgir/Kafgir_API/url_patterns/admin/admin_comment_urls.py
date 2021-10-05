from django.urls import path
from ...views.admin.admin_comment_view import AdminCommentView

admin_confirm_the_comment = AdminCommentView.as_view({
    'put': 'confirm_the_comment'
})

admin_confirm_comments = AdminCommentView.as_view({
    'put': 'confirm_comments'
})

root = AdminCommentView.as_view({
    'get': 'get_comments'
})

admin_comment_remove_edit = AdminCommentView.as_view({
    'delete': 'remove_comment',
    'put': 'update_comment'
})

urlpatterns = [
    path('<int:comment_id>/', admin_comment_remove_edit),
    path('confirm/<int:comment_id>/', admin_confirm_the_comment),
    path('confirm/', admin_confirm_comments),
    path('', root),
]
