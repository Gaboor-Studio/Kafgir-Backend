from ..repositories.comment_repo import CommentRepository

from ..models.comment import Comment
from ..models.food import Food

from typing import List
from django.db.models import Q

class CommentRepositoryImpl(CommentRepository):
    
    def get_some_food_comments(self, food: Food, num: int) -> List[Comment]:
        comments = Comment.objects.filter(Q(food=food) , Q(allowed=True) , ~Q(text=''))
        comment_count = comments.count()
        if(comment_count>=num) :
            return list(comments.order_by('date_time')[-1*num:])
        return list(comments.all().order_by('-date_time'))

    def get_food_comments(self, food: Food) -> List[Comment]:
        return list (Comment.objects.filter(Q(food=food) , Q(allowed=True) , ~Q(text='')))

    def find_comment_by_user_id(self, id: int, food: Food) -> Comment:
        return Comment.objects.get(user=id,food=food)

    def are_there_any_user_comment(self, id: int, food: Food) -> bool:
        return Comment.objects.filter(user=id,food=food).exists()

    def get_not_confirmed_comments(self) -> List[Comment]:
        return list (Comment.objects.filter(allowed=False))

    def find_by_id(self, id: int) -> Comment:
        return Comment.objects.get(pk=id)

    def save(self, comment: Comment) -> None:
        comment.save()

    def delete_by_id(self, id: int) -> None:
        Comment.objects.filter(id=id).delete()