from django.urls import path
from ...views.member.member_comment_views import MemberCommentView

member_get_some_food_comments = MemberCommentView.as_view({
    'get': 'get_some_food_comments'
})

member_get_food_comments = MemberCommentView.as_view({
    'get': 'get_food_comments'
})

member_get_my_comment = MemberCommentView.as_view({
    'get': 'get_comment_by_user_id'
})

member_create_new_comment = MemberCommentView.as_view({
    'post': 'create_new_comment'
})

member_comment_remove_edit = MemberCommentView.as_view({
    'delete': 'remove_comment',
    'put': 'update_comment'
})

urlpatterns = [
    path('get-some-comments/<int:num>/food/<int:food_id>/', member_get_some_food_comments),
    path('food/<int:food_id>/', member_get_food_comments),
    path('my-comment/food/<int:food_id>/', member_get_my_comment),
    path('', member_create_new_comment),
    path('<int:comment_id>/', member_comment_remove_edit),
]
