from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.comment import Comment
from ...models.food import Food

from ...usecases.admin.admin_comment_usecases import AdminCommentUsecase
from ...dto.comment_dto import CommentOutput,CommentInput,CommentBriefInput,CommentIdListInput
from ...repositories.comment_repo import CommentRepository
from ...repositories.food_repo import FoodRepository
from ...mappers.comment_mapper import CommentMapper
from ...exceptions.not_found import CommentNotFoundException,FoodNotFoundException

from typing import List

class AdminCommentService(AdminCommentUsecase):
    ''' This class is an abstract class for usecases of admin_comment api '''

    @inject
    def __init__(self, comment_repo: CommentRepository = Provide['comment_repo'],
                       food_repo: FoodRepository = Provide['food_repo'],
                       comment_mapper: CommentMapper = Provide['comment_mapper']):

        self.comment_repo = comment_repo
        self.food_repo = food_repo
        self.comment_mapper = comment_mapper


    def get_some_unconfirmed_comments(self, num: int) -> List[CommentOutput]:
        ''' This method returns a list of all unconfirmed comments .'''

        return list(map(self.comment_mapper.from_model, self.comment_repo.get_some_unconfirmed_comments(num=num)))
 
    def confirm_the_comment(self, comment_id: int) -> None:
        '''This method receives a comment ID to confirm user comment .'''

        try:
            comment = self.comment_repo.find_by_id(comment_id)
                   
            comment.confirmed = True

            comment.save()
        
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')
 
    def confirm_comments(self, comments: CommentIdListInput) -> None:
        '''This method receives a list of comment IDs for confirming user comments .'''

        for comment_id in comments.commentid_list:
            try:
                comment = self.comment_repo.find_by_id(comment_id)
                    
                comment.confirmed = True

                comment.save()
            
            except Comment.DoesNotExist:
                raise CommentNotFoundException(
                    detail=f'comment with comment_id={comment_id} does not exist!')


    def update_comment(self, comment_id: int, input:  CommentBriefInput) -> None:
        '''updates a comment .'''

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
        ''' deletes a comment by ID.'''

        self.comment_repo.delete_by_id(comment_id)
