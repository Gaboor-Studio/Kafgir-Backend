from django.urls import path
from ...views.admin.admin_comment_view import AdminCommentView

admin_get_some_food_comments = AdminCommentView.as_view({
    'get': 'get_some_food_comments'
})

admin_get_food_comments = AdminCommentView.as_view({
    'get': 'get_food_comments'
})

admin_confirm_the_comment = AdminCommentView.as_view({
    'put': 'confirm_the_comment'
})

admin_confirm_comments = AdminCommentView.as_view({
    'put': 'confirm_comments'
})

admin_get_some_unconfirmed_comments = AdminCommentView.as_view({
    'get': 'get_some_unconfirmed_comments'
})

admin_comment_remove_edit = AdminCommentView.as_view({
    'delete': 'remove_comment',
    'put': 'update_comment'
})

urlpatterns = [
    path('get-some-comments/<int:num>/food/<int:food_id>/', admin_get_some_food_comments),
    path('food/<int:food_id>/', admin_get_food_comments),
    path('<int:comment_id>/', admin_comment_remove_edit),
    path('confirm/<int:comment_id>/', admin_confirm_the_comment),
    path('confirm/', admin_confirm_comments),
    path('get-some-unconfirmed-comments/<int:num>/', admin_get_some_unconfirmed_comments),
]
