from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.comment import Comment
from ...models.food import Food
from ...models.user import User

from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...dto.comment_dto import CommentOutput,CommentInput,CommentBriefInput
from ...repositories.comment_repo import CommentRepository
from ...repositories.food_repo import FoodRepository
from ...mappers.comment_mapper import CommentMapper
from ...exceptions.not_found import CommentNotFoundException,FoodNotFoundException

from typing import List

class MemberCommentService(MemberCommentUsecase):

    @inject
    def __init__(self, comment_repo: CommentRepository = Provide['comment_repo'],
                       food_repo: FoodRepository = Provide['food_repo'],
                       user_repo: UserRepository = Provide['user_repo'],
                       commment_mapper: CommentMapper = Provide['commment_mapper']):

        self.comment_repo = comment_repo
        self.user_repo = user_repo
        self.food_repo = food_repo
        self.commment_mapper = commment_mapper

    def get_some_food_comments(self, food_id: int, num: int) -> List[CommentOutput]:
        try:
            food = self.food_repo.find_by_id(food_id)
            return list(map(self.commment_mapper.from_model, self.comment_repo.get_some_food_comments(num=num, food=food)))
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!')

    def get_food_comments(self, food_id: int) -> List[CommentOutput]:
        try:
            food = self.food_repo.find_by_id(food_id)
            return list(map(self.commment_mapper.from_model, self.comment_repo.get_food_comments(food=food)))
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!') 

    def find_comment_by_user_id(self, id: int, food_id: int) -> CommentOutput:
        try:
            food = self.food_repo.find_by_id(food_id)
            return map(self.commment_mapper.from_model, self.comment_repo.find_comment_by_user_id(food=food, id=id))
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!')

    def add_comment(self, input:  CommentInput, user: User) -> None:
        try:
            food = self.food_repo.find_by_id(input.food)
            if not self.comment_repo.are_there_any_user_comment(id=user.pk, food=input.food):
                comment = Comment(food=food,user=user,confirmed=False,text=input.text,rating=input.rating)
                comment.save()
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={input.food}) not found!')

    def update_comment(self, comment_id: int, input:  CommentBriefInput) -> None:
        try:
            comment = self.comment_repo.find_by_id(comment_id)
            
            comment.rating = input.rating
            comment.text = input.text           
            comment.confirmed = False

            comment.save()
        
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')


    def remove_comment(self, comment_id: int) -> None:
        self.comment_repo.delete_by_id(comment_id)
